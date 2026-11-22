// Exhaustive forward-time checker for synchronous 3-state two-contact excitation.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_forward.cpp -o verify_forward
// Run: ./verify_forward
// Standalone: no graph-data file or nonstandard package is needed.
#include <iostream>
#include <vector>
#include <array>
#include <stdexcept>
#include <string>
using namespace std;
using Edge=pair<int,int>;
struct Case {string name;int n;int cutoff;vector<Edge> edges;};
int main(){
 const vector<Case> cases={
  {"groetzsch",11,5,{{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{6,10},{7,10},{8,10},{9,10}}},
  {"chvatal",12,6,{{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}}}
 };
 for (const Case &c:cases){
  vector<vector<int>> adj(c.n);
  for (auto [u,v]:c.edges){if(u==v || u<0 || v>=c.n) throw runtime_error("invalid edge");adj[u].push_back(v);adj[v].push_back(u);}
  array<int,13> power{};power[0]=1;
  for(int v=1;v<=c.n;v++)power[v]=3*power[v-1];
  const int N=power[c.n];
  auto forward=[&](int state,int theta){
   array<int,12> a{};
   for(int v=0;v<c.n;v++)a[v]=(state/power[v])%3;
   int next=0;
   for(int v=0;v<c.n;v++){
    int b=0;
    if(a[v]==1)b=2;
    else if(a[v]==2)b=0;
    else{
     int active=0;
     for(int w:adj[v]) active+=(a[w]==1);
     if(active>=theta)b=1;
    }
    next+=b*power[v];
   }
   return next;
  };
  vector<long long> histogram(c.cutoff+1,0);
  int witness=-1; long long first_max_count=0;
  for(int initial=0;initial<N;initial++){
   int state=initial;
   int t=0;
   while(state!=0 && t<c.cutoff){state=forward(state,2);t++;}
   if(state!=0)throw runtime_error("extinction bound failed");
   histogram[t]++;
   if(t==c.cutoff){first_max_count++;if(witness<0)witness=initial;}
  }
  if(!first_max_count)throw runtime_error("sharpness failed");
  const int w=448;
  const int w1=forward(w,1), w2=forward(w1,1), w3=forward(w2,1);
  if(w1==w || w2==w || w3!=w) throw runtime_error("one-contact witness failed");
  cout<<c.name<<" n="<<c.n<<" N="<<N<<" histogram=";
  for(size_t i=0;i<histogram.size();i++){if(i)cout<<",";cout<<histogram[i];}
  cout<<" max="<<c.cutoff<<" first_max_witness="<<witness
      <<" one_contact_three_cycle="<<w<<","<<w1<<","<<w2<<","<<w3<<"\n";
 }
 // Independent four-cycle witness on the four-regular, triangle-free biclique.
 const array<array<int,8>,4> k44={{{2,2,0,0,1,1,0,0},
    {0,0,1,1,2,2,0,0},{0,0,2,2,0,0,1,1},{1,1,0,0,0,0,2,2}}};
 for(int t=0;t<4;t++) {
  array<int,8> next{};const auto &a=k44[t];
  for(int v=0;v<8;v++){
   if(a[v]==1)next[v]=2;
   else if(a[v]==2)next[v]=0;
   else {
     int count=0;
     for(int w=0;w<8;w++){
      if(((v<4 && w>=4)||(v>=4 && w<4)) && a[w]==1)count++;
     }
     next[v]=(count>=2)?1:0;
    }
  }
  if(next!=k44[(t+1)%4])throw runtime_error("biclique cycle witness failed");
 }
 cout<<"K4,4 two-contact primitive four-cycle: PASS\n";
 return 0;
}
