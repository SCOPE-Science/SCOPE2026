// Exact integer-polynomial Gray-code census of sign circulants for odd semiprime orders.
// No floating point or rank tolerance; independent of the margin-counting formulas.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
vector<ll> polynomial_quotient(vector<ll> a, const vector<ll>& b) {
    if (a.size()<b.size()) throw runtime_error("bad division");
    vector<ll> quotient(a.size()-b.size()+1);
    for (int i=(int)a.size()-(int)b.size();i>=0;--i) {
        ll factor=a[i+b.size()-1];
        if (factor) {
            quotient[i]=factor;
            for(int j=0;j<(int)b.size();j++) a[i+j]-=factor*b[j];
        }
    }
    for(auto v:a) if(v!=0) throw runtime_error("nonexact division");
    return quotient;
}
vector<ll> x_to_d_minus_one(int d) {vector<ll> a(d+1);a[0]=-1;a[d]=1;return a;}
vector<vector<ll>> cyclotomic_remainders(int n, int d, const vector<ll>& phi) {
    int degree=(int)phi.size()-1;
    vector<vector<ll>> col(n,vector<ll>(degree));
    for(int j=0;j<n;j++) {
        vector<ll> a(max(j+1,degree+1),0);
        a[j]=1;
        for(int k=(int)a.size()-1;k>=degree;--k) {
            ll fac=a[k];
            for(int t=0;t<=degree;t++) a[k-degree+t]-=fac*phi[t];
        }
        for(int t=0;t<degree;t++) col[j][t]=a[t];
    }
    return col;
}
int main(int argc,char**argv) {
    int p=argc>1?atoi(argv[1]):3,q=argc>2?atoi(argv[2]):5;
    if(p>=q || p<3 || p*q>21) {cerr<<"expect 3<=p<q and pq<=21\n";return 2;}
    int n=p*q;
    vector<int> divs={1,p,q,n};
    vector<vector<ll>> phis;
    for(int d:divs) {
        auto v=x_to_d_minus_one(d);
        for(int a:divs) if(a<d && d%a==0) {
            int k=find(divs.begin(),divs.end(),a)-divs.begin();
            v=polynomial_quotient(v,phis[k]);
        }
        phis.push_back(v);
    }
    vector<vector<vector<ll>>> rem;
    vector<vector<ll>> vals;
    for(size_t i=0;i<divs.size();i++) {
        rem.push_back(cyclotomic_remainders(n,divs[i],phis[i]));
        vals.push_back(vector<ll>(phis[i].size()-1));
        for(int j=0;j<n;j++)for(int t=0;t<(int)vals.back().size();t++)vals.back()[t]-=rem.back()[j][t];
    }
    map<int,ll> counts;
    vector<map<int,ll>> byweight(n+1);
    uint32_t prev=0;
    uint32_t limit=(1u<<n);
    for(uint32_t step=0;step<limit;step++) {
        uint32_t mask=step^(step>>1);
        if(step) {
            int bit=__builtin_ctz(step);
            ll delta=(mask&(1u<<bit))?2:-2;
            for(size_t k=0;k<divs.size();k++)
                for(int t=0;t<(int)vals[k].size();t++)vals[k][t]+=delta*rem[k][bit][t];
        }
        int rank=0;
        for(size_t k=0;k<divs.size();k++) {
            bool zero=true;
            for(ll c:vals[k])if(c) {zero=false;break;}
            if(!zero)rank+=(int)vals[k].size();
        }
        counts[rank]++;
        byweight[__builtin_popcount(mask)][rank]++;
        prev=mask;
    }
    cout<<"n="<<n<<" masks="<<limit<<" exact rank counts:";
    for(auto [rank,count]:counts)cout<<" "<<rank<<":"<<count;
    cout<<"\n";
    for(int k=0;k<=n;k++) {
        cout<<"weight "<<k<<": ";
        for(auto [rank,count]:byweight[k])cout<<rank<<"="<<count<<" ";
        cout<<"\n";
    }
}
