/* Independent Leibniz-determinant calculation in a second prime field.
   No Gaussian elimination and no divisions are used. */
#include <stdint.h>
#include <stdio.h>
#define PRIME 1300000003LL
static int64_t B[48][6];
static int64_t power(int64_t a,int64_t n){int64_t out=1;while(n){if(n&1)out=out*a%PRIME;a=a*a%PRIME;n>>=1;}return out;}
static int64_t red(int64_t x){x%=PRIME;return x<0?x+PRIME:x;}
static int64_t det6(int cols[6]){
 int64_t d[64]={1};
 for(int mask=0;mask<63;mask++){
  int j=__builtin_popcount((unsigned)mask);
  if(j>=6)continue;
  int64_t v=d[mask];
  if(v==0)continue;
  for(int row=0;row<6;row++)if(!(mask & (1<<row))){
    int inversions=__builtin_popcount((unsigned)mask >> (row+1));
    int64_t add=v*B[cols[j]][row]%PRIME;
    int dest=mask | (1<<row);
    d[dest]=red(d[dest]+(inversions%2 ? -add : add));
  }
 }
 return d[63];
}
static int isprime(int64_t n){if(n<2)return 0;for(int64_t k=2;k*k<=n;k++)if(n%k==0)return 0;return 1;}
int main(void){
 if(!isprime(PRIME)){puts("NONPRIME MODULUS");return 2;}
 int e[7]={0,1,1,0,1,0,0};
 int64_t z=power(2,(PRIME-1)/7),t=power(2,(PRIME-1)/3);
 if(z==1||t==1||power(z,7)!=1||power(t,3)!=1)return 2;
 int64_t zz[7]={1},tt[3]={1},g[7];
 for(int i=1;i<7;i++)zz[i]=zz[i-1]*z%PRIME;
 for(int i=1;i<3;i++)tt[i]=tt[i-1]*t%PRIME;
 for(int i=0;i<7;i++)g[i]=tt[e[i]];
 for(int c=1;c<49;c++){
  int a=c/7,b=c%7;
  int64_t offset=g[(7-a)%7];
  for(int x=1;x<7;x++){
    int64_t y=zz[(b*x)%7]*g[(x-a+7)%7]%PRIME;
    y=y*power(g[x],PRIME-2)%PRIME;
    B[c-1][x-1]=red(y-offset);
  }
 }
 int col[6]={0,1,2,3,4,5};
 long long passed=0;
 do{
  passed++;
  if(det6(col)==0){printf("FAIL at %lld with",passed);for(int i=0;i<6;i++)printf(" %d",col[i]+1);putchar('\n');return 1;}
  int k=5;while(k>=0 && col[k]==42+k)k--;
  if(k<0)break;
  col[k]++;for(int j=k+1;j<6;j++)col[j]=col[j-1]+1;
 }while(1);
 printf("PASS %lld minors, prime %lld, root7 %lld, root3 %lld\n",passed,PRIME,(long long)z,(long long)t);
 return 0;
}
