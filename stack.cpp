#include <iostream>

using namespace std;

const int MAX = 10;
int stack_arr[MAX];
int top = -1;

void push(int data);
int pop();
void peek();
bool isEmpty();

int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    peek();
    cout << stack_arr[0] << endl;
    cout << isEmpty() << endl;
    return 0;
}

void push(int data){
    if (top == MAX - 1){
        cout << "STACK OVERFLOW!" << endl;
    }
    top++;
    stack_arr[top] = data;
}

int pop(){
    if (top == -1){
        cout << "STACK UNDERFLOW" << endl;
    }
    int popped = stack_arr[top];
    stack_arr[top] = 99999;
    top--;
    return popped;
}

void peek(){
    cout << stack_arr[top] << endl;
}

bool isEmpty(){
    if (top == -1){
        return true;
    }
    return false;
}
