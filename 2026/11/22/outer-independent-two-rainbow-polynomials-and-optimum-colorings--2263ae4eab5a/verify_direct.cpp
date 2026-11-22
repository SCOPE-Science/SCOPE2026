// Direct exhaustive check using the Kneser adjacency definition.
#include <bits/stdc++.h>
using namespace std;
using LL=long long;
vector<pair<int,int>> E;
vector<vector<int>> adj;
void init(int n){
 E.clear(); adj.clear();
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)E.push_back({u,v});
 int N=E.size(); adj.resize(N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){
 auto [a,b]=E[i]; auto [c,d]=E[j];
 if(a!=c&&a!=d&&b!=c&&b!=d) adj[i].push_back(j);
 }
}
bool good(const vector<int>&f){
 for(int i=0;i<(int)f.size();i++)if(f[i]==0){
   int mask=0;
   for(int j:adj[i]){
     if(f[j]==0)return false;
     mask|=f[j];
   }
   if(mask!=3)return false;
 }
 return true;
}
int main(){
 init(5);
 const int N=E.size();
 vector<int> f(N);
 vector<LL> freq(2*N+1);
 for(int code=0;code<(1<<(2*N));code++){
  int x=code,weight=0;
  for(int i=0;i<N;i++){
   f[i]=x&3;
   weight+=((x&3)==3?2:(x&3)!=0);
   x>>=2;
  }
  if(good(f))freq[weight]++;
 }
 cout<<"n5:";for(int k=0;k<(int)freq.size();k++)if(freq[k])cout<<" "<<k<<":"<<freq[k];cout<<"\n";
 vector<LL> expected={0,0,0,0,0,0,90,2120,13640,42460,80404,103700,97005,68220,36750,15244,4830,1140,190,20,1};
 if(freq!=expected)return 1;
 for(int n=5;n<=7;n++){
  init(n);
  vector<vector<int>> stars(n);vector<int> core;
  LL count=0;
  for(int c=0;c<n;c++){
   stars.assign(n,{});core.clear();
   for(int i=0;i<(int)E.size();i++){
      if(E[i].first==c || E[i].second==c)stars[c].push_back(i);
      else core.push_back(i);
   }
   if(core.size()>22)return 2;
   f.assign(E.size(),0);
   for(uint64_t mask=0;mask<(1ULL<<core.size());mask++){
      for(int i=0;i<(int)core.size();i++) f[core[i]]=(mask>>i&1)?1:2;
      count+=good(f);
   }
  }
  LL expected=(n==5?90:n==6?5352:226968);
  cout<<"optimal "<<n<<":"<<count<<" expected="<<expected<<"\n";
  if(count!=expected)return 3;
 }
 cout<<"DIRECT_OK\n";
}
