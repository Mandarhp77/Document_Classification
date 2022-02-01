import sys
import os
import glob
import re
import numpy as np
import PyPDF2

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        a = PyPDF2.PdfFileReader('test.pdf')
        pages = a.getNumPages()

        w2 = ['identificatin','EIN','(EIN)','Contrl','Wages','tips','Social Security Wages',
          'Verification','Nonqualified','Federal','withheld','Medicare','Allocated','tips','State','income',
          'Local','Locality','Tax','TreasuryŠInternal','Statutory','Retirement']

        loan_estimate = ['Prepayment','Balloon','Disclosure','Penalty','Mortgage','Projected','Insurance','Underwriting','Appraisal','Flood',
          'Property','Agent','Borrower','Refinance','Servicing','Loan','Prepaids','Interest'] 

        if pages == 1:
            input = (a.getPage(0).extractText())
            input_list = input.split()
            #print(input_list)

        if pages == 3:
            input = (a.getPage(0).extractText())
            input1 = (a.getPage(1).extractText())
            input2 = (a.getPage(2).extractText())

            input_list = input.split()
            input_list1 = input1.split()
            input_list2= input2.split()

            input_list.extend(input_list1)
            input_list.extend(input_list2)

        W2_doc = []
        for words in w2:
            if words in input_list:
                W2_doc.append(words)
        len_w2 = len(W2_doc)
        print(W2_doc)       
        if len_w2>7:
            return render_template('index.html', prediction_texts=(f"The given dcument is W2, words matched {len_w2}"))


        loan_doc = []
        for words in loan_estimate:
            if words in input_list:
                loan_doc.append(words)
        len_loan = len(loan_doc)
        print(loan_doc)          
        if len_loan>7:
            return render_template('index.html', prediction_texts=(f"The given dcument is Loan Estimation, words matched {len_loan}"))
  
        if len_w2<5 and len_loan<5:
            return render_template('index.html', prediction_texts=("Review your Document"))
    return None


if __name__ == '__main__':
    app.run(debug=True)