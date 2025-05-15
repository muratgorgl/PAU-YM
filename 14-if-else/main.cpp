#include <iostream>

using namespace std;

int main()
{
    /* 
    int sicaklik = 40;

    if (sicaklik >=35)
    {
        cout << "Hava cok sicak" << endl;
    }
    else
    {
        cout << "Hava sicak degil" << endl;
    }
  */

 /* 
    int sifre = 1234;
    int kullaiciInput;
    cout << "Lutfen sifrenizi giriniz: ";
    cin >> kullaiciInput;

    if (sifre == kullaiciInput)
    {
        cout << "Sifre dogru" << endl;
    }
    else
    {
        cout << "Sifre yanlis" << endl;
    }
  */   
    int sayi1, sayi2, sonuc;
    int yapilacakIslem;
    cout << "Lutfen 1. sayiyi giriniz: ";
    cin >> sayi1;
    cout << "Lutfen 2. sayiyi giriniz: ";
    cin >> sayi2;
    cout << "Lutfen yapilacak islemi seciniz: (1-Toplama, 2-Cikarma, 3-Carpma, 4-Bolme)" << endl;
    cin >> yapilacakIslem;

    if (yapilacakIslem==1)
    {
        sonuc = sayi1 + sayi2;
        cout << "Sonuc: " << sonuc << endl;
    }
    else if (yapilacakIslem==2)
    {
        sonuc = sayi1 - sayi2;
        cout << "Sonuc: " << sonuc << endl;
    }
    else if (yapilacakIslem==3)
    {
        sonuc = sayi1 * sayi2;
        cout << "Sonuc: " << sonuc << endl;
    }
    else if (yapilacakIslem==4)
    {
        sonuc = sayi1 / sayi2;
        cout << "Sonuc: " << sonuc << endl;
    }
    else
    {
        cout << "Gecersiz islem" << endl;
    }
    




    return 0;
}