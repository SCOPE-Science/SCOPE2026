// Direct, nonalgebraic exhaustive census of every press subset on two cubic ladders.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
using namespace std;
using U = uint64_t;
map<int,U> expected(const string& kind,int n,int t){
 if(n%2) return t ? map<int,U>{{n,2}} : map<int,U>{{0,1},{2*n,1}};
 if(kind=="mobius"){
  if(n%4==0) return t ? map<int,U>{{n,4}} : map<int,U>{{0,1},{n,2},{2*n,1}};
  return t ? map<int,U>{{n/2,4},{3*n/2,4}} : map<int,U>{{0,1},{n,6},{2*n,1}};
 }
 if(n%4==2) return t ? map<int,U>{{n,4}} : map<int,U>{{0,1},{n,2},{2*n,1}};
 return t ? map<int,U>{{n/2,4},{n,8},{3*n/2,4}} : map<int,U>{{0,1},{n,14},{2*n,1}};
}
int main(){
 int tested=0;
 for(int n=3;n<=11;n++)for(auto kind:{string("mobius"),string("prism")}){
  int N=2*n;array<U,22> col{};
  for(int i=0;i<N;i++){
   array<int,4> nei;
   if(kind=="mobius") nei={(i-1+N)%N,i,(i+1)%N,(i+n)%N};
   else {int l=i/n,j=i%n;nei={i,l*n+(j+n-1)%n,l*n+(j+1)%n,(1-l)*n+j};}
   for(int v:nei)col[i]|=U(1)<<v;
   assert(__builtin_popcountll(col[i])==4);
  }
  map<int,U> cnt0,cnt1;
  U out=0,prev=0;
  U target=(U(1)<<N)-1;
  for(U t=0;t<(U(1)<<N);t++){
   U gray=t^(t>>1);
   if(t){U diff=prev^gray;int pos=__builtin_ctzll(diff);out^=col[pos];}
   prev=gray;
   int weight=__builtin_popcountll(gray);
   if(out==0)cnt0[weight]++;
   if(out==target)cnt1[weight]++;
  }
  assert(cnt0==expected(kind,n,0));
  assert(cnt1==expected(kind,n,1));
  tested+=2;
 }
 cout<<"PASS: "<<tested<<" complete subsets censuses on 3 <= n <= 11; direct neighbor toggles"<<endl;
}
