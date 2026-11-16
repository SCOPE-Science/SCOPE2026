// Exact independent verification of signed edge-character sums of labelled unicyclic graphs.
// Compile: g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using ll=long long;
struct Graph {int n,m;vector<pair<int,int>>edges;int id[8][8];Graph(int nn):n(nn){fill(&id[0][0],&id[0][0]+64,-1);for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int k=edges.size();edges.push_back({i,j});id[i][j]=id[j][i]=k;}m=edges.size();}};
int components(const Graph&g,int s){int par[8];iota(par,par+g.n,0);auto root=[&](int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;};int cc=g.n;for(int k=0;k<g.m;k++)if((s>>k)&1){auto [x,y]=g.edges[k];x=root(x);y=root(y);if(x!=y){par[x]=y;--cc;}}return cc;}
vector<int>by_connected_edge_sets(const Graph&g){vector<int>a;for(int s=0;s<(1<<g.m);s++)if(__builtin_popcount((unsigned)s)==g.n && components(g,s)==1)a.push_back(s);return a;}
struct Cycle {int roots;int mask;};
vector<Cycle>cycles(const Graph&g){vector<Cycle>out;for(int sub=0;sub<(1<<g.n);sub++)if(__builtin_popcount((unsigned)sub)>=3){vector<int>v;for(int i=0;i<g.n;i++)if((sub>>i)&1)v.push_back(i);vector<int>tail(v.begin()+1,v.end());do {if(tail.front()>tail.back())continue;int mask=0,last=v[0];for(int z:tail){mask|=1<<g.id[last][z];last=z;}mask|=1<<g.id[last][v[0]];out.push_back({sub,mask});}while(next_permutation(tail.begin(),tail.end()));}return out;}
vector<int>by_cycle_and_rooted_forest(const Graph&g,const vector<Cycle>&cycs){vector<int>out;for(const auto& c:cycs){vector<int>free;for(int i=0;i<g.n;i++)if(!(c.roots>>i&1))free.push_back(i);vector<int>parent(g.n,-1);auto recur=[&](auto&&self,int j)->void{if(j==(int)free.size()){for(int x:free){int at=x,steps=0;while(!(c.roots>>at&1) && steps<=g.n){at=parent[at];++steps;}if(steps>g.n)return;}int mask=c.mask;for(int x:free)mask|=1<<g.id[x][parent[x]];out.push_back(mask);return;}int x=free[j];for(int y=0;y<g.n;y++)if(x!=y){parent[x]=y;self(self,j+1);}};recur(recur,0);}sort(out.begin(),out.end());assert(unique(out.begin(),out.end())==out.end());return out;}
void fwht(vector<int>&a){int N=a.size();for(int len=1;len<N;len*=2)for(int b=0;b<N;b+=len*2)for(int j=0;j<len;j++){int x=a[b+j],y=a[b+j+len];a[b+j]=x+y;a[b+j+len]=x-y;}}
int small_det(const int M[8][8],const vector<int>&v){int d=v.size();if(d==0)return 1;if(d==1)return M[v[0]][v[0]];if(d==2)return M[v[0]][v[0]]*M[v[1]][v[1]]-M[v[0]][v[1]]*M[v[1]][v[0]];assert(d==3);int a=v[0],b=v[1],c=v[2];return M[a][a]*(M[b][b]*M[c][c]-M[b][c]*M[c][b])-M[a][b]*(M[b][a]*M[c][c]-M[b][c]*M[c][a])+M[a][c]*(M[b][a]*M[c][b]-M[b][b]*M[c][a]);}
int cycle_forest_signed_sum(const Graph&g,const vector<Cycle>&cycs,int s){int L[8][8]={};for(int j=0;j<g.m;j++){int w=(s>>j&1)?-1:1;auto [a,b]=g.edges[j];L[a][a]+=w;L[b][b]+=w;L[a][b]-=w;L[b][a]-=w;}int total=0;for(auto c:cycs){vector<int>nonroots;for(int i=0;i<g.n;i++)if(!(c.roots>>i&1))nonroots.push_back(i);int sign=(__builtin_popcount((unsigned)(s&c.mask))&1)?-1:1;total+=sign*small_det(L,nonroots);}return total;}
int triangle_count(const Graph&g,int s){int t=0;for(int i=0;i<g.n;i++)for(int j=i+1;j<g.n;j++)for(int k=j+1;k<g.n;k++)if((s>>g.id[i][j]&1)&&(s>>g.id[j][k]&1)&&(s>>g.id[i][k]&1))++t;return t;}
int main(){for(int n=3;n<=7;n++){Graph g(n);vector<int>by1=by_connected_edge_sets(g);vector<Cycle>cycs=cycles(g);vector<int>by2=by_cycle_and_rooted_forest(g,cycs);assert(by1==by2);cout<<"family n="<<n<<" unicyclic="<<by1.size()<<" cycle_forest_reconstruction=PASS\n";if(n>=7)continue;
int N=1<<g.m;vector<int>a(N);for(int s:by1)a[s]=1;fwht(a);map<int,int>absfreq;vector<int>wzeros(g.m+1);int minpos=999999,zeros=0;long long normNumerator=0;for(int s=0;s<N;s++){int w=a[s];absfreq[abs(w)]++;if(w==0){zeros++;wzeros[__builtin_popcount((unsigned)s)]++;}else minpos=min(minpos,abs(w));}
vector<int>b(N);for(int s=0;s<N;s++)b[s]=(a[s]!=0);fwht(b);for(int z:b)normNumerator+=abs(z);
if(n==5 || n==6){for(int s=0;s<N;s++){int direct=0;for(int edges:by1)direct+= (__builtin_popcount((unsigned)(s&edges))&1)?-1:1;assert(direct==a[s]);assert(cycle_forest_signed_sum(g,cycs,s)==a[s]);}}
if(n==5){assert(by1.size()==222 && zeros==212 && minpos==4 && normNumerator==8104);assert(wzeros[1]==10&&wzeros[5]==192&&wzeros[9]==10);}
if(n==6){assert(by1.size()==3660 && zeros==1200 && minpos==4 && normNumerator==580928);assert(wzeros[4]==420&&wzeros[7]==180&&wzeros[8]==180&&wzeros[11]==420);int checked=0,zerodegree4=0;for(int s=0;s<N;s++)if(__builtin_popcount((unsigned)s)<=4){if(__builtin_popcount((unsigned)s)<4)assert(a[s]!=0);else{int deg[8]={};for(int j=0;j<g.m;j++)if(s>>j&1){auto [u,v]=g.edges[j];deg[u]++;deg[v]++;}sort(deg,deg+g.n);bool classed = vector<int>(deg,deg+g.n)==vector<int>({0,1,1,2,2,2});assert((a[s]==0)==classed);if(classed)zerodegree4++;}checked++;}assert(checked==1941&&zerodegree4==420);}
cout<<"spectrum n="<<n<<" zeros="<<zeros<<" rank="<<N-zeros<<" min_nonzero="<<minpos<<" projection_abs_sum="<<normNumerator<<"/"<<N<<"\n";
cout<<"zero_weights";for(int k=0;k<=g.m;k++)if(wzeros[k])cout<<" "<<k<<":"<<wzeros[k];cout<<"\n";
cout<<"absolute_multiplier_histogram";for(auto [val,count]:absfreq)cout<<" "<<val<<":"<<count;cout<<"\n";
}cout<<"UNICYCLIC_WALSH_CERTIFICATE_PASS\n";}
