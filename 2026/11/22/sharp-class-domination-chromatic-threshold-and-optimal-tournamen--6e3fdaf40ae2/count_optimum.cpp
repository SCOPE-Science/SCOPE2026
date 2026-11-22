// Independent finite verification of bounded-tournament colourings of KG(n,2).
// Build: c++ -std=c++17 -O2 -Wall -Wextra count_optimum.cpp -o count_optimum
// Run:   ./count_optimum
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
using E=pair<int,int>;

bool check_classes(int n, const vector<vector<E>>& cls){
    vector<vector<int>> tally(n,vector<int>(n,0));
    for(const auto& C:cls){
        if(C.empty())return false;
        for(auto [a,b]:C){
            if(a>b)swap(a,b);
            if(++tally[a][b]!=1)return false;
        }
        for(size_t i=0;i<C.size();++i)
        for(size_t j=i+1;j<C.size();++j){
            auto [a,b]=C[i];auto [c,d]=C[j];
            if(a!=c && a!=d && b!=c && b!=d)return false;
        }
        bool witness=false;
        for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){
            bool yes=true;
            for(auto [c,d]:C)if(a==c||a==d||b==c||b==d){yes=false;break;}
            witness|=yes;
        }
        if(!witness)return false;
    }
    for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)
        if(tally[a][b]!=1)return false;
    return true;
}

long long count_canonical(int n){
    const int c=n-3;
    vector<E> pairs;
    for(int i=0;i<c;++i)for(int j=i+1;j<c;++j)pairs.emplace_back(i,j);
    const uint64_t tot=uint64_t(1)<<pairs.size();
    long long accepted=0;
    for(uint64_t mask=0;mask<tot;++mask){
        vector<vector<E>> cls(c+1);
        for(int i=0;i<c;++i)for(int k=c;k<n;++k)cls[i].emplace_back(i,k);
        cls.back()={{c,c+1},{c,c+2},{c+1,c+2}};
        for(size_t k=0;k<pairs.size();++k){
            auto [a,b]=pairs[k];
            int center=(mask&(uint64_t(1)<<k))?a:b;
            cls[center].emplace_back(a,b);
        }
        if(check_classes(n,cls))++accepted;
    }
    return accepted;
}

int main(){
    long long a=count_canonical(8),b=count_canonical(9);
    cout<<"n=8 count_per_triangle="<<a<<" unlabelled="<<a*56<<"\n";
    cout<<"n=9 count_per_triangle="<<b<<" unlabelled="<<b*84<<"\n";
    assert(a==24 && b==5184);
    cout<<"TOURNAMENT_CENSUS_OK\n";
}
