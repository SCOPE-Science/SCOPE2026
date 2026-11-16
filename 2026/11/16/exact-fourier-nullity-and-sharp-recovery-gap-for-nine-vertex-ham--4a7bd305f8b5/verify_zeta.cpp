#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

static constexpr int K=8, D=28, TOTAL=1<<D;
static int end_a[D], end_b[D];
static int64_t factorial[K+1];
static int32_t *values;
static long long accepted=0;

int32_t forest_weight(uint32_t subset,int edges) {
    if(edges==0) return static_cast<int32_t>(factorial[K]/2);
    array<int,K> degrees{}; array<int,K> parent{};
    for(int i=0;i<K;i++) parent[i]=i;
    auto root=[&](int x){while(parent[x]!=x){parent[x]=parent[parent[x]]; x=parent[x];}return x;};
    uint32_t s=subset;
    while(s) {
        int e=__builtin_ctz(s);s&=s-1;
        int u=end_a[e], v=end_b[e];
        if(++degrees[u]>2 || ++degrees[v]>2) return 0;
        int a=root(u),b=root(v);
        if(a==b)return 0;
        parent[a]=b;
    }
    int paths=0;
    for(int i=0;i<K;i++) if(degrees[i]>0 && root(i)==i) paths++;
    int64_t count=(1LL<<(paths-1))*factorial[K-edges];
    int64_t weighted=((edges&1)?-1:1)*(1LL<<edges)*count;
    if(weighted<INT32_MIN || weighted>INT32_MAX)abort();
    return static_cast<int32_t>(weighted);
}
static void choose(int next,int rem,int count,uint32_t mask){
 if(rem==0){int v=forest_weight(mask,count);if(v){values[mask]=v;accepted++;}return;}
 for(int i=next;i<=D-rem;i++)choose(i+1,rem-1,count,mask|(1u<<i));
}
int main(){
 factorial[0]=1;for(int i=1;i<=K;i++)factorial[i]=factorial[i-1]*i;
 int idx=0;for(int i=0;i<K;i++)for(int j=i+1;j<K;j++){end_a[idx]=i;end_b[idx]=j;idx++;}
 values=new int32_t[TOTAL]();
 for(int t=0;t<=K-1;t++)choose(0,t,t,0);
 cerr<<"nonzero initial forced-forest terms="<<accepted<<"\n";
 for(int j=0;j<D;j++){
  int stride=1<<j, span=2*stride;
  for(int start=0;start<TOTAL;start+=span)
    for(int offset=0;offset<stride;offset++)
      values[start+stride+offset]+=values[start+offset];
 }
 vector<int64_t>hist(20161,0);
 int64_t total=0,abs_total=0,second=0;
 for(int i=0;i<TOTAL;i++){int64_t v=values[i];if(llabs(v)>20160)abort();hist[llabs(v)]++;total+=v;abs_total+=llabs(v);second+=v*v;}
 cout<<"N="<<TOTAL<<"; paths=20160; sum="<<total<<"; abs_sum="<<abs_total<<"; sumsq="<<second<<"\n";
 for(int i=0;i<=20160;i++)if(hist[i])cout<<i<<":"<<hist[i]<<"\n";
 delete[] values;
}
