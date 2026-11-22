#include <bits/stdc++.h>
using namespace std;
long long hist[4000]={}, profiles=0, perm_count=0;
int r[5];
long long fact[6]={1,1,2,6,24,120};
void calc(){
 long long wt=120;int count=1;
 for(int i=1;i<=5;i++) {if(i<5&&r[i]==r[i-1])count++;else {wt/=fact[count];count=1;}}
 int dp[32]={1};
 for(int i=0;i<5;i++){
   int dq[32]={};for(int m=0;m<32;m++)if(dp[m]){
     dq[m]+=dp[m];for(int c=0;c<5;c++)if(!(m>>c&1))dq[m|(1<<c)]+= (r[i]>>c&1)?-dp[m]:dp[m];
   }memcpy(dp,dq,sizeof(dp));
 }
 int W=0;for(int x:dp)W+=x;
 hist[W+1600]+=wt;profiles++;perm_count+=wt;
}
void dfs(int i,int start){if(i==5){calc();return;}for(int p=start;p<32;p++){r[i]=p;dfs(i+1,p);}}
int main(){dfs(0,0);cerr<<"profiles "<<profiles<<" freq "<<perm_count<<"\n";long long pos=0,zeros=0;int minv=99999;for(int v=-1600;v<2400;v++)if(hist[v+1600]) {if(v){pos+=hist[v+1600];minv=min(minv,abs(v));}else zeros=hist[v+1600];cout<<v<<":"<<hist[v+1600]<<" ";}cout<<"\nrank "<<pos<<" zeros "<<zeros<<" minpos "<<minv<<"\n";}
