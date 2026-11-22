// Exact census of locally identifying 4-colourings of the Fano incidence graph.
// Compile: g++ -std=c++17 -O3 fano_lid_exact.cpp -o fano_lid_exact
// Run: ./fano_lid_exact
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using Word = array<unsigned char,14>;
struct DSU { vector<int> p,s; explicit DSU(int n):p(n),s(n,1){iota(p.begin(),p.end(),0);} int root(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;} void join(int a,int b){a=root(a);b=root(b);if(a!=b){if(s[a]<s[b])swap(a,b);p[b]=a;s[a]+=s[b];}} };
vector<int> adj[14];vector<pair<int,int>> edge_list;
int color_of[14],order_v[14]={0,7,8,10,1,2,3,4,5,6,9,11,12,13};
vector<Word> states;
int pop(int mask){return __builtin_popcount((unsigned)mask);}
uint32_t code(const Word& w){uint32_t z=0;for(int i=13;i>=0;--i)z=4*z+w[i];return z;}
bool acceptable_partial(){
 for(auto [u,v]:edge_list){
  if(color_of[u]>=0&&color_of[v]>=0&&color_of[u]==color_of[v])return false;
  int mask_u=0,mask_v=0;bool done_u=true,done_v=true;
  for(int t:adj[u])if(color_of[t]<0){done_u=false;break;}else mask_u|=1<<color_of[t];
  if(color_of[u]<0)done_u=false;else mask_u|=1<<color_of[u];
  if(!done_u)continue;
  for(int t:adj[v])if(color_of[t]<0){done_v=false;break;}else mask_v|=1<<color_of[t];
  if(color_of[v]<0)done_v=false;else mask_v|=1<<color_of[v];
  if(done_v&&mask_u==mask_v)return false;
 }
 return true;
}
void enumerate(int p){
 if(p==14){Word w{};for(int i=0;i<14;i++)w[i]=(unsigned char)color_of[i];states.push_back(w);return;}
 const int v=order_v[p];
 for(int a=0;a<4;a++){color_of[v]=a;if(acceptable_partial())enumerate(p+1);}
 color_of[v]=-1;
}
int main(){
 for(int i=0;i<7;i++)for(int d:{0,1,3}){
  int u=(i+d)%7,v=7+i;adj[u].push_back(v);adj[v].push_back(u);edge_list.push_back({u,v});
 }
 assert(edge_list.size()==21);for(auto &a:adj)assert(a.size()==3);
 fill(color_of,color_of+14,-1);enumerate(0);
 unordered_map<uint32_t,int> lookup;lookup.reserve(states.size()*2);
 map<array<int,3>,int> profiles;
 for(int i=0;i<(int)states.size();i++){
  auto &w=states[i];assert(lookup.emplace(code(w),i).second);
  int p=0,l=0;for(int j=0;j<7;j++){p|=1<<w[j];l|=1<<w[7+j];}
  profiles[{pop(p),pop(l),pop(p&l)}]++;
 }
 const int n=states.size();DSU single(n),double_move(n);
 long long single_edges=0,double_edges=0;
 for(int i=0;i<n;i++){
  const Word& w=states[i];const uint32_t base=code(w);
  uint32_t place[14];place[0]=1;for(int j=1;j<14;j++)place[j]=4*place[j-1];
  for(int u=0;u<14;u++)for(int a=0;a<4;a++)if(a!=w[u]){
   uint32_t changed=base+(a-(int)w[u])*place[u];
   auto it=lookup.find(changed);
   if(it!=lookup.end() && it->second>i){single.join(i,it->second);double_move.join(i,it->second);single_edges++;}
  }
  for(int u=0;u<14;u++)for(int v=u+1;v<14;v++)
   for(int a=0;a<4;a++)if(a!=w[u])for(int b=0;b<4;b++)if(b!=w[v]){
    uint32_t changed=base+(a-(int)w[u])*place[u]+(b-(int)w[v])*place[v];
    auto it=lookup.find(changed);
    if(it!=lookup.end() && it->second>i){double_move.join(i,it->second);double_edges++;}
   }
 }
 map<int,vector<int>> components;for(int i=0;i<n;i++)components[single.root(i)].push_back(i);
 map<int,int> sizes;set<string> large_ids,small_ids;
 for(auto &[root,vec]:components){
  int ncomp=vec.size();sizes[ncomp]++;
  if(ncomp!=6860&&ncomp!=882)continue;
  set<string> markers;
  for(int state_id:vec){const Word &w=states[state_id];int p=0,l=0;
   for(int j=0;j<7;j++){p|=1<<w[j];l|=1<<w[7+j];}
   if(ncomp==882){
    if(pop(p)==1)markers.insert("P"+to_string(p));
    else if(pop(l)==1)markers.insert("L"+to_string(l));
    else {cerr<<"unexpected 882 profile\n";return 2;}
   }else{
    int core=(pop(p)==2?p:(p&(~l)));
    assert(pop(core)==2);markers.insert(to_string(core));
   }
  }
  assert(markers.size()==1);
  if(ncomp==882)small_ids.insert(*markers.begin());else large_ids.insert(*markers.begin());
 }
 set<int> double_roots;for(int i=0;i<n;i++)double_roots.insert(double_move.root(i));
 cout<<"valid_named_4="<<n<<"\n";
 cout<<"profiles_point_line_shared:";
 for(auto [profile,count]:profiles)cout<<" ("<<profile[0]<<","<<profile[1]<<","<<profile[2]<<")="<<count;
 cout<<"\n";
 cout<<"single_change_edges="<<single_edges<<"\n";
 cout<<"single_change_component_sizes:";
 for(auto [size,count]:sizes)cout<<" "<<size<<"x"<<count;
 cout<<"\n";
 cout<<"components_882_identifiers="<<small_ids.size()<<" components_6860_identifiers="<<large_ids.size()<<"\n";
 cout<<"exact_two_change_edges="<<double_edges<<"\n";
 cout<<"up_to_two_change_components="<<double_roots.size()<<"\n";
 assert(n==54264);
 assert((profiles==map<array<int,3>,int>{{{1,3,0},3528},{{2,2,0},29064},{{2,3,1},6048},{{3,1,0},3528},{{3,2,1},6048},{{3,3,2},6048}}));
 assert(single_edges==185808);
 assert((sizes==map<int,int>{{1,6048},{882,8},{6860,6}}));
 assert(small_ids.size()==8&&large_ids.size()==6);
 assert(double_edges==897456&&double_roots.size()==1);
 cout<<"checks_passed\n";
}
