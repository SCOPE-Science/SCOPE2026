// Standard C++17 standalone direct-state verification of a finite rooted b-ary GHM.
// Build: c++ -O3 -std=c++17 verify_extremizers.cpp -o verify_extremizers
// Run:   ./verify_extremizers
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stdexcept>
using namespace std;
using u64=uint64_t;

static u64 ipow(u64 a,int n){u64 r=1;while(n--)r*=a;return r;}
static int nodes(int b,int h){int n=1,p=1;for(int i=0;i<h;i++){p*=b;n+=p;}return n;}
static u64 predicted(int b,int h){
 if(h<=1)return 1;
 int block=1; for(int i=0;i<h-2;i++)block*=b;
 u64 z=ipow(2,block);for(int i=0;i<(block-1)/(b-1);i++)z*=3;
 return z;
}
static bool check_case(int b,int h,bool fixed_leaves){
 int n=nodes(b,h),leaf=(n-1)/b,vars=fixed_leaves?leaf:n;
 u64 end=ipow(3,vars),seen=0;
 vector<uint8_t> cur(n),next(n);
 for(u64 q=0;q<end;q++){
  u64 x=q;
  for(int i=0;i<vars;i++){cur[i]=x%3;x/=3;}
  if(fixed_leaves)for(int i=leaf;i<n;i++)cur[i]=1;
  for(int t=0;t<h;t++){
   for(int v=0;v<n;v++){
    if(cur[v]){next[v]=(cur[v]==1?2:0);continue;}
    int ex=0;
    if(v)ex+=(cur[(v-1)/b]==1);
    for(int k=0;k<b;k++){
     int child=b*v+k+1;
     if(child<n)ex+=(cur[child]==1);
    }
    next[v]=(ex>=b?1:0);
   }
   cur.swap(next);
  }
  if(cur[0]==1)seen++;
 }
 u64 want=predicted(b,h);
 printf("b=%d h=%d mode=%s candidates=%llu root_excited_at_h=%llu predicted=%llu %s\n",
        b,h,fixed_leaves?"leaves-fixed":"all-states",
        (unsigned long long)end,(unsigned long long)seen,
        (unsigned long long)want,(seen==want?"PASS":"FAIL"));
 return seen==want;
}
int main(){
 bool ok=true;
 // All initial states; these tests independently check that all-leaf excitation is necessary.
 for(int b=2;b<=3;b++)for(int h=0;h<=2;h++)ok=check_case(b,h,false)&&ok;
 // A larger complete 15-vertex binary tree; all 3^15 states.
 ok=check_case(2,3,false)&&ok;
 // Sufficient-condition exhaustive checks (leaves=1), including height four.
 ok=check_case(2,4,true)&&ok;
 ok=check_case(3,3,true)&&ok;
 if(!ok){fprintf(stderr,"VERIFICATION FAILED\n");return 1;}
 printf("ALL DIRECT ENUMERATION CHECKS PASSED\n");
}
