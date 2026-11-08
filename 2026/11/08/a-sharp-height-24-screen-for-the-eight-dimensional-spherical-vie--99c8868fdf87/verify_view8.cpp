#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using i64=long long;
struct Event {int k,v;};
struct Score {i64 num,den;};
bool lessQ(Score a,Score b){return (__int128)a.num*b.den < (__int128)b.num*a.den;}
bool equalQ(Score a,Score b){return (__int128)a.num*b.den == (__int128)b.num*a.den;}
Score exact_score(const array<int,8>& v){
 i64 Q=0,CV=0,C2=8;
 vector<Event> events;
 for(int a:v){Q+=i64(a)*a;CV+=a;for(int k=1;2*k<a;k++)events.push_back({k,a});}
 sort(events.begin(),events.end(),[](Event a,Event b){return a.k*b.v<b.k*a.v;});
 i64 min_num=Q*C2-CV*CV;
 for(size_t i=0;i<events.size();){
  size_t j=i;
  while(j<events.size() && events[j].k*events[i].v==events[i].k*events[j].v){
   CV+=2*events[j].v;
   C2+=8*events[j].k;
   j++;
  }
  min_num=min(min_num,Q*C2-CV*CV);
  i=j;
 }
 return {min_num,4*Q};
}
int main(int argc,char**argv){
 int B=argc>1?atoi(argv[1]):24;
 if(B<1 || B>50)return 2;
 array<int,8> v{};
 Score best={0,1};
 vector<array<int,8>> champions;
 uint64_t count=0;
 auto dfs = [&](auto&& self,int k,int lower)->void {
  if(k==8){
    count++;
    Score s=exact_score(v);
    if(lessQ(best,s)){best=s;champions.assign(1,v);}
    else if(equalQ(best,s)) champions.push_back(v);
    return;
  }
  for(int x=lower;x<=B;x++){
   v[k]=x;
   self(self,k+1,x);
  }
 };
 dfs(dfs,0,1);
 i64 g=gcd(best.num,best.den);
 cout<<"EXACT_ENUM B="<<B<<" nondecreasing_tuples="<<count
     <<" max="<<best.num/g<<"/"<<best.den/g<<" optimizing_tuples="<<champions.size()<<"\n";
 for(auto& x:champions){
   int g=0;
   for(auto a:x){cout<<a<<' ';g=gcd(g,a);}
   cout<<" gcd="<<g<<"\n";
 }
}
