// Exact Fourier census for ideals in [2] x [3] x [4].
// Compile: c++ -std=c++17 -O3 check.cpp -o check
// Run: ./check   (writes spectrum.csv and projection_kernel.csv)
// Uses standard C++17 only; all arithmetic is exact integer arithmetic.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <unordered_set>
#include <vector>
using namespace std;
static constexpr int A=2,B=3,C=4,M=A*B*C;
static constexpr int N=1<<M;
static int ix(int i,int j,int k){return (i*B+j)*C+k;}
static void demand(bool ok,const char* msg){if(!ok)throw runtime_error(msg);}
// First, independently enumerate weakly decreasing plane-partition height arrays.
static vector<uint32_t> height_ideals(){
 array<int,A*B> h{};vector<uint32_t> out;
 auto dfs=[&](auto&& self,int p)->void{
  if(p==A*B){
   uint32_t mask=0;
   for(int i=0;i<A;++i)for(int j=0;j<B;++j)for(int k=0;k<h[i*B+j];++k)
    mask|=uint32_t(1)<<ix(i,j,k);
   out.push_back(mask);return;
  }
  int i=p/B,j=p%B,upper=C;
  if(i)upper=min(upper,h[(i-1)*B+j]);
  if(j)upper=min(upper,h[i*B+j-1]);
  for(int v=0;v<=upper;v++){h[p]=v;self(self,p+1);}
 };
 dfs(dfs,0);sort(out.begin(),out.end());return out;
}
// Second, generate the distributive lattice by legal single-cube additions.
static vector<uint32_t> covers_ideals(){
 unordered_set<uint32_t> seen;queue<uint32_t> q;seen.insert(0);q.push(0);
 while(!q.empty()){
  auto x=q.front();q.pop();
  for(int i=0;i<A;i++)for(int j=0;j<B;j++)for(int k=0;k<C;k++){
   int t=ix(i,j,k);uint32_t bit=uint32_t(1)<<t;
   if(x&bit)continue;
   if(i&&!(x&(uint32_t(1)<<ix(i-1,j,k))))continue;
   if(j&&!(x&(uint32_t(1)<<ix(i,j-1,k))))continue;
   if(k&&!(x&(uint32_t(1)<<ix(i,j,k-1))))continue;
   auto y=x|bit;
   if(seen.insert(y).second)q.push(y);
  }
 }
 vector<uint32_t> out(seen.begin(),seen.end());sort(out.begin(),out.end());return out;
}
// DIT and DIF implementations have opposite butterfly orders.
static void transform(vector<int32_t>&v,bool forward_order){
 if(forward_order){
  for(int h=1;h<N;h*=2)for(int i=0;i<N;i+=h*2)for(int j=0;j<h;j++){
   int32_t a=v[i+j],b=v[i+j+h];v[i+j]=a+b;v[i+j+h]=a-b;
  }
 }else{
  for(int h=N/2;h>=1;h/=2)for(int i=0;i<N;i+=h*2)for(int j=0;j<h;j++){
   int32_t a=v[i+j],b=v[i+j+h];v[i+j]=a+b;v[i+j+h]=a-b;
  }
 }
}
static void csv(const string&file,const map<int,long long>& h){
 ofstream f(file);demand(bool(f),"CSV file open failed");f<<"value,multiplicity\n";
 for(auto [v,m]:h)f<<v<<","<<m<<"\n";
 demand(bool(f),"CSV write failed");
}
int main(){try{
 auto X=height_ideals(),Y=covers_ideals();demand(X==Y,"Independent enumerations differ");demand(X.size()==490,"Ideal count differs from MacMahon");
 vector<int32_t> first(N,0),second(N,0);
 for(auto x:X)first[x]=1;
 for(auto y:Y)second[y]=1;
 transform(first,true);transform(second,false);
 demand(first==second,"Independent exact Fourier transforms differ");
 // Also check every low-13-bit character directly, without any transform.
 for(int t=0;t<(1<<13);++t){
  int v=0;for(auto x:X)v+=__builtin_parity(x&uint32_t(t))?-1:1;
  demand(v==first[t],"Direct character sum disagrees");
 }
 map<int,long long> hist;long long rank=0, sum=0, parseval=0;int minimum=INT32_MAX, maximum=0;
 for(int i=0;i<N;i++){
  int v=first[i];hist[v]++;sum+=v;parseval+=1LL*v*v;
  if(v){rank++;minimum=min(minimum,abs(v));maximum=max(maximum,abs(v));}
 }
 demand(hist[0]==1234934,"Unexpected zero count");
 demand(rank==15542282,"Unexpected rank");
 demand(hist.size()==442,"Unexpected signed spectrum cardinality");
 demand(minimum==2&&maximum==490,"Unexpected positive spectrum extremes");
 demand(sum==N,"Character orthogonality failed");
 demand(parseval==1LL*N*490,"Plancherel failed");
 demand(hist.at(0)==hist.at(2),"Minimum-element pairing failed at zero");
 for(auto [v,m]:hist){demand(hist[2-v]==m,"All-level minimum-element pairing failed");}
 csv("spectrum.csv",hist);
 // The projection kernel equals N^{-1} times the Fourier transform of the spectral support.
 for(int i=0;i<N;i++){first[i]=first[i]!=0;second[i]=second[i]!=0;}
 transform(first,true);transform(second,false);
 demand(first==second,"Independent spectral support transforms differ");
 map<int,long long> phist;long long abs_sum=0, psum=0, pparseval=0;
 for(int i=0;i<N;i++){
  int v=first[i];phist[v]++;abs_sum+=llabs((long long)v);
  psum+=v;pparseval+=1LL*v*v;
 }
 demand(first[0]==rank,"Projection Fourier zero mode mismatch");
 demand(psum==N,"Support-kernel first moment failed");
 demand(pparseval==1LL*N*rank,"Support-kernel Parseval failed");
 demand(abs_sum==11078918348LL,"Projection norm numerator mismatch");
 csv("projection_kernel.csv",phist);
 long long g=std::gcd(abs_sum,(long long)N);
 demand(abs_sum/g==2769729587LL&&N/g==4194304,"Projection fraction mismatch");
 cout<<"BOXED_PLANE_PARTITION_234_WALSH_PASS count="<<X.size()
 <<" frequencies="<<N<<" zeros="<<hist[0]<<" rank="<<rank
 <<" signed_levels="<<hist.size()<<" smallest="<<minimum
 <<" largest="<<maximum<<" projection="<<abs_sum/g<<"/"<<N/g<<"\n";
 }catch(const exception&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;} }
