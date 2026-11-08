// Exhaustive independent bitmask implementation for locating-total codes on C_3 square C_n.
// Build: c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;
struct Info{int k,states,slide_edges,jump_edges,jump_components;map<int,int> sizes;map<pair<int,int>,int> shape;};
Info inspect(int n){
 int N=3*n;vector<unsigned int> nbr(N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){
   int ci=i/3,cj=j/3,ri=i%3,rj=j%3;
   if(ci==cj || (ri==rj && ((ci+1)%n==cj || (cj+1)%n==ci)))nbr[i]|=1u<<j;
 }
 vector<unsigned int> states;int k=-1;
 for(int weight=0;weight<=N;weight++){
  for(int mask=0;mask<(1<<N);mask++)if(__builtin_popcount((unsigned)mask)==weight){
   bool good=true;unsigned sig[24];
   for(int v=0;v<N;v++){sig[v]=nbr[v]&mask;if(!sig[v]){good=false;break;}}
   if(!good)continue;
   for(int v=0;v<N&&good;v++)if(!(mask>>v&1))for(int w=v+1;w<N;w++)
    if(!(mask>>w&1) && sig[v]==sig[w]){good=false;break;}
   if(good)states.push_back(mask);
  }
  if(!states.empty()){k=weight;break;}
 }
 map<unsigned,int> idx;for(int i=0;i<(int)states.size();i++)idx[states[i]]=i;
 vector<vector<int>> S(states.size()),J(states.size());int ns=0,nj=0;
 for(int i=0;i<(int)states.size();i++)for(int a=0;a<N;a++)if(states[i]&(1<<a))
   for(int b=0;b<N;b++)if(!(states[i]&(1<<b))){
    unsigned t=states[i]^(1u<<a)^(1u<<b);
    auto it=idx.find(t);if(it==idx.end()||it->second<=i)continue;
    int j=it->second;J[i].push_back(j);J[j].push_back(i);nj++;
    if(nbr[a]&(1u<<b)){S[i].push_back(j);S[j].push_back(i);ns++;}
   }
 auto cc=[&](const vector<vector<int>>&graph){vector<vector<int>> res;vector<bool> seen(graph.size());
   for(int i=0;i<(int)graph.size();i++)if(!seen[i]){vector<int> C={i};seen[i]=true;
    for(size_t pos=0;pos<C.size();pos++)for(int j:graph[C[pos]])if(!seen[j])seen[j]=true,C.push_back(j);
    res.push_back(C);
   }return res;
 };
 auto cs=cc(S),cj=cc(J);
 Info info{k,(int)states.size(),ns,nj,(int)cj.size(),{}, {}};
 for(auto &C:cs){int e=0;for(int v:C)e+=(int)S[v].size();e/=2;info.sizes[(int)C.size()]++;info.shape[{(int)C.size(),e}]++;}
 return info;
}
int main(){
 for(int n=3;n<=4;n++){
  Info r=inspect(n);
  cout<<"n="<<n<<" minimum="<<r.k<<" bases="<<r.states<<" jump_edges="<<r.jump_edges
  <<" jump_components="<<r.jump_components<<" slide_edges="<<r.slide_edges<<"\n";
  for(auto [key,count]:r.shape)cout<<" component_shape=("<<key.first<<" vertices, "<<key.second<<" edges) count="<<count<<"\n";
  if(n==3){assert(r.k==4 && r.states==81 && r.jump_edges==522 && r.jump_components==1 && r.slide_edges==198 && r.shape[make_pair(81,198)]==1);}
  if(n==4){assert(r.k==5 && r.states==120 && r.jump_edges==468 && r.jump_components==1 && r.slide_edges==192 && r.shape[make_pair(18,36)]==4 && r.shape[make_pair(8,8)]==6);}
 }
 cout<<"INDEPENDENT ENUMERATION PASS\n";
}
