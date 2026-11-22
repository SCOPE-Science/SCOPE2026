#include <bits/stdc++.h>
using namespace std; const int N=20,S=1<<N;
int main(int argc,char**argv){int variant=argc>1?atoi(argv[1]):2; vector<uint32_t> mask(N);auto add=[&](int a,int b){mask[a]|=1u<<b;mask[b]|=1u<<a;};
for(int i=0;i<10;i++){add(i,(i+1)%10);add(i,10+i);add(10+i,10+(i+variant)%10);}
vector<uint32_t> succ(S);vector<int> indeg(S,0);
for(int x=0;x<S;x++){uint32_t y=0;for(int i=0;i<N;i++)if((x&mask[i])==0)y|=1u<<i;succ[x]=y;indeg[y]++;}
queue<int>Q; for(int x=0;x<S;x++)if(!indeg[x])Q.push(x);vector<int>order;order.reserve(S);
while(!Q.empty()){int x=Q.front();Q.pop();order.push_back(x);if(!--indeg[succ[x]])Q.push(succ[x]);}
vector<int> cycle(S,-1),depth(S,0),per;vector<uint64_t> basins;
for(int x=0;x<S;x++)if(indeg[x]&&cycle[x]<0){int t=x,id=per.size(),p=0;do{cycle[t]=id;depth[t]=0;t=succ[t];p++;}while(t!=x);per.push_back(p);basins.push_back(p);}
for(auto it=order.rbegin();it!=order.rend();++it){int x=*it; cycle[x]=cycle[succ[x]];depth[x]=depth[succ[x]]+1;basins[cycle[x]]++;}
map<int,int> pcount;map<int,uint64_t> pbasins;map<int,uint64_t> dc;map<pair<int,int>,uint64_t> pd;
for(int p:per){pcount[p]++;}
for(int x=0;x<S;x++){dc[depth[x]]++;pd[{depth[x],per[cycle[x]]}]++;pbasins[per[cycle[x]]]++;}
map<int, map<uint64_t,int>> basin_spectrum;for(int i=0;i<(int)per.size();i++)basin_spectrum[per[i]][basins[i]]++;
cout<<"variant="<<variant<<" S="<<S<<" cycles="<<per.size()<<" maxdepth="<<dc.rbegin()->first<<"\n";
for(auto [p,v]:pcount)cout<<"period "<<p<<" cycles "<<v<<" attracted "<<pbasins[p]<<"\n";
for(auto [d,v]:dc)cout<<"depth "<<d<<" count "<<v<<"\n";
for(auto [p,bs]:basin_spectrum){cout<<"period "<<p<<" basin spectrum "<<bs.size()<<" values\n";for(auto [size,c]:bs)cout<<" "<<size<<":"<<c;cout<<"\n";}
for(auto [k,v]:pd)cout<<"cell "<<k.first<<" "<<k.second<<" "<<v<<"\n";
int witness=-1;for(int x=0;x<S;x++)if(depth[x]==dc.rbegin()->first){witness=x;break;}cout<<"witness "<<witness<<"\n";
return 0;}
