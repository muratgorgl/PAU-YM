#include <iostream>

using namespace std;

int main()
{
    int input;
    int faktoriyel = 1;
    cout << "Lutfen bir sayi giriniz:";
    cin >> input;

    for (int i=input; i>0; i--)
    {
        faktoriyel *= i;

    }
    cout << input << " sayisinin faktoriyeli: " << faktoriyel << endl;
    

    

    
    
}