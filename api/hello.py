from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    font_config = FontConfiguration()
    html = HTML(string='<h1>The title</h1>')
    css = CSS(string='''
        @font-face {
            font-family: Gentium;
            src: url(http://example.com/fonts/Gentium.otf);
        }
        h1 { font-family: Gentium }''', font_config=font_config)
    html.write_pdf(
        '/tmp/example.pdf',
        stylesheets=[css],
        font_config=font_config)

    return send_file('/tmp/example.pdf', 'application/pdf')
