#include <iostream>

using namespace std;

int main()
{
    int sayi1, sayi2, sayi3;
    cout << "1. sayiyi giriniz: ";
    cin >> sayi1;
    cout << "2. sayiyi giriniz: ";
    cin >> sayi2;
    cout << "3. sayiyi giriniz: ";
    cin >> sayi3;
    int enKucuk;
    
    if ((sayi1 < sayi2) && (sayi1 <sayi3))
    {
        enKucuk = sayi1;
    }
    else if ((sayi2 < sayi1) && (sayi2 < sayi3))
    {
        enKucuk = sayi2;
    }
    else if ((sayi3 < sayi1) && (sayi3 < sayi2))
    {
        enKucuk = sayi3;
    }

    cout << "En kucuk sayi: " << enKucuk << endl;
    
    return 0;

}