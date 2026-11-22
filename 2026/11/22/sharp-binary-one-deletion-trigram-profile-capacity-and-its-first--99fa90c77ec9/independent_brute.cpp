// Direct deletion-and-recount verifier, independent of neighborhood-class DP.
// Compile: g++ -O2 -std=c++17 independent_brute.cpp -o independent_brute
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
using namespace std;
using H=array<int,8>;
H profile(const string &s){
 H h{};
 for(size_t j=2;j<s.size();++j){
  unsigned k=4*(s[j-2]-'0')+2*(s[j-1]-'0')+(s[j]-'0');
  ++h[k];
 }
 return h;
}
unsigned sphere(const string &w){
 set<H> got;
 for(size_t i=0;i<w.size();++i){
  string del=w.substr(0,i)+w.substr(i+1);
  got.insert(profile(del));
 }
 return got.size();
}
int main(){
 for(unsigned n=1;n<=19;++n){
  unsigned mx=0;unsigned cnt=0;
  for(uint32_t x=0;x<(1u<<n);++x){
   string w(n,'0');
   for(unsigned j=0;j<n;++j)w[j]=(x>>(n-1-j)&1)?'1':'0';
   unsigned s=sphere(w);
   if(s>mx){mx=s;cnt=1;}else if(s==mx){++cnt;}
  }
  cout<<"n="<<n<<" max="<<mx<<" extremizers="<<cnt<<"\n";
  if(n<20)assert(mx<14);
 }
 for(unsigned t=0;t<=10;++t){
  string w="01"+string(3+t,'0')+"100101011011101";
  assert(sphere(w)==14);
 }
 cout<<"family 20..30: PASS\n";
}
