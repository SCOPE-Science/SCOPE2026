/* Fully independent engine: max-insertion (append new max at END only... no).
   Independent: plain DFS building perm left-to-right (values), full 4-tuple check on completion
   only for small n, but prune with partial check: any 4-tuple of assigned positions tested. n<=10. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int N, P1[4], P2[4];
static int permv[14], usedv[14];
static long long cnt;
static int haspat_partial(int len){
  /* check all 4-tuples within assigned prefix positions 0..len-1 */
  for(int i1=0;i1<len;i1++)for(int i2=i1+1;i2<len;i2++)for(int i3=i2+1;i3<len;i3++)for(int i4=i3+1;i4<len;i4++){
    int v[4]={permv[i1],permv[i2],permv[i3],permv[i4]};
    int r[4]={0,1,2,3};
    for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)if(v[r[y]]<v[r[x]]){int t=r[x];r[x]=r[y];r[y]=t;}
    int rank[4];for(int t=0;t<4;t++)rank[r[t]]=t+1;
    int ok1=1,ok2=1;
    for(int t=0;t<4;t++){if(rank[t]!=P1[t])ok1=0; if(rank[t]!=P2[t])ok2=0;}
    if(ok1||ok2)return 1;
  }
  return 0;
}
static void dfs(int len){
  if(len==N){cnt++;return;}
  for(int v=1;v<=N;v++){
    if(usedv[v])continue;
    permv[len]=v; usedv[v]=1;
    if(!haspat_partial(len+1)) dfs(len+1);
    usedv[v]=0;
  }
}
int main(int argc,char**argv){
  N=argc>1?atoi(argv[1]):9;
  int which=argc>2?atoi(argv[2]):0;
  int a1324[4]={1,3,2,4},a1234[4]={1,2,3,4},a1243[4]={1,2,4,3};
  memcpy(P1,a1324,16);
  if(which==0)memcpy(P2,a1234,16); else memcpy(P2,a1243,16);
  memset(usedv,0,sizeof usedv); cnt=0; dfs(0);
  printf("n=%d class=%d count=%lld\n",N,which,cnt);
  return 0;
}
