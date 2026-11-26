#include <cstdio>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;
struct Census{
 long long hist[64]={},sym[64]={};long long processed=0; int top=-1; array<unsigned char,8> topmap{};
};
static int reset_len(const array<unsigned char,8>& trans){
 int depth[256];for(int &x:depth)x=-1;
 int frontier[256],length=0;frontier[length++]=255;depth[255]=0;
 for(int pos=0;pos<length;pos++){
  int s=frontier[pos], d=depth[s];
  for(int c=0;c<2;c++){
   int out=0;
   for(int i=0;i<8;i++)if(s&(1<<i)){
    int j=c==0? ((i+1)&7):trans[i];out|=1<<j;
   }
   if(depth[out]>=0)continue;
   if((out&(out-1))==0)return d+1;
   depth[out]=d+1;frontier[length++]=out;
  }
 }
 return -1;
}
void rec(int i,int mask,array<unsigned char,8>& t,Census &c){
 if(i==8){if(__builtin_popcount((unsigned)mask)!=6)return;
   c.processed++; int len=reset_len(t);c.hist[len+1]++;
   bool period4=true;
   for(int j=0;j<8;j++)if(t[(j+4)&7]!=((t[j]+4)&7)){period4=false;break;}
   if(period4)c.sym[len+1]++;
   if(len>c.top){c.top=len;c.topmap=t;}
   return;
 }
 for(unsigned char v=0;v<8;v++){
  auto m=mask|(1<<v);if(__builtin_popcount((unsigned)m)>6)continue;
  if(__builtin_popcount((unsigned)m)+(8-i-1)<6)continue;
  t[i]=v;rec(i+1,m,t,c);
 }
}
int main(){Census c;array<unsigned char,8> t;rec(0,0,t,c);
 printf("labeled=%lld max=%d exemplar=",c.processed,c.top);
 for(auto v:c.topmap)printf("%u",unsigned(v));puts("");
 for(int i=0;i<64;i++)if(c.hist[i] || c.sym[i])printf("%d,%lld,%lld,%lld\n",i-1,c.hist[i],c.sym[i],(c.hist[i]+c.sym[i])/8);
}
