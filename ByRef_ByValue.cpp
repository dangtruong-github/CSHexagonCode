#include <iostream>

using namespace std;

void plusByRef(int &a) {
    a = a + 1;
};

// By value
void plusByValue(int a) {
    a = a + 1;
};

int main() {
    cout << "\n\n";
    int a = 4;

    cout << "Initial value of a: " << a << endl;

    plusByValue(a);

    cout << "Value of a after plusByValue: " << a << endl;

    // plusByRef(a);

    // cout << "Value of a after plusByRef: " << a << endl;
}