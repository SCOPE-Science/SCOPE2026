#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <array>
#include <map>
#include <climits>
#include <vector>
#include <algorithm>
using namespace std;
int main(int argc,char**argv){int n=argc>1?atoi(argv[1]):6;int m=n-1;int sz=1<<(m*(m-1));int row[6][32][6]={};for(int i=0;i<m;i++)for(int a=0;a<(1<<(m-1));a++) {int s=1;for(int j=0;j<m;j++)if(i!=j){int b=j<i?j:j-1;int sign=((a>>b)&1)?-1:1;s+=sign;row[i][a][j]=-sign;}row[i][a][i]=s;}
 map<int,int> h;int minval=INT_MAX;int maxval=0;int minword=-1;int zeroword=-1;long long parseval=0;int singlezero=0;map<int,long long> zero_by_canonical_support;vector<int> zero_words;int dp[1<<5];for(int w=0;w<sz;w++){
 int L[6][6];for(int i=0;i<m;i++){int a=(w>>(i*(m-1)))&((1<<(m-1))-1);for(int j=0;j<m;j++) L[i][j]=row[i][a][j];}
 dp[0]=1;for(int mask=1;mask<(1<<m);mask++){int i=__builtin_popcount((unsigned)mask)-1;int v=0;for(int x=mask;x;x&=x-1){int j=__builtin_ctz((unsigned)x);int sub=mask^(1<<j);int sign=__builtin_popcount((unsigned)(sub>>(j+1)))&1?-1:1;v+=sign*dp[sub]*L[i][j];}dp[mask]=v;}
 int d=dp[(1<<m)-1];h[d]++;parseval+=1LL*d*d;if(d==0){if(zeroword<0)zeroword=w;zero_words.push_back(w);} if(d!=0&&abs(d)<minval){minval=abs(d);minword=w;}maxval=max(maxval,abs(d));}
 printf("n %d signings %d zero %zu min %d minword %d zeroword %d max %d parseval %lld distinct %zu\n",n,sz,zero_words.size(),minval,minword,zeroword,maxval,parseval,h.size());for(auto&[a,b]:h)printf("%d:%d ",a,b);puts("");
 // zero count by minimal gauge-weight (root sign choose each row to minimize 1+4 edges), negative slots 4 internal / root edge
 for(int w:zero_words){int support=0;for(int i=0;i<m;i++){int c=__builtin_popcount((unsigned)((w>>(i*(m-1)))&((1<<(m-1))-1)));support+=min(c,m-c);}zero_by_canonical_support[support]++;}
 printf("zeros by minimum row-gauge weight:\n");for(auto&[a,b]:zero_by_canonical_support) printf("%d:%lld ",a,b);puts("");
}
