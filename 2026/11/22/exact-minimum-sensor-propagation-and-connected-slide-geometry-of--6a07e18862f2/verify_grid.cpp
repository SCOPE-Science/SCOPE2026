// Exact enumeration of minimum power domination, synchronous forcing times,
// and token-slide connectivity for the Gray point-line incidence graph.
// Standard C++17, no external data files required.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using U = uint64_t;
constexpr U ALL=(U(1)<<54)-1;
U adj[54]={}, closed[54]={};
int point(int a,int b,int c){return 9*a+3*b+c;}
int line(int axis,int a,int b){return 27+9*axis+3*a+b;}
void graph(){
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++){
  int p=point(a,b,c);
  for(int l:{line(0,b,c),line(1,a,c),line(2,a,b)}){
   adj[p]|=U(1)<<l;adj[l]|=U(1)<<p;
  }
 }
 for(int i=0;i<54;i++){closed[i]=adj[i]|U(1)<<i;assert(__builtin_popcountll(adj[i])==3);}
}
// -1 denotes failure; a nonnegative result is the number of rounds AFTER N[S].
int forcing(U S){
 U observed=0;
 for(U s=S;s;s&=s-1)observed|=closed[__builtin_ctzll(s)];
 int t=0;
 while(observed!=ALL){
  U next=observed,white=ALL^observed;
  for(U s=observed;s;s&=s-1){
   U newneighbors=adj[__builtin_ctzll(s)]&white;
   if(newneighbors && (newneighbors&(newneighbors-1))==0)next|=newneighbors;
  }
  if(next==observed)return -1;
  observed=next;++t;
 }
 return t;
}
struct DSU {
 vector<int> parent,size;
 explicit DSU(int n):parent(n),size(n,1){iota(parent.begin(),parent.end(),0);}
 int root(int i){while(parent[i]!=i){parent[i]=parent[parent[i]];i=parent[i];}return i;}
 void join(int x,int y){x=root(x);y=root(y);if(x==y)return;if(size[x]<size[y])swap(x,y);parent[y]=x;size[x]+=size[y];}
};
int main(){
 graph();
 array<array<long long,11>,7> hist{};
 vector<U> successful;
 for(int k:{5,6}){
  int a[6]={0,1,2,3,4,5};long long tested=0,wins=0;
  while(true){
   U S=0;int points=0;for(int j=0;j<k;j++){S|=U(1)<<a[j];points+=(a[j]<27);}
   int t=forcing(S);++tested;
   if(t>=0){++wins;if(k==6){assert(t+1<11);hist[points][t+1]++;successful.push_back(S);}}
   int j=k-1;while(j>=0 && a[j]==54-k+j)--j;
   if(j<0)break;
   ++a[j];for(int u=j+1;u<k;u++)a[u]=a[u-1]+1;
  }
  assert(tested==(k==5?3162510:25827165));
  assert(wins==(k==5?0:880632));
  cout<<"k="<<k<<" tested="<<tested<<" successful="<<wins<<"\n";
 }
 const long long expect[7][11]={
  {},{},
  {0,0,0,0,0,15552,83592,63504,33696,16200,0},
  {0,0,0,0,0,36288,180144,126360,73872,31104,1296},
  {0,0,0,0,0,13608,96552,65448,33048,9072,1296},
  {},{}
 };
 for(int j=0;j<=6;j++)for(int t=0;t<=10;t++)assert(hist[j][t]==expect[j][t]);
 unordered_map<U,int> index;index.reserve(successful.size()*2);
 for(int i=0;i<(int)successful.size();i++)index.emplace(successful[i],i);
 DSU cc(successful.size());array<long long,20> degrees{};long long edges=0;
 for(int i=0;i<(int)successful.size();i++){
  U S=successful[i];int deg=0;
  for(U occupied=S;occupied;occupied&=occupied-1){
   int v=__builtin_ctzll(occupied);
   for(U vacant=adj[v]&~S;vacant;vacant&=vacant-1){
    int w=__builtin_ctzll(vacant);
    U T=(S^(U(1)<<v))|(U(1)<<w);
    auto it=index.find(T);
    if(it!=index.end()){
     ++deg;if(it->second>i){++edges;cc.join(i,it->second);}
    }
   }
  }
  assert(deg<20);degrees[deg]++;
 }
 assert(edges==3412368);
 const long long degree_expected[20]={0,0,0,0,77760,0,58968,182736,316872,130896,92016,9072,12312};
 for(int i=0;i<20;i++)assert(degrees[i]==degree_expected[i]);
 int components=0;for(int i=0;i<(int)successful.size();i++)if(cc.root(i)==i){components++;assert(cc.size[i]==(int)successful.size());}
 assert(components==1);
 cout<<"slide_vertices="<<successful.size()<<" slide_edges="<<edges<<" slide_components="<<components<<"\n";
 for(int j=2;j<=4;j++)for(int t=5;t<=10;t++)if(hist[j][t])cout<<"points="<<j<<" round_index="<<t<<" count="<<hist[j][t]<<"\n";
 cout<<"PASS\n";
}
