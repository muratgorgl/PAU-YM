#include <iostream>

using namespace std;

int main()
{
/* 
    int index = 0;
    while (true)
    {
        cout << "index degeri " << index << endl;
        index++;
    }
    cout << "Toplan index sayisi: " << index << endl;
*/   

    int baslangic, bitis;
    cout << "Baslangic degerini giriniz: ";
    cin >> baslangic;
    cout << "Bitis degerini giriniz: ";
    cin >> bitis;
    while (baslangic <= bitis)
    {
        if (baslangic % 7 ==0)
        {
            cout << "baslangic degeri: " << baslangic << endl;
        }
        
        baslangic++;
    }
    return 0;
}