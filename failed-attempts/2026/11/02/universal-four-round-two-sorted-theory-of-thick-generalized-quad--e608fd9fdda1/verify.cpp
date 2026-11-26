// Exact finite-rank first-order types of four finite generalized quadrangles.
// A type at (k,r) is the atomic k-tuple diagram, together with the set
// of (k+1,r-1) types of its one-vertex extensions. This is the usual
// first-order back-and-forth recursion and handles all quantifier alternations.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

struct Geometry {
    int n = 0, np = 0;
    vector<vector<uint8_t>> edge;
};

Geometry read_geometry(const string& filename) {
    ifstream f(filename);
    if (!f) throw runtime_error("Cannot read " + filename);
    int n, np, m;
    if (!(f >> n >> np >> m) || !(0 < np && np < n))
        throw runtime_error("Invalid model header");
    Geometry g{n,np,vector<vector<uint8_t>>(n,vector<uint8_t>(n,0))};
    for (int i=0;i<m;i++) {
        int p,l;
        if (!(f >> p >> l) || p<0 || p>=np || l<np || l>=n || g.edge[p][l])
            throw runtime_error("Invalid incidence edge");
        g.edge[p][l]=g.edge[l][p]=1;
    }
    return g;
}

pair<int,int> check_axioms(const Geometry& g) {
    // Count point and line valences, and unique paths of length three
    // between any nonincident point and line.
    int splus1=0,tplus1=0;
    for (int p=0;p<g.np;p++) {
        int deg=0;
        for (int l=g.np;l<g.n;l++) deg+=g.edge[p][l];
        if (p==0) tplus1=deg;
        if (deg!=tplus1) throw runtime_error("Nonuniform point degree");
    }
    for (int l=g.np;l<g.n;l++) {
        int deg=0;
        for (int p=0;p<g.np;p++) deg+=g.edge[p][l];
        if (l==g.np) splus1=deg;
        if (deg!=splus1) throw runtime_error("Nonuniform line degree");
    }
    if (splus1<3 || tplus1<3) throw runtime_error("Not thick");
    for (int p=0;p<g.np;p++) for (int l=g.np;l<g.n;l++) {
        if (g.edge[p][l]) continue;
        int count=0;
        for (int m=g.np;m<g.n;m++) if(g.edge[p][m])
            for (int q=0;q<g.np;q++) if (g.edge[m][q] && g.edge[q][l]) count++;
        if (count!=1) throw runtime_error("Nonincident pair projection failure");
    }
    for (int a=0;a<g.np;a++) for(int b=a+1;b<g.np;b++) {
        int common=0;
        for (int l=g.np;l<g.n;l++) common+=g.edge[a][l]&&g.edge[b][l];
        if (common>1) throw runtime_error("Two points share two lines");
    }
    for (int a=g.np;a<g.n;a++) for(int b=a+1;b<g.n;b++) {
        int common=0;
        for(int p=0;p<g.np;p++) common+=g.edge[a][p]&&g.edge[b][p];
        if (common>1) throw runtime_error("Two lines share two points");
    }
    return {splus1-1,tplus1-1};
}

uint32_t atomic_type(const Geometry& g,const int* t,int k) {
    uint32_t key=0;
    int bit=0;
    for(int i=0;i<k;i++) key |= uint32_t(t[i]>=g.np)<<bit++;
    for(int i=0;i<k;i++) for(int j=i+1;j<k;j++) {
        key |= uint32_t(t[i]==t[j])<<bit++;
        key |= uint32_t(g.edge[t[i]][t[j]])<<bit++;
    }
    return key;
}

struct Intern {
    unordered_map<string,int> ids;
    int get(uint32_t base,const vector<int>& extensions) {
        vector<int> sorted=extensions; // Never modify caller's extension array.
        sort(sorted.begin(),sorted.end());
        sorted.erase(unique(sorted.begin(),sorted.end()),sorted.end());
        string signature;
        for(int j=0;j<4;j++) signature.push_back(char((base>>(8*j))&255));
        for(int v:sorted) for(int j=0;j<4;j++)
            signature.push_back(char((uint32_t(v)>>(8*j))&255));
        auto it=ids.find(signature);
        if(it!=ids.end()) return it->second;
        int id=int(ids.size());
        ids.emplace(signature,id);
        return id;
    }
};

vector<int> rank1_triples(const Geometry& g,Intern& intern) {
    int n=g.n,t[4];
    vector<int> types(size_t(n)*n*n),extensions(n);
    size_t offset=0;
    for(t[0]=0;t[0]<n;t[0]++) for(t[1]=0;t[1]<n;t[1]++)
        for(t[2]=0;t[2]<n;t[2]++) {
            for(t[3]=0;t[3]<n;t[3]++)
                extensions[t[3]]=int(atomic_type(g,t,4));
            types[offset++]=intern.get(atomic_type(g,t,3),extensions);
        }
    return types;
}

vector<int> rank2_pairs(const Geometry&g,const vector<int>& old,Intern& intern) {
    int n=g.n,t[2];
    vector<int> types(size_t(n)*n),extensions(n);
    size_t offset=0;
    for(t[0]=0;t[0]<n;t[0]++) for(t[1]=0;t[1]<n;t[1]++) {
        for(int z=0;z<n;z++) extensions[z]=old[(t[0]*n+t[1])*n+z];
        types[offset++]=intern.get(atomic_type(g,t,2),extensions);
    }
    return types;
}

vector<int> rank3_singletons(const Geometry&g,const vector<int>&old,Intern&intern) {
    int n=g.n,t[1];
    vector<int> types(n),extensions(n);
    for(t[0]=0;t[0]<n;t[0]++) {
        for(int z=0;z<n;z++) extensions[z]=old[t[0]*n+z];
        types[t[0]]=intern.get(atomic_type(g,t,1),extensions);
    }
    return types;
}

int rank4_sentence(const Geometry&g,const vector<int>&old,Intern&intern) {
    int unused[1]{};
    return intern.get(atomic_type(g,unused,0),old);
}

int main(int argc,char** argv) {
    try {
        if(argc!=5) throw runtime_error("Supply w2.txt w3.txt qminus2.txt qminus2dual.txt");
        vector<Geometry> models;
        for(int i=1;i<argc;i++) models.push_back(read_geometry(argv[i]));
        vector<pair<int,int>> order;
        for(const auto&g:models) order.push_back(check_axioms(g));
        if(order!=vector<pair<int,int>>{{2,2},{3,3},{2,4},{4,2}})
            throw runtime_error("Unexpected quadrangle orders");
        cout<<"FOUR_CLASSICAL_QUADRANGLE_AXIOMS_OK\n";
        Intern level3,level2,level1,level0;
        vector<vector<int>> t3,t2,t1;
        for(const auto&g:models) t3.push_back(rank1_triples(g,level3));
        for(int i=0;i<4;i++) { set<int> three_types(t3[i].begin(),t3[i].end()); cout<<"TRIPLE_ONE_STEP_TYPES_ORDER_"<<order[i].first<<"_"<<order[i].second<<"="<<three_types.size()<<"\n"; }
        for(int i=0;i<4;i++) t2.push_back(rank2_pairs(models[i],t3[i],level2));
        for(int i=0;i<4;i++) { set<int> pair_types(t2[i].begin(),t2[i].end()); cout<<"PAIR_TWO_STEP_TYPES_ORDER_"<<order[i].first<<"_"<<order[i].second<<"="<<pair_types.size()<<"\n"; }
        for(int i=0;i<4;i++) t1.push_back(rank3_singletons(models[i],t2[i],level1));
        set<int> answers;
        for(int i=0;i<4;i++) {
            int a=rank4_sentence(models[i],t1[i],level0);
            answers.insert(a);
            set<int> types(t1[i].begin(),t1[i].end());
            if(types.size()!=2) throw runtime_error("Unexpected singleton type count");
            cout<<"MODEL_ORDER_"<<order[i].first<<"_"<<order[i].second
                <<" RANK4_TYPE="<<a<<" RANK3_POINTED_TYPES="<<types.size()<<"\n";
        }
        if(answers.size()!=1) throw runtime_error("Fourth-rank theories differ");
        cout<<"TWO_SORTED_RANK_FOUR_AGREEMENT_OK\n";
        set<pair<bool,bool>> degree_visible;
        for(const auto&pr:order) degree_visible.insert({pr.first>=3,pr.second>=3});
        if(degree_visible.size()!=4) throw runtime_error("Rank-five witness strata missing");
        cout<<"FOUR_PAIRWISE_RANK_FIVE_DEGREE_WITNESSES_OK\n";
        cout<<"VERIFY_OK\n";
        return 0;
    } catch(const exception&e) {
        cerr<<"VERIFY_FAILED "<<e.what()<<"\n";
        return 1;
    }
}
