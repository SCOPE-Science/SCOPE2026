// Independently test the actual defining condition, not the degree-support reduction.
// Each vertex of T_n is an edge of K_n and neighbors share an endpoint.
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int main(){
 for(int n=3;n<=6;n++){
  vector<pair<int,int>> edge;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edge.push_back({a,b});
  int m=edge.size(); vector<int> nei(m,0);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){
   auto [a,b]=edge[i];auto [c,d]=edge[j];
   if(a==c||a==d||b==c||b==d)nei[i] |= (1<<j);
  }
  uint64_t total=1;for(int i=0;i<m;i++)total*=3;
  int minimum=1<<20;uint64_t num=0;
  for(uint64_t q=0;q<total;q++){
   uint64_t temp=q;int labels[16]={};int zeros=0,twos=0,weight=0;
   for(int i=0;i<m;i++){int x=temp%3;temp/=3;labels[i]=x;weight+=x;if(x==0)zeros|=1<<i;else if(x==2)twos|=1<<i;}
   if(weight>minimum)continue;
   bool valid=true;
   for(int j=0;j<m;j++)if(zeros>>j&1){
     if(__builtin_popcount((unsigned)(nei[j]&twos))!=1){valid=false;break;}
   }
   if(!valid)continue;
   if(weight<minimum){minimum=weight;num=0;}
   num++;
  }
  cout<<"n="<<n<<" min="<<minimum<<" optimal_labelings="<<num<<" ternary_labelings="<<total<<"\n";
 }
}
