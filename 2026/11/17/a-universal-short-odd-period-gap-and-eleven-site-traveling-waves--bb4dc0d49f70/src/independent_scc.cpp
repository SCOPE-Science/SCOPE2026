#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
struct Report{int t;uint64_t total_edges;vector<int> recurrent;};
Report examine(int t){
 const uint32_t m=1u<<t,N=m*m;
 vector<uint32_t> od(N),id(N);
 auto edge_list=[&](auto add){
  for(uint32_t a=0;a<m;a++)for(uint32_t b=0;b<m;b++){
   uint32_t forced=0,freedom=0;bool impossible=false;
   for(int i=0;i<t;i++){
    int aa=(a>>i)&1,bb=(b>>i)&1,output=(b>>((i+1)%t))&1;
    int allow0=(54>>(4*aa+2*bb))&1;
    int allow1=(54>>(4*aa+2*bb+1))&1;
    bool z=allow0==output,o=allow1==output;
    if(!z&&!o){impossible=true;break;}
    if(o&&!z)forced|=uint32_t(1)<<i;
    if(o&&z)freedom|=uint32_t(1)<<i;
   }
   if(impossible)continue;
   uint32_t sub=freedom;
   while(true){add(a*m+b,b*m+(forced|sub));if(sub==0)break;sub=(sub-1)&freedom;}
  }
 };
 uint64_t E=0;
 edge_list([&](uint32_t u,uint32_t v){++od[u];++id[v];++E;});
 vector<uint32_t> os(N+1),is(N+1);
 for(uint32_t i=0;i<N;i++){os[i+1]=os[i]+od[i];is[i+1]=is[i]+id[i];}
 vector<uint32_t> oe(E),ie(E),op=os,ip=is;
 edge_list([&](uint32_t u,uint32_t v){oe[op[u]++]=v;ie[ip[v]++]=u;});
 vector<uint8_t> seen(N,0);
 vector<uint32_t> order;order.reserve(N);
 vector<pair<uint32_t,uint32_t>> stack;
 for(uint32_t start=0;start<N;start++)if(!seen[start]){
  seen[start]=1;stack.push_back({start,os[start]});
  while(!stack.empty()){
   auto &last=stack.back();uint32_t u=last.first;
   if(last.second==os[u+1]){order.push_back(u);stack.pop_back();}
   else{uint32_t v=oe[last.second++];if(!seen[v]){seen[v]=1;stack.push_back({v,os[v]});}}
  }
 }
 fill(seen.begin(),seen.end(),0);
 vector<int> cyc;
 for(auto it=order.rbegin();it!=order.rend();++it)if(!seen[*it]){
  vector<uint32_t> todo={*it};seen[*it]=1;
  for(size_t i=0;i<todo.size();i++){
   uint32_t u=todo[i];for(uint32_t j=is[u];j<is[u+1];j++){
    uint32_t v=ie[j];if(!seen[v]){seen[v]=1;todo.push_back(v);}
   }
  }
  uint32_t u=*it;
  bool self=false;for(uint32_t j=os[u];j<os[u+1];j++)if(oe[j]==u)self=true;
  if(todo.size()>1||self){
   if(todo.size()>1){
    for(uint32_t v:todo){
     int inside_in=0,inside_out=0;
     for(uint32_t j=os[v];j<os[v+1];j++)if(find(todo.begin(),todo.end(),oe[j])!=todo.end())inside_out++;
     for(uint32_t j=is[v];j<is[v+1];j++)if(find(todo.begin(),todo.end(),ie[j])!=todo.end())inside_in++;
     if(inside_in!=1||inside_out!=1)throw runtime_error("Non-cycle recurrent SCC");
    }
   }
   cyc.push_back(todo.size());
  }
 }
 sort(cyc.begin(),cyc.end());return {t,E,cyc};
}
int main(){for(int t:{1,3,5,7,9,11}){
 auto r=examine(t);cout<<"t="<<t<<" edges="<<r.total_edges<<" recurrent_SCC_sizes=";
 for(size_t i=0;i<r.recurrent.size();i++){if(i)cout<<",";cout<<r.recurrent[i];}cout<<'\n';
}}
