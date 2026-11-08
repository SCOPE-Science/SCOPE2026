// Exact integer enumerator for four consecutive quartic-residue coset labels.
// Standard C++17 only: g++ -std=c++17 -O2 verify_quartic4.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static constexpr int LIM=263681; // all smaller eligible primes are checked
static vector<int> sieve(){
 vector<bool> ok(LIM+1,true);ok[0]=ok[1]=false;
 for(int k=2;k*k<=LIM;k++)if(ok[k])for(int j=k*k;j<=LIM;j+=k)ok[j]=false;
 vector<int> out;for(int p=5;p<LIM;p++)if(ok[p]&&p%4==1)out.push_back(p);return out;
}
static vector<int> factors(int n){vector<int>v;for(int d=2;d*d<=n;d++)if(n%d==0){v.push_back(d);while(n%d==0)n/=d;}if(n>1)v.push_back(n);return v;}
static int power(int a,int b,int p){long long v=1,t=a;while(b){if(b&1)v=v*t%p;t=t*t%p;b>>=1;}return (int)v;}
static int primitive(int p){auto fs=factors(p-1);for(int g=2;g<p;g++){bool ok=true;for(int q:fs)if(power(g,(p-1)/q,p)==1){ok=false;break;}if(ok)return g;}assert(false);return -1;}
static array<uint64_t,4> cover(int p){
 int g=primitive(p);vector<uint8_t> lab(p,255);int x=1;
 for(int k=0;k<p-1;k++){assert(lab[x]==255);lab[x]=uint8_t(k%4);x=(long long)x*g%p;}assert(x==1);
 array<uint64_t,4> seen{};for(int n=1;n+3<p;n++){
   int code=64*lab[n]+16*lab[n+1]+4*lab[n+2]+lab[n+3];
   seen[code>>6]|=uint64_t(1)<<(code&63);
   if(seen[0]==UINT64_MAX&&seen[1]==UINT64_MAX&&seen[2]==UINT64_MAX&&seen[3]==UINT64_MAX) break;
 }return seen;
}
int main(){auto ps=sieve();int last_bad=0,last_zero_bad=0,num_bad=0;int prev_good=0;int max_miss=0;
 vector<int> bads;for(int p:ps){auto bits=cover(p);int missing=0;for(int i=0;i<4;i++)missing+=64-__builtin_popcountll(bits[i]);
 if(missing){num_bad++;last_bad=p;max_miss=max(max_miss,missing);bads.push_back(p);}
 if(!(bits[0]&1)){last_zero_bad=p;}
 if(p==3361){assert(missing==1);assert((bits[195/64]&(uint64_t(1)<<(195%64)))==0);}
 if(p==3373)assert(missing==0);
 }
 cout<<"eligible_primes="<<ps.size()<<" bad_primes="<<num_bad<<" last_bad="<<last_bad<<" first_good_after_last="<<3373<<" last_zero_bad="<<last_zero_bad<<" max_missing="<<max_miss<<"\n";
 cout<<"bad_primes:";for(int p:bads)cout<<" "<<p;cout<<"\n";
 assert(last_bad==3361 && last_zero_bad==2689);
}
