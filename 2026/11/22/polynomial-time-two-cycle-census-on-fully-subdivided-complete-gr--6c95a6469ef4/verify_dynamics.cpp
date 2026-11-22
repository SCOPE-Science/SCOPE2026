// Independent full chip-state enumeration, using update dynamics rather than cut weights.
// Build: c++ -O2 -std=c++17 verify_dynamics.cpp -o verify_dynamics
// Run: ./verify_dynamics
#include <vector>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;

uint64_t count_primitive_two_orbits(int n) {
    vector<pair<int,int>> edges;
    for (int a=0;a<n;a++) for (int b=a+1;b<n;b++) edges.push_back({a,b});
    int N=n+(int)edges.size();
    vector<vector<int>> neighbors(N);
    for (int e=0;e<(int)edges.size();e++) {
        int a=edges[e].first,b=edges[e].second,z=n+e;
        neighbors[a].push_back(z);neighbors[z].push_back(a);
        neighbors[b].push_back(z);neighbors[z].push_back(b);
    }
    vector<int> radix(N), degree(N);
    uint64_t total=1;
    for (int i=0;i<N;i++) {
        degree[i]=(int)neighbors[i].size();
        radix[i]=2*degree[i];total*=radix[i];
    }
    vector<int> x(N), y(N), z(N), firing(N), firing2(N);
    uint64_t states=0;
    for (uint64_t code=0;code<total;code++) {
        auto tmp=code;
        for (int i=0;i<N;i++){x[i]=tmp%radix[i];tmp/=radix[i];firing[i]=(x[i]>=degree[i]);}
        for (int i=0;i<N;i++) {
            int incoming=0;
            for(int j:neighbors[i])incoming+=firing[j];
            y[i]=x[i]-degree[i]*firing[i]+incoming;
            firing2[i]=(y[i]>=degree[i]);
        }
        bool nonfixed=false, return_to_start=true;
        for (int i=0;i<N;i++) {
            nonfixed |= (y[i]!=x[i]);
            int incoming=0;
            for(int j:neighbors[i])incoming+=firing2[j];
            z[i]=y[i]-degree[i]*firing2[i]+incoming;
            return_to_start &= (z[i]==x[i]);
        }
        if (nonfixed && return_to_start)states++;
    }
    assert((states%2)==0);
    cout << "n="<<n<<" enumerated_states="<<total<<" primitive_two_orbits="<<states/2<<"\n";
    return states/2;
}
int main() {
    assert(count_primitive_two_orbits(3)==100);
    assert(count_primitive_two_orbits(4)==12312);
    cout << "DYNAMICAL_CHECKS_PASSED\n";
}
