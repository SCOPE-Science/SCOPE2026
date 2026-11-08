#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <numeric>
#include <string>
using namespace std;
using U=uint32_t;
static const int n=5;
struct Perm{array<int,n> p;array<uint8_t,1<<n> c;};
vector<Perm> perms;
static inline U transformed(U x,const Perm &g){U r=0;for(int i=0;i<n;i++){U v=(x>>(n*i))&31u;r|=(U)g.c[v]<<(n*g.p[i]);}return r;}
static inline bool nonsingular(U x){uint8_t row[n];for(int i=0;i<n;i++)row[i]=uint8_t((x>>(n*i))&31);int piv=0;for(int c=0;c<n;c++){int j=piv;while(j<n&&!(row[j]&(1<<c)))j++;if(j==n)continue;swap(row[piv],row[j]);for(int t=piv+1;t<n;t++)if(row[t]&(1<<c))row[t]^=row[piv];piv++;}return piv==n;}
int main(){array<int,n> p{0,1,2,3,4};do{Perm q; q.p=p;for(int x=0;x<(1<<n);x++){int y=0;for(int i=0;i<n;i++)if((x>>i)&1)y|=1<<p[i];q.c[x]=y;}perms.push_back(q);}while(next_permutation(p.begin(),p.end()));
 uint64_t all=0,classes=0,by_labeled=0;map<int,uint64_t> by_aut; map<std::string,uint64_t> by_type;
 for(U x=0;x<(1u<<(n*n));x++){
  if(!nonsingular(x))continue;all++;bool rep=true;int fixed=0; int c2=0,c3=0,c4=0,c5=0,c6=0;
  for(const auto &g:perms){U y=transformed(x,g);if(y<x){rep=false;break;}if(y==x){fixed++;int order=1;array<bool,n> used{};for(int i=0;i<n;i++)if(!used[i]){int a=i,len=0;do{used[a]=true;a=g.p[a];len++;}while(a!=i);order=std::lcm(order,len);}if(order==2)c2++;if(order==3)c3++;if(order==4)c4++;if(order==5)c5++;if(order==6)c6++;}}
  if(rep){if(fixed==0 || (perms.size()%fixed)!=0){cerr<<"bad stabilizer";return 1;}by_aut[fixed]++; std::string name;switch(fixed){case 1:name="1";break;case 2:name="C2";break;case 3:name="C3";break;case 4:name=c4?"C4":"V4";break;case 5:name="C5";break;case 6:name=c6?"C6":"S3";break;case 8:name="D8";break;case 10:name="D10";break;case 12:name=c6?"S3xC2":"A4";break;case 24:name="S4";break;case 120:name="S5";break;default:name="UNCLASSIFIED";}by_type[name]++; classes++;by_labeled+=perms.size()/fixed;}
 }
 cout<<"count nonsingular="<<all<<" orbits="<<classes<<" reconstructed_labeled="<<by_labeled<<"\n";
 for(auto [k,v]:by_aut)cout<<k<<":"<<v<<" ";cout<<"\n";
 if(all!=9999360 || classes!=85411 || by_labeled!=all)return 2;
 for(auto [name,cnt]:by_type)cout<<"TYPE "<<name<<" "<<cnt<<"\n";cout<<"VERIFY_OK\n";
}
