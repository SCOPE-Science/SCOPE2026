#include <iostream>
#include <iomanip>
#include <cstdint>
#include <array>
#include <chrono>
using namespace std;
constexpr unsigned NN=16,FULL=0xffff;
static unsigned nb[2][NN];
static unsigned T[2][1<<NN];
static bool neigh(int g,int v,int w){
 if(v==w) return false;
 int x=v%4,y=v/4,a=w%4,b=w/4;
 if(g==0)return x==a||y==b;
 int dx=(a-x+4)%4,dy=(b-y+4)%4;
 return (dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||(dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3);
}
static unsigned threshold(int g,unsigned ex){
 unsigned out=0;
 for(unsigned v=0;v<NN;v++){
  unsigned cnt=0;
  for(unsigned w=0;w<NN;w++) if((ex>>w&1u) && neigh(g,v,w))cnt++;
  if(cnt>=3) out|=1u<<v;
 }
 return out;
}
int main(){
 for(int g=0;g<2;g++) {
  for(unsigned e=0;e<(1u<<NN);e++)T[g][e]=threshold(g,e);
  unsigned long long hist[20]={},groups=0,weighted=0;
  for(unsigned e=0;e<(1u<<NN);e++){
   unsigned eligible=T[g][e]&(~e&FULL);
   unsigned weight=1u<<(NN-__builtin_popcount(e)-__builtin_popcount(eligible));
   for(unsigned s=eligible;;s=(s-1u)&eligible){
    // time-one state: excited=s, refractory=e
    unsigned E=s, R=e;int steps=1;
    while((E||R)&&steps<=15){
     unsigned next=T[g][E]&(~(E|R)&FULL);
     R=E;E=next;++steps;
    }
    if(steps>15){cerr<<"unresolved\n";return 2;}
    hist[steps]+=weight;
    groups++;weighted+=weight;
    if(!s)break;
   }
  }
  // t=0 all-rest initial state was counted in class one; transfer one count to time zero.
  hist[1]-=1;hist[0]=1;
  cout<<(g==0?"Rook":"Shrikhande")<<" grouped pairs "<<groups<<" weighted "<<weighted<<"\n";
  for(int i=0;i<20;i++) if(hist[i]) cout<<i<<":"<<hist[i]<<" ";cout<<"\n";
 }
}
