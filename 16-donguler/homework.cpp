#include <iostream>

using namespace std;

int main()
{
    int input;
    cout << "Lutfen bir sayi giriniz:";
    cin >> input;
    for(int i =1; i<=input; i++)
    {
        for (int j = 1; j<=i; j++)
        {
            cout << i << " ";
        }
        cout << endl;
    }
}