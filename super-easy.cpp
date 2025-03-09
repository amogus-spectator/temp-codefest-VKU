#include <iostream>

using namespace std;

float calculateArea(int& a) {
    float f = float(((a * a)) / 4.0);
    return f;
}

int main() {
    int n;
    cin >> n;
    try {
        if ((n <= 0) || (n > 1000)) {
            throw 0;
        } else {
            cout << calculateArea(n) << endl;
        }
    } catch (int error) {
        cout << "Invalid input" << endl;
        return 1;
    }
    return 0;
}