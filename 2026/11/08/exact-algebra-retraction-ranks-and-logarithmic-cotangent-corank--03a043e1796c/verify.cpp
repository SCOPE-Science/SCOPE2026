#include <array>
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int prod(int x,int y,int n){int out=0;for(int i=0;i<(1<<n);++i)if(x>>i&1)for(int j=0;j<(1<<n);++j)if(y>>j&1)if(!(i&j))out^=1<<(i|j);return out;}
int linear_rank(const vector<int>&imgs,int n){int b[8]={0},r=0;for(int i=0;i<n;i++){int v=0;for(int j=0;j<n;j++)if(imgs[i]>>(1<<j)&1)v|=1<<j;for(int j=n-1;j>=0;j--)if(v>>j&1){if(b[j])v^=b[j];else {b[j]=v;r++;break;}}}return r;}
int main(){for(int n=1;n<=3;n++){long long cnt[4]={0,0,0,0};int m=1<<n, sz=1<<(m-1); vector<int> vals;for(int a=0;a<(1<<m);a+=2)vals.push_back(a);
for(int a:vals)for(int b: (n>=2?vals:vector<int>{0}))for(int c: (n>=3?vals:vector<int>{0})){
 vector<int> img={a};if(n>=2)img.push_back(b);if(n>=3)img.push_back(c);
 int p[8]={};p[0]=1;for(int mask=1;mask<m;mask++){int bit=mask&-mask;int j=__builtin_ctz((unsigned)bit);p[mask]=prod(p[mask^bit],img[j],n);}
 bool good=true;for(int x:img){int y=0;for(int mask=0;mask<m;mask++)if(x>>mask&1)y^=p[mask];if(x!=y){good=false;break;}}
 if(good)cnt[linear_rank(img,n)]++;
}
cout<<n;for(int r=0;r<=n;r++)cout<<" "<<cnt[r];cout<<"\n";
}}
