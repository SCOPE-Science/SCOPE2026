#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Q {int e[6];};
int main(int argc, char**argv){int n=argc>1?atoi(argv[1]):6;int m=n*(n-1)/2;int N=1<<m;vector<vector<int>> idx(n,vector<int>(n,-1));int pos=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)idx[i][j]=idx[j][i]=pos++;
vector<Q> qs;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)for(int l=k+1;l<n;l++){Q q={{idx[i][j],idx[i][k],idx[i][l],idx[j][k],idx[j][l],idx[k][l]}};qs.push_back(q);}
bool p4[64]={};for(int z=0;z<64;z++){int deg[4]={};int e=0; int ed[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};for(int t=0;t<6;t++)if(z>>t&1){e++;deg[ed[t][0]]++;deg[ed[t][1]]++;}sort(deg,deg+4);p4[z]=(e==3 && deg[0]==1&&deg[1]==1&&deg[2]==2&&deg[3]==2);}
vector<ll> a(N);long long count=0;for(int x=0;x<N;x++){bool ok=true;for(auto &q:qs){int z=0;for(int b=0;b<6;b++)z|=((x>>q.e[b])&1)<<b;if(p4[z]){ok=false;break;}}if(ok){a[x]=1;count++;}}
cout<<"n "<<n<<" m "<<m<<" total "<<count<<"\n";
for(int step=1;step<N;step<<=1)for(int i=0;i<N;i+=2*step)for(int j=0;j<step;j++){ll u=a[i+j],v=a[i+j+step];a[i+j]=u+v;a[i+j+step]=u-v;}
map<ll,ll> hist;ll zc=0,mn=LLONG_MAX,mx=0;int minSupp=1000, maxSupp=0;map<int,ll>zeroSupport; map<int,ll>firstSupport;ll W0=a[0];for(int x=0;x<N;x++){ll v=llabs(a[x]);hist[v]++;if(!v){zc++;zeroSupport[__builtin_popcount((unsigned)x)]++;minSupp=min(minSupp,__builtin_popcount((unsigned)x));} else {mn=min(mn,v);mx=max(mx,v);}}cout<<"zeros "<<zc<<" rank "<<N-zc<<" minnonzero "<<mn<<" max "<<mx<<" minimal_zero_degree "<<minSupp<<"\n";cout<<"zero_by_degree ";for(auto [k,v]:zeroSupport)cout<<k<<":"<<v<<" ";cout<<"\n";cout<<"hist ";for(auto [k,v]:hist)cout<<k<<":"<<v<<" ";cout<<"\n";ll m4[4]={},m8[8]={};for(ll v:a){m4[(v%4+4)%4]++;m8[(v%8+8)%8]++;}cout<<"mod4";for(auto v:m4)cout<<" "<<v;cout<<" mod8";for(auto v:m8)cout<<" "<<v;cout<<"\n";

}
