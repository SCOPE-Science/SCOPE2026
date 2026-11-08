// Exhaustive independent reverse-column DFS and direct switch testing.
// Compile: g++ -O2 -std=c++17 verify_reverse.cpp -o verify_reverse
// Run: ./verify_reverse
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
static int n, a[16];
static uint32_t seen[16];
static unsigned long long count_total, n_edges_directed, adj_directed;
static map<int,unsigned long long> degree_hist, gap_directed;

static bool costas_direct(){
 for(int h=1;h<n;h++){
  uint32_t diffmask=0;
  for(int i=0;i+h<n;i++){
   int diff=a[i+h]-a[i]+(n-1);
   uint32_t bit=uint32_t(1)<<diff;
   if(diffmask & bit)return false;
   diffmask |= bit;
  }
 }
 return true;
}
static void dfs(int k,uint32_t used){
 if(k<0){
  count_total++;
  unsigned deg=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
   swap(a[i],a[j]);
   if(costas_direct()){
    deg++; n_edges_directed++;gap_directed[j-i]++;
    if(j==i+1)adj_directed++;
   }
   swap(a[i],a[j]);
  }
  degree_hist[deg]++;
  return;
 }
 for(int v=n-1;v>=0;v--){
  if(used & (uint32_t(1)<<v))continue;
  bool ok=true;
  for(int j=1;k+j<n;j++){
   uint32_t bit=uint32_t(1)<<(a[k+j]-v+(n-1));
   if(seen[j] & bit){ok=false;break;}
  }
  if(!ok)continue;
  a[k]=v;
  for(int j=1;k+j<n;j++)seen[j]|=uint32_t(1)<<(a[k+j]-v+(n-1));
  dfs(k-1,used|(uint32_t(1)<<v));
  for(int j=1;k+j<n;j++)seen[j]&=~(uint32_t(1)<<(a[k+j]-v+(n-1)));
 }
}
int main(){
 for(int size:{11,12,13,14}){
  n=size;count_total=n_edges_directed=adj_directed=0;degree_hist.clear();gap_directed.clear();
  for(auto &v:seen)v=0;
  dfs(n-1,0);
  if(n_edges_directed%2 || adj_directed%2){cerr<<"odd count"<<endl;return 1;}
  const map<int,pair<unsigned long long,unsigned long long>> expected={{11,{4368,140}},{12,{7852,136}},{13,{12828,88}},{14,{17252,120}}};
  if(count_total!=expected.at(n).first || n_edges_directed/2!=expected.at(n).second)return 2;
  if((size>=12 && degree_hist.size()!=2)||(size>=12 && degree_hist.count(1) && degree_hist.at(1)!=n_edges_directed))return 3;
  const map<int,vector<int>> gaps={
   {11,{16,20,20,16,8,16,16,8,12,8}},
   {12,{8,16,4,0,20,40,8,8,20,8,4}},
   {13,{12,16,8,4,12,4,8,0,0,8,8,8}},
   {14,{12,0,20,0,0,8,8,0,12,12,32,12,4}}};
  for(int g=1;g<size;g++)if(gap_directed[g]!=2*(unsigned long long)gaps.at(n)[g-1])return 4;
  cout<<"n="<<n<<" vertices="<<count_total<<" edges="<<n_edges_directed/2<<" adjacent="<<adj_directed/2<<" degrees=";
  for(auto [d,v]:degree_hist)cout<<d<<":"<<v<<",";
  cout<<" gaps=";
  for(auto [g,v]:gap_directed)cout<<g<<":"<<v/2<<",";
  cout<<"\n";
 }
}
