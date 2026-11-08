#include <iostream>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>
using namespace std;
int main(){ const int n=12,N=531441; const int edges[][2]={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}}; int nbr[n][4]={};int cnt[n]={}; for(auto &e:edges){nbr[e[0]][cnt[e[0]]++]=e[1];nbr[e[1]][cnt[e[1]]++]=e[0];} int pow3[n+1];pow3[0]=1;for(int i=1;i<=n;i++)pow3[i]=pow3[i-1]*3;
vector<int> succ(N),degree(N,0);int s[n];for(int x=0;x<N;x++){int z=x;for(int i=0;i<n;i++){s[i]=z%3;z/=3;}int y=0;for(int i=0;i<n;i++){int t=(s[i]==1?2:s[i]==2?0:0);if(s[i]==0){for(int j=0;j<4;j++)if(s[nbr[i][j]]==1){t=1;break;}}y+=pow3[i]*t;}succ[x]=y;degree[y]++;}
vector<int> q; q.reserve(N); for(int i=0;i<N;i++)if(!degree[i])q.push_back(i);for(size_t j=0;j<q.size();j++){int y=succ[q[j]];if(--degree[y]==0)q.push_back(y);}vector<int> entry(N,-1),period(N,0);map<int,int> cyc, perstate;map<pair<int,int>,int> joint;vector<int> extremal; int maxT=0;
for(int x=0;x<N;x++)if(degree[x]>0 && entry[x]<0){int y=x,k=0;do{entry[y]=0;y=succ[y];k++;}while(y!=x);cyc[k]++;y=x;do{period[y]=k;y=succ[y];}while(y!=x);}
for(auto it=q.rbegin();it!=q.rend();it++){int x=*it,y=succ[x];entry[x]=entry[y]+1;period[x]=period[y];}
for(int i=0;i<N;i++){joint[{entry[i],period[i]}]++;maxT=max(maxT,entry[i]);perstate[period[i]]++;}for(int i=0;i<N;i++)if(entry[i]==maxT)extremal.push_back(i);
cout << "N "<<N<<" maxT "<<maxT<<" extremal "<<extremal.size()<<" periodic "<<N-q.size()<<" cycles "<<accumulate(cyc.begin(),cyc.end(),0,[](int s,const auto& kv){return s+kv.second;})<<" classes "<<joint.size()<<"\n";
for(auto [k,v]:cyc)cout<<"C "<<k<<" "<<v<<"\n";
for(auto [k,v]:joint)cout<<"J "<<k.first<<" "<<k.second<<" "<<v<<"\n";
for(int x:extremal)cout<<"E "<<x<<" "<<period[x]<<"\n";
}
