#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
struct Graph {
 int C;
 vector<pair<int,int>> edges;
 vector<int> parent,depth;
 string label;
 Graph(int c,string s):C(c),parent(c,-1),depth(c,0),label(s){ for(int i=0;i<c;i++)for(int j=i+1;j<c;j++)edges.emplace_back(i,j); }
 void add(int p){ if(p<0 || p >=(int)parent.size())throw runtime_error("bad parent");int v=parent.size();parent.push_back(p); depth.push_back(depth[p]+1);edges.emplace_back(p,v); }
 int size()const{return parent.size();}
 int H()const{return *max_element(depth.begin(),depth.end());}
 int diameter()const{
  int n=size(),best=0;for(int s=0;s<n;s++){
   vector<int>d(n,-1);vector<int>q{s};d[s]=0;
   for(int z=0;z<(int)q.size();z++){int v=q[z];for(auto[e,f]:edges){int u=(v==e?f:v==f?e:-1);if(u>=0&&d[u]<0){d[u]=d[v]+1;q.push_back(u);}}}
   best=max(best,*max_element(d.begin(),d.end()));
  }return best;
 }
};
static uint64_t encode(const vector<int>& x){uint64_t t=0,p=1;for(int z:x){t+=(uint64_t)z*p;p*=3;}return t;}
static vector<int> decode(uint64_t v,int n){vector<int>x(n);for(int i=0;i<n;i++){x[i]=v%3;v/=3;}return x;}
static vector<int> step(const Graph& g, const vector<int>& x){
 vector<int>y=x;
 for(int v=0;v<g.size();v++)for(auto[e,f]:g.edges){int w=(e==v?f:f==v?e:-1);if(w>=0&&x[w]==(x[v]+1)%3){y[v]=(x[v]+1)%3;break;}}
 return y;
}
static void test(const Graph& g){
 int n=g.size(),h=g.H(),D=g.diameter(),T=max(2*h,D);
 uint64_t all=1;for(int j=0;j<n;j++)all*=3;
 uint64_t fixes=0,osc=0,maximum=0,maxfix=0,maxosc=0;
 map<uint64_t,uint64_t> orbit_basin;
 uint64_t max_per=0;
 for(uint64_t key=0;key<all;key++){
  auto x=decode(key,n),init=x;
  bool rainbow=false;bool present[3]={0,0,0};for(int j=0;j<g.C;j++)present[x[j]]=1;
  rainbow=present[0]&&present[1]&&present[2];
  vector<uint64_t> states;states.reserve(T+4);
  for(int k=0;k<=T+3;k++){states.push_back(encode(x));x=step(g,x);}
  if(states[T]!=states[T+3])throw runtime_error("period cutoff failed");
  int period=(states[T]==states[T+1]?1:3);
  if((period==3)!=rainbow)throw runtime_error("rainbow criterion failed");
  int t=0;while(t<=T&&states[t]!=states[t+period])t++;
  if(t>T)throw runtime_error("entry time not found");
  if(rainbow){osc++;maxosc=max<uint64_t>(maxosc,t);}
  else{fixes++;maxfix=max<uint64_t>(maxfix,t);}
  maximum=max<uint64_t>(maximum,t);max_per=max<uint64_t>(max_per,period);
  uint64_t canonical=states[t];for(int j=1;j<period;j++)canonical=min(canonical,states[t+j]);
  orbit_basin[canonical]++;
 }
 uint64_t twoC=1,threeC=1,threeTail=1;
 for(int i=0;i<g.C;i++){twoC*=2;threeC*=3;}for(int i=g.C;i<n;i++)threeTail*=3;
 uint64_t expfix=3*threeTail*(twoC-1),exposc=threeTail*(threeC-3*twoC+3);
 uint64_t expected_orbits=(threeC-3*twoC+3)/3,expected_basin_osc=3*threeTail;
 uint64_t expected_basin_fix=threeTail*(twoC-1);
 if(fixes!=expfix||osc!=exposc||orbit_basin.size()!=expected_orbits+3||maxfix!=D||maxosc!=2*h||maximum!=T)throw runtime_error("enumeration theorem mismatch");
 for(auto[rep,count]:orbit_basin){auto y=decode(rep,n);bool has[3]={0,0,0};for(int i=0;i<g.C;i++)has[y[i]]=1;bool cyc=has[0]&&has[1]&&has[2];if(count!=(cyc?expected_basin_osc:expected_basin_fix))throw runtime_error("wrong individual basin");}
 cout<<"OK "<<g.label<<" C="<<g.C<<" nodes="<<n<<" H="<<h<<" D="<<D<<" states="<<all<<" fixedbasin="<<fixes<<" period3basin="<<osc<<" primitive3="<<expected_orbits<<" sharpT="<<T<<"\n";
}
int main(){
 try{
  {Graph g(3,"one-leaf");g.add(0);test(g);}
  {Graph g(3,"two-leaf-star");g.add(0);g.add(0);test(g);}
  {Graph g(3,"two-core-roots");g.add(0);g.add(1);test(g);}
  {Graph g(3,"length-two-tail");g.add(0);g.add(3);test(g);}
  {Graph g(3,"branching-tail");g.add(0);g.add(3);g.add(3);test(g);}
  {Graph g(3,"two-root-unequal");g.add(0);g.add(3);g.add(1);test(g);}
  {Graph g(3,"length-three-tail");g.add(0);g.add(3);g.add(4);test(g);}
  {Graph g(3,"two-long-tails");g.add(0);g.add(3);g.add(1);g.add(5);test(g);}
  {Graph g(3,"long-asymmetric-tails");g.add(0);g.add(3);g.add(4);g.add(1);g.add(6);test(g);}
  {Graph g(4,"three-roots-four-clique");g.add(0);g.add(1);g.add(2);test(g);}
  {Graph g(4,"four-clique-branching");g.add(0);g.add(4);g.add(4);g.add(1);g.add(7);test(g);}
  {Graph g(5,"five-leaves");for(int i=0;i<5;i++)g.add(i);test(g);}
  {Graph g(5,"double-deep-branches");g.add(0);g.add(5);g.add(1);g.add(7);g.add(2);g.add(9);test(g);}
  cout<<"ALL_CASES_OK\n";
 }catch(exception&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
