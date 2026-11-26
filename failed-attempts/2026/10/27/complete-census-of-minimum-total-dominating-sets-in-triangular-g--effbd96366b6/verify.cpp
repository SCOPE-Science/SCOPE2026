// Exhaustive independent verification of minimum total dominating sets of J(n,2).
// A Johnson vertex is represented by an edge of K_n.
#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
struct Edge {int u,v;};
int n,m; vector<Edge> E;vector<int> sel;vector<ull> typecount(5,0);ull total=0, visited=0;
int type_of(){
 vector<int> par(n);iota(par.begin(),par.end(),0);
 auto find=[&](int a){while(par[a]!=a){par[a]=par[par[a]];a=par[a];}return a;};
 for(int i:sel){auto [a,b]=E[i];int x=find(a),y=find(b);par[x]=y;}
 map<int,int> sizes;for(int i=0;i<n;i++)sizes[find(i)]++;
 int iso=0;vector<int> comp;
 for(auto [r,s]:sizes){if(s==1)iso++;else comp.push_back(s);}
 sort(comp.begin(),comp.end());
 bool all3=all_of(comp.begin(),comp.end(),[](int s){return s==3;});
 if(iso==0&&all3) return 0;
 if(iso==1&&all3) return 1;
 if(iso==1&&count(comp.begin(),comp.end(),4)==1&&all_of(comp.begin(),comp.end(),[](int s){return s==3||s==4;})) return 2;
 if(iso==1&&count(comp.begin(),comp.end(),5)==1&&all_of(comp.begin(),comp.end(),[](int s){return s==3||s==5;})) return 3;
 if(iso==1&&count(comp.begin(),comp.end(),4)==2&&all_of(comp.begin(),comp.end(),[](int s){return s==3||s==4;})) return 4;
 return -1;
}
void test(){
 visited++;int deg[20]={};ull mask=0;
 for(int i:sel){deg[E[i].u]++;deg[E[i].v]++;mask |= 1ULL<<i;}
 for(int i=0;i<(int)E.size();i++){
  auto [u,v]=E[i];
  int neighbors=deg[u]+deg[v]-2*((mask>>i)&1ULL);
  if(neighbors==0)return;
 }
 ++total;
 int kind=type_of();
 if(kind<0){cerr<<"UNCLASSIFIED witness n="<<n<<"\n";exit(2);}
 typecount[kind]++;
}
void rec(int next,int need){
 if(!need){test();return;}
 if((int)E.size()-next<need)return;
 for(int i=next;i<=(int)E.size()-need;i++){
  sel.push_back(i);rec(i+1,need-1);sel.pop_back();
 }
}
int main(){
 for(n=4;n<=10;n++){
  E.clear();for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)E.push_back({i,j});
  m=(2*(n-1)+2)/3;
  total=visited=0;fill(typecount.begin(),typecount.end(),0);
  rec(0,m);
  cout<<"n="<<n<<" m="<<m<<" tested="<<visited<<" total="<<total<<" shape_full_P3="<<typecount[0]<<" iso_P3="<<typecount[1]<<" iso_T4="<<typecount[2]<<" iso_T5="<<typecount[3]<<" iso_T4_T4="<<typecount[4]<<"\n";
 }
}
