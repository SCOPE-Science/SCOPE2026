// Independent Hamiltonian LCF description and white-set forcing enumeration.
// This version does not use the point-line incidence construction to build edges.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr U ALL=(U(1)<<54)-1;
int nbr[54][3],degree[54]={};
void add(int a,int b){assert(a!=b&&degree[a]<3&&degree[b]<3);nbr[a][degree[a]++]=b;nbr[b][degree[b]++]=a;}
void graph(){
 for(int j=0;j<54;j++)add(j,(j+1)%54);
 constexpr int shift[6]={-25,7,-7,13,-13,25};
 for(int j=0;j<54;j++){
  int k=(j+54+shift[j%6])%54;
  if(j<k)add(j,k);
 }
 for(int i=0;i<54;i++)assert(degree[i]==3);
}
// Returns total number of rounds INCLUDING domination, or -1 on failure.
int forcing(const int *a,int k){
 U white=ALL;
 for(int j=0;j<k;j++){
  int v=a[j];white&=~(U(1)<<v);
  for(int h=0;h<3;h++)white&=~(U(1)<<nbr[v][h]);
 }
 for(int round=1;round<=55;round++){
  if(white==0)return round;
  U forced=0;
  for(int v=0;v<54;v++)if(!(white>>v&1)){
   int count=0,last=-1;
   for(int h=0;h<3;h++)if(white>>nbr[v][h]&1){count++;last=nbr[v][h];}
   if(count==1)forced|=U(1)<<last;
  }
  if(!forced)return -1;
  white&=~forced;
 }
 return -1;
}
struct DSU{
 vector<int> parent,sz;
 DSU(int n):parent(n),sz(n,1){iota(parent.begin(),parent.end(),0);}
 int find(int x){while(parent[x]!=x){parent[x]=parent[parent[x]];x=parent[x];}return x;}
 void unite(int a,int b){a=find(a);b=find(b);if(a==b)return;if(sz[a]<sz[b])swap(a,b);parent[b]=a;sz[a]+=sz[b];}
};
int main(){
 graph();
 long long cells[7][11]={};vector<U> opt;
 for(int k:{5,6}){
  int tuple[6]={0,1,2,3,4,5};long long checked=0,good=0;
  for(;;){
   int t=forcing(tuple,k);checked++;
   if(t>=0){good++;if(k==6){
    U m=0;int pointCount=0;
    for(int j=0;j<k;j++){m|=U(1)<<tuple[j];pointCount+=(tuple[j]%2==0);}
    opt.push_back(m);assert(t<=10);cells[pointCount][t]++;
   }}
   int j=k-1;while(j>=0 && tuple[j]==54-k+j)j--;
   if(j<0)break;tuple[j]++;for(int a=j+1;a<k;a++)tuple[a]=tuple[a-1]+1;
  }
  assert(checked==(k==5?3162510:25827165));
  assert(good==(k==5?0:880632));
  cout<<"k="<<k<<" candidates="<<checked<<" success="<<good<<"\n";
 }
 const long long expect[3][6]={
  {15552,83592,63504,33696,16200,0},
  {36288,180144,126360,73872,31104,1296},
  {13608,96552,65448,33048,9072,1296}
 };
 for(int j=0;j<=6;j++)for(int t=1;t<=10;t++){
  long long target=(j>=2&&j<=4&&t>=5)?expect[j-2][t-5]:0;
  assert(cells[j][t]==target);
 }
 unordered_map<U,int> at;at.reserve(opt.size()*2);
 for(int i=0;i<(int)opt.size();i++)at.emplace(opt[i],i);
 DSU dsu(opt.size());long long edges=0;long long histdeg[20]={};
 for(int i=0;i<(int)opt.size();i++){
  U m=opt[i];int d=0;
  for(int v=0;v<54;v++)if(m>>v&1)
   for(int h=0;h<3;h++){
    int w=nbr[v][h];if(m>>w&1)continue;
    U target=(m&~(U(1)<<v))|(U(1)<<w);
    auto found=at.find(target);
    if(found!=at.end()){
     ++d;if(found->second>i){edges++;dsu.unite(i,found->second);}
    }
   }
  assert(d<20);histdeg[d]++;
 }
 const long long expected_deg[13]={0,0,0,0,77760,0,58968,182736,316872,130896,92016,9072,12312};
 for(int i=0;i<20;i++)assert(histdeg[i]==(i<13?expected_deg[i]:0));
 int components=0;for(int i=0;i<(int)opt.size();i++)if(dsu.find(i)==i){components++;assert(dsu.sz[i]==(int)opt.size());}
 assert(edges==3412368&&components==1);
 cout<<"slide_vertices="<<opt.size()<<" slide_edges="<<edges<<" slide_components="<<components<<"\n";
 cout<<"PASS\n";
}
