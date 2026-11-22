#include <bits/stdc++.h>
using namespace std;
static uint32_t transform(uint32_t c,int n,const vector<int>&perm){
 int e=0;uint32_t out=0;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
   bool from_i=((c>>e)&1);int a=perm[i],b=perm[j];
   int lo=min(a,b),hi=max(a,b),k=0;
   for(int u=0;u<lo;u++)k+=n-u-1;
   k+=hi-lo-1;
   bool from_lo=(from_i?(a==lo):(b==lo));
   if(from_lo)out|=1u<<k;
   e++;
 }
 return out;
}
int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):7; if(n!=7){cerr<<"require n=7\n";return 2;}int m=n*(n-1)/2,N=1<<n,G=1<<m;
 vector<uint32_t> p9; vector<pair<uint32_t,int>> deep;
 int maxperiod=0,maxdepth=0;
 uint8_t ff[128], indeg[128], dep[128]; int queue[128];
 for(uint32_t c=0;c<(uint32_t)G;c++){
  int pred[8]={},e=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,e++){
   if((c>>e)&1) pred[j]|=1<<i; else pred[i]|=1<<j;
  }
  memset(indeg,0,N);
  for(int s=0;s<N;s++){
   int t=0;for(int i=0;i<n;i++){int k=__builtin_popcount(pred[i]&s); if(k==2||k==3||k==5)t|=1<<i;}
   ff[s]=t;indeg[t]++;
  }
  int head=0,tail=0;
  for(int s=0;s<N;s++)if(indeg[s]==0) queue[tail++]=s;
  while(head<tail){int s=queue[head++];if(--indeg[ff[s]]==0)queue[tail++]=ff[s];}
  memset(dep,0,N);
  for(int k=tail-1;k>=0;k--){int s=queue[k];dep[s]=dep[ff[s]]+1;}
  int period=0;bool vis[128]={};
  for(int s=0;s<N;s++)if(indeg[s]&&!vis[s]){
   int j=s,d=0;do{vis[j]=true; j=ff[j];d++;}while(j!=s);
   period=max(period,d);
  }
  maxperiod=max(maxperiod,period);
  if(period==9)p9.push_back(c);
  for(int s=0;s<N;s++)maxdepth=max(maxdepth,(int)dep[s]);
  if(n==7){for(int s=0;s<N;s++)if(dep[s]==23)deep.emplace_back(c,s);}
 }
 cout<<"maxperiod="<<maxperiod<<" maxdepth="<<maxdepth<<" period9-graphs="<<p9.size()<<" depth23-graph-state-pairs="<<deep.size()<<"\n";
 vector<int> perm(n);iota(perm.begin(),perm.end(),0);
 unordered_set<uint32_t> unseen(p9.begin(),p9.end());
 int ix=0;while(!unseen.empty()){
  uint32_t c=*unseen.begin();int count=0; iota(perm.begin(),perm.end(),0);
  do{uint32_t u=transform(c,n,perm);if(unseen.erase(u))count++;}while(next_permutation(perm.begin(),perm.end()));
  cout<<"period9 isomorphism class "<<++ix<<" rep="<<c<<" labelled graphs="<<count<<"\n";
 }
 // Mark graph-state relabel orbits; a state mask must be relabeled too.
 set<pair<uint32_t,int>> up(deep.begin(),deep.end());ix=0;
 while(!up.empty()){
  auto [c,s]=*up.begin(); int count=0;iota(perm.begin(),perm.end(),0);
  do{
   int ss=0;for(int i=0;i<n;i++)if(s>>i&1)ss|=1<<perm[i];
   if(up.erase({transform(c,n,perm),ss}))count++;
  }while(next_permutation(perm.begin(),perm.end()));
  cout<<"depth23 orbit "<<++ix<<" rep graph="<<c<<" state="<<s<<" relabelled pairs="<<count<<"\n";
 }
}
