#include <bits/stdc++.h>
using namespace std;
static vector<int32_t> a;
int n=5; long long matches=0;
void gen(int row,int cols,int mask){
 if(row==n){a[mask]=1;matches++;return;}
 gen(row+1,cols,mask);
 for(int c=0;c<n;c++)if(!(cols>>c&1))gen(row+1,cols|(1<<c),mask|(1<<(row*n+c)));
}
void fwt(){size_t N=a.size();for(size_t step=1;step<N;step*=2)for(size_t k=0;k<N;k+=2*step)for(size_t j=0;j<step;j++){int x=a[k+j],y=a[k+j+step];a[k+j]=x+y;a[k+j+step]=x-y;}}
int main(int argc,char**argv){auto s=chrono::steady_clock::now();int N=1<<25;a.resize(N);gen(0,0,0); cerr<<"matches "<<matches<<"\n";fwt();map<int,long long> h;long long rank=0;int minAbs=9999;for(int v:a){h[v]++;if(v){rank++;minAbs=min(minAbs,abs(v));}}cout<<"rank "<<rank<<" nullity "<<N-rank<<" minpos "<<minAbs<<"\n";for(auto [x,y]:h)cout<<x<<":"<<y<<" ";cout<<"\n";cerr<<"elapsed 1 "<<chrono::duration<double>(chrono::steady_clock::now()-s).count()<<"\n";if(argc>1){for(auto &v:a)v=(v!=0); fwt();long long L=0;for(int v:a)L+=abs((long long)v);cout<<"projection numerator "<<L<<" denominator "<<N<<"\n";cerr<<"elapsed 2 "<<chrono::duration<double>(chrono::steady_clock::now()-s).count()<<"\n";}}
