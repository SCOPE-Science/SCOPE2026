// Independent exact verifier for the ternary three-cube antipodal family.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
#include <array>
#include <bitset>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
static int digits[27][3];
static unsigned int sets[27];
int distance_(int a, int b){int count=0;for(int i=0;i<3;i++)count+=(digits[a][i]!=digits[b][i]);return count;}
int trace_count(const vector<int>& s){
  bool seen[16] = {false};int cnt=0;
  for(int c=0;c<27;c++){
    int t=0;for(int j=0;j<(int)s.size();j++) if((sets[c]>>s[j])&1U)t|=1<<j;
    if(!seen[t]){seen[t]=true;cnt++;}
  }
  return cnt;
}
int main(){
 for(int i=0;i<27;i++){digits[i][0]=i/9;digits[i][1]=(i/3)%3;digits[i][2]=i%3;}
 for(int c=0;c<27;c++)for(int x=0;x<27;x++)if(distance_(c,x)==3)sets[c]|=1U<<x;
 int f1=0,f2=0,f3=0,f4=0, special_n=0;
 vector<array<int,2>> edges;
 vector<array<int,3>> faces;
 for(int a=0;a<27;a++)if(trace_count({a})==2)f1++;
 for(int a=0;a<27;a++)for(int b=a+1;b<27;b++){
   bool yes=trace_count({a,b})==4;
   if(yes){f2++;edges.push_back({a,b});}
 }
 for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)for(int c=b+1;c<27;c++){
   bool p=distance_(a,b)==2 && distance_(a,c)==2 && distance_(b,c)==2;
   for(int j=0;j<3;j++){
      bool distinct=digits[a][j]!=digits[b][j] && digits[a][j]!=digits[c][j] && digits[b][j]!=digits[c][j];
      if(distinct)p=false;
   }
   bool s=trace_count({a,b,c})==8;
   assert(p==s);
   if(s){f3++;faces.push_back({a,b,c});special_n++;}
 }
 for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)for(int c=b+1;c<27;c++)for(int d=c+1;d<27;d++)if(trace_count({a,b,c,d})==16)f4++;
 assert(f1==27&&f2==351&&f3==216&&f4==0&&special_n==216);
 int id[27][27];for(auto &row:id)for(int &j:row)j=-1;
 for(int j=0;j<(int)edges.size();j++){auto e=edges[j];id[e[0]][e[1]]=j;}
 bitset<351> pivots[351];bool pivot_exists[351]={false};int rank=0;
 for(auto t:faces){bitset<351> v;v.set(id[t[0]][t[1]]);v.set(id[t[0]][t[2]]);v.set(id[t[1]][t[2]]);
   while(v.any()){int p=-1;for(int j=350;j>=0;j--)if(v[j]){p=j;break;}
     if(pivot_exists[p])v^=pivots[p];else{pivot_exists[p]=true;pivots[p]=v;rank++;break;}}
 }
 assert(rank==133);
 int maximal_edges=0;
 for(auto e:edges){bool contained=false;for(auto t:faces)if((e[0]==t[0]||e[0]==t[1]||e[0]==t[2])&&(e[1]==t[0]||e[1]==t[1]||e[1]==t[2])){contained=true;break;}if(!contained)maximal_edges++;}
 assert(maximal_edges==189);
 assert(351-26-rank==192&&216-rank==83);
 cout << "PASS C++: faces 1,27,351,216; maximal edges 189; triangles 216; boundary rank 133; mod-2 reduced Betti numbers 192,83\n";
}
