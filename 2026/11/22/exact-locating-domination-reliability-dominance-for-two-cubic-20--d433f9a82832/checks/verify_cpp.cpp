// Complete exact location-domination census; no external graph or data files.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
using Mask = unsigned;
constexpr int n=20;
constexpr Mask ALL=(1u<<n)-1;

array<Mask,n> desargues(){
 array<Mask,n> adj{};
 vector<unsigned> e;
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)e.push_back((1u<<i)|(1u<<j));
 assert(e.size()==10);
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)if((e[i]&e[j])==0){
  adj[i]|=1u<<(10+j);adj[10+j]|=1u<<i;
 }
 return adj;
}
array<Mask,n> dodeca(){
 array<Mask,n> adj{};
 auto link=[&](int u,int v){adj[u]|=1u<<v;adj[v]|=1u<<u;};
 for(int i=0;i<10;i++){link(i,(i+1)%10);link(i,10+i);link(10+i,10+(i+2)%10);}
 return adj;
}
bool valid(Mask S,const array<Mask,n>& A){
 Mask U=ALL^S;
 Mask signatures[20];int m=0;
 while(U){
  int v=__builtin_ctz(U);U&=U-1;
  Mask sig=A[v]&S;
  if(!sig)return false;
  for(int j=0;j<m;j++)if(signatures[j]==sig)return false;
  signatures[m++]=sig;
 }
 return true;
}
array<unsigned long long,21> spectrum(const array<Mask,n>& A){
 for(int v=0;v<n;v++){
  assert(__builtin_popcount(A[v])==3);
  for(int w=0;w<n;w++) assert(((A[v]>>w)&1u)==((A[w]>>v)&1u));
 }
 array<unsigned long long,21> C{};
 for(Mask S=0;S<=ALL;S++)if(valid(S,A))C[__builtin_popcount(S)]++;
 return C;
}
void print(const char* name,const array<unsigned long long,21>& a){
 cout<<name<<":";for(auto x:a)cout<<" "<<x;cout<<"\n";
}
int main(){
 constexpr array<unsigned long long,21> de={0,0,0,0,0,0,0,0,1475,15100,49826,83840,88890,66020,36330,15184,4825,1140,190,20,1};
 constexpr array<unsigned long long,21> do_={0,0,0,0,0,0,0,220,3935,21760,57054,87720,89940,66140,36330,15184,4825,1140,190,20,1};
 auto a=spectrum(desargues()),b=spectrum(dodeca());
 print("DESARGUES",a);print("DODECAHEDRON",b);
 assert(a==de && b==do_);
 for(int i=0;i<21;i++)assert(b[i]>=a[i]);
 for(int i=0;i<7;i++)assert(b[i]==a[i]);
 for(int i=7;i<=13;i++)assert(b[i]>a[i]);
 for(int i=14;i<21;i++)assert(b[i]==a[i]);
 cout<<"CPP_EXACT_PASS\n";
}
