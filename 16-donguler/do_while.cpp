#include <iostream>

using namespace std;

int main()
{
    int sifre =1234;
    int input;
    do
    {   cout << "Lutfen sifrenizi giriniz:";
        cin >> input;

    } while(input != sifre);

    cout << "Skynet'e hosgeldiniz!" << endl;

    return 0;

}