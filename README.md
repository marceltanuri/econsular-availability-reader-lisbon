# econsular-availability-reader-lisbon

It access `https://ec-lisboa.itamaraty.gov.br/availability` page (credentials needed) and find whether a service has appointment available or not

How to use it:
1. Clone the repository
2. Go to the porject directiory
3. Run `py econsular.py '<service_name>' <email> <password>`

Notes:
* `<service_name>`: Replace it by the service name you want to schedule, e.g: 'CNH - Declaração'. It must be the same name that apears in the <i>ec-lisboa.itamaraty.gov.br/availability</i> page.
* `<email>`: Enter your email registered in the econsular portal
* `<password>`: Enter your password

4. The program will keep in looping with 60 secounds interval.
5. A ring sound will be played whenever the service was found available <i>(Only for Windows)</i>
