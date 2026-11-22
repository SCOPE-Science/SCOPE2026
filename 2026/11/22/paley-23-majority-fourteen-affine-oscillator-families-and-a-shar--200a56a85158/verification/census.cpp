#include <bits/stdc++.h>
using namespace std;
int main(int argc, char**argv){
 const int p=23, N=1<<p; vector<uint32_t> masks(p); bool q[p]={};
 for(int i=1;i<p;i++)q[(i*i)%p]=true;
 for(int i=0;i<p;i++)for(int j=0;j<p;j++)if(q[(j-i+p)%p])masks[i]|=1u<<j;
 auto eval=[&](uint32_t x){uint32_t y=0;for(int i=0;i<p;i++)if(__builtin_popcount(x&masks[i])>=6)y|=1u<<i;return y;};
 vector<uint32_t> next(N);vector<uint32_t> indeg(N,0);vector<uint32_t> queue;queue.reserve(N);
 for(uint32_t x=0;x<(uint32_t)N;x++){uint32_t y=eval(x);next[x]=y;indeg[y]++;}
 for(uint32_t x=0;x<(uint32_t)N;x++)if(!indeg[x])queue.push_back(x);
 for(size_t k=0;k<queue.size();k++){auto z=next[queue[k]];if(--indeg[z]==0)queue.push_back(z);}
 map<int,long long> recurrent, cyclic_count, maxdepth_at_period;vector<uint8_t> period(N,0),depth(N,0);vector<uint32_t> rep(N,UINT32_MAX);vector<pair<uint32_t,int>> orbits;
 for(uint32_t x=0;x<(uint32_t)N;x++)if(indeg[x] && !period[x]){
  uint32_t y=x;vector<uint32_t>c;do{c.push_back(y);y=next[y];}while(y!=x);
  int d=c.size();uint32_t leader=*min_element(c.begin(),c.end());orbits.emplace_back(leader,d);
  for(auto z:c){period[z]=d;rep[z]=leader;recurrent[d]++;cyclic_count[d]++;}
 }
 map<pair<int,int>,long long> histogram;for(auto [d,count]:recurrent)histogram[{0,d}]=count;
 for(int j=(int)queue.size()-1;j>=0;j--){uint32_t z=queue[j];uint32_t y=next[z];depth[z]=depth[y]+1;period[z]=period[y];rep[z]=rep[y];histogram[{(int)depth[z],(int)period[z]}]++;}
 int deepest=0;for(auto [k,v]:histogram){deepest=max(deepest,k.first);}
 map<int,int> orbcount;for(auto [x,d]:orbits)orbcount[d]++;
 cout<<"SIZE "<<N<<"\n"<<"MAX_DEPTH "<<deepest<<"\n"<<"ORBITS ";for(auto [d,c]:orbcount)cout<<d<<":"<<c<<" ";cout<<"\n";
 cout<<"RECURRENT ";for(auto [d,c]:recurrent)cout<<d<<":"<<c<<" ";cout<<"\n";
 cout<<"ENTRY_HISTOGRAM\n";for(auto [k,v]:histogram)cout<<k.first<<" "<<k.second<<" "<<v<<"\n";
 unordered_map<uint32_t,uint32_t> basins;for(uint32_t x=0;x<(uint32_t)N;x++){assert(rep[x]!=UINT32_MAX);basins[rep[x]]++;}
 cout<<"BASIN_COUNTS\n";for(auto [x,d]:orbits)cout<<d<<" "<<x<<" "<<basins[x]<<"\n";
 cout<<"LAST_DEPTH_STATES\n";for(uint32_t x=0;x<(uint32_t)N;x++)if(depth[x]==deepest)cout<<x<<"\n";
 return 0;
}
