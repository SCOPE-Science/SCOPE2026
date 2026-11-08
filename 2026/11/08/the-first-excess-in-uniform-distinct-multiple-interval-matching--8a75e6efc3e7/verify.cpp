// Exact finite-period check of interval-to-divisor matchings. Standard C++17.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
static uint64_t nbr[18][18], sets[18];
static int match_right[36];
static uint64_t seen;
static bool aug(int i) {
  uint64_t x=sets[i]&~seen;
  while(x){ int j=__builtin_ctzll(x); seen|=(1ULL<<j);
    if(match_right[j]==0 || aug(match_right[j])) { match_right[j]=i; return true; }
    x=sets[i]&~seen;
  }
  return false;
}
static bool matching_one(int n,int H) {
  fill(match_right,match_right+36,0);
  for(int i=n;i>=1;--i){seen=0; if(!aug(i))return false;}
  bool used[18]={};
  for(int j=1;j<=H;++j)if(match_right[j]) {
    if(used[match_right[j]]||!(sets[match_right[j]]&(1ULL<<j))) throw runtime_error("Invalid matching");
    used[match_right[j]]=true;
  }
  for(int i=1;i<=n;++i)if(!used[i])throw runtime_error("Unmatched left vertex");
  return true;
}
// Independent alternating-path BFS formulation, not using recursion/bit scanning.
static bool matching_two(int n,[[maybe_unused]] int H,int64_t m){
  int owner[36]={};
  for(int start=1;start<=n;start++){
    int q[36]={}, head=0,tail=0;
    int pred_left[18]={},pred_right[36]={};
    bool visited_left[18]={},visited_right[36]={};
    q[tail++]=start; visited_left[start]=true;
    int end=-1;
    while(head<tail&&end==-1){
      int i=q[head++];
      for(int j=1;j<=H;j++)if((m+j)%i==0&&!visited_right[j]){
        visited_right[j]=true;pred_right[j]=i;
        if(owner[j]==0){end=j;break;}
        int other=owner[j];
        if(!visited_left[other]){visited_left[other]=true;pred_left[other]=j;q[tail++]=other;}
      }
    }
    if(end==-1)return false;
    int j=end;
    while(j){int i=pred_right[j];owner[j]=i;j=pred_left[i];}
  }
  return true;
}
static int64_t period(int n){int64_t r=1;for(int i=1;i<=n;i++)r=lcm(r,(int64_t)i);return r;}
static void init(int n,int H){
  for(int i=1;i<=n;i++) for(int r=0;r<i;r++){
    uint64_t mask=0;
    for(int j=1;j<=H;j++)if((r+j)%i==0)mask|=1ULL<<j;
    nbr[i][r]=mask;
  }
}
static bool hall_witness(int n,[[maybe_unused]] int H,int64_t m){
  // Exhaustive Hall subset check, used only on exceptional starts.
  const unsigned count=1u<<n;
  vector<uint64_t> union_mask(count,0);
  for(unsigned s=1;s<count;s++){
    unsigned b=__builtin_ctz(s);unsigned t=s&(s-1);
    union_mask[s]=union_mask[t]|nbr[b+1][m%(b+1)];
    if(__builtin_popcountll(union_mask[s])<__builtin_popcount(s)) return true;
  }
  return false;
}
int main(int argc,char**argv){
  bool full_second=argc>1 && string(argv[1])=="--dual";
  uint64_t total_starts=0, bad32=0,first=0,all_bad_hash=14695981039346656037ULL;
  for(int n=2;n<=17;n++){
    const int64_t L=period(n);
    for(int H=2*n-2;H<=2*n-2+(n==17);H++){
      init(n,H);int64_t bad=0;
      for(int64_t m=0;m<L;m++){
        for(int i=1;i<=n;i++)sets[i]=nbr[i][m%i];
        bool ok=matching_one(n,H);
        if(full_second && (n<17 || m%997==0 || !ok) && matching_two(n,H,m)!=ok)throw runtime_error("Independent matching disagrees");
        if(!ok){
          if(n!=17 || H!=32)throw runtime_error("Unexpected failure");
          if(!hall_witness(n,H,m)) throw runtime_error("Failed matching without Hall obstruction");
          if(!bad)first=m;
          bad32++;
          all_bad_hash=(all_bad_hash^(uint64_t)m)*1099511628211ULL;
          bad++;
        }
        total_starts++;
      }
      cout<<"n="<<n<<" H="<<H<<" L="<<L<<" deficient="<<bad<<'\n';
      if(n<17 && bad)throw runtime_error("Small n contradicts claimed optimal length");
      if(n==17&&H==32&&bad!=32)throw runtime_error("Bad class count changed");
      if(n==17&&H==33&&bad!=0)throw runtime_error("Upper bound incorrect");
    }
  }
  if(first!=485749)throw runtime_error("First obstruction disagrees");
  cout<<"VERIFY_OK all_start_classes="<<total_starts<<" exceptional_32="<<bad32
      <<" first_exception="<<first<<" ordered_exceptions_checksum="<<all_bad_hash
      <<" dual_augmenting_paths="<<(full_second?"yes":"no")<<"\n";
}
