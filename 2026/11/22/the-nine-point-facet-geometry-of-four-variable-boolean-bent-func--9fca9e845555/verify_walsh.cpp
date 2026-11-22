// Independent truth-table/Walsh verification. C++17, standard library only.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  vector<uint16_t> bent;
  for (uint32_t f=0; f<65536; ++f) {
    int walsh[16];
    for (int x=0; x<16; ++x) walsh[x]=((f>>x)&1)?-1:1;
    for (int step=1;step<16;step*=2)
      for (int base=0;base<16;base+=2*step)
        for(int i=0;i<step;++i){
          int a=walsh[base+i], b=walsh[base+i+step];
          walsh[base+i]=a+b; walsh[base+i+step]=a-b;
        }
    bool ok=true;
    for(int i=0;i<16;++i)if(walsh[i]!=4 && walsh[i]!=-4)ok=false;
    if(ok)bent.push_back(static_cast<uint16_t>(f));
  }
  assert(bent.size()==896);
  int weight6=0,weight10=0;
  vector<uint16_t> ten;
  for(auto f:bent){
    int k=__builtin_popcount(static_cast<unsigned>(f));
    if(k==6)++weight6; else if(k==10){++weight10; ten.push_back(f);}else assert(false);
  }
  assert(weight6==448 && weight10==448);
  array<uint8_t,65536> proper{};
  for (auto b:ten) {
    uint32_t s=(b-1u)&b;
    while(true){ proper[s]=1; if(s==0)break; s=(s-1u)&b; }
  }
  long long counts[17]={}, misses[17]={};
  for(uint32_t s=0;s<65536;++s){
    int xlist[16],k=0;
    for(int x=0;x<16;++x)if(s>>x&1)xlist[k++]=x;
    bool shatter=false;
    if(k<=9){
      uint8_t seen[512]={};
      int distinct=0;
      for(uint16_t f:bent){
        int trace=0;
        for(int j=0;j<k;++j)trace|=((f>>xlist[j])&1)<<j;
        if(!seen[trace]){seen[trace]=1; ++distinct;}
        if(distinct==(1<<k)){shatter=true;break;}
      }
    }
    assert(shatter==bool(proper[s]));
    if(shatter)++counts[k];else ++misses[k];
  }
  constexpr long long expected[10]={1,16,120,560,1820,4368,8008,11200,10080,4480};
  for(int k=0;k<10;++k)assert(counts[k]==expected[k]);
  for(int k=10;k<17;++k)assert(counts[k]==0);
  // The complete shattering complex is pure: every face lies below a nine-face.
  for(uint32_t s=0;s<65536;++s){
    if(!proper[s])continue;
    bool extends=false;
    for(auto b:ten){
      if((s&b)==s && s!=b){extends=true;break;}
    }
    assert(extends);
  }
  cout<<"INDEPENDENT_WALSH_TRACE_ENUMERATION_PASS\n";
}
