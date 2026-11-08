#include <iostream>
#include <vector>
#include <array>
#include <map>
using namespace std;
using A=array<int,4>;
int prod(int x,int y,int typ){if(!typ)return (x*y)%25;int a=x%5,b=x/5,c=y%5,d=y/5;return (a*c)%5+5*((a*d+b*c)%5);}
int add(int x,int y,int typ){if(!typ)return (x+y)%25;return (x%5+y%5)%5+5*((x/5+y/5)%5);}
A mul(const A&a,const A&b,int typ){A c{};for(int i=0;i<2;i++)for(int j=0;j<2;j++){int s=0;for(int k=0;k<2;k++)s=add(s,prod(a[2*i+k],b[2*k+j],typ),typ);c[2*i+j]=s;}return c;}
int main(){A id{1,0,0,1};for(int typ=0;typ<2;typ++){
vector<A> inv;for(int i=0;i<25;i++)for(int j=0;j<25;j++)for(int k=0;k<25;k++)for(int l=0;l<25;l++){
 A a{i,j,k,l}; if(((i%5)*(l%5)-(j%5)*(k%5)+25)%5==0)continue;
 if(mul(a,a,typ)==id)inv.push_back(a);
}
map<int,long long> orders;long long commuting=0;
for(const auto&a:inv)for(const auto&b:inv){A p=mul(a,b,typ);if(p==mul(b,a,typ))commuting++;A t=id;int ord=-1;for(int z=1;z<=300;z++){t=mul(t,p,typ);if(t==id){ord=z;break;}}orders[ord]++;}
cout<<(typ==0?"Z25":"dual5")<<" inv="<<inv.size()<<" commuting="<<commuting<<" orders:";for(auto [a,b]:orders)cout<<" "<<a<<":"<<b;cout<<"\n";
}}
