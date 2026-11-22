// Exact enumeration of size-eight induced online-shattering witnesses in C5 square C5.
// Compile: g++ -std=c++17 -O2 verify_census.cpp -o verify_census && ./verify_census
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
constexpr int P=5, V=25;
U neigh[V];
int idx(int x,int y){return ((x%P+P)%P)*P+(y%P+P)%P;}
int pc(U z){return __builtin_popcount(z);}
vector<int> vertices(U m){vector<int> v;for(int j=0;j<V;j++)if(m&(U(1)<<j))v.push_back(j);return v;}
bool separate(U E,int a,int b){
 for(int z:vertices(E))if(bool(neigh[z]&(U(1)<<a))!=bool(neigh[z]&(U(1)<<b)))return true;
 return false;
}
bool depth2(U E,U group){
 if(pc(group)!=4)return false;
 for(int z:vertices(E)){
  U A=group&neigh[z];U B=group&~neigh[z];
  if(pc(A)!=2 || pc(B)!=2)continue;
  auto a=vertices(A), b=vertices(B);
  if(separate(E,a[0],a[1]) && separate(E,b[0],b[1]))return true;
 }
 return false;
}
bool depth3root(U E,int root){
 if(!(E&(U(1)<<root)))return false;
 U pos=E&neigh[root],neg=E&~neigh[root];
 return pc(pos)==4&&pc(neg)==4&&depth2(E,pos)&&depth2(E,neg);
}
bool depth3(U E){for(int x:vertices(E))if(depth3root(E,x))return true;return false;}
U transform(U E,int sx,int sy,int sw,int dx,int dy){
 U out=0;
 for(int j:vertices(E)){
   int x=j/P,y=j%P;if(sw)swap(x,y);
   out|=U(1)<<idx(sx*x+dx,sy*y+dy);
 }
 return out;
}
int main(){
 for(int x=0;x<P;x++)for(int y=0;y<P;y++){
  int a=idx(x,y);neigh[a]=0;
  for(int v=0;v<V;v++){
   int dx=(x-v/P+P)%P,dy=(y-v%P+P)%P;
   if((dx==0&&(dy==1||dy==4))||(dy==0&&(dx==1||dx==4)))neigh[a]|=U(1)<<v;
  }
  assert(pc(neigh[a])==4);
 }
 U root_fixed=neigh[0]|U(1);
 vector<int> extra=vertices(((U(1)<<V)-1)&~root_fixed);
 assert(extra.size()==20);
 vector<U> rooted;
 for(int a=0;a<20;a++)for(int b=a+1;b<20;b++)for(int c=b+1;c<20;c++){
  U E=root_fixed|(U(1)<<extra[a])|(U(1)<<extra[b])|(U(1)<<extra[c]);
  if(depth3root(E,0))rooted.push_back(E);
 }
 assert(rooted.size()==84);
 set<U> all;
 for(U E:rooted)for(int x=0;x<P;x++)for(int y=0;y<P;y++)all.insert(transform(E,1,1,0,x,y));
 assert(all.size()==2050);
 long root_pairs=0;map<int,int> multiplicities;
 for(U E:all){
  int r=0;
  for(int x:vertices(E))r+=depth3root(E,x);
  assert(r>=1);root_pairs+=r;multiplicities[r]++;
 }
 assert(root_pairs==2100);
 assert(multiplicities[1]==2000&&multiplicities[2]==50&&multiplicities.size()==2);
 map<int,int> orbit_sizes;int number_of_orbits=0;
 set<U> remaining=all;
 while(!remaining.empty()){
  U E=*remaining.begin();set<U> orb;
  for(int sx:{-1,1})for(int sy:{-1,1})for(int sw:{0,1})
    for(int dx=0;dx<P;dx++)for(int dy=0;dy<P;dy++)orb.insert(transform(E,sx,sy,sw,dx,dy));
  for(U F:orb)assert(all.count(F));
  for(U F:orb)remaining.erase(F);
  number_of_orbits++;orbit_sizes[orb.size()]++;
 }
 assert(number_of_orbits==12);
 assert(orbit_sizes[200]==9&&orbit_sizes[100]==2&&orbit_sizes[50]==1&&orbit_sizes.size()==3);
 // Full independent classification: all size-eight supports with a depth-three tree
 // must have some root and its four neighbors, so the 25 translates above suffice.
 cout<<"PENTAGONAL_LOCAL_ONLINE_PASS rooted=84 count=2050 root_pairs=2100 roots_1=2000 roots_2=50 orbits=12 orbit_200=9 orbit_100=2 orbit_50=1\n";
}
