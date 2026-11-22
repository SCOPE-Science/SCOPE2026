// Exact independent line-subset-first enumeration of all minimum domination configurations
// in the Levi graphs of both thirteen-point Steiner triple systems.
// C++17: g++ -std=c++17 -O2 verify_q_first.cpp -o verify_q_first && ./verify_q_first
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr unsigned ALLP=(1u<<13)-1,ALLL=(1u<<26)-1;
using Triple=array<int,3>;
Triple sorted3(Triple t){sort(t.begin(),t.end());return t;}
vector<Triple> get_design(bool changed){
  set<Triple> S;
  for(Triple t : {Triple{1,3,9}, Triple{2,5,6}})
    for(int shift=0;shift<13;shift++)
      S.insert(sorted3({(t[0]+shift)%13,(t[1]+shift)%13,(t[2]+shift)%13}));
  assert(S.size()==26);
  if(changed){
    for(Triple t:{Triple{2,4,10},Triple{2,5,6},Triple{4,6,12},Triple{5,10,12}})
      assert(S.erase(t)==1);
    for(Triple t:{Triple{2,4,6},Triple{2,5,10},Triple{4,10,12},Triple{5,6,12}})
      assert(S.insert(t).second);
  }
  return {S.begin(),S.end()};
}
struct Outcome{set<U> states;map<pair<int,bool>,int> types;int edges=0;map<int,int> comps,degrees;};
Outcome compute(bool changed){
  auto T=get_design(changed);
  vector<unsigned> blockpoints;
  int pairCounts[13][13]{};
  for(auto b:T){
    unsigned bm=0;
    for(auto x:b)bm|=(1u<<x);
    blockpoints.push_back(bm);
    for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)pairCounts[b[i]][b[j]]++;
  }
  for(int i=0;i<13;i++)for(int j=i+1;j<13;j++)assert(pairCounts[i][j]==1);
  array<unsigned,8192> hit{};
  vector<unsigned> five,six,seven;
  for(unsigned p=0;p<=ALLP;p++){
    for(int j=0;j<26;j++)if(p&blockpoints[j])hit[p]|=1u<<j;
    if(__builtin_popcount(p)==5)five.push_back(p);
    if(__builtin_popcount(p)==6)six.push_back(p);
    if(__builtin_popcount(p)==7)seven.push_back(p);
  }
  assert(five.size()==1287&&six.size()==1716&&seven.size()==1716);
  Outcome out;
  auto visit=[&](unsigned Qmask,int q,unsigned pointCover){
    int p=9-q;
    auto &pool = (p==5?five:(p==6?six:seven));
    for(unsigned P:pool){
      if((P|pointCover)!=ALLP)continue;
      if((hit[P]|Qmask)!=ALLL)continue;
      U state=U(P)|(U(Qmask)<<13);
      assert(out.states.insert(state).second);
      int mandatory=26-__builtin_popcount(hit[P]);
      out.types[{p,mandatory==q}]++;
    }
  };
  int count8=0;
  // Count all optimal nine-sets by choosing Q first, then the point-side P.
  for(int a=0;a<26;a++)for(int b=a+1;b<26;b++){
    unsigned Q=(1u<<a)|(1u<<b);
    unsigned cover=blockpoints[a]|blockpoints[b];
    visit(Q,2,cover);
    for(int c=b+1;c<26;c++){
      unsigned Q3=Q|(1u<<c),cover3=cover|blockpoints[c];
      visit(Q3,3,cover3);
      // Size-8 candidate must have p=5, q=3 (other p excluded by degree counting).
      for(unsigned P:five)if((P|cover3)==ALLP && (hit[P]|Q3)==ALLL)count8++;
      for(int d=c+1;d<26;d++){
        unsigned Q4=Q3|(1u<<d),cover4=cover3|blockpoints[d];
        visit(Q4,4,cover4);
      }
    }
  }
  assert(count8==0);
  // Exchange graph: flip precisely one present and one absent vertex.
  vector<U> states(out.states.begin(),out.states.end());
  unordered_map<U,int> index;
  for(int i=0;i<(int)states.size();i++)index[states[i]]=i;
  vector<vector<int>> neighbors(states.size());
  for(int k=0;k<(int)states.size();k++){
    U s=states[k];
    for(int i=0;i<39;i++)if((s>>i)&1ULL)
      for(int j=0;j<39;j++)if(!((s>>j)&1ULL)){
        auto it=index.find(s^(1ULL<<i)^(1ULL<<j));
        if(it!=index.end())neighbors[k].push_back(it->second);
      }
    out.edges+=neighbors[k].size();out.degrees[(int)neighbors[k].size()]++;
  }
  assert(out.edges%2==0);out.edges/=2;
  vector<bool> visited(states.size());
  for(int i=0;i<(int)states.size();i++)if(!visited[i]){
    vector<int> stack={i};visited[i]=true;int size=0;
    while(!stack.empty()){
      int k=stack.back();stack.pop_back();size++;
      for(int j:neighbors[k])if(!visited[j]){visited[j]=true;stack.push_back(j);}
    }
    out.comps[size]++;
  }
  return out;
}
int main(){
  for(bool switched:{false,true}){
    const char* name=switched?"switched":"cyclic";
    auto out=compute(switched);
    const int expectedN=switched?1511:1456;
    const int expectedE=switched?3192:2652;
    map<int,int> expectedComps=switched?map<int,int>{{1,82},{10,9},{13,1},{17,3},{24,6},{48,3},{51,1},{936,1}}:
      map<int,int>{{1,117},{17,39},{676,1}};
    map<pair<int,bool>,int> expectedTypes=switched?
      map<pair<int,bool>,int>{{{5,true},195},{{6,true},574},{{6,false},612},{{7,true},130}}:
      map<pair<int,bool>,int>{{{5,true},195},{{6,true},624},{{6,false},507},{{7,true},130}};
    assert((int)out.states.size()==expectedN && out.edges==expectedE && out.comps==expectedComps && out.types==expectedTypes);
    cout<<name<<" N="<<out.states.size()<<" edges="<<out.edges<<" components=";
    for(auto [sz,n]:out.comps)cout<<sz<<":"<<n<<",";
    cout<<" point-neat classes=";
    for(auto [class_,n]:out.types)cout<<class_.first<<"/"<<class_.second<<":"<<n<<",";
    cout<<"\n";
    // Can be compared against independently generated point-first state list.
    for(U x:out.states)cout<<"@"<<name<<" "<<hex<<x<<dec<<"\n";
  }
  cout<<"PASS: independent block-first enumeration and exchange components\n";
}
