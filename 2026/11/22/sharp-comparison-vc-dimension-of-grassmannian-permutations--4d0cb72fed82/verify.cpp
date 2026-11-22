// Standalone finite verification using subset-generated Grassmannian permutations.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using Vec=vector<int>;
int main(){
  const map<int,Vec> expected={{2,{1,1}},{3,{1,3,2}},{4,{1,6,10}},{5,{1,10,30,6}},{6,{1,15,70,41}},{7,{1,21,140,161,10}},{8,{1,28,252,476,89}}};
  for(int n=2;n<=8;n++){
    set<Vec> unique;
    for(int a=0;a<(1<<n);a++){
      Vec p;
      for(int i=1;i<=n;i++)if(a&(1<<(i-1)))p.push_back(i);
      for(int i=1;i<=n;i++)if(!(a&(1<<(i-1))))p.push_back(i);
      unique.insert(p);
    }
    vector<Vec> ps(unique.begin(),unique.end());
    assert((int)ps.size()==(1<<n)-n);
    vector<pair<int,int>> qs;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)qs.push_back({i,j});
    Vec poly={1};
    vector<Vec> supports(1);
    while(!supports.empty()){
      vector<Vec> next;
      for(auto &s:supports){
        for(int q=(s.empty()?0:s.back()+1);q<(int)qs.size();q++){
          Vec t=s;t.push_back(q);
          vector<unsigned char> flags(1u<<t.size(),0);
          int count=0;
          for(const Vec &p:ps){
            int value=0;
            for(int h=0;h<(int)t.size();h++){
              auto [i,j]=qs[t[h]];
              if(p[i]>p[j])value|=(1<<h);
            }
            if(!flags[value]){flags[value]=1;count++;}
          }
          if(count==(int)flags.size())next.push_back(move(t));
        }
      }
      if(next.empty())break;
      poly.push_back((int)next.size());
      supports.swap(next);
    }
    assert(poly==expected.at(n));
    cout<<"n="<<n<<" permutations="<<ps.size()<<" poly=";
    for(int x:poly)cout<<x<<',';
    cout<<'\n';
    if(n==6){
      // The n=6 full support census proves that no 4-comparison set is shattered.
      assert(poly.size()==4);
      // n=4 has no three-comparison shattered set. Restriction to a
      // subpermutation preserves the at-most-one-descent property.
      assert(expected.at(4).size()==3);
    }
  }
  cout<<"verified\n";
}
