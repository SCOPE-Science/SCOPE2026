#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
int mult(int x,int y){if(!x||!y)return 0;int lg[4]={-99,0,1,2},an[3]={1,2,3};return an[(lg[x]+lg[y])%3];}
array<int,3> norm(array<int,3> v){int first=0;while(!v[first])++first;int inv[4]={0,1,3,2};int d=inv[v[first]];for(int &x:v)x=mult(x,d);return v;}
int main(){
 vector<array<int,3>> pts;set<array<int,3>> unique;
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)for(int c=0;c<4;c++)if(a||b||c)unique.insert(norm({a,b,c}));
 for(auto v:unique)pts.push_back(v);
 assert(pts.size()==21); vector<U> lines;
 for(auto l:pts){U m=0;for(int i=0;i<21;i++){auto p=pts[i];if((mult(l[0],p[0])^mult(l[1],p[1])^mult(l[2],p[2]))==0)m|=1u<<i;}lines.push_back(m);}
 assert(set<U>(lines.begin(),lines.end()).size()==21);
 auto valid=[&](U s){for(U l:lines)if(__builtin_popcount(s&l)<2)return false;return true;};
 vector<U> opt;array<int,13> less{};
 for(U s=0;s<(1u<<21);++s){int k=__builtin_popcount(s);if(k<=12&&valid(s)){if(k<12)less[k]++;else opt.push_back(s);}}
 assert(opt.size()==11480);for(int k=0;k<12;k++)assert(less[k]==0);
 auto profile=[&](U s){array<int,6> a{};for(U l:lines)++a[__builtin_popcount(s&l)];return a;};
 map<array<int,6>, vector<U>> groups;for(U s:opt)groups[profile(s)].push_back(s);
 assert(groups.size()==3);
 map<array<int,6>,int> expected={{{0,0,9,9,0,3},1120},{{0,0,10,6,3,2},10080},{{0,0,12,0,9,0},280}};
 for(auto &[p,v]:groups)assert((int)v.size()==expected.at(p));
 unordered_map<U,int> idx;idx.reserve(opt.size()*2);for(int i=0;i<(int)opt.size();i++)idx[opt[i]]=i;
 vector<vector<int>> ad(opt.size());int nedges=0;array<int,3> degdist{};
 for(int i=0;i<(int)opt.size();i++){
  U s=opt[i];for(int a=0;a<21;a++)if(s&(1u<<a))for(int b=0;b<21;b++)if(!(s&(1u<<b))){auto it=idx.find(s^(1u<<a)^(1u<<b));if(it!=idx.end())ad[i].push_back(it->second);}
  auto p=profile(s);int degree=(int)ad[i].size();assert((p==array<int,6>{0,0,12,0,9,0}&&degree==0)||(p==array<int,6>{0,0,10,6,3,2}&&degree==15)||(p==array<int,6>{0,0,9,9,0,3}&&degree==27));nedges+=degree;
 }
 assert(nedges==181440); // oriented edges
 int n=opt.size();vector<int> component(n,-1);vector<int> sizes;
 for(int i=0;i<n;i++)if(component[i]<0){int id=sizes.size();vector<int> q={i};component[i]=id;for(int z=0;z<(int)q.size();z++)for(int j:ad[q[z]])if(component[j]<0){component[j]=id;q.push_back(j);}sizes.push_back(q.size());}
 assert(sizes.size()==281);assert(count(sizes.begin(),sizes.end(),1)==280);assert(count(sizes.begin(),sizes.end(),11200)==1);
 auto bfs=[&](int start,bool two){vector<int>d(n,-1),q={start};d[start]=0;for(int z=0;z<(int)q.size();z++){
   int v=q[z];vector<int> neighbors=ad[v];
   if(two){U mask=opt[v];vector<int> in,out;for(int a=0;a<21;a++)((mask>>a)&1?in:out).push_back(a);
    for(int i=0;i<(int)in.size();i++)for(int j=i+1;j<(int)in.size();j++){
     U zmask=mask^(1u<<in[i])^(1u<<in[j]);
     for(int p=0;p<(int)out.size();p++)for(int r=p+1;r<(int)out.size();r++){
      auto it=idx.find(zmask|(1u<<out[p])|(1u<<out[r]));if(it!=idx.end())neighbors.push_back(it->second);
     }
    }
   }
   for(int w:neighbors)if(d[w]<0){d[w]=d[v]+1;q.push_back(w);}
  }
  int ecc=0;for(int x:d)if(x>ecc)ecc=x;return make_pair((int)q.size(),ecc);
 };
 for(auto &[p,v]:groups){int start=idx[v[0]];auto r1=bfs(start,false),r2=bfs(start,true);
  cout<<"profile";for(int x:p)cout<<" "<<x;cout<<" count "<<v.size()<<" one_BFS "<<r1.first<<","<<r1.second<<" two_BFS "<<r2.first<<","<<r2.second<<"\n";
  if(v.size()==280){assert(r1.first==1&&r2.first==n&&r2.second==5);}else{assert(r1.first==11200&&r1.second==8&&r2.first==n&&r2.second==(v.size()==1120?5:4));}
 }
 cout<<"PASS: 11480 optimum point double-blocking sets, 90720 exchange edges, 281 components; 2-swaps connected with diameter 5 via orbit symmetry.\n";
}
