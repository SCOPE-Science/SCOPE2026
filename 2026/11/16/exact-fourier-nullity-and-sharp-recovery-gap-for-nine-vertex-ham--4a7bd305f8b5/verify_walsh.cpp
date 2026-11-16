#include <bits/stdc++.h>
using namespace std;
int main(){
 constexpr int k=8,d=k*(k-1)/2,N=1<<d;
 unique_ptr<int16_t[]> arr(new int16_t[N]());
 int ix[k][k];int j=0;for(int a=0;a<k;a++)for(int b=a+1;b<k;b++)ix[a][b]=ix[b][a]=j++;
 array<int,k> per; iota(per.begin(),per.end(),0);
 int paths=0;
 do{if(per[0]>per[k-1])continue;int mask=0;for(int i=0;i<k-1;i++)mask|=1<<ix[per[i]][per[i+1]];if(arr[mask]!=0){cerr<<"Duplicate Hamilton path mask"<<endl;return 2;}arr[mask]=1;paths++;}while(next_permutation(per.begin(),per.end()));
 cerr<<"paths "<<paths<<" target 20160\n";if(paths!=20160)return 3;
 for(int b=0;b<d;b++){
  int stride=1<<b,step=stride<<1;
  for(int start=0;start<N;start+=step){int16_t* a=arr.get()+start;for(int q=0;q<stride;q++){int x=a[q],y=a[q+stride];a[q]=(int16_t)(x+y);a[q+stride]=(int16_t)(x-y);}}
  if((b+1)%4==0)cerr<<"FWHT stage "<<(b+1)<<"/28\n";
 }
 vector<long long> hist(paths+1,0);long long abs_sum=0;long long sumsq=0;long long sum=0; long long sum4mod=0;const long long mod=1000000007;
 for(int i=0;i<N;i++){int v=arr[i];hist[abs(v)]++;abs_sum+=abs(v);sumsq+=1LL*v*v;sum+=v;long long t=1LL*v*v%mod;sum4mod=(sum4mod+t*t)%mod;}
 cout<<"N="<<N<<"; paths="<<paths<<"; sum="<<sum<<"; abs_sum="<<abs_sum<<"; sumsq="<<sumsq<<"; sum4mod="<<sum4mod<<"; mod="<<mod<<"\n";
 for(int i=0;i<=paths;i++)if(hist[i])cout<<i<<":"<<hist[i]<<"\n";
}
