#include <iostream>
#include <vector>
#include <array>
#include <cassert>
#include <cstdint>
using namespace std;
using u64=unsigned long long;

// B_m is the m-page quadrilateral book, with hubs 0,1 and arms (2+2i,3+2i).
// State 0 rests, 1 excites, 2 is refractory. At rest, >=2 excited neighbors trigger.
static void step(const vector<unsigned char> &x,vector<unsigned char> &y,int m){
  auto advance=[](unsigned char q,int excited)->unsigned char{
    if(q==1)return 2;
    if(q==2)return 0;
    return (excited>=2)?1:0;
  };
  int e0=(x[1]==1),e1=(x[0]==1);
  for(int i=0;i<m;i++){
    e0+=(x[2+2*i]==1);
    e1+=(x[3+2*i]==1);
  }
  y[0]=advance(x[0],e0); y[1]=advance(x[1],e1);
  for(int i=0;i<m;i++){
    int a=2+2*i,b=a+1;
    y[a]=advance(x[a],(x[0]==1)+(x[b]==1));
    y[b]=advance(x[b],(x[1]==1)+(x[a]==1));
  }
}
static bool all_zero(const vector<unsigned char> &x){
  for(auto z:x)if(z)return false;
  return true;
}
static u64 powi(u64 a,int k){u64 v=1;while(k--)v*=a;return v;}
static u64 formula_S(int m){
  return powi(9,m)+powi(7,m)+2*powi(8,m)+4*powi(6,m)
   +6ULL*m*powi(6,m-1)+u64(m+2)*(m+2)*powi(4,m-1);
}
int main(){
  for(int m=1;m<=6;m++){
    int n=2*m+2;u64 N=powi(3,n);
    vector<unsigned char>x(n),y(n),z(n),w(n);array<u64,4>hist={0,0,0,0};
    u64 bad=0;
    for(u64 code=0;code<N;code++){
      u64 q=code;
      for(int i=0;i<n;i++){x[i]=q%3;q/=3;}
      if(all_zero(x)){hist[0]++;continue;}
      step(x,y,m);
      if(all_zero(y)){hist[1]++;continue;}
      step(y,z,m);
      if(all_zero(z)){hist[2]++;continue;}
      step(z,w,m);
      if(all_zero(w)){hist[3]++;continue;}
      bad++;
    }
    u64 S=formula_S(m);
    array<u64,4> predicted={1,powi(4,m+1)-1,S-powi(4,m+1),N-S};
    if(hist!=predicted||bad!=0){cerr<<"FAIL m="<<m<<"\n";return 1;}
    cout<<"m="<<m<<" total="<<N<<" N0="<<hist[0]<<" N1="<<hist[1]
    <<" N2="<<hist[2]<<" N3="<<hist[3]<<" beyond3="<<bad<<" PASS\n";
  }
  return 0;
}
