// Finite exact enumeration of binary reverse-complement five-mer covering words.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
int rc(int x,int k){int y=0; for(int j=0;j<k;j++)y=(y<<1)|(1-((x>>j)&1));return y;}
string reversebits(string a){reverse(a.begin(),a.end());return a;}
string complement(string a){for(char& c:a)c=(c=='0'?'1':'0');return a;}
string minrotation(const string& s){string best=s;for(int j=1;j<(int)s.size();j++){string a=s.substr(j)+s.substr(0,j);if(a<best)best=a;}return best;}
int main(){
 array<int,32> orbit{};vector<array<int,2>> pairs;
 for(int e=0;e<32;e++)if(e<rc(e,5)){int i=(int)pairs.size();pairs.push_back({e,rc(e,5)});orbit[e]=orbit[rc(e,5)]=i;}
 if(pairs.size()!=16)return 1;
 uint64_t rooted=0,noncyclic=0;set<string> cycle_roots, symmetry_classes;
 for(int w=0;w<(1<<20);w++){
  uint32_t seen=0;
  for(int i=0;i<16;i++)seen|=1u<<orbit[(w>>i)&31];
  if(seen!=65535u)continue;
  rooted++;
  if(((w>>16)&15)!=(w&15)){noncyclic++;continue;}
  string s;
  for(int j=19;j>=4;j--)s.push_back('0'+((w>>j)&1));
  cycle_roots.insert(minrotation(s));
  string rep=s;
  for(string v:{s,reversebits(s),complement(s),reversebits(complement(s))})rep=min(rep,minrotation(v));
  symmetry_classes.insert(rep);
 }
 cout<<"rooted="<<rooted<<" noncyclic="<<noncyclic<<" rotation_classes="<<cycle_roots.size()<<" reversal_complement_classes="<<symmetry_classes.size()<<"\n";
 cout<<"class_representatives:";for(auto&s:symmetry_classes)cout<<' '<<s;cout<<'\n';
 long balanced=0,connected=0,cycles=0;map<int,int> tourhist;
 vector<pair<int,int>> cert;
 for(int choice=0;choice<(1<<16);choice++){
  array<int,16> indeg{},outdeg{};array<vector<pair<int,int>>,16> adj;
  vector<pair<int,int>> es;
  for(int i=0;i<16;i++){
   int e=pairs[i][(choice>>i)&1];int a=e>>1,b=e&15;
   es.push_back({a,b});outdeg[a]++;indeg[b]++;adj[a].push_back({i,b});
  }
  if(indeg!=outdeg)continue;
  balanced++;
  int root=es[0].first;
  auto is_reachable=[&](bool transpose){
   uint32_t vis=1u<<root;
   for(int j=0;j<16;j++)for(auto [a,b]:es){if(transpose)swap(a,b);if(vis&(1u<<a))vis|=1u<<b;}
   for(int v=0;v<16;v++)if(outdeg[v] && !(vis&(1u<<v)))return false;
   return true;
  };
  if(!is_reachable(false)||!is_reachable(true))continue;
  connected++;
  auto dfs=[&](auto&& self,int v,uint32_t used)->int{
   if(used==65535u)return v==root?1:0;
   int cnt=0;
   for(auto [i,b]:adj[v])if(!(used&(1u<<i)))cnt+=self(self,b,used|(1u<<i));
   return cnt;
  };
  int cnt=dfs(dfs,es[0].second,1u);
  if(cnt){tourhist[cnt]++;cert.push_back({choice,cnt});cycles+=cnt;}
 }
 cout<<"balanced_edge_choices="<<balanced<<" strongly_connected_choices="<<connected<<" canonical_tours="<<cycles<<"\n";
 cout<<"tours_per_choice_histogram:";for(auto [num,count]:tourhist)cout<<' '<<num<<':'<<count;cout<<'\n';
 cout<<"choice_mask_and_tour_count:";for(auto [mask,num]:cert)cout<<' '<<mask<<':'<<num;cout<<'\n';
 if(rooted!=512||noncyclic!=0||cycle_roots.size()!=32||symmetry_classes.size()!=8||balanced!=52||connected!=18||cycles!=32)return 2;
 cout<<"ALL_INDEPENDENT_CHECKS_PASSED\n";
}
