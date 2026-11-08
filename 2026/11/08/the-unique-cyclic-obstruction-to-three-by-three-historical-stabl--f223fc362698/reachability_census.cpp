#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;
struct Market {
 int men[3][3], women[3][3], rm[3][3], rw[3][3];
 void setup(const array<int,6>& codes, const vector<array<int,3>>& perms) {
  for(int i=0;i<3;i++)for(int j=0;j<3;j++){
   men[i][j]=perms[codes[i]][j]; women[i][j]=perms[codes[i+3]][j];
   rm[i][men[i][j]]=j; rw[i][women[i][j]]=j;
  }
 }
 bool stable(int mask,const array<int,3>& a) const {
  int b[3]={-1,-1,-1};
  for(int i=0;i<3;i++)if(a[i]>=0){
   if(!(mask&(1<<i)) || !(mask&(1<<(a[i]+3))) || b[a[i]]>=0)return false;
   b[a[i]]=i;
  }
  for(int i=0;i<3;i++)if(!(mask&(1<<i))&&a[i]>=0)return false;
  for(int i=0;i<3;i++)if(mask&(1<<i))for(int j=0;j<3;j++)if(mask&(1<<(j+3))){
   if(rm[i][j]<(a[i]==-1?3:rm[i][a[i]]) && rw[j][i]<(b[j]==-1?3:rw[j][b[j]]))return false;
  }
  return true;
 }
 array<int,3> chain(int entrant, array<int,3> a) const {
  int b[3]={-1,-1,-1}; for(int i=0;i<3;i++)if(a[i]>=0)b[a[i]]=i;
  bool enteringMan=entrant<3; int prop=enteringMan?entrant:entrant-3;
  int tries=0;
  for(int z=0;z<18;z++){
   bool moved=false;
   for(int k=0;k<3;k++){
    int target=enteringMan?men[prop][k]:women[prop][k];
    if(enteringMan) {
     if(rw[target][prop] < (b[target]<0?3:rw[target][b[target]])){
      int old=b[target];b[target]=prop;a[prop]=target;
      if(old>=0){a[old]=-1;prop=old;}else return a;
      moved=true;break;
     }
    }else{
     if(rm[target][prop] < (a[target]<0?3:rm[target][a[target]])){
      int old=a[target];a[target]=prop;b[prop]=target;
      if(old>=0){b[old]=-1;prop=old;}else return a;
      moved=true;break;
     }
    }
    tries++;
   }
   if(!moved)return a;
  }
  cerr<<"chain exceeded"<<endl;abort();
 }
 vector<array<int,3>> getStable(int mask) const {
  vector<array<int,3>> out;
  for(int i=-1;i<3;i++)for(int j=-1;j<3;j++)for(int k=-1;k<3;k++){
   array<int,3> a={i,j,k};
   if(stable(mask,a))out.push_back(a);
  }
  return out;
 }
};
int main(){
 vector<array<int,3>> perms;
 array<int,3> x={0,1,2};do{perms.push_back(x);}while(next_permutation(x.begin(),x.end()));
 Market m; map<pair<int,int>,long long> distribution; map<int,long long> badByK;
 long long total=0,bad=0,unreachable=0;
 for(int c0=0;c0<6;c0++)for(int c1=0;c1<6;c1++)for(int c2=0;c2<6;c2++)
 for(int c3=0;c3<6;c3++)for(int c4=0;c4<6;c4++)for(int c5=0;c5<6;c5++){
  array<int,6> codes={c0,c1,c2,c3,c4,c5};m.setup(codes,perms);
  auto all=m.getStable(63);
  bool reachable[3][3][3]={};
  for(int missing=0;missing<6;missing++){
   int mask=63^(1<<missing);auto prev=m.getStable(mask);
   for(auto a:prev){
    auto nxt=m.chain(missing,a);
    if(!m.stable(63,nxt)){cerr<<"BUG unstable"<<endl; return 1;}
    reachable[nxt[0]][nxt[1]][nxt[2]]=true;
   }
  }
  int r=0;for(auto a:all)r+=reachable[a[0]][a[1]][a[2]];
  if(r==0){cerr<<"no reachable";return 1;}
  distribution[{int(all.size()),r}]++;
  total++;
  if(r<int(all.size())){bad++;unreachable+=int(all.size())-r;badByK[int(all.size())]++;}
 }
 cout<<"profiles "<<total<<" bad "<<bad<<" unreachable outcomes "<<unreachable<<"\n";
 for(auto [key,v]:distribution)cout<<"stable "<<key.first<<" reachable "<<key.second<<" profiles "<<v<<"\n";
}
