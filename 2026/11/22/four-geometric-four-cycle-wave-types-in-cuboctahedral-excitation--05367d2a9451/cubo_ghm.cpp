#include<bits/stdc++.h>
using namespace std;
int main(){
 const int N=12,S=531441; int p3[N+1];p3[0]=1;for(int i=1;i<=N;i++)p3[i]=3*p3[i-1];
 vector<pair<int,int>> E;for(int x=0;x<8;x++)for(int bit=0;bit<3;bit++){int y=x^(1<<bit);if(x<y)E.push_back({x,y});}
 assert(E.size()==12);
 vector<vector<int>> adj(N);for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){auto [a,b]=E[i]; auto[c,d]=E[j];if(a==c||a==d||b==c||b==d)adj[i].push_back(j);}
 for(auto a:adj)assert(a.size()==4);
 vector<int> next(S);
 for(int s=0;s<S;s++){
    int d[N]; int z=s;for(int i=0;i<N;i++){d[i]=z%3;z/=3;}
    int out=0;for(int i=0;i<N;i++){
      int nd= d[i]==1?2:d[i]==2?0:0;
      if(d[i]==0){for(int j:adj[i])if(d[j]==1){nd=1;break;}}
      out+=p3[i]*nd;
    }
    next[s]=out;
 }
 vector<int> indeg(S);for(int s=0;s<S;s++)indeg[next[s]]++;
 vector<int> queue;queue.reserve(S);for(int s=0;s<S;s++)if(indeg[s]==0)queue.push_back(s);
 for(size_t h=0;h<queue.size();h++){int t=next[queue[h]];if(--indeg[t]==0)queue.push_back(t);}
 vector<int> dist(S,-1),period(S,0),basin(S,0); map<int,int> cycstates,cycorbits, min_dist_count, exactentryperiod;
 int maxd=0;
 for(int s=0;s<S;s++)if(indeg[s]>0&&dist[s]<0){
 int t=s,cyc=0;do{cyc++;t=next[t];}while(t!=s);
 t=s;do{dist[t]=0;period[t]=cyc;cycstates[cyc]++;t=next[t];}while(t!=s);
 cycorbits[cyc]++;
 }
 for(int h=(int)queue.size()-1;h>=0;h--){int s=queue[h],t=next[s];dist[s]=dist[t]+1;period[s]=period[t];maxd=max(maxd,dist[s]);}
 map<pair<int,int>,int> by;for(int s=0;s<S;s++)by[{dist[s],period[s]}]++;
 cout<<"GRAPH_EDGES ";for(auto e:E)cout<<"("<<e.first<<","<<e.second<<") ";cout<<"\n";
 cout<<"CYCLE_STATES ";for(auto [k,v]:cycstates)cout<<k<<":"<<v<<" ";cout<<"\nCYCLE_ORBITS ";for(auto [k,v]:cycorbits)cout<<k<<":"<<v<<" ";cout<<"\nMAX_TRANSIENT "<<maxd<<"\n";
 cout<<"ENTRY_PERIOD\n";for(auto [k,v]:by)cout<<k.first<<" "<<k.second<<" "<<v<<"\n";
 return 0;
}
