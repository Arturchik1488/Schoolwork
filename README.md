Šī ir Flask bāzēta tīmekļa aplikācija, kas nodrošina lietotāju autentifikāciju un piekļuves kontroli, balstoties uz lomām. Kods ir strukturēts moduļos, dalot funkcionalitāti specifiskos failos.

Pamata faili un to funkcijas:

1. app.py
Šis fails iestatīs Flask aplikāciju un tās paplašinājumus:
Importē nepieciešamās Flask bibliotēkas un moduļus
Konfigurē žurnālu pierakstīšanu problēmu risināšanai
Izveido pielāgotu SQLAlchemy bāzes klasi datu bāzes modeļiem
Inicializē Flask paplašinājumus (SQLAlchemy datu bāzes apstrādei un Bcrypt paroles šifrēšanai)
Konfigurē datu bāzes savienojumu, izmantojot vides mainīgos
Iestata noslēpumta atslēgu sesiju pārvaldībai
Izveido datu bāzes tabulas, kad aplikācija tiek uzsākta

2. models.py
Definē datu bāzes modeli lietotājiem:
Satur vienu User klasi, kas manto no SQLAlchemy Model
Ietver laukus lietotāja ID, lietotājvārdu, e-pastu, paroli (uzglabātu kā hashu) un lomu
Lomas lauks nosaka, vai lietotājs ir parastais lietotājs vai administrators
Ietver reprezentācijas metodi, kas paredzēta atkļūdošanai/žurnālu rakstīšanai

3. forms.py
Izveido formu klases, izmantojot Flask-WTF lietotāja ievades apstrādei:
RegistrationForm: Iegūst lietotājvārdu, e-pastu, paroli un paroles apstiprinājumu
Ietver validāciju, lai pārbaudītu lietotājvārda/e-pasta unikālumu
Ietver validatorus datu esamībai, garuma prasībām un e-pasta formātam
LoginForm: Parastajam lietotājam paredzēta pieteikšanās forma ar e-pasta un paroles laukiem
AdminLoginForm: Speciāla forma administratori pieteikšanās ar lietotājvārdu, nevis e-pastu

4. routes.py
Satur visas aplikācijas maršrutus un skatījumu funkcijas:
Home route: Sākuma lapa
Registration route: Jauna lietotāja reģistrācijas maršruts
Login route: Lietotāja autentifikācija
Logout route: Sesijas datu dzēšana
Dashboard route: Piekļuve apstiprinātajiem lietotājiem
Admin login route: Speciāla administratora autentifikācija
Pielāgotie dekoratori pieteikšanās un administratora piekļuves kontrolei
Kļūdu apstrāde 404 lapas atrastās kļūdas gadījumā
Komandu rindiņas interfeiss administratora lietotāju izveidošanai

5. create_admin.py
Palīgskripts, lai izveidotu noklusējuma administratora lietotāju:
Definē noklusējuma administratoru ar lietotājvārdu "admin", e-pastu "admin@example.com" un paroli "adminpass123"
Pārbauda, vai administrators jau eksistē, pirms izveidošanu
Šifrē paroli, izmantojot Bcrypt
Pievieno administratora lietotāju datu bāzē ar lomu "admin"

6. main.py
Vienkāršs ieejas punkts, kas palaiž Flask aplikāciju:
Importē aplikāciju no app.py
Palaid Flask izstrādes serveri uz hosta 0.0.0.0 un portu 5000 ar ieslēgtu atkļūdošanas režīmu

Šablonu faili
Aplikācija ietver vairākus HTML šablonus, izmantojot Jinja2:
layout.html: Pamatšablons ar vietnes navigāciju un struktūru
home.html: Sākuma lapa ar ievadu un pieteikšanās/reģistrēšanās saitēm
register.html: Lietotāja reģistrācijas forma
login.html: Parastā lietotāja pieteikšanās forma ar saiti uz administratora pieteikšanās formu
admin_login.html: Speciāla forma administratora pieteikšanās
dashboard.html: Droša zona, kas parāda lietotāja informāciju pēc autentifikācijas
404.html: Pielāgota kļūdu lapa neeksistējošiem maršrutiem

Autentifikācijas plūsma
Jauni lietotāji reģistrējas, izmantojot reģistrācijas formu
Reģistrācija izveido jaunu lietotāja ierakstu ar šifrētu paroli
Lietotāji autentificējas, izmantojot pieteikšanās formu ar e-pasta un paroles laukiem
Administratora lietotāji autentificējas ar atsevišķu administrātora pieteikšanās formu, izmantojot lietotājvārdu
Veiksmīga autentifikācija iestata sesijas mainīgos (user_id un role)
Piekļuve dashboard ir aizsargāta ar login_required dekoratoru
Administratora funkcijas ir aizsargātas ar admin_required dekoratoru

Datu bāzes integrācija
Izmanto SQLAlchemy ORM datu bāzes operācijām
Savienojas ar PostgreSQL datu bāzi, kuru norāda vides mainīgie
Automātiski izveido tabulas aplikācijas palaišanas laikā
Veic validāciju pirms datu bāzes operācijām

Drošības funkcijas
Paroles šifrēšana ar Bcrypt, nevis uzglabājot nešifrētas paroles
Sesiju balstīta autentifikācija
Lomu balstīta piekļuves kontrole
Formu validācija ar CSRF aizsardzību
Pielāgotie dekoratori maršrutu aizsardzībai
Atsevišķa administratora pieteikšanās mehānisms

Stilizācija
Izmanto Bootstrap CSS ietvaru ar tumšo tēmu
Responsīvs dizains dažādiem ekrāna izmēriem
Pielāgota stilistika formu elementiem un pogām
Font Awesome ikonas vizuālai uzlabošanai

Iestrādes konfigurācija
Konfigurēts darbam ar Gunicorn tīmekļa serveri
Saista visus tīkla interfeisus (0.0.0.0) uz 5000. portu
Ietver vides mainīgo integrāciju datu bāzes savienojumam

Šī ir visaptveroša, bet modulāra autentifikācijas sistēma, kas var kalpot kā pamats lielākām aplikācijām, kas prasa lietotāju pārvaldību un piekļuves kontroli.

Admina pieslēgšanās dati:
Username - Admin
Email - admin@example.com
Password - adminpass123
