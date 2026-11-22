#include <bits/stdc++.h>
using namespace std;
static const int N=14, SZ=4782969;
int ne[N][4]; int pw[N+1];
inline int step(int x) {
 int c[N], y=0; for(int i=0;i<N;i++){c[i]=x%3; x/=3;}
 for(int i=0;i<N;i++){
  int v=c[i]; int nv=v? (v==1?2:0) : ((c[ne[i][0]]==1)+(c[ne[i][1]]==1)+(c[ne[i][2]]==1)+(c[ne[i][3]]==1)>=2?1:0);
  y+=nv*pw[i];
 } return y;
}
int main(){
 ios::sync_with_stdio(false);
 
 vector<vector<int>> adj(N);
 for(int k=0;k<7;k++)for(int d:{2,4,5,6}) {int p=(k+d)%7, l=k+7; adj[p].push_back(l); adj[l].push_back(p);}
 for(int v=0;v<N;v++){if(adj[v].size()!=4) abort(); for(int j=0;j<4;j++)ne[v][j]=adj[v][j];}
 pw[0]=1;for(int i=1;i<=N;i++) pw[i]=pw[i-1]*3;
 vector<int> nxt(SZ); vector<uint32_t> deg(SZ); auto t0=chrono::steady_clock::now();
 for(int x=0;x<SZ;x++){int y=step(x);nxt[x]=y;deg[y]++;}
 deque<int> q; for(int i=0;i<SZ;i++)if(!deg[i])q.push_back(i);
 vector<int> order;order.reserve(SZ); while(!q.empty()){int u=q.front();q.pop_front(); order.push_back(u); int v=nxt[u];if(--deg[v]==0)q.push_back(v);}
 vector<uint8_t> dep(SZ,255),per(SZ,0);vector<int> comp(SZ,-1);map<int,int> cycles;
 int cid=0; vector<int> reps;
 for(int i=0;i<SZ;i++) if(deg[i]&& comp[i]==-1){int u=i, length=0;vector<int>cy;
  do{cy.push_back(u);comp[u]=cid;dep[u]=0;u=nxt[u];length++;}while(u!=i);
  cycles[length]++; for(int j:cy)per[j]=length;
  reps.push_back(i);cid++;
 }
 for(int j=(int)order.size()-1;j>=0;j--){int u=order[j],v=nxt[u];dep[u]=dep[v]+1;per[u]=per[v];comp[u]=comp[v];}
 vector<long long> basinCount(cid);map<pair<int,int>,long long> hist;
 for(int i=0;i<SZ;i++){if(comp[i]<0 || per[i]==0||dep[i]==255){cerr<<"ERROR "<<i<<endl;return 1;}basinCount[comp[i]]++;hist[{dep[i],per[i]}]++;}
 map<pair<int,long long>,int> bc;for(int id=0;id<cid;id++)bc[{per[reps[id]],basinCount[id]}]++;
 cerr<<"seconds "<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<endl;
 cout<<"GRAPH ";for(int i=0;i<N;i++){cout<<i<<":";for(auto v:adj[i])cout<<v<<",";cout<<" ";}cout<<"\n";
 cout<<"CYCLES ";for(auto [p,n]:cycles)cout<<p<<":"<<n<<" ";cout<<"\n";
 cout<<"HIST ";for(auto [a,n]:hist)cout<<a.first<<","<<a.second<<":"<<n<<" ";cout<<"\n";
 cout<<"BASINS ";for(auto [a,n]:bc)cout<<a.first<<","<<a.second<<":"<<n<<" ";cout<<"\n";
 cout<<"REP ";for(int i=0;i<min(30,cid);i++)cout<<i<<":"<<reps[i]<<":"<<int(per[reps[i]])<<":"<<basinCount[i]<<" ";cout<<"\n";
}
