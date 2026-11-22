// Exhaustive closed-neighborhood three-limited packing check on triangular graphs.
// Compile: c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce
#include <bits/stdc++.h>
using namespace std;
using i64=long long;
struct Enumerator {
 int n, m; vector<pair<int,int>> edges; vector<int> deg,chosen; vector<i64> good, maximal;
 bool feasible() const {
   for(int i=0;i<m;i++) {
     auto [u,v]=edges[i];
     int chosen_edge=chosen[i];
     if(deg[u]+deg[v]-chosen_edge>3) return false;
   }
   return true;
 }
 void rec(int i,int k) {
   if(i==m) {
     good[k]++;
     bool ismax=true;
     for(int j=0;j<m;j++) if(!chosen[j]) {
       auto [u,v]=edges[j]; deg[u]++;deg[v]++;chosen[j]=1;
       bool possible=feasible();
       deg[u]--;deg[v]--;chosen[j]=0;
       if(possible){ismax=false;break;}
     }
     if(ismax)maximal[k]++;
     return;
   }
   rec(i+1,k);
   auto [u,v]=edges[i];deg[u]++;deg[v]++;chosen[i]=1;
   if(feasible()) rec(i+1,k+1);
   deg[u]--;deg[v]--;chosen[i]=0;
 }
 void run() {
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)edges.push_back({u,v});
  m=edges.size();deg.assign(n,0);chosen.assign(m,0);good.assign(m+1,0);maximal.assign(m+1,0);
  rec(0,0);
  cout << n << "\t";
  for(int k=0;k<=m;k++)if(good[k])cout<<k<<":"<<good[k]<<",";
  cout << "\t";
  for(int k=0;k<=m;k++)if(maximal[k])cout<<k<<":"<<maximal[k]<<",";
  cout<<"\n";
 }
};
int main(int argc,char**argv){
 int lo=argc>1?atoi(argv[1]):3, hi=argc>2?atoi(argv[2]):9;
 for(int n=lo;n<=hi;n++){Enumerator e;e.n=n;e.run();}
}
