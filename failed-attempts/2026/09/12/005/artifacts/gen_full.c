#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define NMAX 16
static long long cA[NMAX+1],cB[NMAX+1]; static int N;
static unsigned char pA[24],pB[24];
static int badA(unsigned char*pm,int m,int g){
  unsigned char np[24]; for(int i=0;i<g;i++)np[i]=pm[i]; np[g]=m+1; for(int i=g;i<m;i++)np[i+1]=pm[i];
  if(g>=3) for(int i1=0;i1<g;i1++)for(int i2=i1+1;i2<g;i2++)for(int i3=i2+1;i3<g;i3++){
    int a=np[i1],b=np[i2],c=np[i3]; if((a<c)&&(c<b))return 1; if((a<b)&&(b<c))return 1; }
  return 0;
}
static int badB(unsigned char*pm,int m,int g){
  unsigned char np[24]; for(int i=0;i<g;i++)np[i]=pm[i]; np[g]=m+1; for(int i=g;i<m;i++)np[i+1]=pm[i];
  int M=m+1;
  if(g>=3) for(int i1=0;i1<g;i1++)for(int i2=i1+1;i2<g;i2++)for(int i3=i2+1;i3<g;i3++){
    int a=np[i1],b=np[i2],c=np[i3]; if((a<c)&&(c<b))return 1; }
  if(g>=2&&g<=m-1) for(int t1=0;t1<g;t1++)for(int t2=t1+1;t2<g;t2++){ int a=np[t1],b=np[t2];
    if(a>b)continue; for(int t3=g+1;t3<M;t3++) if(b<np[t3]) return 1; }
  return 0;
}
static void rA(int m){ for(int g=0;g<=m;g++){ if(badA(pA,m,g))continue;
  unsigned char np[24]; for(int i=0;i<g;i++)np[i]=pA[i]; np[g]=m+1; for(int i=g;i<m;i++)np[i+1]=pA[i];
  cA[m+1]++; if(m+1<N){unsigned char s[24];memcpy(s,pA,24);memcpy(pA,np,m+1);rA(m+1);memcpy(pA,s,24);} } }
static void rB(int m){ for(int g=0;g<=m;g++){ if(badB(pB,m,g))continue;
  unsigned char np[24]; for(int i=0;i<g;i++)np[i]=pB[i]; np[g]=m+1; for(int i=g;i<m;i++)np[i+1]=pB[i];
  cB[m+1]++; if(m+1<N){unsigned char s[24];memcpy(s,pB,24);memcpy(pB,np,m+1);rB(m+1);memcpy(pB,s,24);} } }
int main(int argc,char**argv){ N=argc>1?atoi(argv[1]):14; cA[0]=cB[0]=1; pA[0]=1; pB[0]=1; cA[1]=cB[1]=1;
  rA(1); rB(1); for(int n=0;n<=N;n++) printf("%d %lld %lld\n",n,cA[n],cB[n]); return 0; }
