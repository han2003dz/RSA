#include <iostream>
using namespace std;

string Z26(){
	string x = "";
	for(int i = 0; i < 26; i++){
		x+= char(65 + i);
		
	} 
	return x; 
} 
// bình phuong và nhân 
long equare_and_mul(long x, long n, long m){
	if(n == 0){
		return 1; 
	}else{
		long p = equare_and_mul(x, n / 2, m);
		if(n % 2 == 0){
			return (p * p) % m; 
		}else{
			return p * p * x % m;
		} 
	} 
} 

long inverse(long a, long b){
	long b0 = b, t, q;
	long x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a < 0) a += b;
	while (a > 1) {
		q = (long)a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
} 

string MaHoaAffine(string x, int a, int b) {
	string z = Z26();
	string y = "";
	for (int i = 0; i < x.length(); i++) {
		x[i] = toupper(x[i]);
	}
	for (int i = 0; i < x.length(); i++) {
		int j = (a*(int(x[i])-65)+b)%26;
		y += z[j];
	}
	return y;
}

string GiaMaAffine(string x, int a, int b) {
	int a_1 = timNghichDao(a, 26);
	string z = Z26();
	string y = "";
	for (int i = 0; i < x.length(); i++) {
		x[i] = toupper(x[i]);
	}
	for (int i = 0; i < x.length(); i++) {
		int j = (a_1 * ((int(x[i]) - 65) - b+26)) % 26;
		y += z[j];
	}
	return y;
}



int main(){
	
} 
