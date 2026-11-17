#include <bits/stdc++.h>
using namespace std;
const int V=14;
int pw[V+1];
int nb[V][3];
const int lines[7][3]={{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}};
int transform(int state,int mode){
 int s[V],out=0;for(int i=0;i<V;i++)s[i]=(state/pw[i])%3;
 for(int i=0;i<V;i++){
   int x=s[i];int y=x;
   if(mode==0){int target=(x+1)%3;for(int j=0;j<3;j++)if(s[nb[i][j]]==target){y=target;break;}}
   else if(x==1)y=2;else if(x==2)y=0;else for(int j=0;j<3;j++)if(s[nb[i][j]]==1){y=1;break;}
   out+=pw[i]*y;
 }
 return out;
}
struct Census{vector<uint8_t>period,depth;map<pair<int,int>,long long> cnt; int maxdepth=0;};
Census census(int mode){
 int N=pw[V];vector<int> to(N),indeg(N); 
 for(int i=0;i<N;i++){int o=transform(i,mode);to[i]=o;indeg[o]++;}
 deque<int> q;vector<int> order;order.reserve(N);
 for(int i=0;i<N;i++)if(!indeg[i])q.push_back(i);
 while(!q.empty()) {int v=q.front();q.pop_front();order.push_back(v);int u=to[v];if(!--indeg[u])q.push_back(u);}
 Census c;c.period.assign(N,0);c.depth.assign(N,0);
 for(int i=0;i<N;i++)if(indeg[i] && !c.period[i]) {
 int u=i,len=0; do{len++;u=to[u];}while(u!=i);
 if(len<1 || len>255)throw runtime_error("cycle length exceeds checked representation");
 u=i;do{c.period[u]=len;u=to[u];}while(u!=i);
 }
 for(auto it=order.rbegin();it!=order.rend();it++){
 int i=*it,u=to[i]; c.period[i]=c.period[u];if(c.depth[u]==255)throw runtime_error("depth exceeds checked representation");c.depth[i]=c.depth[u]+1;
 }
 for(int i=0;i<N;i++){c.cnt[{c.period[i],c.depth[i]}]++;c.maxdepth=max<int>(c.maxdepth,c.depth[i]);}
 cerr << "mode="<<mode<<" cycles="<<N-order.size()<<" maxdepth="<<c.maxdepth<<"\n";
 return c;
}
int main(){
 pw[0]=1;for(int i=1;i<=V;i++)pw[i]=pw[i-1]*3;
 for(int i=0;i<7;i++)for(int j=0;j<3;j++)nb[i][j]=-1;
 int deg[V]={};
 for(int l=0;l<7;l++)for(int j=0;j<3;j++){int p=lines[l][j];nb[p][deg[p]++]=7+l;nb[7+l][deg[7+l]++]=p;}
 for(int i=0;i<14;i++)if(deg[i]!=3)throw runtime_error("degree!");
 auto a=census(0), b=census(1);
 map<pair<int,int>,long long> joint;map<tuple<int,int,int,int>,long long> d4;
 long long diff=0;
 for(int i=0;i<pw[V];i++){
  joint[{a.period[i],b.period[i]}]++;
  if(a.period[i]!=b.period[i]){diff++;d4[{a.period[i],b.period[i],a.depth[i],b.depth[i]}]++;}
 }
 cout<<"N "<<pw[V]<<" mismatch "<<diff<<"\n";
 cout<<"JOINT\n";for(auto [k,v]:joint)cout<<k.first<<" "<<k.second<<" "<<v<<"\n";
 cout<<"CCA classes\n";for(auto [k,v]:a.cnt)cout<<k.first<<":"<<k.second<<" "<<v<<"\n";
 cout<<"GHM classes\n";for(auto [k,v]:b.cnt)cout<<k.first<<":"<<k.second<<" "<<v<<"\n";
 cout<<"Discrepancy shells\n";for(auto [k,v]:d4) {auto [p1,p2,d1,d2]=k;cout<<p1<<" "<<p2<<" "<<d1<<" "<<d2<<" "<<v<<"\n";}
}
