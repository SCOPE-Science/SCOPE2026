// A second implementation: Cayley F_2^4 model rather than even 5-bit words.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
static int pc(int x){return __builtin_popcount((unsigned)x);}
int main(){
  constexpr int N=16, ALL=(1<<N)-1;
  const array<int,5> gens={1,2,4,8,15};
  array<int,N> adj{};
  for(int v=0;v<N;v++)for(int g:gens) adj[v]|=1<<(v^g);
  for(int v=0;v<N;v++) assert(pc(adj[v])==5);
  set<int> geodesics;
  for(int v=0;v<N;v++)for(int a=0;a<N;a++)if(adj[v]>>a&1)
    for(int b=a+1;b<N;b++)if(adj[v]>>b&1)
      assert(!(adj[a]>>b&1)), geodesics.insert((1<<a)|(1<<v)|(1<<b));
  assert(geodesics.size()==160);
  array<bool,1<<N> good{};
  map<int,int> poly;
  int valid=0;
  for(int t=0;t<=ALL;t++){
    bool hit=true;
    for(int path:geodesics){if((t&path)==path){hit=false;break;}}
    bool deg=true;
    for(int v=0;v<N;v++)if((t>>v)&1 && pc(adj[v]&t)>1){deg=false;break;}
    assert(hit==deg);
    good[t]=hit;
    if(hit){valid++;poly[N-pc(t)]++;}
  }
  assert(valid==2143);
  assert((poly==map<int,int>({{8,10},{9,80},{10,280},{11,576},{12,660},
                             {13,400},{14,120},{15,16},{16,1}})));
  // Five linearly independent-character masks with the one relation among generators.
  const array<int,5> forms={14,13,11,7,15};
  set<int> H,J;
  for(int f:forms)for(int parity=0;parity<=1;parity++){
    int mask=0;for(int v=0;v<N;v++)if((pc(v&f)&1)==parity)mask|=1<<v;
    H.insert(mask);
  }
  for(int v=0;v<N;v++)J.insert(adj[v]);
  assert(H.size()==10&&J.size()==16);
  set<int> maximal;
  for(int t=0;t<=ALL;t++)if(good[t]){
    bool max=true;
    for(int v=0;v<N;v++)if(!(t>>v&1) && good[t|(1<<v)]){max=false;break;}
    if(max) maximal.insert(t);
  }
  set<int> expected=H;expected.insert(J.begin(),J.end());
  assert(maximal==expected);
  const array<int,5> expect_comps={10,10,10,26,1};
  const array<int,5> expect_sizes={10,90,370,946,1606};
  for(int budget=8;budget<=12;budget++){
    vector<char> exists(ALL+1,false), seen(ALL+1,false);
    int nstate=0, components=0;
    for(int t=0;t<=ALL;t++)if(good[t] && 16-pc(t)<=budget){exists[t]=true;nstate++;}
    for(int t=0;t<=ALL;t++)if(exists[t]&&!seen[t]){
      components++;queue<int> q;q.push(t);seen[t]=true;
      while(!q.empty()){
        int u=q.front();q.pop();
        for(int bit=0;bit<N;bit++){
          int w=u^(1<<bit);
          if(exists[w]&&!seen[w]){seen[w]=true;q.push(w);}
        }
      }
    }
    assert(nstate==expect_sizes[budget-8]);
    assert(components==expect_comps[budget-8]);
  }
  // Independent breadth-first derivation of all minimum-to-minimum distances.
  vector<int> opt(H.begin(),H.end()); map<int,int> distance_hist;
  for(int k=0;k<(int)opt.size();k++){
    vector<int> dist(ALL+1,-1);queue<int> q;
    q.push(opt[k]);dist[opt[k]]=0;
    while(!q.empty()){
      int t=q.front();q.pop();
      for(int v=0;v<N;v++){
        int w=t^(1<<v);
        if(good[w]&&16-pc(w)<=12&&dist[w]==-1){dist[w]=dist[t]+1;q.push(w);}
      }
    }
    for(int j=k+1;j<(int)opt.size();j++)distance_hist[dist[opt[j]]]++;
  }
  assert((distance_hist==map<int,int>({{8,40},{16,5}})));
  cout<<"VERIFY_OK CLEBSCH_FOLDED_CUBE_INDEPENDENT\n";
  cout<<"VALID_SETS "<<valid<<" MAXIMAL "<<maximal.size()<<" OPTIMAL "<<H.size()<<"\n";
  cout<<"BUDGET_8_TO_12_COMPONENTS 10 10 10 26 1\n";
}
