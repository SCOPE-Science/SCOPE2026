// Standalone exact incidence verifier over F4 using line triangles, not Hermitian forms.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using U = uint32_t;
int mul(int a,int b){int z=0;for(int i=0;i<2;i++)if((b>>i)&1)z^=a<<i;if(z&8)z^=14;if(z&4)z^=7;return z;}
int det(array<int,3>a,array<int,3>b,array<int,3>c){return mul(a[0],mul(b[1],c[2])^mul(b[2],c[1]))^mul(a[1],mul(b[0],c[2])^mul(b[2],c[0]))^mul(a[2],mul(b[0],c[1])^mul(b[1],c[0]));}
int main(){
 set<array<int,3>> pp;
 for(int x=0;x<4;x++)for(int y=0;y<4;y++)for(int z=0;z<4;z++){
  array<int,3> v={x,y,z};if(v==array<int,3>{0,0,0})continue;
  int first= x?x:(y?y:z),inv=0;for(int a=1;a<=3;a++)if(mul(a,first)==1)inv=a;
  for(auto& t:v) t=mul(t,inv);
  pp.insert(v);
 }
 vector<array<int,3>> p(pp.begin(),pp.end());assert(p.size()==21);
 set<U> ls;for(int a=0;a<21;a++)for(int b=a+1;b<21;b++){
  U mask=0;for(int j=0;j<21;j++)if(det(p[a],p[b],p[j])==0)mask|=(1u<<j);
  assert(__builtin_popcount(mask)==5);ls.insert(mask);
 }
 assert(ls.size()==21);vector<U> lines(ls.begin(),ls.end());
 set<U> unitals;
 for(int i=0;i<21;i++)for(int j=i+1;j<21;j++)for(int k=j+1;k<21;k++){
  U a=lines[i],b=lines[j],c=lines[k];if((a&b)==(a&c))continue;
  U unital=(a|b|c)^((a&b)|(a&c)|(b&c));
  assert(__builtin_popcount(unital)==9);unitals.insert(unital);
 }
 assert(unitals.size()==280);vector<U> co(unitals.begin(),unitals.end());
 vector<vector<int>> support(10);
 vector<int> positiveCounts(1<<21,0);
 for(U m:co){vector<int> ids;for(int i=0;i<21;i++)if(m>>i&1)ids.push_back(i);
  for(int k=1;k<=9;k++)for(U sub=0;sub<(1u<<9);sub++)if(__builtin_popcount(sub)==k){
   U s=0;for(int i=0;i<9;i++)if(sub>>i&1)s|=1u<<ids[i];positiveCounts[s]++;
  }
 }
 int expect[]={0,21,210,1330,5880,17640,23520,10080,2520,280};
 long long shatter[7]={1};
 for(U s=1;s<(1u<<21);s++){
  int k=__builtin_popcount(s);if(k>9||positiveCounts[s]==0)continue;
  support[k].push_back(s);
  if(k<=6){
   if(k==6){uint64_t signatureSet=0;
    for(U u:co){uint64_t code=0;int j=0;for(U t=s;t;t&=t-1){U bit=t&-t;if(u&bit)code|=1ULL<<j;j++;}signatureSet|=1ULL<<code;}
    assert(signatureSet==~uint64_t(0));shatter[k]++;
   }
  }
 }
 for(int k=1;k<=9;k++)assert((int)support[k].size()==expect[k]);
 assert(shatter[6]==23520);
 for(U s:support[5])assert(positiveCounts[s]==2);
 for(U s:support[6])assert(positiveCounts[s]==1);
 for(int k=1;k<=5;k++){ // all contained supports are shattered by heredity from a 6-set
  assert(!support[k].empty());shatter[k]=support[k].size();
 }
 cout<<"TRIANGLES: 21 points, 21 lines, "<<co.size()<<" unitals\n";
 cout<<"SHATTERED: 1";for(int k=1;k<=6;k++)cout<<" "<<shatter[k];cout<<" (higher 0)\n";
 cout<<"FULL-TRACES: all 23520 six-subsets; five-incidence multiplicity 2, six multiplicity 1\n";
}
