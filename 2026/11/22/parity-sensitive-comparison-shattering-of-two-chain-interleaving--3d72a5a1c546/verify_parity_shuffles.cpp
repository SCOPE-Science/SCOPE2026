// Standalone C++17 exhaustive check of trace realization and cross-adjacency obstructions.
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>
#include <string>
using namespace std;
using P=pair<int,int>;
struct W {unsigned long long bits; int parity; set<P> crossing;};
static vector<W> create(int a,int b){
 vector<W> out;
 int n=a+b;
 for(int mask=0; mask<(1<<n); ++mask){
  if(__builtin_popcount((unsigned)mask)!=a)continue;
  string s; int pa=0,pb=0,inv=0; vector<int> ia,ib;
  for(int h=0;h<n;h++){
   char c=((mask>>h)&1)?'A':'B';s.push_back(c);
   if(c=='A'){ia.push_back(h);inv+=pb;pa++;}
   else{ib.push_back(h);pb++;}
  }
  unsigned long long bits=0;
  for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(ia[i]<ib[j])bits|=1ULL<<(i*b+j);
  set<P> crossing;pa=pb=0;
  for(int h=0;h<n;h++){
   if(s[h]=='A')pa++;else pb++;
   if(h>0&&s[h]!=s[h-1])crossing.insert({pa-1,pb-1});
  }
  out.push_back({bits,inv%2,crossing});
 }
 return out;
}
static vector<vector<int>> choose(int n,int k){
 vector<vector<int>> o; int lim=1<<n;
 for(int m=0;m<lim;m++)if(__builtin_popcount((unsigned)m)==k){
  vector<int> v;for(int x=0;x<n;x++)if(m>>x&1)v.push_back(x);o.push_back(v);
 }return o;
}
static void test(int a,int b){
 auto words=create(a,b); int vc=0;
 for(int k=0;k<=min(a,b);k++){
  int count=0;
  auto AS=choose(a,k),BS=choose(b,k);
  for(const auto& aa:AS)for(const auto& bb:BS){
   set<P> S; vector<int> bitpos;
   for(int t=0;t<k;t++){S.insert({aa[t],bb[t]});bitpos.push_back(aa[t]*b+bb[t]);}
   set<int> traces;
   bool oddSingleton=false;
   for(const auto& w:words){
    if(!w.parity){int t=0;for(int z=0;z<k;z++)if(w.bits>>bitpos[z]&1)t|=1<<z;traces.insert(t);}
    else if(includes(S.begin(),S.end(),w.crossing.begin(),w.crossing.end()))oddSingleton=true;
   }
   bool actual=(int)traces.size()==(1<<k);
   assert(actual==!oddSingleton);
   count+=actual;
  }
  if(count)vc=k;
 }
 assert(vc==(a==b&&a%2?min(a,b)-1:min(a,b)));
}
int main(){int tests=0;for(int sum=2;sum<=12;sum++)for(int a=1;a<sum;a++){test(a,sum-a);tests++;}
 cout<<"PARITY_TWO_CHAIN_CPP_PASS "<<tests<<" profiles"<<endl;return 0;}
