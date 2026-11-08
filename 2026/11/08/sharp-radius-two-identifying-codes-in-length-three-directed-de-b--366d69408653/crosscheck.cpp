#include <cstdio>
#include <vector>
#include <set>
#include <cassert>
#include <algorithm>
// Independent C++ implementation: direct reversed-arc enumeration and signature vectors.
int main(){
  for(int d=3;d<=8;d++){
    const int n=d*d*d;
    std::vector<int> chosen;
    for(int x=0;x<n;x++)if(x/(d*d)!=x%d)chosen.push_back(x);
    assert((int)chosen.size()==d*d*(d-1));
    std::set<std::vector<int>> signatures;
    for(int x=0;x<n;x++){
       std::set<int> predecessors; predecessors.insert(x);
       std::set<int> active{x};
       for(int step=0;step<2;step++){
          std::set<int> next;
          for(int v:active){
             for(int k=0;k<d;k++) next.insert(k*d*d+v/d);
          }
          predecessors.insert(next.begin(),next.end());
          active=next;
       }
       std::vector<int> key;
       for(int y:chosen) if(predecessors.count(y))key.push_back(y);
       assert(!key.empty());
       bool new_key=signatures.insert(key).second;
       assert(new_key);
    }
    assert((int)signatures.size()==n);
    std::printf("d=%d code=%zu signatures=%zu\n",d,chosen.size(),signatures.size());
  }
  puts("CROSSCHECK_OK");
}
