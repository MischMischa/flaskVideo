#@author Michael Kress
#Copyright (c) 2018 Michael Kress
from time import sleep
from flask import Flask, render_template, Response, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from moviepy.editor import *
import random
from datetime import datetime
from time import mktime
import sys
import os

app = Flask(__name__)
Bootstrap(app)
mongo = PyMongo(app)
static_img = "static/img/"
static_video = "static/video/"
jpg = ".jpg"
mp4 = ".mp4"

app.config['UPLOAD_FOLDER'] = static_img

class Controller:
    def __init__(self):
        self.mongo = MongoDb()

    #startseite zum hochladen von dateien
    def upload(self):
        if request.method == 'POST':
            file = request.files['file']
            if file:
                date = self.mongo.date.get_current_unix_time()
                print('date '+date)
                self.mongo.insert_image(date)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],date+jpg))
                Video().make_video()
        return render_template('upload.html')

    #funktionen zum auslesen von bilddateipfaden und rendern von templates
    def gallery(self):
        images = []
        for document in self.mongo.read_images():
            images.append(str(document["Image"]))
        return render_template('gallery.html', images=images)

    #funktionen zum auslesen von video dateipfaden und rendern von templates
    def gallery_video(self):
        videos = []
        for document in self.mongo.read_videos():
            videos.append(str(document["Movie"]))
        print("videos "+str(videos))
        return render_template('gallery_video.html', videos=videos)
#video class zum generieren von videos direkt nach dem upload
class Video:
    def __init__(self):
        self.mongo = MongoDb()

    def make_video(self):
        image_list = []
        date = self.mongo.date.get_current_unix_time()
        movie_name = static_video+date+mp4
        for document in self.mongo.read_images_casual():
            image_list.append(str(document["Image"]))
        print(image_list[1:-1])
        movie = [ImageClip(m).set_duration(2)
                 for m in image_list]
        make_movie = concatenate_videoclips(movie, method="compose")
        write_movie = make_movie.write_videofile(movie_name, fps=2)
        self.mongo.insert_movie(movie_name)
# ist für die weiterleitung von pfaden gedacht
class Rules:
    def __init__(self, app, controller):
        app.add_url_rule('/', 'home', lambda: controller.upload())
        app.add_url_rule('/upload_image', 'upload', lambda: controller.upload(), methods=['GET', 'POST'])
        app.add_url_rule('/gallery', 'gallery', lambda: controller.gallery())
        app.add_url_rule('/gallery_video', 'gallery_video', lambda: controller.gallery_video())

#mongodb klasse,die die pfade der videos und der bilder enthält
class MongoDb:
    def __init__(self):
        with app.app_context():
            self.mongo = mongo
            self.coll_images = self.mongo.db.images
            self.coll_videos = self.mongo.db.videos
        self.date = Date()
        self.image_str = 'Image'
        self.movie_str = 'Movie'
        self.date_str = 'Date'
        self.time_str = 'Time'
        self.limit = 12

    def insert_image(self, image_name):
        self.coll_images.insert({self.image_str: static_img + image_name + jpg,
                                 self.date_str: image_name})

    def insert_movie(self, movie_name):
        self.coll_videos.insert({self.movie_str: movie_name,
                                 self.date_str: movie_name})

    def read_images(self):
        return self.coll_images.find().sort(self.date_str, -1).limit(self.limit)

    def read_images_casual(self):
        pics_amount = random.randint(1, self.count_images())#min amount of images
        return self.coll_images.find().limit(pics_amount).skip(random.randint(0,3))#choose random images

    def read_videos(self):
        return self.coll_videos.find().sort(self.date_str, -1).limit(self.limit)

    def count_images(self):
        return self.coll_images.find().count()

#datumsklasse für generierung von video und image namen
class Date:
    def get_current_datetime(self):
        return str(datetime.now())

    def get_current_unix_time(self):
        t = datetime.now()
        return str(mktime(t.timetuple()))

if __name__ == "__main__":
    controller = Controller()
    rules = Rules(app, controller)
    app.run(host='0.0.0.0', port=80, threaded=True)
