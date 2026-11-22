// C++17 standalone exhaustive verifier, independent enumeration and graph representation.
// Compile: g++ -O2 -std=c++17 -Wall -Wextra verify_cpp.cpp -o verify_cpp && ./verify_cpp
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
static constexpr int n=18;
static vector<vector<int>> nei(n);

static void construct(){
  // Points are 3*x+y, lines are 9+a,12+a,15+a.
  for(int x=0;x<3;x++)for(int y=0;y<3;y++){
    int v=3*x+y;
    for(int w:{9+x,12+y,15+(x+y)%3}){
      nei[v].push_back(w);nei[w].push_back(v);
    }
  }
  for(auto& a:nei){sort(a.begin(),a.end()); assert(a.size()==3);}
}
static bool dominates(int set){
  for(int v=0;v<n;v++)if(!(set&(1<<v))){
    bool found=false;
    for(int w:nei[v])if(set&(1<<w)){found=true;break;}
    if(!found)return false;
  }
  return true;
}
static bool restrained(int set){
  if(!dominates(set))return false;
  for(int v=0;v<n;v++)if(!(set&(1<<v))){
    bool outside=false;
    for(int w:nei[v])if(!(set&(1<<w))){outside=true;break;}
    if(!outside)return false;
  }
  return true;
}
static vector<int> opt;
static map<int,int> all,ord;
static void rec(int v,int bits,int count){
  if(v==n){
    if(dominates(bits))ord[count]++;
    if(restrained(bits)){all[count]++;if(count==6)opt.push_back(bits);}
    return;
  }
  rec(v+1,bits,count);
  rec(v+1,bits|(1<<v),count+1);
}
static void componentAnalysis(bool sliding){
  map<int,int> index;
  for(int i=0;i<(int)opt.size();i++)index[opt[i]]=i;
  vector<vector<int>> g(opt.size());
  for(int i=0;i<(int)opt.size();i++){
    int s=opt[i];
    for(int u=0;u<n;u++)if(s&(1<<u))for(int v=0;v<n;v++)if(!(s&(1<<v))){
      if(sliding && !binary_search(nei[u].begin(),nei[u].end(),v))continue;
      auto it=index.find(s^(1<<u)^(1<<v));
      if(it!=index.end())g[i].push_back(it->second);
    }
    sort(g[i].begin(),g[i].end());g[i].erase(unique(g[i].begin(),g[i].end()),g[i].end());
  }
  map<int,int> degree,ecc;
  int e=0;
  for(const auto& a:g){degree[a.size()]++;e+=a.size();}e/=2;
  vector<int> seen(opt.size());vector<int> sizes;
  for(int i=0;i<(int)opt.size();i++)if(!seen[i]){
    vector<int> q(1,i);seen[i]=1;
    for(size_t k=0;k<q.size();k++)for(int j:g[q[k]])if(!seen[j]){seen[j]=1;q.push_back(j);}
    sizes.push_back(q.size());
  }
  for(int i=0;i<(int)opt.size();i++){
    vector<int> d(opt.size(),-1);queue<int> q;q.push(i);d[i]=0;int em=0;
    while(!q.empty()){
      int v=q.front();q.pop();em=max(em,d[v]);
      for(int u:g[v])if(d[u]<0){d[u]=d[v]+1;q.push(u);}
    }
    ecc[em]++;
  }
  sort(sizes.begin(),sizes.end());
  assert(sizes.size()==28 && sizes.front()==1 && sizes.back()==180);
  if(!sliding){assert((e==432 && degree==map<int,int>({{0,27},{4,108},{6,72}}) && ecc==map<int,int>({{0,27},{6,180}})));}
  else{assert((e==324 && degree==map<int,int>({{0,27},{2,108},{6,72}}) && ecc==map<int,int>({{0,27},{8,180}})));}
  cout<<(sliding?"slide":"jump")<<": edges="<<e<<" isolated=27 core=180 core_diameter="<<(sliding?8:6)<<"\n";
}
int main(){
  construct();rec(0,0,0);
  assert(ord[5]==18 && all[6]==207 && opt.size()==207);
  for(int i=0;i<5;i++)assert(ord.find(i)==ord.end());
  for(int i=0;i<6;i++)assert(all.find(i)==all.end());
  const map<int,int> expected={{6,207},{7,1242},{8,3429},{9,5040},{10,4671},{11,3294},{12,1809},{13,756},{14,297},{15,54},{16,27},{18,1}};
  assert(all==expected);
  componentAnalysis(false);componentAnalysis(true);
  cout<<"ordinary minimum 5 count="<<ord[5]<<", restrained minimum 6 count="<<opt.size()<<"\nPASS\n";
}
