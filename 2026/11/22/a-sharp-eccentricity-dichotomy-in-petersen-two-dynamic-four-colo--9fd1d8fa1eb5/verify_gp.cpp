// Exhaustive certificate for finite proper 2-dynamic colourings of GP(5,2).
// C++17; compile g++ -O2 -std=c++17 verify_dynamic_gp.cpp -o verify && ./verify
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <vector>
using namespace std;
using A=array<int,10>;
vector<int> nb[10];
void edge(int u,int v){nb[u].push_back(v);nb[v].push_back(u);}
bool valid(const A& a){
 for(int u=0;u<10;u++){
   int mask=0;
   for(int v:nb[u]){
    if(a[v]==a[u])return false;
    mask|=1<<a[v];
   }
   if(__builtin_popcount((unsigned)mask)<2)return false;
 }
 return true;
}
vector<A> states;
int cnt[5]={};
void gen(A& a,int p,int k){
 if(p==10){cnt[k]++;if(valid(a) && k==4)states.push_back(a);return;}
 for(int c=0;c<k;c++){
  bool ok=true;
  for(int v:nb[p])if(v<p && a[v]==c){ok=false;break;}
  if(ok){a[p]=c;gen(a,p+1,k);}
 }
}
int enc(const A&a){int x=0;for(int i=9;i>=0;i--)x=4*x+a[i];return x;}
string profile(const A& a){
 int z[4]={};for(int c:a)z[c]++;
 sort(z,z+4);string s="";for(int i=0;i<4;i++)s+=to_string(z[i]);return s;
}
int main(){
 for(int i=0;i<5;i++){
  edge(i,(i+1)%5);
  edge(5+i,5+(i+2)%5);
  edge(i,5+i);
 }
 for(int u=0;u<10;u++)assert(nb[u].size()==3);
 A a{};gen(a,0,3);int prop3=cnt[3];
 // The three-colour dynamic count is independently obtained from proper leaves.
 int dyn3=0;
 auto rec3=[&](auto&&self,int p)->void{
  if(p==10){dyn3+=valid(a);return;}
  for(int c=0;c<3;c++){
   bool ok=true;for(int v:nb[p])if(v<p && a[v]==c)ok=false;
   if(ok){a[p]=c;self(self,p+1);}
  }
 };rec3(rec3,0);
 gen(a,0,4);
 const int n=(int)states.size();assert(n==5760);
 vector<int> index(1<<20,-1);
 for(int i=0;i<n;i++){int h=enc(states[i]);assert(index[h]==-1);index[h]=i;}
 int pow4[10];pow4[0]=1;for(int i=1;i<10;i++)pow4[i]=4*pow4[i-1];
 vector<vector<int>> g(n);
 map<string,int> profiles,grades;
 for(int i=0;i<n;i++){
  const A& s=states[i];profiles[profile(s)]++;
  int code=enc(s);
  for(int v=0;v<10;v++)for(int c=0;c<4;c++)if(c!=s[v]){
   int other=code+(c-s[v])*pow4[v];
   int j=index[other];if(j>=0)g[i].push_back(j);
  }
  grades[to_string(g[i].size())]++;
 }
 for(int i=0;i<n;i++)for(int j:g[i]){
  assert(find(g[j].begin(),g[j].end(),i)!=g[j].end());
 }
 map<string,map<int,int>> eccprof;
 vector<long long> distcount(18,0);
 int radius=999,diameter=0;
 for(int src=0;src<n;src++){
  vector<int> d(n,-1),q(n);int begin=0,end=0;
  d[src]=0;q[end++]=src;
  while(begin<end){int u=q[begin++];for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q[end++]=v;}}
  assert(end==n);
  int ecc=*max_element(d.begin(),d.end());
  eccprof[profile(states[src])][ecc]++;
  radius=min(radius,ecc);diameter=max(diameter,ecc);
  for(int j=src+1;j<n;j++){
    assert(d[j] < (int)distcount.size());distcount[d[j]]++;
  }
 }
 long long tot=accumulate(distcount.begin(),distcount.end(),0LL);
 assert(tot==1LL*n*(n-1)/2);
 cout<<"proper3="<<prop3<<" dynamic3="<<dyn3
     <<" proper4="<<cnt[4]<<" dynamic4="<<n<<"\n";
 cout<<"profiles=";
 for(auto [s,v]:profiles)cout<<s<<":"<<v<<" ";cout<<"\n";
 cout<<"degrees=";
 for(auto [s,v]:grades)cout<<s<<":"<<v<<" ";cout<<"\n";
 cout<<"eccentricities=";
 for(auto [p, mp]:eccprof)for(auto [e,v]:mp)cout<<p<<":"<<e<<":"<<v<<" ";cout<<"\n";
 cout<<"radius="<<radius<<" diameter="<<diameter<<" edges=";
 long long twice=0;for(auto&v:g)twice+=v.size();cout<<twice/2<<"\n";
 cout<<"unordered_distance_histogram=";
 for(int d=1;d<(int)distcount.size();d++)if(distcount[d])cout<<d<<":"<<distcount[d]<<" ";cout<<"\n";
}
