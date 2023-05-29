from flask import Flask, render_template, request, redirect
from database import mycursor, mydb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', backup_url='view_backup', user_url='view_user',
                           accessory_url='view_accessory', client_url='view_client',
                           dealer_url='view_dealer', delivery_url='view_delivery',
                           departure_url='view_departure',
                           installation_and_deployment_url='view_installation_and_deployment',
                           order_in_the_hall_url='view_order_in_the_hall', purchase_url='view_purchase',
                           report_for_tax_url='view_report_for_tax', service_department_url='view_service_department',
                           stock_url='view_stock', technique_url='view_technique')


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
        sql = "INSERT INTO backup (date_of_backup, content_of_backup, size_of_backup, u" \
              "sers_login_responsible_of_backup) VALUES (%s, %s, %s, %s)"
        val = (backup.date_of_backup, backup.content_of_backup,
               backup.size_of_backup, backup.users_login_responsible_of_backup)
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
        sql = "UPDATE backup SET date_of_backup=%s, size_of_backup=%s," \
              " users_login_responsible_of_backup=%s WHERE content_of_backup=%s"
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
        sql = "INSERT INTO client (name_of_client, surname_of_client, address_of_client, " \
              "number_phone_of_client, type_of_appeals) VALUES (%s, %s, %s, %s, %s)"
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
        sql = "UPDATE client SET surname_of_client=%s, address_of_client=%s, number_phone_of_client=%s, " \
              "type_of_appeals=%s WHERE name_of_client=%s"
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
    def __init__(self, name_of_dealer, address_of_dealer, type_of_services_from_dealer,
                 payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer):
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
        dealer = Dealer(name_of_dealer, address_of_dealer, type_of_services_from_dealer,
                        payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer)
        sql = "INSERT INTO dealer (name_of_dealer, address_of_dealer, type_of_services_from_dealer," \
              " payment_to_the_dealer, date_of_contract_with_dealer, number_of_dealer) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (dealer.name_of_dealer, dealer.address_of_dealer, dealer.type_of_services_from_dealer,
               dealer.payment_to_the_dealer, dealer.date_of_contract_with_dealer, dealer.number_of_dealer)
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
        sql = "UPDATE dealer SET address_of_dealer=%s, type_of_services_from_dealer=%s, payment_to_the_dealer=%s, " \
              "date_of_contract_with_dealer=%s, number_of_dealer=%s WHERE name_of_dealer=%s"
        val = (address_of_dealer, type_of_services_from_dealer, payment_to_the_dealer, date_of_contract_with_dealer,
               number_of_dealer, name_of_dealer)
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



class Delivery:
    def __init__(self, name_of_courier, surname_of_courier, name_of_product, price_with_delivery,
                 from_Stock_address_of_stock, to_Client_address_of_client):
        self.name_of_courier = name_of_courier
        self.surname_of_courier = surname_of_courier
        self.name_of_product = name_of_product
        self.price_with_delivery = price_with_delivery
        self.from_Stock_address_of_stock = from_Stock_address_of_stock        
        self.to_Client_address_of_client = to_Client_address_of_client


@app.route('/view_delivery')
def view_delivery():
    mycursor.execute("SELECT * FROM delivery")
    delivery = mycursor.fetchall()
    return render_template('view_delivery.html', delivery=delivery)


@app.route('/add_delivery', methods=['GET', 'POST'])
def add_delivery():
    if request.method == 'POST':
        name_of_courier = request.form['name_of_courier']
        surname_of_courier = request.form['surname_of_courier']
        name_of_product = request.form['name_of_product']
        price_with_delivery = request.form['price_with_delivery']
        from_Stock_address_of_stock = request.form['from_Stock_address_of_stock']     
        to_Client_address_of_client = request.form['to_Client_address_of_client']
        delivery = Delivery(name_of_courier, surname_of_courier, name_of_product, price_with_delivery,
                            from_Stock_address_of_stock, to_Client_address_of_client)
        sql = "INSERT INTO delivery (name_of_courier, surname_of_courier, name_of_product, price_with_delivery," \
              " from_Stock_address_of_stock, to_Client_address_of_client) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (delivery.name_of_courier, delivery.surname_of_courier, delivery.name_of_product,
               delivery.price_with_delivery, delivery.from_Stock_address_of_stock,
               delivery.to_Client_address_of_client)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_delivery')
    else:
        return render_template('add_delivery.html')


@app.route('/edit_delivery/<string:name_of_courier>', methods=['GET', 'POST'])
def edit_delivery(name_of_courier):
    mycursor.execute("SELECT * FROM delivery WHERE name_of_courier=%s", (name_of_courier,))
    delivery = mycursor.fetchone()
    if request.method == 'POST':
        name_of_courier = request.form['name_of_courier']
        surname_of_courier = request.form['surname_of_courier']
        name_of_product = request.form['name_of_product']
        price_with_delivery = request.form['price_with_delivery']
        from_Stock_address_of_stock = request.form['from_Stock_address_of_stock']          
        to_Client_address_of_client = request.form['to_Client_address_of_client']
        sql = "UPDATE delivery SET surname_of_courier=%s, name_of_product=%s, price_with_delivery=%s, " \
              "from_Stock_address_of_stock=%s, to_Client_address_of_client=%s WHERE name_of_courier=%s"
        val = (surname_of_courier, name_of_product, price_with_delivery, from_Stock_address_of_stock,
               to_Client_address_of_client, name_of_courier)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_delivery')
    else:
        return render_template('edit_delivery.html', delivery=delivery)


@app.route('/delete_delivery/<string:name_of_courier>')
def delete_delivery(name_of_courier):
    mycursor.execute("DELETE FROM delivery WHERE name_of_courier=%s", (name_of_courier,))
    mydb.commit()
    return redirect('/view_delivery')


class Departure:
    def __init__(self, type_of_service, price_of_service, result, status_of_departure,
                 To_Client_address_of_client, responsible):
        self.type_of_service = type_of_service
        self.price_of_service = price_of_service
        self.result = result
        self.status_of_departure = status_of_departure
        self.To_Client_address_of_client = To_Client_address_of_client        
        self.responsible = responsible


@app.route('/view_departure')
def view_departure():
    mycursor.execute("SELECT * FROM departure")
    departure = mycursor.fetchall()
    return render_template('view_departure.html', departure=departure)


@app.route('/add_departure', methods=['GET', 'POST'])
def add_departure():
    if request.method == 'POST':
        type_of_service = request.form['type_of_service']
        price_of_service = request.form['price_of_service']
        result = request.form['result']
        status_of_departure = request.form['status_of_departure']
        To_Client_address_of_client = request.form['To_Client_address_of_client']     
        responsible = request.form['responsible']
        departure = Departure(type_of_service, price_of_service, result, status_of_departure,
                              To_Client_address_of_client, responsible)
        sql = "INSERT INTO departure (type_of_service, price_of_service, result, status_of_departure, " \
              "To_Client_address_of_client, responsible) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (departure.type_of_service, departure.price_of_service, departure.result, departure.status_of_departure,
               departure.To_Client_address_of_client, departure.responsible)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_departure')
    else:
        return render_template('add_departure.html')


@app.route('/edit_departure/<string:To_Client_address_of_client>', methods=['GET', 'POST'])
def edit_departure(To_Client_address_of_client):
    mycursor.execute("SELECT * FROM departure WHERE To_Client_address_of_client=%s", (To_Client_address_of_client,))
    departure = mycursor.fetchone()
    if request.method == 'POST':
        type_of_service = request.form['type_of_service']
        price_of_service = request.form['price_of_service']
        result = request.form['result']
        status_of_departure = request.form['status_of_departure']
        To_Client_address_of_client = request.form['To_Client_address_of_client']          
        responsible = request.form['responsible']
        sql = "UPDATE departure SET type_of_service=%s, price_of_service=%s, result=%s, " \
              "status_of_departure=%s, responsible=%s WHERE To_Client_address_of_client=%s"
        val = (type_of_service, price_of_service, result, status_of_departure, responsible, To_Client_address_of_client)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_departure')
    else:
        return render_template('edit_departure.html', departure=departure)


@app.route('/delete_departure/<string:To_Client_address_of_client>')
def delete_departure(To_Client_address_of_client):
    mycursor.execute("DELETE FROM departure WHERE To_Client_address_of_client=%s", (To_Client_address_of_client,))
    mydb.commit()
    return redirect('/view_departure')

class Installation_and_deployment:
    def __init__(self, date_of_installation, type_of_installation, status_of_installation, duration_time,
                 result, Users_login_responsible_of_installation):
        self.date_of_installation = date_of_installation
        self.type_of_installation = type_of_installation
        self.status_of_installation = status_of_installation
        self.duration_time = duration_time
        self.result = result        
        self.Users_login_responsible_of_installation = Users_login_responsible_of_installation


@app.route('/view_installation_and_deployment')
def view_installation_and_deployment():
    mycursor.execute("SELECT * FROM installation_and_deployment")
    installation_and_deployment = mycursor.fetchall()
    return render_template('view_installation_and_deployment.html',
                           installation_and_deployment=installation_and_deployment)


@app.route('/add_installation_and_deployment', methods=['GET', 'POST'])
def add_installation_and_deployment():
    if request.method == 'POST':
        date_of_installation = request.form['date_of_installation']
        type_of_installation = request.form['type_of_installation']
        status_of_installation = request.form['status_of_installation']
        duration_time = request.form['duration_time']
        result = request.form['result']     
        Users_login_responsible_of_installation = request.form['Users_login_responsible_of_installation']
        installation_and_deployment = Installation_and_deployment(date_of_installation, type_of_installation,
                                                                  status_of_installation, duration_time, result,
                                                                  Users_login_responsible_of_installation)
        sql = "INSERT INTO installation_and_deployment (date_of_installation, type_of_installation, " \
              "status_of_installation, duration_time, result, Users_login_responsible_of_installation)" \
              " VALUES (%s, %s, %s, %s, %s, %s)"
        val = (installation_and_deployment.date_of_installation, installation_and_deployment.type_of_installation,
               installation_and_deployment.status_of_installation, installation_and_deployment.duration_time,
               installation_and_deployment.result, installation_and_deployment.Users_login_responsible_of_installation)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_installation_and_deployment')
    else:
        return render_template('add_installation_and_deployment.html')


@app.route('/edit_installation_and_deployment/<string:Users_login_responsible_of_installation>',
           methods=['GET', 'POST'])
def edit_installation_and_deployment(Users_login_responsible_of_installation):
    mycursor.execute("SELECT * FROM installation_and_deployment WHERE Users_login_responsible_of_installation=%s",
                     (Users_login_responsible_of_installation,))
    installation_and_deployment = mycursor.fetchone()
    if request.method == 'POST':
        date_of_installation = request.form['date_of_installation']
        type_of_installation = request.form['type_of_installation']
        status_of_installation = request.form['status_of_installation']
        duration_time = request.form['duration_time']
        result = request.form['result']          
        Users_login_responsible_of_installation = request.form['Users_login_responsible_of_installation']
        sql = "UPDATE installation_and_deployment SET date_of_installation=%s, type_of_installation=%s, " \
              "status_of_installation=%s, duration_time=%s, result=%s WHERE Users_login_responsible_of_installation=%s"
        val = (date_of_installation, type_of_installation, status_of_installation, duration_time, result,
               Users_login_responsible_of_installation)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_installation_and_deployment')
    else:
        return render_template('edit_installation_and_deployment.html',
                               installation_and_deployment=installation_and_deployment)


@app.route('/delete_installation_and_deployment/<string:Users_login_responsible_of_installation>')
def delete_installation_and_deployment(Users_login_responsible_of_installation):
    mycursor.execute("DELETE FROM installation_and_deployment WHERE Users_login_responsible_of_installation=%s",
                     (Users_login_responsible_of_installation,))
    mydb.commit()
    return redirect('/view_installation_and_deployment')


class Order_in_the_hall:
    def __init__(self, date_of_order, price_for_technique, quantity_of_technique, Client_name_of_client,
                 Technique_type_of_technique, Users_loginresponsible_for_order):
        self.date_of_order = date_of_order
        self.price_for_technique = price_for_technique
        self.quantity_of_technique = quantity_of_technique
        self.Client_name_of_client = Client_name_of_client
        self.Technique_type_of_technique = Technique_type_of_technique        
        self.Users_loginresponsible_for_order = Users_loginresponsible_for_order


@app.route('/view_order_in_the_hall')
def view_order_in_the_hall():
    mycursor.execute("SELECT * FROM order_in_the_hall")
    order_in_the_hall = mycursor.fetchall()
    return render_template('view_order_in_the_hall.html', order_in_the_hall=order_in_the_hall)


@app.route('/add_order_in_the_hall', methods=['GET', 'POST'])
def add_order_in_the_hall():
    if request.method == 'POST':
        date_of_order = request.form['date_of_order']
        price_for_technique = request.form['price_for_technique']
        quantity_of_technique = request.form['quantity_of_technique']
        Client_name_of_client = request.form['Client_name_of_client']
        Technique_type_of_technique = request.form['Technique_type_of_technique']     
        Users_loginresponsible_for_order = request.form['Users_loginresponsible_for_order']
        order_in_the_hall = Order_in_the_hall(date_of_order, price_for_technique, quantity_of_technique,
                                              Client_name_of_client, Technique_type_of_technique,
                                              Users_loginresponsible_for_order)
        sql = "INSERT INTO order_in_the_hall (date_of_order, price_for_technique, quantity_of_technique, " \
              "Client_name_of_client, Technique_type_of_technique, Users_loginresponsible_for_order) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        val = (order_in_the_hall.date_of_order, order_in_the_hall.price_for_technique,
               order_in_the_hall.quantity_of_technique, order_in_the_hall.Client_name_of_client,
               order_in_the_hall.Technique_type_of_technique, order_in_the_hall.Users_loginresponsible_for_order)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_order_in_the_hall')
    else:
        return render_template('add_order_in_the_hall.html')


@app.route('/edit_order_in_the_hall/<string:Users_loginresponsible_for_order>', methods=['GET', 'POST'])
def edit_order_in_the_hall(Users_loginresponsible_for_order):
    mycursor.execute("SELECT * FROM order_in_the_hall WHERE Users_loginresponsible_for_order=%s",
                     (Users_loginresponsible_for_order,))
    order_in_the_hall = mycursor.fetchone()
    if request.method == 'POST':
        date_of_order = request.form['date_of_order']
        price_for_technique = request.form['price_for_technique']
        quantity_of_technique = request.form['quantity_of_technique']
        Client_name_of_client = request.form['Client_name_of_client']
        Technique_type_of_technique = request.form['Technique_type_of_technique']          
        Users_loginresponsible_for_order = request.form['Users_loginresponsible_for_order']
        sql = "UPDATE order_in_the_hall SET date_of_order=%s, price_for_technique=%s, quantity_of_technique=%s, " \
              "Client_name_of_client=%s, Technique_type_of_technique=%s WHERE Users_loginresponsible_for_order=%s"
        val = (date_of_order, price_for_technique, quantity_of_technique, Client_name_of_client,
               Technique_type_of_technique, Users_loginresponsible_for_order)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_order_in_the_hall')
    else:
        return render_template('edit_order_in_the_hall.html', order_in_the_hall=order_in_the_hall)


@app.route('/delete_order_in_the_hall/<string:Users_loginresponsible_for_order>')
def delete_order_in_the_hall(Users_loginresponsible_for_order):
    mycursor.execute("DELETE FROM order_in_the_hall WHERE Users_loginresponsible_for_order=%s",
                     (Users_loginresponsible_for_order,))
    mydb.commit()
    return redirect('/view_order_in_the_hall')


class Purchase:
    def __init__(self, name_of_product, quantity_of_product, description_of_product,
                 factory_number, serial_number, purchase_amount):
        self.name_of_product = name_of_product
        self.quantity_of_product = quantity_of_product
        self.description_of_product = description_of_product
        self.factory_number = factory_number
        self.serial_number = serial_number        
        self.purchase_amount = purchase_amount


@app.route('/view_purchase')
def view_purchase():
    mycursor.execute("SELECT * FROM purchase")
    purchase = mycursor.fetchall()
    return render_template('view_purchase.html', purchase=purchase)


@app.route('/add_purchase', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        name_of_product = request.form['name_of_product']
        quantity_of_product = request.form['quantity_of_product']
        description_of_product = request.form['description_of_product']
        factory_number = request.form['factory_number']
        serial_number = request.form['serial_number']     
        purchase_amount = request.form['purchase_amount']
        purchase = Purchase(name_of_product, quantity_of_product, description_of_product,
                            factory_number, serial_number, purchase_amount)
        sql = "INSERT INTO purchase (name_of_product, quantity_of_product, description_of_product, " \
              "factory_number, serial_number, purchase_amount) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (purchase.name_of_product, purchase.quantity_of_product, purchase.description_of_product,
               purchase.factory_number, purchase.serial_number, purchase.purchase_amount)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_purchase')
    else:
        return render_template('add_purchase.html')


@app.route('/edit_purchase/<string:name_of_product>', methods=['GET', 'POST'])
def edit_purchase(name_of_product):
    mycursor.execute("SELECT * FROM purchase WHERE name_of_product=%s", (name_of_product,))
    purchase = mycursor.fetchone()
    if request.method == 'POST':
        name_of_product = request.form['name_of_product']
        quantity_of_product = request.form['quantity_of_product']
        description_of_product = request.form['description_of_product']
        factory_number = request.form['factory_number']
        serial_number = request.form['serial_number']          
        purchase_amount = request.form['purchase_amount']
        sql = "UPDATE purchase SET quantity_of_product=%s, description_of_product=%s, factory_number=%s," \
              " serial_number=%s, purchase_amount=%s WHERE name_of_product=%s"
        val = (name_of_product, quantity_of_product, description_of_product, factory_number,
               serial_number, purchase_amount, name_of_product)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_purchase')
    else:
        return render_template('edit_purchase.html', purchase=purchase)


@app.route('/delete_purchase/<string:name_of_product>')
def delete_purchase(name_of_product):
    mycursor.execute("DELETE FROM purchase WHERE name_of_product=%s", (name_of_product,))
    mydb.commit()
    return redirect('/view_purchase')


class Technique:
    def __init__(self, name_of_technique, type_of_technique, serial_number, factory_number,
                 quantity_of_technique, Users_login_responsible_for_the_technique):
        self.name_of_technique = name_of_technique
        self.type_of_technique = type_of_technique
        self.serial_number = serial_number
        self.factory_number = factory_number
        self.quantity_of_technique = quantity_of_technique        
        self.Users_login_responsible_for_the_technique = Users_login_responsible_for_the_technique


@app.route('/view_technique')
def view_technique():
    mycursor.execute("SELECT * FROM technique")
    technique = mycursor.fetchall()
    return render_template('view_technique.html', technique=technique)


@app.route('/add_technique', methods=['GET', 'POST'])
def add_technique():
    if request.method == 'POST':
        name_of_technique = request.form['name_of_technique']
        type_of_technique = request.form['type_of_technique']
        serial_number = request.form['serial_number']
        factory_number = request.form['factory_number']
        quantity_of_technique = request.form['quantity_of_technique']     
        Users_login_responsible_for_the_technique = request.form['Users_login_responsible_for_the_technique']
        technique = Technique(name_of_technique, type_of_technique, serial_number, factory_number,
                              quantity_of_technique, Users_login_responsible_for_the_technique)
        sql = "INSERT INTO technique (name_of_technique, type_of_technique, serial_number, factory_number, " \
              "quantity_of_technique, Users_login_responsible_for_the_technique) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (technique.name_of_technique, technique.type_of_technique, technique.serial_number,
               technique.factory_number, technique.quantity_of_technique,
               technique.Users_login_responsible_for_the_technique)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_technique')
    else:
        return render_template('add_technique.html')


@app.route('/edit_technique/<string:Users_login_responsible_for_the_technique>', methods=['GET', 'POST'])
def edit_technique(Users_login_responsible_for_the_technique):
    mycursor.execute("SELECT * FROM technique WHERE Users_login_responsible_for_the_technique=%s",
                     (Users_login_responsible_for_the_technique,))
    technique = mycursor.fetchone()
    if request.method == 'POST':
        name_of_technique = request.form['name_of_technique']
        type_of_technique = request.form['type_of_technique']
        serial_number = request.form['serial_number']
        factory_number = request.form['factory_number']
        quantity_of_technique = request.form['quantity_of_technique']          
        Users_login_responsible_for_the_technique = request.form['Users_login_responsible_for_the_technique']
        sql = "UPDATE technique SET name_of_technique=%s, type_of_technique=%s, serial_number=%s, " \
              "factory_number=%s, quantity_of_technique=%s WHERE Users_login_responsible_for_the_technique=%s"
        val = (name_of_technique, type_of_technique, serial_number, factory_number, quantity_of_technique,
               Users_login_responsible_for_the_technique)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_technique')
    else:
        return render_template('edit_technique.html', technique=technique)


@app.route('/delete_technique/<string:Users_login_responsible_for_the_technique>')
def delete_technique(Users_login_responsible_for_the_technique):
    mycursor.execute("DELETE FROM technique WHERE Users_login_responsible_for_the_technique=%s",
                     (Users_login_responsible_for_the_technique,))
    mydb.commit()
    return redirect('/view_technique')


class Stock:
    def __init__(self, address_of_stock, quantity_of_stuff, type_of_stock, number_phone_of_stock,
                 Users_login_responsible_of_stock):
        self.address_of_stock = address_of_stock
        self.quantity_of_stuff = quantity_of_stuff
        self.type_of_stock = type_of_stock
        self.number_phone_of_stock = number_phone_of_stock
        self.Users_login_responsible_of_stock = Users_login_responsible_of_stock


@app.route('/view_stock')
def view_stock():
    mycursor.execute("SELECT * FROM stock")
    stock = mycursor.fetchall()
    return render_template('view_stock.html', stock=stock)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        address_of_stock = request.form['address_of_stock']
        quantity_of_stuff = request.form['quantity_of_stuff']
        type_of_stock = request.form['type_of_stock']
        number_phone_of_stock = request.form['number_phone_of_stock']    
        Users_login_responsible_of_stock = request.form['Users_login_responsible_of_stock']
        stock = Stock(address_of_stock, quantity_of_stuff, type_of_stock, number_phone_of_stock,
                      Users_login_responsible_of_stock)
        sql = "INSERT INTO stock (address_of_stock, quantity_of_stuff, type_of_stock," \
              " number_phone_of_stock, Users_login_responsible_of_stock) VALUES (%s, %s, %s, %s, %s)"
        val = (stock.address_of_stock, stock.quantity_of_stuff, stock.type_of_stock, stock.number_phone_of_stock,
               stock.Users_login_responsible_of_stock)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_stock')
    else:
        return render_template('add_stock.html')


@app.route('/edit_stock/<string:Users_login_responsible_of_stock>', methods=['GET', 'POST'])
def edit_stock(Users_login_responsible_of_stock):
    mycursor.execute("SELECT * FROM stock WHERE Users_login_responsible_of_stock=%s",
                     (Users_login_responsible_of_stock,))
    stock = mycursor.fetchone()
    if request.method == 'POST':
        address_of_stock = request.form['address_of_stock']
        quantity_of_stuff = request.form['quantity_of_stuff']
        type_of_stock = request.form['type_of_stock']
        number_phone_of_stock = request.form['number_phone_of_stock']       
        Users_login_responsible_of_stock = request.form['Users_login_responsible_of_stock']
        sql = "UPDATE stock SET address_of_stock=%s, quantity_of_stuff=%s, type_of_stock=%s, " \
              "number_phone_of_stock=%s, WHERE Users_login_responsible_of_stock=%s"
        val = (address_of_stock, quantity_of_stuff, type_of_stock, number_phone_of_stock,
               Users_login_responsible_of_stock)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_stock')
    else:
        return render_template('edit_stock.html', stock=stock)


@app.route('/delete_stock/<string:Users_login_responsible_of_stock>')
def delete_stock(Users_login_responsible_of_stock):
    mycursor.execute("DELETE FROM stock WHERE Users_login_responsible_of_stock=%s", (Users_login_responsible_of_stock,))
    mydb.commit()
    return redirect('/view_stock')


class Service_department:
    def __init__(self, address_of_service_department, quantity_stuff_in_service_department,
                 number_phone_of_service_department, post_code_of_service_department):
        self.address_of_service_department = address_of_service_department
        self.quantity_stuff_in_service_department = quantity_stuff_in_service_department
        self.number_phone_of_service_department = number_phone_of_service_department
        self.post_code_of_service_department = post_code_of_service_department


@app.route('/view_service_department')
def view_service_department():
    mycursor.execute("SELECT * FROM service_department")
    service_department = mycursor.fetchall()
    return render_template('view_service_department.html', service_department=service_department)


@app.route('/add_service_department', methods=['GET', 'POST'])
def add_service_department():
    if request.method == 'POST':
        address_of_service_department = request.form['address_of_service_department']
        quantity_stuff_in_service_department = request.form['quantity_stuff_in_service_department']
        number_phone_of_service_department = request.form['number_phone_of_service_department']
        post_code_of_service_department = request.form['post_code_of_service_department']    
        service_department = Service_department(address_of_service_department, quantity_stuff_in_service_department,
                                                number_phone_of_service_department, post_code_of_service_department)
        sql = "INSERT INTO service_department (address_of_service_department, " \
              "quantity_stuff_in_service_department, number_phone_of_service_department, " \
              "post_code_of_service_department) VALUES (%s, %s, %s, %s)"
        val = (service_department.address_of_service_department,
               service_department.quantity_stuff_in_service_department,
               service_department.number_phone_of_service_department,
               service_department.post_code_of_service_department)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_service_department')
    else:
        return render_template('add_service_department.html')


@app.route('/edit_service_department/<string:post_code_of_service_department>', methods=['GET', 'POST'])
def edit_service_department(post_code_of_service_department):
    mycursor.execute("SELECT * FROM service_department WHERE post_code_of_service_department=%s",
                     (post_code_of_service_department,))
    service_department = mycursor.fetchone()
    if request.method == 'POST':
        address_of_service_department = request.form['address_of_service_department']
        quantity_stuff_in_service_department = request.form['quantity_stuff_in_service_department']
        number_phone_of_service_department = request.form['number_phone_of_service_department']
        post_code_of_service_department = request.form['post_code_of_service_department']       
        sql = "UPDATE service_department SET address_of_service_department=%s, " \
              "quantity_stuff_in_service_department=%s, number_phone_of_service_department=%s " \
              "WHERE post_code_of_service_department=%s"
        val = (address_of_service_department, quantity_stuff_in_service_department,
               number_phone_of_service_department, post_code_of_service_department)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_service_department')
    else:
        return render_template('edit_service_department.html', service_department=service_department)


@app.route('/delete_service_department/<string:post_code_of_service_department>')
def delete_service_department(post_code_of_service_department):
    mycursor.execute("DELETE FROM service_department WHERE post_code_of_service_department=%s",
                     (post_code_of_service_department,))
    mydb.commit()
    return redirect('/view_service_department')

class Report_for_TAX:
    def __init__(self, date_of_formation_report, date_of_sendig_report, signature, to_tax, from_company,
                 content_of_report, type_of_delivery_report, Users_login_responsible_for_the_report):
        self.date_of_formation_report = date_of_formation_report
        self.date_of_sendig_report = date_of_sendig_report
        self.signature = signature
        self.to_tax = to_tax
        self.from_company = from_company
        self.content_of_report = content_of_report
        self.type_of_delivery_report = type_of_delivery_report
        self.Users_login_responsible_for_the_report = Users_login_responsible_for_the_report


@app.route('/view_report_for_tax')
def view_report_for_tax():
    mycursor.execute("SELECT * FROM report_for_tax")
    report_for_tax = mycursor.fetchall()
    return render_template('view_report_for_tax.html', report_for_tax=report_for_tax)


@app.route('/add_report_for_tax', methods=['GET', 'POST'])
def add_report_for_tax():
    if request.method == 'POST':
        date_of_formation_report = request.form['date_of_formation_report']
        date_of_sendig_report = request.form['date_of_sendig_report']
        signature = request.form['signature']
        to_tax = request.form['to_tax']
        from_company = request.form['from_company']
        content_of_report = request.form['content_of_report']
        type_of_delivery_report = request.form['type_of_delivery_report']
        Users_login_responsible_for_the_report = request.form['Users_login_responsible_for_the_report']
        report_for_tax = Report_for_TAX(date_of_formation_report, date_of_sendig_report,
                                        signature, to_tax, from_company, content_of_report,
                                        type_of_delivery_report, Users_login_responsible_for_the_report)
        sql = "INSERT INTO report_for_tax (date_of_formation_report, date_of_sendig_report, signature, " \
              "to_tax, from_company, content_of_report, type_of_delivery_report, " \
              "Users_login_responsible_for_the_report) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (report_for_tax.date_of_formation_report, report_for_tax.date_of_sendig_report,
               report_for_tax.signature, report_for_tax.to_tax, report_for_tax.from_company,
               report_for_tax.content_of_report, report_for_tax.type_of_delivery_report,
               report_for_tax.Users_login_responsible_for_the_report)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_report_for_tax')
    else:
        return render_template('add_report_for_tax.html')


@app.route('/edit_report_for_tax/<string:from_company>', methods=['GET', 'POST'])
def edit_report_for_tax(from_company):
    mycursor.execute("SELECT * FROM report_for_tax WHERE from_company=%s", (from_company,))
    report_for_tax = mycursor.fetchone()
    if request.method == 'POST':
        date_of_formation_report = request.form['date_of_formation_report']
        date_of_sendig_report = request.form['date_of_sendig_report']
        signature = request.form['signature']
        to_tax = request.form['to_tax']
        from_company = request.form['from_company']
        content_of_report = request.form['content_of_report']
        type_of_delivery_report = request.form['type_of_delivery_report']
        Users_login_responsible_for_the_report = request.form['Users_login_responsible_for_the_report']
        sql = "UPDATE report_for_tax SET date_of_formation_report=%s, date_of_sendig_report=%s," \
              " signature=%s, to_tax=%s, content_of_report=%s, type_of_delivery_report=%s," \
              " Users_login_responsible_for_the_report=%s WHERE from_company=%s"
        val = (date_of_formation_report, date_of_sendig_report, signature, to_tax, content_of_report,
               type_of_delivery_report, Users_login_responsible_for_the_report, from_company)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/view_report_for_tax')
    else:
        return render_template('edit_report_for_tax.html', report_for_tax=report_for_tax)


@app.route('/delete_report_for_tax/<string:from_company>')
def delete_report_for_tax(from_company):
    mycursor.execute("DELETE FROM report_for_tax WHERE from_company=%s", (from_company,))
    mydb.commit()
    return redirect('/view_report_for_tax')



if __name__ == '__main__':
    app.run(debug=True)
