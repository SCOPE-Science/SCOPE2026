// Independent exhaustive certificate using an LCF/Hamiltonian representation.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_hamilton.cpp -o check && ./check
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cassert>
using namespace std;
const int n=14,full=(1<<14)-1;
int adj[n]{};
void add(int a,int b){adj[a]|=1<<b;adj[b]|=1<<a;}
int pop(int x){return __builtin_popcount((unsigned)x);}
bool conn(int m){if(!m)return false;int seen=m&-m;while(true){int next=seen;for(int i=0;i<n;i++)if(seen&(1<<i))next|=adj[i]&m;if(next==seen)break;seen=next;}return seen==m;}
int edgecount(int m){int twice=0;for(int i=0;i<n;i++)if(m&(1<<i))twice+=pop(adj[i]&m);return twice/2;}
bool forest(int m){int seen=0,components=0;for(int i=0;i<n;i++)if((m&(1<<i))&&!(seen&(1<<i))){components++;int reach=(1<<i);while(true){int next=reach;for(int j=0;j<n;j++)if(reach&(1<<j))next|=adj[j]&m;if(reach==next)break;reach=next;}seen|=reach;}return edgecount(m)==pop(m)-components;}
int main(){
 for(int i=0;i<n;i++)add(i,(i+1)%n);
 for(int i=0;i<n;i+=2)add(i,(i+5)%n);
 for(int i=0;i<n;i++)assert(pop(adj[i])==3);
 int plain4=0;vector<int>opt;vector<char>valid(full+1,false);
 for(int m=0;m<=full;m++){
  if(pop(m)<4)assert(!forest(full^m));
  if(pop(m)==4&&forest(full^m))plain4++;
  if(pop(m)<7)assert(!(conn(m)&&forest(full^m)));
  if(pop(m)==7&&conn(m)&&forest(full^m)){
   assert(edgecount(m)==6&&edgecount(full^m)==6&&conn(full^m));
   valid[m]=true;opt.push_back(m);
  }
 }
 assert(plain4==70&&opt.size()==770);
 vector<vector<int>>edges(full+1); map<int,int>deg;
 long long total=0;
 for(int s:opt){
  assert(valid[full^s]);
  for(int a=0;a<n;a++)if(s&(1<<a))for(int b=0;b<n;b++)if(!(s&(1<<b))){int t=s^(1<<a)^(1<<b);if(valid[t])edges[s].push_back(t);}
  deg[(int)edges[s].size()]++;total+=edges[s].size();
 }
 assert(total==13776);
 assert((deg==map<int,int>{{16,378},{18,56},{20,336}}));
 map<int,long long>distances,exc;map<int,int>ecc;
 long long reached=0;
 for(int s:opt){
  vector<int>dist(full+1,-1);queue<int>q;q.push(s);dist[s]=0;int maximum=0,count=0;
  while(!q.empty()){int a=q.front();q.pop();count++;maximum=max(maximum,dist[a]);for(int b:edges[a])if(dist[b]<0){dist[b]=dist[a]+1;q.push(b);}}
  assert(count==770);ecc[maximum]++;
  for(int t:opt)if(t>s){int d=dist[t],j=7-pop(s&t);assert(d==j||d==j+1);distances[d]++;exc[d-j]++;reached++;}
 }
 assert(reached==770LL*769/2);
 assert((ecc==map<int,int>{{7,770}}));
 assert((exc==map<int,long long>{{0,290605},{1,5460}}));
 cout<<"Hamiltonian verifier: PASS\n";
 cout<<"unrestricted FVS size=4 count="<<plain4<<"; connected FVS size=7 count="<<opt.size()<<"\n";
 cout<<"one-vertex exchange edges="<<total/2<<" degree spectrum:";
 for(auto [k,v]:deg)cout<<" ("<<k<<":"<<v<<")";cout<<"\n";
 cout<<"distance spectrum:";for(auto [k,v]:distances)cout<<" ("<<k<<":"<<v<<")";cout<<"\n";
 cout<<"eccentricity spectrum:";for(auto [k,v]:ecc)cout<<" ("<<k<<":"<<v<<")";cout<<"\n";
 cout<<"extra move pairs="<<exc[1]<<"\n";
}
