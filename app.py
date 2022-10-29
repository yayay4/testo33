#!/usr/bin/env python
# coding: utf-8

# In[43]:


from flask import Flask


# In[44]:


import joblib
app = Flask(__name__)


# In[45]:


from flask import request, render_template

#have to run decorater before running Flask, otherwise Flask won't work
@app.route("/", methods=["GET","POST"]) 
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression.joblib")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree.joblib")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
    else: 
        return(render_template("index.html", result1 = "waiting", result2 = "waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




