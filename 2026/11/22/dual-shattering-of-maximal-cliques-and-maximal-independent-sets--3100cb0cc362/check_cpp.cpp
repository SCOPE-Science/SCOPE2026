// Standalone full 16-bit exhaustive verification of four membership concept families.
// Compile: g++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
using U=uint32_t;
using U128=unsigned __int128;
constexpr int N=16;
int pc(U x){return __builtin_popcount(x);}
int index(int i,int j){return 4*((i+4)%4)+(j+4)%4;}
array<U,N> graph(bool rook){
  array<U,N>a{};
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){
    int r=i/4,c=i%4,s=j/4,t=j%4;
    bool edge=rook?(r==s||c==t):(((r-s+4)%4==1&&(c-t+4)%4==0)||((r-s+4)%4==3&&(c-t+4)%4==0)||((r-s+4)%4==0&&(c-t+4)%4==1)||((r-s+4)%4==0&&(c-t+4)%4==3)||((r-s+4)%4==1&&(c-t+4)%4==1)||((r-s+4)%4==3&&(c-t+4)%4==3));
    if(edge)a[i]|=(U(1)<<j);
  }
  return a;
}
vector<U> maximal_independent(const array<U,N>& a){
  vector<U> res;
  for(U s=1;s<(U(1)<<N);s++){
    bool ind=true; U covered=s;
    for(int i=0;i<N;i++) if(s>>i&1){
      if(a[i]&s){ind=false;break;}
      covered|=a[i];
    }
    if(ind&&covered==65535)res.push_back(s);
  }
  return res;
}
vector<U> all_shattered(const vector<U>& concepts){
 vector<U> out;
 for(U s=0;s<65536;s++){
  int k=pc(s);if(k>4)continue;
  U chosen[4]{};int j=0;
  for(int v=0;v<N;v++)if(s>>v&1)chosen[j++]=U(1)<<v;
  bool seen[16]{};int n=0;
  for(U c:concepts){int trace=0;for(int v=0;v<k;v++)if(c&chosen[v])trace|=1<<v;
   if(!seen[trace]){seen[trace]=true;n++;}
  }
  if(n==(1<<k))out.push_back(s);
 }
 return out;
}
array<int,5> fvector(const vector<U>& faces){array<int,5>a{};for(U f:faces)a[pc(f)]++;return a;}
int rank128(const vector<U128>& columns){
 array<U128,128> piv{};int r=0;
 for(U128 x:columns)while(x){int bit=0;for(int b=127;b>=0;b--)if(x>>b&1){bit=b;break;}
  if(!piv[bit]){piv[bit]=x;r++;break;}
  x^=piv[bit];
 }
 return r;
}
int boundary_rank(const vector<U>& faces,int size){
 vector<U> lo,hi;
 for(U f:faces)if(pc(f)==size-1)lo.push_back(f);else if(pc(f)==size)hi.push_back(f);
 assert(lo.size()<=128);
 map<U,int> ids;for(int i=0;i<(int)lo.size();i++)ids[lo[i]]=i;
 vector<U128> cols;
 for(U f:hi){U128 x=0;for(int v=0;v<N;v++)if(f>>v&1){U g=f^(U(1)<<v);x ^= (U128(1)<<ids.at(g));}
 cols.push_back(x);}
 return rank128(cols);
}
int main(){
 for(bool rook:{true,false}){
  auto a=graph(rook);array<U,N>co{};
  for(int v=0;v<N;v++){
   assert(pc(a[v])==6);co[v]=65535^(a[v]|(U(1)<<v));
   for(int w=v+1;w<N;w++)assert(pc(a[v]&a[w])==2);
  }
  auto independent=maximal_independent(a);
  auto cliques=maximal_independent(co);
  auto sf=all_shattered(independent);
  auto sc=all_shattered(cliques);
  auto fi=fvector(sf),fc=fvector(sc);
  assert(fi==(array<int,5>{1,16,72,96,0}));
  assert(fc==(rook?array<int,5>{1,16,48,0,0}:array<int,5>{1,16,48,32,0}));
  assert(independent.size()==(rook?24:48));assert(cliques.size()==(rook?8:32));
  // Every independent support of size <=3, and no other support, is shattered.
  for(U s=0;s<65536;s++){
    bool candidate=pc(s)<=3;
    for(int v=0;v<N;v++)if(s>>v&1)if(a[v]&s)candidate=false;
    bool observed=binary_search(sf.begin(),sf.end(),s);
    assert(candidate==observed);
    bool ccl=pc(s)<= (rook?2:3);
    for(int v=0;v<N;v++)if(s>>v&1)if((co[v]&s))ccl=false;
    // The rook graph's size-three cliques are intentionally NOT shattered.
    assert((ccl && (!rook || pc(s)<=2))==binary_search(sc.begin(),sc.end(),s));
  }
  assert(boundary_rank(sf,2)==15);
  assert(boundary_rank(sf,3)==57);
  assert(boundary_rank(sc,2)==15);
  if(rook){ assert(boundary_rank(sc,3)==0); }
  else{
    assert(boundary_rank(sc,3)==31);
    // A 4x4 periodic triangulation accounts for every shattered triangle.
    vector<U> torus;
    for(int r=0;r<4;r++)for(int c=0;c<4;c++){
      int A=index(r,c),B=index(r+1,c),C=index(r,c+1),D=index(r+1,c+1);
      torus.push_back((U(1)<<A)|(U(1)<<B)|(U(1)<<D));
      torus.push_back((U(1)<<A)|(U(1)<<C)|(U(1)<<D));
    }
    sort(torus.begin(),torus.end());
    vector<U> faces3;for(U s:sc)if(pc(s)==3)faces3.push_back(s);
    assert(faces3==torus);
  }
  cout<<(rook?"rook":"shrikhande")<<" concepts_independent="<<independent.size()<<" concepts_clique="<<cliques.size()
      <<" shat_independent=1,16,72,96 shat_clique="<<(rook?"1,16,48":"1,16,48,32")<<"\n";
 }
 cout<<"SHRIKHANDE_ROOK_DUAL_SHATTER_PASS\n";
}
