// Exact finite-state enumeration for binary digit-sum shift extremal densities.
// Standard C++17, no external libraries. Compile: g++ -O2 -std=c++17 verify_extrema.cpp -o verify_extrema
// Execute: ./verify_extrema
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using U = unsigned __int128;

string dec(U x) {
    if (!x) return "0";
    string s;
    while (x) { s.push_back(char('0'+x%10)); x/=10; }
    reverse(s.begin(),s.end());
    return s;
}

// The two states distinguish outgoing carry 0 and 1. Entry j counts
// the 0/1 input prefixes giving exactly j carries; prefixes are equiprobable.
// The final geometric carry tail is integrated out algebraically.
// Return the numerator of the density with shared denominator 2^(k*k+k+1).
U scaled_density(const vector<int>& gaps, int k) {
    int p=0;
    U t=1;
    for (int gap:gaps) {p+=gap;t|=U(1)<<p;}
    const int L=p+1;
    U a[10]={}, b[10]={};
    a[0]=1;
    for (int i=0;i<L;i++) {
        U x[10]={}, y[10]={};
        if ((t>>i)&1) {
            for (int j=0;j<=k;j++) {
                x[j]+=a[j];
                if(j<k)y[j+1]+=a[j]+2*b[j];
            }
        } else {
            for (int j=0;j<=k;j++) {
                x[j]+=2*a[j]+b[j];
                if(j<k)y[j+1]+=b[j];
            }
        }
        copy(x,x+10,a);copy(y,y+10,b);
    }
    U numerator=0;
    for (int j=0;j<=k;j++) {
        numerator+=(a[j]<<(k+1));
        numerator+=b[j]*((U(1)<<(k+1))-(U(1)<<j));
    }
    int exponent=k*k+k+1;
    int local_exponent=L+k+1;
    if (local_exponent>exponent) throw logic_error("bad exponent");
    return numerator <<(exponent-local_exponent);
}

U integer_from_gaps(const vector<int>& gaps) {
    U n=1;
    int p=0;
    for(int x:gaps){p+=x;n|=U(1)<<p;}
    return n;
}

int main() {
    struct Expected {U numerator,denominator; vector<U> integers;};
    const vector<Expected> expected={
      {3,4,{1}}, {5,8,{5}}, {19,32,{11,13}}, {73,128,{27}},
      {9,16,{107}}, {567,1024,{219}}, {2239,4096,{439,475}},
      {8839,16384,{951}}
    };
    for (int k=1;k<=8;k++) {
        int m=k-1;
        int base=k+1;
        uint64_t count=1;
        for(int j=0;j<m;j++)count*=base;
        U optimum=~U(0);
        vector<U> minimizers;
        for(uint64_t idx=0;idx<count;idx++) {
            uint64_t u=idx;
            vector<int> gaps(m);
            for (int j=0;j<m;j++) {gaps[j]=1+(u%base);u/=base;}
            U val=scaled_density(gaps,k);
            if(val<optimum){optimum=val;minimizers.clear();}
            if(val==optimum)minimizers.push_back(integer_from_gaps(gaps));
        }
        sort(minimizers.begin(),minimizers.end());
        U P=optimum,Q=U(1)<<(k*k+k+1);
        while(P%2==0 && Q%2==0){P/=2;Q/=2;}
        if (P!=expected[k-1].numerator || Q!=expected[k-1].denominator || minimizers!=expected[k-1].integers)
            throw runtime_error("exact minimum or minimizer mismatch");
        cout<<"k="<<k<<" candidates="<<count<<" c_min="<<dec(P)<<"/"<<dec(Q)<<" minimizers=";
        for(size_t i=0;i<minimizers.size();i++){if(i)cout<<',';cout<<dec(minimizers[i]);}
        cout<<" PASS\n";
    }
    cout<<"VERIFY_OK all_4782969_weight8_patterns=yes exact_integer_arithmetic=yes\n";
}
