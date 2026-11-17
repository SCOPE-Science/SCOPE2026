#include <iostream>
#include <cstdint>
#include <vector>
#include <cassert>
using namespace std;
static constexpr int born[9]={0,0,0,1,0,0,1,1,1};
static constexpr int survive[9]={0,0,0,1,1,0,1,1,1};
static uint64_t update(uint64_t x, int n) {
 uint64_t y=0;
 for(int col=0;col<n;++col) for(int row=0;row<3;++row) {
  int live=0;
  for(int dc=-1;dc<=1;++dc) for(int dr=-1;dr<=1;++dr){
   if(dr==0&&dc==0)continue;
   int cc=(col+dc+n)%n,rr=(row+dr+3)%3;
   live += (int)((x>>(3*cc+rr))&1ULL);
  }
  int old=(int)((x>>(3*col+row))&1ULL);
  int v=old?survive[live]:born[live];
  y |= uint64_t(v)<<(3*col+row);
 }
 return y;
}
int main() {
 vector<uint64_t> L(10);L[0]=2;L[1]=1;
 for(int i=2;i<10;++i)L[i]=L[i-1]+L[i-2];
 for(int n=3;n<=7;++n){
  uint64_t total=uint64_t(1)<<(3*n),count=0;
  uint64_t mask=total-1;
  for(uint64_t x=0;x<total;++x){
    uint64_t y=update(x,n);
    bool local_ok=true;
    for(int j=0;j<n;++j){
      int t=0;
      for(int dc=-1;dc<=1;++dc){
        int k=(j+dc+n)%n;
        for(int r=0;r<3;++r)t+=int((x>>(3*k+r))&1ULL);
      }
      if(t!=3&&t!=6){local_ok=false;break;}
    }
    bool flips=(y==(x^mask));
    assert(flips==local_ok);
    if(flips){
      ++count;
      assert(update(y,n)==x);
    }
  }
  uint64_t pow3=1;for(int i=0;i<n;++i)pow3*=3;
  uint64_t expected=2*pow3+L[n]+(n%3==0?2:-1);
  if(n%3==0){uint64_t v=1;for(int j=0;j<n/3;++j)v*=18;expected+=6*v;}
  assert(count==expected);
  cout<<"n="<<n<<" all_states="<<total<<" complement_flips="<<count<<" two_cycle_orbits="<<count/2<<" PASS\n";
 }
 cout<<"ALL_CHECKS_PASS\n";
}
