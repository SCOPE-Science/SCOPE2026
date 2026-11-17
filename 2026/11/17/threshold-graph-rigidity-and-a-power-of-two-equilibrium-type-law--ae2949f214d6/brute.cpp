#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int main(){
 for(int n=3;n<=7;++n){
  vector<pair<int,int>> edge;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++) edge.push_back({i,j});
  int e=edge.size();uint64_t matches=0;
  for(uint32_t mask=0;mask<(1U<<e);++mask){
   int d[7]={};
   for(int p=0;p<e;p++)if(mask>>p&1){++d[edge[p].first];++d[edge[p].second];}
   bool ok=true;
   for(int p=0;p<e;p++){
    auto [i,j]=edge[p];
    int neighbor1=d[i]+d[j]-2*((mask>>p)&1);
    bool is1=(mask>>p)&1;
    if(is1 && neighbor1<n-2){ok=false;break;}
    if(!is1 && neighbor1>n-2){ok=false;break;}
   }
   if(ok)++matches;
  }
  cout<<n<<" "<<matches<<"\n";
  if(matches!=(n==3?2:n==4?10:n==5?12:n==6?164:268))return 1;
 }
 cout<<"PASS\n";
}
