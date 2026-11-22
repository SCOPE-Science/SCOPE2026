// Independent direct graph enumeration for minimum paired domination in C5(1,1,1,a,b).
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

bool adj(int p, int q) { return p == q || (p+1)%5 == q || (q+1)%5 == p; }

bool pd(const vector<int>& fiber, const vector<int>& s) {
  for (int v=0;v<(int)fiber.size();v++) {
    bool seen=false;
    for (int u:s) if (adj(fiber[v],fiber[u])) {seen=true;break;}
    if (!seen) return false;
  }
  return (adj(fiber[s[0]],fiber[s[1]]) && adj(fiber[s[2]],fiber[s[3]])) ||
         (adj(fiber[s[0]],fiber[s[2]]) && adj(fiber[s[1]],fiber[s[3]])) ||
         (adj(fiber[s[0]],fiber[s[3]]) && adj(fiber[s[1]],fiber[s[2]]));
}

bool roles(const vector<int>& fiber, const vector<int>& s) {
  const int roleMask[] = {1, 6, 9, 10, 12};
  int p[] = {0,1,2,3};
  do {
    bool ok=true;
    for(int i=0;i<4;i++) if (!(roleMask[fiber[s[i]]] & (1<<p[i]))) {ok=false;break;}
    if(ok) return true;
  } while(next_permutation(p,p+4));
  return false;
}

int main(){
  long long tests=0;
  for(int a=1;a<=9;a++) for(int b=1;b<=9;b++) {
    vector<int> fiber={0,1,2};
    fiber.insert(fiber.end(),a,3);
    fiber.insert(fiber.end(),b,4);
    vector<uint64_t> bases;
    int n=fiber.size();
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++)
      for(int k=j+1;k<n;k++) for(int l=k+1;l<n;l++) {
        vector<int> s={i,j,k,l};
        bool g=pd(fiber,s), t=roles(fiber,s);
        assert(g==t);
        tests++;
        if(g) bases.push_back((1ULL<<i)|(1ULL<<j)|(1ULL<<k)|(1ULL<<l));
      }
    long long expectation=1LL*a*a*b+1LL*a*b*b+a*a+a*b+b*b;
    assert((long long)bases.size()==expectation);
    if(a==5 && b==5) {
      unordered_set<uint64_t> B(bases.begin(),bases.end());
      for(uint64_t s:bases)for(uint64_t t:bases){
        uint64_t remove=s&~t, add=t&~s;
        for(uint64_t rem=remove;rem;rem&=(rem-1)){
          uint64_t x=rem&-rem; bool found=false;
          for(uint64_t ins=add;ins;ins&=(ins-1)) {
            uint64_t y=ins&-ins;
            if(B.count((s^x)|y)) {found=true;break;}
          }
          assert(found);
        }
      }
    }
  }
  cout<<"PASS: "<<tests<<" direct tests of graph and role matching, 81 parameter pairs\n";
  cout<<"PASS: all counted four-subsets match the polynomial\n";
  cout<<"PASS: complete strong basis-exchange test at a=b=5\n";
}
