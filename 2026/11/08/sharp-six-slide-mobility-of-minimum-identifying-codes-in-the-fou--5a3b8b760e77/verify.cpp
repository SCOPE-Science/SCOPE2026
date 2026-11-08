// Independent, self-contained C++17 verifier: no external data or libraries.
// g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <iostream>
#include <stdexcept>
#include <cstdint>
using namespace std;
using U=uint32_t;
void require(bool b,const char *msg){if(!b)throw runtime_error(msg);}
array<U,16> graph(bool shrikhande){
    array<U,16> A{};
    for(int u=0;u<16;++u)for(int v=0;v<16;++v){
        if(u==v)continue;
        int x=u/4, y=u%4, a=v/4,b=v%4;
        int dx=(a-x+4)%4,dy=(b-y+4)%4;
        bool close=shrikhande?((dy==0 && (dx==1||dx==3))||(dx==0&&(dy==1||dy==3))||((dx==1&&dy==1)||(dx==3&&dy==3))): (a==x||b==y);
        if(close)A[u]|=U(1)<<v;
    }
    for(int i=0;i<16;++i){
        require(__builtin_popcount(A[i])==6,"graph degree");
        for(int j=0;j<16;++j)require(bool(A[i]&(U(1)<<j))==bool(A[j]&(U(1)<<i)),"undirected");
    }
    return A;
}
bool check(U C,const array<U,16>& B){
    for(int i=0;i<16;++i){
        if(!(C&B[i]))return false;
        for(int j=i+1;j<16;++j){
            if(!(C&(B[i]^B[j])))return false;
        }
    }
    return true;
}
struct Report{
  int edge_count;
  map<int,int> component_sizes, degree_count, eccentricities;
};
Report classify(const vector<U>& valid,const array<U,16>& A,bool slide){
    int n=valid.size();
    vector<vector<int>> nei(n);
    int edges=0;
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){
       U diff=valid[i]^valid[j];
       if(__builtin_popcount(diff)!=2)continue;
       U rem=valid[i]&diff,add=valid[j]&diff;
       if(slide && !(A[__builtin_ctz(rem)]&add))continue;
       nei[i].push_back(j);nei[j].push_back(i);++edges;
    }
    Report out{};out.edge_count=edges;
    vector<int> visited(n);
    for(int root=0;root<n;++root){
        out.degree_count[nei[root].size()]++;
        if(visited[root])continue;
        queue<int> q; q.push(root);visited[root]=1;
        int sz=0;
        while(!q.empty()){
          int v=q.front();q.pop();++sz;
          for(int w:nei[v])if(!visited[w]){visited[w]=1;q.push(w);}
        }
        out.component_sizes[sz]++;
    }
    if(out.component_sizes.size()==1 && out.component_sizes.count(n)){
       for(int root=0;root<n;++root){
          vector<int> d(n,-1);
          queue<int> q;q.push(root);d[root]=0;
          while(!q.empty()){
              int v=q.front();q.pop();
              for(int w:nei[v])if(d[w]<0){d[w]=d[v]+1;q.push(w);}
          }
          require(*min_element(d.begin(),d.end())>=0,"disconnected BFS");
          out.eccentricities[*max_element(d.begin(),d.end())]++;
       }
    }
    return out;
}
void compare(bool shri){
    auto A=graph(shri);
    array<U,16>B{};
    for(int i=0;i<16;++i)B[i]=A[i]|(U(1)<<i);
    int k=shri?5:6;
    vector<U> codes;
    int smaller=0;
    // Exhaust all 65536 subsets, using an alternative pair-separation criterion.
    for(U c=0;c<(U(1)<<16);++c){
       int pop=__builtin_popcount(c);
       if(pop==k-1 && check(c,B))++smaller;
       if(pop==k && check(c,B))codes.push_back(c);
    }
    int n=shri?96:2208;
    require(!smaller,"unexpected smaller identifying code");
    require(int(codes.size())==n,"incorrect code count");
    cout << (shri?"S":"R")<<": min="<<k<<" codes="<<n<<" smaller="<<smaller<<"\n";
    for(int mode=0;mode<2;++mode){
       bool slide=(mode==0);
       auto r=classify(codes,A,slide);
       if(shri){
         if(slide){require(r.edge_count==0 && r.component_sizes==map<int,int>{{1,96}} && r.degree_count==map<int,int>{{0,96}},"S slide mismatch");}
         else{require(r.edge_count==96 && r.component_sizes==map<int,int>{{6,16}} && r.degree_count==map<int,int>{{2,96}},"S jump mismatch");}
       }else{
         if(slide){require(r.edge_count==14976 && r.degree_count==map<int,int>{{12,1344},{16,864}},"R slide mismatch");}
         else{require(r.edge_count==28800,"R jump mismatch");}
         require(r.component_sizes==map<int,int>{{2208,1}},"R disconnected");
         require(r.eccentricities==map<int,int>{{6,2208}},"R radius/diam mismatch");
       }
       cout << (shri?"S":"R")<<(slide?" slide":" jump")
            <<": edges="<<r.edge_count<<" components=";
       for(auto [a,b]:r.component_sizes)cout<<a<<"x"<<b<<" ";
       cout<<"deg=";
       for(auto [a,b]:r.degree_count)cout<<a<<":"<<b<<" ";
       cout<<"ecc=";
       for(auto [a,b]:r.eccentricities)cout<<a<<":"<<b<<" ";
       cout<<"\n";
    }
}
int main(){try{compare(true);compare(false);cout<<"PASS: independent exhaustive reconstruction and BFS\n";}catch(const exception&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}}
