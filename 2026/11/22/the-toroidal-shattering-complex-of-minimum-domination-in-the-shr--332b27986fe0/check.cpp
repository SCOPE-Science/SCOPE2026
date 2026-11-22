// Standalone enumeration: independent bitmask implementation of domination and trace tests.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 constexpr int N=16, FULL=(1<<16)-1;
 auto bit=[](int i){return 1<<i;};
 auto xx=[](int i){return i/4;}; auto yy=[](int i){return i%4;};
 auto adj=[&](int a,int b){
  int dx=(xx(b)-xx(a)+4)%4,dy=(yy(b)-yy(a)+4)%4;
  return (dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||(dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3);
 };
 int Ncl[N]={};
 for(int i=0;i<N;++i)for(int j=0;j<N;++j)if(i==j||adj(i,j))Ncl[i]|=bit(j);
 vector<int> D;
 for(int i=0;i<N;++i)for(int j=i+1;j<N;++j)for(int k=j+1;k<N;++k)
  if((Ncl[i]|Ncl[j]|Ncl[k])==FULL)D.push_back(bit(i)|bit(j)|bit(k));
 assert(D.size()==32);
 for(int i=0;i<N;++i)for(int j=i+1;j<N;++j)assert((Ncl[i]|Ncl[j])!=FULL);
 int freq[17]={},E[16][16]={},tri=0;
 for(int s=0;s<=FULL;++s){
  int count=__builtin_popcount((unsigned)s);
  if(count>3)continue;
  unsigned char trace[65536]={},unique=0;
  for(auto d:D){
   int pattern=d&s;
   if(!trace[pattern]){trace[pattern]=1;++unique;}
  }
  if(unique==(1<<count)){
   ++freq[count];
   if(count==2){int i=__builtin_ctz((unsigned)s),j=__builtin_ctz((unsigned)(s&~bit(i)));E[i][j]=E[j][i]=1;}
   if(count==3)++tri;
  }
 }
 assert(freq[0]==1&&freq[1]==16&&freq[2]==48&&freq[3]==32&&tri==32);
 for(int i=0;i<N;++i){int deg=0;for(int j=0;j<N;++j)deg+=E[i][j];assert(deg==6);}
 int triCount=0;
 for(int i=0;i<N;++i)for(int j=i+1;j<N;++j)for(int k=j+1;k<N;++k)
   if(E[i][j]&&E[i][k]&&E[j][k])++triCount;
 assert(triCount==32);
 cout<<"minimum_cardinality=3; minimum_concepts="<<D.size()<<"\n";
 cout<<"shattered_supports="<<freq[0]<<","<<freq[1]<<","<<freq[2]<<","<<freq[3]<<"\n";
 cout<<"shattered_pair_graph_edges="<<freq[2]<<"; triangles="<<triCount<<"\n";
 cout<<"PASS\n";
}
