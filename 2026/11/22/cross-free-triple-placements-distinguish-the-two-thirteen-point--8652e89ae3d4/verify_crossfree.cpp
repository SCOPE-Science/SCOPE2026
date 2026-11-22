#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
using S=array<int,13>;
using Triple=array<int,3>;
using Design=set<Triple>;
Triple canon(Triple t){sort(t.begin(),t.end());return t;}
Design cyclic(){
 Design b;
 for(int r=0;r<13;r++)for(Triple s: {Triple{1,3,9},Triple{2,5,6}}){
  for(int &x:s)x=(x+r)%13;
  b.insert(canon(s));
 }
 return b;
}
Design switched(Design b){
 for(Triple t:{Triple{2,4,10},Triple{2,5,6},Triple{4,6,12},Triple{5,10,12}})
  assert(b.erase(canon(t))==1);
 for(Triple t:{Triple{2,4,6},Triple{2,5,10},Triple{4,10,12},Triple{5,6,12}})
  assert(b.insert(canon(t)).second);
 return b;
}
void valid_design(const Design& b){
 assert(b.size()==26);
 int pair[13][13]={};
 for(auto t:b)for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)pair[t[i]][t[j]]++;
 for(int i=0;i<13;i++)for(int j=i+1;j<13;j++)assert(pair[i][j]==1);
}
// 2-bit digits encode the three named colour classes and the unused class.
// Restrict to states in which the lexicographically first nonzero-colour point has colour 1,
// and the first point of colour 2 precedes the first point of colour 3.
// Equivalently all 3! permutations of named colours are quotiented canonically.
uint64_t encode(const S& s){uint64_t x=0;for(int i=0;i<13;i++)x|=(uint64_t)s[i]<<(2*i);return x;}
uint64_t canonical(S s){
 int remap[4]={0,0,0,0},next=1;
 for(int i=0;i<13;i++)if(s[i] && !remap[s[i]])remap[s[i]]=next++;
 for(int i=0;i<13;i++)if(s[i])s[i]=remap[s[i]];
 return encode(s);
}
S decode(uint64_t code){S s{};for(int i=0;i<13;i++)s[i]=(code>>(2*i))&3;return s;}
bool crossfree(const S& s,const Design& blocks){
 for(const auto& t:blocks){int b=(1<<s[t[0]])|(1<<s[t[1]])|(1<<s[t[2]]);
  if((b & 14)==14)return false;
 }
 return true;
}
vector<uint64_t> enumerate(const Design& blocks){
 // Choose three disjoint labelled 3-sets, then identify colour permutations.
 vector<uint64_t> ret;
 for(int a=0;a<(1<<13);a++)if(__builtin_popcount((unsigned)a)==3){
  for(int b=0;b<(1<<13);b++)if(!(a&b)&&__builtin_popcount((unsigned)b)==3){
   for(int c=0;c<(1<<13);c++)if(!((a|b)&c)&&__builtin_popcount((unsigned)c)==3){
    S s{};
    for(int i=0;i<13;i++)s[i]=(a>>i&1)?1:(b>>i&1)?2:(c>>i&1)?3:0;
    if(crossfree(s,blocks))ret.push_back(canonical(s));
   }
  }
 }
 sort(ret.begin(),ret.end());ret.erase(unique(ret.begin(),ret.end()),ret.end());return ret;
}
void run(const Design& blocks){
 valid_design(blocks);
 auto states=enumerate(blocks);
 unordered_map<uint64_t,int> index;
 for(size_t i=0;i<states.size();i++)index[states[i]]=i;
 vector<vector<int>> adj(states.size());
 for(size_t i=0;i<states.size();i++){
  S s=decode(states[i]);
  for(int x=0;x<13;x++)if(s[x])for(int y=0;y<13;y++)if(!s[y]){
   S t=s;swap(t[x],t[y]);
   if(!crossfree(t,blocks))continue;
   auto it=index.find(canonical(t));assert(it!=index.end());
   adj[i].push_back(it->second);
  }
  sort(adj[i].begin(),adj[i].end());adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
 }
 long long degree_sum=0;
 for(size_t i=0;i<states.size();i++){
  degree_sum+=adj[i].size();
  for(int j:adj[i])assert(binary_search(adj[j].begin(),adj[j].end(),(int)i));
 }
 assert(degree_sum%2==0);
 vector<bool> seen(states.size());map<int,int> component_count;
 map<pair<int,vector<pair<int,int>>>,int> component_profiles;
 for(size_t i=0;i<states.size();i++)if(!seen[i]){
  queue<int> q;q.push(i);seen[i]=1;
  int size=0;map<int,int> hist;
  while(!q.empty()){
   int u=q.front();q.pop();size++;hist[(int)adj[u].size()]++;
   for(int w:adj[u])if(!seen[w]){seen[w]=1;q.push(w);}
  }
  component_count[size]++;
  vector<pair<int,int>> h(hist.begin(),hist.end());component_profiles[{size,h}]++;
 }
 cout<<"crossfree="<<states.size()<<" edges="<<(degree_sum/2)<<" components=";
 for(auto [size,m]:component_count)cout<<size<<":"<<m<<",";
 cout<<" small_profiles=";
 for(auto [profile,m]:component_profiles)if(profile.first<100)
  {cout<<"size"<<profile.first<<" count"<<m<<" degrees[";for(auto [d,num]:profile.second)cout<<d<<":"<<num<<",";cout<<"]";}
 cout<<"\n";
}
int main(){
 auto a=cyclic(),b=switched(a);
 S witness_c{}, witness_n{};
 for(int x: {0,1,2}){witness_c[x]=1;witness_n[x]=1;}
 for(int x: {3,4,7}){witness_c[x]=2;witness_n[x]=2;}
 for(int x: {6,8,11})witness_c[x]=3;
 for(int x: {8,10,11})witness_n[x]=3;
 assert(crossfree(witness_c,a)&&crossfree(witness_n,b));
 cout<<"cyclic ";run(a);cout<<"noncyclic ";run(b);}
