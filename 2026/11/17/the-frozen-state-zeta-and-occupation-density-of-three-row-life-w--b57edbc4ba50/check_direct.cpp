// Independently enumerate the B3/S012345678 fixed points on three-row tori.
#include <cstdio>
#include <cstdint>
#include <vector>
int main(){
 for(int n=3;n<=7;n++){
   uint64_t fixed=0;
   std::vector<uint64_t> hist(3*n+1,0);
   const uint64_t bound=uint64_t(1)<<(3*n);
   for(uint64_t state=0;state<bound;state++){
     bool is_fixed=true;
     for(int c=0;c<n && is_fixed;c++)for(int r=0;r<3 && is_fixed;r++){
       if((state>>(3*c+r))&1)continue;
       int neighbors=0;
       for(int dx=-1;dx<=1;dx++)for(int dy=-1;dy<=1;dy++){
          if(dx==0 && dy==0)continue;
          int cc=(c+dx+n)%n,rr=(r+dy+3)%3;
          neighbors+=int((state>>(3*cc+rr))&1);
       }
       if(neighbors==3)is_fixed=false;
     }
     if(is_fixed){fixed++;hist[__builtin_popcountll(state)]++;}
   }
   printf("n=%d fixed=%llu histogram=",n,(unsigned long long)fixed);
   for(int k=0;k<=3*n;k++)printf("%s%llu",k?",":"",(unsigned long long)hist[k]);
   puts("");
 }
}
