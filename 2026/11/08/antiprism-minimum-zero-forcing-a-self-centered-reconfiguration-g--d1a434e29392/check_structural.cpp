// Standalone check of minimum zero-forcing sets of even cycle squares.
// Compile: c++ -std=c++17 -O2 check_structural.cpp -o check_structural
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using Set=array<int,4>;
static int mod(int v,int m) {v%=m;return v<0?v+m:v;}
static Set make(int m,int i,initializer_list<int> ds) {
 Set x{}; int j=0;for(int d:ds)x[j++]=mod(i+d,m);sort(x.begin(),x.end());return x;
}
static int forcing(int m, Set s){
 vector<int> blue(m,0);for(int u:s)blue[u]=1;
 int cnt=4,rounds=0;
 while(cnt<m){
  set<int> add;
  for(int v=0;v<m;++v) if(blue[v]){
   int miss=-1,num=0;
   for(int d:{-2,-1,1,2}){
     int w=mod(v+d,m);
     if(!blue[w]){miss=w;++num;}
   }
   if(num==1)add.insert(miss);
  }
  if(add.empty())return -1;
  for(int w:add)if(!blue[w]){blue[w]=1;++cnt;}
  ++rounds;
 }
 return rounds;
}
static int common(const Set&a,const Set&b){int n=0;for(int x:a)for(int y:b) if(x==y)++n;return n;}
int main(){
 for(int m=8;m<=30;m+=2){
   map<Set,int> predicted;
   for(int i=0;i<m;i++){
    predicted[make(m,i,{0,1,2,3})]=m/2-2;
    predicted[make(m,i,{0,1,2,4})]=m/2-1;
    predicted[make(m,i,{-2,0,1,2})]=m/2-1;
   }
   if((int)predicted.size()!=3*m) return 1;
   // Independent all-subsets exhaustive check for moderately sized graphs.
   if(m<=22)for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)for(int d=c+1;d<m;d++){
       Set s{a,b,c,d};int got=forcing(m,s);
       auto it=predicted.find(s);
       if(got != (it==predicted.end()?-1:it->second))return 2;
   }
   else for(auto [s,t]:predicted)if(forcing(m,s)!=t)return 3;
   vector<Set> states;for(auto [s,t]:predicted)states.push_back(s);
   int N=states.size(); vector<vector<int>>adj(N);long long edges=0;
   for(int i=0;i<N;i++)for(int j=0;j<i;j++)if(common(states[i],states[j])==3){
      adj[i].push_back(j);adj[j].push_back(i);edges++;
   }
   if(edges!=9*m)return 4;
   int degree5=0,degree8=0;
   for(auto v:adj){ if(v.size()==5)degree5++;else if(v.size()==8)degree8++;else return 5;}
   if(degree5!=2*m || degree8!=m)return 6;
   for(int src=0;src<N;src++){
     vector<int> dist(N,-1);queue<int> q;q.push(src);dist[src]=0;
     while(!q.empty()){
       int u=q.front();q.pop();
       for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;q.push(v);}
     }
     if(*min_element(dist.begin(),dist.end())!=0 || *max_element(dist.begin(),dist.end())!=m/2)return 7;
   }
   cout<<"PASS "<<m<<" states="<<N<<" edges="<<edges<<" eccentricity="<<m/2<<"\n";
 }
 cout<<"CPP_STRUCTURAL_PASS\n";
}
