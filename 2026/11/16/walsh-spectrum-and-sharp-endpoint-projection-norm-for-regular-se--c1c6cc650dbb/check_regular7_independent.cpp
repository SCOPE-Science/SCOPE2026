// Independent exact direct character sums, using all 2^21 edge orientations.
// Compile: c++ -std=c++17 -O2 check_regular7_independent.cpp -o check7
// Execute from directory containing walsh_quotient.csv: ./check7
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main() {
    vector<pair<int,int>> edges;
    vector<int> free_index;
    for(int i=0;i<7;i++) for(int j=i+1;j<7;j++) {
        edges.push_back({i,j});
        if(i>0) free_index.push_back(int(edges.size())-1);
    }
    if(edges.size()!=21 || free_index.size()!=15) return 1;
    vector<int> supports;
    vector<int> ambient_vectors;
    // Independent enumeration in the *full* ambient edge cube,
    // rather than parity reconstruction from the free inner edges.
    for(int x=0;x<(1<<21);x++) {
        int degree[7]={};
        for(int k=0;k<21;k++) {
            auto [i,j]=edges[k];
            if((x>>k)&1) degree[i]++;
            else degree[j]++;
        }
        bool regular=true;
        for(int d:degree) if(d!=3){regular=false;break;}
        if(!regular) continue;
        int y=0;
        for(int k=0;k<15;k++) if((x>>free_index[k])&1) y|=(1<<k);
        supports.push_back(y);
        ambient_vectors.push_back(x);
    }
    if(supports.size()!=2640) return 2;
    sort(supports.begin(),supports.end());
    if(unique(supports.begin(),supports.end())!=supports.end()) return 3;
    ifstream input("walsh_quotient.csv");
    if(!input) return 4;
    string header;
    getline(input,header);
    if(header!="index,value") return 5;
    int nonzero=0,minval=1<<30,maxval=0;
    vector<int> spectrum(1<<15);
    long long squares=0;
    for(int u=0;u<(1<<15);u++) {
        int s=0;
        for(int y:supports) s += (__builtin_parity((unsigned)(u&y))?-1:1);
        string line;
        if(!getline(input,line)) return 6;
        stringstream ss(line);string a,b;
        if(!getline(ss,a,',') || !getline(ss,b,',')) return 7;
        if(stoi(a)!=u || stoi(b)!=s) {
            cerr<<"Mismatch at "<<u<<"\n";
            return 8;
        }
        spectrum[u]=s;
        if(s){nonzero++;minval=min(minval,abs(s));maxval=max(maxval,abs(s));}
        squares+=(long long)s*s;
    }
    string trailing;
    if(getline(input,trailing)) return 9;
    if(nonzero!=8656 || minval!=16 || maxval!=2640 || squares!=(1LL<<15)*2640) return 10;
    // Independently test the affine-lift sign formula at 256 ambient frequencies.
    int edgebit[7][7] = {};
    for(int k=0;k<21;k++) {
        auto [i,j]=edges[k]; edgebit[i][j]=k;
    }
    unsigned int state=0xC1200D27u;
    for(int sample=0;sample<256;sample++) {
        state^=state<<13;state^=state>>17;state^=state<<5;
        int xi=int(state&((1u<<21)-1));
        int eta=0,phase=0;
        for(int j=1;j<7;j++) {
            if(((xi>>edgebit[0][j])&1) && ((3-j)&1)) phase^=1;
        }
        for(int k=0;k<15;k++) {
            auto [i,j]=edges[free_index[k]];
            int coefficient=((xi>>free_index[k])&1) ^
                ((xi>>edgebit[0][i])&1) ^ ((xi>>edgebit[0][j])&1);
            eta|=(coefficient<<k);
        }
        int direct=0;
        for(int x:ambient_vectors) direct+=(__builtin_parity((unsigned)(x&xi))?-1:1);
        if(direct!=(phase?-spectrum[eta]:spectrum[eta])) {
            cerr<<"Affine lift mismatch at sample "<<sample<<"\n";
            return 11;
        }
    }
    cout<<"REGULAR7_WALSH_INDEPENDENT_DIRECT_PASS full_orientations=2097152 regular=2640 frequencies=32768 ambient_lift_samples=256"<<endl;
}
