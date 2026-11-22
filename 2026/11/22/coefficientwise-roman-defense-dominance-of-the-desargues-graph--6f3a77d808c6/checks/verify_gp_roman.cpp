// Exact finite Roman-domination polynomial comparison for GP(10,2) and GP(10,3).
// Standard C++17. No third-party dependencies.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using ull=unsigned long long;
using Hist=array<array<ull,21>,21>;
using Poly=array<ull,41>;
struct Result{Poly poly{};Hist hist{};};
static Result enumerate(int n, int k){
    assert(n==10 && (k==2 || k==3));
    const int N=2*n;
    array<uint32_t,20> adj{};
    auto add=[&](int i,int j){assert(i!=j);adj[i]|=uint32_t(1)<<j;adj[j]|=uint32_t(1)<<i;};
    for(int i=0;i<n;++i){add(i,(i+1)%n);add(i,n+i);add(n+i,n+(i+k)%n);}
    for(uint32_t mask:adj)assert(__builtin_popcount(mask)==3);
    ull choose[21][21]{};
    for(int i=0;i<=20;++i){choose[i][0]=choose[i][i]=1;for(int j=1;j<i;++j)choose[i][j]=choose[i-1][j-1]+choose[i-1][j];}
    const uint32_t full=(uint32_t(1)<<20)-1;
    Result out;
    for(uint32_t B=0;B<=full;++B){
        uint32_t covered=B, remain=B;
        while(remain){uint32_t lsb=remain & (~remain+1);int i=__builtin_ctz(lsb);remain^=lsb;covered|=adj[i];}
        int twos=__builtin_popcount(B);
        int forced=20-__builtin_popcount(covered);
        int optional=__builtin_popcount(covered & ~B);
        assert(twos+forced+optional==20);
        ++out.hist[twos][forced];
        for(int j=0;j<=optional;++j){int weight=2*twos+forced+j;assert(weight<=40);out.poly[weight]+=choose[optional][j];}
    }
    return out;
}
int main(){
    auto P=enumerate(10,2),D=enumerate(10,3);
    // Coefficients of Q(z) in 4 z^12 (1+z)^6 Q(z), ascending degrees.
    constexpr array<ull,12> q={80,760,3025,6748,9712,9873,7427,4233,1825,580,125,15};
    ull choose6[7]={1,6,15,20,15,6,1};
    array<ull,41> expected{};
    for(int i=0;i<12;++i)for(int j=0;j<7;++j)expected[12+i+j]+=4*q[i]*choose6[j];
    ull countP=0,countD=0, numB_P=0,numB_D=0;
    for(int i=0;i<41;++i){
        countP+=P.poly[i];countD+=D.poly[i];
        assert(D.poly[i]>=P.poly[i]);
        assert(D.poly[i]-P.poly[i]==expected[i]);
        if(i<12)assert(P.poly[i]==0 && D.poly[i]==0);
        if(i>=12 && i<=29)assert(D.poly[i]>P.poly[i]);
        if(i>=30)assert(D.poly[i]==P.poly[i]);
    }
    for(int i=0;i<=20;++i)for(int j=0;j<=20;++j){numB_P+=P.hist[i][j];numB_D+=D.hist[i][j];}
    assert(numB_P==(1<<20) && numB_D==(1<<20));
    assert(P.poly[12]==20 && D.poly[12]==340);
    assert(countP==742721362ULL && countD==754088530ULL);
    cout << "PASS EXACT SUBSETS=" << numB_P << " EACH\n";
    cout << "PASS TOTALS=" << countP << " " << countD << " DIFFERENCE=" << countD-countP << "\n";
    cout << "PASS Q-FACTOR AND ALL 41 COEFFICIENTS\n";
    cout << "P ";for(auto x:P.poly)cout << x << ' ';cout << '\n';
    cout << "D ";for(auto x:D.poly)cout << x << ' ';cout << '\n';
    return 0;
}
