// Reproduce the finite checks for independent-fibre zero forcing.
// Compile: g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

using U = uint32_t;

bool force_closure(const vector<U>& nb, U blue, bool skew) {
    const int n=(int)nb.size();
    const U all=(U(1)<<n)-1;
    U white=all^blue;
    while (white) {
        bool moved=false;
        for(int u=0;u<n;++u) {
            if(!skew && (white&(U(1)<<u))) continue;
            U cand=nb[u]&white;
            if(cand && !(cand&(cand-1))) {
                white ^=cand;
                moved=true;
                break;
            }
        }
        if(!moved) break;
    }
    return white==0;
}

vector<U> base_graph(int n, unsigned long long bits) {
    vector<U> a(n,0); int j=0;
    for(int u=0;u<n;++u)for(int v=u+1;v<n;++v,++j)
      if((bits>>j)&1ull) {a[u]|=U(1)<<v;a[v]|=U(1)<<u;}
    return a;
}
vector<U> cycle(int n) {
    vector<U> a(n,0);
    for(int i=0;i<n;++i) {a[i]|=U(1)<<((i+1)%n);a[i]|=U(1)<<((i+n-1)%n);}
    return a;
}
vector<U> blowup(const vector<U>& a,int m) {
    int n=a.size(); vector<U> b(n*m,0);
    for(int i=0;i<n;++i)for(int k=0;k<m;++k)
      for(int j=0;j<n;++j)if(a[i]&(U(1)<<j))
        for(int t=0;t<m;++t)b[i*m+k]|=U(1)<<(j*m+t);
    return b;
}
unsigned long long choose(int n,int k) {
    if(k<0||k>n) return 0;
    unsigned long long a=1;
    for(int i=1;i<=k;++i)a=a*(n-i+1)/i;
    return a;
}
unsigned long long power(int x,int p) {
    unsigned long long r=1;
    for(int i=0;i<p;++i)r*=x;
    return r;
}
// Exact exhaustive equivalence for every initial set; also checks the
// polynomial coefficients and inclusion-minimal conditions by direct deletion.
void audit_graph(const vector<U>& a,int m,bool cycle_case=false) {
    int n=a.size(),N=n*m;
    assert(N<=20);
    auto b=blowup(a,m);
    unsigned total=1u<<N, allmask=(1u<<m)-1;
    vector<char> skew_good(1u<<n,0),skew_min(1u<<n,0);
    for(U f=0;f<(U(1)<<n);++f) {
        skew_good[f]=force_closure(a,f,true);
        if(skew_good[f]) {
            bool min=true;
            for(int u=0;u<n;++u)if(f&(U(1)<<u))
                if(force_closure(a,f^(U(1)<<u),true)) {min=false;break;}
            skew_min[f]=min;
        }
    }
    vector<unsigned long long> counts(N+1,0),mins(N+1,0),expected(N+1,0),exmins(N+1,0);
    for(U s=0;s<total;++s) {
        U f=0;bool okay=true;
        for(int i=0;i<n;++i) {
            U part=(s>>(i*m))&allmask;
            int q=__builtin_popcount(part);
            if(q<m-1){okay=false;break;}
            if(q==m)f|=U(1)<<i;
        }
        bool pred=okay && skew_good[f];
        bool actual=force_closure(b,s,false);
        if(pred!=actual){cerr<<"FAIL_TRANSFER n="<<n<<" m="<<m<<" subset="<<s<<"\n";exit(1);}
        if(!actual)continue;
        int k=__builtin_popcount(s);counts[k]++;
        bool minimal=true;
        for(int u=0;u<N;++u)if((s&(U(1)<<u)) && force_closure(b,s^(U(1)<<u),false)) {minimal=false;break;}
        if(minimal) {
            mins[k]++;
            if(!(okay && skew_min[f])){cerr<<"FAIL_MIN_CLASS\n";exit(1);}
        } else if(okay&&skew_min[f]){cerr<<"FAIL_MIN_CONVERSE\n";exit(1);}
    }
    for(U f=0;f<(U(1)<<n);++f) {
        int k=n*(m-1)+__builtin_popcount(f);
        unsigned long long w=power(m,n-__builtin_popcount(f));
        if(skew_good[f])expected[k]+=w;
        if(skew_min[f])exmins[k]+=w;
    }
    if(counts!=expected || mins!=exmins){cerr<<"FAIL_POLYNOMIAL n="<<n<<" m="<<m<<"\n";exit(1);}
    if(cycle_case){
        vector<unsigned long long> ec(N+1),em(N+1);
        int h=n/2;
        for(int t=0;t<=n;++t){
            unsigned long long c=(n%2) ? choose(n,t)-(t==0) : (choose(n,t)-2*choose(h,t)+(t==0));
            ec[n*(m-1)+t]=c*power(m,n-t);
        }
        int z=n*(m-1)+(n%2?1:2);
        em[z]=(n%2 ? (unsigned long long)n : (unsigned long long)h*h)*power(m,n-(n%2?1:2));
        if(counts!=ec || mins!=em){cerr<<"FAIL_CYCLE_CLOSED_FORM n="<<n<<" m="<<m<<"\n";exit(1);}
        cout<<"CYCLE n="<<n<<" m="<<m<<" min="<<z<<" count="<<em[z]<<" OK\n";
    }
}
int main(){
    unsigned long long tested=0;
    for(int n=1;n<=4;++n){
      int edges=n*(n-1)/2;
      for(U g=0;g<(U(1)<<edges);++g){
        audit_graph(base_graph(n,g),2);
        ++tested;
        if(n<=3){audit_graph(base_graph(n,g),3);++tested;}
      }
    }
    // Every one of the 1024 labelled graphs on five vertices, double fibres.
    for(U g=0;g<1024;++g){audit_graph(base_graph(5,g),2);++tested;}
    cout<<"ALL_BASE_GRAPHS_AND_ALL_SUBSETS_OK instances="<<tested<<"\n";
    for(int n=5;n<=9;++n)audit_graph(cycle(n),2,true);
    for(int n=3;n<=5;++n)audit_graph(cycle(n),3,true);
    audit_graph(cycle(4),4,true);
    cout<<"TRANSFER_MINIMAL_AND_CYCLE_CERTIFICATES_OK\n";
}
