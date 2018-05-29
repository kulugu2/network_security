#include<stdio.h>
#include<unistd.h>
using namespace std;

int main(){
    char buf[8];
    read(0,&buf, 8);
    printf("%s", buf);
}
