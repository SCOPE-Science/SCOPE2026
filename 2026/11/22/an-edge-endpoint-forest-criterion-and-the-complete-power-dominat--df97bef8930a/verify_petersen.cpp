// Separate verification using the classical outer/inner/spoke Petersen model.
// Does not rely on the Kneser labels or on the other verifier.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
  constexpr int N = 15;
  vector<pair<int,int>> edges;
  for (int i=0; i<5; ++i) edges.push_back({i,(i+1)%5});
  for (int i=0; i<5; ++i) edges.push_back({5+i,5+(i+2)%5});
  for (int i=0; i<5; ++i) edges.push_back({i,5+i});
  assert(edges.size()==N);
  array<int,N> neighbors{};
  for(int i=0;i<N;++i) for(int j=0;j<N;++j) {
    if(i==j) continue;
    auto [a,b]=edges[i]; auto [c,d]=edges[j];
    if(a==c||a==d||b==c||b==d) neighbors[i] |= 1<<j;
  }
  for(int i=0;i<N;++i) assert(__builtin_popcount((unsigned)neighbors[i])==4);
  vector<char> success(1<<N);
  map<int,int> count, failures;
  for(int s=0;s<(1<<N);++s){
    int observed=s;
    for(int j=0;j<N;++j) if(s>>j&1) observed |= neighbors[j];
    int prior;
    do {
      prior=observed;
      int newObs=0;
      for(int j=0;j<N;++j) if(observed>>j&1) {
        int missing=neighbors[j]&~observed;
        if(__builtin_popcount((unsigned)missing)==1) newObs|=missing;
      }
      observed |= newObs;
    } while(prior!=observed);
    success[s] = observed == ((1<<N)-1);
    // Disjoint-set acyclicity check on the original Petersen graph.
    int covered=0;
    for(int j=0;j<N;++j) if(s>>j&1) {
      covered |= (1<<edges[j].first) | (1<<edges[j].second);
    }
    array<int,10> parent;
    iota(parent.begin(),parent.end(),0);
    auto find=[&](int x){while(x!=parent[x]) x=parent[x];return x;};
    bool forest=true;
    for(auto [a,b]:edges) if(!(covered>>a&1) && !(covered>>b&1)){
      int ra=find(a), rb=find(b);
      if(ra==rb){forest=false;break;}
      parent[ra]=rb;
    }
    assert((bool)success[s]==forest);
    int k=__builtin_popcount((unsigned)s);
    if(success[s]) ++count[k]; else ++failures[k];
  }
  vector<int> min2, min3, minOther;
  for(int s=0;s<(1<<N);++s) if(success[s]) {
    bool minimal=true;
    for(int j=0;j<N;++j) if((s>>j&1) && success[s^(1<<j)]) minimal=false;
    if(minimal){int k=__builtin_popcount((unsigned)s);if(k==2)min2.push_back(s);else if(k==3)min3.push_back(s);else minOther.push_back(s);}
  }
  assert(min2.size()==15 && min3.size()==140 && minOther.empty());
  auto compSizes=[&](int budget, bool tokenJump){
    vector<char> visited(1<<N);
    vector<int> sizes;
    for(int s=0;s<(1<<N);++s){
      if(!success[s] || __builtin_popcount((unsigned)s)>budget || visited[s] || (tokenJump && __builtin_popcount((unsigned)s)!=2)) continue;
      queue<int> q;visited[s]=true;q.push(s);int count=0;
      while(!q.empty()){
        int t=q.front();q.pop();++count;
        for(int i=0;i<N;++i){
          if(!tokenJump){
            int nxt=t^(1<<i);
            if(success[nxt]&&__builtin_popcount((unsigned)nxt)<=budget&&!visited[nxt]){visited[nxt]=true;q.push(nxt);}
          } else if(t>>i&1) for(int j=0;j<N;++j) if(!(t>>j&1)) {
            int nxt=t^(1<<i)^(1<<j);
            if(success[nxt]&&!visited[nxt]){visited[nxt]=true;q.push(nxt);}
          }
        }
      }
      sizes.push_back(count);
    }
    sort(sizes.begin(),sizes.end());
    return sizes;
  };
  assert(compSizes(2,true)==vector<int>(5,3));
  assert(compSizes(2,false)==vector<int>(15,1));
  vector<int> tar3(140,1);tar3.insert(tar3.end(),5,40);
  assert(compSizes(3,false)==tar3);
  assert(compSizes(4,false)==vector<int>{1645});
  assert(count[2]==15 && count[3]==325 && count[4]==1305);
  assert(failures[0]==1 && failures[1]==15 && failures[2]==90 && failures[3]==130 && failures[4]==60 && failures[5]==12);
  for(int i=6;i<=15;++i) assert(failures[i]==0);
  cout<<"PASS Petersen outer-inner-spoke model; 32768 initial sets; forest equivalence; 15 optimal pairs; 140 minimal triples; TJ=5K3; k-TAR 2/3/4 = 15 isolates / (5x40 +140 isolates) / connected 1645 states.\n";
}
