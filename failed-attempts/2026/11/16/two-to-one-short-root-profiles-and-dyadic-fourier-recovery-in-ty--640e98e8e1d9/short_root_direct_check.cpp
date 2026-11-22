// Independent exact character-sum check for type-C short-root profiles.
// Build: c++ -O3 -std=c++17 short_root_direct_check.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
struct Root { vector<int> c; bool short_root; };

vector<Root> make_roots(int n) {
    vector<Root> roots;
    for(int i=0;i<n;++i) {
        for(int j=i+1;j<n;++j) {
            vector<int> minus(n,0), plus(n,0);
            for(int k=i;k<j;++k) minus[k]=plus[k]=1;
            for(int k=j;k<n-1;++k) plus[k]=2;
            plus[n-1]=1;
            roots.push_back({minus,true});
            roots.push_back({plus,true});
        }
        vector<int> twice(n,0);
        for(int k=i;k<n-1;++k) twice[k]=2;
        twice[n-1]=1;
        roots.push_back({twice,false});
    }
    sort(roots.begin(),roots.end(),[](const Root &a,const Root &b){
      int sa=0,sb=0;
      for(int x:a.c)sa+=x;
      for(int x:b.c)sb+=x;
      if(sa!=sb)return sa<sb;
      return a.c<b.c;
    });
    return roots;
}
bool leq(const vector<int>&a,const vector<int>&b) {
    for(size_t i=0;i<a.size();++i)if(a[i]>b[i])return false;
    return true;
}

int main() {
    const int expected_zero[]={0,0,0,18,0,126056};
    const int expected_min[]={0,0,2,4,2,4};
    for(int n=2;n<=5;++n) {
        auto roots=make_roots(n);
        int r=roots.size(); assert(r==n*n);
        vector<uint32_t> down(r,0); vector<int> sh;
        for(int i=0;i<r;++i) {
            for(int j=0;j<r;++j)if(leq(roots[j].c,roots[i].c))down[i]|=1u<<j;
            if(roots[i].short_root) sh.push_back(i);
        }
        set<uint32_t> ideals{0}; vector<uint32_t> stack{0};
        while(!stack.empty()) {
            uint32_t mask=stack.back(); stack.pop_back();
            for(int i=0;i<r;++i) {
                if(mask&(1u<<i))continue;
                if((mask&down[i])!=(down[i]^(1u<<i)))continue;
                uint32_t next=mask|(1u<<i);
                if(ideals.insert(next).second) stack.push_back(next);
            }
        }
        vector<uint32_t> profiles;
        for(uint32_t mask:ideals) {
            uint32_t p=0;
            for(int j=0;j<(int)sh.size();++j)if(mask&(1u<<sh[j]))p|=1u<<j;
            profiles.push_back(p);
        }
        int zeros=0,minimum=INT32_MAX;
        for(uint32_t k=0;k<(1u<<sh.size());++k) {
            int coefficient=0;
            for(uint32_t p:profiles)coefficient+= __builtin_parity(k&p) ? -1 : 1;
            if(coefficient==0) ++zeros;
            else minimum=min(minimum,abs(coefficient));
        }
        assert(zeros==expected_zero[n]);
        assert(minimum==expected_min[n]);
        cout<<"C"<<n<<" ideals="<<profiles.size()<<" zeros="<<zeros
            <<" min_nonzero="<<minimum<<"\n";
    }
    cout<<"SHORT_ROOT_DIRECT_CHARACTER_PASS\n";
}
