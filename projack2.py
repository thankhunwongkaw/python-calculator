from flask import Flask , request , render_template , redirect , url_for

app = Flask(__name__)


stri = ""
into = 0
intt = 0
summ  = 0
calfun = 0
count = 1
strv =""
fun = ""
selfun = 0
@app.route('/')
def inter():
    return render_template('cal.html' , stri = stri , fun = fun , into = into , intt = intt)

@app.route('/numc' , methods=['POST' , 'GET'])
def add():
    global stri
    stri = stri+request.form['num']
    return redirect('/')
 
@app.route('/calf' , methods=['POST','GET'])
def selectf():
    global stri ,into  ,intt ,summ ,calfun ,count ,strv , fun , selfun
    try:
        calfun = int(request.form['fun'])
    except:
        calfun=0
        pass
    strv = stri
    if count%2 != 0:
        if strv:
            into = int(strv)
            strv =""
            stri =""
            count+=1
    elif count%2 ==0:
        if strv:
            intt = int(strv)
            strv =""
            stri =""
            count+=1

    if (into != 0 ,intt != 0):
        if selfun == 1:
            summ = into + intt
            stri = str(summ)
        elif selfun ==2:
            summ= into - intt
            stri= str(summ)
        elif selfun == 3:
            summ = into*intt
            stri = str(summ)
        elif selfun ==4:
            try:
                summ = into/intt
                stri = str(summ)
            except:
                stri = "AN ERROR OCCURED"
    if calfun ==1:
        fun ="+"
        selfun = 1
    elif calfun ==2:
        fun ="-"
        selfun = 2
    elif calfun ==3:
        fun ="*"
        selfun = 3
    elif calfun == 4:
        fun ="/"
        selfun =4
    elif calfun ==0:
        pass
    
    return redirect('/')

@app.route('/con' , methods=['POST' , 'GET'])
def con():
    global stri ,into  ,intt ,summ ,calfun ,count ,strv , fun , selfun
    stri = ""
    into = 0
    intt = 0
    summ  = 0
    calfun = 0
    count = 1
    strv =""
    fun =""
    selfun =0
    return redirect('/')
        
@app.route('/firm' , methods=['POST'])
def firm():
    return redirect("/calf")
if __name__ == '__main__':
    app.run(port=5287 , debug = True)
