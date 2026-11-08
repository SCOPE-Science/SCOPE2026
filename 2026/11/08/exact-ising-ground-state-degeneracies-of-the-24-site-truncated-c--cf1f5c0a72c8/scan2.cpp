#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;
int main(){ int id[8][8];fill(&id[0][0],&id[0][0]+64,-1); int N=0;
for(int u=0;u<8;u++)for(int j=0;j<3;j++)id[u][u^(1<<j)]=N++;
vector<pair<int,int>> intra,inter;vector<pair<int,int>> adj[24];
for(int u=0;u<8;u++){int a[3];for(int j=0;j<3;j++)a[j]=id[u][u^(1<<j)];for(int j=0;j<3;j++)for(int k=j+1;k<3;k++)intra.push_back({a[j],a[k]});}
for(int u=0;u<8;u++)for(int j=0;j<3;j++){int v=u^(1<<j);if(u<v)inter.push_back({id[u][v],id[v][u]});}
for(auto [i,j]:intra){adj[i].push_back({j,0});adj[j].push_back({i,0});}
for(auto [i,j]:inter){adj[i].push_back({j,1});adj[j].push_back({i,1});}
static uint32_t hist[25][25][13];
uint32_t gray=0;int pop=0,ci=0,ce=0;
for(uint32_t t=0;t<(1u<<N);t++){
 if(t){int b=__builtin_ctz(t);int old=(gray>>b)&1;for(auto [j,typ]:adj[b]){int other=(gray>>j)&1;((typ==0)?ci:ce)+=(old==other)?1:-1;}pop+=old?-1:1;gray^=1u<<b;}
 hist[pop][ci][ce]++;
}
for(int k=0;k<=24;k++)for(int i=0;i<=24;i++)for(int j=0;j<=12;j++)if(hist[k][i][j])printf("%d,%d,%d,%u\n",k,i,j,hist[k][i][j]);
}
