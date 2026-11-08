#include <bits/stdc++.h>
using namespace std;
int main(){const int n=6,m=6,sz=36,k=8;unsigned long long x=(1ULL<<k)-1,lim=(1ULL<<sz);long long eligible=0,res=0,star=0; while(x<lim){
int g[6]={},h[6]={},e[8],p=0;unsigned long long t=x;
while(t){int q=__builtin_ctzll(t);g[q/6]++;h[q%6]++;e[p++]=q;t&=t-1;}
bool ok=true;for(int i=0;i<6;i++) if(g[i]==0||h[i]==0){ok=false;break;}
if(ok){for(int z:e)if(g[z/6]==1 && h[z%6]==1){ok=false;break;}}
if(ok){eligible++;int deg3=0;for(int i=0;i<6;i++)if(g[i]>2||h[i]>2)deg3++;
if(deg3==0)star++;
// check exactly all pairs via direct graph distances
bool works=true;
for(int i=0;i<6&&works;i++)for(int ii=i;ii<6&&works;ii++)for(int j=0;j<6&&works;j++)for(int jj=0;jj<6;jj++){if(i==ii&&j>=jj)continue;int delta=0;for(int z:e){int a=z/6,b=z%6;int u=(i!=a)+(j!=b),v=(ii!=a)+(jj!=b);delta+=abs(u-v);}if(delta<2){works=false;break;}}
if(works)res++;
}
unsigned long long c=x&-x,r=x+c;x=(((r^x)>>2)/c)|r;
}
cout<<"eligible="<<eligible<<" direct_wdim2="<<res<<" degree<=2="<<star<<"\n";
}
