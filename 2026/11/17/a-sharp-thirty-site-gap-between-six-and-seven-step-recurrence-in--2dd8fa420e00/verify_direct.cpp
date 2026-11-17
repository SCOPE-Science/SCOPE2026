// Independent finite-state verification for Rule 110; standard C++17.
#include <cstdint>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;
uint32_t step(uint32_t x,int n) {
 uint32_t z=0;
 for(int i=0;i<n;i++) {
  int a=(x>>((i+n-1)%n))&1,b=(x>>i)&1,c=(x>>((i+1)%n))&1;
  z|=uint32_t((110>>((a<<2)|(b<<1)|c))&1)<<i;
 }
 return z;
}
int main(){
 map<int,uint32_t> want7={{9,64},{11,78},{14,15},{17,120},{18,64},{20,421}};
 for(int n=3;n<=20;n++){
  uint32_t total=1u<<n,fix1=0,fix6=0,fix7=0;
  for(uint32_t x=0;x<total;x++){
   uint32_t y=x;
   for(int k=1;k<=7;k++){
    y=step(y,n);
    if(k==1&&y==x)fix1++;
    if(k==6&&y==x)fix6++;
    if(k==7&&y==x)fix7++;
   }
  }
  uint32_t expected7=want7.count(n)?want7[n]:1;
  assert(fix1==1);
  assert(fix7==expected7);
  // For sixth return all initial states have period 1,2,or3;
  // thus no genuine period 6: for every state fixed by F^6,
  // it must be fixed by F^2 or F^3. Tested in independent loop below.
  uint32_t union23=0;
  for(uint32_t x=0;x<total;x++){
    uint32_t y=x; bool f2=false,f3=false;
    for(int k=1;k<=3;k++){
      y=step(y,n);
      if(k==2&&y==x)f2=true;
      if(k==3&&y==x)f3=true;
    }
    union23+=(f2||f3);
  }
  assert(fix6==union23);
  cout<<"n="<<n<<" fix7="<<fix7<<" period7_orbits="<<(fix7-1)/7
      <<" fix6="<<fix6<<" PASS\n";
 }
 cout<<"PASS independent direct enumeration: all labelled binary rings n=3..20.\n";
}
