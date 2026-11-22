// Exact finite enumeration of radius-one identifying sets in the undirected
// length-two Kautz graph. Compile with: c++ -O3 -std=c++17 enumerate_codes.cpp -o codes
// Run with: ./codes
#include <cstdint>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;
using U=uint64_t;
struct Exhaustive {
  int q,n,k; vector<pair<int,int>> vertices; vector<U> neighborhoods;
  U count=0, first=0;
  Exhaustive(int qq,int kk):q(qq),n(qq*(qq-1)),k(kk),neighborhoods(n,0){
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)if(a!=b)vertices.push_back({a,b});
    for(int i=0;i<n;i++)for(int j=0;j<n;j++){
      auto [a,b]=vertices[i];auto [c,d]=vertices[j];
      if(i==j || b==c || d==a) neighborhoods[i]|=(U(1)<<j);
    }
  }
  bool identifies(U chosen){
    U signature[64];
    for(int i=0;i<n;i++){
      U sig=chosen&neighborhoods[i];
      if(sig==0) return false;
      for(int j=0;j<i;j++) if(sig==signature[j])return false;
      signature[i]=sig;
    }
    return true;
  }
  void traverse(int next,int remaining,U chosen){
    if(remaining==0){if(identifies(chosen)){count++;if(!first)first=chosen;}return;}
    if(n-next<remaining)return;
    traverse(next+1,remaining-1,chosen|(U(1)<<next));
    traverse(next+1,remaining,chosen);
  }
  void run(){traverse(0,k,0);cout<<q<<","<<k<<","<<count<<","<<first<<"\n";}
};
int main(){
  for(int q=3;q<=6;q++)for(int k=q-1;k<=q+1;k++){
    Exhaustive a(q,k);a.run();if(a.count)break;
  }
}
