// Independent finite graph-subset check for maximal induced cluster graphs of triangular graphs.
// Build: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
using C=map<int,long long>;

C prediction(int n) {
    vector<C> dp(n+1); dp[0][0]=1;
    auto binom=[](int n,int k)->long long {
        long long v=1; for(int i=1;i<=k;i++)v=v*(n-i+1)/i; return v;
    };
    for(int j=1;j<=n;j++){
        for(int k=2;k<=j;k++) {
            int ed=(k==2?1:(k==3?3:k-1));
            long long ways=(k>=4?k:1)*binom(j-1,k-1);
            for(auto [s,c]:dp[j-k]) dp[j][s+ed]+=ways*c;
        }
    }
    C result=dp[n];
    if(n>=4 && (n-1)%3==0){
        int t=(n-1)/3;
        long long f=1,den=1;
        for(int i=1;i<=n;i++)f*=i;
        for(int i=1;i<=t;i++)den*=6*i;
        result[3*t]+=f/den;
    }
    return result;
}
int main(){
    long long examined=0, validtotal=0, maximal_total=0;
    for(int n=3;n<=7;n++){
        vector<pair<int,int>> E;
        for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)E.push_back({a,b});
        int N=E.size(),lim=1<<N;
        vector<U> closed(N);
        for(int i=0;i<N;i++)for(int j=0;j<N;j++){
            auto [a,b]=E[i];auto [c,d]=E[j];
            if(i==j||a==c||a==d||b==c||b==d)closed[i]|=U(1)<<j;
        }
        vector<uint8_t> iscluster(lim);
        for(int s=0;s<lim;s++){
            bool good=true;U left=s;
            while(left && good){
                int i=__builtin_ctz(left);
                U component=s&closed[i]; U todo=component;
                while(todo){
                    int j=__builtin_ctz(todo);todo&=todo-1;
                    if((s&closed[j])!=component){good=false;break;}
                }
                left &=~component;
            }
            if(good){iscluster[s]=1;validtotal++;}
        }
        C actual;
        for(int s=0;s<lim;s++)if(iscluster[s]) {
            bool maximal=true;
            for(int j=0;j<N;j++) if(!(s&(1<<j)) && iscluster[s|(1<<j)]){
                maximal=false;break;
            }
            if(maximal){actual[__builtin_popcount((unsigned)s)]++;maximal_total++;}
        }
        examined+=lim;
        if(actual!=prediction(n)){
            cerr<<"FAIL n="<<n<<"\n";return 1;
        }
        cout<<"n="<<n<<" ";for(auto [k,v]:actual)cout<<k<<":"<<v<<" ";cout<<"OK\n";
    }
    cout<<"VERIFY_OK exhaustive_orders=3..7 examined="<<examined
        <<" cluster_subsets="<<validtotal<<" maximal_sets="<<maximal_total
        <<" coefficient_comparison=PASS\n";
}
