#include <bits/stdc++.h>
using namespace std;using ll=long long;
int Nvert;vector<vector<int>> edgeidx;
int nbrMask(int graph,int vertex,int set,bool complement){int a=0;for(int i=0;i<Nvert;i++)if((set>>i&1) && i!=vertex){bool b=(graph>>edgeidx[vertex][i])&1;if(b^complement)a|=1<<i;}return a;}
vector<int> components(int graph,int V,bool complement){vector<int>cs;int rest=V;while(rest){int root=__builtin_ctz((unsigned)rest);int comp=1<<root;int boundary=comp;rest^=comp;while(boundary){int v=__builtin_ctz((unsigned)boundary);boundary^=1<<v;int next=nbrMask(graph,v,rest,complement);boundary|=next;comp|=next;rest&=~next;}cs.push_back(comp);}return cs;}
bool cograph(int graph,int V){if((V&(V-1))==0)return true;auto a=components(graph,V,false);if(a.size()>1){for(int part:a)if(!cograph(graph,part))return false;return true;}a=components(graph,V,true);if(a.size()==1)return false;for(int part:a)if(!cograph(graph,part))return false;return true;}
int main(int argc,char**argv){int n=argc>1?atoi(argv[1]):6;Nvert=n;edgeidx.assign(n,vector<int>(n,-1));int m=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edgeidx[i][j]=edgeidx[j][i]=m++;
int N=1<<m;vector<ll>f(N);vector<int> graphs;for(int x=0;x<N;x++)if(cograph(x,(1<<n)-1)){f[x]=1;graphs.push_back(x);}
cout<<"recursive membership: n="<<n<<" graphs="<<graphs.size()<<"\n";
if(n==6){for(int missingCycle=0;missingCycle<2;missingCycle++){int missing=0;vector<pair<int,int>> ed;if(!missingCycle)ed={{0,1},{1,2},{2,3}};else ed={{0,1},{1,2},{2,3},{3,4},{4,0}}; for(auto [u,v]:ed)missing|=1<<edgeidx[u][v];int mask=(N-1)^missing;ll w=0;for(auto g:graphs)w+=(__builtin_parity((unsigned)(g&mask))?-1:1);cout<<"exception witness complement "<<(missingCycle?"C5+K1":"P4+2K1")<<" coefficient="<<w<<"\n";}}
for(int s=1;s<N;s<<=1)for(int i=0;i<N;i+=2*s)for(int j=0;j<s;j++){ll a=f[i+j],b=f[i+j+s];f[i+j]=a+b;f[i+j+s]=a-b;}
ll oddzero=0,evenzero=0,nonzero=0,minpos=LLONG_MAX;vector<int>exceptionMasks;for(int i=0;i<N;i++){if(f[i]==0){if(__builtin_popcount((unsigned)i)&1)oddzero++;else{evenzero++;exceptionMasks.push_back(i);}}else{nonzero++;minpos=min(minpos,llabs(f[i]));}}
cout<<"oddzero="<<oddzero<<" evenzero="<<evenzero<<" rank="<<nonzero<<" min_nonzero="<<minpos<<"\n";
if(n==6){set<int> expected;vector<int>perm(n);iota(perm.begin(),perm.end(),0);do{for(int type=0;type<2;type++){vector<pair<int,int>>ed;if(type==0)ed={{0,1},{1,2},{2,3}};else ed={{0,1},{1,2},{2,3},{3,4},{4,0}};int missing=0;for(auto [u,v]:ed)missing|=1<<edgeidx[perm[u]][perm[v]];expected.insert((N-1)^missing);}}while(next_permutation(perm.begin(),perm.end()));set<int> actual(exceptionMasks.begin(),exceptionMasks.end());cout<<"exception_orbit_C5_and_P4="<<expected.size()<<" matches_all_even_zeros="<<(expected==actual?"YES":"NO")<<"\n";if(expected!=actual)return 3;}

if(n==6 && (oddzero!=16384 || evenzero!=252 || nonzero!=16132 || minpos!=16))return 5;
if(n==7 && (oddzero!=1048576 || evenzero!=0 || nonzero!=1048576 || minpos!=16))return 6;
if(n==5 && (oddzero!=512 || evenzero!=0 || nonzero!=512 || minpos!=8))return 7;
if(n==4 && (oddzero!=32 || evenzero!=0 || nonzero!=32 || minpos!=4))return 8;
return 0;}
