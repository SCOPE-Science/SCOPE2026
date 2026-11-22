#include <array>
#include <iostream>
#include <vector>
#include <map>
#include <cstdint>
#include <algorithm>
using namespace std;
struct Pt {int x,y;};
int main(){
 vector<Pt> S;
 for(int x=-2;x<=2;x++)for(int y=-2;y<=2;y++)if(max({abs(x),abs(y),abs(x+y)})<=2)S.push_back({x,y});
 int n=S.size();
 int anchor=find_if(S.begin(),S.end(),[](Pt p){return p.x==0&&p.y==0;})-S.begin();
 map<pair<int,int>,int> shifts;
 struct Edge{int j,k;}; vector<vector<Edge>> edges(n);
 for(int i=0;i<n;i++) for(int j=i+1;j<n;j++){
  int dx=S[i].x-S[j].x,dy=S[i].y-S[j].y;
  if(dx<0||(dx==0&&dy<0))dx=-dx,dy=-dy;
  auto [it,newone]=shifts.emplace(make_pair(dx,dy),shifts.size());
  int k=it->second;edges[i].push_back({j,k});edges[j].push_back({i,k});
 }
 int nshift=shifts.size(); vector<int> C(nshift,0);vector<int> a(n,1);
 for(int i=0;i<n;i++)for(const auto&e:edges[i])if(i<e.j)C[e.k]++;
 long long en=n*n;for(int z:C)en+=2LL*z*z;
 vector<int> freeidx;for(int i=0;i<n;i++)if(i!=anchor)freeidx.push_back(i);
 long long minval=1LL<<62,next=1LL<<62,maxval=-1; uint64_t nmin=0;vector<uint32_t> minimizers;map<long long,long long> hist;
 uint32_t prev=0, states=1u<<freeidx.size();
 for(uint32_t step=0;step<states;step++){
  if(step){uint32_t g=step^(step>>1);uint32_t diff=g^prev;int b=__builtin_ctz(diff),i=freeidx[b];
   int dC[100]={};
   for(const auto&e:edges[i])dC[e.k]-=2*a[i]*a[e.j];
   for(int k=0;k<nshift;k++)if(dC[k]){en+=2LL*((long long)(C[k]+dC[k])*(C[k]+dC[k])-(long long)C[k]*C[k]);C[k]+=dC[k];}
   a[i]=-a[i];prev=g;
  }
  hist[en]++;maxval=max(maxval,en);
  if(en<minval){next=minval;minval=en;nmin=1;minimizers.assign(1,prev);}else if(en==minval){nmin++;minimizers.push_back(prev);}else if(en<next)next=en;
 }
 cout<<"n="<<n<<" shifts="<<nshift<<" anchor="<<anchor<<" states="<<states<<" min="<<minval<<" next="<<next<<" max="<<maxval<<" nmin_gauge="<<nmin<<"\n";
 cout<<"coords=";for(Pt p:S)cout<<"("<<p.x<<","<<p.y<<")";cout<<"\n";
 cout<<"hist_first=";int count=0;for(auto [v,c]:hist){if(count++==12)break;cout<<"("<<v<<","<<c<<")";}cout<<"\n";
 cout<<"minimizers=";for(uint32_t m:minimizers)cout<<m<<",";cout<<"\n";
 bool ok=(n==19&&nshift==30&&states==262144&&minval==467&&next==475&&maxval==3259&&nmin==72);
 cout<<(ok?"INCREMENTAL_EXHAUSTIVE_PASS":"INCREMENTAL_EXHAUSTIVE_FAIL")<<"\n";
 return ok?0:1;
}
