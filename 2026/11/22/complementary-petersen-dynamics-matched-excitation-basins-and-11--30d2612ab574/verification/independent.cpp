// Independent finite-state orbit verification by Floyd's tortoise-and-hare algorithm.
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
using K = pair<int,int>;
constexpr int V=10, N=59049;
const array<array<int,2>,V> p={{{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}};
int advance(int z,bool gh){
 array<int,V> bits{};
 int q=z;
 for(int i=0;i<V;i++){bits[i]=q%3;q/=3;}
 int factor=1,out=0;
 for(int i=0;i<V;i++){
  bool has=false;
  int wanted=gh?1:(bits[i]+1)%3;
  for(int j=0;j<V;j++)if(j!=i){
   bool intersects=(p[i][0]==p[j][0]||p[i][0]==p[j][1]||p[i][1]==p[j][0]||p[i][1]==p[j][1]);
   if(intersects && bits[j]==wanted){has=true;break;}
  }
  int v=gh ? (bits[i]==0? (int)has:(bits[i]+1)%3): (has?(bits[i]+1)%3:bits[i]);
  out+=v*factor;factor*=3;
 }
 return out;
}
K floyd(int start,bool gh){
 auto f=[gh](int x){return advance(x,gh);};
 int tort=f(start),hare=f(f(start));
 while(tort!=hare){tort=f(tort);hare=f(f(hare));}
 int mu=0;tort=start;
 while(tort!=hare){tort=f(tort);hare=f(hare);mu++;}
 int period=1;hare=f(tort);
 while(tort!=hare){hare=f(hare);period++;}
 return {mu,period};
}
int main(){
 map<K,int>a,b,links;
 for(int s=0;s<N;s++){
  K c=floyd(s,false),g=floyd(s,true);
  ++a[c];++b[g];++links[{c.second,g.second}];
 }
 map<K,int> expectA={{{0,1},3},{{0,3},30240},{{1,1},2916},{{1,3},20370},{{2,1},480},{{2,3},5040}};
 map<K,int> expectB={{{0,1},1},{{0,3},30240},{{1,1},1023},{{1,3},6700},{{2,1},1133},{{2,3},8470},{{3,1},1082},{{3,3},8560},{{4,1},160},{{4,3},1680}};
 assert(a==expectA && b==expectB);
 map<K,int> expectedLinks={{{1,1},3399},{{3,3},55650}};
 assert(links==expectedLinks);
 cout << "INDEPENDENT_FLOYD_ALL_59049_OK\n";
 return 0;
}
