#include <cstdint>
#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
  bool homo[256]{};
  long long cnt[16]{}; long long surv[4]{};long long patterns[8]{};
  int ex[8][3];fill(&ex[0][0],&ex[0][0]+8*3,-1);
  int depthmax=0;int exmax[3]={};
  int path[4][8][3],fin[4][8];
  for(int st=0;st<4;st++)for(int w=0;w<8;w++){
    int b[5]={st>>1,st&1,w>>2,(w>>1)&1,w&1};
    for(int i=0;i<3;i++)path[st][w][i]=4*b[i]+2*b[i+1]+b[i+2];
    fin[st][w]=w&3;
  }
  // surj homo for single rule via 4-state subset 2 output labels
  for(int a=0;a<256;a++){
    unsigned char tr[4][2]={};
    for(int st=0;st<4;st++)for(int bit=0;bit<2;bit++){
      int v=((st&1)<<1)|bit, j=((st<<1)|bit)&7;
      tr[st][(a>>j)&1]|=1<<v;
    }
    unsigned char move[16][2]={};for(int sub=1;sub<16;sub++)for(int v=0;v<4;v++)if(sub>>v&1)for(int o=0;o<2;o++)move[sub][o]|=tr[v][o];
    bool seen[16]={};int q[16],head=0,tail=0;seen[15]=true;q[tail++]=15;bool sur=true;
    while(head<tail&&sur){int s=q[head++];for(int o=0;o<2;o++){int k=move[s][o];if(!k){sur=false;break;}if(!seen[k])seen[k]=true,q[tail++]=k;}}
    homo[a]=sur;
  }
  for(int a=0;a<256;a++)for(int b=0;b<256;b++)for(int c=0;c<256;c++){
    unsigned char tr[4][8]={};
    for(int st=0;st<4;st++)for(int w=0;w<8;w++){
      int o=4*((a>>path[st][w][0])&1)+2*((b>>path[st][w][1])&1)+((c>>path[st][w][2])&1);
      tr[st][o]|=1<<fin[st][w];
    }
    unsigned char move[16][8]={};
    for(int sub=1;sub<16;sub++){
      int bit=__builtin_ctz((unsigned int)sub);
      for(int o=0;o<8;o++)move[sub][o]=move[sub&(sub-1)][o]|tr[bit][o];
    }
    bool seen[16]={};unsigned char q[16],depth[16];int head=0,tail=0;seen[15]=true;q[tail]=15;depth[tail++]=0;int L=0;
    while(head<tail&&!L){int s=q[head],d=depth[head++];for(int o=0;o<8;o++){
      int k=move[s][o];if(!k){L=d+1;break;}
      if(!seen[k])seen[k]=true,q[tail]=k,depth[tail++]=d+1;
    }}
    if(L>=16){fprintf(stderr,"L >= 16 exceeds count: %d\n",L);return 2;}
    cnt[L]++;if(L>depthmax)depthmax=L,exmax[0]=a,exmax[1]=b,exmax[2]=c;
    if(!L){int sn=homo[a]+homo[b]+homo[c];surv[sn]++;int mask=(homo[a]?4:0)|(homo[b]?2:0)|(homo[c]?1:0);patterns[mask]++;if(ex[mask][0]<0){ex[mask][0]=a;ex[mask][1]=b;ex[mask][2]=c;}}
  }
  fprintf(stdout,"max depth %d at %d %d %d\n",depthmax,exmax[0],exmax[1],exmax[2]);
  for(int i=0;i<16;i++)if(cnt[i])fprintf(stdout,"count %d %lld\n",i,cnt[i]);
  for(int i=0;i<4;i++)fprintf(stdout,"surj with %d constituents surj: %lld\n",i,surv[i]);
  for(int i=0;i<8;i++)fprintf(stdout,"pattern %d count %lld example (%d,%d,%d)\n",i,patterns[i],ex[i][0],ex[i][1],ex[i][2]);
  return 0;
}
