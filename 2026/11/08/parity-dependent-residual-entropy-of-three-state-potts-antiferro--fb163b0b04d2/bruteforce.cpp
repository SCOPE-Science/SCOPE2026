// Independent exhaustive three-spin-state enumeration for small Mycielskian cycles.
// Build: c++ -O3 -std=c++17 bruteforce.cpp -o brute && ./brute
#include <iostream>
#include <vector>
#include <utility>
#include <cstdint>
using namespace std;
int main(){
 for(int n=4;n<=7;n++){
  vector<pair<int,int>> e;
  for(int i=0;i<n;i++){
   int j=(i+1)%n;
   e.emplace_back(i,j);
   e.emplace_back(i,n+j);
   e.emplace_back(j,n+i);
   e.emplace_back(n+i,2*n);
  }
  const int N=2*n+1;
  uint64_t total=1;
  for(int i=0;i<N;i++)total*=3;
  uint64_t count=0;
  int min_b=4*n+1;
  vector<int> s(N,0);
  for(uint64_t mask=0;mask<total;mask++){
   int b=0;
   for(const auto &edge:e)b+=(s[edge.first]==s[edge.second]);
   if(b<min_b){min_b=b;count=1;}
   else if(b==min_b)count++;
   for(int i=0;i<N;i++){
    if(++s[i]!=3)break;
    s[i]=0;
   }
  }
  cout << "n="<<n<<" configurations="<<total<<" minimum="<<min_b<<" ground_states="<<count<<"\n";
  if(n==4 && (min_b!=0||count!=78))return 2;
  if(n==5 && (min_b!=1||count!=660))return 2;
  if(n==6 && (min_b!=0||count!=228))return 2;
  if(n==7 && (min_b!=1||count!=3192))return 2;
 }
 cout<<"BRUTE_OK\n";
}
