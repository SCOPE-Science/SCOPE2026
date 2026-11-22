#include <bits/stdc++.h>
using namespace std;
int N=24; vector<int> adj[24]; int col[24];
long long nodes=0,sol=0; vector<vector<int>> sols;
int getmask(int v,int k){
 int mask=(1<<k)-1;
 for(int u:adj[v])if(col[u]>=0)mask&=~(1<<col[u]);
 // For each neighbor w of v, the other two neighbors of w restrict v.
 for(int w:adj[v]){
  int a=-1,b=-1;
  for(int u:adj[w])if(u!=v && col[u]>=0){if(a<0)a=col[u];else b=col[u];}
  if(b>=0){
   if(a==b)mask&=(1<<a);
   else mask&=~((1<<a)|(1<<b));
  }
 }
 return mask;
}
void dfs(int filled,int k,int maxc){
 nodes++;
 if(filled==N){sol++;sols.emplace_back(col,col+N); return;}
 // dynamic MRV, with new color allowed up to maxc+1
 int opts=(1<<min(maxc+2,k))-1;
 int bv=-1,bmask=-1,bb=999,bscore=-1;
 for(int v=0;v<N;v++)if(col[v]<0){
  int mask=getmask(v,k)&opts;
  int count=__builtin_popcount((unsigned)mask);if(count==0)return;
  int score=0;
  for(int u:adj[v])if(col[u]>=0)score+=4;
  for(int u:adj[v]){int s=0;for(int a:adj[u])if(a!=v&&col[a]>=0)s++;score+=s*s;}
  if(count<bb || (count==bb&&score>bscore)) {bb=count;bscore=score;bv=v;bmask=mask;}
 }
 for(int c=0;c<k;c++)if((bmask>>c)&1){
  col[bv]=c;
  dfs(filled+1,k,max(maxc,c));
  col[bv]=-1;
 }
}
int main(int argc,char**argv){
 int lcf[]={12,7,-7};
 set<pair<int,int>> es;
 for(int i=0;i<N;i++){
  es.insert(minmax(i,(i+1)%N));
  int v=(i+lcf[i%3]+N)%N;
  es.insert(minmax(i,v));
 }
 for(auto [u,v]:es){adj[u].push_back(v);adj[v].push_back(u);}
 cout << "edges "<<es.size()<<" degree ";for(int i=0;i<N;i++)cout<<adj[i].size()<<',';cout<<endl;
 int k=argc>1?atoi(argv[1]):4;
 fill(col,col+N,-1);
 col[0]=0;dfs(1,k,0);
 cerr<<"nodes="<<nodes<<" canonical="<<sol<<" k="<<k<<endl;
 ofstream f("search_colorings_"+to_string(k)+".txt");for(auto& s:sols){for(int x:s)f<<x;f<<'\n';}
}
