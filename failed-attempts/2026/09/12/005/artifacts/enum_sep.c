/* Separate min-insertion trees per class. Avoidance test for child = parent-avoids (by induction)
   AND no occurrence using the new-min position. Each class has its own recursion. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NMAX 16
static long long cntA[NMAX+1], cntB[NMAX+1];
static int N;
static unsigned char pA[20], pB[20];
static int P1324[4]={1,3,2,4},P1234[4]={1,2,3,4},P1243[4]={1,2,4,3};
static int occurs_at(unsigned char*np,int m,int j,int*pat){
  int vj=np[j];
  for(int i1=0;i1<m;i1++)for(int i2=i1+1;i2<m;i2++)for(int i3=i2+1;i3<m;i3++)for(int i4=i3+1;i4<m;i4++){
    int idx[4]={i1,i2,i3,i4},has=0;
    for(int t=0;t<4;t++) if(idx[t]==j)has=1;
    if(!has)continue;
    int v[4]={np[i1],np[i2],np[i3],np[i4]};
    int mn=v[0];for(int t=1;t<4;t++)if(v[t]<mn)mn=v[t];
    if(mn!=vj)continue;
    int r[4]={0,1,2,3};
    for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)if(v[r[y]]<v[r[x]]){int t=r[x];r[x]=r[y];r[y]=t;}
    int rank[4];for(int t=0;t<4;t++)rank[r[t]]=t+1;
    int ok=1;for(int t=0;t<4;t++)if(rank[t]!=pat[t]){ok=0;break;}
    if(ok)return 1;
  }
  return 0;
}
static void recA(int m){
  for(int p=0;p<=m;p++){
    unsigned char np[20];
    for(int i=0;i<p;i++)np[i]=pA[i]+1;
    np[p]=1;
    for(int i=p;i<m;i++)np[i+1]=pA[i]+1;
    if(occurs_at(np,m+1,p,P1324)||occurs_at(np,m+1,p,P1234))continue;
    cntA[m+1]++;
    if(m+1<N){unsigned char s[20];memcpy(s,pA,20);memcpy(pA,np,m+1);recA(m+1);memcpy(pA,s,20);}
  }
}
static void recB(int m){
  for(int p=0;p<=m;p++){
    unsigned char np[20];
    for(int i=0;i<p;i++)np[i]=pB[i]+1;
    np[p]=1;
    for(int i=p;i<m;i++)np[i+1]=pB[i]+1;
    if(occurs_at(np,m+1,p,P1324)||occurs_at(np,m+1,p,P1243))continue;
    cntB[m+1]++;
    if(m+1<N){unsigned char s[20];memcpy(s,pB,20);memcpy(pB,np,m+1);recB(m+1);memcpy(pB,s,20);}
  }
}
int main(int argc,char**argv){
  N=argc>1?atoi(argv[1]):12; if(N>NMAX)N=NMAX;
  cntA[0]=cntB[0]=1;pA[0]=1;pB[0]=1;cntA[1]=cntB[1]=1;
  recA(1); recB(1);
  for(int n=0;n<=N;n++)printf("%d %lld %lld\n",n,cntA[n],cntB[n]);
  return 0;
}
