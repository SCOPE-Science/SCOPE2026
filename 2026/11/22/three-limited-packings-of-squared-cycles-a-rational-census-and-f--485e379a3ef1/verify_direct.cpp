// A direct vertex-mask checker, independent of the transfer recurrence.
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int main(){
 for(int n=5;n<=18;++n){
   vector<unsigned long long> ans(n+1,0);
   for(uint64_t s=0;s<(uint64_t(1)<<n);++s){
     bool feasible=true;
     for(int i=0;i<n && feasible;++i){
       int local=0;
       for(int d=-2;d<=2;++d){
         int j=(i+d+n)%n;
         local+=int((s>>j)&1ULL);
       }
       if(local>3)feasible=false;
     }
     if(feasible)++ans[__builtin_popcountll(s)];
   }
   cout << "n=" << n;
   for(auto x:ans)cout << ' ' << x;
   cout << '\n';
 }
}
