// Finite ambiguity in three-state singleton-component chain automata.
// Uses integer path matrices; no floating-point or external dependencies.
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using Matrix=std::array<int,9>;
Matrix identity(){return {1,0,0,0,1,0,0,0,1};}
Matrix letter(int mask){Matrix m{}; const int cells[5]={0,1,4,5,8};for(int i=0;i<5;i++)m[cells[i]]=(mask>>i)&1;return m;}
Matrix product(Matrix a,Matrix b){Matrix c{};for(int i=0;i<3;i++)for(int k=0;k<3;k++)for(int j=0;j<3;j++)c[3*i+j]+=a[3*i+k]*b[3*k+j];return c;}
bool admissible(int t,int side){const bool a=t&1,b=t&2,c=t&4,d=t&8,e=t&16;
 if(a&&b&&c)return false;
 if(c&&d&&e)return false;
 if(side==0&&a&&b&&e)return false;
 if(side==1&&a&&d&&e)return false;
 return true;
}
std::set<Matrix> orbit(const std::vector<int>& alphabet){
 std::set<Matrix> result;std::queue<Matrix> q;auto I=identity();result.insert(I);q.push(I);
 while(!q.empty()){auto a=q.front();q.pop();for(int t:alphabet){auto b=product(a,letter(t));if(result.insert(b).second)q.push(b);}}
 return result;
}
int main(){
 std::vector<int> A[2];
 for(int s=0;s<2;s++){
  for(int t=0;t<32;t++)if(admissible(t,s))A[s].push_back(t);
  assert(A[s].size()==23);auto closure=orbit(A[s]);assert(closure.size()==48);
  int bound=0;for(auto M:closure)bound=std::max(bound,M[2]);assert(bound==4);
  std::cout<<"family "<<(s==0?'X':'Y')<<" has 23 generators, 48 products, maximum 4\n";
 }
 std::map<int,int> counts;
 for(int x=0;x<32;x++)for(int y=0;y<32;y++){
  if(!((x|y)&2)||!((x|y)&8))continue;
  if(!((admissible(x,0)&&admissible(y,0))||(admissible(x,1)&&admissible(y,1))))continue;
  auto c=orbit({x,y});int maximum=0;for(auto m:c)maximum=std::max(maximum,m[2]);
  assert(maximum>=1&&maximum<=3);counts[maximum]++;
 }
 assert(counts[1]==216&&counts[2]==28&&counts[3]==2);
 auto witness=[](const std::vector<int>&types,const std::string&w)->int{
  std::array<int,3> vec{1,0,0};
  for(char c:w){Matrix m=letter(types.at(c-'a'));std::array<int,3> next{};
   for(int i=0;i<3;i++){for(int j=0;j<3;j++){next[j]+=vec[i]*m[3*i+j];}}
   vec=next;}
  return vec[2];};
 assert(witness({10},"aa")==1);
 assert(witness({11,26},"aabb")==3);
 assert(witness({3,14,24},"abbc")==4);
 std::cout<<"binary degrees: ";for(auto [k,v]:counts)std::cout<<k<<":"<<v<<" ";std::cout<<"\nVERIFY_OK\n";
}
