// Independent linear-algebra verification of all-on Lights Out spectra on GP(n,3).
// C++17. No external libraries. The variables are u_0,...,u_(n-1),v_0,...,v_(n-1).
#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;

using B = bitset<256>;

map<int,int> tab(int g) {
    switch (g) {
        case 1: return {{1,2}};
        case 2: return {{2,4}};
        case 4: return {{2,4},{4,8},{6,4}};
        case 5: return {{3,10},{5,12},{7,10}};
        case 10: return {{6,10},{10,44},{14,10}};
        case 20: return {{10,4},{12,10},{18,60},{20,108},
                         {22,60},{28,10},{30,4}};
        default: throw runtime_error("unexpected divisor");
    }
}

vector<B> system_matrix(int n, int step=3) {
    const int m=2*n;
    assert(m<255);
    vector<B> R(m);
    auto add = [&](int row, int col){ R[row].set(col); };
    auto idx = [&](int i){ return (i%n+n)%n; };
    for(int i=0;i<n;i++) {
        // Press effects on the outer vertices.
        add(i,idx(i-1)); add(i,i); add(i,idx(i+1)); add(i,n+i);
        // Press effects on the inner vertices.
        add(n+i,i); add(n+i,n+idx(i-step)); add(n+i,n+i); add(n+i,n+idx(i+step));
        R[i].set(m); R[n+i].set(m);
    }
    return R;
}

map<int,int> rref_count(int n, int step=3) {
    int m=2*n;
    vector<B> R = system_matrix(n,step);
    vector<int> pivots;
    int row=0;
    for(int col=0; col<m; ++col) {
        int pivot=row;
        while(pivot<m && !R[pivot][col]) pivot++;
        if(pivot==m) continue;
        swap(R[row],R[pivot]);
        for(int j=0;j<m;++j) if(j!=row && R[j][col]) R[j]^=R[row];
        pivots.push_back(col); ++row;
    }
    for(int j=row;j<m;j++) assert(!R[j][m]);
    vector<int> freecols;
    for(int j=0;j<m;j++) if(find(pivots.begin(),pivots.end(),j)==pivots.end())
        freecols.push_back(j);
    assert(freecols.size()<=8);
    map<int,int> hist;
    for(int mask=0;mask<(1<<freecols.size());mask++) {
        B sol;
        for(int i=0;i<(int)freecols.size();i++) if((mask>>i)&1) sol.set(freecols[i]);
        for(int i=0;i<row;i++) {
            bool v=R[i][m];
            for(int j:freecols) if(R[i][j] && sol[j]) v=!v;
            if(v) sol.set(pivots[i]);
        }
        // Verify original equations, not only the reduced system.
        vector<B> O=system_matrix(n,step);
        for(int i=0;i<m;i++) {
            B lhs=O[i]&sol; lhs.reset(m);
            assert(lhs.count()%2 == 1);
        }
        hist[(int)sol.count()]++;
    }
    return hist;
}

map<int,int> brute_count(int n, int step=3) {
    const int m=2*n;
    vector<B> R=system_matrix(n,step);
    map<int,int> hist;
    for(int bits=0;bits<(1<<m);bits++) {
        bool ok=true;
        for(int i=0;i<m && ok;i++) {
            int parity=0;
            for(int col=0;col<m;col++) if(R[i][col] && ((bits>>col)&1)) parity^=1;
            ok=(parity==1);
        }
        if(ok) hist[__builtin_popcount((unsigned)bits)]++;
    }
    return hist;
}

int main(){
    for(int n=7;n<=100;n++) {
        int g=gcd(n,20);
        map<int,int> predicted;
        for(auto [w,c]:tab(g)) predicted[w*(n/g)] = c;
        auto exact=rref_count(n);
        if(exact!=predicted) {
            cerr << "Mismatch at n=" << n << '\n';
            return 1;
        }
        if(n<=10) assert(brute_count(n)==predicted);
        auto step2=rref_count(n,2);
        int c2=0,c3=0;
        for(auto [weight,count]:step2) c2+=count;
        for(auto [weight,count]:exact) c3+=count;
        if(n%4==0) assert(c3==4*c2);
        else assert(exact==step2);
    }
    cout << "INDEPENDENT_GAUSS_PASS: all n=7..100; step-two comparison; brute force n=7..10" << '\n';
}
