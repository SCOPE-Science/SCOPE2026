#include <bits/stdc++.h>
using namespace std;
const int NN=10,S=1<<20;
array<array<int,3>,NN> adj(int k) {
 array<array<int,3>,NN> A{};vector<vector<int>> vv(NN);
 auto add=[&](int x,int y){vv[x].push_back(y);vv[y].push_back(x);};
 for(int i=0;i<5;i++){add(i,(i+1)%5);add(i,i+5);add(i+5,5+(i+k)%5);}
 for(int i=0;i<NN;i++){sort(vv[i].begin(),vv[i].end());if(vv[i].size()!=3){cerr<<"bad deg";exit(1);}for(int j=0;j<3;j++) A[i][j]=vv[i][j];}
 return A;
}
inline int step(int x,const array<array<int,3>,NN>& A,int mode){
 int y=0;
 for(int i=0;i<NN;i++){
  int c=(x>>(2*i))&3, v;
  if(mode==0){int succ=(c+1)&3;v=(((x>>(2*A[i][0]))&3)==succ||((x>>(2*A[i][1]))&3)==succ||((x>>(2*A[i][2]))&3)==succ)?succ:c;}
  else if(c!=0)v=(c+1)&3;
  else v=((((x>>(2*A[i][0]))&3)==1)||(((x>>(2*A[i][1]))&3)==1)||(((x>>(2*A[i][2]))&3)==1))?1:0;
  y|=v<<(2*i);
 }
 return y;
}
struct Data {vector<uint8_t> per,depth;vector<int> next; map<int,long long> bp;map<pair<int,int>,long long> td; int maxdepth=0;};
Data classify(int k,int mode){
 Data z;z.per.assign(S,0);z.depth.assign(S,0);z.next.resize(S);auto A=adj(k);
 for(int i=0;i<S;i++)z.next[i]=step(i,A,mode);
 vector<uint8_t> vis(S,0); vector<int> idx(S,-1);vector<int> path;
 for(int s=0;s<S;s++){
  if(vis[s])continue;
  int u=s;path.clear();
  while(!vis[u]){vis[u]=1;idx[u]=path.size();path.push_back(u);u=z.next[u];}
  int cycstart=idx[u];
  if(cycstart>=0){int p=path.size()-cycstart;for(int j=cycstart;j<(int)path.size();j++){int v=path[j];z.per[v]=p;z.depth[v]=0;}}
  for(int j=min((int)path.size(),(cycstart>=0?cycstart:(int)path.size()))-1;j>=0;j--){int v=path[j],w=z.next[v];z.per[v]=z.per[w];z.depth[v]=z.depth[w]+1;}
  for(int v:path){idx[v]=-1;}
 }
 for(int i=0;i<S;i++){
  z.bp[z.per[i]]++;
  z.td[{z.depth[i],z.per[i]}]++;
  z.maxdepth=max(z.maxdepth,(int)z.depth[i]);
 }
 return z;
}
int main(){
 for(int k:{1,2}){
  auto a=classify(k,0),b=classify(k,1);cout<<"GP(5,"<<k<<")\nCCA per:";for(auto [p,c]:a.bp)cout<<" "<<p<<":"<<c;cout<<" depth "<<a.maxdepth<<"\nGHM per:";for(auto [p,c]:b.bp)cout<<" "<<p<<":"<<c;cout<<" depth "<<b.maxdepth<<"\n";
  map<pair<int,int>,long long> joint;map<pair<int,int>,int> witnesses;map<int,long long> different;long long mismatches=0;int max_ratio=0;
  for(int i=0;i<S;i++){auto key=make_pair((int)a.per[i],(int)b.per[i]);joint[key]++;if(!witnesses.count(key))witnesses[key]=i;if(a.per[i]!=b.per[i]){mismatches++;different[(int)a.per[i]*100+b.per[i]]++;}}
  cout<<"Joint periods";for(auto [p,c]:joint)cout<<" ("<<p.first<<","<<p.second<<")="<<c;cout<<"\nperiod mismatch "<<mismatches<<"\n";cout<<"witnesses:";for(auto [pair,state]:witnesses)cout<<" ("<<pair.first<<","<<pair.second<<")="<<state;cout<<"\n";
  cout<<"CCA td:";for(auto [p,c]:a.td)cout<<" ("<<p.first<<","<<p.second<<")="<<c;cout<<"\nGHM td:";for(auto [p,c]:b.td)cout<<" ("<<p.first<<","<<p.second<<")="<<c;cout<<"\n";
 }
}
