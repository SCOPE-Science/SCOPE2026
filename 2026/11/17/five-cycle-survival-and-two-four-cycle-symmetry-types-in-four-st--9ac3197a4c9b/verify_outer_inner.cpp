// Independent outer-cycle, spoke, and inner-star implementation.
#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int q=argc>1?atoi(argv[1]):4;int th=argc>2?atoi(argv[2]):1;
 int N=10;vector<pair<int,int>> es;for(int i=0;i<5;i++){es.push_back({i,(i+1)%5});es.push_back({i,i+5});es.push_back({i+5,5+(i+2)%5});}
 vector<int> adj[10];for(auto [a,b]:es){adj[a].push_back(b);adj[b].push_back(a);}
 int size=1;for(int i=0;i<N;i++)size*=q;cerr<<"size="<<size<<"\n";
 vector<int> pw(N,1);for(int i=1;i<N;i++)pw[i]=pw[i-1]*q;
 vector<int> nxt(size);vector<int> indeg(size);int state[10];
 for(int x=0;x<size;x++){
   int rem=x;for(int i=0;i<N;i++){state[i]=rem%q;rem/=q;}
   int y=0;for(int i=0;i<N;i++){
     int nv=state[i];if(nv){nv=(nv+1)%q;}else{int count=0;for(int j:adj[i])count+=state[j]==1; if(count>=th)nv=1;}
     y+=pw[i]*nv;
   }
   nxt[x]=y;indeg[y]++;
 }
 vector<int> queue,order;queue.reserve(size);order.reserve(size);
 for(int i=0;i<size;i++)if(!indeg[i])queue.push_back(i);
 for(size_t a=0;a<queue.size();a++){int v=queue[a],w=nxt[v];order.push_back(v);if(!--indeg[w])queue.push_back(w);}
 vector<int> period(size),tau(size);map<pair<int,int>,int64_t> census;map<int,int> cycles;
 for(int i=0;i<size;i++)if(indeg[i] && !period[i]){
   int x=i,len=0;do{len++;x=nxt[x];}while(x!=i);
   x=i;do{period[x]=len;tau[x]=0;census[{0,len}]++;x=nxt[x];}while(x!=i);
   cycles[len]++;
 }
 for(int i=(int)order.size()-1;i>=0;i--){int x=order[i],y=nxt[x];period[x]=period[y];tau[x]=tau[y]+1;census[{tau[x],period[x]}]++;}
 int maxTau=0;map<int,int64_t> basin;for(auto [k,v]:census){maxTau=max(maxTau,k.first);basin[k.second]+=v;}
 if(q==4 && th==1){
   assert(size==1048576 && maxTau==11);
   assert(cycles[1]==1 && cycles[4]==90 && cycles[5]==30 && cycles.size()==3);
   assert(census[make_pair(11,4)]==1920 && census[make_pair(0,4)]==360 && census[make_pair(0,5)]==150);
   assert(basin[1]==429136 && basin[4]==90600 && basin[5]==528840);
 }
 if(q==4 && th==2){
   assert(size==1048576 && maxTau==5 && cycles.size()==1 && cycles[1]==1);
   assert(census[make_pair(5,1)]==3740 && basin[1]==1048576);
 }
 cout<<"N "<<size<<" q "<<q<<" threshold "<<th<<" maxTau "<<maxTau<<"\ncycles ";for(auto [k,v]:cycles)cout<<k<<":"<<v<<" ";cout<<"\nbasin ";for(auto [k,v]:basin)cout<<k<<":"<<v<<" ";cout<<"\n";
 for(auto [k,v]:census)cout<<k.first<<","<<k.second<<","<<v<<"\n";cout<<"ALL ASSERTIONS PASSED\n";
}
