// Exhaustive ternary-code verification of minimum weak Roman defense on the
// eighteen-vertex Pappus graph, with a second standard vertex labelling.
// Build: c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary
// Run: ./verify_ternary
#include <array>
#include <cassert>
#include <iostream>
using namespace std;
constexpr int N = 18;
// Neighbor masks of the standard Pappus LCF (networkx.pappus_graph) labelling.
constexpr int ADJ[N] = {131106,261,8202,1044,32808,81,2208,16704,642,
  66816,2568,5184,141312,20484,41088,81936,164352,69633};

bool dominates(int support) {
 for(int v=0;v<N;v++)
  if(!(support&(1<<v)) && !(ADJ[v]&support)) return false;
 return true;
}

bool weak_roman(const array<int,N>& f,int support) {
 if(!dominates(support)) return false;
 for(int v=0;v<N;v++) if(!f[v]) {
  int donors=ADJ[v]&support;bool defended=false;
  while(donors) {
   int u=__builtin_ctz((unsigned)donors);donors&=donors-1;
   int post=support|(1<<v);
   if(f[u]==1) post&=~(1<<u);
   if(dominates(post)) {defended=true;break;}
  }
  if(!defended) return false;
 }
 return true;
}

int main() {
 for(int i=0;i<N;i++) {
  assert(__builtin_popcount((unsigned)ADJ[i])==3);
  for(int j=0;j<N;j++) assert(bool(ADJ[i]&(1<<j))==bool(ADJ[j]&(1<<i)));
 }
 int codes=1;for(int i=0;i<N;i++)codes*=3;
 long long by_weight[9]={}, by_double[5]={};
 for(int code=0;code<codes;code++) {
  int t=code,weight=0,doubles=0,support=0;
  array<int,N> f{};
  for(int i=0;i<N;i++) {
   f[i]=t%3;t/=3;weight+=f[i];
   if(f[i]) support|=1<<i;
   if(f[i]==2) doubles++;
  }
  if(weight>8)continue;
  if(weak_roman(f,support)) {
   by_weight[weight]++;
   if(weight==8)by_double[doubles]++;
  }
 }
 for(int w=0;w<8;w++)assert(by_weight[w]==0);
 assert(by_weight[8]==2691);
 assert(by_double[0]==1755 && by_double[1]==882 && by_double[2]==54 &&
        by_double[3]==0 && by_double[4]==0);
 cout<<"PASS: all 3^18 labelings checked; weak Roman minimum is 8; "
     <<"optimal counts by doubled vertices 1755,882,54.\n";
}
