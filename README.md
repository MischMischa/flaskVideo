# flaskVideo
flask video web app

Generell:
-	Upload.html (zum hochladen von bildern)
-	Gallery.html (darstellen der Bilder)
-	Gallery_video.html (video galerie)

Funktionen:
-	Beim Hochladen eines Bildes wird der Pfad des hochgeladenen Bildes in der Datenbank gespeichert
-	Beim Betreten von gallery.html werden alle Pfade ausgegeben und �ber Jinja2-Direktiven dargestellt
-	Kurz nach dem hochladen der Bilder wird die Datenbank nach vorhandenen Bildern ausgelesen. Diese vorhandenen Bilder(die halbwegs zuf�llig auserw�hlt sind) werden zu einem Videoclip gewandelt
-	Der Pfad des Videoclips wird ebenfalls in der Datenbank gespeichert
-	Beim Betreten von gallery_video.html werden alle Video pfade ausgelesen und �bermittelt. Die Videos aus zuf�llig erstellten Bildern k�nnen nun anschaut werden

Abh�ngigkeiten:
-	Flask
-	Flask-Pymongo
-	Flask-Bootstrap
-	Moviepy