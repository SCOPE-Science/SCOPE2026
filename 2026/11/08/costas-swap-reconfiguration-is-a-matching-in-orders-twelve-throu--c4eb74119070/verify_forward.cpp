// Complete left-to-right Costas enumeration; all valid arrays stored then indexed for swaps.
// Compile: g++ -O2 -std=c++17 verify_forward.cpp -o verify_forward
// Run: ./verify_forward 11 12 13 14
#include <bits/stdc++.h>
using namespace std;
int n,p[17];bool used[17],seen[17][40];vector<uint64_t> arr;
void rec(int k,uint64_t enc){
 if(k==n){arr.push_back(enc);return;}
 for(int x=0;x<n;x++)if(!used[x]){
  bool ok=true;
  for(int j=1;j<=k;j++)if(seen[j][x-p[k-j]+n]){ok=false;break;}
  if(!ok)continue;
  used[x]=true;p[k]=x;
  for(int j=1;j<=k;j++)seen[j][x-p[k-j]+n]=true;
  rec(k+1,enc | (uint64_t(x)<<(4*k)));
  for(int j=1;j<=k;j++)seen[j][x-p[k-j]+n]=false;
  used[x]=false;
 }
}
int main(int argc,char **argv){
 for(int ai=1;ai<argc;ai++){
  n=atoi(argv[ai]); if(n<11||n>14)return 1;
  auto t=chrono::steady_clock::now();
  arr.clear(); memset(used,0,sizeof used);memset(seen,0,sizeof seen);
  rec(0,0);
  long long edges=0, adjacent=0;map<int,int> dist;vector<int> degree(arr.size());
  unordered_map<uint64_t,int> idx;idx.reserve(arr.size()*2+1);
  for(int i=0;i<(int)arr.size();i++)idx[arr[i]]=i;
  for(int i=0;i<(int)arr.size();i++){
   uint64_t x=arr[i];
   for(int j=0;j<n;j++)for(int k=j+1;k<n;k++){
    uint64_t a=(x>>(4*j))&15,b=(x>>(4*k))&15;
    uint64_t q=x ^ ((a^b)<<(4*j)) ^ ((a^b)<<(4*k));
    auto it=idx.find(q);
    if(it!=idx.end()&&it->second>i){edges++;degree[i]++;degree[it->second]++;dist[k-j]++;if(k==j+1)adjacent++;}
   }
  }
  map<int,int> hist;for(int d:degree)hist[d]++;
  auto elapsed=chrono::duration<double>(chrono::steady_clock::now()-t).count();
  const map<int,tuple<int,int,map<int,int>,vector<int>>> expected={
    {11,{4368,140,{{0,4096},{1,264},{2,8}},{16,20,20,16,8,16,16,8,12,8}}},
    {12,{7852,136,{{0,7580},{1,272}},{8,16,4,0,20,40,8,8,20,8,4}}},
    {13,{12828,88,{{0,12652},{1,176}},{12,16,8,4,12,4,8,0,0,8,8,8}}},
    {14,{17252,120,{{0,17012},{1,240}},{12,0,20,0,0,8,8,0,12,12,32,12,4}}}};
  auto [v,ex_edges,ex_hist,ex_gaps]=expected.at(n);
  if((int)arr.size()!=v || edges!=ex_edges || hist!=ex_hist) return 2;
  for(int gap=1;gap<n;gap++)if(dist[gap]!=ex_gaps[gap-1])return 3;
  cout<<"n="<<n<<" count="<<arr.size()<<" edge="<<edges<<" adjacent="<<adjacent<<" degrees ";for(auto [d,k]:hist)cout<<d<<":"<<k<<" ";cout<<" gaps ";for(auto [d,k]:dist)cout<<d<<":"<<k<<" ";cout<<" time="<<elapsed<<"\n"<<flush;
 }
}
