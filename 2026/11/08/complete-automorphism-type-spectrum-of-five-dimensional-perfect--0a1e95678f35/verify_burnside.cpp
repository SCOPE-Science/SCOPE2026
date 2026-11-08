#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;
using U=uint32_t;
static const int n=5;
static bool invertible(U x){uint32_t a[n];for(int i=0;i<n;i++)a[i]=(x>>(i*n))&31u;int r=0;for(int j=0;j<n;j++){int p=r;while(p<n&&!((a[p]>>j)&1u))p++;if(p==n)continue;swap(a[p],a[r]);for(int k=r+1;k<n;k++)if((a[k]>>j)&1u)a[k]^=a[r];r++;}return r==n;}
static uint64_t centralizer(const array<int,5>&p,bool id=false){
 bool seen[25]={};vector<U> orbits;
 for(int k=0;k<25;k++){if(seen[k])continue;int t=k;U row=0;do{seen[t]=1;row|=1u<<t;t=n*p[t/n]+p[t%n];}while(t!=k);orbits.push_back(row);}
 int d=orbits.size();if(id)return 9999360ULL;
 uint64_t count=0;for(uint32_t mask=0;mask<(1u<<d);mask++){U M=0;for(int j=0;j<d;j++)if(mask&(1u<<j))M|=orbits[j];if(invertible(M))count++;}
 cout<<"dimension="<<d<<" centralizer_units="<<count<<"\n";return count;
}
int main(){
 const array<array<int,5>,7> rep={{{0,1,2,3,4},{1,0,2,3,4},{1,0,3,2,4},{1,2,0,3,4},{1,2,0,4,3},{1,2,3,0,4},{1,2,3,4,0}}};
 const array<int,7> sz={{1,10,15,20,20,30,24}};
 uint64_t tot=0;for(int t=0;t<7;t++){auto k=centralizer(rep[t],t==0);tot+=k*sz[t];}
 cout<<"Burnside numerator="<<tot<<" classes="<<tot/120<<"\n";
 if(tot!=120ULL*85411)return 2;
 cout<<"VERIFY_OK\n";
}
