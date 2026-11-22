#include <iostream>
#include <array>
#include <cstdint>
#include <vector>
#include <cassert>
using namespace std;
constexpr int V=14, N=4782969, MASK=(1<<14)-1;
int main(){
  // Dual Fano coordinates: lines k incident with points k,k+1,k+3 modulo 7.
  array<unsigned, V> adjacent{};
  for(int p=0;p<7;p++)for(int k=0;k<7;k++) {
    int d=(p+7-k)%7;
    if(d!=0 && d!=1 && d!=3){adjacent[p] |=1u<<(7+k);adjacent[7+k] |=1u<<p;}
  }
  for(int p=0;p<V;p++)assert(__builtin_popcount(adjacent[p])==4);
  long long freq[9]={};int witness=-1; bool bad=false;
  for(int initial=0;initial<N;initial++){
    int number=initial;unsigned exc=0,ref=0;
    for(int v=0;v<V;v++){
      int value=number%3;number/=3;
      if(value==1)exc|=1u<<v;
      else if(value==2)ref|=1u<<v;
    }
    if(exc==0 && ref==0){freq[0]++;continue;}
    bool stopped=false;
    for(int time=1;time<=8;time++){
      unsigned soon=0;
      for(int v=0;v<V;v++){
        if((exc|ref)&(1u<<v)) continue;
        if(__builtin_popcount(adjacent[v]&exc)>=2)soon|=1u<<v;
      }
      ref=exc;exc=soon;
      if(exc==0 && ref==0){freq[time]++;if(time==7 && witness<0)witness=initial;stopped=true;break;}
    }
    if(!stopped){bad=true;cerr<<"FAILED "<<initial<<"\n";break;}
  }
  if(bad)return 1;
  cout<<"FREQUENCY";for(int t=0;t<=8;t++)cout<<" "<<t<<":"<<freq[t];cout<<"\n";
  cout<<"SHARP_WITNESS "<<witness<<"\n";
  if(witness>=0){int z=witness;cout<<"WITNESS_TERNARY ";for(int i=0;i<V;i++){cout<<z%3;z/=3;}cout<<"\n";}
}
