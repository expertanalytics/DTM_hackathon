# Hackathon
While starting up Expert Analytics in Munich, I came in contact with **Deutsches Museum** https://www.deutsches-museum.de/.
It is one of the largest technical museums in Europe and worth a visit.
I did some pro-bono work for them to get our name and competence out to the world and on their homepage.
Now, they proposed another interesting problem, which involves image recognition and api development.
The results of our successful efforts will be shown off on their homepage or maybe even as an exhibit in the museum.
It's all about fame :smile:
So please join all!

## The Challenge
The challenge is to find the one famous scientist, explorer or pioneer, which resembles a given photo of a person (you?) the most.
Then, create a REST-API around the algorithm to query it with a photo.
The stretch goal is a small web page, which takes your picture and sends it to the API, and shows the results.
If the algorithm contains parameters it is also interesting to expose them to the user, so he/she might learn
something about the inner workings of the algorithms.

## Data
We have a dataset of 6758 images of famous historical figures with extensive metadata (in German).
For some people there are several photographs in the dataset, e.g. Newton.
And, some photos contain more than one person, so they are a bit more challenging to use.
The data is of course quite skewed. A lot of white men! So beards should maybe not be the main feature of the algorithm.
http://www.digiporta.net/opendata/
(See photo below)

## How it works
I will present the challenge once more at fagdag, and answer questions.
You can work alone or in a team of how many you wish.
If we are running out of time at this fagdag, we might extend it to the next fagdag.
In the end we want of course a short presentation of each solution :)
The solutions or a merged version will be presented to **Deutsches Museum**. If we have different approaches, we could also showcase all of them or create a merged version. This would allow the users to play with different algorithms.
It is allowed to start thinking and hacking away, from now!

## Hints for tools and Frameworks
There are many tools and frameworks one could use, and the choices are up to you.
Here are some ideas and hints with tools I have had the joy of working with during the last year.

### Image manipulation
- OpenCV, there is no other way.

### Face detection
- mediapipe https://google.github.io/mediapipe/ from google to find the faces in the images.
- Yolo3 https://pjreddie.com/darknet/yolo/ to find the faces
- dlib https://dlib.net/ from c++ or the python wrapper https://pypi.org/project/dlib/
- face_recognition https://github.com/ageitgey/face_recognition uses dlib with a nice interface

### Feature extraction
 - Use a trained resnet https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/ResNet50 model to extract features from fc1 layer of a face to compare the faces
 - face_recognition https://github.com/ageitgey/face_recognition has some tools to find resemblance, not sure how accurate they are.

### Rest API
- Fast API https://fastapi.tiangolo.com/
- Flask https://flask.palletsprojects.com/en/2.0.x/

### Homepage
- vue.js https://vuejs.org/  and vuetify.js https://vuetifyjs.com/en/ .works also with static homepages published with a REST-API endpoint.


# DividedAtBirth
DividedAtBirth uses a package called `face_recognition` from https://github.com/ageitgey/face_recognition. It requires a bank of images and and image to compare.
It should by default be plug'n'play.