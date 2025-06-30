from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('p4home.html')

@app.route('/p4collection.html')
def collection():
    return render_template('p4collection.html')

@app.route('/p4tryon.html')
def tryon():
    return render_template('p4tryon.html')
    

@app.route('/p4order.html')
def order():
    return render_template('p4order.html')

@app.route('/p4reviews.html')
def reviews():
    return render_template('p4reviews.html')

@app.route('/p4contact.html')
def contact():
    return render_template('p4contact.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Collect order form data
    name = request.form['name']
    contact= request.form['contact']
    email = request.form['email']
    dress = request.form['dress']

    # (Optional) You can print or save these details
    print(f"New Order: {name}, {contact},  {email}, {dress}")

    # After order submission, redirect to Thank You page
    return render_template('p4thankyou.html', name=name,email=email,dress=dress,contact=contact,message="Your order has been placed successfully!")

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Collect contact form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    msg = request.form['msg']

    # (Optional) You can print or save these contact messages
    print(f"New Message: {name}, {email}, {phone}, {msg}")

    # After contact form submission, redirect to Thank You page
    return render_template('p4thankyou.html',message="Your message has been placed successfully!",name=name,email=email,phone=phone,msg=msg)
@app.route('/p4trygirl.html')
def trygirl():
    return render_template('p4trygirl.html')
@app.route('/p4sareegirl.html')
def sareegirl():
    return render_template('p4sareegirl.html')
@app.route('/p4casualgirl.html')
def casualgirl():
    return render_template('p4casualgirl.html')

if __name__ == '__main__':
    app.run(debug=True)