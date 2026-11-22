#include <bits/stdc++.h>
using namespace std;
// Direct definition, without using the four-type criterion as a filter.
int main(){constexpr int n=6,N=36,k=9; uint64_t row[n]={},col[n]={},nb[N];
for(int i=0;i<n;i++)for(int j=0;j<n;j++){row[i]|=1ULL<<(i*n+j);col[j]|=1ULL<<(i*n+j);}
for(int q=0;q<N;q++)nb[q]=row[q/n]|col[q%n];
uint64_t all=0,valid=0;array<uint64_t,4> types={};
auto start=chrono::steady_clock::now();
for(uint64_t x=(1ULL<<k)-1;x<(1ULL<<N);){all++;
 bool ok=true;
 for(int i=0;i<n;i++)if(!(x&row[i])||!(x&col[i])){ok=false;break;}
 if(ok){uint64_t s[N];int seen=0;
 for(int q=0;q<N;q++){
  uint64_t sig=nb[q]&x;if(!sig){ok=false;break;}
  for(int j=0;j<seen;j++)if(s[j]==sig){ok=false;break;}
  if(!ok)break;s[seen++]=sig;
 }
 if(ok){valid++;
  int deg[12]={};int adj[12][12]={};
  for(uint64_t v=x;v;v&=v-1){int q=__builtin_ctzll(v),r=q/n,c=q%n;deg[r]++;deg[n+c]++;adj[r][n+c]=adj[n+c][r]=1;}
  bool visited[12]={};vector<string> components;
  for(int u=0;u<12;u++)if(!visited[u]){
   vector<int> nodes={u};visited[u]=true;
   for(int t=0;t<(int)nodes.size();t++)for(int j=0;j<12;j++)if(adj[nodes[t]][j]&&!visited[j]){visited[j]=true;nodes.push_back(j);}
   string a=to_string(nodes.size())+":";vector<int>d;for(int v:nodes)d.push_back(deg[v]);sort(d.begin(),d.end());for(int v:d)a+=to_string(v);components.push_back(a);
  }sort(components.begin(),components.end());
  string cat;for(const auto &z:components)cat+=z+"/";
  if(cat=="4:1122/4:1122/4:1122/")types[0]++;
  else if(cat=="2:11/4:1122/6:112222/")types[1]++;
  else if(cat=="2:11/4:1122/6:111223/")types[2]++;
  else if(cat=="2:11/5:11222/5:11222/")types[3]++;
  else{cerr<<"Unexpected valid configuration "<<cat<<"\n";return 2;}
 }
 }
 uint64_t c=x&-x,y=x+c;x=(((x^y)>>2)/c)|y;
}
cout<<"candidates="<<all<<" identified="<<valid<<" four_types=";
for(int i=0;i<4;i++)cout<<types[i]<<(i==3?'\n':',');
cout<<"elapsed_seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<'\n';
if(all!=94143280 || types!=array<uint64_t,4>{86400,518400,518400,129600})return 1;
}
