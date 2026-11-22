// Exact independent orbit test of every coordinate-invariant code for 3<=n<=14.
// Compile: g++ -std=c++17 -O2 independent.cpp -o independent && ./independent
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
static int weight(unsigned z){return __builtin_popcount(z);}
static set<unsigned> ball(unsigned x,int n){
    set<unsigned> a; a.insert(x);
    for(int i=0;i<n;i++) a.insert(x^(1u<<i));
    return a;
}
int main(){
    const int bests[]={0,0,0,4,8,10,22,44,86,172,344,682,1366,2732,5462};
    const int counts[]={0,0,0,2,2,1,2,1,1,2,1,1,2,1,1};
    for(int n=3;n<=14;n++){
        set<unsigned> obstacles;
        for(int k=0;k<=n;k++){
            unsigned b=0;
            for(int t=max(0,k-1);t<=min(n,k+1);t++) b|=1u<<t;
            obstacles.insert(b); // domination of one entire weight layer
        }
        for(int common=0;common<=n;common++){
          for(int a=0;a<=n-common;a++)for(int b=0;b<=n-common-a;b++){
            if(a+b==0)continue;
            unsigned x=(1u<<(common+a))-1;
            unsigned y=((1u<<common)-1)|(((1u<<b)-1)<<(common+a));
            auto nx=ball(x,n), ny=ball(y,n);
            unsigned distinguish=0;
            for(unsigned z:nx)if(!ny.count(z))distinguish|=1u<<weight(z);
            for(unsigned z:ny)if(!nx.count(z))distinguish|=1u<<weight(z);
            assert(distinguish);
            obstacles.insert(distinguish);
          }
        }
        int best=1000000000,count=0;
        for(unsigned profile=0;profile<(1u<<(n+1));profile++){
            int cost=0;
            for(int k=0;k<=n;k++)if(profile&(1u<<k)){
                long long c=1;
                for(int i=1;i<=k;i++)c=c*(n-i+1)/i;
                cost+=(int)c;
            }
            if(cost>best)continue;
            bool valid=true;
            for(unsigned dis:obstacles)if(!(dis&profile)){valid=false;break;}
            if(valid){if(cost<best){best=cost;count=0;} count++;}
        }
        assert(best==bests[n]&&count==counts[n]);
        cout<<"n="<<n<<" minimum="<<best<<" optimal_profiles="<<count
            <<" distinct_orbit_constraints="<<obstacles.size()<<"\n";
    }
    cout<<"ALTERNATE_OK\n";
}
