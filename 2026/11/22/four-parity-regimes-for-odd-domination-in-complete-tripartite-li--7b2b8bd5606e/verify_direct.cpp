// Independent exhaustive closed-neighborhood search on finite complete tripartite line graphs.
// The finite tests do not replace the universal parity proof.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Case{int a,b,c;};
int main(){
  vector<Case> cases={{1,1,1},{2,2,2},{1,1,2},{1,2,2},{3,2,2},{3,3,2},{1,3,3},{1,2,4},{3,1,4},{1,1,4},{2,2,3}};
  for(auto [a,b,c]:cases){
    vector<int> part;for(int i=0;i<a;i++)part.push_back(0);
    for(int i=0;i<b;i++)part.push_back(1);
    for(int i=0;i<c;i++)part.push_back(2);
    int n=part.size();vector<pair<int,int>> ed;
    for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(part[u]!=part[v])ed.push_back({u,v});
    int m=ed.size();if(m>21){cerr<<"overlarge test";return 1;}
    vector<uint64_t> neigh(m), adj(m);
    for(int i=0;i<m;i++)for(int j=0;j<m;j++){
      auto [u,v]=ed[i];auto [x,y]=ed[j];
      if(i==j || u==x||u==y||v==x||v==y)neigh[i]|=1ULL<<j;
      if(i!=j && (u==x||u==y||v==x||v==y))adj[i]|=1ULL<<j;
    }
    map<int,ll> all, connected;
    for(uint64_t mask=0;mask<(1ULL<<m);mask++){
      bool ok=true;for(uint64_t nm:neigh)if((__builtin_popcountll(mask&nm)&1)==0){ok=false;break;}
      if(!ok)continue;
      int w=__builtin_popcountll(mask);all[w]++;
      uint64_t reached=mask&(-mask),last=0;
      while(reached!=last){last=reached;uint64_t frontier=reached;
        while(frontier){int e=__builtin_ctzll(frontier);frontier&=frontier-1;reached|=adj[e]&mask;}
      }
      if(reached==mask)connected[w]++;
    }
    // Independent expected profiles by counting parity-based vertex partition patterns.
    map<int,ll> predicted,pc;
    for(unsigned int p=0;p<(1U<<n);p++){
      int t[3]={0,0,0};for(int v=0;v<n;v++)t[part[v]]^=(p>>v)&1U;
      bool condition=true;
      for(int v=0;v<n;v++){
        int others=0;for(int j=0;j<3;j++)if(j!=part[v])others+= (j==0?a:(j==1?b:c));
        int parity=others&1;
        if((((1+parity)*((p>>v)&1U))&1) != (parity ^ t[(part[v]+1)%3] ^ t[(part[v]+2)%3])){condition=false;break;}
      }
      if(!condition)continue;
      uint64_t selected=0;for(int e=0;e<m;e++){auto [u,v]=ed[e];if(((p>>u)&1U)==((p>>v)&1U))selected|=1ULL<<e;}
      int w=__builtin_popcountll(selected);predicted[w]++;
      uint64_t reached=selected&(-selected),last=0;
      while(reached!=last){last=reached;uint64_t frontier=reached;while(frontier){int e=__builtin_ctzll(frontier);frontier&=frontier-1;reached|=adj[e]&selected;}}
      if(reached==selected)pc[w]++;
    }
    if(all!=predicted||connected!=pc){cerr<<"Mismatch "<<a<<","<<b<<","<<c<<"\n";return 2;}
    ll cnt=0,conn=0;for(auto [w,k]:all)cnt+=k;for(auto[w,k]:connected)conn+=k;
    int odd=(a&1)+(b&1)+(c&1);ll expected=0,expectedc=0;
    if(odd==0){expected=1;expectedc=1;}
    else if(odd==3){expected=4;expectedc=4;}
    else if(odd==2){int u=0;for(int k:{a,b,c})if(k&1)u+=k;expected=1LL<<(u-2);expectedc=1;}
    else {int u=0;for(int k:{a,b,c})if(!(k&1))u+=k;expected=1LL<<(u-2);expectedc=0;}
    if(cnt!=expected||conn!=expectedc){cerr<<"Classification failed";return 3;}
    cout<<"K_("<<a<<","<<b<<","<<c<<") edges="<<m<<" odd="<<cnt<<" connected="<<conn<<" profile=";
    for(auto [w,k]:all)cout<<w<<":"<<k<<",";cout<<"\n";
  }
  cout<<"ALL_DIRECT_CASES_PASS\n";
}
