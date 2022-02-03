# econsular-availability-reader-lisbon

It access `https://ec-lisboa.itamaraty.gov.br/availability` page (credentials needed) and find whether a service has appointment available or not

How to use it:
1. Clone the repository
2. Go to the porject directiory
3. Run `py econsular.py '<service_name>' <email> <password>`

Notes:
* `<service_name>`: Replace it by the service name you want to schedule, e.g: 'CNH - Declaração'. It must be the same name that apears in the <i>ec-lisboa.itamaraty.gov.br/availability</i> page.
* `<email>`: Enter your email registered in the econsular portal
* `<passwprd>`: Enter your password
