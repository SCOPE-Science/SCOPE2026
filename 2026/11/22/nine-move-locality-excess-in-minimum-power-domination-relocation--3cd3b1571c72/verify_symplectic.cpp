// Exhaustive independent certification on the symplectic generalized quadrangle of order two.
// Build: g++ -O2 -std=c++17 verify_symplectic.cpp -o verify_symplectic
// Run: ./verify_symplectic
#include <bits/stdc++.h>
using namespace std;
uint32_t adjv[30], V=(1u<<30)-1;
int symp(int x,int y){
 auto b=[](int x,int k){return (x>>k)&1;};
 return (b(x,0)&b(y,1))^(b(x,1)&b(y,0))^(b(x,2)&b(y,3))^(b(x,3)&b(y,2));
}
vector<array<int,3>> lines;
void build(){
 set<array<int,3>> L;
 for(int x=1;x<16;x++) for(int y=x+1;y<16;y++) if(symp(x,y)==0){
   array<int,3> line={x,y,x^y};sort(line.begin(),line.end());L.insert(line);
 }
 lines.assign(L.begin(),L.end());
 if(lines.size()!=15)throw runtime_error("not 15 isotropic lines");
 for(int i=0;i<15;i++) for(int j=0;j<15;j++){
  if(find(lines[j].begin(),lines[j].end(),i+1)!=lines[j].end()){
   adjv[i] |=1u<<(j+15);adjv[j+15]|=1u<<i;
  }
 }
 for(auto x:adjv) if(__builtin_popcount(x)!=3)throw runtime_error("degree");
}
bool pd(uint32_t S){
 uint32_t O=S;
 for(int i=0;i<30;i++) if((S>>i)&1)O |=adjv[i];
 while(1){
  uint32_t add=0;
  for(int i=0;i<30;i++) if((O>>i)&1){
   uint32_t un=adjv[i]&~O;
   if(__builtin_popcount(un)==1)add|=un;
  }
  if(add==0)break;
  O |=add;
 }
 return O==V;
}
vector<uint32_t> configs;
unordered_map<uint32_t,int> indexx;
void enumerate(){
 long fail3=0;
 for(int k=1;k<=4;k++){
  int count=0;
  for(int a=0;a<30;a++)for(int b=a+1;b<30;b++){
   if(k==1)continue;
   if(k==2){if(pd((1u<<a)|(1u<<b)))count++;continue;}
   for(int c=b+1;c<30;c++){
    uint32_t m=(1u<<a)|(1u<<b)|(1u<<c);
    if(k==3){if(pd(m))count++;continue;}
    for(int d=c+1;d<30;d++){
     auto s=m|(1u<<d);if(pd(s)){count++;configs.push_back(s);}
    }
   }
  }
  if(k==1){for(int a=0;a<30;a++)count+=pd(1u<<a);}
  cout<<"successful_size_"<<k<<"="<<count<<"\n";
  if(k<=3 && count)throw runtime_error("bad minimum");
 }
 if(configs.size()!=6540)throw runtime_error("4-set census");
 for(int i=0;i<(int)configs.size();i++)indexx[configs[i]]=i;
}
vector<vector<int>> graph(bool sliding){
 vector<vector<int>> A(configs.size());
 for(int i=0;i<(int)configs.size();i++){
  uint32_t s=configs[i];
  for(int u=0;u<30;u++)if((s>>u)&1){
   auto destinations=sliding ? adjv[u] : (V&~s);
   for(int v=0;v<30;v++)if((destinations>>v)&1 && !((s>>v)&1)){
    uint32_t t=(s^(1u<<u))|(1u<<v);
    auto it=indexx.find(t);if(it!=indexx.end())A[i].push_back(it->second);
   }
  }
  sort(A[i].begin(),A[i].end());A[i].erase(unique(A[i].begin(),A[i].end()),A[i].end());
 }
 for(int i=0;i<(int)A.size();i++)for(int j:A[i]){
  if(!binary_search(A[j].begin(),A[j].end(),i))throw runtime_error("asymmetric move");
 }
 return A;
}
void summarize(const vector<vector<int>>& A,const string&name){
 map<int,long long> degrees,ec,dist_hist;
 long long arcs=0;int count=A.size();
 for(auto &a:A){degrees[a.size()]++;arcs+=a.size();}
 for(int root=0;root<count;root++){
  vector<int> dist(count,-1);dist[root]=0;
  vector<int> q(count);int head=0,tail=0;q[tail++]=root;
  while(head<tail){int u=q[head++];for(int v:A[u])if(dist[v]<0){dist[v]=dist[u]+1;q[tail++]=v;}}
  if(tail!=count)throw runtime_error("disconnected");
  int ecc=0;
  for(int j=0;j<count;j++){
   ecc=max(ecc,dist[j]); if(j>root)dist_hist[dist[j]]++;
  }
  ec[ecc]++;
 }
 cout<<name<<"_edges="<<arcs/2<<"\n";
 cout<<name<<"_degrees=";for(auto [k,v]:degrees)cout<<k<<":"<<v<<" ";cout<<"\n";
 cout<<name<<"_eccentricities=";for(auto [k,v]:ec)cout<<k<<":"<<v<<" ";cout<<"\n";
 cout<<name<<"_distance_pairs=";for(auto [k,v]:dist_hist)cout<<k<<":"<<v<<" ";cout<<"\n";
}

vector<int> distances(const vector<vector<int>>& A,int root){
 int n=A.size();vector<int> dist(n,-1),Q(n);int head=0,tail=0;
 dist[root]=0;Q[tail++]=root;
 while(head<tail){int u=Q[head++];for(int v:A[u])if(dist[v]<0){dist[v]=dist[u]+1;Q[tail++]=v;}}
 if(tail!=n)throw runtime_error("disconnected during locality census");
 return dist;
}
void locality(const vector<vector<int>>& J,const vector<vector<int>>& S){
 map<int,long long> extra;
 long long total=0;
 for(int i=0;i<(int)J.size();i++){
  auto dj=distances(J,i),ds=distances(S,i);
  for(int j=i+1;j<(int)J.size();j++){
   if(ds[j]<dj[j])throw runtime_error("slide shorter than jump");
   extra[ds[j]-dj[j]]++;total++;
  }
 }
 if(total!=6540LL*6539/2)throw runtime_error("incorrect pair count");
 cout<<"locality_excess_pairs=";
 for(auto [k,v]:extra)cout<<k<<":"<<v<<" ";cout<<"\n";
}
int main(){build();enumerate();auto J=graph(false),S=graph(true);summarize(J,"jump");summarize(S,"slide");locality(J,S);}

