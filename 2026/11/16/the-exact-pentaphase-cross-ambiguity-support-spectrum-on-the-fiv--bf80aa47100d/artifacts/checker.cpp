#include <cstdio>
#include <array>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cassert>
using namespace std;
int main(){
 const int p=5,Q=625;
 int a[Q][5]{};
 for(int z=0;z<Q;z++){int t=z; for(int j=1;j<p;j++){a[z][j]=t%p;t/=p;}}
 map<int,uint64_t> support;
 map<vector<int>,uint64_t> profiles;
 map<int,vector<pair<int,int>>> samples;
 map<int,uint64_t> zero_shift_count;
 int maxzeros=-1; uint64_t max_count=0;
 for(int fi=0;fi<Q;fi++) for(int gi=0;gi<Q;gi++){
  int zeros=0; vector<int> prof;
  for(int x=0;x<p;x++){
   int zrow=0;
   for(int k=0;k<p;k++){
    int bit=0;
    for(int t=0;t<p;t++){
     int e=(a[fi][t]-a[gi][(t-x+p)%p]-k*t+100)%p;
     bit |= (1<<e);
    }
    if(bit==31){zeros++;zrow++;}
   }
   prof.push_back(zrow); zero_shift_count[zrow]++;
  }
  sort(prof.begin(),prof.end());
  support[p*p-zeros]++;
  profiles[prof]++;
  if((int)samples[p*p-zeros].size()<3) samples[p*p-zeros].push_back({fi,gi});
  if(zeros>maxzeros){maxzeros=zeros;max_count=1;}else if(zeros==maxzeros)max_count++;
 }
 assert((support==map<int,uint64_t>{{5,125},{17,12500},{20,12500},{21,52500},{25,313000}}));
 assert((profiles==map<vector<int>,uint64_t>{
 {{0,0,0,0,0},313000},{{0,0,0,0,4},2500},
 {{0,1,1,1,1},50000},{{1,1,1,1,1},12500},
 {{1,1,1,1,4},12500},{{4,4,4,4,4},125}}));
 assert(maxzeros==20 && max_count==125);
 printf("PENTAPHASE_CPP_CHECK_PASS %d maximal zeros %d count %llu\n",Q*Q,maxzeros,(unsigned long long)max_count);
 for(auto [supp,c]:support){printf("support %d count %llu samples",supp,(unsigned long long)c);for(auto [f,g]:samples[supp]) printf(" (%d,%d)",f,g);puts("");}
 puts("profiles:");for(auto [v,c]:profiles){for(auto k:v)printf("%d",k);printf(" %llu\n",(unsigned long long)c);}
 printf("row zeros:\n");for(auto [v,c]:zero_shift_count) printf("%d %llu\n",v,(unsigned long long)c);
}
