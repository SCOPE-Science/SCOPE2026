// Exhaustive, self-contained verifier for ordinary locating-dominating sets
// in the simple undirected length-two Kautz graph. C++17.
// Usage: g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;
struct Instance {
    int q,n;
    vector<pair<int,int>> words;
    vector<U> near;
    Instance(int Q):q(Q) {
        for (int a=0;a<q;a++) for(int b=0;b<q;b++) if(a!=b) words.push_back({a,b});
        n=(int)words.size();
        if(n>63) throw runtime_error("mask capacity exceeded");
        near.resize(n,0);
        for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(i!=j){
            auto [a,b]=words[i]; auto [c,d]=words[j];
            if(b==c || d==a) near[i]|=U(1)<<j;
        }
    }
    bool qualifies(U selected) const {
        U sigs[64]; int n_sigs=0;
        for(int i=0;i<n;i++) if(!(selected & (U(1)<<i))){
            U s=near[i]&selected;
            if(s==0)return false;
            for(int j=0;j<n_sigs;j++) if(sigs[j]==s)return false;
            sigs[n_sigs++]=s;
        }
        return true;
    }
    vector<int> mapping(int which) const {
        vector<int> perm(q);iota(perm.begin(),perm.end(),0);
        if(which<q-1)swap(perm[which],perm[which+1]);
        vector<int> mapping(n);
        for(int i=0;i<n;i++){
            auto [a,b]=words[i];
            if(which==q-1)swap(a,b);else {a=perm[a];b=perm[b];}
            int j=0;
            while(j<n && words[j]!=make_pair(a,b))++j;
            if(j==n) throw runtime_error("not a word permutation");
            mapping[i]=j;
        }
        return mapping;
    }
    U moved(U s,const vector<int>& m) const {
        U result=0;
        while(s){int i=__builtin_ctzll(s);s&=s-1;result|=U(1)<<m[i];}
        return result;
    }
    vector<pair<int,int>> decode(U s) const {
        vector<pair<int,int>> r;
        for(int i=0;i<n;i++)if(s&(U(1)<<i))r.push_back(words[i]);
        return r;
    }
};
static U choose_count(int n,int k){
    U r=1;for(int i=1;i<=k;i++){r=r*(n-k+i)/i;}return r;
}
struct Census {U count, attempts; vector<U> good; U first;};
Census enumerate(const Instance& g,int k,bool keep){
    if(k<0 || k>g.n) return {0,0,{},0};
    U limit=U(1)<<g.n;
    U selected=k? (U(1)<<k)-1 : 0;
    U trials=0,success=0,first=0;
    vector<U> good;
    while(selected<limit){
        ++trials;
        if(g.qualifies(selected)){
            ++success;if(!first)first=selected;
            if(keep)good.push_back(selected);
        }
        if(k==0)break;
        U low=selected & (~selected+1);
        U higher=selected+low;
        if(higher==0)break;
        selected=(((higher^selected)>>2)/low)|higher;
    }
    if(trials!=choose_count(g.n,k)) throw runtime_error("incomplete combination enumeration");
    return {success,trials,move(good),first};
}
map<int,int> orbit_sizes(const Instance& g,const vector<U>& good){
    unordered_set<U> unseen(good.begin(),good.end());
    vector<vector<int>> maps;
    for(int j=0;j<g.q;j++)maps.push_back(g.mapping(j));
    map<int,int> histogram;
    while(!unseen.empty()){
        vector<U> queue{*unseen.begin()};unseen.erase(queue[0]);
        int count=0;
        while(!queue.empty()){
            U x=queue.back();queue.pop_back();++count;
            for(const auto& p:maps){
                U y=g.moved(x,p);
                if(!g.qualifies(y))throw runtime_error("symmetry not preserving condition");
                auto it=unseen.find(y);
                if(it!=unseen.end()){unseen.erase(it);queue.push_back(y);}
            }
        }
        ++histogram[count];
    }
    return histogram;
}
int main(){
    try{
        const int optimal[]={0,0,1,3,4,5,7,8};
        const U total[]={0,0,2,20,168,84,11040,13860};
        vector<map<int,int>> expected(8);
        expected[2]={{2,1}};
        expected[3]={{2,1},{6,1},{12,1}};
        expected[4]={{6,2},{12,1},{24,2},{48,2}};
        expected[5]={{24,1},{60,1}};
        expected[6]={{120,2},{360,4},{720,7},{1440,3}};
        expected[7]={{630,2},{2520,1},{5040,2}};
        for(int q=2;q<=7;q++){
            Instance g(q); int k=optimal[q];
            Census below=enumerate(g,k-1,false);
            Census at=enumerate(g,k,true);
            if(below.count!=0 || at.count!=total[q])throw runtime_error("capacity/census disagrees");
            auto orbits=orbit_sizes(g,at.good);
            if(orbits!=expected[q])throw runtime_error("orbit census disagrees");
            U sum=0;for(auto [size,multiplicity]:orbits)sum+=U(size)*multiplicity;
            if(sum!=total[q])throw runtime_error("orbit partition incomplete");
            cout<<"q="<<q<<" min="<<k<<" optimal_sets="<<at.count<<" orbits="<<accumulate(orbits.begin(),orbits.end(),0,[](int z,const auto& e){return z+e.second;})
                <<" tested_below="<<below.attempts<<" tested_at="<<at.attempts<<" witness=";
            for(auto [a,b]:g.decode(at.first))cout<<"("<<a<<","<<b<<")";
            cout<<'\n';
        }
        cout<<"VERIFY_OK\n";
    }catch(const exception& e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
