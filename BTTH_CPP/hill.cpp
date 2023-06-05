#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

//chuyen tu ki tu sang mang
void getKeyMatrix(string key, int keyMatrix[][3]){
	int k = 0;
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			keyMatrix[i][j] = key[k] % 65;
			k++;
		}
	}
}

void encrypt(int keyMatrix[][3], int messageVector[][1], int cipherMatrix[][1]){
	for(int i = 0; i < 3; i++){
	
		for(int j = 0; j < 1; j++){
			cipherMatrix[i][j] = 0;
			for(int x = 0; x < 3; x++){
				cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j];
			}
			cipherMatrix[i][j] %= 26;	
		}
	}
}

void HillCipher(string message, string key){
	int keyMatrix[3][3];
	getKeyMatrix(key, keyMatrix);
	int messageVector[3][1];
	for(int i = 0; i < 3; i++){
		messageVector[i][0] = message[i] % 65; 
	}
	int cipherMatrix[3][1];
	encrypt(keyMatrix, messageVector, cipherMatrix);
	string CipherText;
	for(int i = 0; i < 3; i++){
		CipherText += cipherMatrix[i][0] + 65; 
	} 
	cout << "Ciphertext: " << CipherText; 
} 
int main(){
	string message = "ACT"; 
	string key = "GYBNQKURP";
	HillCipher(message, key);
	return 0;
}

