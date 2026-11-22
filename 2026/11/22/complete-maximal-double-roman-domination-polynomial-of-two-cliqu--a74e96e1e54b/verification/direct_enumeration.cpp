#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int n=stoi(argv[1]);uint64_t total=1ULL<<(4*n);map<int,long long> hist; long long zeroside=0,nzeros=0;
for(uint64_t key=0;key<total;key++){uint64_t x=key;int a[32]={0};int w=0;for(int i=0;i<2*n;i++){a[i]=x&3;x>>=2;w+=a[i];}bool z0=0,z1=0,any=0;for(int i=0;i<n;i++){z0|=(a[i]==0);z1|=(a[i+n]==0);}if(z0&&z1)continue;if(!z0&&!z1)any=true;else {int full=z0?1:0;for(int i=0;i<n;i++)if(a[full*n+i]>0&&a[(1-full)*n+i]>0){any=true;break;}}if(!any)continue;
 bool ok=true;for(int v=0;v<2*n&&ok;v++){if(a[v]>=2)continue;int side=v/n,idx=v%n,n2=0,n3=0,high=0;for(int j=0;j<n;j++)if(j!=idx){n2+=(a[side*n+j]==2);n3+=(a[side*n+j]==3);high+=(a[side*n+j]>=2);}int t=a[(1-side)*n+idx];n2+=(t==2);n3+=(t==3);high+=(t>=2);if(a[v]==0&&!(n3>=1||n2>=2))ok=false; if(a[v]==1&&!high)ok=false;}if(ok)hist[w]++;}
cout<<"n="<<n<<" count="<<accumulate(hist.begin(),hist.end(),0ll,[](long long a,auto b){return a+b.second;})<<" poly:";for(auto [w,c]:hist)cout<<" "<<w<<":"<<c;cout<<"\n";}
