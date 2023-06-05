#include <iostream>
#include <bits/stdc++.h > 
using namespace std;

int gcd(int a, int m){
	if(m == 0){
		return a; 
	} 
	return gcd(m, a % m); 
} 

bool check(int a, int m){
	int result = gcd(a, m);
	return result == 1; 
}

int findInverse(int a, int b) { //a^-1 mod b
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a < 0) a += b;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}


int main(){
	int a, m, b;
	cout << "Nhap a: ";
	cin >> a; 
	cout << "Nhap m: ";
	cin >> m;
	cout << "Nhap b: ";
	cin >> b; 
	
	if(check(a, m)){
		cout << "Ok";
		cout << "(" << findInverse(a, m) << ", " << b << ")";  
	}else{
		cout << "!Ok"; 
	}	 
	return 0; 
} 
