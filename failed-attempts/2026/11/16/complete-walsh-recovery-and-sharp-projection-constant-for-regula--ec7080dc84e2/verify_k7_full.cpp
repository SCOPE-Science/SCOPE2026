#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main(){ const int n=7,m=21,N=1<<m;vector<pair<int,int>> E;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)E.push_back({i,j});
vector<int> f(N),out(n);long long cnt=0;
for(int s=0;s<N;s++) {fill(out.begin(),out.end(),0);for(int k=0;k<m;k++){auto [i,j]=E[k];out[((s>>k)&1)? j:i]++;}bool good=true;for(int i=0;i<n;i++)if(out[i]!=3) {good=false;break;}if(good){f[s]=1;cnt++;}}
cout<<"count "<<cnt<<"\n";auto fwht=[&](vector<int> &a){for(int p=1;p<N;p<<=1)for(int b=0;b<N;b+=2*p)for(int j=0;j<p;j++){int x=a[b+j],y=a[b+j+p];a[b+j]=x+y;a[b+j+p]=x-y;}};
fwht(f);long long z=0, evenz=0,oddz=0;int minw=100, minmag=INT_MAX, maxmag=0;map<int,long long> hist,zeros_weight;long long e2=0;
for(int s=0;s<N;s++){int v=f[s],w=__builtin_popcount((unsigned)s);hist[v]++;e2+=(long long)v*v;if(v==0){z++;zeros_weight[w]++;minw=min(minw,w);if(w%2) oddz++;else evenz++;}else{minmag=min(minmag,abs(v));maxmag=max(maxmag,abs(v));}}
cout<<"zeros "<<z<<" odd "<<oddz<<" even "<<evenz<<" rank "<<N-z<<" minzero_weight "<<minw<<" minmag "<<minmag<<" maxmag "<<maxmag<<" parseval "<<e2<<" exp "<<cnt*(long long)N<<"\n";
cout<<"zero weights: ";for(auto [a,b]:zeros_weight)cout<<a<<":"<<b<<" ";cout<<"\n";
cout<<"hist: ";for(auto [a,b]:hist)cout<<a<<":"<<b<<" ";cout<<"\n";
vector<int> p(N);for(int i=0;i<N;i++)p[i]=(f[i]!=0);fwht(p);long long sumabs=0;for(auto a:p)sumabs+=llabs(a);cout<<"projection_sumabs "<<sumabs<<" over "<<N<<"\n"; assert(cnt==2640 && z==1543168 && N-z==553984 && minmag==16 && maxmag==2640 && sumabs==91381760 && e2==(long long)cnt*N); cout<<"REGULAR_K7_FULL_PASS\n";
}
