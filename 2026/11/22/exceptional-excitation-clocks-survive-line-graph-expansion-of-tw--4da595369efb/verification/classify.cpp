#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 int step=argc>1?atoi(argv[1]):2; if(step!=1 && step!=2) return 2; bool reps=argc>2 && string(argv[2])=="--reps";
 vector<pair<int,int>> ed;
 for(int i=0;i<5;i++) ed.push_back({i,(i+1)%5});
 for(int i=0;i<5;i++) ed.push_back({i,5+i});
 for(int i=0;i<5;i++) ed.push_back({5+i,5+(i+step)%5});
 int n=ed.size(); int N=1;int pw[16]; pw[0]=1;for(int i=1;i<=15;i++)pw[i]=pw[i-1]*3;N=pw[15];
 int mask[15]={};for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){if(ed[i].first==ed[j].first||ed[i].first==ed[j].second||ed[i].second==ed[j].first||ed[i].second==ed[j].second)mask[i]|=1<<j;}
 for(int i=0;i<n;i++) if(__builtin_popcount((unsigned)mask[i])!=4) return 1;
 // compute transition once for each state, based on ternary digits
 auto nxt=[&](int st)->int{
  int dig[15],ones=0;int t=st;
  for(int i=0;i<n;i++){dig[i]=t%3;t/=3;if(dig[i]==1)ones|=1<<i;}
  int out=0;
  for(int i=0;i<n;i++){
    int d=dig[i];int z=(d==0)?((mask[i]&ones)?1:0):(d==1?2:0);
    out+=z*pw[i];
  }
  return out;
 };
 vector<unsigned char> status(N,0); // 0 unprocessed,1 active DFS, 2 done
 vector<unsigned short> depth(N,0),period(N,0);
 vector<int> path;path.reserve(100000);
 unordered_map<int,uint64_t> cyc;map<pair<int,int>,uint64_t> ent;map<int,uint64_t> orbit;
 map<int,int> witness,cycleWitness;int maxD=0,maxP=0,maxState=-1;int longest=0;
 
 for(int seed=0;seed<N;seed++){
  if(status[seed])continue;
  path.clear(); int cur=seed;
  while(status[cur]==0){status[cur]=1;path.push_back(cur);cur=nxt(cur);}
  int old=(int)path.size();
  if(status[cur]==1){
   int at=old-1;while(path[at]!=cur)at--;
   int p=old-at;
   for(int j=at;j<old;j++){
    int s=path[j];period[s]=p;depth[s]=0;status[s]=2;
   }
   cyc[p]+=p;orbit[p]++;if(p>=4 && reps)cout<<p<<" "<<cur<<"\n";if(!cycleWitness.count(p))cycleWitness[p]=cur;
   old=at;
  }
  for(int j=old-1;j>=0;j--){int s=path[j],r=nxt(s);period[s]=period[r];depth[s]=depth[r]+1;status[s]=2;}
 }
 for(int s=0;s<N;s++){
  int p=period[s],d=depth[s];ent[{p,d}]++;
  if(d>maxD){maxD=d;maxState=s;}
  if(p>maxP)maxP=p;
 }
 if(reps)return 0;
 cout<<"CYCLE_STATE_COUNTS\n";
 for(auto [p,c]:cyc) cout<<p<<" "<<c<<" "<<c/p<<" "<<cycleWitness[p]<<"\n";
 cout<<"MAXD "<<maxD<<" MAXP "<<maxP<<" MAXSTATE "<<maxState<<"\n";
 cout<<"ENTRANCES\n";
 for(auto [pair,c]:ent)cout<<pair.first<<" "<<pair.second<<" "<<c<<"\n";
}
