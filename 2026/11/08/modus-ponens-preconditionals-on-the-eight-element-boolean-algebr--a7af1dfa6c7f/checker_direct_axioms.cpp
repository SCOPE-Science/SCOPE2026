#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
using namespace std;
static constexpr int N=8;
int main(){
 vector<array<int,N>> choices[N];
 for(int a=0;a<N;++a){
  vector<int> subs, outs;
  for(int x=0;x<N;++x){if((x&a)==x)subs.push_back(x);if((x&a)==0)outs.push_back(x);}
  size_t total=1;for(size_t i=0;i<subs.size();++i)total*=outs.size();
  for(size_t z=0;z<total;++z){
   array<int,N> row{};size_t t=z;
   for(int x:subs){row[x]=x|outs[t%outs.size()];t/=outs.size();}
   bool monotone=true;
   for(int x:subs)for(int y:subs)if((x&y)==x && (row[x]&row[y])!=row[x])monotone=false;
   if(!monotone)continue;
   array<int,N> expanded{};for(int b=0;b<N;++b)expanded[b]=row[b&a];
   choices[a].push_back(expanded);
  }
 }
 array<array<int,N>,N> op{};long long count=0;long long byempty[8]={};
 long long considered=0;
 auto evaluate=[&](){
  ++considered;
  for(int a=0;a<N;++a)for(int b=0;b<N;++b){
   if(a==N-1&&((op[a][b]&~b)!=0 || (b&~op[a][b])!=0))return;
   if((a&b&~op[a][b])!=0)return;
   if((op[a][b]&~op[a][a&b])!=0)return;
   if((a&op[a][b]&~b)!=0)return;
   for(int c=0;c<N;++c){
    if((op[a][b&c]&~op[a][b])!=0)return;
    if((op[a][op[a&b][c]]&~op[a&b][c])!=0)return;
   }
  }
  ++count;++byempty[op[0][0]];
 };
 auto rec=[&](auto&& self,int a)->void{
  if(a==N){evaluate();return;}
  for(const auto &row:choices[a]){op[a]=row;self(self,a+1);}
 };rec(rec,0);
 cout<<"candidate_tuples "<<considered<<" valid "<<count<<" by_empty";
 for(int a=0;a<N;++a)cout<<' '<<byempty[a];cout<<'\n';
 if(count!=19127 || considered!=1259712)return 1;
}
