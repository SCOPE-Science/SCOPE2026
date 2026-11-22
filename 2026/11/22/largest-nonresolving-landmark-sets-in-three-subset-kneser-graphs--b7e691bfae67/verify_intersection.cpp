// Independent intersection-count verifier of resolving-threshold obstructions.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
static int dist(int n, unsigned a, unsigned b) {
    if(a==b) return 0;
    int r=__builtin_popcount(a&b);
    if(r==0) return 1;
    if(n==7) return r==2 ? 2 : 3;
    return 2;
}
static long long choose(int n,int k) {
    if(k<0||k>n) return 0;
    long long x=1;
    for(int i=1;i<=k;i++) x=x*(n-i+1)/i;
    return x;
}
int main(){
    for(int n=7;n<=11;n++){
        vector<unsigned> v;
        for(int a=0;a<n;a++) for(int b=a+1;b<n;b++) for(int c=b+1;c<n;c++)
            v.push_back((1u<<a)|(1u<<b)|(1u<<c));
        int N=v.size();
        map<int,map<int,int>> counts;
        map<string,int> bisector_witnesses;
        int least=N;
        for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){
            int r=__builtin_popcount(v[i]&v[j]);
            int distinguishing=0;
            string equal(N,'0');
            for(int w=0;w<N;w++){
                if(dist(n,v[i],v[w])!=dist(n,v[j],v[w])) distinguishing++;
                else equal[w]='1';
            }
            counts[r][distinguishing]++;
            least=min(least,distinguishing);
            bisector_witnesses[equal]++;
        }
        int maxeq=N-least, best=0;
        map<int,int> multiplicity;
        for(const auto& [s,k]:bisector_witnesses){
            if(count(s.begin(),s.end(),'1')==maxeq){best++;multiplicity[k]++;}
        }
        if(n==7) {assert(least==20 && best==21 && multiplicity[10]==21);}
        else {assert(least==2+2*choose(n-4,2)); assert(best==choose(n,2)*choose(n-2,2));assert(multiplicity[1]==best);}
        cout << "n="<<n<<" N="<<N<<" intersections=";
        for(auto [r,h]:counts){cout<<"("<<r<<":";for(auto [d,c]:h) cout<<d<<"="<<c<<",";cout<<")";}
        cout<<" min="<<least<<" threshold="<<N-least+1<<" largest="<<maxeq
            <<" distinct="<<best<<" multiplicities=";
        for(auto [k,vv]:multiplicity) cout<<k<<":"<<vv<<",";
        cout<<"\n";
    }
}
