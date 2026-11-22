// Independent direct enumeration of closed-neighborhood 2-limited packing colorings.
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
long long count_valid(int n,int k){
  long long ans=0,lim=1;
  for(int i=0;i<2*n;i++)lim*=k;
  vector<int> color(2*n);
  for(long long code=0;code<lim;code++){
    long long v=code;
    for(int i=0;i<2*n;i++){color[i]=v%k; v/=k;}
    bool good=true;
    for(int i=0;i<n&&good;i++) for(int r=0;r<2;r++) {
      int c[4]={color[2*i+r],color[2*i+1-r],color[2*((i+n-1)%n)+r],color[2*((i+1)%n)+r]};
      int cnt[3]={0,0,0}; for(int j:c)cnt[j]++;
      for(int p=0;p<k;p++) if(cnt[p]>2)good=false;
      if(!good)break;
    }
    ans+=good;
  }
  return ans;
}
int main(){
 const long long known[]={0,0,90,702,2430,11346,56574};
 for(int n=3;n<=7;n++){
   long long v=count_valid(n,3);
   assert(v==known[n-1]);
 }
 for(int n=3;n<=10;n++){
   long long v=count_valid(n,2);
   long long expected=n%4==0?6:n%2==0?2:0;
   assert(v==expected);
 }
 cout<<"PRISM_2LP_BRUTE_OK (n=3..7; 2 colors n=3..10)"<<endl;
}
