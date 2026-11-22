// Exact finite checks of a local characterization of distance-equalizer sets on trees.
// Standard C++17: g++ -O2 -std=c++17 verify_trees.cpp -o verify_trees && ./verify_trees
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
static uint64_t seed64=0xdecaf123456789abULL;
uint64_t rng(){seed64^=seed64<<13;seed64^=seed64>>7;seed64^=seed64<<17;return seed64;}
vector<vector<int>> from_prufer(int n,vector<int> p){vector<vector<int>> g(n);vector<int> degree(n,1);for(int x:p)degree[x]++;
for(int x:p){int leaf=0;while(degree[leaf]!=1)leaf++;g[x].push_back(leaf);g[leaf].push_back(x);degree[x]--;degree[leaf]--;}
int x=0,y=0;while(degree[x]!=1)x++;y=x+1;while(degree[y]!=1)y++;g[x].push_back(y);g[y].push_back(x);return g;}
void check(vector<vector<int>> const& g, uint64_t &samples, uint64_t &part_good, uint64_t &two_good){int n=(int)g.size();vector<int> color(n,-1), degree(n);vector<vector<int>> dist(n,vector<int>(n,-1));queue<int> q;q.push(0);color[0]=0;while(!q.empty()){int u=q.front();q.pop();for(int v:g[u])if(color[v]<0){color[v]=1-color[u];q.push(v);}};
for(int u=0;u<n;u++){degree[u]=g[u].size();q.push(u);dist[u][u]=0;while(!q.empty()){int v=q.front();q.pop();for(int w:g[v])if(dist[u][w]<0){dist[u][w]=dist[u][v]+1;q.push(w);}}}
uint32_t part[2]={0,0};bool good[2]={true,true};for(int v=0;v<n;v++){part[color[v]]|=1u<<v;if(degree[v]==2 && degree[g[v][0]]!=1 && degree[g[v][1]]!=1)good[1-color[v]]=false;}
vector<uint32_t> equalmask;vector<pair<int,int>> pairs;for(int x=0;x<n;x++)for(int y=0;y<x;y++){uint32_t m=0;for(int z=0;z<n;z++)if(dist[z][x]==dist[z][y])m|=1u<<z;pairs.push_back({x,y});equalmask.push_back(m);}
int minsize=n+1;bool actualGood[2]={false,false};bool both=good[0]&&good[1];for(uint32_t s=0;s<(1u<<n);s++){bool equal=true;for(unsigned j=0;j<pairs.size();j++){auto [x,y]=pairs[j];if(!(s&(1u<<x)) && !(s&(1u<<y)) && !(s&equalmask[j])){equal=false;break;}}if(equal)minsize=min(minsize,__builtin_popcount(s));if(s==part[0])actualGood[0]=equal;if(s==part[1])actualGood[1]=equal;if(both && equal != ((s&part[0])==part[0]||(s&part[1])==part[1])){cerr<<"ALL_SET_FAILURE n="<<n<<"\n";exit(1);}}
if(actualGood[0]!=good[0]||actualGood[1]!=good[1]){cerr<<"CLASS_FAILURE n="<<n<<"\n";exit(1);}int low=min(__builtin_popcount(part[0]),__builtin_popcount(part[1]));bool predicted=(__builtin_popcount(part[0])==low&&good[0])||(__builtin_popcount(part[1])==low&&good[1]);if((minsize==low)!=predicted){cerr<<"MINIMUM_FAILURE n="<<n<<"\n";exit(1);}samples++;part_good+=actualGood[0]+actualGood[1];two_good+=both;}
int main(){uint64_t samples=0,pg=0,bg=0;for(int n=2;n<=7;n++){int ways=1;for(int i=0;i<n-2;i++)ways*=n;for(int id=0;id<ways;id++){int t=id;vector<int> code;for(int i=0;i<n-2;i++){code.push_back(t%n);t/=n;}check(from_prufer(n,code),samples,pg,bg);}}
for(int n=8;n<=12;n++)for(int j=0;j<100;j++){vector<int> code;for(int i=0;i<n-2;i++)code.push_back((int)(rng()%n));check(from_prufer(n,code),samples,pg,bg);}
cout<<"TREE_LOCAL_EQUALIZER_VERIFY_OK trees="<<samples<<" part_classes_valid="<<pg<<" both_classes_valid="<<bg<<"\n";}
