import unittest
from app import app
from database import mycursor


class TestApp(unittest.TestCase):
    def test_view_user(self):
        with app.test_client() as client:
            response = client.get('/view_user')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_user(self):
        with app.test_client() as client:
            response = client.post('/add_user', data=dict(login='test', password='test', authentication='0'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM users WHERE login='test'")
            user = mycursor.fetchone()
            self.assertIsNotNone(user)
    def test_edit_user(self):
        with app.test_client() as client:
            response = client.post('/edit_user/test', data=dict(login='test', password='test2', authentication='1'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM users WHERE login='test'")
            user = mycursor.fetchone()
            if user is not None:
                self.assertEqual(user[1], 'test2')
    def test_delete_user(self):
        with app.test_client() as client:
            response = client.get('/delete_user/test')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM users WHERE login='test'")
            user = mycursor.fetchone()
            self.assertIsNone(user)
    def test_view_backup(self):
        with app.test_client() as client:
            response = client.get('/view_backup')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_backup(self):
        with app.test_client() as client:
            response = client.post('/add_backup',
                                   data=dict(date_of_backup='2022-01-01', content_of_backup='test_backup',
                                             size_of_backup='5GB', users_login_responsible_of_backup='test_user'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM backup WHERE content_of_backup='test_backup'")
            backup = mycursor.fetchone()
            self.assertIsNotNone(backup)
    def test_edit_backup(self):
        with app.test_client() as client:
            response = client.post('/edit_backup/test_backup',
                                   data=dict(date_of_backup='2022-01-02', content_of_backup='test_backup',
                                             size_of_backup='10GB', users_login_responsible_of_backup='test_user2'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM backup WHERE content_of_backup='test_backup'")
            backup = mycursor.fetchone()
            if backup is not None:
                self.assertEqual(backup[2], '10GB')
    def test_delete_backup(self):
        with app.test_client() as client:
            response = client.get('/delete_backup/test_backup')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM backup WHERE content_of_backup='test_backup'")
            backup = mycursor.fetchone()
            self.assertIsNone(backup)
    def test_view_accessory(self):
        with app.test_client() as client:
            response = client.get('/view_accessory')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_accessory(self):
        with app.test_client() as client:
            response = client.post('/add_accessory', data=dict(name_of_accessory='test', quantity_of_accessory='10',
                                                               type_of_accessory='type'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM accessory WHERE name_of_accessory='test'")
            accessory = mycursor.fetchone()
            self.assertIsNotNone(accessory)
    def test_edit_accessory(self):
        with app.test_client() as client:
            response = client.post('/edit_accessory/test',
                                   data=dict(name_of_accessory='test', quantity_of_accessory='20',
                                             type_of_accessory='type2'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM accessory WHERE name_of_accessory='test'")
            accessory = mycursor.fetchone()
            if accessory is not None:
                self.assertEqual(accessory[2], '20')
                self.assertEqual(accessory[3], 'type2')
    def test_delete_accessory(self):
        with app.test_client() as client:
            response = client.get('/delete_accessory/test')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM accessory WHERE name_of_accessory='test'")
            accessory = mycursor.fetchone()
            self.assertIsNone(accessory)
    def test_view_client(self):
        with app.test_client() as client:
            response = client.get('/view_client')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_client(self):
        with app.test_client() as client:
            response = client.post('/add_client', data=dict(name_of_client='test', surname_of_client='test',
                                                            number_phone_of_client='123456789',
                                                            address_of_client='test_address',
                                                            type_of_appeals='test_type'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM client WHERE name_of_client ='test'")
            client = mycursor.fetchone()
            self.assertIsNotNone(client)
    def test_edit_client(self):
        with app.test_client() as client:
            response = client.post('/edit_client/test', data=dict(name_of_client='test', surname_of_client='test2',
                                                                  number_phone_of_client='123456789',
                                                                  address_of_client='test_address',
                                                                  type_of_appeals='test_type'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM client WHERE name_of_client ='test'")
            client = mycursor.fetchone()
            if client is not None:
                self.assertEqual(client[1], 'test2')
    def test_delete_client(self):
        with app.test_client() as client:
            response = client.get('/delete_client/test')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM client WHERE name_of_client ='test'")
            client = mycursor.fetchone()
            self.assertIsNone(client)
    def test_view_technique(self):
        with app.test_client() as client:
            response = client.get('/view_technique')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_technique(self):
        with app.test_client() as client:
            response = client.post('/add_technique', data=dict(
                name_of_technique='test_technique', type_of_technique='typing_technique', serial_number='2141',
                factory_number='21411',
                quantity_of_technique='215', Users_login_responsible_for_the_technique='test_resp_for_technique'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM technique WHERE Users_login_responsible_for_the_technique ='test_resp_for_technique'")
            technique = mycursor.fetchone()
            self.assertIsNotNone(technique)
    def test_edit_technique(self):
        with app.test_client() as client:
            response = client.post('/add_technique', data=dict(
                name_of_technique='test_technique', type_of_technique='typing_technique', serial_number='2141',
                factory_number='21411',
                quantity_of_technique='215', Users_login_responsible_for_the_technique='test_resp_for_technique'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM technique WHERE Users_login_responsible_for_the_technique ='test_resp_for_technique'")
            technique = mycursor.fetchone()
            if technique is not None:
                self.assertEqual(technique[5], 'test_resp_for_technique')
    def test_delete_technique(self):
        with app.test_client() as client:
            response = client.get('/delete_technique/test_resp_for_technique')
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM technique WHERE Users_login_responsible_for_the_technique ='test_resp_for_technique'")
            technique = mycursor.fetchone()
            self.assertIsNone(technique)
    def test_view_delivery(self):
        with app.test_client() as client:
            response = client.get('/view_delivery')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_delivery(self):
        with app.test_client() as client:
            response = client.post('/add_delivery', data=dict(name_of_courier='test', surname_of_courier='test',
                                                              name_of_product='test_product', price_with_delivery='10',
                                                              from_Stock_address_of_stock='test_stock',
                                                              to_Client_address_of_client='test_client'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM delivery WHERE name_of_courier ='test'")
            delivery = mycursor.fetchone()
            self.assertIsNotNone(delivery)
    def test_edit_delivery(self):
        with app.test_client() as client:
            response = client.post('/edit_delivery/test', data=dict(name_of_courier='test', surname_of_courier='test2',
                                                                    name_of_product='test_product',
                                                                    price_with_delivery='10',
                                                                    from_Stock_address_of_stock='test_stock',
                                                                    to_Client_address_of_client='test_client'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM delivery WHERE name_of_courier ='test'")
            delivery = mycursor.fetchone()
            if delivery is not None:
                self.assertEqual(delivery[1], 'test2')
    def test_delete_delivery(self):
        with app.test_client() as client:
            response = client.get('/delete_delivery/test')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM delivery WHERE name_of_courier ='test'")
            delivery = mycursor.fetchone()
            self.assertIsNone(delivery)
    def test_view_departure(self):
        with app.test_client() as client:
            response = client.get('/view_departure')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_departure(self):
        with app.test_client() as client:
            response = client.post('/add_departure', data=dict(
                type_of_service='testing',
                price_of_service='10',
                result='success',
                status_of_departure='in transit',
                To_Client_address_of_client='test_client',
                responsible='test_person'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM departure WHERE type_of_service ='testing'")
            departure = mycursor.fetchone()
            self.assertIsNotNone(departure)
    def test_edit_departure(self):
        with app.test_client() as client:
            response = client.post('/edit_departure/testing',
                                   data=dict(type_of_service='testing', price_of_service='15',
                                             result='success',
                                             status_of_departure='in transit',
                                             To_Client_address_of_client='test_client',
                                             responsible='test_person'))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM departure WHERE type_of_service ='testing'")
            departure = mycursor.fetchone()
            if departure is not None:
                self.assertEqual(departure[1], '15')
    def test_delete_departure(self):
        with app.test_client() as client:
            response = client.get('/delete_departure/test_client')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM departure WHERE type_of_service ='testing'")
            departure = mycursor.fetchone()
            self.assertIsNone(departure)
    def test_view_installation_and_deployment(self):
        with app.test_client() as client:
            response = client.get('/view_installation_and_deployment')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_installation_and_deployment(self):
        with app.test_client() as client:
            response = client.post('/add_installation_and_deployment', data=dict(
                date_of_installation='2023-01-01', type_of_installation='test_type_installation',
                status_of_installation='done', duration_time='0.05',
                result='successfull', Users_login_responsible_of_installation='test_responsible'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM installation_and_deployment WHERE Users_login_responsible_of_installation ='test_responsible'")
            installation_and_deployment = mycursor.fetchone()
            self.assertIsNotNone(installation_and_deployment)
    def test_edit_installation_and_deployment(self):
        with app.test_client() as client:
            response = client.post('/add_installation_and_deployment', data=dict(
                date_of_installation='2023-01-01', type_of_installation='test_type_installation',
                status_of_installation='wait', duration_time='0.05',
                result='successfull', Users_login_responsible_of_installation='test_responsible'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM installation_and_deployment WHERE Users_login_responsible_of_installation ='test_responsible'")
            installation_and_deployment = mycursor.fetchone()
            if installation_and_deployment is not None:
                self.assertEqual(installation_and_deployment[2], 'wait')
    def test_delete_installation_and_deployment(self):
        with app.test_client() as client:
            response = client.get('/delete_installation_and_deployment/test_responsible')
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM installation_and_deployment WHERE Users_login_responsible_of_installation ='test_responsible'")
            installation_and_deployment = mycursor.fetchone()
            self.assertIsNone(installation_and_deployment)
    def test_view_order_in_the_hall(self):
        with app.test_client() as client:
            response = client.get('/view_order_in_the_hall')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_order_in_the_hall(self):
        with app.test_client() as client:
            response = client.post('/add_order_in_the_hall', data=dict(
                date_of_order='2015-05-05', price_for_technique='200', quantity_of_technique='222',
                Client_name_of_client='testing_client',
                Technique_type_of_technique='typee_technique', Users_loginresponsible_for_order='test_resp_order'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM order_in_the_hall WHERE Users_loginresponsible_for_order ='test_resp_order'")
            order_in_the_hall = mycursor.fetchone()
            self.assertIsNotNone(order_in_the_hall)
    def test_edit_order_in_the_hall(self):
        with app.test_client() as client:
            response = client.post('/add_order_in_the_hall', data=dict(
                date_of_order='2015-05-05', price_for_technique='200', quantity_of_technique='222',
                Client_name_of_client='testing_client',
                Technique_type_of_technique='typee_technique', Users_loginresponsible_for_order='test_resp_order'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM order_in_the_hall WHERE Users_loginresponsible_for_order ='test_resp_order'")
            order_in_the_hall = mycursor.fetchone()
            if order_in_the_hall is not None:
                self.assertEqual(order_in_the_hall[3], 'testing_client')
    def test_delete_order_in_the_hall(self):
        with app.test_client() as client:
            response = client.get('/delete_order_in_the_hall/test_resp_order')
            self.assertEqual(response.status_code, 302)
            mycursor.execute(
                "SELECT * FROM order_in_the_hall WHERE Users_loginresponsible_for_order ='test_resp_order'")
            order_in_the_hall = mycursor.fetchone()
            self.assertIsNone(order_in_the_hall)
    def test_view_stock(self):
        with app.test_client() as client:
            response = client.get('/view_stock')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_stock(self):
        with app.test_client() as client:
            response = client.post('/add_stock', data=dict(
                address_of_stock='Severodvinsk', quantity_of_stuff='333', type_of_stock='typee_of_stock',
                number_phone_of_stock='353533',
                Users_login_responsible_of_stock='test_resp_stock_2'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM stock WHERE Users_login_responsible_of_stock ='test_resp_stock_2'")
            stock = mycursor.fetchone()
            self.assertIsNotNone(stock)
    def test_edit_stock(self):
        with app.test_client() as client:
            response = client.post('/add_stock', data=dict(
                address_of_stock='Severodvinsk', quantity_of_stuff='333', type_of_stock='typee_of_stock',
                number_phone_of_stock='353533',
                Users_login_responsible_of_stock='test_resp_stock_2'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM stock WHERE Users_login_responsible_of_stock ='test_resp_stock_2'")
            stock = mycursor.fetchone()
            if stock is not None:
                self.assertEqual(str(stock[1]), '333')
    def test_delete_stock(self):
        with app.test_client() as client:
            response = client.get('/delete_stock/test_resp_stock_2')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM stock WHERE Users_login_responsible_of_stock ='test_resp_stock_2'")
            stock = mycursor.fetchone()
            self.assertIsNone(stock)
    def test_view_service_department(self):
        with app.test_client() as client:
            response = client.get('/view_service_department')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_service_department(self):
        with app.test_client() as client:
            response = client.post('/add_service_department', data=dict(
                address_of_service_department='Serverodvinskk', quantity_stuff_in_service_department='222',
                number_phone_of_service_department='454555', post_code_of_service_department='151525'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM service_department WHERE post_code_of_service_department ='151525'")
            service_department = mycursor.fetchone()
            self.assertIsNotNone(service_department)
    def test_edit_service_department(self):
        with app.test_client() as client:
            response = client.post('/add_service_department', data=dict(
                address_of_service_department='Serverodvinskk', quantity_stuff_in_service_department='222',
                number_phone_of_service_department='454555', post_code_of_service_department='151525'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM service_department WHERE post_code_of_service_department ='151525'")
            service_department = mycursor.fetchone()
            if service_department is not None:
                self.assertEqual(str(service_department[2]), '454555')
    def test_delete_service_department(self):
        with app.test_client() as client:
            response = client.get('/delete_service_department/151525')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM service_department WHERE post_code_of_service_department ='151525'")
            service_department = mycursor.fetchone()
            self.assertIsNone(service_department)
    def test_view_purchase(self):
        with app.test_client() as client:
            response = client.get('/view_purchase')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_purchase(self):
        with app.test_client() as client:
            response = client.post('/add_purchase', data=dict(
                name_of_product='test_product', quantity_of_product='211', description_of_product='Testing_descript',
                factory_number='111', serial_number='313', purchase_amount='2113'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM purchase WHERE name_of_product ='test_product'")
            purchase = mycursor.fetchone()
            self.assertIsNotNone(purchase)
    def test_edit_purchase(self):
        with app.test_client() as client:
            response = client.post('/add_purchase', data=dict(
                name_of_product='test_product', quantity_of_product='211', description_of_product='Testing_descript',
                factory_number='111', serial_number='313', purchase_amount='2113'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM purchase WHERE name_of_product ='test_product'")
            purchase = mycursor.fetchone()
            if purchase is not None:
                self.assertEqual(str(purchase[1]), '211')
    def test_delete_purchase(self):
        with app.test_client() as client:
            response = client.get('/delete_purchase/test_product')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM purchase WHERE name_of_product ='test_product'")
            purchase = mycursor.fetchone()
            self.assertIsNone(purchase)
    def test_view_report_for_tax(self):
        with app.test_client() as client:
            response = client.get('/view_report_for_tax')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)
    def test_add_report_for_tax(self):
        with app.test_client() as client:
            response = client.post('/add_report_for_tax', data=dict(
                    date_of_formation_report='2022-01-11', date_of_sendig_report='2022-02-11', signature='test_sign', to_tax='test_to_tax', from_company='test_company',
                    content_of_report='test_contnet', type_of_delivery_report='test_type_delivery', Users_login_responsible_for_the_report='test_resp_report'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM report_for_tax WHERE Users_login_responsible_for_the_report ='test_resp_report'")
            report_for_tax = mycursor.fetchone()
            self.assertIsNotNone(report_for_tax)
    def test_edit_report_for_tax(self):
        with app.test_client() as client:
            response = client.post('/add_report_for_tax', data=dict(
                        date_of_formation_report='2022-01-12', date_of_sendig_report='2022-02-11', signature='test_sign', to_tax='test_to_tax', from_company='test_company',
                        content_of_report='test_contnet', type_of_delivery_report='test_type_delivery', Users_login_responsible_for_the_report='test_resp_report'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM report_for_tax WHERE Users_login_responsible_for_the_report ='test_resp_report'")
            report_for_tax = mycursor.fetchone()
            if report_for_tax is not None:
                self.assertEqual(report_for_tax[2], 'test_sign')
    def test_delete_report_for_tax(self):
        with app.test_client() as client:
            response = client.get('/delete_report_for_tax/test_company')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM report_for_tax WHERE Users_login_responsible_for_the_report ='test_resp_report'")
            report_for_tax = mycursor.fetchone()
            self.assertIsNone(report_for_tax)

    def test_view_dealer(self):
        with app.test_client() as client:
            response = client.get('/view_dealer')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(response.data), 0)

    def test_add_dealer(self):
        with app.test_client() as client:
            response = client.post('/add_dealer', data=dict(
                    name_of_dealer='test_dealer', address_of_dealer='test_address', type_of_services_from_dealer='type_of_dealer',
                    payment_to_the_dealer='2521', date_of_contract_with_dealer='2022-01-01', number_of_dealer='252525'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM dealer WHERE name_of_dealer ='test_dealer'")
            dealer = mycursor.fetchone()
            self.assertIsNotNone(dealer)

    def test_edit_dealer(self):
        with app.test_client() as client:
            response = client.post('/add_dealer', data=dict(
                        name_of_dealer='test_dealer', address_of_dealer='test_address', type_of_services_from_dealer='type_of_dealer',
                        payment_to_the_dealer='2521', date_of_contract_with_dealer='2022-01-01', number_of_dealer='252525'
            ))
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM dealer WHERE name_of_dealer ='test_dealer'")
            dealer = mycursor.fetchone()
            if dealer is not None:
                self.assertEqual(dealer[2], 'type_of_dealer')

    def test_delete_dealer(self):
        with app.test_client() as client:
            response = client.get('/delete_dealer/test_dealer')
            self.assertEqual(response.status_code, 302)
            mycursor.execute("SELECT * FROM dealer WHERE name_of_dealer ='test_dealer'")
            dealer = mycursor.fetchone()
            self.assertIsNone(dealer)


if __name__ == '__main__':
    unittest.main()