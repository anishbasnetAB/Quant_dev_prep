#include <iostream>
#include <string>

int main(){

    std::string full_Name;
    int age;

    std::cout<<"Enter your full name and age "<<std::endl;
    std::getline(std::cin,full_Name);
    std::cin>>age;

    std::cout<<"Your name is "<<full_Name<<" and your age is "<<age;
}