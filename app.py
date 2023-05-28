from flask import Flask, render_template, request, redirect, render_template_string
from database import mycursor, mydb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', backup_url='view_backup', user_url='view_user',
                           accessory_url='view_accessory', client_url='view_client',
                           dealer_url='view_dealer')


class Users:
    def __init__(self, login, password, authentication):
        self.login = login
        self.password = password
        self.authentication = authentication


@app.route('/view_user')
def view_user():
    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    return render_template('view_user.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        authentication = request.form['authentication']
        user = Users(login, password, authentication)
        sql = "INSERT INTO users (login, password, authentication) VALUES (%s, %s, %s)"
        val = (user.login, user.password, user.authentication)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_user')
    else:
        return render_template('add_user.html')


@app.route('/edit_user/<string:login>', methods=['GET', 'POST'])
def edit_user(login):
    mycursor.execute("SELECT * FROM users WHERE login=%s", (login,))
    user = mycursor.fetchone()
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        authentication = request.form['authentication']
        sql = "UPDATE users SET password=%s, authentication=%s WHERE login=%s"
        val = (password, authentication, login)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_user')
    else:
        return render_template('edit_user.html', user=user)


@app.route('/delete_user/<string:login>')
def delete_user(login):
    mycursor.execute("DELETE FROM users WHERE login=%s", (login,))
    mydb.commit()
    return redirect('/view_user')

class Backup:
    def __init__(self, date_of_backup, content_of_backup, size_of_backup, users_login_responsible_of_backup):
        self.date_of_backup = date_of_backup
        self.content_of_backup = content_of_backup
        self.size_of_backup = size_of_backup
        self.users_login_responsible_of_backup = users_login_responsible_of_backup


@app.route('/view_backup')
def view_backup():
    mycursor.execute("SELECT * FROM backup")
    backup = mycursor.fetchall()
    return render_template('view_backup.html', backup=backup)


@app.route('/add_backup', methods=['GET', 'POST'])
def add_backup():
    if request.method == 'POST':
        date_of_backup = request.form['date_of_backup']
        content_of_backup = request.form['content_of_backup']
        size_of_backup = request.form['size_of_backup']
        users_login_responsible_of_backup = request.form['users_login_responsible_of_backup']
        backup = Backup(date_of_backup, content_of_backup, size_of_backup, users_login_responsible_of_backup)
        sql = "INSERT INTO backup (date_of_backup, content_of_backup, size_of_backup, users_login_responsible_of_backup) VALUES (%s, %s, %s, %s)"
        val = (backup.date_of_backup, backup.content_of_backup, backup.size_of_backup, backup.users_login_responsible_of_backup)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_backup')
    else:
        return render_template('add_backup.html')


@app.route('/edit_backup/<string:content_of_backup>', methods=['GET', 'POST'])
def edit_backup(content_of_backup):
    mycursor.execute("SELECT * FROM backup WHERE content_of_backup=%s", (content_of_backup,))
    backup = mycursor.fetchone()
    if request.method == 'POST':
        date_of_backup = request.form['date_of_backup']
        content_of_backup = request.form['content_of_backup']
        size_of_backup = request.form['size_of_backup']
        users_login_responsible_of_backup = request.form['users_login_responsible_of_backup']
        sql = "UPDATE backup SET date_of_backup=%s, size_of_backup=%s, users_login_responsible_of_backup=%s WHERE content_of_backup=%s"
        val = (date_of_backup, size_of_backup, users_login_responsible_of_backup, content_of_backup)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_backup')
    else:
        return render_template('edit_backup.html', backup=backup)


@app.route('/delete_backup/<string:content_of_backup>')
def delete_backup(content_of_backup):
    mycursor.execute("DELETE FROM backup WHERE content_of_backup=%s", (content_of_backup,))
    mydb.commit()
    return redirect('/view_backup')


class Accesory:
    def __init__(self, name_of_accessory, quantity_of_accessory, type_of_accessory):
        self.name_of_accessory = name_of_accessory
        self.quantity_of_accessory = quantity_of_accessory
        self.type_of_accessory = type_of_accessory


@app.route('/view_accessory')
def view_accessory():
    mycursor.execute("SELECT * FROM accessory")
    accessory = mycursor.fetchall()
    return render_template('view_accessory.html', accessory=accessory)


@app.route('/add_accessory', methods=['GET', 'POST'])
def add_accessory():
    if request.method == 'POST':
        name_of_accessory = request.form['name_of_accessory']
        quantity_of_accessory = request.form['quantity_of_accessory']
        type_of_accessory = request.form['type_of_accessory']
        accessory = Accesory(name_of_accessory, quantity_of_accessory, type_of_accessory)
        sql = "INSERT INTO accessory (name_of_accessory, quantity_of_accessory, type_of_accessory) VALUES (%s, %s, %s)"
        val = (accessory.name_of_accessory, accessory.quantity_of_accessory, accessory.type_of_accessory)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_accessory')
    else:
        return render_template('add_accessory.html')


@app.route('/edit_accessory/<string:name_of_accessory>', methods=['GET', 'POST'])
def edit_accessory(name_of_accessory):
    mycursor.execute("SELECT * FROM accessory WHERE name_of_accessory=%s", (name_of_accessory,))
    accessory = mycursor.fetchone()
    if request.method == 'POST':
        name_of_accessory = request.form['name_of_accessory']
        quantity_of_accessory = request.form['quantity_of_accessory']
        type_of_accessory = request.form['type_of_accessory']
        sql = "UPDATE accessory SET quantity_of_accessory=%s, type_of_accessory=%s WHERE name_of_accessory=%s"
        val = (quantity_of_accessory, type_of_accessory, name_of_accessory)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_accessory')
    else:
        return render_template('edit_accessory.html', accessory=accessory)


@app.route('/delete_accessory/<string:name_of_accessory>')
def delete_accessory(name_of_accessory):
    mycursor.execute("DELETE FROM accessory WHERE name_of_accessory=%s", (name_of_accessory,))
    mydb.commit()
    return redirect('/view_accessory')




class Client:
    def __init__(self, name_of_client, surname_of_client, address_of_client, number_phone_of_client, type_of_appeals):
        self.name_of_client = name_of_client
        self.surname_of_client = surname_of_client
        self.address_of_client = address_of_client
        self.number_phone_of_client = number_phone_of_client
        self.type_of_appeals = type_of_appeals


@app.route('/view_client')
def view_client():
    mycursor.execute("SELECT * FROM client")
    client = mycursor.fetchall()
    return render_template('view_client.html', client=client)


@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name_of_client = request.form['name_of_client']
        surname_of_client = request.form['surname_of_client']
        number_phone_of_client = request.form['number_phone_of_client']
        address_of_client = request.form['address_of_client']
        type_of_appeals = request.form['type_of_appeals']
        client = Client(name_of_client, surname_of_client, address_of_client, number_phone_of_client, type_of_appeals)
        sql = "INSERT INTO client (name_of_client, surname_of_client, address_of_client, number_phone_of_client, type_of_appeals) VALUES (%s, %s, %s, %s, %s)"
        val = (client.name_of_client, client.surname_of_client, client.address_of_client, client.number_phone_of_client, client.type_of_appeals)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_client')
    else:
        return render_template('add_client.html')


@app.route('/edit_client/<string:name_of_client>', methods=['GET', 'POST'])
def edit_client(name_of_client):
    mycursor.execute("SELECT * FROM client WHERE name_of_client=%s", (name_of_client,))
    client = mycursor.fetchone()
    if request.method == 'POST':
        name_of_client = request.form['name_of_client']
        surname_of_client = request.form['surname_of_client']
        number_phone_of_client = request.form['number_phone_of_client']
        address_of_client = request.form['address_of_client']
        type_of_appeals = request.form['type_of_appeals']
        sql = "UPDATE client SET surname_of_client=%s, address_of_client=%s, number_phone_of_client=%s, type_of_appeals=%s WHERE name_of_client=%s"
        val = (surname_of_client, address_of_client, number_phone_of_client, type_of_appeals, name_of_client)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_client')
    else:
        return render_template('edit_client.html', client=client)


@app.route('/delete_client/<string:name_of_client>')
def delete_client(name_of_client):
    mycursor.execute("DELETE FROM client WHERE name_of_client=%s", (name_of_client,))
    mydb.commit()
    return redirect('/view_client')



class Dealer:
    def __init__(self, name_of_dealer, address_of_dealer, type_of_services_from_dealer, payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer):
        self.name_of_dealer = name_of_dealer
        self.address_of_dealer = address_of_dealer
        self.type_of_services_from_dealer = type_of_services_from_dealer
        self.payment_to_the_dealer = payment_to_the_dealer
        self.date_of_contract_with_dealer = date_of_contract_with_dealer        
        self.number_of_dealer = number_of_dealer


@app.route('/view_dealer')
def view_dealer():
    mycursor.execute("SELECT * FROM dealer")
    dealer = mycursor.fetchall()
    return render_template('view_dealer.html', dealer=dealer)


@app.route('/add_dealer', methods=['GET', 'POST'])
def add_dealer():
    if request.method == 'POST':
        name_of_dealer = request.form['name_of_dealer']
        address_of_dealer = request.form['address_of_dealer']
        type_of_services_from_dealer = request.form['type_of_services_from_dealer']
        payment_to_the_dealer = request.form['payment_to_the_dealer']
        date_of_contract_with_dealer = request.form['date_of_contract_with_dealer']     
        number_of_dealer = request.form['number_of_dealer']
        dealer = Dealer(name_of_dealer, address_of_dealer, type_of_services_from_dealer, payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer)
        sql = "INSERT INTO dealer (name_of_dealer, address_of_dealer, type_of_services_from_dealer, payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (dealer.name_of_dealer, dealer.address_of_dealer, dealer.type_of_services_from_dealer, dealer.payment_to_the_dealer, dealer.date_of_contract_with_dealer, dealer.number_of_dealer)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_dealer')
    else:
        return render_template('add_dealer.html')


@app.route('/edit_dealer/<string:name_of_dealer>', methods=['GET', 'POST'])
def edit_dealer(name_of_dealer):
    mycursor.execute("SELECT * FROM dealer WHERE name_of_dealer=%s", (name_of_dealer,))
    dealer = mycursor.fetchone()
    if request.method == 'POST':
        name_of_dealer = request.form['name_of_dealer']
        address_of_dealer = request.form['address_of_dealer']
        type_of_services_from_dealer = request.form['type_of_services_from_dealer']
        payment_to_the_dealer = request.form['payment_to_the_dealer']
        date_of_contract_with_dealer = request.form['date_of_contract_with_dealer']          
        number_of_dealer = request.form['number_of_dealer']
        sql = "UPDATE dealer SET address_of_dealer=%s, type_of_services_from_dealer=%s, payment_to_the_dealer=%s, date_of_contract_with_dealer=%s, number_of_dealer=%s WHERE name_of_dealer=%s"
        val = (address_of_dealer, type_of_services_from_dealer, payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer, name_of_dealer)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_dealer')
    else:
        return render_template('edit_dealer.html', dealer=dealer)


@app.route('/delete_dealer/<string:name_of_dealer>')
def delete_dealer(name_of_dealer):
    mycursor.execute("DELETE FROM dealer WHERE name_of_dealer=%s", (name_of_dealer,))
    mydb.commit()
    return redirect('/view_dealer')


if __name__ == '__main__':
    app.run(debug=True)