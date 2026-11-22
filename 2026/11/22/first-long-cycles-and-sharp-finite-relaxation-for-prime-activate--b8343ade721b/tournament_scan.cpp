#include <bits/stdc++.h>
using namespace std;
// Each pair (i,j), i<j: bit 1 means arc i -> j, else j -> i.
int main(int argc,char**argv) {
 int n=argc>1?atoi(argv[1]):6; if(n<1||n>7){cerr<<"require 1<=n<=7\n";return 2;} int m=n*(n-1)/2, N=1<<n;
 uint64_t total=1ULL<<m;
 vector<pair<int,int>> pairs; for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)pairs.push_back({i,j});
 vector<uint8_t> f(N), seen(N), dist(N); vector<uint16_t> marks(N);
 vector<uint64_t> perGraphMax(N+1,0), occ(N+1,0); uint64_t maxg=0, maxGraph=0;
 for(uint64_t code=0;code<total;code++) {
  uint32_t in[9]={0};
  for(int e=0;e<m;e++){
   auto [i,j]=pairs[e];
   if(code&(1ULL<<e)) in[j]|=1<<i; else in[i]|=1<<j;
  }
  for(int s=0;s<N;s++) {
    int q=0;
    for(int i=0;i<n;i++){
      int k=__builtin_popcount((unsigned)(in[i]&s));
      if(k==2||k==3||k==5||k==7)q|=1<<i;
    }
    f[s]=q;
  }
  memset(seen.data(),0,N);
  int maxp=0;
  for(int s=0;s<N;s++){
   if(seen[s])continue;
   int h=s, l=0;
   while(!seen[h]){seen[h]=1; marks[l++]=h; h=f[h];}
   int t=0;
   if(seen[h]==1){int j=0;while(j<l && marks[j]!=h)j++; t=l-j;}
   maxp=max(maxp,t);
   for(int j=0;j<l;j++)seen[marks[j]]=2;
  }
  perGraphMax[maxp]++;
  if(maxp>maxg){maxg=maxp;maxGraph=code;}
 }
 cout<<"n="<<n<<" total="<<total<<" max="<<maxg<<" witness_code="<<maxGraph<<"\n";
 for(int p=0;p<=N;p++)if(perGraphMax[p]) cout<<p<<":"<<perGraphMax[p]<<" ";cout<<"\n";
}
