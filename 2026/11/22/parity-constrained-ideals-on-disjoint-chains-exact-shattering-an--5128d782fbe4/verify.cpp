// Exact finite cross-check using an independent base-(L+1) ideal enumerator.
#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <stdexcept>
#include <algorithm>
using namespace std;
static int choose(int n,int r) {
    if(r<0||r>n)return 0;
    int a=1;
    for(int i=1;i<=r;i++)a=a*(n-i+1)/i;
    return a;
}
static int power(int a,int n) {
    int x=1;while(n--)x*=a;return x;
}
static vector<int> get_masks(int k,int L,int p){
    vector<int> H;
    for(int t=0;t<power(L+1,k);t++) {
       int z=t,total=0,mask=0;
       for(int i=0;i<k;i++){
          int h=z%(L+1);z/=(L+1);total+=h;
          mask|=((1<<h)-1)<<(i*L);
       }
       if(total%2==p)H.push_back(mask);
    }
    return H;
}
static vector<int> count_shattered(int k,int L,int p){
    auto H=get_masks(k,L,p);
    vector<int> counts(k+1);
    int N=k*L;
    for(int S=0;S<(1<<N);S++){
        int q=__builtin_popcount((unsigned)S);
        if(q>k)continue;
        vector<int> traces;
        for(int h:H) traces.push_back(h&S);
        sort(traces.begin(),traces.end());
        auto end=unique(traces.begin(),traces.end());
        if(end-traces.begin()==(1<<q))counts[q]++;
    }
    return counts;
}
int main(){
    int cases=0;
    for(int L=2;L<=5;L++)
     for(int k=1;k<=3;k++)
      for(int p=0;p<=1;p++){
        auto got=count_shattered(k,L,p);
        vector<int> expect(k+1);
        for(int j=0;j<=k;j++)expect[j]=choose(k,j)*power(L,j);
        int missing=0;
        if(L%2==0){if(p==1)missing=1<<k;}
        else missing=1<<(k-1);
        expect[k]-=missing;
        if(got!=expect)throw runtime_error("mismatch");
        cout<<"L="<<L<<" k="<<k<<" p="<<p<<" f=";
        for(int a:got)cout<<" "<<a;
        cout<<"\n";cases++;
      }
    cout<<"PASS: "<<cases<<" independent C++ finite profiles\n";
}
