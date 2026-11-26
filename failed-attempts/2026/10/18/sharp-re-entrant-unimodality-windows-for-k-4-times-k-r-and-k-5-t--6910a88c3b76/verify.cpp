// Exhaustive small-graph and arithmetic checks for complete-graph direct products.
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
long long C(int n,int k){ if(k<0||k>n)return 0; long long v=1; k=min(k,n-k); for(int i=1;i<=k;i++)v=v*(n-k+i)/i; return v; }
vector<ll> coefficient(int a,int r){ int n=a*r; vector<ll> b(max(n,6)+1,0);b[0]=1;b[1]=n;b[2]=C(n,2);for(int k=3;k<=max(a,r);k++){ if(k>5){b[k]=a*C(r,k);continue;} long long fac=1;for(int j=2;j<=k;j++)fac*=j;b[k]=a*C(r,k)+r*C(a,k)+fac*C(a,k)*C(r,k)+C(a,2)*C(r,2)*C(4,k);}return b;}
void graph_test(int a,int r){int N=a*r;uint32_t all=(1u<<N); vector<uint32_t> forbidden(N,0); // precompute invalid pair tests via adjacency
vector<vector<int>> adj(N,vector<int>(N));for(int i=0;i<N;i++)for(int j=0;j<N;j++) adj[i][j]=(i/r!=j/r)&&(i%r!=j%r);
vector<tuple<int,int,int>> bad; for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)for(int k=j+1;k<N;k++){int cnt=adj[i][j]+adj[i][k]+adj[j][k];if(cnt==2)bad.emplace_back(i,j,k);}
vector<unsigned char> good(all); good[0]=1;vector<long long> count(N+1);count[0]=1;for(uint32_t mask=1;mask<all;mask++){uint32_t bit=mask&-mask;uint32_t rest=mask^bit;int v=__builtin_ctz(bit); if(!good[rest])continue;bool okay=true;for(auto [i,j,k]:bad){if(v!=i&&v!=j&&v!=k)continue;auto triple=(1u<<i)|(1u<<j)|(1u<<k);if((mask&triple)==triple){okay=false;break;}}if(okay){good[mask]=1;count[__builtin_popcount(mask)]++;}}
auto b=coefficient(a,r);for(int k=0;k<=N;k++){if(count[k]!=b[k]){cerr<<"FAILED a="<<a<<" r="<<r<<" k="<<k<<" brute="<<count[k]<<" formula="<<b[k]<<"\n";exit(1);}}
cout<<"GRAPH_OK a="<<a<<" r="<<r<<" vertices="<<N<<" masks="<<all<<" feasible="<<accumulate(count.begin(),count.end(),0LL)<<"\n";}
int main(){for(auto [a,r]:vector<pair<int,int>>{{4,3},{4,4},{4,5},{5,3},{5,4}})graph_test(a,r);
// Big integer arithmetic for coefficient checks in Python companion, here finite small-range exact integer check.
for(int a: {4,5}){int state=-1;for(int r=3;r<=50;r++){auto b=coefficient(a,r);bool peaked=false, unimodal=true;for(int k=1;k<=max(a,r);k++){if(b[k]<b[k-1])peaked=true;if(peaked&&b[k]>b[k-1])unimodal=false;}bool expected = a==4 ? (r<=11||r>=40) : (r<=13||r>=156);if(unimodal!=expected){cerr<<"MODAL_FAILED "<<a<<" "<<r<<"\n";return 2;}}cout<<"SMALL_MODAL_OK a="<<a<<" r=3..50\n";}
cout<<"VERIFICATION_OK\n";}
