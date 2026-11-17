// Independent exhaustive permutation enumerator for strong gradients of the unfilled 10-cycle.
// C++17 standard library only. Compile: g++ -O2 -std=c++17 enumerate_orders.cpp -o enumerate_orders
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
using namespace std;
int main(int argc,char**argv){
 if(argc!=2){cerr<<"usage: enumerate_orders OUTPUT_GRADIENTS\n";return 2;}
 constexpr int N=10;
 array<int,N> p{},pos{};for(int i=0;i<N;++i)p[i]=i;
 set<unsigned> masks; long long count=0;
 do {
  for(int i=0;i<N;++i)pos[p[i]]=i;
  unsigned mask=0;
  for(int v=0;v<N;++v){
   bool prev=pos[(v+N-1)%N]<pos[v];
   bool next=pos[(v+1)%N]<pos[v];
   if(prev!=next)mask |= 1u<<(2*v+(next?1:0));
  }
  masks.insert(mask);++count;
 } while(next_permutation(p.begin(),p.end()));
 if(count!=3628800 || masks.size()!=1021)throw runtime_error("unexpected enumerator totals");
 ofstream out(argv[1]);if(!out)throw runtime_error("cannot write output");
 for(unsigned m:masks)out<<m<<'\n';
 cout<<"ORDERS "<<count<<" GRADIENTS "<<masks.size()<<"\n";
}
