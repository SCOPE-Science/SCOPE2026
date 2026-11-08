// Direct exhaustive check of initial two-periodicity for integer diffusion on K_{2,n}.
// Normalize the first hub to zero.  The edge-reversal lemma bounds each leaf
// label by n+1 in absolute value, and the second hub by 2(n+1).
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;

int sgn(int x) { return (x>0)-(x<0); }
void step(const vector<int>& x,vector<int>& y) {
    int n=(int)x.size()-2;
    int s0=0,s1=0;
    for(int j=2;j<n+2;j++){
        s0+=sgn(x[0]-x[j]);
        s1+=sgn(x[1]-x[j]);
    }
    y[0]=x[0]-s0; y[1]=x[1]-s1;
    for(int j=2;j<n+2;j++) y[j]=x[j]-sgn(x[j]-x[0])-sgn(x[j]-x[1]);
}
int main(){
   uint64_t cumulative=0;
   for(int n=1;n<=5;n++){
     int H=2*(n+1), L=n+1, base=2*L+1;
     uint64_t per_d_total=1;
     for(int k=0;k<n;k++) per_d_total*=base;
     vector<int>x(n+2),y(n+2),z(n+2); x[0]=0;
     vector<uint64_t> cnt(2*H+1,0);
     for(int d=-H;d<=H;d++){
        x[1]=d;
        for(uint64_t idx=0;idx<per_d_total;idx++){
          uint64_t j=idx;
          for(int k=0;k<n;k++){x[2+k]=int(j%base)-L;j/=base;}
          step(x,y); step(y,z);
          if(x==z)cnt[d+H]++;
        }
     }
     uint64_t sum=0;
     for(auto t:cnt)sum+=t;
     cumulative+=(2*H+1)*per_d_total;
     cout<<"n="<<n<<" states="<<(2*H+1)*per_d_total<<" two_periodic="<<sum<<" B0="<<cnt[H]<<" positive_gaps=";
     for(int d=1;d<=H;d++) if(cnt[d+H]) cout<<d<<":"<<cnt[d+H]<<",";
     cout<<"\n";
     for(int d=1;d<=H;d++) assert(cnt[H-d]==cnt[H+d]);
   }
   cout<<"exhaustively_tested="<<cumulative<<"\n";
}
