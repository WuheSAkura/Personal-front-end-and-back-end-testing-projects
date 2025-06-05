from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/emotions')
def emotion():
    return render_template('home.html')

@app.route('/high')
def High():
    return render_template('resume.html')

@app.route('/leader')
def Leaderboard():
    return render_template('contact.html')

@app.route('/blogs')
def blog():
    return render_template('blog.html')

@app.route('/other')
def live():
    return render_template('live.html')


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def handle_request():
#     # 处理请求的逻辑
#     # ...

#     # 假设我们决定需要跳转
#     should_redirect = True
#     redirect_url = '/emotions'  # 或者一个绝对 URL

#     return jsonify({
#         'shouldRedirect': should_redirect,
#         'redirectUrl': redirect_url
#     })



if __name__ == '__main__':
    app.run(debug=True)