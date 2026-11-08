#include <bits/stdc++.h>
using namespace std;
unordered_map<string,bool> memo;
int mode = 0;
long long depthstates[5]={};
int rankof(int code,int i){return (code>>(2*i))&3;}
string keyof(array<int,3> rem,vector<int> events){
 sort(events.begin(), events.end());
 string s;
 for(int x:rem)s.push_back(char(x));
 for(int x:events)s.push_back(char(x+1));
 return s;
}
bool finalEF1(const vector<int>& e){
 vector<vector<int>> bundle(3);
 for(int x:e)bundle[x%3].push_back(x/3);
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++)if(i!=j){
   int own=0,oth=0,high=0;
   for(int c:bundle[i])own+=rankof(c,i)+1;
   for(int c:bundle[j]){int v=rankof(c,i)+1;oth+=v;high=max(high,v);}
   if(own<oth-high)return false;
  }
 }
 return true;
}
bool solve(array<int,3> rem,vector<int> events){
 int t=events.size();
 string key=keyof(rem,events);
 auto it=memo.find(key); if(it!=memo.end())return it->second;
 depthstates[t]++;
 if(t==4)return memo.emplace(key,finalEF1(events)).first->second;
 for(int i=0;i<4;i++)if(rem[0]&(1<<i))
 for(int j=0;j<4;j++)if(rem[1]&(1<<j))
 for(int k=0;k<4;k++)if(rem[2]&(1<<k)){
  int c=i+4*j+16*k;
  auto nr=rem;nr[0]^=1<<i;nr[1]^=1<<j;nr[2]^=1<<k;
  bool possible=false;
  for(int recipient=0;recipient<3;recipient++){
   if(mode==1 && t==1 && !events.empty() && recipient==events[0]%3)continue;
   if(mode==2 && t==1 && !events.empty() && recipient!=events[0]%3)continue;
   if(mode==3 && t<3){bool taken=false;for(int v:events)if(v%3==recipient)taken=true;if(taken)continue;}
   auto ne=events;ne.push_back(3*c+recipient);
   if(solve(nr,ne)){possible=true;break;}
  }
  if(!possible){memo.emplace(key,false);return false;}
 }
 memo.emplace(key,true);return true;
}
int main(){
 const vector<int> expected={1,1,0,0};
 for(mode=0;mode<4;mode++){
  memo.clear();fill(begin(depthstates),end(depthstates),0);
  bool win=solve({15,15,15},{});
  cout<<"mode="<<mode<<" winning="<<win<<" states="<<memo.size();
  for(int t=0;t<=4;t++)cout<<" d"<<t<<"="<<depthstates[t];
  cout<<"\n";
  if(int(win)!=expected[mode])return 1;
 }
 return 0;
}
