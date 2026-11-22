#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
 for(int n=7;n<=10;++n){
  int v=2*n;vector<vector<int>> g(v); vector<pair<int,int>> e;
  auto edge=[&](int a,int b){g[a].push_back(b);g[b].push_back(a);e.push_back({a,b});};
  for(int i=0;i<n;++i){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+3)%n);}
  vector<vector<int>> D(v,vector<int>(v,999));
  for(int s=0;s<v;s++){queue<int> q;q.push(s);D[s][s]=0;while(!q.empty()){int a=q.front();q.pop();for(int b:g[a])if(D[s][b]==999)D[s][b]=D[s][a]+1,q.push(b);}}
  vector<vector<int>> dist(v,vector<int>(e.size()));
  for(int i=0;i<v;i++)for(int j=0;j<(int)e.size();j++)dist[i][j]=min(D[i][e[j].first],D[i][e[j].second]);
  for(int k=2;k<=4;k++){
   long long cnt=0; vector<int> witness, a(k);
   auto recur=[&](auto&& recur,int start,int pos)->void{
    if(pos==k){bool ok=true;for(int j=0;j<(int)e.size();j++){
      for(int z=0;z<j;z++){
       bool eq=true;for(int i:a)if(dist[i][j]!=dist[i][z]){eq=false;break;}
       if(eq){ok=false;break;}
      } if(!ok)break;
     }
     if(ok){cnt++;if(witness.empty())witness=a;}return;
    }
    for(int i=start;i<=v-(k-pos);i++){a[pos]=i;recur(recur,i+1,pos+1);}
   };recur(recur,0,0);
   cout<<n<<" "<<k<<" "<<cnt;
   if(!witness.empty()){cout<<" witness";for(int i:witness)cout<<" "<<i;}
   cout<<"\n";
  }
 }
}
