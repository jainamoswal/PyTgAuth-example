# By @j_projects

# import modules
from flask import Flask, redirect, request
from pytgauth import verify
from config import var


# define app & token
app = Flask(__name__)
token = var.BOT_TOKEN #From @botfather

# define main route.
@app.route('/')
def main():
    if verify(request.args.to_dict(), token):
        return redirect('https://t.me/j_projects')
    return 'Bad request.'

# run the app via __name__ style
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=var.PORT, debug=False)
