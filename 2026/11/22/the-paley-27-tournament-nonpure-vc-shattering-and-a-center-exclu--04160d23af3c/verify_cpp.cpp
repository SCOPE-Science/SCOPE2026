// Standalone exact verification of quadratic-residue translations in GF(27).
// Uses GF(3)[t]/(t^3-t-1) and Euler's criterion (distinct from the Python verifier).
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <map>
#include <set>
#include <numeric>
#include <cstdint>
using namespace std;
using T3=array<int,3>; using T4=array<int,4>;
int digit(int x,int i){while(i--)x/=3;return x%3;}
int encode(int a,int b,int c){return a+3*b+9*c;}
int add(int x,int y){return encode((digit(x,0)+digit(y,0))%3,(digit(x,1)+digit(y,1))%3,(digit(x,2)+digit(y,2))%3);}
int mul(int x,int y){int a[5]={};for(int i=0;i<3;i++)for(int j=0;j<3;j++)a[i+j]=(a[i+j]+digit(x,i)*digit(y,j))%3;
  for(int k=4;k>=3;k--){int c=a[k];a[k]=0;a[k-2]=(a[k-2]+c)%3;a[k-3]=(a[k-3]+c)%3;}
  return encode(a[0],a[1],a[2]);}
int power(int a,int k){int z=1;while(k){if(k&1)z=mul(z,a);a=mul(a,a);k/=2;}return z;}
int main(){
 set<int> squares;for(int a=1;a<27;a++)if(power(a,13)==1)squares.insert(a);
 assert(squares.size()==13 && !squares.count(2));
 array<array<int,27>,27> positive{};
 for(int y=0;y<27;y++)for(int r:squares)positive[y][add(y,r)]=1;
 auto traces=[&](auto s,bool outside){int m=(int)s.size(), seen=0;
   for(int y=0;y<27;y++) {if(outside && find(s.begin(),s.end(),y)!=s.end()) continue;
    int pat=0;for(int i=0;i<m;i++)if(positive[y][s[i]])pat|=1<<i;seen|=1<<pat;}
   return __builtin_popcount((unsigned)seen);
 };
 vector<T3> triples;vector<T4> fours;vector<T3> alltri;
 int counts[5]={1,0,0,0,0}; int strict[5]={1,0,0,0,0};
 for(int a=0;a<27;a++){
   vector<int> s={a};counts[1]+=(traces(s,false)==2);strict[1]+=(traces(s,true)==2);
   for(int b=a+1;b<27;b++){
    s={a,b};counts[2]+=(traces(s,false)==4);strict[2]+=(traces(s,true)==4);
    for(int c=b+1;c<27;c++){
      s={a,b,c};alltri.push_back({a,b,c});counts[3]+=(traces(s,false)==8);strict[3]+=(traces(s,true)==8);
      for(int d=c+1;d<27;d++){
        s={a,b,c,d};if(traces(s,false)==16) {fours.push_back({a,b,c,d});counts[4]++;}
        if(traces(s,true)==16)strict[4]++;
      }
    }
   }
 }
 assert(counts[1]==27 && counts[2]==351 && counts[3]==2925 && counts[4]==5967);
 assert(strict[1]==27 && strict[2]==351 && strict[3]==2925 && strict[4]==0);
 int id[27][27][27];fill(&id[0][0][0],&id[0][0][0]+27*27*27,-1);
 for(int i=0;i<(int)alltri.size();i++){auto x=alltri[i];id[x[0]][x[1]][x[2]]=i;}
 vector<int> incidence(2925,0);
 map<int,vector<uint64_t>> piv;int rank=0;
 for(auto s:fours){vector<uint64_t> col(46,0);
  for(int removed=0;removed<4;removed++){T3 tri{};int j=0;for(int i=0;i<4;i++)if(i!=removed)tri[j++]=s[i];int k=id[tri[0]][tri[1]][tri[2]];assert(k>=0);incidence[k]++;col[k>>6]^=1ULL<<(k&63);}
  while(true){int k=-1;for(int j=45;j>=0;j--)if(col[j]){k=(j<<6)+63-__builtin_clzll(col[j]);break;}if(k<0)break;
   auto p=piv.find(k);if(p==piv.end()){piv.emplace(k,std::move(col));rank++;break;}
   for(int j=0;j<46;j++)col[j]^=p->second[j];
  }
 }
 assert(rank==2249);
 int unextended=count(incidence.begin(),incidence.end(),0);assert(unextended==351);
 map<int,int> ihist;for(int x:incidence)ihist[x]++;
 assert((ihist==map<int,int>({{0,351},{5,351},{8,1053},{9,117},{12,1053}})));
 // Verify affine semilinear symmetry orbits without using canonical representatives.
 vector<array<int,27>> perms;
 for(int j=0;j<3;j++)for(int m:squares)for(int b=0;b<27;b++){
   array<int,27> f{};for(int x=0;x<27;x++)f[x]=add(mul(m,power(x,(j==0?1:j==1?3:9))),b);perms.push_back(f);
 }
 assert(perms.size()==1053);
 set<T4> unseen(fours.begin(),fours.end());map<int,int> ohist;
 while(!unseen.empty()){
   auto s=*unseen.begin();set<T4> orbit;
   for(auto &f:perms){T4 z{};for(int i=0;i<4;i++)z[i]=f[s[i]];sort(z.begin(),z.end());orbit.insert(z);}
   for(auto z:orbit){assert(unseen.erase(z)==1);}
   ohist[(int)orbit.size()]++;
 }
 assert((ohist==map<int,int>({{351,2},{1053,5}})));
 cout<<"FIELD GF(3)[t]/(t^3-t-1) squares="<<squares.size()<<"\n";
 cout<<"SHATTERED 1,27,351,2925,5967; OFF_SUPPORT 1,27,351,2925,0\n";
 cout<<"QUARTET_ORBITS 2x351 + 5x1053\n";
 cout<<"TRIPLES_WITH_NO_QUARTET_EXTENSION "<<unextended<<"\n";
 cout<<"INCIDENCE_0_5_8_9_12 351 351 1053 117 1053\n";
 cout<<"BOUNDARY_RANKS_1_2_3 26 325 "<<rank<<"\n";
 cout<<"BETTI_2_3 "<<(2925-325-rank)<<" "<<(5967-rank)<<"\n";
 cout<<"CPP_INDEPENDENT_EXHAUSTIVE_OK\n";
}
