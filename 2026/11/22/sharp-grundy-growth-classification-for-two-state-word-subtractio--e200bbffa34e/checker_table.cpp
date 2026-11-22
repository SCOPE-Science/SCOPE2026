// Standalone exhaustive check for all 16 labeled binary two-state DFA tables.
// C++17: g++ -O2 -std=c++17 checker_table.cpp -o checker_table && ./checker_table
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
 const array<array<int,2>,4> fs {{{0,0},{0,1},{1,0},{1,1}}}; // Z,I,T,O
 uint64_t tested=0;
 for(int a=0;a<4;++a)for(int b=0;b<4;++b){
  vector<vector<int>> G(17);
  G[0]={0};
  for(int n=1;n<=16;++n){
   G[n].resize(1<<n);
   int maximum=0;
   for(int word=0;word<(1<<n);++word){
    uint32_t options=0;
    for(int cut=0;cut<n;++cut){
     int state=0;
     for(int j=cut;j<n;++j){
      const int symbol=(word>>(n-j-1))&1;
      state=fs[symbol?b:a][state];
     }
     if(state==1){
      const int prefix=(word>>(n-cut)) & ((1<<cut)-1);
      const int g=G[cut][prefix];
      options|=(1u<<g);
     }
    }
    int g=0;
    while(options&(1u<<g))++g;
    G[n][word]=g;
    int expected=-1;
    if(a!=3 && b!=3){
      int types[16];
      for(int j=0;j<n;++j)types[j]=((word>>(n-j-1))&1)?b:a;
      if(a!=2 && b!=2)expected=0;
      else if(a!=0 && b!=0){
       int parity=0;
       for(int j=0;j<n;++j)parity^=(types[j]==2);
       expected=parity;
      }else{
       int segments=0, seenT=0, parity=0;
       for(int j=0;j<n;++j){
        if(types[j]==0){segments+=seenT;seenT=0;parity=0;}
        else if(types[j]==2){seenT=1;parity^=1;}
       }
       expected=parity ? segments+seenT : 0;
      }
     }
     if(expected>=0 && g!=expected)throw runtime_error("pointwise formula mismatch");
     maximum=max(maximum,g);++tested;
   }
   int expectedmax;
   if(a==3 || b==3)expectedmax=n;
   else if((a==0&&b==2)||(a==2&&b==0))expectedmax=(n+1)/2;
   else if((a==1&&b==2)||(a==2&&b==1))expectedmax=1;
   else if(a==2&&b==2)expectedmax=n%2;
   else expectedmax=0;
   if(maximum!=expectedmax)throw runtime_error("maximum formula mismatch");
  }
 }
 cout<<"PASS: 16 binary transition tables, lengths 1..16; words checked: "<<tested<<"\n";
}
