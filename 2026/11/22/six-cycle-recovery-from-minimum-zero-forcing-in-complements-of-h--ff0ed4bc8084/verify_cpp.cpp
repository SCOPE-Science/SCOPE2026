// Independent C++17 finite tests for a complement zero-forcing enumerator.
// For each case exhaustively checks every set of 2, 3 and 4 initially white vertices.
#include <bits/stdc++.h>
using namespace std;
using Graph=vector<vector<int>>;
void add(Graph &g,int a,int b){assert(a!=b);g[a].push_back(b);g[b].push_back(a);}
Graph petersen(){
  Graph g(10);vector<int> v;for(int x=0;x<32;x++)if(__builtin_popcount((unsigned)x)==2)v.push_back(x);
  for(int i=0;i<10;i++)for(int j=i+1;j<10;j++)if(!(v[i]&v[j]))add(g,i,j);return g;
}
Graph heawood(){
  Graph g(14);for(int i=0;i<7;i++)for(int z:{0,1,3})add(g,i,7+(i+z)%7);return g;
}
Graph dodecahedron(){Graph g(20);for(int i=0;i<10;i++){add(g,i,(i+1)%10);add(g,i,10+i);add(g,10+i,10+(i+2)%10);}return g;}
Graph desargues(){Graph g(20);vector<int>a,b;for(int x=1;x<32;x++){int p=__builtin_popcount((unsigned)x);if(p==2)a.push_back(x);if(p==3)b.push_back(x);}
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)if((a[i]&b[j])==a[i])add(g,i,10+j);return g;}
Graph projective(){
 Graph g(26);vector<array<int,3>> x;for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++){
 if(!(a||b||c))continue;array<int,3> v={a,b,c},neg={(3-a)%3,(3-b)%3,(3-c)%3};
 if(find(x.begin(),x.end(),v)==x.end()&&find(x.begin(),x.end(),neg)==x.end())x.push_back(v);
 }
 assert(x.size()==13);
 for(int i=0;i<13;i++)for(int j=0;j<13;j++)if((x[i][0]*x[j][0]+x[i][1]*x[j][1]+x[i][2]*x[j][2])%3==0)add(g,i,13+j);return g;
}
Graph c8_chord(){Graph g(8);for(int i=0;i<8;i++)add(g,i,(i+1)%8);add(g,0,4);return g;}
Graph joined_cycles(){Graph g(11);for(int i=0;i<5;i++)add(g,i,(i+1)%5);for(int i=0;i<6;i++)add(g,5+i,5+(i+1)%6);add(g,0,5);return g;}
bool forces(const Graph &g,const vector<int>& initial){
 int n=g.size();vector<bool> white(n,0);for(int x:initial)white[x]=1;
 // synchronous rounds, unlike the independent Python checker
 for(int round=0;round<=n;round++){
  int rem=count(white.begin(),white.end(),true);if(!rem)return true;
  vector<int> move;
  for(int u=0;u<n;u++)if(!white[u]){
   int seen=0,target=-1;
   for(int v=0;v<n;v++)if(white[v]&&v!=u&&find(g[u].begin(),g[u].end(),v)==g[u].end()){target=v;seen++;}
   if(seen==1)move.push_back(target);
  }
  if(move.empty())return false;
  for(int v:move)white[v]=false;
 }
 return false;
}
long long six_cycles(const Graph&g){
 int n=g.size();long long count=0;vector<int>path;
 function<void(int)>dfs=[&](int u){
   if(path.size()==6){if(find(g[u].begin(),g[u].end(),path[0])!=g[u].end())count++;return;}
   for(int v:g[u])if(find(path.begin(),path.end(),v)==path.end()){path.push_back(v);dfs(v);path.pop_back();}
 };
 for(int i=0;i<n;i++){path={i};dfs(i);}assert(count%12==0);return count/12;
}
long long choose2(long long k){return k*(k-1)/2;}
void check(const Graph &g,const string&name){
 int n=g.size(),d=g[0].size();vector<set<int>> ns(n);for(int i=0;i<n;i++){assert(g[i].size()>=2);ns[i].insert(g[i].begin(),g[i].end());}
 for(int x=0;x<n;x++)for(int y=0;y<x;y++){
  int common=0;for(int z:ns[x])common+=ns[y].count(z);
  assert(common<=1);if(ns[x].count(y))assert(!common);
 }
 auto enumerate=[&](int k){
    long long total=0;vector<int>sel;
    function<void(int)> rec=[&](int from){
      if(sel.size()==(size_t)k){bool b=forces(g,sel);
       if(k==2)assert(b);if(k==4)assert(!b);
       if(k==3){bool structural=false;for(int v=0;v<n;v++)if(find(sel.begin(),sel.end(),v)==sel.end()){
        int m=0;for(int t:sel)m+=ns[v].count(t);if(m==2){structural=true;break;}}
        assert(b==structural);
       }
       total+=b;return;}
      for(int j=from;j<n;j++){sel.push_back(j);rec(j+1);sel.pop_back();}
    };
    rec(0);return total;
 };
 long long low=enumerate(2), mid=enumerate(3), high=enumerate(4);
 long long six=six_cycles(g),pairs2=0,wedges=0;
 for(int i=0;i<n;i++){pairs2+=choose2(g[i].size());int two=0;for(int v=0;v<n;v++)if(v!=i&&!ns[i].count(v)){int common=0;for(int w:ns[i])common+=ns[v].count(w);if(common)two++;}wedges+=choose2(two);}
 long long predicted=(n-3)*pairs2-wedges+2*six;
 assert(mid==predicted);assert(low==choose2(n));assert(high==0);
 cout<<name<<" n="<<n<<" degree_first="<<d<<" six="<<six<<" good3="<<mid<<" count_formula="<<predicted<<" PASS\n";
}
int main(){check(petersen(),"Petersen");check(heawood(),"Heawood");check(dodecahedron(),"Dodecahedron");check(desargues(),"Desargues");check(projective(),"PG3_incidence");check(c8_chord(),"C8_chord");check(joined_cycles(),"C5_C6_bridge");}
