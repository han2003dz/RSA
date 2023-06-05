
#include <iostream>
#include <string>
using namespace std;

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
    int x, i, j;
    for(i = 0; i < 3; i++){
        for(j = 0; j < 1; j++){
            cipherMatrix[i][j] = 0;
            for(x = 0; x < 3; x++){
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j];
            }
            cipherMatrix[i][j] %= 26; 
        }
    }
}

string HillCipher(string message, string key){
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
    return CipherText;

}

string input(){
    string cipher;
    cout << "Nhap chuoi: ";
    getline(cin, cipher);
    return cipher;
}

int main(){
    string message = "ACT";
    string mess = input();
    string key = "GYBNQKURP";
	if (mess == HillCipher(message, key)){
		cout << "OK"; 
	}else {
		cout << "!Ok"; 
	} 

    return 0;
}


































