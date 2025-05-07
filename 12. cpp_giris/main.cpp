#include <iostream>
#include <iomanip>

using namespace std;

int main(){

/* 
    string isim = "Murat";
    int dogumYili=2000;
    float pi = 3.14f;
    double pi2 = 3.14159848568564156;
    bool sinifiGectiMi = true;
    char karakter = 'A';
    int quizNot1 = 72;
    float quizNot2 = 85.f;
    // float quizNotOrtalamasi = (float)(quizNot1 + quizNot2) / 2;
    float quizNotOrtalamasi = (quizNot1 + quizNot2) / 2;
 
    cout << "Isim: " << isim << endl;
    cout << "Dogum Yili: " << dogumYili << endl;
    cout << "Pi: " << pi << endl;
    cout << "Pi2: " << pi2 << endl;
    cout << "Sinifi Gecti Mi: " << sinifiGectiMi << endl;
    cout << "Karakter: " << karakter << endl;
    cout << "Quiz Not Ortalamasi: " << quizNotOrtalamasi << endl;
    return 0; 
*/

/* 
   int x = 20;
   int y = 12;
   int z=x % y;
   cout << z << endl;
   return 0; 
*/
    double deger = 123.456789;

    // toplam kaç karakter yazdırılacak
    cout << setprecision(2) << deger << endl;
    // virgülden sonra kaç basamak yazdırılacak
    cout << fixed << setprecision(2) << deger << endl;

}