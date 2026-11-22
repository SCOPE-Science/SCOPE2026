// Standalone verification in the generalized Petersen GP(10,3) representation.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;
int main(){
    vector<pair<int,int>> edges;
    for(int i=0;i<10;i++){
        edges.push_back({i,(i+1)%10});
        edges.push_back({i,i+10});
        edges.push_back({i+10,(i+3)%10+10});
    }
    assert(edges.size()==30);
    const unsigned LIMIT=1u<<20,ALL=LIMIT-1;
    vector<unsigned char> weight(LIMIT,255);
    map<int,int> spectrum;
    vector<unsigned> low;
    for(unsigned s=0;s<LIMIT;s++)if(__builtin_popcount(s)==10){
        int c=0;
        for(auto [a,b]:edges)c+=((s>>a&1u)!=(s>>b&1u));
        weight[s]=(unsigned char)c;
        ++spectrum[c];
        if(c<=10)low.push_back(s);
    }
    const map<int,int> expected={{6,10},{8,360},{10,5292},{12,20640},
        {14,45990},{16,51900},{18,40600},{20,15852},{22,3630},{24,420},{26,60},{30,2}};
    assert(spectrum==expected);
    assert(count_if(weight.begin(),weight.end(),[](auto x){return x==6;})==10);
    cout<<"all oriented bisection spectrum:";
    for(auto [c,count]:spectrum)cout<<" "<<c<<":"<<count;
    cout<<"\n";
    for(int cap:{6,8,10}){
        unordered_set<unsigned> active;
        for(auto s:low)if(weight[s]<=cap)active.insert(s);
        map<int,int> cc;int largestOptimalCount=0;
        while(!active.empty()){
            unsigned start=*active.begin();active.erase(start);
            queue<unsigned> q;q.push(start);int len=0,opt=0;
            while(!q.empty()){
                unsigned s=q.front();q.pop();++len;opt+=(weight[s]==6);
                for(unsigned a=s;a;a&=a-1){
                    unsigned x=a&-a;
                    for(unsigned b=ALL^s;b;b&=b-1){
                        unsigned y=b&-b,t=s^x^y;
                        auto it=active.find(t);
                        if(it!=active.end()){active.erase(it);q.push(t);}
                    }
                }
            }
            ++cc[len];largestOptimalCount=max(largestOptimalCount,opt);
        }
        if(cap==6)assert((cc==map<int,int>{{1,10}} && largestOptimalCount==1));
        if(cap==8)assert((cc==map<int,int>{{1,60},{31,10}} && largestOptimalCount==1));
        if(cap==10)assert((cc==map<int,int>{{1,12},{5650,1}} && largestOptimalCount==10));
        cout<<"cut budget "<<cap<<": ";
        for(auto [length,count]:cc)cout<<count<<" components x size "<<length<<"; ";
        cout<<"max optima in one component "<<largestOptimalCount<<"\n";
    }
    cout<<"ALL CHECKS PASSED\n";
}
