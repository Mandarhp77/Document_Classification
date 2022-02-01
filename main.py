import PyPDF2
a = PyPDF2.PdfFileReader('test.pdf')
pages = a.getNumPages()
#print(a.documentInfo)

#----------------------------------Unique Keywords-------------------------------------------------

w2 = ['identificatin','EIN','(EIN)','Contrl','Wages','tips','Social Security Wages',
'Verification','Nonqualified','Federal','withheld','Medicare','Allocated','tips','State','income',
'Local','Locality','Tax','TreasuryŠInternal','Statutory','Retirement']

#verification = ['Employment','Lender','Lender's', 'badge number','include employee','Present Position',
#'Base Pay','Overtime','Commissions','Bonus','Pay', 'Grade','Rations','Clothing','Quarters','Pro Pay','Authorized Signature','Position', 'Held']

loan_estimate = ['Prepayment','Balloon','Disclosure','Penalty','Mortgage','Projected','Insurance','Underwriting','Appraisal','Flood',
'Property','Agent','Borrower','Refinance','Servicing','Loan','Prepaids','Interest']

#----------------------------------Text Extraction and Input List Formation-------------------------------------------------

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
#print(input)

#----------------------------------Comparision of Document Keywords-------------------------------------------------

W2_doc = []
for words in w2:
    if words in input_list:
        W2_doc.append(words)
len_w2 = len(W2_doc)
print(W2_doc)       
if len_w2>7:
    print(f"The Uploaded Document is W2, words matched = {len_w2}")


loan_doc = []
for words in loan_estimate:
    if words in input_list:
        loan_doc.append(words)
len_loan = len(loan_doc)
print(loan_doc)          
if len_loan>7:
    print(f"The Uploaded Document is Loan Estimation Documentat, words matched = {len_loan}")


if len_w2<5 and len_loan<5:
    print("review your document")
     



