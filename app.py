from flask import Flask, render_template, jsonify, request

import utils

app = Flask(__name__)


@app.route('/')
def sound_controller_html():
    current_volume = utils.get_current_sound_value()
    return render_template('sound_controller.html', current_volume=current_volume)


@app.route('/api/set_sound_volume')
def sound_controller_api():
    sound_volume = int(request.args.get('sound_volume'))
    utils.set_sound_volume(sound_volume)
    return jsonify({'msg': 'ok'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999)
