// Independent finite verification of the star-first isometry certificate.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using G = vector<vector<int>>;
static vector<vector<int>> dist(const G& adj,const vector<int>& vs){
 int n=adj.size(); vector<vector<int>> out(n,vector<int>(n,1000000));
 for(int s:vs){queue<int> q;out[s][s]=0;q.push(s);
  while(!q.empty()){int x=q.front();q.pop();for(int y:vs) if(adj[x][y] && out[s][y]>out[s][x]+1){out[s][y]=out[s][x]+1;q.push(y);}}
 }
 return out;
}
static bool cert(const G& g,int v){int n=g.size();
 for(int x=0;x<n;x++)for(int y=x+1;y<n;y++)if(!g[x][y]){
  bool ok=false;
  for(int z=0;z<n;z++)if(z!=x && z!=y && (z==v || g[v][z]) && g[x][z] && g[y][z]){ok=true;break;}
  if(!ok)return false;
 }
 return true;
}
static bool verify(const G& g,int v,bool rev1,bool rev2){
 int n=g.size();vector<int> a{v},b;
 for(int x=0;x<n;x++)if(x!=v){if(g[v][x])a.push_back(x);else b.push_back(x);}
 if(rev1)reverse(a.begin()+1,a.end());
 if(rev2)reverse(b.begin(),b.end());
 a.insert(a.end(),b.begin(),b.end());
 vector<int> all(n);for(int i=0;i<n;i++)all[i]=i;
 auto original=dist(g,all);
 for(int k=1;k<=n;k++){
  vector<int> chosen(a.begin(),a.begin()+k);
  auto local=dist(g,chosen);
  for(int x:chosen)for(int y:chosen)if(local[x][y]!=original[x][y])return false;
 }
 return true;
}
int main(){
 uint64_t count=0,checked=0;
 for(int n=1;n<=6;n++){
  int m=n*(n-1)/2;
  uint64_t cases=1ULL<<m;
  for(uint64_t mask=0;mask<cases;mask++){
   G g(n,vector<int>(n,0));int id=0;
   for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,id++)if((mask>>id)&1){g[i][j]=g[j][i]=1;}
   for(int v=0;v<n;v++)if(cert(g,v)){
    checked++;
    for(int r=0;r<4;r++)if(!verify(g,v,r&1,r&2)){
     cerr<<"Counterexample n="<<n<<" mask="<<mask<<" center="<<v<<"\n";return 1;
    }
   }
   count++;
  }
 }
 cout<<"PASS all "<<count<<" labeled graphs of order at most six; "<<checked
     <<" certified (graph, center) pairs; four star-first orders per pair.\n";
}
