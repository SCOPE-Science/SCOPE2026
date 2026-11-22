// Exact exhaustive certificate for degree-minimal Borwein multiples of Lehmer's square.
// Compile: c++ -O2 -std=c++17 check.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using I = long long;
using V = vector<I>;
constexpr I g[21] = {1,2,1,-2,-4,-4,-3,-2,1,6,9,6,1,-2,-3,-4,-4,-2,1,2,1};
struct Case { int degree, sym; }; // 0 unrestricted, +1 reciprocal, -1 antireciprocal
using Solutions = set<V>;

bool valid(const V &h, int D, int sym) {
    const int e = D-20;
    if ((int)h.size() != e+1 || h[0] != 1 || (h[e]!=1 && h[e]!=-1)) return false;
    if (sym) for (int j=0;j<=e;j++) if (h[j] != sym*h[e-j]) return false;
    for (int k=0;k<=D;k++) {
        I c=0;
        for (int i=max(0,k-e);i<=min(20,k);i++) c+=g[i]*h[k-i];
        if (c < -1 || c > 1) return false;
    }
    return true;
}

void walk(int j, const Case &c, V &h, Solutions &out) {
    const int e=c.degree-20;
    const int last=c.sym ? e/2 : e;
    if (j>last) {
        if(c.sym) for (int i=last+1;i<=e;i++) h[i]=c.sym*h[e-i];
        if(valid(h,c.degree,c.sym))out.insert(h);
        return;
    }
    I sum=0;
    for(int i=1;i<=min(20,j);i++)sum+=g[i]*h[j-i];
    for(int digit=-1;digit<=1;digit++) {
        h[j]=digit-sum;  // select the actual coefficient of x^j in L^2 H
        walk(j+1,c,h,out);
    }
}
Solutions recursive(const Case &c) {
    V h(c.degree-19,0);h[0]=1;
    Solutions ans;walk(1,c,h,ans);return ans;
}

Solutions ternary_counter(const Case &c) {
    const int e=c.degree-20;
    const int last=c.sym ? e/2 : e;
    I trials=1;
    for(int j=1;j<=last;j++)trials*=3;
    Solutions ans;
    for(I z=0;z<trials;z++) {
        I t=z;
        V h(e+1,0);h[0]=1;
        for(int j=1;j<=last;j++) {
            const I digit=(t%3)-1;t/=3;
            I prev=0;
            for(int i=1;i<=min(20,j);i++)prev+=g[i]*h[j-i];
            h[j]=digit-prev;
        }
        if(c.sym)for(int j=last+1;j<=e;j++)h[j]=c.sym*h[e-j];
        if(valid(h,c.degree,c.sym))ans.insert(h);
    }
    return ans;
}

int main() {
    const vector<Case> cases={{34,0},{38,1},{41,-1}};
    const vector<size_t> expected={2,1,2};
    const vector<V> expected_h={
      {1,-3,4,-3,0,3,-4,3,-2,1,0,-1,2,-2,1},
      {1,-2,2,-1,0,1,-2,3,-4,3,0,-3,4,-3,1},
      {1,-2,2,0,-2,3,-2,1,0,0,0,1,-2,3,-2,0,2,-2,1},
      {1,-3,5,-5,3,0,-2,3,-3,3,-3,3,-3,3,-3,2,0,-3,5,-5,3,-1},
      {1,-2,3,-3,3,-2,1,1,-3,5,-6,6,-5,3,-1,-1,2,-3,3,-3,2,-1}
    };
    size_t index=0;
    for(size_t c=0;c<cases.size();c++) {
      const auto a=recursive(cases[c]), b=ternary_counter(cases[c]);
      if(a!=b || a.size()!=expected[c])throw runtime_error("exact census mismatch");
      for(const auto &v:a) {
        if(find(expected_h.begin(),expected_h.end(),v)==expected_h.end())
          throw runtime_error("unexpected extremizer");
        index++;
      }
      cout<<"degree="<<cases[c].degree<<" symmetry="<<cases[c].sym
          <<" normalized="<<a.size()<<" signed="<<2*a.size()<<" OK\n";
    }
    if(index!=5)throw runtime_error("missing extremizer");
    // Reciprocity orbit of degree-34 normalized solutions.
    V h=expected_h[0];reverse(h.begin(),h.end());
    if(h!=expected_h[1])throw runtime_error("reciprocal orbit mismatch");
    cout<<"TOTAL signed=10; degree-34 is a single reversal/sign orbit; VERIFIED\n";
}
