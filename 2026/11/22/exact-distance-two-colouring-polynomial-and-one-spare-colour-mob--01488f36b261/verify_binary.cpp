// Independent exact census for two-step colourings of the Fano incidence graph.
// Nonzero F_2^3 vectors are points, nonzero normals are lines, and
// point p is on line n precisely when their binary dot product vanishes.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using A=array<int,7>;

bool incident(int point,int line){
  return (__builtin_popcount((point+1)&(line+1))%2)==0;
}
bool allowed(int line,int color){
  return color==7 || !incident(color,line);
}
int main(){
  for(int p=0;p<7;p++){
    int degree=0;
    for(int line=0;line<7;line++)degree+=incident(p,line);
    assert(degree==3);
  }
  for(int p=0;p<7;p++)for(int q=p+1;q<7;q++){
    int overlap=0;
    for(int line=0;line<7;line++)overlap+=incident(p,line)&&incident(q,line);
    assert(overlap==1);
  }
  // Count nonincidence matchings by line-subset/point-subset DP, with an unassigned option.
  array<long long,128> dp{}; dp[0]=1;
  for(int line=0;line<7;line++){
    array<long long,128> next{};
    for(int m=0;m<128;m++){
      next[m]+=dp[m];
      for(int p=0;p<7;p++)if(!(m&(1<<p))&&!incident(p,line))
         next[m|(1<<p)]+=dp[m];
    }
    dp=next;
  }
  array<long long,8> match{};
  for(int mask=0;mask<128;mask++)match[__builtin_popcount((unsigned)mask)]+=dp[mask];
  assert((match==array<long long,8>{1,28,294,1456,3514,3864,1596,144}));

  vector<A> states;
  for(int miss=0;miss<8;miss++){
    vector<int> pal;
    for(int c=0;c<8;c++)if(c!=miss)pal.push_back(c);
    do{
      A s{};copy(pal.begin(),pal.end(),s.begin());
      bool valid=true;
      for(int line=0;line<7;line++)if(!allowed(line,s[line]))valid=false;
      if(valid)states.push_back(s);
    }while(next_permutation(pal.begin(),pal.end()));
  }
  assert(states.size()==1740);
  map<A,int> id;
  for(int i=0;i<(int)states.size();i++)id[states[i]]=i;
  assert(id.size()==1740);
  vector<vector<int>> adj(states.size());
  map<int,int> degreeCount,nearOptCount;
  long long oriented=0;
  for(int i=0;i<(int)states.size();i++){
    A a=states[i];bool used[8]={};
    for(int c:a)used[c]=true;
    int missing=find(used,used+8,false)-used;
    int toOptimal=0;
    // One-vertex moves on the line shore.
    for(int line=0;line<7;line++)if(allowed(line,missing)){
      A b=a;b[line]=missing;
      int j=id.at(b);adj[i].push_back(j);
      if(missing!=7&&find(b.begin(),b.end(),7)==b.end())toOptimal++;
    }
    // One-vertex moves on point shore; swap colour names after normalization.
    for(int p=0;p<7;p++){
      bool can=true;
      for(int line=0;line<7;line++)if(incident(p,line)&&a[line]==7)can=false;
      if(!can)continue;
      A b=a;
      for(int& c:b){if(c==p)c=7;else if(c==7)c=p;}
      int j=id.at(b);adj[i].push_back(j);
      if(missing!=7&&find(b.begin(),b.end(),7)==b.end())toOptimal++;
    }
    oriented+=adj[i].size();degreeCount[adj[i].size()]++;
    if(missing!=7)nearOptCount[toOptimal]++;
  }
  assert((degreeCount==map<int,int>{{8,1596},{14,144}}));
  assert((nearOptCount==map<int,int>{{0,588},{2,1008}}));
  assert(oriented==14784);
  // Connectedness of the normalized 1740-state graph.
  vector<int> dist(states.size(),-1);queue<int> q;
  q.push(0);dist[0]=0;int count=0,mx=0;
  while(!q.empty()){
    int i=q.front();q.pop();count++;
    mx=max(mx,dist[i]);
    for(int j:adj[i])if(dist[j]<0){dist[j]=dist[i]+1;q.push(j);}
  }
  assert(count==1740);
  assert(144LL*5040==725760);
  assert(1740LL*40320==70156800);
  assert((oriented/2)*40320==298045440);
  cout<<"matching counts:";for(auto n:match)cout<<" "<<n;cout<<"\n";
  cout<<"normalized states="<<states.size()<<" connected="<<count;
  cout<<" root eccentricity="<<mx<<"\n";
  cout<<"degree classes 8:"<<degreeCount[8]<<" 14:"<<degreeCount[14]<<"\n";
  cout<<"eight-used classes with 0/2 edges to seven-used: "<<nearOptCount[0]<<"/"<<nearOptCount[2]<<"\n";
  cout<<"chromatic polynomial values at 7 and 8: 725760, 70156800\n";
  cout<<"reconfiguration edges at 8: 298045440\nPASS\n";
}
