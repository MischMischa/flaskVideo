# flaskVideo
flask video web app

Generell:
-	Upload.html (zum hochladen von bildern)
-	Gallery.html (darstellen der Bilder)
-	Gallery_video.html (video galerie)

Funktionen:
-	Beim Hochladen eines Bildes wird der Pfad des hochgeladenen Bildes in der Datenbank gespeichert
-	Beim Betreten von gallery.html werden alle Pfade ausgegeben und über Jinja2-Direktiven dargestellt
-	Kurz nach dem hochladen der Bilder wird die Datenbank nach vorhandenen Bildern ausgelesen. Diese vorhandenen Bilder(die halbwegs zufällig auserwählt sind) werden zu einem Videoclip gewandelt
-	Der Pfad des Videoclips wird ebenfalls in der Datenbank gespeichert
-	Beim Betreten von gallery_video.html werden alle Video pfade ausgelesen und übermittelt. Die Videos aus zufällig erstellten Bildern können nun anschaut werden

Abhängigkeiten:
-	Flask
-	Flask-Pymongo
-	Flask-Bootstrap
-	Moviepy