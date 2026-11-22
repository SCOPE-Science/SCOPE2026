#include <bits/stdc++.h>
using namespace std;
static inline int pop(unsigned x){return __builtin_popcount(x);}
static inline bool adjC(int x,int y,int n){return (x+1)%n==y || (y+1)%n==x;}
static inline bool d2(int x,int y,int n){return (x+2)%n==y || (y+2)%n==x;}
static inline bool valid3(const array<int,3> &a,int n){
 bool good=d2(a[0],a[1],n)||d2(a[0],a[2],n)||d2(a[1],a[2],n);
 if(!good)return false;
 // no three consecutive cycle sites
 for(int q=0;q<3;q++){
  int t=a[q];
  if(find(a.begin(),a.end(),(t+1)%n)!=a.end() && find(a.begin(),a.end(),(t+2)%n)!=a.end())return false;
 }
 return true;
}
static inline bool validmask(unsigned mask,const vector<int>&coords,int n){
 array<int,3> a;int i=0;
 for(int k=0;k<(int)coords.size();k++)if(mask>>k&1)a[i++]=coords[k];
 return valid3(a,n);
}
static vector<int> reachable(const vector<int>&coords,int n, int sm,int tm){
 // Here all coords distinct; m <= 7
 unsigned size=1u<<coords.size();
 vector<unsigned char> good(size,0),visited(size,0);
 vector<int>state;
 for(unsigned mask=0;mask<size;mask++)if(pop(mask)==3 && validmask(mask,coords,n)){
  good[mask]=1;state.push_back(mask);
 }
 if(!good[sm]||!good[tm])return {};
 if(sm==tm)return {sm};
 vector<int> frontier{sm};visited[sm]=1;
 vector<int> prev(size,-1);
 for(int depth=1;depth<=4;depth++){
  vector<int>next;
  for(int from:frontier)for(int to:state){
   if(visited[to])continue;
   unsigned diff=from^to;
   if(pop(diff)!=2)continue;
   int i=__builtin_ctz((unsigned)(from & diff));
   int j=__builtin_ctz((unsigned)(to & diff));
   if(adjC(coords[i],coords[j],n))continue;
   prev[to]=from;
   if(to==tm){vector<int> rev{tm};int curr=tm;while(curr!=sm){curr=prev[curr];rev.push_back(curr);}reverse(rev.begin(),rev.end());return rev;}
   visited[to]=1;next.push_back(to);
  }
  frontier.swap(next);if(frontier.empty())break;
 }
 return {};
}
static pair<int,vector<int>> solvepair(const vector<int>&coords, int n,int A,int B){
 auto base=reachable(coords,n,A,B);if(!base.empty())return {-1,base};
 vector<char>mark(n,0);
 for(int x:coords)mark[x]=1;
 for(int x:coords){
  for(int offset=-2;offset<=2;offset++){
   int h=((x+offset)%n+n)%n;
   if(mark[h])continue;
   mark[h]=2;
   vector<int>ext=coords;ext.push_back(h);
   auto path=reachable(ext,n,A,B);if(!path.empty())return {h,path};
  }
 }
 return {-1,{}};
}
int main(){
 unsigned long long profiles=0,cases=0,failed=0;int maxn=0;
 for(int m=4;m<=6;m++){
  int base=1;for(int z=0;z<m;z++)base*=7;
  for(int idx=0;idx<base;idx++){
   vector<int>g(m);int v=idx;int n=0;
   for(int j=0;j<m;j++){g[j]=v%7+1;v/=7;n+=g[j];}
   if(n<7)continue;
   bool canonical=true;
   for(int sh=1;sh<m;sh++){
    for(int i=0;i<m;i++){
     if(g[(i+sh)%m]<g[i]){canonical=false;break;}
     if(g[(i+sh)%m]>g[i])break;
    }
    if(!canonical)break;
   }
   if(!canonical)continue;
   vector<int>coords(m);int p=0;
   for(int i=0;i<m;i++){coords[i]=p;p+=g[i];}
   int all=(1<<m)-1;
   vector<int>sm;
   for(int mask=0;mask<=all;mask++)if(pop(mask)==3 && validmask(mask,coords,n))sm.push_back(mask);
   profiles++;maxn=max(maxn,n);
   for(int i=0;i<(int)sm.size();i++)for(int j=i+1;j<(int)sm.size();j++){
    if((sm[i]|sm[j])!=all)continue;
    cases++;
    auto cert=solvepair(coords,n,sm[i],sm[j]);
    if(!cert.second.empty()){cout<<m<<"\t";for(int k=0;k<m;k++){if(k)cout<<",";cout<<g[k];}cout<<"\t"<<sm[i]<<"\t"<<sm[j]<<"\t"<<cert.first<<"\t";for(int k=0;k<(int)cert.second.size();k++){if(k)cout<<",";cout<<cert.second[k];}cout<<"\n";}
    else {
     failed++;
     if(failed<=20){cerr<<"FAIL m="<<m<<" gaps=";for(int x:g)cerr<<x<<",";cerr<<" source="<<sm[i]<<" target="<<sm[j]<<" n="<<n<<"\n";}
    }
   }
  }
  cerr<<"finished m="<<m<<" profiles="<<profiles<<" cases="<<cases<<" failed="<<failed<<"\n";
 }
 cerr<<"{\"profiles\":"<<profiles<<",\"cases\":"<<cases<<",\"failed\":"<<failed<<",\"max_representative_n\":"<<maxn<<"}"<<endl;
 return failed?1:0;
}
