#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdexcept>
#include <numeric>
using namespace std;
using Vertex=array<int,4>;
static void require(bool x,const char* msg){if(!x)throw runtime_error(msg);}
int main(){
 vector<Vertex> v;
 for(int i=0;i<4;i++) for(int j=i+1;j<4;j++)
  for(int s:{-1,1})for(int t:{-1,1}){Vertex x={0,0,0,0};x[i]=s;x[j]=t;v.push_back(x);}
 require(v.size()==24,"incorrect root count");
 array<uint32_t,24> neighbors{};vector<pair<int,int>> edges;
 for(int a=0;a<24;a++)for(int b=a+1;b<24;b++){
  int dot=inner_product(v[a].begin(),v[a].end(),v[b].begin(),0);
  if(dot==1){neighbors[a]|=1u<<b;neighbors[b]|=1u<<a;edges.emplace_back(a,b);}
 }
 require(edges.size()==96,"incorrect edge count");
 for(int i=0;i<24;i++)require(__builtin_popcount(neighbors[i])==8,"incorrect degree");
 // Eight signed-coordinate groups. Each group has three nonadjacent pairs of vertices.
 array<array<uint32_t,3>,8> pairMask{};
 for(int i=0;i<4;i++)for(int sign=0;sign<2;sign++){
  int s=sign?1:-1,g=2*i+sign,slot=0;
  for(int j=0;j<4;j++)if(j!=i){
   uint32_t mask=0;
   for(int a=0;a<24;a++)if(v[a][i]==s&&v[a][j]!=0)mask|=1u<<a;
   require(__builtin_popcount(mask)==2,"bad opposite pair");pairMask[g][slot++]=mask;
  }
 }
 // Check each edge belongs to precisely one of the eight local K_{2,2,2} graphs.
 int checked=0;
 for(int a=0;a<24;a++)for(int b=a+1;b<24;b++){
  int occurrences=0;
  for(const auto& rows:pairMask){int pa=-1,pb=-1;
   for(int k=0;k<3;k++){if(rows[k]&(1u<<a))pa=k;if(rows[k]&(1u<<b))pb=k;}
   if(pa>=0&&pb>=0&&pa!=pb)occurrences++;
  }
  require(occurrences==int((neighbors[a]>>b)&1u),"octahedral edge partition incorrect");
  checked++;
 }
 require(checked==276,"pair census error");
 // First exhaustive certificate: direct Ising energy under Gray-code enumeration.
 array<int,25> minimum;
 array<uint64_t,25> multiplicity{};
 minimum.fill(1000000);
 array<int,24> spin;spin.fill(-1);
 array<int,24> localField;localField.fill(-8);
 int energy=96,magnetization=-24;
 for(uint32_t k=0;k<(1u<<24);k++){
  if(k){int p=__builtin_ctz(k);int previous=spin[p];
   energy-=2*previous*localField[p];spin[p]=-previous;
   magnetization-=2*previous;
   for(int j=0;j<24;j++)if((neighbors[p]>>j)&1u)localField[j]-=2*previous;
  }
  int bin=(magnetization+24)/2;
  if(energy<minimum[bin]){minimum[bin]=energy;multiplicity[bin]=1;}
  else if(energy==minimum[bin])multiplicity[bin]++;
 }
 // Second exhaustive certificate: independent local-octahedron truth-value census.
 array<uint64_t,25> localGround{};
 for(uint32_t subset=0;subset<(1u<<24);subset++){
  bool ground=true;
  for(const auto& rows:pairMask){bool fullMinus=false,fullPlus=false;
   for(uint32_t mask:rows){uint32_t x=subset&mask;
    if(x==mask)fullMinus=true;
    if(x==0u)fullPlus=true;
   }
   if(!(fullMinus&&fullPlus)){ground=false;break;}
  }
  if(ground){int minusCount=__builtin_popcount(subset);localGround[24-minusCount]++;}
 }
 static const array<uint64_t,25> expected={
  0,0,0,0,0,0,0,0,3,48,264,672,948,672,264,48,3,0,0,0,0,0,0,0,0
 };
 uint64_t total=0;
 for(int k=0;k<25;k++){
  if(minimum[k]==-32){require(multiplicity[k]==localGround[k],"independent methods disagree");}
  else require(localGround[k]==0,"local false positive");
  require(localGround[k]==expected[k],"wrong magnetization polynomial coefficient");
  total+=localGround[k];
 }
 require(total==2922,"wrong total degeneracy");
 cout<<"GROUND_ENERGY=-32 GROUND_TOTAL="<<total<<"\n";
 cout<<"MAGNETIZATION_COEFFICIENTS";
 for(int k=0;k<25;k++) if(localGround[k]) cout<<" ("<<2*k-24<<","<<localGround[k]<<")";
 cout<<"\n";
 // Independent-set recursion: comparison with a separately published graph invariant.
 array<uint64_t,25> independent{};
 auto rec=[&](auto&& rec,uint32_t available,int used)->void {
  if(!available){independent[used]++;return;}
  int p=__builtin_ctz(available);
  uint32_t rem=available&~(1u<<p);
  rec(rec,rem,used);
  rec(rec,rem&~neighbors[p],used+1);
 };
 rec(rec,(1u<<24)-1u,0);
 static const array<uint64_t,9> known={1,24,180,488,474,216,84,24,3};
 for(int k=0;k<=8;k++)require(independent[k]==known[k],"independent-set count disagree");
 for(int k=9;k<25;k++)require(independent[k]==0,"unexpected large independent set");
 cout<<"INDEPENDENT_COUNTS";for(int k=0;k<=8;k++)cout<<" "<<independent[k];cout<<"\n";
 cout<<"VERIFY_OK full_spin_masks=16777216 local_masks=16777216 edge_pairs=276\n";
 return 0;
}
