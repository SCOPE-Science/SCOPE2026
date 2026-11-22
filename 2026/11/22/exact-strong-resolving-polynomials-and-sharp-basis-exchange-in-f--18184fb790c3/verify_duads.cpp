// Independent finite check using K_6 duads and synthemes (the doily GQ(2,2)).
#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<pair<int,int>> duads;
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)duads.push_back({i,j});
 vector<array<int,3>> synthemes;
 for(int a=0;a<15;a++)for(int b=a+1;b<15;b++)for(int c=b+1;c<15;c++){
  set<int> v={duads[a].first,duads[a].second,duads[b].first,duads[b].second,
              duads[c].first,duads[c].second};
  if(v.size()==6)synthemes.push_back({a,b,c});
 }
 assert(synthemes.size()==15);
 const int N=30;
 vector<vector<int>> adj(N);
 vector<array<int,3>> linepts=synthemes;
 vector<vector<int>> pencil(15);
 for(int j=0;j<15;j++)for(int a:synthemes[j]){
  adj[a].push_back(15+j);adj[15+j].push_back(a);pencil[a].push_back(j);
 }
 vector<vector<int>> d(N,vector<int>(N,99));
 for(int a=0;a<N;a++){
  queue<int>q;q.push(a);d[a][a]=0;
  while(!q.empty()){
    int v=q.front();q.pop();
    for(int w:adj[v])if(d[a][w]==99){d[a][w]=d[a][v]+1;q.push(w);}
  }
  assert(*max_element(d[a].begin(),d[a].end())==4);
 }
 bool mm[N][N]={};int M=0;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){
  bool ok=true;
  for(int w:adj[a])if(d[w][b]>d[a][b])ok=false;
  for(int w:adj[b])if(d[a][w]>d[a][b])ok=false;
  mm[a][b]=mm[b][a]=ok;
  bool expected=(a<15)==(b<15)&&d[a][b]==4;
  assert(ok==expected);
  M+=ok;
 }
 assert(M==120);
 int opt=0;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)
 for(int e=c+1;e<N;e++)for(int f=e+1;f<N;f++)for(int g=f+1;g<N;g++){
  int idx[]={a,b,c,e,f,g};bool ok=true;
  for(int u=0;u<6;u++)for(int v=u+1;v<6;v++)if(mm[idx[u]][idx[v]])ok=false;
  if(ok)opt++;
 }
 assert(opt==225);
 vector<pair<int,int>> bases;
 for(int j=0;j<15;j++)for(int i=0;i<15;i++)bases.push_back({j,i});
 vector<vector<int>> swapgraph(225);
 long long edges=0;
 for(int a=0;a<225;a++)for(int b=a+1;b<225;b++){
  auto [ja,ia]=bases[a];auto [jb,ib]=bases[b];
  int overlap=0;
  for(int x:linepts[ja])for(int y:linepts[jb])overlap+=(x==y);
  for(int x:pencil[ia])for(int y:pencil[ib])overlap+=(x==y);
  int change=6-overlap;
  if(change<=2){swapgraph[a].push_back(b);swapgraph[b].push_back(a);edges++;}
 }
 assert(edges==1350);
 int diameter=0;
 for(int a=0;a<225;a++){
  vector<int>dist(225,-1);dist[a]=0;queue<int>q;q.push(a);
  while(!q.empty()){
   int v=q.front();q.pop();
   for(int w:swapgraph[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}
  }
  assert(*min_element(dist.begin(),dist.end())>=0);
  diameter=max(diameter,*max_element(dist.begin(),dist.end()));
 }
 assert(diameter==4);
 cout<<"W(3,2) independent duad-syntheme construction: points 15, lines 15, MMD edges "
     <<M<<", six-vertex omitted independent sets "<<opt<<", swap edges "<<edges
     <<", diameter "<<diameter<<". ALL CHECKS PASS\n";
}
