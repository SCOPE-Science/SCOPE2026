// Exact independent backtracking and complete additive Fourier-zero count.
// Standard C++17; no external libraries or precomputed lists.
#include <array>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <iostream>
using V = std::array<int,5>;
std::vector<V> costs, all;
void recurse(V p, int depth, std::array<int,5> used) {
    if(depth==5) { costs.push_back(p); return; }
    for(int x=0;x<5;x++) if(!used[x]) {
        bool good=true;
        for(int d=1;d<=depth && good;d++) {
           int new_difference=x-p[depth-d];
           for(int i=0;i+d<depth;i++) if(p[i+d]-p[i]==new_difference) good=false;
        }
        if(good) {p[depth]=x;used[x]=1;recurse(p,depth+1,used);used[x]=0;}
    }
}
int mod5(int x) {int r=x%5;return r<0?r+5:r;}
V reduce(V k) {
 int shift=k[0];for(int &v:k)v=mod5(v-shift);
 int v=0;for(int x:k) if(x) {v=x;break;}
 if(v) {int inv=1;while(mod5(inv*v)!=1)inv++;for(int &x:k)x=mod5(x*inv);}
 return k;
}
std::array<int,5> counts(const std::vector<V>& data,const V &k) {
 std::array<int,5> out{};
 for(auto &p:data) {int s=0;for(int j=0;j<5;j++)s+=k[j]*p[j];out[mod5(s)]++;}
 return out;
}
bool zero(const std::array<int,5>&a) {
 for(int j=1;j<5;j++)if(a[j]!=a[0])return false;
 return true;
}
int main() {
 recurse(V{},0,std::array<int,5>{});
 V v={0,1,2,3,4};
 do {all.push_back(v);} while(std::next_permutation(v.begin(),v.end()));
 assert(costs.size()==40 && all.size()==120);
 std::set<V> classes, zc, zp;
 for(int a=0;a<3125;a++) {
    int b=a; V k{};
    for(int i=4;i>=0;i--) {k[i]=b%5; b/=5;}
    classes.insert(reduce(k));
    if(zero(counts(costs,k)))zc.insert(reduce(k));
    if(zero(counts(all,k)))zp.insert(reduce(k));
 }
 assert(classes.size()==157 && zc.size()==16 && zp.size()==125);
 int common=0;for(auto x:zc)if(zp.count(x))common++;
 assert(common==12);
 std::cout << "COSTAS5_INDEPENDENT_PASS " << costs.size() << " " << zc.size()
           << " " << zp.size() << " " << common << "\n";
 for(auto k:zc) {
   auto c=counts(costs,k);
   assert(c[0]==8 && c[1]==8 && c[2]==8 && c[3]==8 && c[4]==8);
 }
}
