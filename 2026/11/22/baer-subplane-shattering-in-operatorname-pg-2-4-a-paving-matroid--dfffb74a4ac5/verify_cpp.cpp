// Independent construction by projective joins/meets, followed by exhaustive Boolean traces.
// Build: g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
using P=array<int,3>;
int mul(int a,int b){int p=0;for(int i=0;i<2;i++)for(int j=0;j<2;j++)if((a&(1<<i))&&(b&(1<<j)))p^=(i+j==0?1:i+j==1?2:3);return p;}
P normalize(P p){int a=0;for(int x:p)if(x){a=x;break;}int ai=0;for(int x=1;x<4;x++)if(mul(x,a)==1)ai=x;for(int &x:p)x=mul(x,ai);return p;}
int determinant(P a,P b,P c){return mul(a[0],mul(b[1],c[2])^mul(b[2],c[1]))^mul(a[1],mul(b[0],c[2])^mul(b[2],c[0]))^mul(a[2],mul(b[0],c[1])^mul(b[1],c[0]));}
using B=bitset<360>;
struct Key{array<uint64_t,6> words{};int d;bool operator==(Key const&o)const{return words==o.words&&d==o.d;}};
struct H{size_t operator()(Key const& k)const{size_t h=k.d;for(auto v:k.words)h^=v+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);return h;}};
B Q[21];unordered_map<Key,bool,H> memo;
Key keyOf(B const &x,int d){Key k{};k.d=d;for(size_t i=0;i<360;i++)if(x.test(i))k.words[i/64]|=uint64_t(1)<<(i%64);return k;}
bool fulltree(B const &C,int d){if(!d)return C.any();if((int)C.count()<(1<<d))return false;auto key=keyOf(C,d);auto it=memo.find(key);if(it!=memo.end())return it->second;for(int i=20;i>=0;i--){B Y=C&Q[i],N=C&(~Q[i]);if((int)min(Y.count(),N.count())<(1<<(d-1)))continue;if(fulltree(N,d-1)&&fulltree(Y,d-1))return memo[key]=true;}return memo[key]=false;}
int main(){
 set<P> pointSet;
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)for(int c=0;c<4;c++)if(a||b||c)pointSet.insert(normalize({a,b,c}));
 vector<P> pts(pointSet.begin(),pointSet.end());assert(pts.size()==21);
 vector<uint32_t> lines;for(int i=0;i<21;i++)for(int j=i+1;j<21;j++){
  uint32_t L=0;for(int k=0;k<21;k++)if(determinant(pts[i],pts[j],pts[k])==0)L|=1u<<k;
  if(find(lines.begin(),lines.end(),L)==lines.end())lines.push_back(L);
 }assert(lines.size()==21);for(auto L:lines)assert(__builtin_popcount(L)==5);
 int join[21][21]{};for(int i=0;i<21;i++)for(int j=i+1;j<21;j++)for(int t=0;t<21;t++)if((lines[t]&(1u<<i))&&(lines[t]&(1u<<j)))join[i][j]=join[j][i]=t;
 int meet[21][21]{};for(int i=0;i<21;i++)for(int j=i+1;j<21;j++){
  uint32_t mask=lines[i]&lines[j];assert(__builtin_popcount(mask)==1);
  meet[i][j]=meet[j][i]=__builtin_ctz(mask);
 }
 set<uint32_t> sub;
 int frames=0;
 for(int a=0;a<21;a++)for(int b=a+1;b<21;b++)for(int c=b+1;c<21;c++)for(int d=c+1;d<21;d++){
  if(determinant(pts[a],pts[b],pts[c])==0||determinant(pts[a],pts[b],pts[d])==0||determinant(pts[a],pts[c],pts[d])==0||determinant(pts[b],pts[c],pts[d])==0)continue;
  frames++;uint32_t S=(1u<<a)|(1u<<b)|(1u<<c)|(1u<<d);
  while(true){set<int> L;for(int i=0;i<21;i++)if(S&(1u<<i))for(int j=i+1;j<21;j++)if(S&(1u<<j))L.insert(join[i][j]);
   uint32_t T=S;for(int u:L)for(int v:L)if(u<v)T|=1u<<meet[u][v];
   if(S==T)break;S=T;
  }assert(__builtin_popcount(S)==7);sub.insert(S);
 }
 assert(frames==2520&&sub.size()==360);vector<uint32_t> planes(sub.begin(),sub.end());
 for(int i=0;i<21;i++)for(int j=0;j<360;j++)if(planes[j]&(1u<<i))Q[i].set(j);
 int counts[6]={};
 for(int k=0;k<=5;k++)for(uint32_t S=0;S<(1u<<21);S++)if(__builtin_popcount(S)==k){
  set<uint32_t> traces;for(auto B:planes){uint32_t T=B&S;traces.insert(T);if(traces.size()==(1u<<k))break;}
  bool shattered=traces.size()==(1u<<k);
  if(k<=4){bool predicted=true;if(k==4)for(auto L:lines)if((L&S)==S)predicted=false;assert(shattered==predicted);}
  if(k==5)assert(!shattered);
  if(shattered)counts[k]++;
 }
 assert(counts[0]==1&&counts[1]==21&&counts[2]==210&&counts[3]==1330&&counts[4]==5880&&counts[5]==0);
 B all;all.set();bool five=fulltree(all,5),six=fulltree(all,6);assert(five&&!six);
 cout<<"INDEPENDENT_JOIN_MEET_CONSTRUCTION "<<sub.size()<<" planes from "<<frames<<" quadrangles\n";
 cout<<"SHATTERED_COUNTS 1 21 210 1330 5880 0\n";
 cout<<"LITTLESTONE exactly 5; depth 6 impossible; memoized cases "<<memo.size()<<"\n";
}
