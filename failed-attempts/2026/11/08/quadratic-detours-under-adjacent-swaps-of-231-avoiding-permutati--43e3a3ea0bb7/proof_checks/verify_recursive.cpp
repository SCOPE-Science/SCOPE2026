// Exhaustively checks the 231-avoiding adjacent-swap distance for n=2,...,12.
// Independent Catalan recursion for state enumeration; C++17, no dependencies.
#include <algorithm>
#include <cassert>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using Word=string;
static vector<Word> cat(int n) {
    if(n==0) return {""};
    vector<Word> out;
    for(int k=0;k<n;++k){
        for(const auto& a:cat(k)) for(const auto& b:cat(n-1-k)){
            Word w=a; w.push_back(char(n));
            for(unsigned char c:b) w.push_back(char(c+k));
            out.push_back(w);
        }
    }
    return out;
}
static bool avoids(const Word& w){
    int n=w.size();
    for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) for(int k=j+1;k<n;++k)
        if(w[k]<w[i] && w[i]<w[j]) return false;
    return true;
}
int main(){
    const int cats[] = {1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012};
    for(int n=2;n<=12;++n){
        vector<Word> states=cat(n);
        assert((int)states.size()==cats[n]);
        map<Word,int> index;
        for(int i=0;i<(int)states.size();++i){
            assert(avoids(states[i]));
            assert(index.emplace(states[i],i).second);
        }
        Word a,b;
        for(int i=n-1;i>=1;--i){a.push_back(char(i));} a.push_back(char(n));
        for(int i=n;i>=1;--i)b.push_back(char(i));
        assert(index.count(a) && index.count(b));
        deque<int> q;
        vector<int> distance(states.size(),-1);
        int start=index.at(a),end=index.at(b);distance[start]=0;q.push_back(start);
        while(!q.empty()){
            int v=q.front();q.pop_front();
            for(int i=0;i<n-1;++i){
                Word w=states[v];swap(w[i],w[i+1]);
                auto it=index.find(w);
                if(it==index.end())continue;
                int u=it->second;
                if(distance[u]<0){distance[u]=distance[v]+1;q.push_back(u);}
            }
        }
        int visited=count_if(distance.begin(),distance.end(),[](int d){return d>=0;});
        assert(visited==(int)states.size());
        assert(distance[end]==(n-1)*(n-1));
        cout << "n="<<n<<" states="<<states.size()<<" connected="<<visited
             <<" distance="<<distance[end]<<" ambient="<<n-1<<"\n";
    }
    cout << "RECURSIVE_PASS\n";
}
