#include <bits/stdc++.h>
using namespace std;
int main(){
 for(int K=0;K<=8;++K){
 long long num=0,full=0,fullminimal=0,perF[16]={};uint64_t witnessReach=0,witnessMin=0;auto start=chrono::steady_clock::now();
 uint64_t x=(1ull<<K)-1,bound=1ull<<32;
 while(x<bound){
  ++num;
  uint8_t t[2][16]{};for(int c=0;c<2;c++){uint8_t row[4];for(int j=0;j<4;++j)row[j]=(x>>(16*c+4*j))&15;
  for(int s=1;s<16;++s){int lb=__builtin_ctz((unsigned)s);t[c][s]=t[c][s^(1<<lb)]|row[lb];}}
  uint32_t seen=2;int queue[16]={1},n=1;for(int p=0;p<n;p++)for(int c=0;c<2;++c){int q=t[c][queue[p]];if(!(seen&(1u<<q))){seen|=1u<<q;queue[n++]=q;}}
  if(n==16){full++;if(!witnessReach)witnessReach=x;
   for(int F=1;F<16;++F){int cls[16]={};int groups=0;for(int j=0;j<16;++j){cls[j]=!!(j&F);groups=max(groups,cls[j]+1);}for(int depth=0;depth<16;++depth){map<tuple<int,int,int>,int> ids;int nc[16];for(int j=0;j<16;++j){auto key=make_tuple(cls[j],cls[t[0][j]],cls[t[1][j]]); auto found=ids.find(key);if(found==ids.end())found=ids.emplace(key,ids.size()).first;nc[j]=found->second;}int ng=ids.size();if(ng==groups)break;groups=ng;for(int j=0;j<16;++j)cls[j]=nc[j];}if(groups==16){fullminimal++;perF[F]++;if(!witnessMin)witnessMin=(x<<4)|F;}}
  }
  uint64_t c=x & -x,r=x+c;if(!r)break;x=(((r^x)>>2)/c)|r;
 }
 cerr<<"K "<<K<<" tables "<<num<<" reachable16 "<<full<<" minimal16 "<<fullminimal<<" reachWitness "<<witnessReach<<" minimalWitness "<<witnessMin<<" sec "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 if(fullminimal){for(int f=1;f<16;f++)if(perF[f])cerr<<f<<":"<<perF[f]<<" ";cerr<<"\n";}
 }
}
