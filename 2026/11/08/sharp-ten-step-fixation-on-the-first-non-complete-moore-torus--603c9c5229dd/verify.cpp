#include <array>
#include <vector>
#include <cstdint>
#include <cstdio>
#include <algorithm>
using namespace std;
constexpr int H=4,W=4,N=16;
uint64_t powers[N];int nb[N][8];
uint32_t step(uint32_t state){
 unsigned char x[N];uint32_t z=state;
 for(int i=0;i<N;i++){x[i]=z%3;z/=3;}
 uint32_t output=0;
 for(int i=0;i<N;i++){
  int target=(x[i]+1)%3,cnt=0;
  for(int j=0;j<8;j++)cnt+=x[nb[i][j]]==target;
  output+=powers[i]*((x[i]+(cnt>=4))%3);
 }
 return output;
}
int main(){
 powers[0]=1;for(int i=1;i<N;i++)powers[i]=3*powers[i-1];
 for(int r=0;r<H;r++)for(int c=0;c<W;c++){
  int u=r*W+c,k=0;
  for(int dr=-1;dr<=1;dr++)for(int dc=-1;dc<=1;dc++)if(dr||dc)
   nb[u][k++]=((r+dr+H)%H)*W+((c+dc+W)%W);
 }
 uint32_t M=powers[N-1]*3;vector<uint16_t>dist(M,65535);vector<uint32_t>path;
 uint64_t fixed=0;uint16_t maxdepth=0;uint32_t maxstate=0;uint64_t sumdepth=0;
 for(uint32_t start=0;start<M;start++){
  if(dist[start]!=65535)continue;
  path.clear();uint32_t s=start;
  while(dist[s]==65535){dist[s]=65534;path.push_back(s);uint32_t t=step(s);if(t==s){dist[s]=0;fixed++;break;}s=t;}
  if(dist[s]==65534){printf("FAIL cycle state %u\n",s);return 1;}
  uint16_t d=dist[s];
  for(auto it=path.rbegin();it!=path.rend();++it){uint32_t v=*it;if(v==s&&dist[v]==0)continue; if(d>=65532){printf("FAIL bound\n");return 1;}dist[v]=++d;}
 }
 for(uint32_t s=0;s<M;s++){
  if(dist[s]==65535||dist[s]==65534){puts("FAIL unvisited");return 1;}
  sumdepth+=dist[s];if(dist[s]>maxdepth){maxdepth=dist[s];maxstate=s;}
 }
 printf("VERIFY_OK states=%u fixed=%llu max_transient=%u maximizing_state=%u sum_transient=%llu\n",M,(unsigned long long)fixed,maxdepth,maxstate,(unsigned long long)sumdepth);
 unsigned char arr[N];uint32_t z=maxstate;for(int i=0;i<N;i++){arr[i]=z%3;z/=3;}
 for(int i=0;i<N;i++){printf("%u%s",arr[i],i%4==3?"\n":" ");}
}
