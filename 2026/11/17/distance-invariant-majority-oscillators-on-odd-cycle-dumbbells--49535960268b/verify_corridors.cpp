// Exhaustive labelled-state verification of binary majority dynamics on odd-cycle dumbbells.
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
uint32_t advance(uint32_t x,const vector<vector<int>>& g){
  uint32_t y=0;
  for(unsigned v=0;v<g.size();++v){
    unsigned votes=0;for(int w:g[v])votes+=(x>>w)&1u;
    unsigned degree=g[v].size();
    unsigned bit=(2*votes>degree)?1u:(2*votes<degree)?0u:((x>>v)&1u);
    y|=bit<<v;
  }
  return y;
}
long long word_count(int length){
  long long answer=0;
  for(int runs=2;2*runs<=length;runs+=2){
    int n=length-runs-1,k=runs-1;long long c=1;
    for(int j=1;j<=k;++j)c=c*(n-k+j)/j;
    answer+=2*c;
  }
  return answer;
}
int main(){
  int checks=0;
  for(int a=3;a<=9;a+=2)for(int b=a;b<=9;b+=2)for(int distance=1;distance<=6;distance++){
    int total=a+b+distance-1;
    if(total>20)continue;
    vector<vector<int>> g(total);
    auto edge=[&](int i,int j){g[i].push_back(j);g[j].push_back(i);};
    for(int i=0;i<a;i++)edge(i,(i+1)%a);
    for(int i=0;i<b;i++)edge(a+i,a+(i+1)%b);
    int previous=0;
    for(int k=0;k<distance-1;k++){int next=a+b+k;edge(previous,next);previous=next;}
    edge(previous,a);
    uint32_t required_mask=(1u<<0)|(1u<<a);
    for(int k=0;k<distance-1;k++)required_mask|=1u<<(a+b+k);
    uint64_t fixed=0,two=0;
    for(uint32_t x=0;x<(1u<<total);x++){
      uint32_t y=advance(x,g);
      if(advance(y,g)!=x)continue;
      if(x==y){++fixed;continue;}
      ++two;
      if((x^y)!=required_mask){
        cerr<<"Unsupported flip-set at a="<<a<<", b="<<b<<", distance="<<distance<<", x="<<x<<"\n";
        return 1;
      }
    }
    uint64_t predicted=2*(uint64_t)word_count(a-1)*word_count(b-1);
    if(two!=predicted){
      cerr<<"Count differs: "<<a<<" "<<b<<" "<<distance<<" observed="<<two<<" predicted="<<predicted<<"\n";
      return 2;
    }
    cout<<a<<","<<b<<","<<distance<<" fixed="<<fixed<<" primitive_two_states="<<two
        <<" primitive_two_orbits="<<two/2<<"\n";
    ++checks;
  }
  cout<<"PASS graph_parameter_cases="<<checks<<"\n";
}
