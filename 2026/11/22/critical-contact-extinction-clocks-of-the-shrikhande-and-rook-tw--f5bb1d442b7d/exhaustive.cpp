// Exact finite-state classification for synchronous three-state excitation.
// C++17: g++ -O3 -std=c++17 exhaustive.cpp -o exhaustive && ./exhaustive
#include <bits/stdc++.h>
using namespace std;
constexpr int N=16, FULL=(1<<N)-1, TOTAL=43046721;
static uint16_t neighbor[2][N], trigger[2][1<<N];

void setup(){
  for(int v=0;v<N;v++) for(int w=0;w<N;w++) if(v!=w){
    int x=v%4,y=v/4,a=w%4,b=w/4;
    if(x==a||y==b) neighbor[0][v]|=1u<<w;
    int dx=(a-x+4)%4,dy=(b-y+4)%4;
    if((dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||
       (dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3))
      neighbor[1][v]|=1u<<w;
  }
  for(int g=0;g<2;g++) for(int e=0;e<=FULL;e++){
    int t=0;
    for(int v=0;v<N;v++) if(__builtin_popcount(neighbor[g][v]&e)>=3) t|=1<<v;
    trigger[g][e]=t;
  }
}

int main(){
 setup(); ofstream extreme("shrikhande_last_shell.txt");
 if(!extreme) return 1;
 for(int g=0;g<2;g++){
  array<uint64_t,32> hist{};array<int,32> witness;witness.fill(-1);
  for(int id=0;id<TOTAL;id++){
    int z=id,e=0,r=0;
    for(int v=0;v<N;v++){
      int digit=z%3;z/=3;
      if(digit==1)e|=1<<v;
      else if(digit==2)r|=1<<v;
    }
    if(z) return 2;
    int steps=0;
    while((e||r)&&steps<30){
      int next=trigger[g][e]&(~(e|r)&FULL);
      r=e;e=next;steps++;
    }
    if(e||r){cerr<<"Unresolved state "<<g<<" "<<id<<"\n";return 3;}
    hist[steps]++;
    if(witness[steps]<0)witness[steps]=id;
    if(g==1&&steps==5) extreme<<id<<'\n';
  }
  uint64_t total=0;
  cout<<(g==0?"Rook":"Shrikhande")<<"\n";
  for(int t=0;t<32;t++) if(hist[t]){
    cout<<t<<','<<hist[t]<<','<<witness[t]<<"\n";
    total+=hist[t];
  }
  if(total!=TOTAL) return 4;
 }
}
