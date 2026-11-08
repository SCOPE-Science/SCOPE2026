#include <cstdint>
#include <array>
#include <vector>
#include <unordered_map>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <cassert>
using namespace std;
constexpr int N=4, V=16, E=32;
using A=array<int8_t,E>;
vector<uint32_t> states;
struct Inc {int e; int want;};
array<array<Inc,4>,V> incident;

void recurse(A a){
 bool changed=true;
 while(changed){
  changed=false;
  for(int v=0;v<V;v++){
   int out=0,unk=0;
   for(auto [e,want]:incident[v])if(a[e]<0)unk++;else out+=(a[e]==want);
   if(out>2 || out+unk<2)return;
   if(unk && (out==2 || out+unk==2)){
    for(auto [e,want]:incident[v]) if(a[e]<0){
     int val=(out==2)?1-want:want;
     if(a[e]>=0 && a[e]!=val)return;
     if(a[e]<0){a[e]=val;changed=true;}
    }
   }
  }
 }
 int e=0;
 while(e<E && a[e]>=0)e++;
 if(e==E){
  uint32_t bits=0;
  for(int i=0;i<E;i++)if(a[i])bits|=uint32_t(1)<<i;
  states.push_back(bits);return;
 }
 for(int b=0;b<2;b++){a[e]=b;recurse(a);}
}

int main(){
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){
  int v=i*N+j;
  incident[v]={Inc{v,1},Inc{i*N+(j+N-1)%N,0},Inc{V+v,1},Inc{V+((i+N-1)%N)*N+j,0}};
 }
 A a;a.fill(-1);recurse(a);
 sort(states.begin(),states.end());states.erase(unique(states.begin(),states.end()),states.end());
 assert(states.size()==2970);
 unordered_map<uint32_t,int> index;
 for(int k=0;k<(int)states.size();k++)index[states[k]]=k;
 vector<vector<int>> g(states.size());
 vector<pair<int,int>> flux(states.size());
 auto bit=[](uint32_t x,int b){return int((x>>b)&1);};
 for(int k=0;k<(int)states.size();k++){
  uint32_t s=states[k];int fa=0,fb=0;
  for(int i=0;i<N;i++)fa+=bit(s,i*N);
  for(int j=0;j<N;j++)fb+=bit(s,V+j);
  flux[k]={fa,fb};
  for(int i=0;i<N;i++)for(int j=0;j<N;j++){
   int row2=(i+1)%N, col2=(j+1)%N;
   int top=i*N+j,right=V+i*N+col2,bottom=row2*N+j,left=V+i*N+j;
   int topb=bit(s,top),rightb=bit(s,right),bottomb=bit(s,bottom),leftb=bit(s,left);
   if((topb==rightb)&&(bottomb==leftb)&&(topb!=bottomb)){
    uint32_t t=s^((uint32_t(1)<<top)|(uint32_t(1)<<right)|(uint32_t(1)<<bottom)|(uint32_t(1)<<left));
    auto it=index.find(t); assert(it!=index.end());
    g[k].push_back(it->second);
   }
  }
 }
 int edges=0;for(auto &ns:g)edges+=ns.size();assert(edges%2==0);
 cout<<"STATES "<<states.size()<<" EDGES "<<edges/2<<'\n';
 vector<int> comp(states.size(),-1);
 vector<vector<int>> comps;
 map<pair<int,int>,vector<int>> sectors;
 for(int s=0;s<(int)states.size();s++)if(comp[s]<0){
  int cid=comps.size();vector<int> c;queue<int>q;q.push(s);comp[s]=cid;
  while(!q.empty()){
   int v=q.front();q.pop();c.push_back(v);
   for(int u:g[v])if(comp[u]<0){comp[u]=cid;q.push(u);}
  }
  for(int v:c)assert(flux[v]==flux[s]);
  sectors[flux[s]].push_back(c.size());comps.push_back(c);
 }
 map<int,int> component_sizes;
 for(auto &c:comps)component_sizes[c.size()]++;
 cout<<"COMPONENT_SIZES";for(auto [k,v]:component_sizes)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"FLUX";
 for(auto &[ab,sizes]:sectors){sort(sizes.begin(),sizes.end());cout<<" ("<<ab.first<<","<<ab.second<<"):";for(int x:sizes)cout<<x<<",";}cout<<"\n";
 for(auto &c:comps)if(c.size()>1){
  int rad=100000,diam=0;map<int,int> ecc;map<int,long long> dist;
  for(int s:c){
   vector<int> d(states.size(),-1);queue<int>q;q.push(s);d[s]=0;int mx=0;
   while(!q.empty()){
    int v=q.front();q.pop();
    for(int u:g[v])if(d[u]<0){d[u]=d[v]+1;mx=max(mx,d[u]);q.push(u);}
   }
   rad=min(rad,mx);diam=max(diam,mx);ecc[mx]++;
   for(int t:c)if(t>s){assert(d[t]>=0);dist[d[t]]++;}
  }
  long long total=0;for(auto [k,v]:dist)total+=v;
  assert(total==static_cast<long long>(c.size())*(static_cast<long long>(c.size())-1)/2);
  cout<<"SECTOR "<<flux[c[0]].first<<","<<flux[c[0]].second<<" SIZE "<<c.size()<<" RAD "<<rad<<" DIAM "<<diam<<" ECC";
  for(auto [k,v]:ecc)cout<<" "<<k<<":"<<v;
  cout<<" DIST";for(auto [k,v]:dist)cout<<" "<<k<<":"<<v;cout<<"\n";
 }
}
