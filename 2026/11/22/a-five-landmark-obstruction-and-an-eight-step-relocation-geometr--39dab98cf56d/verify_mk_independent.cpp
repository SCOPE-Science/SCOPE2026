// Independent exhaustive checker for GP(8,3), C++17 standard library only.
// Resolving is tested by hitting each pairwise distinguishing-vertex mask.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
int main(){
 const int N=16;
 bool adj[N][N]{};
 auto add=[&](int a,int b){adj[a][b]=adj[b][a]=true;};
 for(int i=0;i<8;i++){
  add(i,(i+1)%8);
  add(i,8+i);
  add(8+i,8+(i+3)%8);
 }
 vector<pair<int,int>> edges;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)if(adj[a][b])edges.push_back({a,b});
 assert(edges.size()==24);
 int d[N][N];
 for(int a=0;a<N;a++)for(int b=0;b<N;b++)d[a][b]=a==b?0:(adj[a][b]?1:1000);
 for(int k=0;k<N;k++)for(int a=0;a<N;a++)for(int b=0;b<N;b++)d[a][b]=min(d[a][b],d[a][k]+d[k][b]);
 int de[16][24];
 for(int v=0;v<N;v++)for(int j=0;j<24;j++)de[v][j]=min(d[v][edges[j].first],d[v][edges[j].second]);
 vector<unsigned> pair_witness;
 for(int i=0;i<24;i++)for(int j=i+1;j<24;j++){
  unsigned mask=0;
  for(int v=0;v<N;v++)if(de[v][i]!=de[v][j])mask|=1u<<v;
  pair_witness.push_back(mask);
 }
 assert(pair_witness.size()==276);
 vector<unsigned> dom_witness(24);
 for(int j=0;j<24;j++){
  auto [a,b]=edges[j];
  for(int v=0;v<N;v++)if(v==a||v==b||adj[v][a]||adj[v][b])dom_witness[j]|=1u<<v;
 }
 array<int,17> combined{},edonly{},veonly{};
 vector<unsigned> optimum;
 for(unsigned mask=0;mask<65536;mask++){
  bool ve=true,er=true;
  for(unsigned witness:dom_witness)if(!(mask&witness)){ve=false;break;}
  for(unsigned witness:pair_witness)if(!(mask&witness)){er=false;break;}
  int k=__builtin_popcount(mask);
  if(ve)veonly[k]++;
  if(er)edonly[k]++;
  if(er&&ve){combined[k]++;if(k==5)optimum.push_back(mask);}
 }
 const array<int,17> want={0,0,0,0,0,512,3432,8560,11790,11200,7984,4368,1820,560,120,16,1};
 assert(combined==want&&veonly[4]==128&&edonly[4]==368);
 assert(optimum.size()==512);
 unordered_map<unsigned,int> lookup;
 for(int i=0;i<(int)optimum.size();i++)lookup[optimum[i]]=i;
 for(int mode=0;mode<2;mode++){
  vector<vector<int>> g(512);
  for(int i=0;i<512;i++)for(int a=0;a<N;a++)if((optimum[i]>>a)&1u)
   for(int b=0;b<N;b++)if(!((optimum[i]>>b)&1u)&&(mode||adj[a][b])){
    unsigned altered=optimum[i]^(1u<<a)^(1u<<b);
    auto it=lookup.find(altered);
    if(it!=lookup.end())g[i].push_back(it->second);
   }
  int twice_edges=0,diam=0,rad=512,ecc5=0,ecc8=0;
  for(auto &v:g)twice_edges+=v.size();
  for(int i=0;i<512;i++){
   vector<int> ds(512,-1);queue<int> q;ds[i]=0;q.push(i);
   while(!q.empty()){
    int a=q.front();q.pop();
    for(int b:g[a])if(ds[b]<0){ds[b]=ds[a]+1;q.push(b);}
   }
   assert(find(ds.begin(),ds.end(),-1)==ds.end());
   int e=*max_element(ds.begin(),ds.end());diam=max(diam,e);rad=min(rad,e);
   ecc5+=(e==5);ecc8+=(e==8);
  }
  if(mode==0){assert(twice_edges==2640&&rad==8&&diam==8&&ecc8==512);}
  else{assert(twice_edges==7232&&rad==5&&diam==6&&ecc5==368);}
  cout<<(mode?"JUMP":"SLIDE")<<" edges="<<twice_edges/2<<" radius="<<rad<<" diameter="<<diam<<"\n";
 }
 cout<<"INDEPENDENT_PAIR_HITTING_CHECK_OK"<<endl;
}
