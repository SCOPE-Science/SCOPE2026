#include <bits/stdc++.h>
using namespace std;
int E[21][2],cols[21],used[14],n=0; vector<uint64_t> V;
inline uint64_t pack(){uint64_t x=0;for(int i=0;i<21;i++)x|=(uint64_t)cols[i]<<(2*i);return x;}
bool acyclic_prefix(int p,int c){
 int u=E[p][0],v=E[p][1];
 for(int d=0;d<4;d++)if(d!=c){
  int seen=1<<u,Q[14],lo=0,hi=0;Q[hi++]=u;
  while(lo<hi){int x=Q[lo++];for(int t=0;t<p;t++){
    if(cols[t]!=c&&cols[t]!=d)continue;
    int y=E[t][0]==x?E[t][1]:(E[t][1]==x?E[t][0]:-1);
    if(y>=0&&!(seen>>y&1)){if(y==v)return false;seen|=1<<y;Q[hi++]=y;}
  }}
 }
 return true;
}
void dfs(int p){
 if(p==21){V.push_back(pack());return;}
 int u=E[p][0],v=E[p][1];
 for(int c=0;c<4;c++)if(!(used[u]>>c&1)&&!(used[v]>>c&1)){
  cols[p]=c; if(acyclic_prefix(p,c)){
    used[u]|=1<<c;used[v]|=1<<c;dfs(p+1);used[u]^=1<<c;used[v]^=1<<c;
  }
 }
}
inline uint64_t canonical(uint64_t x){
 int rename[4]={-1,-1,-1,-1};for(int i=0;i<3;i++)rename[(x>>(2*i))&3]=i;
 for(int c=0;c<4;c++)if(rename[c]<0)rename[c]=3;
 uint64_t y=0;for(int p=0;p<21;p++)y|=(uint64_t)rename[(x>>(2*p))&3]<<(2*p);return y;
}
// For the entire valid coloring only
bool valid(uint64_t z){
 int used[14]={};int pars[6][14],nr=0;for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
  iota(pars[nr],pars[nr]+14,0);nr++;
 }
 auto find=[&](int *p,int x){while(p[x]!=x)x=p[x]=p[p[x]];return x;};
 for(int e=0;e<21;e++){
  int c=(z>>(2*e))&3;int u=E[e][0],v=E[e][1];
  if(used[u]>>c&1||used[v]>>c&1)return false;
  used[u]|=1<<c;used[v]|=1<<c;
  nr=0;
  for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
   if(c==a||c==b){int x=find(pars[nr],u),y=find(pars[nr],v);if(x==y)return false;pars[nr][x]=y;}nr++;
  }
 }
 return true;
}
int main(){
 int lines[7][3]={{0,1,3},{1,2,4},{2,3,5},{3,4,6},{0,4,5},{1,5,6},{0,2,6}};
 for(int p=0;p<7;p++)for(int l=0;l<7;l++)for(int k=0;k<3;k++)if(lines[l][k]==p)E[n][0]=p,E[n++][1]=7+l;
 for(int p=0;p<3;p++){cols[p]=p;used[E[p][0]]|=1<<p;used[E[p][1]]|=1<<p;}
 dfs(3);cerr<<"enumerated "<<V.size()<<"\n";
 unordered_map<uint64_t,int> M;M.reserve(V.size()*2);for(int i=0;i<(int)V.size();i++)M[V[i]]=i;
 vector<vector<int>> adj(V.size()); long long arcs=0,loops=0;map<int,int> dcounts;
 for(int i=0;i<(int)V.size();i++){
  auto z=V[i];
  for(int e=0;e<21;e++){
   int old=(z>>(2*e))&3;
   for(int c=0;c<4;c++)if(c!=old){
    uint64_t t=(z&~(3ULL<<(2*e)))|((uint64_t)c<<(2*e));
    if(!valid(t))continue;
    t=canonical(t);auto it=M.find(t);
    if(it==M.end()){cerr<<"UNMATCHED!!!"<<e<<"\n";return 1;}
    adj[i].push_back(it->second);arcs++;if(it->second==i)loops++;
   }
  }
  sort(adj[i].begin(),adj[i].end());adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
  dcounts[(int)adj[i].size()]++;
 }
 cout<<"loops="<<loops<<"\n"; cout<<"states="<<V.size()<<" arcs with multiplicity="<<arcs<<" quotient edges="<<accumulate(adj.begin(),adj.end(),0LL,[](long long a,const auto &x){return a+x.size();})/2<<"\n";
 cout<<"degrees ";for(auto [a,b]:dcounts)cout<<a<<":"<<b<<" ";cout<<"\n";
 vector<char> seen(V.size());vector<int> comps;map<int,int> sizes;int nontrivial=0;vector<vector<int>> groups;
 for(int i=0;i<(int)V.size();i++)if(!seen[i]){
  vector<int> Q(1,i);seen[i]=1;
  for(int t=0;t<(int)Q.size();t++)for(int j:adj[Q[t]])if(!seen[j]){seen[j]=1;Q.push_back(j);}
  sizes[Q.size()]++;if(Q.size()>1)nontrivial++; groups.push_back(move(Q));
 }
 cout<<"components ";for(auto [a,b]:sizes)cout<<a<<":"<<b<<" ";cout<<"\n";
  map<int,map<int,int>> profiles;
  for(auto &G:groups){int size=G.size(); for(int idx:G){int cnt[4]={};for(int p=0;p<21;p++)cnt[(V[idx]>>(2*p))&3]++;sort(cnt,cnt+4);int key=cnt[0]*1000+cnt[1]*100+cnt[2]*10+cnt[3];profiles[size][key]++;}}
  for(auto [size,h]:profiles){cout<<"profile size "<<size<<": ";for(auto [key,cnt]:h)cout<<key<<"="<<cnt<<" ";cout<<"\n";}

 // Compute some sample eccentricities and exact diam for small comp; large via 6 sources, no unsupported claim
 for(int gi=0;gi<(int)groups.size();gi++){
  auto &G=groups[gi];if(G.size()==1)continue;
  int lo=INT_MAX,hi=0,nsrc=min((int)G.size(),8);vector<int> dist(V.size(),-1);
  for(int q=0;q<nsrc;q++){
   int src=G[q],maxd=0;vector<int> Q(1,src);dist[src]=0;
   for(int t=0;t<(int)Q.size();t++)for(int j:adj[Q[t]])if(dist[j]<0){dist[j]=dist[Q[t]]+1;maxd=max(maxd,dist[j]);Q.push_back(j);}
   for(int j:Q)dist[j]=-1;
   lo=min(lo,maxd);hi=max(hi,maxd);
  }
  cout<<"sample comp "<<gi<<" size="<<G.size()<<" max-ecc-sample="<<hi<<"\n";if(gi>=6)break;
 }
}
