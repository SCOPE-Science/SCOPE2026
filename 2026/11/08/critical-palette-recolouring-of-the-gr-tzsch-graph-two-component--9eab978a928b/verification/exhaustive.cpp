#include <bits/stdc++.h>
using namespace std;
int main(){
 const int k=4, m=11; vector<vector<int>> adj(m);
 auto add=[&](int i,int j){adj[i].push_back(j); adj[j].push_back(i);};
 for(int i=0;i<5;i++){add(i,(i+1)%5);add(5+i,(i+1)%5);add(5+i,(i+4)%5);add(5+i,10);}
 vector<int> p(m,0),code2id(1<<22,-1),codes; vector<array<uint8_t,11>> cs;
 function<void(int,int)> rec=[&](int v,int code){
  if(v==m){code2id[code]=cs.size();codes.push_back(code);array<uint8_t,11> s{};for(int j=0;j<m;j++)s[j]=p[j];cs.push_back(s);return;}
  for(int c=0;c<k;c++) {bool ok=1;for(int nb:adj[v])if(nb<v && p[nb]==c)ok=0;if(ok){p[v]=c;rec(v+1,code|(c<<(2*v)));}}
 };rec(0,0);
 int n=cs.size();vector<vector<int>> g(n);long long twice=0;map<int,int> degree;
 for(int id=0;id<n;id++){
  auto &s=cs[id];int code=codes[id];
  for(int v=0;v<m;v++) {
   int mask=0;for(int j:adj[v])mask|=(1<<s[j]);
   for(int c=0;c<k;c++)if(c!=s[v] && !(mask>>c&1)) {
    int cod2=(code&~(3<<(2*v)))|(c<<(2*v));int to=code2id[cod2];if(to<0){cerr<<"ERROR code2id\n";return 1;}g[id].push_back(to);
   }
  }
  twice+=g[id].size();degree[g[id].size()]++;
 }
 cout<<"states "<<n<<" edges "<<twice/2<<" degrees";for(auto [d,num]:degree)cout<<" "<<d<<":"<<num;cout<<"\n";
 vector<int> comp(n,-1),sizes;int cc=0;
 for(int root=0;root<n;root++)if(comp[root]<0){
  vector<int> q{root};comp[root]=cc;
  for(int i=0;i<(int)q.size();i++)for(int to:g[q[i]])if(comp[to]<0){comp[to]=cc;q.push_back(to);}
  sizes.push_back(q.size());cc++;
 }
 cout<<"components "<<cc;for(auto sz:sizes)cout<<" "<<sz;cout<<"\n";
 vector<int> eccentric(n);long long distpairs[100]={0};int diam=0;
 vector<int> dist(n,-1),q(n);
 for(int root=0;root<n;root++){
  fill(dist.begin(),dist.end(),-1);int a=0,b=0;dist[root]=0;q[b++]=root;
  while(a<b){int v=q[a++];for(int to:g[v])if(dist[to]<0){dist[to]=dist[v]+1;q[b++]=to;}}
  int ecc=0;
  for(int j=0;j<n;j++)if(dist[j]>=0){ecc=max(ecc,dist[j]);if(j>root)distpairs[dist[j]]++;}
  eccentric[root]=ecc;
  if(root%2000==0)cerr<<"BFS "<<root<<" / "<<n<<"\n";
 }
 map<int,int> eccc;for(int e:eccentric){eccc[e]++;diam=max(diam,e);}cout<<"ecc";for(auto [d,n]:eccc)cout<<" "<<d<<":"<<n;cout<<"\n";
 cout<<"pairdistance";for(int j=1;j<=diam;j++)cout<<" "<<j<<":"<<distpairs[j];cout<<"\n";
 cout<<"percomponent eccentricities\n";for(int c=0;c<cc;c++){
  map<int,int> d;for(int i=0;i<n;i++)if(comp[i]==c)d[eccentric[i]]++;
  cout<<c<<":";for(auto [di,nt]:d)cout<<" "<<di<<":"<<nt;cout<<"\n";
 }
 return 0;
}
