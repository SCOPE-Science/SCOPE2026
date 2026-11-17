// Independent direct vertex-level enumeration for four-state excitation on friendship graphs.
// Compile: g++ -O3 -std=c++17 full_state_census.cpp -o full_state_census
// Run: ./full_state_census
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

uint64_t powu(uint64_t a, int k){uint64_t r=1; while(k--)r*=a;return r;}

int main(){
 for(int k=1;k<=5;k++){
  const int n=2*k+1;
  uint64_t count[8]={};
  uint64_t total=powu(4,n);
  vector<unsigned char> cur(n),next(n);
  for(uint64_t code=0;code<total;code++){
   uint64_t word=code;
   for(int j=0;j<n;j++){cur[j]=word%4;word/=4;}
   int time=0;
   while(true){
    bool allrest=true;for(auto x:cur)if(x){allrest=false;break;}
    if(allrest)break;
    assert(time<7);
    bool hubexcited=false;
    for(int j=1;j<n;j++) hubexcited |= (cur[j]==1);
    next[0] = cur[0] ? (cur[0]+1)%4 : hubexcited;
    for(int j=1;j<n;j++){
     int mate=(j%2)?j+1:j-1;
     next[j]=cur[j] ? (cur[j]+1)%4 : (cur[0]==1 || cur[mate]==1);
    }
    cur.swap(next);
    ++time;
   }
   assert(time<=7);
   count[time]++;
  }
  uint64_t expected[]={
    1,
    2*powu(4,k)-1,
    3*powu(9,k)-2*powu(4,k),
    2*powu(14,k)-powu(9,k),
    powu(16,k)-powu(9,k)+powu(6,k)-1,
    powu(16,k)-powu(14,k)+powu(12,k)-powu(6,k)-powu(5,k)+powu(3,k),
    powu(16,k)-powu(10,k)-powu(9,k)+powu(5,k)-powu(3,k)+1,
    powu(16,k)-powu(14,k)-powu(12,k)+powu(10,k)
  };
  uint64_t sum=0;
  cout<<"k="<<k<<" shells=";
  for(int i=0;i<8;i++){assert(count[i]==expected[i]);sum+=count[i];cout<<(i?",":"")<<count[i];}
  assert(sum==total);
  cout<<" checked="<<sum<<"\n";
 }
 cout<<"full_state_census: PASS\n";
}
