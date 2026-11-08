// Exhaustive three-color Greenberg--Hastings dynamics on the truncated tetrahedral graph.
// Graph vertices are ordered pairs of distinct elements of {0,1,2,3}.
// This is an independent functional-digraph/indegree-pruning implementation.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
constexpr int NV = 12, N = 531441;
using Counts=map<pair<int,int>,long long>;
int main(){
 vector<pair<int,int>> v;
 int idx[4][4];fill(&idx[0][0],&idx[0][0]+16,-1);
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(a!=b){idx[a][b]=(int)v.size();v.push_back({a,b});}
 assert(v.size()==NV);
 array<array<int,3>,NV> neigh{};
 for(int i=0;i<NV;i++){
   auto[a,b]=v[i];int k=0;
   for(int c=0;c<4;c++)if(c!=a&&c!=b)neigh[i][k++]=idx[a][c];
   neigh[i][k++]=idx[b][a];assert(k==3);
 }
 int pow3[NV]; pow3[0]=1;for(int i=1;i<NV;i++)pow3[i]=3*pow3[i-1];
 vector<int> next(N);vector<int> indeg(N,0);
 // Explicit three-phase local rule: 1->2, 2->0, 0->1 iff at least one excited neighbor.
 for(int s=0;s<N;s++){
   int trit[NV];for(int i=0;i<NV;i++)trit[i]=(s/pow3[i])%3;
   int t=0;
   for(int i=0;i<NV;i++){
     int z=0;
     if(trit[i]==1)z=2;
     else if(trit[i]==0){for(int j:neigh[i])if(trit[j]==1){z=1;break;}}
     t+=pow3[i]*z;
   }
   next[s]=t;indeg[t]++;
 }
 vector<int> work(N);int head=0,tail=0;
 for(int i=0;i<N;i++)if(indeg[i]==0)work[tail++]=i;
 while(head<tail){int x=work[head++],y=next[x];if(--indeg[y]==0)work[tail++]=y;}
 vector<int> per(N,0),entry(N,0),cycmin(N,-1);
 map<int,vector<int>> reps;
 for(int i=0;i<N;i++)if(indeg[i]>0&&per[i]==0){
   vector<int> cyc;int cur=i;
   do {cyc.push_back(cur);cur=next[cur];}while(cur!=i);
   int r=*min_element(cyc.begin(),cyc.end());
   reps[(int)cyc.size()].push_back(r);
   for(int x:cyc){per[x]=(int)cyc.size();cycmin[x]=r;}
 }
 for(int k=tail-1;k>=0;k--){int x=work[k],y=next[x];per[x]=per[y];entry[x]=entry[y]+1;}
 Counts hist;map<int,long long> basin;
 int maxent=0;long long maxcount=0;
 for(int s=0;s<N;s++){
   hist[{per[s],entry[s]}]++;basin[per[s]]++;
   if(entry[s]>maxent){maxent=entry[s];maxcount=1;}
   else if(entry[s]==maxent)maxcount++;
 }
 assert(accumulate(basin.begin(),basin.end(),0LL,[](long long a,auto b){return a+b.second;})==N);
 // Construct all S4 vertex permutations; by uniqueness of four triangles this is the full group.
 array<int,4> p={0,1,2,3};vector<array<int,NV>> aut;
 do{
    array<int,NV> im{};
    for(int i=0;i<NV;i++){auto[a,b]=v[i];im[i]=idx[p[a]][p[b]];}
    aut.push_back(im);
 }while(next_permutation(p.begin(),p.end()));
 assert(aut.size()==24);
 auto transformed=[&](int x,const array<int,NV>& phi){
    int z=0;for(int i=0;i<NV;i++)z+=((x/pow3[i])%3)*pow3[phi[i]];
    return z;
 };
 cout<<"{\n\"vertices\":[";
 for(int i=0;i<NV;i++){if(i)cout<<",";cout<<"["<<v[i].first<<","<<v[i].second<<"]";}cout<<"],\n";
 cout<<"\"cycle_counts\":{";bool first=true;
 for(auto&[L,rs]:reps){if(!first)cout<<",";first=false;cout<<"\""<<L<<"\":"<<rs.size();}cout<<"},\n";
 cout<<"\"basin_counts\":{";first=true;
 for(auto [L,m]:basin){if(!first)cout<<",";first=false;cout<<"\""<<L<<"\":"<<m;}cout<<"},\n";
 cout<<"\"max_transient\":"<<maxent<<",\"max_transient_population\":"<<maxcount<<",\n";
 cout<<"\"time_period_counts\":[";first=true;
 for(auto [k,m]:hist){if(!first)cout<<",";first=false;cout<<"["<<k.first<<","<<k.second<<","<<m<<"]";}cout<<"],\n";
 cout<<"\"long_cycle_orbits\":{";first=true;
 for(int L:{4,6,8}){
   if(!first)cout<<",";first=false;
   set<int> rem(reps[L].begin(),reps[L].end());
   cout<<"\""<<L<<"\":[";bool firstorbit=true;
   while(!rem.empty()){
      int x=*rem.begin();set<int> grp;
      for(const auto& im:aut){int y=transformed(x,im);assert(cycmin[y]>=0);grp.insert(cycmin[y]);}
      assert(grp.size()>0);
      for(int y:grp){assert(rem.count(y));rem.erase(y);}
      vector<int> profile;int z=x;
      do {int active=0;for(int j=0;j<NV;j++)active+=((z/pow3[j])%3==1);profile.push_back(active);z=next[z];}while(z!=x);
      assert(profile.size()==(size_t)L);
      vector<int> norm=profile;
      for(int shift=1;shift<L;shift++){
        vector<int> w;for(int j=0;j<L;j++)w.push_back(profile[(j+shift)%L]);
        if(w<norm)norm=w;
      }
      if(!firstorbit)cout<<",";firstorbit=false;
      cout<<"{\"representative\":"<<x<<",\"size\":"<<grp.size()<<",\"stabilizer\":"<<24/grp.size()<<",\"profile\":[";
      for(int i=0;i<L;i++){if(i)cout<<",";cout<<norm[i];}cout<<"],\"cycle_representatives\":[";
      bool fg=true;for(int r:grp){if(!fg)cout<<",";fg=false;cout<<r;}cout<<"]}";
   }
   cout<<"]";
 }
 cout<<"}\n}\n";
}
