#include <iostream>
#include <vector>
#include <map>
#include <cstdint>
using namespace std;
static const int alphabet[4]={-1,1,2,3};
int main(){
 for(int n=3;n<=6;n++){
  int N=2*n; uint64_t limit=uint64_t(1)<<(2*N);
  vector<vector<int>> neighbors(N);
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){neighbors[i].push_back(n+j);neighbors[n+j].push_back(i);}
  map<int,uint64_t> counts;int rom_min=1000;uint64_t rom_count=0;
  for(uint64_t code=0;code<limit;code++){
   uint64_t t=code;int a[32];int weight=0;
   for(int i=0;i<N;i++){a[i]=alphabet[t&3];t>>=2;weight+=a[i];}
   bool italian=true,roman=true;
   for(int i=0;i<N;i++){
    int sum=a[i], pos=0, num2=0, num3=0, high=0;
    for(int j:neighbors[i]){
     int x=a[j];sum+=x;if(x>0)pos+=x;
     if(x==2)num2++;if(x==3)num3++;if(x>=2)high++;
    }
    if(sum<1){italian=false;roman=false;break;}
    if(a[i]==-1){
     if(pos<3)italian=false;
     if(num3==0&&num2<2)roman=false;
    }else if(a[i]==1){
     if(pos<2)italian=false;
     if(high==0)roman=false;
    }
    if(!italian&&!roman)break;
   }
   if(italian)counts[weight]++;
   if(roman){if(weight<rom_min){rom_min=weight;rom_count=1;}else if(weight==rom_min)rom_count++;}
  }
  cout<<"n="<<n<<" italian_min="<<counts.begin()->first<<" weight2="<<counts[2]<<" weight3="<<counts[3]<<" roman_min="<<rom_min<<" roman_opt="<<rom_count<<" all_italian=";
  uint64_t total=0;for(auto [w,c]:counts)total+=c;cout<<total<<"\n";
 }
}
