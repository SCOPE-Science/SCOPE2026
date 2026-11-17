// Independent direct two-phase BML state enumeration on labelled 2-by-n cyclic grids.
// 0=empty, 1=eastbound, 2=northbound. First east phase, then north phase.
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
  const uint64_t wanted[]={0,0,0,148,777,4097,21620,114107};
  for(int n=3;n<=7;n++){
    uint64_t count=0, mixed=0, vacant=0, mixedvac=0, total=1;
    for(int k=0;k<2*n;k++)total*=3;
    vector<int> a(2*n),b(2*n),c(2*n);
    for(uint64_t id=0;id<total;id++){
      uint64_t q=id; bool hasE=false,hasN=false,has0=false;
      for(int i=0;i<2*n;i++){
        a[i]=int(q%3);q/=3;
        has0|=a[i]==0;hasE|=a[i]==1;hasN|=a[i]==2;
      }
      b=a;
      for(int i=0;i<2*n;i++) if(a[i]==1 && a[(i/n)*n+(i%n+1)%n]==0){
        b[i]=0;b[(i/n)*n+(i%n+1)%n]=1;
      }
      c=b;
      for(int i=0;i<2*n;i++)if(b[i]==2 && b[(i+n)%(2*n)]==0){
        c[i]=0;c[(i+n)%(2*n)]=2;
      }
      if(c==a){count++; mixed+=hasE&&hasN;vacant+=has0;mixedvac+=has0&&hasE&&hasN;}
    }
    cout<<"n="<<n<<" frozen="<<count<<" mixed="<<mixed<<" vacant="<<vacant<<" mixed_vacant="<<mixedvac<<"\n";
    if(count!=wanted[n] || mixed!=count-(1ULL<<n)-3 || vacant!=count-(1ULL<<(2*n)) || mixedvac!=count-(1ULL<<(2*n))-(1ULL<<n)-1)return 1;
  }
  cout<<"all exhaustive checks passed\n";
}
