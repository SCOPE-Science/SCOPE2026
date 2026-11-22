#include <bits/stdc++.h>
using namespace std;
int main(){
 int n=7;vector<array<int,3>> lines;
 for(int j=0;j<7;j++)lines.push_back({j,(j+1)%7,(j+3)%7});
 vector<pair<int,int>> e;
 for(int j=0;j<7;j++)for(int p:lines[j])e.push_back({p,j});
 assert(e.size()==21);
 int ei[7][7]; memset(ei,-1,sizeof(ei));for(int i=0;i<21;i++)ei[e[i].first][e[i].second]=i;
 set<array<int,3>> forb;
 for(int p=0;p<7;p++)for(int l=0;l<7;l++)if(ei[p][l]<0){
  for(int q:lines[l]){
   int m=-1;for(int k=0;k<7;k++)if(ei[p][k]>=0&&ei[q][k]>=0){m=k;break;}
   assert(m>=0);array<int,3> t={ei[p][m],ei[q][m],ei[q][l]};sort(t.begin(),t.end());forb.insert(t);
  }
 }
 vector<vector<int>> rules(21);for(auto t:forb){int h=t[2];rules[h].push_back((1<<t[0])|(1<<t[1]));}
 int lim=1<<21;vector<uint8_t> ok(lim,0);ok[0]=1;
 long long count[22]={},maximal[22]={};
 for(int mask=0;mask<lim;mask++){
  if(mask){int h=31-__builtin_clz(mask),prev=mask^(1<<h);if(!ok[prev])continue;bool v=true;for(int pm:rules[h])if((prev&pm)==pm){v=false;break;}ok[mask]=v;}
  if(!ok[mask])continue;int sz=__builtin_popcount((unsigned)mask);count[sz]++;
 }
 for(int mask=0;mask<lim;mask++)if(ok[mask]){
  bool maximal_=true;for(int rem=(lim-1)^mask;rem;rem&=rem-1){int b=rem&-rem;if(ok[mask|b]){maximal_=false;break;}}
  if(maximal_)maximal[__builtin_popcount((unsigned)mask)]++;
 }
 cout<<"edges="<<e.size()<<" forbidden_triples="<<forb.size()<<"\n";
 cout<<"valid:";for(int i=0;i<22;i++)if(count[i])cout<<" "<<i<<":"<<count[i];cout<<"\n";
 cout<<"maximal:";for(int i=0;i<22;i++)if(maximal[i])cout<<" "<<i<<":"<<maximal[i];cout<<"\n";
 cout<<"total valid="<<accumulate(count,count+22,0LL)<<" total maximal="<<accumulate(maximal,maximal+22,0LL)<<"\n";
}
