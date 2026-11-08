#include <iostream>
#include <map>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
int main(){
 const int rs[6]={0,0,0,1,1,2},cs[6]={0,1,2,1,2,2};
 // Independent 3x3 Boolean-field matrix multiplication on full 9 entries.
 int matrix[64][3][3]={};
 for(int m=0;m<64;m++)for(int i=0;i<6;i++) matrix[m][rs[i]][cs[i]]=(m>>i)&1;
 uint8_t prod[64][64];
 for(int a=0;a<64;a++)for(int b=0;b<64;b++){
  int C[3][3]={};
  for(int r=0;r<3;r++)for(int c=0;c<3;c++)for(int t=0;t<3;t++)C[r][c]^=matrix[a][r][t]&matrix[b][t][c];
  int k=0;for(int j=0;j<6;j++) k|=(C[rs[j]][cs[j]]<<j);
  prod[a][b]=k;
 }
 long long total=0; map<int,int> hist; long long nplanes=0,candidates=0;
 for(int u=1;u<64;u++) for(int v=u+1;v<64;v++){
  int w=u^v;
  if(w<v)continue;
  nplanes++;
  int outtype[4]={0,u,v,w};
  int fiber=0;
  for(int code=0;code<4096;code++){
   int cols[6], seen=0;
   for(int i=0;i<6;i++){int t=(code>>(i*2))&3;cols[i]=outtype[t]; if(t)seen|=1<<t;}
   if(__builtin_popcount((unsigned)seen)<2)continue;
   candidates++;
   int P[64]={};
   for(int a=1;a<64;a++){
    int bit=__builtin_ctz((unsigned)a);
    P[a]=P[a^(1<<bit)]^cols[bit];
   }
   bool good=true;
   for(int i=0;i<6 && good;i++)for(int j=0;j<6;j++){
    if(prod[cols[i]][cols[j]]!=P[prod[cols[i]][1<<j]^prod[1<<i][cols[j]]]){good=false;break;}
   }
   if(good)fiber++;
  }
  hist[fiber]++;total+=fiber;
 }
 cout<<"INDEPENDENT planes="<<nplanes<<" candidates="<<candidates<<" rank2_RB="<<total<<"\n";
 for(auto [f,k]:hist)cout<<"FIBER "<<f<<" "<<k<<"\n";
 assert(nplanes==651&&candidates==2542806&&total==652);
 assert(hist[0]==593&&hist[3]==24&&hist[4]==8&&hist[5]==16&&hist[6]==8&&hist[210]==2);
 cout<<"VERIFY_OK\n";
}
