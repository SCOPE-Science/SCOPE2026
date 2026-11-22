// Independent enumeration using cyclic phase indices, instead of iterating a successor array.
// C++17; g++ -std=c++17 -O2 check_phase.cpp -o check_phase && ./check_phase
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
#include <stdexcept>
using namespace std;
int main(){
  const int p=11;array<int,10> a; iota(a.begin(),a.end(),1);
  vector<uint64_t> six,seven;six.reserve(3628800);seven.reserve(3628800);
  do {
    int orbit[11];orbit[0]=0;
    for(int j=0;j<10;j++)orbit[j+1]=a[j];
    int phase[11];for(int j=0;j<p;j++)phase[orbit[j]]=j;
    uint64_t s=0;
    for(int t=1;t<=7;t++){
      for(int x=1;x<=9;x++){
        int y=orbit[(phase[x]+t)%p];
        s=s*2+(y>x);
      }
      if(t==6)six.push_back(s);
    }
    seven.push_back(s);
  }while(next_permutation(a.begin(),a.end()));
  if(six.size()!=3628800||seven.size()!=3628800)throw runtime_error("bad enumeration");
  sort(six.begin(),six.end());sort(seven.begin(),seven.end());
  uint64_t hist1=0,hist2=0,hist4=0,other=0;
  for(size_t i=0;i<six.size();){size_t j=i+1;while(j<six.size()&&six[j]==six[i])j++;
    if(j-i==1)hist1++;else if(j-i==2)hist2++;else if(j-i==4)hist4++;else other++;i=j;
  }
  if(hist1!=3470400||hist2!=77760||hist4!=720||other!=0)
     throw runtime_error("phase six-step counts mismatch");
  if(adjacent_find(seven.begin(),seven.end())!=seven.end())
     throw runtime_error("phase seven-step collision");
  cout<<"PHASE CERTIFICATE PASS: p=11; 6-step fibers {1:"<<hist1<<",2:"<<hist2
    <<",4:"<<hist4<<"}; all 3628800 seven-step fingerprints distinct\n";
}
