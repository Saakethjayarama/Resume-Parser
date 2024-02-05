from flask import Flask, request, jsonify
import uuid
from Parser import parse
import os
import zipfile
from Utilities import getPdfFiles, deleteContents

app = Flask(__name__)

DUMP_PATH = os.path.join(os.getcwd(), 'filedumps')
ZIP_DUMP = os.path.join(os.getcwd(), 'zipdumps')
EXTRACT_PATH = os.path.join(os.getcwd(), 'extractPath')

@app.route('/upload', methods=['POST'])
def postFile():
    file = request.files.get('file')
    path = os.path.join(DUMP_PATH, f"{uuid.uuid4()}.pdf")
    file.save(path)
    parsedData = parse(path)
    return jsonify(parsedData)

@app.route('/zip', methods=['POST'])
def postDump():
    file = request.files.get('file')

    folderName = f"{uuid.uuid4()}"
    dumpPath = os.path.join(DUMP_PATH, f"{folderName}.zip")
    extractPath = os.path.join(EXTRACT_PATH, folderName)
    file.save(dumpPath)

    os.makedirs(extractPath, exist_ok=True)

    with zipfile.ZipFile(dumpPath, 'r') as zip_ref:
        zip_ref.extractall(extractPath)
    
    data = []
    pdfFile = getPdfFiles(extractPath)
    for file in pdfFile:
        data.append(parse(file))

    return jsonify(data)

@app.route('/clean')
def clean():
    deleteContents(DUMP_PATH)
    deleteContents(ZIP_DUMP)
    deleteContents(EXTRACT_PATH)
    return jsonify({'status': "success", 'message': "cleaned successfully!"})
    
    

app.run(debug=True)