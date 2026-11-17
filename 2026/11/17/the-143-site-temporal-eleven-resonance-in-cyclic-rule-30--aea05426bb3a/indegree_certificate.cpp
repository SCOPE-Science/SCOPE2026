// Independent indegree-peeling certificate for Rule 30 temporal-11 spatial profiles.
// Compile: g++ -O2 -std=c++17 indegree_certificate.cpp -o indegree_certificate
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int H=11;
constexpr unsigned SZ=1u<<(2*H), ALL=(1u<<H)-1;
unsigned step(unsigned v){
 unsigned middle=v% (1u<<H);
 unsigned right=v/(1u<<H);
 unsigned nextmiddle=0;
 for(int t=0;t<H;t++){
  unsigned here=(middle>>t)&1u, rhs=(right>>t)&1u;
  unsigned tomorrow=(middle>>((t+1)%H))&1u;
  unsigned lhs=tomorrow^(here|rhs);
  nextmiddle |=lhs<<t;
 }
 return nextmiddle+(middle<<H);
}
int main(){
 vector<uint16_t> indeg(SZ,0);
 for(unsigned i=0;i<SZ;i++){unsigned v=step(i);assert(v<SZ);++indeg[v];}
 vector<unsigned> queue;queue.reserve(SZ);
 for(unsigned i=0;i<SZ;i++)if(indeg[i]==0)queue.push_back(i);
 for(size_t j=0;j<queue.size();j++){
  unsigned v=step(queue[j]);assert(indeg[v]>0);
  if(--indeg[v]==0)queue.push_back(v);
 }
 vector<uint8_t> seen(SZ,0);
 map<int,int> cycles;uint64_t rec=0;
 for(unsigned s=0;s<SZ;s++){
  if(indeg[s]==0||seen[s])continue;
  unsigned p=s;int len=0;
  do{assert(indeg[p]!=0 && !seen[p]);seen[p]=1;++len;p=step(p);}while(p!=s);
  rec+=len;cycles[len]++;
 }
 assert((cycles==map<int,int>{{1,1},{2,1},{143,1},{275,1}}));
 assert(rec==421);
 assert(queue.size()==SZ-rec);
 cout<<"total_pairs="<<SZ<<" peeled="<<queue.size()<<" recurrent="<<rec<<"\n";
 for(auto [p,m]:cycles)cout<<"period="<<p<<" cycles="<<m<<"\n";
 cout<<"independent_recurrent_decomposition=PASS\n";
}
