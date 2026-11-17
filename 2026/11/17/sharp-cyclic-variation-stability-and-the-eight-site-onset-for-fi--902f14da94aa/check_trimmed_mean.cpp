// Exact verification of cyclic five-point one-extreme-per-side trimmed means.
// Build: g++ -O3 -std=c++17 check_trimmed_mean.cpp -o check_trimmed_mean
// Run: ./check_trimmed_mean
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static vector<int> output_counts(const vector<int>& x, const vector<int>& indicator) {
    const int n = (int)x.size();
    assert((int)indicator.size()==n && n>=5);
    vector<int> y(n);
    for(int i=0;i<n;i++){
        array<int,5> w{};
        for(int j=0;j<5;j++)w[j]=(i+j+n-2)%n;
        sort(w.begin(),w.end(),[&](int a,int b){return x[a]<x[b];});
        y[i]=indicator[w[1]]+indicator[w[2]]+indicator[w[3]];
    }
    return y;
}
static int cyclic_tv(const vector<int>& x){
    int total=0;
    for(int i=0;i<(int)x.size();i++)total+=abs(x[i]-x[(i+1)%x.size()]);
    return total;
}
static void check_local_overlap(){
    array<int,6> x{0,1,2,3,4,5};
    long long count=0;
    do {
        array<int,5> a{0,1,2,3,4}, b{1,2,3,4,5};
        sort(a.begin(),a.end(),[&](int i,int j){return x[i]<x[j];});
        sort(b.begin(),b.end(),[&](int i,int j){return x[i]<x[j];});
        int overlap=0;
        for(int i=1;i<4;i++)for(int j=1;j<4;j++)overlap+=(a[i]==b[j]);
        assert(overlap>=2);
        ++count;
    }while(next_permutation(x.begin(),x.end()));
    cout<<"ADJACENT_MIDDLE_TRIPLE_OVERLAP_PASS "<<count<<"\n";
}
static void exhaustive_small(){
    const int nums[]={0,3,3,4,4};
    const int dens[]={1,3,3,3,3};
    for(int n=5;n<=9;n++){
        vector<int> order(n);iota(order.begin(),order.end(),0);
        vector<int> tv(1<<(n-1));
        for(int mask=1;mask<(1<<(n-1));mask++){
            vector<int> b(n);
            for(int j=1;j<n;j++)b[j]=(mask>>(j-1))&1;
            tv[mask]=cyclic_tv(b);
        }
        int num=0,den=1;long long cases=0;
        do {
            int row_mask[9]{};
            for(int i=0;i<n;i++){
                array<int,5> w{};
                for(int j=0;j<5;j++)w[j]=(i+j+n-2)%n;
                sort(w.begin(),w.end(),[&](int a,int b){return order[a]<order[b];});
                row_mask[i]=(1<<w[1])|(1<<w[2])|(1<<w[3]);
            }
            for(int mask=1;mask<(1<<(n-1));mask++){
                const int bits=mask<<1;
                int y[9];
                for(int i=0;i<n;i++)y[i]=__builtin_popcount((unsigned)(bits&row_mask[i]));
                int v=abs(y[0]-y[n-1]);
                for(int i=1;i<n;i++)v+=abs(y[i]-y[i-1]);
                if(v*den>num*tv[mask]){num=v;den=tv[mask];}
                ++cases;
            }
        }while(next_permutation(order.begin(),order.end()));
        assert(num*dens[n-5]==3*nums[n-5]*den);
        cout<<"EXACT n="<<n<<" L="<<nums[n-5]<<"/"<<dens[n-5]
            <<" rank_cut_pairs="<<cases<<" PASS\n";
    }
}
static void sharp_witnesses(){
    vector<vector<int>> xs={
        {6,8,5,3,9,2,1,4,7,0},
        {4,1,5,0,3,10,6,8,9,7,2},
        {1,3,10,0,2,4,9,5,8,6,11,7},
        {9,10,2,7,11,12,3,4,6,8,1,5,0},
        {4,9,5,10,2,3,6,7,0,13,8,1,12,11}
    };
    for(int n=10;n<=80;n++){
        vector<int> x;
        if(n<=14)x=xs[n-10];
        else{
            x=xs[4];
            x.insert(x.begin()+11,n-14,0);
            for(int j=0;j<n-14;j++)x[11+j]=14+j;
        }
        vector<int>b(n,0);
        for(int i=2;i<=6;i++)b[i]=1;
        auto y=output_counts(x,b);
        assert(cyclic_tv(b)==2 && cyclic_tv(y)==10);
    }
    cout<<"EXACT_SHARP_WITNESSES_AND_PADDING n=10..80 PASS\n";
}
int main(){
    check_local_overlap();
    exhaustive_small();
    sharp_witnesses();
    cout<<"ALL_TRIMMED_MEAN_CHECKS_PASS\n";
}
