from flask import Flask, render_templete ,request
app =Flask(__name__) 
@app.route('/')
def home ():
    return render_templete('index.html')


if __name__ =="__main__" :
    app.run(debbug=True)
    

#@app.route("/get")
#def get_model_reponse()
