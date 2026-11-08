// Exhaustive base-k encoding of all proper vertex colourings of the Wagner graph.
// Compile: c++ -O2 -std=c++17 wagner_direct.cpp -o wagner_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
static bool proper(const array<int,8>& a) {
  for(int v=0;v<8;v++) if(a[v]==a[(v+1)%8] || a[v]==a[(v+4)%8])return false;
  return true;
}
int main(){
 for(int k=3;k<=4;k++){
  int powers[8];powers[0]=1;for(int i=1;i<8;i++)powers[i]=powers[i-1]*k;
  const int K=powers[7]*k;
  vector<array<int,8>> states;
  vector<int> lookup(K,-1);
  for(int code=0;code<K;code++){
   int x=code;array<int,8>a{};
   for(int v=0;v<8;v++){a[v]=x%k;x/=k;}
   if(proper(a)){lookup[code]=(int)states.size();states.push_back(a);}
  }
  int n=states.size();vector<vector<int>> g(n);
  for(int i=0;i<n;i++){
   int code=0;for(int v=0;v<8;v++)code+=states[i][v]*powers[v];
   for(int v=0;v<8;v++)for(int c=0;c<k;c++){
    if(c==states[i][v])continue;
    int target=code+(c-states[i][v])*powers[v];
    if(lookup[target]>=0)g[i].push_back(lookup[target]);
   }
  }
  map<int,int>degrees;long long arcs=0;
  for(int v=0;v<n;v++){
   sort(g[v].begin(),g[v].end());
   degrees[g[v].size()]++;arcs+=g[v].size();
   for(int w:g[v])assert(find(g[w].begin(),g[w].end(),v)!=g[w].end());
  }
  vector<int> comp(n,-1);map<int,int>sizes;int nc=0;
  for(int v=0;v<n;v++)if(comp[v]<0){
   queue<int> q;q.push(v);comp[v]=nc;int size=0;
   while(!q.empty()){int u=q.front();q.pop();size++;
    for(int w:g[u])if(comp[w]<0){comp[w]=nc;q.push(w);}}
   sizes[size]++;nc++;
  }
  map<int,long long> pairCounts;map<int,int> ecc;
  long long unreachablePairs=0;
  for(int s=0;s<n;s++){
   vector<int> dist(n,-1);queue<int>q;q.push(s);dist[s]=0;
   while(!q.empty()){
    int v=q.front();q.pop();
    for(int w:g[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}
   }
   int mx=0;
   for(int v=0;v<n;v++){
    if(dist[v]<0){if(v>s)unreachablePairs++;continue;}
    mx=max(mx,dist[v]);if(v>s)pairCounts[dist[v]]++;
   }
   ecc[mx]++;
  }
  cout<<"k="<<k<<" states="<<n<<" edges="<<arcs/2<<" components="<<nc
      <<" comp_sizes=";for(auto [sz,m]:sizes)cout<<sz<<":"<<m<<",";
  cout<<" degrees=";for(auto [deg,m]:degrees)cout<<deg<<":"<<m<<",";
  cout<<" ecc=";for(auto [e,m]:ecc)cout<<e<<":"<<m<<",";
  cout<<" pair_dists=";for(auto [d,m]:pairCounts)cout<<d<<":"<<m<<",";
  cout<<" unreachable_pairs="<<unreachablePairs<<"\n";
  if(k==3){assert((n==48&&arcs/2==48&&nc==2&&sizes==map<int,int>{{24,2}}&&degrees==map<int,int>{{2,48}}&&ecc==map<int,int>{{12,48}}));}
  if(k==4){assert((n==2160&&arcs/2==7872&&nc==1&&ecc==map<int,int>{{12,2160}}&&pairCounts[12]==5160&&unreachablePairs==0));}
 }
 cout<<"INDEPENDENT_EXHAUSTIVE_PASS\n";
}
