/* Independent engine #2: MAX-insertion separate trees per class.
   Child-libs: parent perm q of 1..m (values), insert new global MAX m+1 at gap g.
   New max plays value-role 4. New occurrences must use the new max position g.
   - 1324 (4 at index 3): triples strictly left of g order-isomorphic to 132.
   - 1234 (4 at index 3): triples strictly left of g order-isomorphic to 123.
   - 1243 (4 at index 2): one index left of g (role1) + ordered pair (i<j) with
     i left of g (role 2) and j right of g (role 3), values vi < vj.
   Recurrence is exact per class with SEPARATE trees (no shared-tree leakage).
   Entirely independent from min-insertion engine (different insertion element,
   different occurrence-role logic, different traversal). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NMAX 16
static long long cntA[NMAX+1], cntB[NMAX+1];
static int N;
static unsigned char pA[20], pB[20];
static inline int is132(int a,int b,int c){ return (a<c)&&(c<b); }
static inline int is123(int a,int b,int c){ return (a<b)&&(b<c); }
/* returns 1 if inserting max at gap g into perm[0..m-1] creates a forbidden pattern of class cls */
static int bad(unsigned char*perm,int m,int g,int cls){
  unsigned char np[20];
  for(int i=0;i<g;i++)np[i]=perm[i];
  np[g]=(unsigned char)(m+1);
  for(int i=g;i<m;i++)np[i+1]=perm[i];
  int M=m+1;
  /* 1324/1234 via triples left of g */
  if(g>=3){
    for(int i1=0;i1<g;i1++)for(int i2=i1+1;i2<g;i2++)for(int i3=i2+1;i3<g;i3++){
      int a=np[i1],b=np[i2],c=np[i3];
      if(is132(a,b,c)) return 1;
      if(cls==0 && is123(a,b,c)) return 1;
    }
  }
  /* 1243 (cls==1): role1 at i<g, role2 at j with i<j<g... wait roles: pattern 1243,
     max at index 2. Occurrence indices t1<t2<g<t3 with values v1<v2<v3 (ranks 1,2,4,3). */
  if(cls==1 && g>=2 && g<M-1+1 && g<=m-1){
    for(int t1=0;t1<g;t1++)for(int t2=t1+1;t2<g;t2++){
      int a=np[t1],b=np[t2];
      if(a>b)continue;
      for(int t3=g+1;t3<M;t3++){ int c=np[t3]; if(b<c) return 1; }
    }
  }
  return 0;
}
static void recA(int m){
  for(int g=0;g<=m;g++){
    if(bad(pA,m,g,0))continue;
    unsigned char np[20];
    for(int i=0;i<g;i++)np[i]=pA[i];
    np[g]=(unsigned char)(m+1);
    for(int i=g;i<m;i++)np[i+1]=pA[i];
    cntA[m+1]++;
    if(m+1<N){unsigned char s[20];memcpy(s,pA,20);memcpy(pA,np,m+1);recA(m+1);memcpy(pA,s,20);}
  }
}
static void recB(int m){
  for(int g=0;g<=m;g++){
    if(bad(pB,m,g,1))continue;
    unsigned char np[20];
    for(int i=0;i<g;i++)np[i]=pB[i];
    np[g]=(unsigned char)(m+1);
    for(int i=g;i<m;i++)np[i+1]=pB[i];
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
