#include <array>
#include <cstdint>
#include <cstdio>
#include <algorithm>
using namespace std;
static unsigned char rule[256][8];
static unsigned char reach[4][8];
static int best(int a,int b,int c) {
    for (auto &row:reach)for(auto &x:row)x=0;
    for (int window=0;window<32;window++){
        int bit[5];for(int j=0;j<5;j++) bit[j]=(window>>(4-j))&1;
        int indices[3]={4*bit[0]+2*bit[1]+bit[2],4*bit[1]+2*bit[2]+bit[3],4*bit[2]+2*bit[3]+bit[4]};
        int output=(rule[a][indices[0]]<<2)|(rule[b][indices[1]]<<1)|rule[c][indices[2]];
        int before=bit[0]*2+bit[1],after=bit[3]*2+bit[4];
        reach[before][output] |= (1<<after);
    }
    unsigned char cur[16][8]{};
    for(int s=1;s<16;s++){
        for(int i=0;i<4;i++)if((s>>i)&1)
            for(int z=0;z<8;z++)cur[s][z]|=reach[i][z];
    }
    int marked[16]{};int layer[16]{};int que[16]{};int len=1,front=0;
    que[0]=15;marked[15]=1;
    while(front<len){int st=que[front++];for(int output=0;output<8;output++){
       int nxt=cur[st][output];
       if(nxt==0) return layer[st]+1;
       if(!marked[nxt]) {marked[nxt]=1;layer[nxt]=layer[st]+1;que[len++]=nxt;}
    }}
    return 0;
}
int main(){
  for(int r=0;r<256;r++)for(int i=0;i<8;i++)rule[r][i]=(r>>i)&1;
  bool hom[256];
  for(int r=0;r<256;r++) hom[r]=best(r,r,r)==0;
  long long n[10]={},weights[8]={}; int witness[3]={-1,-1,-1};int nonsw[3]={-1,-1,-1};
  for(int b=0;b<256;b++)for(int c=0;c<256;c++)for(int a=0;a<256;a++){
      int L=best(a,b,c);
      if(L>9) return 2;
      n[L]++;
      if(L==4 && witness[0]<0)witness[0]=a,witness[1]=b,witness[2]=c;
      if(!L){int mask=(hom[a]?4:0)+(hom[b]?2:0)+(hom[c]?1:0);weights[mask]++;
      if(__builtin_popcount((unsigned)mask)==2 && nonsw[0]<0)nonsw[0]=a,nonsw[1]=b,nonsw[2]=c;}
  }
  for(int i=0;i<10;i++)if(n[i])printf("L %d count %lld\n",i,n[i]);
  for(int i=0;i<8;i++)printf("mask %d count %lld\n",i,weights[i]);
  printf("witness L4 %d,%d,%d; witness 1 bad %d,%d,%d\n",witness[0],witness[1],witness[2],nonsw[0],nonsw[1],nonsw[2]);
  return 0;
}
