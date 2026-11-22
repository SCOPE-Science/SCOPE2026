// Independent exhaustive test of power domination versus the residual-forest criterion.
// C++17. Compile: g++ -O3 -std=c++17 check_forest.cpp -o check_forest
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
#include <cassert>
using namespace std;
int root(vector<int>& p, int a){while(p[a]!=a){a=p[a]=p[p[a]];}return a;}
int main(){
 for(int n=3;n<=6;n++){
  vector<pair<int,int>> pairs;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)pairs.push_back({a,b});
  int m=n+(int)pairs.size();
  vector<uint32_t> neigh(m,0);
  for(int k=0;k<(int)pairs.size();k++){
   auto [a,b]=pairs[k];int j=n+k;
   neigh[j]|=(1u<<a)|(1u<<b);neigh[a]|=1u<<j;neigh[b]|=1u<<j;
  }
  vector<unsigned long long> counts(m+1,0);
  unsigned long long total=1ULL<<m;
  for(unsigned long long S=0;S<total;S++){
   uint32_t mask=(uint32_t)S;
   uint32_t seen=mask,prev=0;
   for(int v=0;v<m;v++)if((mask>>v)&1u)seen|=neigh[v];
   while(prev!=seen){
    prev=seen;uint32_t newseen=seen;
    for(int v=0;v<m;v++)if((seen>>v)&1u){
     uint32_t remaining=neigh[v]&~seen;
     if(remaining && !(remaining&(remaining-1u)))newseen|=remaining;
    }
    seen=newseen;
   }
   bool power=(seen==((1u<<m)-1u));
   vector<int> par(n);iota(par.begin(),par.end(),0);
   bool acyclic=true;
   for(int k=0;k<(int)pairs.size();k++){
    auto [a,b]=pairs[k];
    if(((mask>>a)&1u)||((mask>>b)&1u)||((mask>>(n+k))&1u))continue;
    int x=root(par,a),y=root(par,b);
    if(x==y){acyclic=false;break;}
    par[x]=y;
   }
   // Residual edges are pairs whose endpoints are unselected originals and
   // whose edge-vertices are unselected.
   if(power!=acyclic){cerr<<"MISMATCH order "<<n<<" mask="<<S<<"\n";return 2;}
   if(power)counts[__builtin_popcountll(S)]++;
  }
  int minimum=0;while(minimum<=m&&!counts[minimum])minimum++;
  unsigned long long expected=(unsigned long long)n*(n-1)*(n-1)/2;
  if(minimum!=n-2||counts[minimum]!=expected){cerr<<"MINIMUM MISMATCH\n";return 3;}
  cout<<"order="<<n<<" graph_vertices="<<m<<" masks="<<total
      <<" minimum="<<minimum<<" optimum_count="<<counts[minimum]<<" coefficients=";
  for(int i=0;i<=m;i++)if(counts[i])cout<<i<<":"<<counts[i]<<",";
  cout<<" PASS\n";
 }
}
