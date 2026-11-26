#include <algorithm>
#include <array>
#include <iostream>
#include <cassert>
#include <map>
#include <vector>
using namespace std;
int main(){
 vector<array<int,4>> ps;
 array<int,4> a={0,1,2,3}; do{ps.push_back(a);}while(next_permutation(a.begin(),a.end()));
 map<array<int,4>,int> ix; for(int i=0;i<24;i++)ix[ps[i]]=i;
 long long hs[25]={0}; map<vector<int>,long long> shapes;
 for(int v0=0;v0<24;v0++)for(int v1=0;v1<24;v1++)for(int v2=0;v2<24;v2++)for(int v3=0;v3<24;v3++){
  int v[]={v0,v1,v2,v3}; int counts[24]={};
  for(int pi=0;pi<24;pi++){
   int mask=0;array<int,4> ans;
   for(int j=0;j<4;j++){
    int ag=ps[pi][j];
    for(int x:ps[v[ag]])if((mask&(1<<x))==0){ans[ag]=x;mask|=1<<x;break;}
   }
   assert(mask==15); auto it=ix.find(ans);assert(it!=ix.end());++counts[it->second];
  }
  int supp=0;vector<int> shape;
  for(auto x:counts)if(x){supp++;shape.push_back(x);}
  sort(shape.begin(),shape.end());
  hs[supp]++; shapes[shape]++;
 }
 const map<int,long long> expected={{1,31104},{2,20736},{3,20736},{4,53856},{5,48384},{6,40032},{7,45504},{8,26568},{9,12672},{10,15120},{11,6336},{12,5880},{14,4032},{16,216},{18,576},{24,24}};
 long long n=0, sum_support=0;
 for(int i=0;i<25;i++){n+=hs[i];sum_support+=(long long)i*hs[i];auto it=expected.find(i);assert(hs[i]==(it==expected.end()?0:it->second));}
 assert(n==331776 && sum_support==1839744 && shapes.size()==57);
 cout<<"VERIFY_OK labeled exhaustive 331776 profiles, 24 priorities each, 57 multiplicity shapes\n";
 cout<<"HIST\n";for(int i=0;i<25;i++)if(hs[i])cout<<i<<" "<<hs[i]<<"\n";
 cout<<"SHAPES "<<shapes.size()<<"\n";
 for(auto [shape,count]:shapes){cout<<count<<" :";for(int x:shape)cout<<" "<<x;cout<<"\n";}
}
