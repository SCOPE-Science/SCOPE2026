#include <bits/stdc++.h>
using namespace std;
int main(){
vector<pair<int,int>> edges={{0,9},{0,10},{0,12},{0,16},{0,21},{1,8},{1,11},{1,13},{1,17},{1,20},{2,8},{2,11},{2,14},{2,18},{2,23},{3,9},{3,10},{3,15},{3,19},{3,22},{4,8},{4,12},{4,14},{4,16},{4,20},{5,9},{5,13},{5,15},{5,17},{5,21},{6,10},{6,12},{6,14},{6,18},{6,22},{7,11},{7,13},{7,15},{7,19},{7,23},{8,14},{8,20},{9,15},{9,21},{10,12},{10,22},{11,13},{11,23},{12,16},{13,17},{14,18},{15,19},{16,20},{16,21},{17,20},{17,21},{18,22},{18,23},{19,22},{19,23}};
uint32_t nbr[24]={};for(auto [u,v]:edges){nbr[u]|=1u<<v;nbr[v]|=1u<<u;}
const uint32_t N=(1u<<24); int cut=0,m=-24; uint32_t mask=0;
int globalMax=-1; array<int,25> maxcut;array<long long,25> countAtMax; maxcut.fill(-1);countAtMax.fill(0);
uint64_t sum=0;
for(uint32_t step=0;step<N;++step){
 int mi=(m+24)/2; if(cut>maxcut[mi]){maxcut[mi]=cut;countAtMax[mi]=1;}else if(cut==maxcut[mi])countAtMax[mi]++;
 if(cut>globalMax)globalMax=cut;

 if(step+1==N)break;
 int bit=__builtin_ctz(step+1); uint32_t adj=nbr[bit];
 int ones=__builtin_popcount(adj&mask); int deg=__builtin_popcount(adj);
 if(!(mask&(1u<<bit))){cut+=deg-2*ones; m+=2;mask|=(1u<<bit);} else {cut+=2*ones-deg; m-=2;mask&=~(1u<<bit);}
}
cout<<"maxcut "<<globalMax<<" groundE/J "<<60-2*globalMax<<"\n";
long long total=0;
for(int x=-24;x<=24;x+=2){int mi=(x+24)/2; if(maxcut[mi]==globalMax){total+=countAtMax[mi];cout<<"GS_M "<<x<<" count "<<countAtMax[mi]<<"\n";}}
cout<<"total "<<total<<"\n";
for(int x=-24;x<=24;x+=2){int i=(x+24)/2;cout<<"MAXCUT_BY_M "<<x<<" "<<maxcut[i]<<" "<<countAtMax[i]<<"\n";}
bool ok=(globalMax==44 && total==18);
for(int q=0;q<=12;++q){
  const int target[13]={0,5,10,15,20,25,30,35,40,41,42,43,44};
  const long long expected[13]={1,24,216,912,1854,1680,564,48,3,24,84,72,18};
  int mi=24-q; if(maxcut[mi]!=target[q] || countAtMax[mi]!=expected[q])ok=false;
}
if(!ok){cerr<<"FULL_ENUMERATION_FAILED\n";return 1;}
cout<<"VERIFY_EXHAUSTIVE_OK 16777216 configurations\n";
}
