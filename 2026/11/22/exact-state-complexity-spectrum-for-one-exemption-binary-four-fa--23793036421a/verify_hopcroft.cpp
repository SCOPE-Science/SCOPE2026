#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

struct Node { unsigned mask, suffix, used; array<int,2> next; };
static uint64_t encode(unsigned mask,unsigned suffix,unsigned used){ return (uint64_t(mask)<<8)|(uint64_t(used)<<5)|suffix; }

pair<int,int> census(int k,int excluded=-1){
 const unsigned all=(1u<<(1u<<k))-1u, target=excluded>=0 ? (all^(1u<<excluded)) : all, suffixmask=(1u<<(k-1))-1u;
 vector<Node> states(1, {0,0,0,{-1,-1}});
 unordered_map<uint64_t,int> index;
 index[encode(0,0,0)]=0;
 for (size_t i=0;i<states.size();++i){
   for(unsigned c=0;c<2;c++){
     Node q=states[i];
     unsigned mask=q.mask,suffix=q.suffix,used=q.used;
     if(used==(unsigned)k-1) mask|=1u<<((suffix<<1)|c);
     if(used<(unsigned)k-1) used++;
     suffix=((suffix<<1)|c)&suffixmask;
     uint64_t key=encode(mask,suffix,used);
     auto it=index.find(key);
     int j;
     if(it==index.end()){
        j=states.size(); index.emplace(key,j);
        states.push_back({mask,suffix,used,{-1,-1}});
     }else j=it->second;
     states[i].next[c]=j;
   }
 }
 int n=states.size();
 vector<array<vector<int>,2>> pred(n);
 for(int i=0;i<n;i++)for(int c=0;c<2;c++)pred[states[i].next[c]][c].push_back(i);
 vector<vector<int>> blocks(2);
 vector<int> part(n), hit(n,0), cnt(2,0);
 for(int i=0;i<n;i++){
   int b=(states[i].mask&target)==target?1:0;
   blocks[b].push_back(i);part[i]=b;
 }
 assert(!blocks[0].empty()&&!blocks[1].empty());
 queue<pair<int,int>> work;
 vector<array<char,2>> pending(2, {0,0});
 auto enqueue=[&](int b,int c){ if(!pending[b][c]){pending[b][c]=1;work.push({b,c});} };
 for(int c=0;c<2;c++){
  enqueue(0,c); enqueue(1,c);
 }
 int stamp=0;
 while(!work.empty()){
   auto [a,c]=work.front();work.pop();pending[a][c]=0;
   ++stamp;
   vector<int> touched;
   for(int target:blocks[a])for(int from:pred[target][c]){
     if(hit[from]==stamp)continue;
     hit[from]=stamp;
     int b=part[from];
     if(cnt[b]==0)touched.push_back(b);
     cnt[b]++;
   }
   for(int b:touched){
     int marked=cnt[b];cnt[b]=0;
     if(marked==0 || marked==(int)blocks[b].size())continue;
     vector<int> stay,move;
     stay.reserve(blocks[b].size()-marked);
     move.reserve(marked);
     for(int x:blocks[b]){
        if(hit[x]==stamp)move.push_back(x);
        else stay.push_back(x);
     }
     blocks[b].swap(stay);
     int nb=blocks.size();
     blocks.push_back(std::move(move));
     cnt.push_back(0);pending.push_back({0,0});
     for(int x:blocks[nb])part[x]=nb;
     for(int d=0;d<2;d++){
        if(pending[b][d])enqueue(nb,d);
        else enqueue(blocks[b].size()<=blocks[nb].size()?b:nb,d);
     }
   }
 }
 // Every block is acceptance uniform and transitions are block-stable.
 for(auto &block:blocks){
   assert(!block.empty());
   int rep=block[0];
   for(int x:block){
     assert(((states[x].mask&target)==target)==((states[rep].mask&target)==target));
     for(int c=0;c<2;c++)assert(part[states[x].next[c]]==part[states[rep].next[c]]);
   }
 }
 return {n,(int)blocks.size()};
}
int main(){
 const int expected[16]={8435,11121,9670,10152,9956,9537,8524,11746,
                         11746,8524,9537,9956,10152,9670,11121,8435};
 for(int excluded=0;excluded<16;excluded++){
   auto [reached,minimum]=census(4,excluded);
   assert(reached==19205 && minimum==expected[excluded]);
   cout<<"excluded="<<excluded<<" reachable="<<reached<<" minimal="<<minimum<<"\n";
 }
 cout<<"Hopcroft refinement: ALL 16 EXACT COUNTS PASS\n";
}
