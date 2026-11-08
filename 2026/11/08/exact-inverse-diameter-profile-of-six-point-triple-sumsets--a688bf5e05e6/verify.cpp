#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;
int main(int argc,char**argv){int maxD=argc>1?atoi(argv[1]):45;int m[57];for(int i=0;i<57;i++)m[i]=1000;array<int,6> wit[57]{};long long cnt=0;int nseen=0;vector<array<int,6>> maxext;
int ti[56],tj[56],tk[56],idx=0;for(int i=0;i<6;i++)for(int j=i;j<6;j++)for(int k=j;k<6;k++)ti[idx]=i,tj[idx]=j,tk[idx]=k,idx++;
for(int e=5;e<=maxD;e++){
 for(int d=4;d<e;d++)for(int c=3;c<d;c++)for(int b=2;b<c;b++)for(int a=1;a<b;a++){
   int A[6]={0,a,b,c,d,e};uint64_t bits[4]={0,0,0,0};
   for(int t=0;t<56;t++){int x=A[ti[t]]+A[tj[t]]+A[tk[t]];bits[x>>6]|=(uint64_t)1<<(x&63);}
   int sz=__builtin_popcountll(bits[0])+__builtin_popcountll(bits[1])+__builtin_popcountll(bits[2])+__builtin_popcountll(bits[3]);cnt++;
   if(e<m[sz]){m[sz]=e;for(int k=0;k<6;k++)wit[sz][k]=A[k];nseen++;}
   if(sz==56 && e==m[56]){maxext.push_back({0,a,b,c,d,e});}
 }
 if(e%5==0){fprintf(stderr,"e=%d count=%lld nseen=%d m56=%d\n",e,cnt,nseen,m[56]);}
 if(m[56]<1000 && e>=m[56])break;
}
for(int s=16;s<=56;s++){printf("%d %d",s,m[s]);if(m[s]<1000)for(int k=0;k<6;k++)printf(" %d",wit[s][k]);puts("");}
printf("STATES %lld MAXEXT %zu\n",cnt,maxext.size());for(auto x:maxext){for(int v:x)printf("%d ",v);puts("");}
}
