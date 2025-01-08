#include <bits/stdc++.h>
using namespace std;

vector<int> v; 

int fib(int n)
{
    if (v.size() < n + 1) v.resize(n+1,-1);
    if (n <= 2) 
    {
        return 1;
    }
    if (v[n] != -1) 
    {
        return v[n];
    }
    v[n] = fib(n - 1) + fib(n - 2);
    return v[n];
}

int main()
{
    int n;
    cin >> n;
    cout << fib(n) << endl;
    return 0;
}
