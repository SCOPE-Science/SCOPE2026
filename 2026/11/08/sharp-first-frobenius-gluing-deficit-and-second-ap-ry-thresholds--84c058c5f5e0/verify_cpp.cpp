// Independent bounded-denumerant dynamic program for a family of 3-generator numerical semigroups.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    long long pairs=0, residue_checks=0, integers_checked=0, max_f1=0;
    for (int q=3; q<=36; ++q) for (int k=2; k<=36; ++k) {
        int a=q*k, b=a+1, c=a+q, d=min(q-1,k+1);
        long long f0=1LL*a*(k+q-2)-1;
        long long f1=1LL*a*(k+q-2+d)-1;
        long long n0=1LL*a*(k+q-2)/2;
        long long n1=n0+1LL*q*(k+1)+1LL*q*(k-1)*d;
        int limit=static_cast<int>(f1+a);
        vector<uint8_t> v(limit+1,0); v[0]=1;
        for (int coin: {a,b,c}) for (int x=coin;x<=limit;x++)
            v[x]=min(2,int(v[x])+int(v[x-coin]));
        long long tested_g0=-1,tested_g1=-1,tested_n0=0,tested_n1=0;
        for (long long x=0; x<=limit; ++x) {
            if (v[x]==0) {tested_g0=x; if(x<=f1) ++tested_n0;}
            if (v[x]<=1) {tested_g1=x; if(x<=f1) ++tested_n1;}
        }
        if(tested_g0!=f0 || tested_g1!=f1 || tested_n0!=n0 || tested_n1!=n1) {
          cerr << "FAIL invariant q="<<q<<" k="<<k<<" expected "<<f0<<","<<f1<<","<<n0<<","<<n1<<" observed "<<tested_g0<<","<<tested_g1<<","<<tested_n0<<","<<tested_n1<<"\n";
          return 1;
        }
        for(int r=0;r<a;r++) {
            int u=r/q, digit=r%q;
            int first=r+a*(u+digit);
            int second=first+a*(u==0?k+1:d);
            if(v[first]==0 || (first>=a && v[first-a]!=0) || v[second]<2 || v[second-a]>1) {
                cerr << "FAIL Apéry q="<<q<<" k="<<k<<" r="<<r<<"\n";return 2;
            }
            ++residue_checks;
        }
        ++pairs; integers_checked+=limit+1;max_f1=max(max_f1,f1);
    }
    cout << "PASS parameter_pairs="<<pairs<<" residue_threshold_checks="<<residue_checks
         <<" bounded_integer_counts="<<integers_checked<<" largest_f1="<<max_f1<<"\n";
}
