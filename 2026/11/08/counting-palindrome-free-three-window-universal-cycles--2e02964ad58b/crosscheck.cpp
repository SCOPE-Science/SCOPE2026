#include <bits/stdc++.h>
using namespace std;
// Checks distinct length-three nonpalindromic windows using an independent
// enumeration of local edge-orderings in the directed overlap graph.
int main(){
 for(int q=2;q<=3;++q){
   int N=q*q;
   vector<vector<int>> out(N);
   vector<int> tail,head;
   for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)if(a!=c){
      tail.push_back(a*q+b);head.push_back(b*q+c);out[a*q+b].push_back((int)tail.size()-1);
   }
   int E=(int)tail.size();int first=0;
   long long good=0;
   // Each Euler tour starting with first edge chooses a permutation of outgoing arcs
   // for each vertex. A greedy traversal from the fixed edge consumes the first
   // currently unused arc in the local order; valid configurations are counted once.
   vector<vector<vector<int>>> perms(N);
   for(int v=0;v<N;v++){
     auto a=out[v];sort(a.begin(),a.end());
     do{perms[v].push_back(a);}while(next_permutation(a.begin(),a.end()));
   }
   vector<int> choose(N,0);
   auto visit=[&](){
     vector<vector<int>> order(N);
     for(int v=0;v<N;v++)order[v]=perms[v][choose[v]];
     // Anchor the first edge: it must be first at its own vertex.
     if(order[tail[first]][0]!=first)return;
     vector<int> cursor(N,0);
     int v=tail[first],k=0;
     while(k<E && cursor[v]<(int)order[v].size()){
       int e=order[v][cursor[v]++];v=head[e];k++;
     }
     if(k==E && v==tail[first])good++;
   };
   function<void(int)> dfs=[&](int v){
     if(v==N){visit();return;}
     for(int i=0;i<(int)perms[v].size();i++){choose[v]=i;dfs(v+1);}
   };
   dfs(0);
   long long expected = q==2?1:108;
   if(good!=expected){cerr<<"FAILED q="<<q<<" count="<<good<<"\n";return 1;}
   cout<<"ORDER_CROSSCHECK "<<q<<" "<<good<<"\n";
 }
 cout<<"CROSSCHECK_OK\n";
}
