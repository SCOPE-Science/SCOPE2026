#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <queue>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;
static constexpr int C=6, D=24, N=1<<D;
static int bit(int i,int j,int k){return 12*i+6*j+k;}
static uint32_t rotate180(uint32_t s){
 uint32_t t=0;
 for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<6;k++)
  if(s&(1u<<bit(i,j,k)))t|=1u<<bit(1-i,1-j,5-k);
 return t;
}
static uint32_t trans(uint32_t s){
 uint32_t t=0;
 for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<6;k++)
  if(s&(1u<<bit(i,j,k)))t|=1u<<bit(j,i,k);
 return t;
}
static vector<uint32_t> heights(){
 vector<uint32_t> out;
 for(int a=0;a<=6;a++)for(int b=0;b<=a;b++)
 for(int c=0;c<=a;c++)for(int d=0;d<=min(b,c);d++){
  array<int,4> h={a,b,c,d}; uint32_t x=0;
  for(int q=0;q<4;q++)for(int k=0;k<h[q];k++)x|=1u<<(6*q+k);
  out.push_back(x);
 }
 sort(out.begin(),out.end());return out;
}
static vector<uint32_t> predecessor_bfs(){
 unordered_set<uint32_t> seen;queue<uint32_t> q;seen.insert(0);q.push(0);
 while(!q.empty()){
  uint32_t s=q.front();q.pop();
  for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<6;k++){
   int p=bit(i,j,k);uint32_t b=1u<<p; if(s&b)continue;
   bool allowed=(!i||(s&(1u<<bit(i-1,j,k))))&&(!j||(s&(1u<<bit(i,j-1,k))))&&(!k||(s&(1u<<bit(i,j,k-1))));
   if(allowed&&seen.insert(s|b).second)q.push(s|b);
  }
 }
 vector<uint32_t> out(seen.begin(),seen.end());sort(out.begin(),out.end());return out;
}
static int signed_sum(const vector<uint32_t>& v,uint32_t f){
 int sum=0;for(uint32_t x:v) sum+=((__builtin_popcount(x&f)&1)?-1:1);return sum;
}
static void walsh(vector<int32_t>& a,bool reverse){
 if(!reverse){for(int d=0;d<D;d++)for(int base=0;base<N;base+=(2<<d))
  for(int i=0;i<(1<<d);i++){
   int p=base+i,q=p+(1<<d);int32_t x=a[p],y=a[q];a[p]=x+y;a[q]=x-y;}}
 else {for(int d=D-1;d>=0;d--)for(int base=0;base<N;base+=(2<<d))
  for(int i=0;i<(1<<d);i++){
   int p=base+i,q=p+(1<<d);int32_t x=a[p],y=a[q];a[p]=x+y;a[q]=x-y;}}
}

static int small_minimum_zero_weight(int length){
  int dim=4*length, total=1<<dim;
  vector<int32_t> t(total,0);
  for(int a=0;a<=length;a++)for(int b=0;b<=a;b++)
  for(int c=0;c<=a;c++)for(int d=0;d<=min(b,c);d++){
    array<int,4> h={a,b,c,d};unsigned mask=0;
    for(int j=0;j<4;j++)for(int k=0;k<h[j];k++)mask|=1u<<(j*length+k);
    t[mask]=1;
  }
  for(int j=0;j<dim;j++)for(int base=0;base<total;base+=(2<<j))
    for(int k=0;k<(1<<j);k++){
      int pos=base+k,q=pos+(1<<j);
      int32_t x=t[pos],y=t[q];t[pos]=x+y;t[q]=x-y;
    }
  int mn=dim+1;
  for(int x=0;x<total;x++)if(t[x]==0)mn=min(mn,__builtin_popcount((unsigned)x));
  return mn==dim+1?-1:mn;
}

int main(){
 assert(small_minimum_zero_weight(1)==1);
 assert(small_minimum_zero_weight(2)==2);
 assert(small_minimum_zero_weight(3)==1);
 assert(small_minimum_zero_weight(4)==-1);
 assert(small_minimum_zero_weight(5)==1);
 assert(small_minimum_zero_weight(6)==3);
 auto v=heights(),v2=predecessor_bfs();assert(v.size()==336&&v==v2);
 int minzero=999;vector<uint32_t> zero_triples;
 for(int i=0;i<D;i++){
  assert(signed_sum(v,1u<<i)!=0);
  for(int j=i+1;j<D;j++){
   assert(signed_sum(v,(1u<<i)|(1u<<j))!=0);
   for(int k=j+1;k<D;k++){
    uint32_t f=(1u<<i)|(1u<<j)|(1u<<k);
    if(signed_sum(v,f)==0)zero_triples.push_back(f);
   }
  }
 }
 assert(zero_triples.size()==32);
 array<array<int,3>,8> reps={{{2,5,7},{2,7,15},{2,10,18},{4,6,19},{4,7,19},{4,8,19},{5,6,18},{6,10,14}}};
 set<uint32_t> predicted;
 for(auto r:reps){
  uint32_t f=(1u<<r[0])|(1u<<r[1])|(1u<<r[2]);
  predicted.insert(f);predicted.insert(trans(f));predicted.insert(rotate180(f));predicted.insert(trans(rotate180(f)));
 }
 assert(predicted.size()==32&&set<uint32_t>(zero_triples.begin(),zero_triples.end())==predicted);
 auto a=vector<int32_t>(N,0);for(uint32_t x:v)a[x]=1;
 walsh(a,false);
 const array<int,25> expected={{0,0,0,32,109,820,2838,9928,24656,56898,98458,171922,206155,253202,210188,180324,103021,61140,23013,8898,2017,420,51,4,0}};
 array<int,25> weights={}; int64_t moment1=0,moment2=0;int zero=0,minimum=1000000,maximum=0;
 for(int f=0;f<N;f++){
  int x=a[f];moment1+=x;moment2+=int64_t(x)*x;
  if(!x){zero++;weights[__builtin_popcount((unsigned)f)]++;}
  else {minimum=min(minimum,abs(x));maximum=max(maximum,abs(x));}
 }
 assert(weights==expected&&zero==1414094&&minimum==2&&maximum==336);
 assert(moment1==N&&moment2==int64_t(336)*N);
 for(uint32_t f=0;f<8192;f++)assert(a[f]==signed_sum(v,f));
 int rank=N-zero;
 for(int f=0;f<N;f++)a[f]=(a[f]!=0);
 walsh(a,true);
 int64_t l1=0,projsquare=0,projsum=0;
 for(int32_t x:a){l1+=llabs((long long)x);projsquare+=(long long)x*x;projsum+=x;}
 assert(rank==15363122&&a[0]==rank&&l1==9182696964LL);
 assert(projsquare==int64_t(rank)*N&&projsum==N);
 cout<<"BOX_226_WALSH_PASS ideals=336 zeros="<<zero<<" rank="<<rank
 <<" minwt=3 triples=32 minnonzero="<<minimum<<" max="<<maximum
 <<" projection_sum="<<l1<<" projection_ratio=2295674241/4194304"<<endl;
}
