// Exact direct arithmetic check for online unit-chore proportionality.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_independent.cpp -o verify_cpp && ./verify_cpp
#include <array>
#include <cassert>
#include <iostream>
using A=std::array<int,4>;
long long cases=0, tested_steps=0;
int countbits(int x){int c=0;while(x){c+=x&1;x>>=1;}return c;}
void test(A load,A proportional,int depth){
 ++cases;
 if(depth==4) return;
 for(int mask=1;mask<16;mask++){
  int k=countbits(mask);
  A p=proportional;
  for(int i=0;i<4;i++) if(mask&(1<<i))p[i]+=12/k;
  int recipient=-1;
  for(int i=0;i<4;i++)if(mask&(1<<i)){
    if(recipient<0 || 12*load[i]-proportional[i] <
       12*load[recipient]-proportional[recipient]) recipient=i;
  }
  assert(recipient>=0);
  A l=load;l[recipient]++;
  for(int i=0;i<4;i++){
    assert(l[i]==0 || 12*(l[i]-1)<=p[i]);
  }
  ++tested_steps;
  test(l,p,depth+1);
 }
}
int main(){test({0,0,0,0},{0,0,0,0},0);
 assert(cases==54241);
 assert(tested_steps==54240);
 std::cout<<"Direct all-eligibility 4-job prefixes checked: "<<cases<<"; allocation transitions: "<<tested_steps<<"\n";
 return 0;
}
