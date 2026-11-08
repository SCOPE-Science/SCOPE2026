// Standalone exact census of ternary synchronization parameters at lengths 1..28.
// ISO C++17. No external dependencies.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

struct Fraction { int a, b; };
bool lessF(Fraction x, Fraction y) { return (int64_t)x.a * y.b < (int64_t)y.a * x.b; }
bool equalF(Fraction x, Fraction y) { return (int64_t)x.a * y.b == (int64_t)y.a * x.b; }
Fraction normalized(Fraction x) { int g = gcd(x.a, x.b); return {x.a/g,x.b/g}; }

int lcs(const string &s, int i, int j, int k) {
    vector<int> prev(k-j+1,0), cur(k-j+1,0);
    for (int u=i;u<j;u++) {
        cur[0]=0;
        for (int v=j;v<k;v++)
            cur[v-j+1]=(s[u]==s[v]) ? prev[v-j]+1 : max(prev[v-j+1],cur[v-j]);
        swap(prev,cur);
    }
    return prev.back();
}

Fraction extensionMaximum(const string &s) {
    int k=s.size();
    Fraction b={0,1};
    for(int i=0;i<k-1;i++) for(int j=i+1;j<k;j++) {
        Fraction q={2*lcs(s,i,j,k),k-i};
        if(lessF(b,q))b=q;
    }
    return normalized(b);
}

bool squareFreeOnAppend(const string &s) {
    int n=s.size();
    for(int root=1;2*root<=n;root++) {
        if (equal(s.end()-root,s.end(),s.end()-2*root)) return false;
    }
    return true;
}

struct Level {
    unsigned long long all=0, optimal=0;
    Fraction beta={2,1};
    vector<string> witnesses;
};

int main() {
    vector<Level> R(29);
    string s;
    auto visit = [&](auto&& self, Fraction running) -> void {
        if(!s.empty()) {
            auto& L=R[s.size()];L.all++;
            if(lessF(running,L.beta)) {
                L.beta=running;L.optimal=1;L.witnesses={s};
            } else if(equalF(running,L.beta)) {
                L.optimal++;L.witnesses.push_back(s);
            }
        }
        if(s.size()==28)return;
        int used=0;
        for(char c:s)used=max(used, (int)(c-'0'+1));
        for(int c=0;c<3;c++) {
            if(c>used)continue; // first-occurrence normalization
            s.push_back((char)('0'+c));
            if(squareFreeOnAppend(s)) {
                Fraction f=extensionMaximum(s);
                if(lessF(running,f))self(self,f);
                else self(self,running);
            }
            s.pop_back();
        }
    };
    visit(visit,{0,1});
    for(int n=1;n<=28;n++) {
        auto &L=R[n];
        auto beta=normalized(L.beta);
        cout << n << ',' << L.all << ',' << beta.a << '/' << beta.b << ',' << L.optimal << '\n';

    }
    for (int n=27;n<=28;n++) for (auto &w:R[n].witnesses)
        cout << "EXTREMIZER," << n << ',' << w << '\n';
    // Invariant checks on the natural 27/28 breakpoint.
    assert(R[27].all==2581 && R[27].optimal==1 && equalF(R[27].beta,{20,23}));
    assert(R[28].all==3370 && R[28].optimal==13 && equalF(R[28].beta,{8,9}));
    assert(R[27].witnesses[0]=="012010212021012102010212012");
    cerr << "SYNC_TERNARY_CXX_VERIFY_OK" << '\n';
}
