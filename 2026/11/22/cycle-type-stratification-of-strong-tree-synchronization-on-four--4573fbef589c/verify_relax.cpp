// Independent label-setting computation of minimal synchronizing term height.
// Every mask represents a nonempty set of possible states; the term cost of
// f(S,T) is 1+max(cost(S),cost(T)) and that of w(S) is 1+cost(S).
// Build: c++ -O3 -std=c++17 verify_relax.cpp -o verify_relax
// Run: ./verify_relax
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
static const int E[10][2]={{3,3},{2,3},{2,2},{1,3},{1,2},{1,1},{0,3},{0,2},{0,1},{0,0}};
static const int W[5][4]={{0,1,2,3},{1,0,2,3},{1,0,3,2},{1,2,0,3},{1,2,3,0}};
static const int EXPECT_MAX[5]={3,7,8,10,11};
static const long long EXPECT_SYNC[5]={13048,27668,36464,68422,97216};
int main(){
 long long sync[5]={},high[5]={},hist[5][12]={};int highest[5]={};
 for(int code=0;code<1048576;code++){
  int f[4][4],x=code;
  for(int e=9;e>=0;e--){int val=x%4;x/=4;f[E[e][0]][E[e][1]]=f[E[e][1]][E[e][0]]=val;}
  unsigned char B[16][16]={};
  for(int s=1;s<16;s++)for(int t=1;t<16;t++){
   int v=0;
   for(int i=0;i<4;i++)for(int j=0;j<4;j++)
     if((s>>i&1)&&(t>>j&1))v |= 1<<f[i][j];
   B[s][t]=v;
  }
  for(int kind=0;kind<5;kind++){
   int d[16];bool done[16]={};for(int i=0;i<16;i++)d[i]=100;d[15]=0;
   for(int it=0;it<15;it++){
    int m=0;for(int s=1;s<16;s++)if(!done[s]&&d[s]<d[m])m=s;
    if(m==0 || d[m]>=100)break;
    done[m]=true;
    int u=0;for(int i=0;i<4;i++)if(m>>i&1)u|=1<<W[kind][i];
    if(d[u]>d[m]+1)d[u]=d[m]+1;
    for(int t=1;t<16;t++)if(done[t]){
      int v=B[m][t];if(d[v]>d[m]+1)d[v]=d[m]+1;
    }
   }
   int h=100;for(int s=1;s<16;s++)if((s&(s-1))==0&&h>d[s])h=d[s];
   if(h<100){assert(h>=1 && h<=11);hist[kind][h]++;sync[kind]++;if(h>highest[kind]){highest[kind]=h;high[kind]=1;}else if(h==highest[kind])high[kind]++;}else hist[kind][0]++;
  }
 }
 for(int k=0;k<5;k++){
   assert(sync[k]==EXPECT_SYNC[k]);assert(highest[k]==EXPECT_MAX[k]);
   cout<<"type="<<k<<" synchronized="<<sync[k]<<" maximum="<<highest[k]<<" maximum_cases="<<high[k]<<" histogram=";for(int j=0;j<12;j++)cout<<(j?",":"")<<hist[k][j];cout<<"\n";
 }
 assert(high[4]==224);cout<<"INDEPENDENT_LABEL_SETTING_OK\n";
}
