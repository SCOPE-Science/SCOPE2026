#include <bits/stdc++.h>
using namespace std;
int main(){vector<pair<int,int>> P;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)P.push_back({i,j});const int N=15,FULL=(1<<15)-1;int neigh[15]={};for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(P[i].first!=P[j].first && P[i].first!=P[j].second && P[i].second!=P[j].first && P[i].second!=P[j].second)neigh[i]|=(1<<j),neigh[j]|=(1<<i);vector<int> cost(1<<N);for(int s=1;s<=FULL;s++){int b=__builtin_ctz(s);int t=s^(1<<b);cost[s]=cost[t]+__builtin_popcount((unsigned)(t&neigh[b]));}int best[16];long long ways[16]={};fill(best,best+16,1000);long long tot=0;int mini=1000;vector<int> min_configs;for(int a=0;a<=FULL;a++){int rem=FULL^a, b=rem;do {int c=rem^b;int mono=cost[a]+cost[b]+cost[c];int occ=__builtin_popcount((unsigned)a); if(mono<best[occ])best[occ]=mono,ways[occ]=1;else if(mono==best[occ])ways[occ]++;if(mono<mini)mini=mono,min_configs.clear();if(mono==mini)min_configs.push_back(a|(b<<15));tot++;if(b==0)break;b=(b-1)&rem;}while(1);}cout<<"Total "<<tot<<" min "<<mini<<" solutions "<<min_configs.size()<<"\n";for(int i=0;i<=N;i++)cout<<i<<" "<<best[i]<<" "<<ways[i]<<"\n";
// classify color population multiset in min configs
map<string,int> mp;for(int st:min_configs){int a=st&FULL,b=(st>>15)&FULL,c=FULL^a^b;vector<int> sizes={__builtin_popcount((unsigned)a),__builtin_popcount((unsigned)b),__builtin_popcount((unsigned)c)};sort(sizes.begin(),sizes.end());string key=to_string(sizes[0])+","+to_string(sizes[1])+","+to_string(sizes[2]);mp[key]++;}
for(auto [k,v]:mp)cout<<"pattern "<<k<<" "<<v<<"\n";
set<int> found(min_configs.begin(),min_configs.end()), family;
int colors[3]={0,1,2};
for(int a=0;a<6;a++)for(int b=0;b<6;b++)if(a!=b){
  sort(colors, colors+3);
  do {
    int bit0=0,bit1=0;
    for(int i=0;i<N;i++){
      auto [u,v]=P[i];
      int type=(u==b||v==b)?1:((u==a||v==a)?2:0);
      int col=colors[type];
      if(col==0) bit0|=1<<i;
      if(col==1) bit1|=1<<i;
    }
    family.insert(bit0|(bit1<<N));
  }while(next_permutation(colors,colors+3));
}
if(family!=found || family.size()!=180){cerr<<"STRUCTURAL_CLASSIFICATION_FAILED\n";return 1;}
cout<<"FAMILY "<<family.size()<<"\n";
}
