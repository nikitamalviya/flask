import sys, datetime, base64
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/index', methods =['POST'])
def main():
    try:
        print("\n\n")
        if request.method == 'POST':
            try:
                response = request.get_json(force=True)
                image_data = bytes(response['imageBase64'], encoding="ascii")
                uploaded_file = Image.open(BytesIO(base64.b64decode(image_data)))

                # save image on a path
                uploaded_filename = str(datetime.datetime.now())
                print("uploaded_filename : ", uploaded_filename)
                uploaded_file.save('processing/' + uploaded_filename + '.png')
                
            except Exception as e:
               print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")
               result=""
               return jsonify({'result':result, 'errorcode': "1",  'errormessage':"Error while reading image!"})
            
            result = "Successfully processed image!"
            return jsonify({"result": result , 'errorcode':"0" ,'errormessage':""})

    except Exception as e:
        print(f"Exception Raised : {e}, errorOnLine: {sys.exc_info()[-1].tb_lineno}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)


'''
## url : 127.0.0.1:8000/index
## method : "POST"
## request :
{
"imageBase64" : b"__image_in_base64__"
}
## response :
{"result": result , 'errorcode':"0" ,'errormessage':""}
'''
