// Exhaustive finite certificate for skew forcing and optimal-set exchange on the folded five-cube.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify_clebsch.cpp -o verify_clebsch
// Run: ./verify_clebsch
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int pc(unsigned x){return __builtin_popcount(x);}
int main(){
 const int N=16, ALL=(1<<N)-1;
 const array<int,5> generator={1,2,4,8,15};
 array<int,N> nb{};
 for(int x=0;x<N;++x){for(int g:generator)nb[x]|=1<<(x^g);assert(pc(nb[x])==5);}
 for(int x=0;x<N;++x)for(int y=0;y<N;++y)assert(bool(nb[x]&(1<<y))==bool(nb[y]&(1<<x)));
 auto closure=[&](int s){
   while(true){int t=s;for(int x=0;x<N;++x){int w=nb[x]&(~s)&ALL;
       if(w && (w&(w-1))==0)t|=w;}
     if(t==s) return s;
     s=t;
   }
 };
 array<int,17> counts{};vector<int> opt;int kmin=17;
 for(int s=0;s<=ALL;++s){if(closure(s)!=ALL)continue;
  int k=pc(s);counts[k]++;
  if(k<kmin){kmin=k;opt.clear();}
  if(k==kmin)opt.push_back(s);
 }
 assert(kmin==8 && opt.size()==6490);
 const array<int,17> expected={0,0,0,0,0,0,0,0,6490,9760,7752,4352,1820,560,120,16,1};
 assert(counts==expected);
 vector<int> index(1<<N,-1);for(int i=0;i<(int)opt.size();++i)index[opt[i]]=i;
 for(int s:opt)assert(index[ALL^s]>=0);
 // Exact Cayley automorphism family: translations and permutations of five generators.
 // Four distinct generator images define a nonsingular linear map on F_2^4.
 vector<array<int,N>> transforms;
 for(int a:generator)for(int b:generator)for(int c:generator)for(int d:generator){
   if(a==b||a==c||a==d||b==c||b==d||c==d)continue;
   array<int,N> p{};
   for(int x=0;x<N;++x){int v=0;
      if(x&1) v^=a;
      if(x&2) v^=b;
      if(x&4) v^=c;
      if(x&8) v^=d;
      p[x]=v;
   }
   bool visited[16]={};for(int v:p){assert(v>=0&&v<N&&!visited[v]);visited[v]=true;}
   for(int x=0;x<N;++x)for(int g:generator)assert(nb[p[x]]&(1<<p[x^g]));
   transforms.push_back(p);
 }
 assert(transforms.size()==120);
 set<int> remaining(opt.begin(),opt.end());
 vector<pair<int,int>> orbits;
 while(!remaining.empty()){
   int s=*remaining.begin();set<int> orbit;
   for(auto &p:transforms)for(int shift=0;shift<N;++shift){
     int t=0;for(int x=0;x<N;++x)if(s&(1<<x))t|=1<<p[x^shift];
     assert(index[t]>=0);orbit.insert(t);
   }
   for(int t:orbit)remaining.erase(t);
   orbits.push_back({(int)orbit.size(),s});
 }
 sort(orbits.begin(),orbits.end());
 const vector<pair<int,int>> eo={{10,0x3cc3},{160,0x033f},{240,0x069f},
    {320,0x166b},{480,0x037d},{480,0x06bb},{960,0x035f},
    {1920,0x036f},{1920,0x067b}};
 assert(orbits==eo);
 // Build the token-jump graph of minimum skew forcing sets.
 int n=(int)opt.size();vector<vector<int>> edges(n);map<int,int> degree_hist;long long degree_sum=0;
 for(int i=0;i<n;++i){
    int s=opt[i];for(int a=0;a<N;++a)if(s&(1<<a))
      for(int b=0;b<N;++b)if(!(s&(1<<b))){
        int j=index[s^(1<<a)^(1<<b)];if(j>=0)edges[i].push_back(j);
      }
    sort(edges[i].begin(),edges[i].end());
    assert(unique(edges[i].begin(),edges[i].end())==edges[i].end());
    degree_hist[(int)edges[i].size()]++;degree_sum+=edges[i].size();
 }
 assert(degree_sum/2==116320);
 assert((degree_hist==map<int,int>{{32,10},{35,3200},{36,2160},{38,1120}}));
 for(int i=0;i<n;++i)for(int j:edges[i])assert(binary_search(edges[j].begin(),edges[j].end(),i));
 long long exceptions=0;map<int,int> orbit_exc;int min_ecc=99,max_ecc=0;
 for(auto [sz,rep]:orbits){
   vector<int> dist(n,-1);queue<int> q;
   int start=index[rep];dist[start]=0;q.push(start);
   while(!q.empty()){int v=q.front();q.pop();for(int w:edges[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}}
   int ecc=0,extra=0;for(int j=0;j<n;++j){
      assert(dist[j]>=0);
      ecc=max(ecc,dist[j]);
      int johnson=8-pc(rep&opt[j]);
      assert(dist[j]>=johnson && dist[j]<=johnson+1);
      extra+=(dist[j]==johnson+1);
   }
   assert(ecc==8);min_ecc=min(min_ecc,ecc);max_ecc=max(max_ecc,ecc);
   orbit_exc[rep]=extra;exceptions+=(long long)sz*extra;
 }
 assert(exceptions%2==0 && exceptions/2==9120);
 assert(min_ecc==8&&max_ecc==8);
 // A concrete failure of the basis-exchange axiom despite connected exchanges.
 int A=0x037d, B=0x195d, vertex=5;
 assert(index[A]>=0 && index[B]>=0 && (A&(1<<vertex)) && !(B&(1<<vertex)));
 int alternatives=B&~A;assert(alternatives==((1<<11)|(1<<12)));
 for(int v=0;v<N;++v)if(alternatives&(1<<v))assert(index[A^(1<<vertex)^(1<<v)]<0);
 for(auto [sz,rep]:orbits){int expected_ex=(rep==0x035f?9:(rep==0x036f?5:0));assert(orbit_exc[rep]==expected_ex);}
 cout<<"GRAPH 16 vertices 40 edges group 1920\n";
 cout<<"MINIMUM 8 COUNT 6490 TOTAL_FORCE_SETS "<<accumulate(counts.begin(),counts.end(),0)<<"\n";
 cout<<"POLYNOMIAL";for(int i=0;i<=16;++i)if(counts[i])cout<<" "<<i<<":"<<counts[i];cout<<"\n";
 cout<<"ORBIT_REP_SIZE_DEGREE_EXCESS";for(auto [sz,rep]:orbits)cout<<" 0x"<<hex<<rep<<dec<<":"<<sz<<":"<<edges[index[rep]].size()<<":"<<orbit_exc[rep];cout<<"\n";
 cout<<"DEGREES";for(auto [d,c]:degree_hist)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"EXCHANGE_EDGES 116320 RADIUS 8 DIAMETER 8 EXCEPTIONAL_PAIRS 9120\n";
 cout<<"BASIS_EXCHANGE_FAILURE A=0x037d B=0x195d removed=5 candidates=11,12\nPASS\n";
}
