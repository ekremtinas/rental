# rental
drone rental


"/admin" //Admin girişi içerisinde iha,iha marka,iha kategori,iha model iha kiralama,users gibi bir çok tablonun eklenmesi listelenmesi ve güncellenmesi mevcuttur.
"/account/login" //Kullanıcı girişi
"/account/register" //Kullanıcı kaydı

"/" //Anasayfa filtreleme işlemlerinin yapıldığı yer
"/my-rentals" //Kiralanma durumları 


python3 manage.py makemigrations  //migrasyoın oluşturulması

python3 manage.py migrate //migrasyonların postgres'e işlenmesi

python3 manage.py runserver //program başlatılması

python3 manage.py createsuperuser //admin ekleyebilirsiniz

