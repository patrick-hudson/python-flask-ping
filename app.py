from flask import Flask, render_template, request, jsonify
from werkzeug.routing import BaseConverter
import pyping
app = Flask(__name__)
statusPing = 0
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

@app.route("/")
def main():
    #
    #return_time = r.output
    return render_template('index.html')
@app.route("/ping/<region>",methods=['POST'])
def catch_all(region):
    ip = request.form['ip']
    if request.method == 'POST':
        r = pyping.ping(ip)
        result = "REGION: " + region + "<br />"
        for i, item in enumerate(r.output):
            result+=item + "<br />"
        #result = r.output
        #aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)
        #result = "\n".join(r.output)
        print result
        return result
    
    #return 'You want path: %s' % param

if __name__ == "__main__":
    app.run(debug=True)