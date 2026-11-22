#include <bits/stdc++.h>
using namespace std;
using Perm=array<uint8_t,56>;
using Sept=array<uint8_t,7>;
struct HashP {size_t operator()(const Perm& p) const noexcept {uint64_t h=1469598103934665603ull;for(auto x:p){h^=x;h*=1099511628211ull;}return h;}};
struct HashS {size_t operator()(const Sept& p) const noexcept {uint64_t h=1469598103934665603ull;for(auto x:p){h^=x;h*=1099511628211ull;}return h;}};
int main(){
 ifstream in("markings.txt");if(!in){cerr<<"missing markings.txt\n";return 2;}
 vector<Perm> gens(7);for(auto&g:gens)for(int i=0;i<56;i++){int v;if(!(in>>v)||v<0||v>=56)return 3;g[i]=v;}
 vector<Sept> marks(576);unordered_map<Sept,int,HashS> loc;loc.reserve(600);
 for(int m=0;m<576;m++){for(int j=0;j<7;j++){int v;if(!(in>>v)||v<0||v>=56)return 4;marks[m][j]=v;}loc.emplace(marks[m],m);}
 if(loc.size()!=576)return 5;
 Perm e; iota(e.begin(),e.end(),0);
 for(auto &g:gens)for(int i=0;i<56;i++)if(g[g[i]]!=i){cerr<<"generator not involution\n";return 6;}
 unordered_map<Perm,uint32_t,HashP> idx;idx.max_load_factor(.75);idx.reserve(3000000);
 vector<Perm> group;group.reserve(3000000);idx.emplace(e,0);group.push_back(e);
 for(size_t i=0;i<group.size();i++){
   auto x=group[i];for(auto&g:gens){Perm y;for(int k=0;k<56;k++)y[k]=x[g[k]];
     auto [it,ins]=idx.emplace(y,(uint32_t)group.size());if(ins)group.push_back(y);}}
 if(group.size()!=2903040){cerr<<"wrong W(E7) size: "<<group.size()<<"\n";return 7;}
 vector<uint8_t> marked(group.size());vector<uint32_t> queue;queue.reserve(300000);
 map<int,uint64_t> totals;int nclasses=0;uint64_t sizesum=0;
 for(size_t i=0;i<group.size();i++)if(!marked[i]){
   queue.clear();queue.push_back(i);marked[i]=1;
   for(size_t j=0;j<queue.size();j++){
      Perm a=group[queue[j]];
      for(auto&g:gens){Perm y;for(int k=0;k<56;k++)y[k]=g[a[g[k]]];
        auto it=idx.find(y);if(it==idx.end()){cerr<<"bad conjugacy\n";return 8;}
        auto v=it->second;if(!marked[v]){marked[v]=1;queue.push_back(v);}}
   }
   const auto& g=group[i];array<uint16_t,576> p;
   for(int j=0;j<576;j++){
      Sept s;for(int k=0;k<7;k++)s[k]=g[marks[j][k]];sort(s.begin(),s.end());
      auto it=loc.find(s);if(it==loc.end()){cerr<<"marking not preserved\n";return 9;}p[j]=it->second;
   }
   uint8_t visited[576]={};int d=999;map<int,int> cycles;
   for(int j=0;j<576;j++)if(!visited[j]){int u=j,l=0;do{visited[u]=1;l++;u=p[u];}while(u!=j);d=min(d,l);cycles[l]++;}
   totals[d]+=queue.size();sizesum+=queue.size();nclasses++;
   cout<<"CLASS "<<nclasses<<" size="<<queue.size()<<" min="<<d<<" permutation=";
   for(auto v:g)cout<<(int)v<<",";
   cout<<" cycle_lengths=";for(auto [l,n]:cycles)cout<<l<<"^"<<n<<",";cout<<"\n";
 }
 cout<<"GROUP "<<group.size()<<" CLASSES "<<nclasses<<" SUM "<<sizesum<<"\n";
 for(auto [d,n]:totals)cout<<"MIN "<<d<<" ELEMENTS "<<n<<"\n";
 if(nclasses!=60||sizesum!=2903040)return 10;
}
