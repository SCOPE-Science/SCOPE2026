// Reproducible exhaustive finite check for a point-line incidence graph over GF(4).
// Independent affine/slope model; no external libraries required (C++17).
#include <array>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
using U=uint64_t;
struct EdgeMask {U a=0,b=0;};
struct Fiber {U X,Y; vector<EdgeMask> pm;};
int mul(int a,int b){int c=0; for(int i=0;i<2;i++) if(b>>i&1)c ^= a<<i; if(c&8)c^=12; if(c&4)c^=7; return c;}
int main(){
 // Points 0..15=(x,y), 16..19=infinity of slopes 0..3, 20=vertical infinity.
 // Lines 0..15=(slope, intercept), 16..19=vertical x=c, 20=infinity.
 int inc[21][21]={}; U lm[21]={};int eid[21][21];int edges=0;
 for(int p=0;p<21;p++)for(int l=0;l<21;l++){
  bool ok=false;
  if(p<16){int x=p/4,y=p%4;
   if(l<16){int s=l/4,t=l%4;ok=(y==(mul(s,x)^t));}
   else if(l<20)ok=(x==l-16);
  }else if(p<20)ok=(l<16 && l/4==p-16)||l==20;
  else ok=l>=16;
  inc[p][l]=ok; if(ok){lm[l]|=U(1)<<p;eid[p][l]=edges++;}
  else eid[p][l]=-1;
 }
 assert(edges==105);
 for(int p=0;p<21;p++){int z=0;for(int l=0;l<21;l++)z+=inc[p][l];assert(z==5);}
 for(int l=0;l<21;l++)assert(__builtin_popcountll(lm[l])==5);
 vector<Fiber> h;
 for(int a=0;a<16;a++)for(int b=a+1;b<17;b++)for(int c=b+1;c<18;c++)
  for(int d=c+1;d<19;d++)for(int e=d+1;e<20;e++)for(int f=e+1;f<21;f++){
   U X=(U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d)|(U(1)<<e)|(U(1)<<f);
   bool arc=true;U Y=0;
   for(int j=0;j<21;j++){int k=__builtin_popcountll(X&lm[j]);if(k>2) {arc=false;break;} if(k==0) Y|=U(1)<<j;}
   if(!arc)continue;
   assert(__builtin_popcountll(Y)==6);
   Fiber fib;fib.X=X;fib.Y=Y;
   vector<int> ps,ls;for(int i=0;i<21;i++)if(!(X>>i&1))ps.push_back(i);
   for(int j=0;j<21;j++)if(!(Y>>j&1))ls.push_back(j);
   assert(ps.size()==15 && ls.size()==15);
   int deg[15];for(int i=0;i<15;i++){deg[i]=0;for(int j:ls)deg[i]+=inc[ps[i]][j];assert(deg[i]==3);}
   auto rec=[&](auto&& rec,int k,U used,EdgeMask E)->void{
    if(k==15){fib.pm.push_back(E);return;}
    for(int j:ls)if(inc[ps[k]][j]&&!(used>>j&1)){
     EdgeMask N=E;int z=eid[ps[k]][j];if(z<64)N.a|=U(1)<<z;else N.b|=U(1)<<(z-64);
     rec(rec,k+1,used|(U(1)<<j),N);
    }
   };
   rec(rec,0,0,EdgeMask{});
   assert(fib.pm.size()==288);
   h.push_back(move(fib));
  }
 assert(h.size()==168);
 auto delta=[](const EdgeMask&a,const EdgeMask&b){return 15-__builtin_popcountll(a.a&b.a)-__builtin_popcountll(a.b&b.b);};
 long long internal4=0,internal7=0,cross7=0;map<int,int> degree7,partdeg;
 for(auto &H:h){
  vector<vector<int>> ad(288);vector<int> dg(288,0);
  for(int i=0;i<288;i++)for(int j=i+1;j<288;j++){
   int t=delta(H.pm[i],H.pm[j]);assert(t>=4);
   if(t<=4){ad[i].push_back(j);ad[j].push_back(i);internal4++;}
   if(t<=7){dg[i]++;dg[j]++;internal7++;}
  }
  for(int i=0;i<288;i++){assert(ad[i].size()==10);partdeg[dg[i]]++;}
  vector<int> ds(288,-1);queue<int> Q;ds[0]=0;Q.push(0);
  while(!Q.empty()){int u=Q.front();Q.pop();for(int v:ad[u])if(ds[v]<0){ds[v]=ds[u]+1;Q.push(v);}}
  assert(*min_element(ds.begin(),ds.end())>=0);
 }
 assert(internal4==168*1440LL && internal7==168*5616LL);
 assert(partdeg[37]==168*144 && partdeg[41]==168*144 && partdeg.size()==2);
 vector<vector<int>> qh(168);vector<int> crossdeg(168*288,0);map<pair<int,int>,int> inter;
 for(int i=0;i<168;i++)for(int j=i+1;j<168;j++){
  int r=__builtin_popcountll(h[i].X&h[j].X);
  int s=__builtin_popcountll(h[i].Y&h[j].Y);inter[{r,s}]++;
  assert(r==s && r<=3);
  if(r<3)continue; // A new edge cannot simultaneously cover old free point and old free line; t>=2(6-r)>=8.
  int z=0;
  for(int a=0;a<288;a++)for(int b=0;b<288;b++){
   int t=delta(h[i].pm[a],h[j].pm[b]);assert(t>=7);
   if(t==7){z++;crossdeg[i*288+a]++;crossdeg[j*288+b]++;}
  }
  assert(z==216);cross7+=z;qh[i].push_back(j);qh[j].push_back(i);
 }
 assert((inter[{0,0}]==840 && inter[{1,1}]==6048 && inter[{2,2}]==3780 && inter[{3,3}]==3360));
 assert(cross7==725760);
 for(int z:crossdeg) assert(z==30);
 for(auto &n:qh)assert(n.size()==40);
 for(int i=0;i<168;i++){
  vector<int> ds(168,-1);queue<int> Q;ds[i]=0;Q.push(i);
  while(!Q.empty()){int u=Q.front();Q.pop();for(int v:qh[u])if(ds[v]<0){ds[v]=ds[u]+1;Q.push(v);}}
  assert(*min_element(ds.begin(),ds.end())>=0);
  assert(*max_element(ds.begin(),ds.end())==2);
 }
 cout << "PASS | PG(2,4) | 168 hyperovals | 288 matchings/fiber | 48384 minima of size 15\n";
 cout << "PASS | 4-exchange 168 connected fibers | 6-exchange 168 components | 7-exchange connected\n";
 cout << "PASS | 3360 hyperoval pairs sharing 3 points and 3 lines | 216 seven-exchange edges per pair\n";
 cout << "PASS | 7-exchange cross edges " << cross7 << " | all cross degrees 30\n";
 cout << "PASS | 7-exchange total edges " << internal7+cross7 << " | degrees 67:24192 and 71:24192\n";
}
