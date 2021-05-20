import os, sys, datetime
from flask import Flask, request, jsonify
from PIL import Image

# to save uploaded images
if not os.path.exists('processing'):
    os.mkdir('processing')

app = Flask(__name__)

@app.route('/index', methods =['POST'])
def main():
    try:
        print("\n\n")
        if request.method == 'POST':
            try:
                if 'image' not in request.files:
                    return jsonify({'result':"", "errorcode" : "1", 'message':"File not selected!"})
                else:
                    uploaded_file = request.files['image']
            
                if uploaded_file.filename != '':
                    uploaded_filename = uploaded_file.filename
                else:
                    uploaded_filename = str(datetime.datetime.now())

                # save image on a path
                print("uploaded_filename : ", uploaded_filename)
                uploaded_file.save('processing/' + uploaded_filename + '.png')
                
            except Exception as e:
               print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")
               return jsonify({'result':"", 'errorcode': "1",  'errormessage':"Error while reading image!"})
            
            return jsonify({"result": "Successfully processed image!" , 'errorcode':"0" ,'errormessage':""})

    except Exception as e:
        print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)


'''
## API DETAILS 
## url : 127.0.0.1:8000/index
## method : "POST"
## request : form-data , "image" : "testImage.png"
## response :
{"result": result , 'errorcode':"0" ,'errormessage':""}
'''

'''
## TEST API
import requests
url_='http://127.0.0.1:8000/index'

uploaded_image_name = "myTestImage.png"
with open(uploaded_image_name, 'rb') as f:
    img_data = f.read()

multipart_form_data = {'file': img_data}

res = requests.post(url=url_,files=multipart_form_data)
f.close()

parsed_json_response = res.json()
print("parsed_json : ", parsed_json_response)
'''
