#include <cstdint>
#include <iostream>
#include <array>
#include <cassert>
using namespace std;

// Row r and column c occupy bit (3*c+r), all indices periodic.
static uint32_t advance(uint32_t x,int n){
 uint32_t y=0;
 for(int c=0;c<n;c++)for(int r=0;r<3;r++){
  unsigned p=3*c+r;
  if((x>>p)&1U)continue;
  int neighbors=0;
  for(int dc=-1;dc<=1;dc++)for(int dr=-1;dr<=1;dr++){
   if(dc==0 && dr==0)continue;
   int cc=(c+dc+n)%n,rr=(r+dr+3)%3;
   neighbors+=((x>>(3*cc+rr))&1U);
  }
  if(neighbors==2)y|=uint32_t(1)<<p;
 }
 return y;
}
int main(){
 for(int n=3;n<=6;n++){
  uint64_t total=uint64_t(1)<<(3*n);
  array<uint64_t,5> exact{};
  for(uint32_t x=0;x<total;x++){
   uint32_t y=x;int t=0;
   while(y && t<=4){y=advance(y,n);++t;}
   assert(y==0 && t<=4);
   ++exact[t];
  }
  int max_t=4;
  while(max_t>0 && exact[max_t]==0)--max_t;
  assert(max_t==(n==3?2:(n==4?3:4)));
  cout<<"n="<<n<<" states="<<total<<" extinction_histogram=";
  for(int t=0;t<=4;t++)cout<<(t?",":"")<<exact[t];
  cout<<" sharp="<<max_t<<"\n";
 }
 cout<<"BINARY_REPLAY_PASS\n";
}
