from flask import Flask, request, send_file
from src import upload, search_result
import sys


application = Flask(__name__)


@application.route("/")
def main_page():
    template = ""
    with open("./src/main1.html", "r") as t:
        template = t.read()
    return template


@application.route("/upload", methods=['POST'])
def upload_page():
    template = ""
    with open("./src/upload.html", "r") as t:
        template = t.read()
    return template


@application.route("/upload/result", methods=['POST'])
def upload_result_page():
    user_id = request.form['user_id']
    course_num = request.form['course_num']
    course_name = request.form['course_name']
    professor_name = request.form['professor_name']
    year = request.form['year']
    semester = request.form['semester']
    content = request.form['jokbo']
    template = ""
    upload_code = upload.process(user_id, course_num, course_name, professor_name, year, semester, content)
    template = upload.result_page(upload_code)
    return template


@application.route("/search", methods=['POST'])
def search_page():
    template = ""
    with open("./src/search.html", "r") as t:
        template = t.read()
    return template


@application.route("/search/result", methods=['POST'])
def search_result_page():
    course_num = request.form['course_num']
    course_name = request.form['course_name']
    professor_name = request.form['professor_name']
    template = search_result.search_result(course_num, course_name, professor_name)
    return template


@application.route("/search/result/browse")
def browse_page():
    template = ""
    return template

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
