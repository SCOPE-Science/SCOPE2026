#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct Edge {array<int,4> x;};
int code3(const Edge&e,int from){return 9*e.x[from]+3*e.x[from+1]+e.x[from+2];}
int main(){
 vector<array<Edge,2>> pairs;
 for(int v=0;v<81;v++){
  Edge e;int z=v;for(int i=3;i>=0;i--){e.x[i]=z%3;z/=3;}
  Edge ne=e;int nv=0;for(int i=0;i<4;i++){ne.x[i]=(3-e.x[i])%3;nv=3*nv+ne.x[i];}
  if(v<nv)pairs.push_back({e,ne});
 }
 assert(pairs.size()==40);
 vector<int> reps;for(int v=1;v<27;v++){
  int t=v, d[3];for(int i=2;i>=0;i--){d[i]=t%3;t/=3;}
  int nv=9*((3-d[0])%3)+3*((3-d[1])%3)+((3-d[2])%3);
  if(v<nv)reps.push_back(v);
 }
 assert(reps.size()==13);
 array<int,27> pos;pos.fill(-1);for(int i=0;i<13;i++)pos[reps[i]]=i;
 array<array<int,13>,40> deltas{};array<array<int,13>,40> initial{};
 array<array<int,2>,40> countone{};
 for(int j=0;j<40;j++)for(int t=0;t<2;t++){
  auto &e=pairs[j][t];int a=code3(e,0),b=code3(e,1);
  for(int v=0;v<13;v++){int rep=reps[v];int d=(a==rep)-(b==rep);if(t==0)initial[j][v]=d;else deltas[j][v]=d-initial[j][v];}
  countone[j][t]=(e.x[0]==1);
 }
 struct Entry{uint64_t key;uint32_t mask;uint8_t cnt;bool operator<(const Entry&other)const{return key<other.key;}};
 auto fill = [&](int a,int b){
  vector<Entry> res;res.reserve(1u<<(b-a));
  array<int,13> f{};int c=0;
  for(int j=a;j<b;j++){for(int v=0;v<13;v++)f[v]+=initial[j][v];c+=countone[j][0];}
  auto keyval=[&](){uint64_t key=0;for(int v=0;v<13;v++){assert(-6<=f[v]&&f[v]<=6);key|=(uint64_t)(f[v]+7)<<(4*v);}return key;};
  res.push_back({keyval(),0u,(uint8_t)c});
  int prev=0;
  for(int i=1;i<(1<<(b-a));i++){
   int gray=i^(i>>1),j=__builtin_ctz((unsigned)(gray^prev))+a;
   bool on=(gray&(1<<(j-a)))!=0;
   for(int v=0;v<13;v++)f[v]+=(on?1:-1)*deltas[j][v];
   c+=(on?1:-1)*(countone[j][1]-countone[j][0]);
   res.push_back({keyval(),(uint32_t)gray,(uint8_t)c});prev=gray;
  }
  sort(res.begin(),res.end());return res;
 };
 vector<Entry> left=fill(0,20), right=fill(20,40);
 unsigned long long hist[28]={}, connectedHist[28]={}, disconnected[28]={};
 auto connected = [&](uint32_t lm,uint32_t rm){
  int parent[27], degree[27]{};
  for(int i=0;i<27;i++)parent[i]=i;
  auto findroot = [&](int x){while(parent[x]!=x)x=parent[x]=parent[parent[x]];return x;};
  for(int j=0;j<40;j++){
   int bit = (j<20)? ((lm>>j)&1):((rm>>(j-20))&1);
   auto &e=pairs[j][bit];int a=code3(e,0),b=code3(e,1);
   degree[a]++;degree[b]++;
   parent[findroot(a)]=findroot(b);
  }
  int root=-1;
  for(int i=0;i<27;i++)if(degree[i]){
   if(root==-1)root=findroot(i);
   else if(root!=findroot(i))return false;
  }
  return true;
 };

 for(size_t i=0;i<left.size();){
  size_t j=i;while(j<left.size()&&left[j].key==left[i].key)j++;
  uint64_t negkey=0;
  for(int v=0;v<13;v++){
   int digit=(left[i].key>>(v*4))&15;
   int opp=14-digit;assert(opp>=0&&opp<=15);
   negkey|=(uint64_t)opp<<(v*4);
  }
  auto it=lower_bound(right.begin(),right.end(),Entry{negkey,0,0});
  if(it!=right.end()&&it->key==negkey){
   size_t k=it-right.begin(),l=k;
   while(l<right.size()&&right[l].key==negkey)l++;
   unsigned long long x[28]={},y[28]={};
   for(size_t z=i;z<j;z++)x[left[z].cnt]++;
   for(size_t z=k;z<l;z++)y[right[z].cnt]++;
   for(int a=0;a<28;a++)for(int b=0;b+a<28;b++)hist[a+b]+=x[a]*y[b];
   for(size_t z=i;z<j;z++)for(size_t w=k;w<l;w++){
    int count=left[z].cnt+right[w].cnt;
    if(connected(left[z].mask,right[w].mask))connectedHist[count]++;
    else disconnected[count]++;
   }
  }
  i=j;
 }
 unsigned long long total=0;
 for(int i=0;i<28;i++){if(hist[i])cout<<i<<","<<hist[i]<<"\n";total+=hist[i];}
 cout<<"total,"<<total<<"\n";
 unsigned long long sumconnected=0,sumdisconnected=0;
 for(int i=0;i<28;i++)if(hist[i]){
  assert(hist[i]==connectedHist[i]+disconnected[i]);
  cout<<"detail,"<<i<<","<<connectedHist[i]<<","<<disconnected[i]<<"\n";
  sumconnected+=connectedHist[i];sumdisconnected+=disconnected[i];
 }
 cout<<"connected_total,"<<sumconnected<<",disconnected_total,"<<sumdisconnected<<"\n";
}
