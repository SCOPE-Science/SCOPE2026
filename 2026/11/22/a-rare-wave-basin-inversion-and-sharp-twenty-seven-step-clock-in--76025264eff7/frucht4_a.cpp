// Finite exhaustive deterministic classifier of four-state graph excitation.
#include <bits/stdc++.h>
using namespace std;
const int V=12,N=(1<<24);
const int adj[V][3]={{1,6,7},{0,2,7},{1,3,8},{2,4,9},{3,5,9},{4,6,10},{0,5,10},{0,1,11},{2,9,11},{3,4,8},{5,6,11},{7,8,10}};
inline uint32_t step(uint32_t x){
 uint32_t excited=(x & 0x555555u) & ~((x>>1)&0x555555u);
 uint32_t y=0;
 for(int v=0;v<V;v++){
   uint32_t old=(x>>(2*v))&3;
   uint32_t z=old?((old+1)&3):((excited & ((1u<<(2*adj[v][0]))|(1u<<(2*adj[v][1]))|(1u<<(2*adj[v][2]))))!=0);
   y|=z<<(2*v);
 }
 return y;
}
int main(){
 auto start=chrono::steady_clock::now();
 vector<uint32_t> succ(N),deg(N,0),order; order.reserve(N);
 for(uint32_t i=0;i<N;i++){auto j=step(i);succ[i]=j; deg[j]++;}
 fprintf(stderr,"mapped %.2fs\n",chrono::duration<double>(chrono::steady_clock::now()-start).count());
 for(uint32_t i=0;i<N;i++)if(deg[i]==0)order.push_back(i);
 for(size_t head=0;head<order.size();head++){auto j=succ[order[head]];if(!--deg[j])order.push_back(j);}
 vector<uint16_t> per(N,0),entry(N,0),orbitID(N,0);
 vector<int> orbitPeriods(1,0);map<unsigned, uint64_t> recurrent;
 uint64_t orbits=0,cycstates=0;map<unsigned,uint64_t> orbitcounts;
 for(uint32_t i=0;i<N;i++)if(deg[i]&& !per[i]){
   uint32_t j=succ[i];int len=1;while(j!=i){len++;j=succ[j];}
   orbitPeriods.push_back(len);
   j=i;do{per[j]=len;orbitID[j]=(uint16_t)orbitPeriods.size()-1;cycstates++;j=succ[j];}while(j!=i);
   orbitcounts[len]++;orbits++;
 }
 for(auto it=order.rbegin();it!=order.rend();it++){
    auto j=succ[*it];per[*it]=per[j];orbitID[*it]=orbitID[j];entry[*it]=entry[j]+1;
 }
 vector<uint64_t> basin(orbitPeriods.size(),0);
 map<pair<int,int>,uint64_t> hist;map<int,uint64_t> maxstates,byperiod,maxentry_byperiod;
 int maxentry=0;uint32_t maxWitness=0;for(uint32_t i=0;i<N;i++){
   hist[{entry[i],per[i]}]++;basin[orbitID[i]]++;byperiod[per[i]]++;if(entry[i]>maxentry){maxentry=entry[i];maxWitness=i;maxstates.clear();}if(entry[i]==maxentry)maxstates[per[i]]++;
   maxentry_byperiod[per[i]]=max<long long>(maxentry_byperiod[per[i]],entry[i]);
 }
 cout<<"N "<<N<<" orbits "<<orbits<<" cyclicstates "<<cycstates<<" maxentry "<<maxentry<<"\n";
 cout<<"ORBITCOUNTS\n";for(auto [p,v]:orbitcounts)cout<<p<<" "<<v<<"\n";
 cout<<"BY_PERIOD\n";for(auto [p,v]:byperiod)cout<<p<<" "<<v<<" maxentry "<<maxentry_byperiod[p]<<"\n";
 cout<<"MAX_WITNESS "<<maxWitness<<" PERIOD "<<per[maxWitness]<<" FIRST_PERIODIC "<<entry[maxWitness]<<"\n";
 cout<<"MAX_STATES\n";for(auto [p,v]:maxstates)cout<<p<<" "<<v<<"\n";
 cout<<"BASIN_SIZES_BY_PERIOD\n";
 map<int,vector<uint64_t>> basins;for(int j=1;j<(int)orbitPeriods.size();j++)basins[orbitPeriods[j]].push_back(basin[j]);
 for(auto &[p,v]:basins){sort(v.begin(),v.end());cout<<p<<" count="<<v.size()<<" min="<<v.front()<<" max="<<v.back()<<" sum="<<accumulate(v.begin(),v.end(),0ULL)<<"\n";if(p!=4){cout<<"VALUES";for(auto k:v)cout<<" "<<k;cout<<"\n";}}
 cout<<"HIST\n";for(auto [key,v]:hist)cout<<key.first<<" "<<key.second<<" "<<v<<"\n";
 fprintf(stderr,"finished %.2fs\n",chrono::duration<double>(chrono::steady_clock::now()-start).count());
}
