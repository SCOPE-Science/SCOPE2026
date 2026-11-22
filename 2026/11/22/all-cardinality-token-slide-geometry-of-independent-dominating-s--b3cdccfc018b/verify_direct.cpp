#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using U=unsigned int;
long long comb(int n,int k){if(k<0||k>n)return 0;long long v=1;for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v;}
int main(){
 for(int n=2;n<=10;n++){
  int N=2*n;vector<U> neigh(N,0);auto add=[&](int a,int b){neigh[a]|=(U(1)<<b);neigh[b]|=(U(1)<<a);};
  for(int j=0;j<n;j++){add(2*j,2*j+1);if(j)for(int b=0;b<2;b++)add(2*j+b,2*(j-1)+b);}
  vector<vector<U>> sets(n+1);
  for(U mask=0;mask<(U(1)<<N);mask++){
   int k=__builtin_popcount(mask);if(k>n)continue;
   bool independent=true;
   U dominated=mask;
   for(int v=0;v<N;v++)if((mask>>v)&1){if(neigh[v]&mask){independent=false;break;}dominated|=neigh[v];}
   if(independent && dominated==(U(1)<<N)-1)sets[k].push_back(mask);
  }
  long long total=0;
  for(int k=0;k<=n;k++){
   auto &vec=sets[k];int z=n-k,p=k-1;long long expected=2*comb(p,z);
   assert((long long)vec.size()==expected);
   total+=vec.size();
   map<U,int> ix;for(int j=0;j<(int)vec.size();j++)ix[vec[j]]=j;
   vector<vector<int>> adj(vec.size());long long e=0;
   for(int i=0;i<(int)vec.size();i++){
    U mask=vec[i];
    for(int a=0;a<N;a++)if((mask>>a)&1){
     U cand=neigh[a] & ~mask;
     for(int b=0;b<N;b++)if((cand>>b)&1){
      U next=(mask^(U(1)<<a))|(U(1)<<b);
      auto it=ix.find(next);
      if(it!=ix.end() && it->second>i){adj[i].push_back(it->second);adj[it->second].push_back(i);e++;}
     }
    }
   }
   long long expe=(z>=1 && z<=k-2)? 2LL*(k-2)*comb(k-3,z-1) : 0;
   assert(e==expe);
   if(!vec.empty()){
    vector<int> component(vec.size(),-1);vector<int> sizes,diam;
    for(int s=0;s<(int)vec.size();s++)if(component[s]<0){
     int id=sizes.size();queue<int> q;q.push(s);component[s]=id;int cnt=0;
     while(!q.empty()){int a=q.front();q.pop();cnt++;for(int b:adj[a])if(component[b]<0){component[b]=id;q.push(b);}}
     sizes.push_back(cnt);
    }
    assert(sizes.size()==2);
    assert(sizes[0]==comb(p,z)&&sizes[1]==comb(p,z));
    int expected_d=z*(p-z);
    for(int s=0;s<(int)vec.size();s++){
     vector<int>d(vec.size(),-1);queue<int>q;q.push(s);d[s]=0;int far=0;
     while(!q.empty()){int a=q.front();q.pop();far=max(far,d[a]);for(int b:adj[a])if(d[b]<0){d[b]=d[a]+1;q.push(b);}}
     assert(far<=expected_d);
     diam.push_back(far);
    }
    assert(*max_element(diam.begin(),diam.end())==expected_d);
   }
  }
  cout<<"n="<<n<<" max_independent_sets="<<total<<" min_size=";for(int k=0;k<=n;k++)if(!sets[k].empty()){cout<<k;break;}cout<<" all_size_components=2 edge_and_distance_checked\n";
 }
 cout<<"DIRECT_EXHAUSTIVE_PASS\n";
}
