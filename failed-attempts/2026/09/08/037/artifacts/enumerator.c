#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Exact counter for permutations of {0..N-1}, N<=12, avoiding two length-4
   patterns. Patterns are encoded as 6-bit pairwise-comparison signatures,
   which are order-isomorphism invariants (hence characterize the pattern).
   Prefix backtracking: a prefix is pruned as soon as any quadruple using the
   newest position matches a forbidden signature. */
static int code1, code2;
static long long total;
static int permv[12];
static int used_[12];
static int N;
static inline int tcode(int a,int b,int c,int d){
    int t=0;
    if(a<b)t|=1; if(a<c)t|=2; if(a<d)t|=4;
    if(b<c)t|=8; if(b<d)t|=16; if(c<d)t|=32;
    return t;
}
static inline int hit(int pos){
    int al=permv[pos];
    for(int i=0;i<pos-2;i++){int ai=permv[i];
      for(int j=i+1;j<pos-1;j++){int aj=permv[j];
        for(int k=j+1;k<pos;k++){int ak=permv[k];
          int t=tcode(ai,aj,ak,al);
          if(t==code1||t==code2)return 1;
        }}}
    return 0;
}
static void rec(int pos){
    if(pos==N){total++;return;}
    for(int v=0;v<N;v++){
        if(!used_[v]){
            permv[pos]=v;used_[v]=1;
            if(pos<3||!hit(pos))rec(pos+1);
            used_[v]=0;
        }
    }
}
static int pcode(int *P){
    int a=P[0],b=P[1],c=P[2],d=P[3];
    int t=0;
    if(a<b)t|=1; if(a<c)t|=2; if(a<d)t|=4;
    if(b<c)t|=8; if(b<d)t|=16; if(c<d)t|=32;
    return t;
}
int main(int argc,char**argv){
    if(argc!=10){fprintf(stderr,"usage: enum2 N a1 a2 a3 a4 b1 b2 b3 b4\n");return 1;}
    N=atoi(argv[1]);
    if(N<1||N>12){fprintf(stderr,"N must be 1..12\n");return 1;}
    int a[8];
    for(int i=0;i<8;i++)a[i]=atoi(argv[i+2])-1;
    int P1[4]={a[0],a[1],a[2],a[3]},P2[4]={a[4],a[5],a[6],a[7]};
    code1=pcode(P1);code2=pcode(P2);
    memset(used_,0,sizeof used_);
    total=0;
    rec(0);
    printf("%lld\n",total);
    return 0;
}
