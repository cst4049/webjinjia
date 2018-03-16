from flask import Flask, render_template
import requests

# 2.实例化app
app = Flask(__name__)

# 3.映射，默认情况下flask从templates文件夹中寻找模板文件（index.html）
@app.route('/')
def index():
    url ='http://www.kuangjijia.com/tool/api/coinInfo.php'
    data = requests.get(url).json()
    return render_template('a.html',data=data)

if __name__ == '__main__':
    app.run()

