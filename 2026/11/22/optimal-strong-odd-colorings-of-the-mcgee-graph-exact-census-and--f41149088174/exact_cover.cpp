#include <bits/stdc++.h>
using namespace std;
constexpr int N=24; const unsigned FULL=(1u<<N)-1;
unsigned nb[N]; vector<unsigned> by[N]; long long cnt[7]={}; vector<vector<unsigned>> witness;
void recgen(int p,unsigned chosen){
 if(p==N){
  if(!chosen)return;
  for(int v=0;v<N;v++)if(__builtin_popcount(chosen&nb[v])==2)return;
  for(int v=0;v<N;v++)if(chosen>>v&1) by[v].push_back(chosen);
  return;
 }
 recgen(p+1,chosen);
 if(!(chosen&nb[p]))recgen(p+1,chosen|(1u<<p));
}
vector<unsigned> curr; ofstream out("exact_cover_partitions.txt");
void cover(unsigned remaining,int depth,int k){
 if(!remaining){if(depth==k){cnt[k]++; if(k==5){auto v=curr;sort(v.begin(),v.end());for(auto a:v)out<<a<<" ";out<<"\n";}}return;}
 if(depth>=k)return;
 int v=__builtin_ctz(remaining);
 for(unsigned a:by[v]) if((a&remaining)==a){curr.push_back(a);cover(remaining^a,depth+1,k);curr.pop_back();}
}
int main(){int lcf[]={12,7,-7};
 for(int i=0;i<N;i++){
 int j=(i+1)%N; nb[i]|=1u<<j;nb[j]|=1u<<i;
 j=(i+lcf[i%3]+N)%N;nb[i]|=1u<<j;nb[j]|=1u<<i;
 }
 recgen(0,0);
 long long total=0;for(auto v:by)total+=v.size();
 cout << "candidate_class_memberships=" << total << "\n";
 for(int k=2;k<=5;k++){cover(FULL,0,k);cout<<"k="<<k<<" partitions="<<cnt[k]<<"\n";}
}
