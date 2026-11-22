#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>
#include <queue>
using namespace std;
int main(){
 map<int,int>hist;map<int,vector<unsigned>>witness;int maxstates=0;int maxlen=0;
 for(unsigned rule=0;rule<65536;rule++){
  unsigned adj[2][8]={};
  for(int st=0;st<8;st++)for(int b=0;b<2;b++){
   int four=(st<<1)|b;
   int v=(rule>>four)&1;
   adj[v][st]|=1u<<((st<<1|b)&7);
  }
  unsigned char depth[256]={};
  int Q[256],head=0,tail=1; Q[0]=255;depth[255]=1;int found=-1;
  while(head<tail){
   int st=Q[head++];if(st==0){found=(int)depth[0]-1;break;}
   for(int v=0;v<2;v++){
     int mask=0;
     for(int a=0;a<8;a++)if(st>>a&1)mask|=adj[v][a];
     if(!depth[mask]){ depth[mask]=depth[st]+1;Q[tail++]=mask;}
   }
  }
  int nstates=tail; if(nstates>maxstates)maxstates=nstates;
  if(found>maxlen)maxlen=found;
  hist[found]++;
  if(witness[found].size()<8)witness[found].push_back(rule);
 }
 printf("MAX STATES %d MAX SHORTEST FORBIDDEN LENGTH %d\n",maxstates,maxlen);
 for(auto &it:hist){printf("length %d count %d witnesses:",it.first,it.second);for(auto x:witness[it.first])printf(" %u",x);puts("");}
}
