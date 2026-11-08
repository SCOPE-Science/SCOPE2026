#include <bits/stdc++.h>
using namespace std;
int q,L;vector<vector<int>> permutations_;vector<int>w;long long success;
void dfs(int d,int seen){
 if(d==L){
  for(auto &p:permutations_){int k=0;for(int v:w)if(k<q&&v==p[k])++k;if(k!=q)return;}
  ++success;return;
 }
 for(int x=0;x<=seen&&x<q;x++){
  if(d&&w[d-1]==x)continue;
  w.push_back(x);dfs(d+1,seen+(x==seen));w.pop_back();
 }
}
int main(){
 for(q=1;q<=4;q++){
  vector<int>p(q);iota(p.begin(),p.end(),0);permutations_.clear();do{permutations_.push_back(p);}while(next_permutation(p.begin(),p.end()));
  int L0=(q==1?1:(q==2?2:(q==3?6:11)));
  int L1=(q==1?1:(q==2?3:(q==3?7:12)));
  for(L=L0;L<=L1;L++){
   success=0;dfs(0,0);cout<<"q="<<q<<" length="<<L<<" normalized_complete="<<success<<'\n';
  }
 }
}
