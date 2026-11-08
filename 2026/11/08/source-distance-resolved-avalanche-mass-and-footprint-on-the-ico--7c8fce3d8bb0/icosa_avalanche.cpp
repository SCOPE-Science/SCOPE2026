// Standalone finite exhaustive census of one-sink sandpile avalanches
// on the labeled icosahedral graph. No third-party libraries.
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
constexpr int N=12;
static const int ee[][2]={{0,1},{0,5},{0,7},{0,8},{0,11},{1,2},{1,5},{1,6},{1,8},{2,3},{2,6},{2,8},{2,9},{3,4},{3,6},{3,9},{3,10},{4,5},{4,6},{4,10},{4,11},{5,6},{5,11},{7,8},{7,9},{7,10},{7,11},{8,9},{9,10},{10,11}};
array<array<int,5>,12> adj{};
array<array<unsigned char,2048>,11> degreeIn{};
array<int,12> h{};
array<map<pair<int,int>,uint64_t>,3> hist;
uint64_t recurrent=0;
array<uint64_t,3> sinkTopples{};
constexpr int source[3]={1,2,3};
bool burning(){
 int mask=2047;
 while(mask){
  bool progress=false;
  for(int j=0;j<11;j++)if(mask&(1<<j)){
    if(h[j+1]>=degreeIn[j][mask]){mask^=(1<<j);progress=true;break;}
  }
  if(!progress)return false;
 }
 return true;
}
void avalanche(int category){
  int x[12];for(int j=0;j<N;j++)x[j]=h[j];
  ++x[source[category]];
  int num=0,mask=0;
  while(true){
    int v=1;while(v<N && x[v]<5)++v;
    if(v==N)break;
    if(++num>1000){cerr<<"unstable cycle\n";exit(2);}
    x[v]-=5;mask|=1<<(v-1);
    for(int w:adj[v])if(w!=0)++x[w];
    for(int w:adj[v])if(w==0)++sinkTopples[category];
  }
  hist[category][{num,__builtin_popcount((unsigned)mask)}]++;
}
int main(){
  array<int,12> d{};
  for(auto e:ee){adj[e[0]][d[e[0]]++]=e[1];adj[e[1]][d[e[1]]++]=e[0];}
  for(int i=0;i<12;i++)if(d[i]!=5){cerr<<"bad degree\n";return 2;}
  for(int j=0;j<11;j++)for(int mask=0;mask<2048;mask++){
    int cnt=0;for(int w:adj[j+1])if(w!=0 && (mask&(1<<(w-1))))++cnt;
    degreeIn[j][mask]=cnt;
  }
  uint64_t possible=1;for(int j=1;j<12;j++)possible*=5;
  for(uint64_t ii=0;ii<possible;ii++){
    if(burning()){
      ++recurrent;
      for(int cat=0;cat<3;cat++)avalanche(cat);
    }
    for(int j=1;j<12;j++)if(++h[j]<5)break;else h[j]=0;
  }
  cout<<"recurrent "<<recurrent<<"\n";
  for(int cat=0;cat<3;cat++){
    cout<<"distance "<<cat+1<<" sink_firings "<<sinkTopples[cat]<<" terms "<<hist[cat].size()<<"\n";
    for(auto [nk,c]:hist[cat])cout<<nk.first<<","<<nk.second<<":"<<c<<" ";cout<<"\n";
  }
}
