// Exact finite temporal-column proof certificate for elementary cellular automaton Rule 18.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra check_transfer.cpp -o check_transfer
// Run: ./check_transfer
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
static uint32_t advance_time(uint32_t m,int t){return (m>>1)|((m&1U)<<(t-1));}
int main(){
 for(int t : {1,3,5,7,9}){
  const int N=1<<t, V=N*N, mask=N-1;
  vector<vector<int>> g(V),rg(V);
  vector<char> used(V,0);
  long long edge_count=0;
  for(int l=0;l<N;l++)for(int m=0;m<N;m++){
   int next=advance_time(m,t);
   if(m&next)continue;
   int base=(l^next)&(mask^m);
   vector<int> freebits;
   for(int i=0;i<t;i++)if((m>>i)&1)freebits.push_back(i);
   for(int q=0;q<(1<<freebits.size());q++){
    int r=base;
    for(int j=0;j<(int)freebits.size();j++)if((q>>j)&1)r|=1<<freebits[j];
    int u=l*N+m,v=m*N+r;
    g[u].push_back(v);rg[v].push_back(u);
    used[u]=used[v]=1;
    ++edge_count;
   }
  }
  vector<uint8_t> seen(V,0);vector<int> order;order.reserve(V);
  for(int s=0;s<V;s++)if(used[s]&&!seen[s]){
   vector<pair<int,size_t>> st={{s,0}};seen[s]=1;
   while(!st.empty()){
    int v=st.back().first;
    auto &i=st.back().second;
    if(i<g[v].size()){
     int w=g[v][i++];if(!seen[w]){seen[w]=1;st.push_back({w,0});}
    }else{order.push_back(v);st.pop_back();}
   }
  }
  fill(seen.begin(),seen.end(),0);
  int cyclic_components=0, cyclic_vertices=0, nonzero_cyclic_vertices=0;
  for(auto it=order.rbegin();it!=order.rend();it++)if(!seen[*it]){
   vector<int> component;vector<int> st={*it};seen[*it]=1;
   while(!st.empty()){
    int v=st.back();st.pop_back();component.push_back(v);
    for(int w:rg[v])if(!seen[w]){seen[w]=1;st.push_back(w);}
   }
   bool cyclic=component.size()>1;
   if(!cyclic){int v=component[0];for(int w:g[v])if(v==w){cyclic=true;break;}}
   if(cyclic){
    ++cyclic_components;cyclic_vertices+=component.size();
    for(int v:component)if(v)++nonzero_cyclic_vertices;
   }
  }
  int active=0;for(char a:used)active+=a;
  assert(cyclic_components==1&&cyclic_vertices==1&&nonzero_cyclic_vertices==0);
  // The only directed cycle in each graph is its all-zero self-loop.
  cout<<"t="<<t<<" active_vertices="<<active<<" edges="<<edge_count
   <<" cyclic_components="<<cyclic_components<<" cyclic_vertices="<<cyclic_vertices
   <<" nonzero_cyclic_vertices="<<nonzero_cyclic_vertices<<"\n";
 }
 cout<<"ALL_ODD_HEIGHTS_BELOW_ELEVEN_EXCLUDED\n";
}
