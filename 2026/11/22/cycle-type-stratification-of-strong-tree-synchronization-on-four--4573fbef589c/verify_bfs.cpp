// Exact census of strongly synchronizing full contexts for four-state
// commutative binary algebras with a unary permutation.
// Build: c++ -O3 -std=c++17 verify_bfs.cpp -o verify_bfs
// Run: ./verify_bfs
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
constexpr int P[10][2]={{0,0},{0,1},{0,2},{0,3},{1,1},{1,2},{1,3},{2,2},{2,3},{3,3}};
constexpr int W[5][4]={{0,1,2,3},{1,0,2,3},{1,0,3,2},{1,2,0,3},{1,2,3,0}};
constexpr int MULT[5]={1,6,3,8,6};
constexpr int INF=100;
int main(){
  uint64_t totals[5][12]={};
  int first[5][12];for(auto &r:first)for(int &v:r)v=-1;
  for(int code=0;code<(1<<20);++code){
    int f[4][4];int c=code;
    for(int k=0;k<10;k++){int v=c%4;c/=4;f[P[k][0]][P[k][1]]=f[P[k][1]][P[k][0]]=v;}
    unsigned char bin[16][16]={};
    for(int s=1;s<16;s++)for(int t=1;t<16;t++){
      unsigned x=0;
      for(int i=0;i<4;i++)if(s&(1<<i))
        for(int j=0;j<4;j++)if(t&(1<<j))x|=1u<<f[i][j];
      bin[s][t]=x;
    }
    for(int kind=0;kind<5;kind++){
      uint16_t reached=uint16_t(1u<<15);
      int result=0;
      for(int h=1;h<=11;h++){
        uint16_t next=reached;
        for(int s=1;s<16;s++)if(reached&(1<<s)){
          int wim=0;for(int i=0;i<4;i++)if(s&(1<<i))wim|=1<<W[kind][i];
          next|=1u<<wim;
          for(int t=1;t<16;t++)if(reached&(1<<t))next|=1u<<bin[s][t];
        }
        if(next&((1<<1)|(1<<2)|(1<<4)|(1<<8))){result=h;break;}
        if(next==reached)break;
        reached=next;
      }
      totals[kind][result]++;
      if(first[kind][result]==-1)first[kind][result]=code;
    }
  }
  const uint64_t EXPECT[5][12]={
    {1035528,4,2124,10920},
    {1020908,4,2124,12160,7128,4916,1204,132},
    {1012112,4,2124,12664,7328,11080,2568,688,8},
    {980154,4,2124,12780,11814,18279,10617,8640,3003,1104,57},
    {951360,4,2124,13032,11576,19672,17232,14360,10608,6568,1816,224}
  };
  for(int k=0;k<5;k++)for(int h=0;h<12;h++)assert(totals[k][h]==EXPECT[k][h]);
  uint64_t tot_sync=0;for(int k=0;k<5;k++){
    uint64_t sum=0;for(int h=0;h<12;h++)sum+=totals[k][h];assert(sum==(1<<20));
    for(int h=1;h<12;h++)tot_sync+=(uint64_t)MULT[k]*totals[k][h];
    cout<<"type "<<k<<"; w=";for(int i=0;i<4;i++)cout<<W[k][i];
    cout<<"; histogram=";
    for(int h=0;h<12;h++)cout<<(h?",":"")<<totals[k][h];
    cout<<"; first_code_at_max=";
    for(int h=11;h>=1;h--)if(totals[k][h]){cout<<first[k][h];break;}
    cout<<'\n';
  }
  assert(tot_sync==1419120);
  cout<<"TOTAL_SYNC "<<tot_sync<<" OF 25165824; EXACT_HEIGHT_11 1344; OK\n";
}
