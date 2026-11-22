// Complete binary prefix-tree literal-decoder census, maximum depth four.
// Compile: c++ -std=c++17 -O2 prefix_verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<string> shapes(int h) {
    if(h==0) return {"L"};
    vector<string> out={"L"};
    auto p=shapes(h-1);
    for(const auto& x:p) for(const auto& y:p)
       out.push_back("("+x+y+")");
    return out;
}

struct Parser {
 const string &s;
 int pos=0;
 vector<string> internal, leaves;
 Parser(const string &s):s(s){}
 void visit(string p) {
    if(s[pos]=='L') {++pos;leaves.push_back(p);return;}
    assert(s[pos++]=='(');
    internal.push_back(p);
    visit(p+'0');visit(p+'1');
    assert(s[pos++]==')');
 }
};

int threshold(const vector<string>& states) {
 int n=states.size();
 if(n==1) return 0;
 unordered_map<string,int> ids;
 for(int j=0;j<n;++j) ids[states[j]]=j;
 array<vector<int>,2> shift;
 for(int c=0;c<2;++c){
     shift[c].resize(n);
     for(int i=0;i<n;++i){
         auto it=ids.find(states[i]+char('0'+c));
         shift[c][i]=it==ids.end()?0:it->second;
     }
 }
 int start=(1<<n)-1;
 vector<int> distances(1<<n,-1);
 queue<int> Q;Q.push(start);distances[start]=0;
 while(!Q.empty()){
    int s=Q.front();Q.pop();
    if((s&(s-1))==0) return distances[s];
    for(int c=0;c<2;++c){
      int image=0;
      for(int i=0;i<n;++i) if((s>>i)&1) image|=1<<shift[c][i];
      if(distances[image]<0){distances[image]=distances[s]+1;Q.push(image);}
    }
 }
 return -1;
}
int main() {
 auto ss=shapes(4);assert(ss.size()==677);
 map<pair<int,int>,int> bins;
 vector<string> extremals;
 int seen=0;
 for (const auto& shape:ss) {
    if(shape=="L") continue;
    Parser p(shape);p.visit("");assert(p.pos==(int)shape.size());
    int h=0;for(auto& w:p.leaves) h=max(h,(int)w.size());
    int d=threshold(p.internal);++bins[{h,d}];++seen;
    if(h==4&&d==17){extremals.push_back(shape);}
 }
 assert(seen==676);
 map<int,int> expected4={{-1,19},{1,2},{2,20},{3,44},{4,92},{5,96},{6,56},{7,50},{8,144},{9,118},{10,4},{11,2},{12,2},{17,2}};
 for(auto [d,count]:expected4)assert((bins[{4,d}]==count));
 int height4total=0;
 for(auto [h_d,count]:bins)if(h_d.first==4)height4total+=count;
 assert(height4total==651 && extremals.size()==2);
 assert((bins[{3,-1}]==1 && bins[{3,7}]==2));
 cout<<"total="<<seen<<" height4="<<height4total<<" max=17 extremals="<<extremals.size()<<"\n";
 for(auto [key,num]:bins)cout<<"height="<<key.first<<" distance="<<key.second<<" count="<<num<<"\n";
 return 0;
}
