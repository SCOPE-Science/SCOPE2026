#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 const int n=15; vector<pair<int,int>> vert;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)vert.push_back({i,j});
 int mask[n]{};for(int i=0;i<n;i++)for(int j=0;j<n;j++){auto [a,b]=vert[i];auto [c,d]=vert[j];if(a!=c&&a!=d&&b!=c&&b!=d)mask[i]|=1<<j;}
 for(int i=0;i<n;i++)if(__builtin_popcount((unsigned)mask[i])!=6){cerr<<"degree fail\n";return 1;}
 int p3[n+1];p3[0]=1;for(int i=1;i<=n;i++)p3[i]=3*p3[i-1];int N=p3[n];
 vector<int> next(N),indeg(N,0),queue;queue.reserve(N);
 for(int st=0;st<N;st++){
  int x=st,active=0,z=st;
  for(int j=0;j<n;j++){int c=x%3;x/=3;if(c==1)active|=1<<j;}
  x=st;int out=0;
  for(int j=0;j<n;j++){int c=x%3;x/=3;int q=(c==1)?2:(c==2?0:((mask[j]&active)?1:0));out+=q*p3[j];}
  next[st]=out;indeg[out]++;
 }
 for(int st=0;st<N;st++)if(indeg[st]==0)queue.push_back(st);
 for(size_t qi=0;qi<queue.size();qi++){int u=queue[qi],v=next[u];if(--indeg[v]==0)queue.push_back(v);}
 map<int,long long> cycleN;map<int,long long> cycleStates;map<int,long long> flow;
 vector<uint8_t> orbitperiod(N,0);map<pair<int,int>,long long> joint;
 map<int,vector<int>> reps;
 int cycStates=0; for(int st=0;st<N;st++)if(indeg[st]>0){
   int j=st,L=0;do{indeg[j]=0;j=next[j];L++;}while(j!=st);
 j=st;do{orbitperiod[j]=L;j=next[j];}while(j!=st);
   cycleN[L]++;cycleStates[L]+=L;cycStates+=L;
   if(L>=4) reps[L].push_back(st);
 }
 vector<uint16_t> dist(N,0);
 for(size_t qi=queue.size();qi-->0;){int st=queue[qi];int v=next[st];dist[st]=dist[v]+1;orbitperiod[st]=orbitperiod[v];flow[dist[st]]++;joint[{dist[st],orbitperiod[st]}]++;}
 flow[0]=cycStates;for(auto [L,c]:cycleStates)joint[{0,L}]=c;
 cerr<<"N "<<N<<" cyclic "<<cycStates<<" removed "<<queue.size()<<"\n";
 for(auto [p,c]:cycleN)cerr<<"period "<<p<<" cycles "<<c<<" states "<<cycleStates[p]<<"\n";
 for(auto [t,c]:flow)cerr<<"transient "<<t<<" population "<<c<<"\n";
 for(auto [tp,c]:joint)cerr<<"joint "<<tp.first<<" "<<tp.second<<" "<<c<<"\n";
 // enumerate rotation-normalized cycles representative and color profiles for longer cycles
 for(auto &[L,cs]:reps){map<vector<int>,int> profiles;long long uniform=0;for(int s:cs){vector<int> counts(L);int v=s;for(int i=0;i<L;i++){int x=v;int exc=0;while(x){exc+=(x%3==1);x/=3;}counts[i]=exc;v=next[v];}
 // lexicographically minimal rotation
 auto best=counts;for(int i=1;i<L;i++){auto rot=counts;rotate(rot.begin(),rot.begin()+i,rot.end());if(rot<best)best=rot;}
 profiles[best]++;}
 cerr<<"PROFILES period "<<L<<" types "<<profiles.size()<<"\n";
 for(auto &[vec,c]:profiles){cerr<<"[";for(int k=0;k<L;k++)cerr<<(k?",":"")<<vec[k];cerr<<"] "<<c<<"\n";}
 }
 ofstream repout("representatives.txt");for(auto &[L,cs]:reps)for(int x:cs)repout<<L<<" "<<x<<"\n";repout.close();
 ofstream out("raw_census.txt");out<<"N "<<N<<" cycStates "<<cycStates<<"\n";for(auto [p,c]:cycleN)out<<"P "<<p<<" "<<c<<"\n";for(auto [t,c]:flow)out<<"T "<<t<<" "<<c<<"\n";for(auto [tp,c]:joint)out<<"J "<<tp.first<<" "<<tp.second<<" "<<c<<"\n";
 return 0;
}
