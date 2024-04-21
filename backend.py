import re
import os
from flask import Flask, render_template, redirect, url_for
from flask.globals import request
from werkzeug.utils import secure_filename
from workers import  txt2questions
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def submit():
    questions = []
    if request.method == 'POST':
        if request.form.get("submit_section1"):  
            print(request.form)
            print(request.files)
            print(request.data)
            # if os.path.exists("some_video.mp4"):
            #     os.remove("some_video.mp4")
            # if os.path.exists("extracted_audio.webm"):
            #     os.remove("extracted_audio.webm")

            # noOfQues = request.form["noq"]    
            # profile = request.files['file']
            # profile.save("some_video.mp4")
            # model.audio_extraction("some_video.mp4")
            # text = model.transcribe_file("extracted_audio.webm")
            # model.text_summarization(text)
            # quiz = model.generate_questions(text)
            # with open('test.txt', 'w', encoding='utf-8') as f:
            #     f.write(str(quiz))
            # return render_template('Quiz.html', text=quiz)
        
        elif request.form.get("submit_section2"):
            print(request.form)
            print(request.files)
            print(request.data)
            # if os.path.exists("extracted_audio.webm"):
            #     os.remove("extracted_audio.webm")
            # video = request.form["video_link"]
            # print(video)
            # noOfQues = request.form["noq"]
            # text = model.youtube_conversion(video)
            # # print(text)
            # # with open('test.txt', 'w', encoding='utf-8') as f:
            # #     f.write(str(text))
            # text_generator = quizTest(text, noOfQues)
            # question_list, answer_list = text_generator.generate_test()

            # testgenerate = zip(question_list, answer_list)
            # return render_template('quiz.html', cresults=testgenerate)
        
        elif request.form.get("submit_section3"):
            # print("Hello")
            # print(request.form)
            # print(request.files)
            # print(request.data)
            # if os.path.exists("Output.txt"): 
            #     os.remove("Output.txt")
            try:
             text = request.form["text_input"]
            #  print(text)
             questions = txt2questions(text)
            #  print(questions)
             # File upload + convert success
             if text is not None:
                UPLOAD_STATUS = True
            except Exception as e:
               print(e)
        return render_template(
              'quiz.html',
              uploaded=UPLOAD_STATUS,
            questions=questions,
            size=len(questions))

@app.route('/result', methods=['POST', 'GET'])
def result():
    correct_q = 0
    for k, v in request.form.items():
        correct_q += 1
    return render_template('result.html', total=5, correct=correct_q)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="8000")
