// Exhaustive finite-state certificate for temporal periods 6 and 12 of Rule 30.
// C++17; g++ -O2 -std=c++17 transfer_certificate.cpp -o certificate && ./certificate
#include <cstdint>
#include <algorithm>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using namespace std;
struct Spec {int space, time; bool operator<(const Spec& q)const {return tie(space,time)<tie(q.space,q.time);} };
void certify(int p){
 const uint32_t Q=1u<<p, MASK=Q-1, N=Q*Q;
 auto successor=[&](uint32_t state)->uint32_t {
   uint32_t center=state>>p, right=state&MASK;
   uint32_t shifted=(center>>1)|((center&1u)<<(p-1));
   uint32_t left=shifted^(center|right);
   return (left<<p)|center;
 };
 vector<uint16_t> incoming(N,0);
 for(uint32_t s=0;s<N;++s){uint32_t t=successor(s);if(incoming[t]==UINT16_MAX)throw 1;incoming[t]++;}
 vector<uint32_t> queue;queue.reserve(N);
 for(uint32_t s=0;s<N;++s)if(incoming[s]==0)queue.push_back(s);
 for(size_t k=0;k<queue.size();++k){uint32_t t=successor(queue[k]);if(incoming[t]==0)throw 2;if(--incoming[t]==0)queue.push_back(t);}
 map<Spec,pair<int,vector<uint32_t>>> cycles;
 uint32_t periodic_states=0;
 for(uint32_t s=0;s<N;++s){
  if(incoming[s]==0)continue;
  vector<uint32_t> orbit;uint32_t t=s;
  do {if(incoming[t]==0)throw 3;incoming[t]=0;orbit.push_back(t);t=successor(t);}while(t!=s);
  int primitive=p;
  for(int d=1;d<=p;++d){if(p%d)continue;bool all=true;
   for(uint32_t z:orbit){uint32_t word=z>>p;
    for(int j=0;j<p;++j)if(((word>>j)&1u)!=((word>>((j+d)%p))&1u)){all=false;break;}
    if(!all)break;
   }
   if(all){primitive=d;break;}
  }
  uint32_t minstate=*min_element(orbit.begin(),orbit.end());
  auto& ent=cycles[{(int)orbit.size(),primitive}];ent.first++;ent.second.push_back(minstate);
  periodic_states+=(uint32_t)orbit.size();
 }
 if(queue.size()+periodic_states!=N)throw 4;
 cout<<"height="<<p<<" all_pairs="<<N<<" transient_pairs="<<queue.size()<<" cyclic_pairs="<<periodic_states<<"\n";
 for(const auto& [sp,entry]:cycles){cout<<"space="<<sp.space<<" time="<<sp.time<<" component_count="<<entry.first<<" minima=";for(auto v:entry.second)cout<<v<<",";cout<<"\n";}
}
int main(){certify(6);certify(12);}
