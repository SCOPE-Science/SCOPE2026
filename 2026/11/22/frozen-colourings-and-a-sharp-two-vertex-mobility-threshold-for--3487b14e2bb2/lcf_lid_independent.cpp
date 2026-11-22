// Separate finite enumeration using a 14-cycle with seven length-five chords.
// Compile: g++ -std=c++17 -O3 lcf_lid_independent.cpp -o lcf_lid_independent
// Run: ./lcf_lid_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
static bool linked[14][14]{};
static int digits[14];
static array<int,14> nbrmask{};
static vector<uint32_t> approved;
static long long proper=0;
void add(int a,int b){linked[a][b]=linked[b][a]=true;}
bool legal_end(){
 int colors[14]{};
 for(int x=0;x<14;x++){
  colors[x]=1<<digits[x];
  for(int y=0;y<14;y++)if(linked[x][y])colors[x]|=1<<digits[y];
 }
 for(int x=0;x<14;x++)for(int y=x+1;y<14;y++)if(linked[x][y] && colors[x]==colors[y])return false;
 return true;
}
void generate(int position,uint32_t index){
 if(position==14){proper++;if(legal_end())approved.push_back(index);return;}
 for(int a=0;a<4;a++){
  bool good=true;for(int y=0;y<position;y++)if(linked[position][y]&&digits[y]==a){good=false;break;}
  if(good){digits[position]=a;generate(position+1,index|(uint32_t(a)<<(2*position)));}
 }
}
int main(){
 for(int x=0;x<14;x++)add(x,(x+1)%14);
 for(int x=0;x<14;x+=2)add(x,(x+5)%14);
 int edges=0;for(int x=0;x<14;x++)for(int y=0;y<14;y++){
  if(linked[x][y]){nbrmask[x]|=1<<y;if(x<y)edges++;}
 }
 assert(edges==21);for(int x=0;x<14;x++)assert(__builtin_popcount((unsigned)nbrmask[x])==3);
 generate(0,0);
 unordered_map<uint32_t,int> idx;idx.reserve(approved.size()*2);
 for(int i=0;i<(int)approved.size();i++)idx[approved[i]]=i;
 int N=approved.size();
 vector<vector<int>> adj(N);long long e1=0,e2=0;
 vector<int> parents(N);for(int i=0;i<N;i++)parents[i]=i;
 auto root=[&](int x){while(parents[x]!=x){parents[x]=parents[parents[x]];x=parents[x];}return x;};
 auto join=[&](int x,int y){x=root(x);y=root(y);if(x!=y)parents[x]=y;};
 map<array<int,3>,int> profile;
 for(int i=0;i<N;i++){
  uint32_t x=approved[i];int A=0,B=0;
  for(int v=0;v<14;v++){
   int c=(x>>(2*v))&3;
   if(v%2==0)A|=1<<c;else B|=1<<c;
   for(int b=0;b<4;b++)if(b!=c){
    uint32_t y=(x&(~(3u<<(2*v))))|(uint32_t(b)<<(2*v));
    auto it=idx.find(y);
    if(it!=idx.end()&&it->second>i){adj[i].push_back(it->second);adj[it->second].push_back(i);e1++;}
   }
  }
  profile[{__builtin_popcount((unsigned)A),__builtin_popcount((unsigned)B),__builtin_popcount((unsigned)(A&B))}]++;
  for(int u=0;u<14;u++)for(int v=u+1;v<14;v++){
   uint32_t mask=(3u<<(2*u))|(3u<<(2*v)),other=x&~mask;
   int cu=(x>>(2*u))&3,cv=(x>>(2*v))&3;
   for(int a=0;a<4;a++)if(a!=cu)for(int b=0;b<4;b++)if(b!=cv){
    uint32_t y=other|(uint32_t(a)<<(2*u))|(uint32_t(b)<<(2*v));
    auto it=idx.find(y);if(it!=idx.end()&&it->second>i){join(i,it->second);e2++;}
   }
  }
 }
 map<int,int> sizes;vector<char> seen(N);
 for(int s=0;s<N;s++)if(!seen[s]){
  queue<int> q;q.push(s);seen[s]=1;int sz=0;
  while(!q.empty()) {int v=q.front();q.pop();sz++;for(int w:adj[v])if(!seen[w]){seen[w]=1;q.push(w);}}
  sizes[sz]++;
 }
 int c2=0;for(int i=0;i<N;i++)if(root(i)==i)c2++;
 cout<<"LCF_named4="<<N<<" proper="<<proper<<"\n";
 cout<<"LCF_profiles:";for(auto [p,c]:profile)cout<<" ("<<p[0]<<","<<p[1]<<","<<p[2]<<")="<<c;cout<<"\n";
 cout<<"LCF_edges1="<<e1<<" edges2="<<e2<<"\n";
 cout<<"LCF_one_change_components:";for(auto [s,c]:sizes)cout<<" "<<s<<"x"<<c;cout<<"\n";
 // The pair-change relation already contains all one-change edges in the same
 // connected set: each one-change edge has a two-change detour when needed.
 cout<<"LCF_exact_two_change_components="<<c2<<"\n";
 assert(N==54264&&e1==185808&&e2==897456&&c2==1);
 assert((sizes==map<int,int>{{1,6048},{882,8},{6860,6}}));
 assert((profile==map<array<int,3>,int>{{{1,3,0},3528},{{2,2,0},29064},{{2,3,1},6048},{{3,1,0},3528},{{3,2,1},6048},{{3,3,2},6048}}));
 cout<<"independent_checks_passed\n";
}
