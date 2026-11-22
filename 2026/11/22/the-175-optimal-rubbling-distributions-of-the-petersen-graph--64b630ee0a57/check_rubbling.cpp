// Exact four-pebble rubbling classification on the Petersen graph.
// Compile: g++ -std=c++17 -O2 verify_rubbling.cpp -o verify_rubbling
#include <array>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cassert>
using namespace std;
using State=array<int,10>;
vector<int> V;
vector<int> N[10];
vector<State> states[5];
void generate(int i,int left,State &s,int m){
 if(i==9){s[9]=left;states[m].push_back(s);return;}
 for(int c=0;c<=left;++c){s[i]=c;generate(i+1,left-c,s,m);}
}
int reach(const State &start,bool strict){
 queue<State> Q;set<State> visited;visited.insert(start);Q.push(start);int mask=0;
 while(!Q.empty()){
  State a=Q.front();Q.pop();
  for(int i=0;i<10;++i){if(a[i])mask|=(1<<i);}
  for(int t=0;t<10;++t){
   for(int ix=0;ix<(int)N[t].size();++ix){
    int u=N[t][ix];
    for(int jx=ix;jx<(int)N[t].size();++jx){
     int v=N[t][jx];if((u!=v&&!strict)||a[u]<1||a[v]<(u==v?2:1))continue;
     State b=a;b[u]--;b[v]--;b[t]++;
     if(visited.insert(b).second)Q.push(b);
    }
   }
  }
 }
 return mask;
}
string shape(State a){
 vector<int> q;for(int x:a)if(x)q.push_back(x);sort(q.rbegin(),q.rend());
 string s;for(int x:q)s+=char('0'+x);return s;
}
string induced(State a){
 vector<int> ix;for(int i=0;i<10;++i)if(a[i])ix.push_back(i);
 int edges=0,degree[4]={};
 for(int i=0;i<4;++i)for(int j=i+1;j<4;++j){
  if(find(N[ix[i]].begin(),N[ix[i]].end(),ix[j])!=N[ix[i]].end()){
    edges++;degree[i]++;degree[j]++;
  }
 }
 vector<int>d(degree,degree+4);sort(d.begin(),d.end());
 if(edges==0)return "4K1";
 if(edges==1)return "K2+2K1";
 if(edges==2){if(d==vector<int>({1,1,1,1}))return "2K2";return "P3+K1";}
 if(edges==3){if(d==vector<int>({1,1,1,3}))return "K1,3";return "P4";}
 assert(false);return "";
}
int main(){
 for(int a=0;a<5;++a)for(int b=a+1;b<5;++b)V.push_back((1<<a)|(1<<b));
 for(int i=0;i<10;++i)for(int j=0;j<10;++j)if(i!=j&&!(V[i]&V[j]))N[i].push_back(j);
 State s{};for(int m=0;m<=4;++m)generate(0,m,s,m);
 map<string,int> rub,peb,graphs,graphfails;
 int lower=0,all=0;
 for(int m=0;m<=4;++m)for(auto a:states[m]){
  int r=reach(a,true),p=reach(a,false);
  if(m<=3 && r==1023)lower++;
  if(m==4){
    bool success=r==1023;
    if(success)rub[shape(a)]++;
    if(p==1023)peb[shape(a)]++;
    if(shape(a)=="1111"){
      if(success)graphs[induced(a)]++;
      else graphfails[induced(a)]++;
    }
    all++;
  }
 }
 cout<<"states_before_four="<<states[0].size()+states[1].size()+states[2].size()+states[3].size()<<" lower_success="<<lower<<"\n";
 cout<<"states_four="<<all<<"\n";
 for(auto [k,v]:rub)cout<<"rubbling "<<k<<" "<<v<<"\n";
 for(auto [k,v]:peb)cout<<"pebbling "<<k<<" "<<v<<"\n";
 for(auto [k,v]:graphs)cout<<"uniform_success "<<k<<" "<<v<<"\n";
 for(auto [k,v]:graphfails)cout<<"uniform_failure "<<k<<" "<<v<<"\n";
 assert(lower==0&&all==715);
 assert(rub["4"]==10&&rub["22"]==45&&rub["211"]==30&&rub["1111"]==90);
 assert(peb["4"]==10&&peb.size()==1);
 assert(graphs["4K1"]==5&&graphs["K2+2K1"]==60&&graphs["2K2"]==15&&graphs["K1,3"]==10);
 assert(graphfails["P3+K1"]==60&&graphfails["P4"]==60);
}
