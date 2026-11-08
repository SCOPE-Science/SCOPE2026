#include <bits/stdc++.h>
using namespace std;
int dista[10][10], labels[10];
vector<array<unsigned char,10>> states;
unordered_map<unsigned long long,int> ids;
unsigned long long code(const array<unsigned char,10>& a){unsigned long long x=0;for(int i=0;i<10;i++)x|=(unsigned long long)a[i]<<(i*4);return x;}
int recurse(int i,int high,int limit){
  if(i==10){if(high!=limit-1)return 0;
    array<unsigned char,10> p;for(int j=0;j<10;j++)p[j]=labels[j];
    int bins[4][10];int nbin[4]={};
    for(int j=0;j<10;j++)bins[labels[j]][nbin[labels[j]]++]=j;
    for(int x=0;x<10;x++)for(int y=x+1;y<10;y++){
      bool distinct=0;
      for(int b=0;b<limit;b++){
        int a=20,c=20;
        for(int t=0;t<nbin[b];t++){a=min(a,dista[x][bins[b][t]]);c=min(c,dista[y][bins[b][t]]);}
        if(a!=c){distinct=1;break;}
      }
      if(!distinct)return 0;
    }
    ids[code(p)]=states.size();states.push_back(p);return 1;
  }
  int v=0;for(int j=0;j<=min(limit-1,high+1);j++){labels[i]=j;v+=recurse(i+1,max(high,j),limit);}return v;
}
array<unsigned char,10> normalize(array<unsigned char,10> p){int trans[4]={-1,-1,-1,-1},k=0;for(int i=0;i<10;i++){auto &x=trans[p[i]];if(x<0)x=k++;p[i]=x;}return p;}
int main(){vector<pair<int,int>> E;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)E.push_back({i,j});
  for(int i=0;i<10;i++)for(int j=0;j<10;j++)dista[i][j]=(i==j)?0:(E[i].first!=E[j].first&&E[i].first!=E[j].second&&E[i].second!=E[j].first&&E[i].second!=E[j].second)?1:2;
  labels[0]=0;
  int s3=recurse(1,0,3);cout<<"three_partitions="<<s3<<"\n";if(s3!=0){cerr<<"unexpected three-block resolution";return 3;}
  states.clear();ids.clear();int s4=recurse(1,0,4);cout<<"four_partitions="<<s4<<"\n";if(s4!=7040){cerr<<"unexpected four-block count";return 4;}
  vector<vector<int>> adj(states.size());
  for(int i=0;i<(int)states.size();i++){
    auto p=states[i];int counts[4]={};for(auto x:p)counts[x]++;
    for(int v=0;v<10;v++)if(counts[p[v]]>1){for(int z=0;z<4;z++)if(z!=p[v]){
       auto q=p;q[v]=z;q=normalize(q);
       auto it=ids.find(code(q));if(it!=ids.end())adj[i].push_back(it->second);
    }}
    sort(adj[i].begin(),adj[i].end());adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
  }
  int e=0;map<int,int> degrees;for(int i=0;i<(int)states.size();i++) {e+=adj[i].size();degrees[adj[i].size()]++;for(int j:adj[i])if(!binary_search(adj[j].begin(),adj[j].end(),i)){cerr<<"asymmetry";return 5;} }
  cout<<"edges="<<e/2<<" degrees=";for(auto [a,b]:degrees)cout<<a<<":"<<b<<",";cout<<"\n";
  vector<char> vis(states.size(),0);int comps=0;map<int,int> compsizes;
  for(int i=0;i<(int)states.size();i++)if(!vis[i]){comps++;int x=0;queue<int> q;q.push(i);vis[i]=1;while(q.size()){int u=q.front();q.pop();x++;for(int v:adj[u])if(!vis[v])vis[v]=1,q.push(v);}compsizes[x]++;}cout<<"components="<<comps<<" comp_sizes=";for(auto [a,b]:compsizes)cout<<a<<":"<<b<<",";cout<<"\n";
  vector<int> dd(states.size());map<int,int> ecc;long long pairs=0;map<int,long long> distance_profile;
  for(int i=0;i<(int)states.size();i++){
    fill(dd.begin(),dd.end(),-1);dd[i]=0;vector<int> q;q.reserve(states.size());q.push_back(i);int maxd=0;
    for(size_t j=0;j<q.size();j++){int u=q[j];maxd=max(maxd,dd[u]);for(int v:adj[u])if(dd[v]<0)dd[v]=dd[u]+1,q.push_back(v);}
    if(q.size()!=states.size()){cerr<<"disconnected";return 2;}
    ecc[maxd]++;for(int j=i+1;j<(int)states.size();j++)distance_profile[dd[j]]++,pairs++;
  }
  cout<<"eccentricities=";for(auto [a,b]:ecc)cout<<a<<":"<<b<<",";cout<<"\n";
  cout<<"pair_distances=";for(auto [a,b]:distance_profile)cout<<a<<":"<<b<<",";cout<<"\n";
  // Record size distributions of unlabelled partitions
  map<string,int> types;
  for(auto &p:states){int sizes[4]={};for(auto c:p)sizes[c]++;sort(sizes,sizes+4);string s;for(int x:sizes)s+=to_string(x)+",";types[s]++;}
  cout<<"part_sizes=";for(auto [a,b]:types)cout<<a<<":"<<b<<";";cout<<"\n";
  if(e/2!=34500 || comps!=1 || ecc!=map<int,int>{{7,6300},{8,740}} || pairs!=24777280){cerr<<"certification mismatch";return 6;}cout<<"CHECK_OK\n";
}
