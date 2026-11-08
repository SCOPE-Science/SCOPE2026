#include <bits/stdc++.h>
using namespace std;
// Exhaustive enumeration with explicit reachable-subsequence sets, rather than
// the greedy per-permutation automaton used by the companion checker.
using BS=bitset<120>;
array<vector<array<int,5>>,6> strings_by_size;
int jump_idx[6][120][5];
array<BS,6> seen;
int word_[20];
vector<string> solutions;
long long visits[20];
int m[6]={0,1,3,7,12,19};
int L;
void init(){
 for(int len=1;len<=5;len++){
  function<void(int,int,array<int,5>)> f=[&](int d,int mask,array<int,5> a){
   if(d==len){strings_by_size[len].push_back(a);return;}
   for(int x=0;x<5;x++)if(!(mask&(1<<x))){a[d]=x;f(d+1,mask|(1<<x),a);}
  };
  f(0,0,{});
 }
 memset(jump_idx,-1,sizeof(jump_idx));
 for(int len=1;len<=4;len++)for(int i=0;i<(int)strings_by_size[len].size();i++)for(int x=0;x<5;x++){
  bool present=false;for(int k=0;k<len;k++)if(strings_by_size[len][i][k]==x)present=true;
  if(present)continue;
  auto a=strings_by_size[len][i];a[len]=x;
  auto &v=strings_by_size[len+1];
  for(int j=0;j<(int)v.size();j++)if(v[j]==a){jump_idx[len][i][x]=j;break;}
 }
}
void dfs(int d,int used){
 visits[d]++;
 if(d==L){if(seen[5].count()==120){string s;for(int i=0;i<L;i++)s.push_back('0'+word_[i]);solutions.push_back(s);}return;}
 for(int x=0;x<=used&&x<5;x++){
  if(d&&word_[d-1]==x)continue;
  word_[d]=x;
  array<BS,6> save=seen;
  for(int len=5;len>=2;len--){
   for(int j=0;j<(int)strings_by_size[len-1].size();j++)if(seen[len-1][j]){
    int k=jump_idx[len-1][j][x];if(k>=0)seen[len].set(k);
   }
  }
  seen[1].set(x);
  int nd=d+1;
  // The first t symbols of every full permutation must have been embedded
  // by L-m(5-t); m(r) is certified independently for r<5.
  bool ok=true;
  for(int t=1;t<=5;t++)if(nd>=L-m[5-t]){
    if(seen[t].count()!=strings_by_size[t].size()){ok=false;break;}
  }
  if(ok)dfs(nd,used+(x==used));
  seen=save;
 }
}
int main(int argc,char**argv){L=(argc>1)?atoi(argv[1]):19;if(L<5||L>19)return 2;init();dfs(0,0);sort(solutions.begin(),solutions.end());cerr<<"L="<<L<<" normalized="<<solutions.size()<<" nodes=";for(int d=0;d<=L;d++)cerr<<visits[d]<<",";cerr<<"\n";for(auto&s:solutions)cout<<s<<'\n';}
