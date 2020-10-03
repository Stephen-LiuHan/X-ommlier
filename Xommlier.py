from flask import Flask, render_template, request
import MainSys


app = Flask(__name__)

@app.route('/')
def top():
    """
    http://domain or IP/で表示されるhtml
    """
    content = MainSys.top()
    return render_template('top.html', title='X\'ommlier')

@app.route('/detail/<id>')
def show_detail(id):
    """
    http://domain or IP/detail/<id> で表示される
    データベースIDがidの詳細画面を表示
    """
    content = MainSys.show_detail(id)
    return render_template('detail.html', title='詳細画面', content=content)

@app.route('/detail/<id>/update', methods=['POST'])
def update_detail(id):
    """
    http://domain or IP/detail/<id>/update で表示される
    データベースIDがidの変更画面を表示

    実装予定なし
    """
    if request.method == 'POST':
        content = MainSys.update_detail(id)
        return render_template('detail.html', title='変更完了', content=content, change='Yes')

@app.route('/detail/<id>/remove')
def remove(id):
    """
    http://domain or IP/detail/<id>/remove で表示される
    データベースIDがidを削除
    """
    content = MainSys.remove(id)
    return render_template('remove.html', title='削除完了', content=content)

@app.route('/new', methods = ['POST'])
def new():
    """
    http://domain or IP/new　で新規データを追加
    """
    if request.method == 'POST':
        content = MainSys.new(request)
        return render_templeate('new.html', title='追加', content=content)
@app.route('/led/light')
def light_led():
    """
    http://domain or IP/led/light でledを点灯
    """
    content = MainSys.light_led()

if __name__ == '__main__':
    app.run()