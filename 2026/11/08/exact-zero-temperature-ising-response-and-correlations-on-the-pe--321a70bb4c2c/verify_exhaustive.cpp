// An independent complete 2^15-spin enumeration using the Kneser KG(5,2)
// representation of the Petersen graph; C++17 standard library only.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
  vector<unsigned> pairmasks;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)
    pairmasks.push_back((1u<<i)|(1u<<j));
  vector<pair<int,int>> root;
  for(int i=0;i<10;i++)for(int j=i+1;j<10;j++)
    if((pairmasks[i]&pairmasks[j])==0)root.push_back({i,j});
  assert(root.size()==15);
  vector<pair<int,int>> line;
  for(int i=0;i<15;i++)for(int j=i+1;j<15;j++){
    auto [a,b]=root[i];auto [c,d]=root[j];
    if(a==c||a==d||b==c||b==d)line.push_back({i,j});
  }
  assert(line.size()==30);
  array<array<int,15>,15> distances{};
  for(int a=0;a<15;a++){
    distances[a].fill(99);
    distances[a][a]=0;
    queue<int> work;work.push(a);
    while(!work.empty()){
      int u=work.front();work.pop();
      for(auto [i,j]:line){
        int w=(i==u)?j:(j==u)?i:-1;
        if(w>=0 && distances[a][w]==99){
          distances[a][w]=distances[a][u]+1;work.push(w);
        }
      }
    }
  }
  array<array<int,15>,15> correlationNumerator{};
  array<int,16> maxcut;maxcut.fill(-1);
  array<int,16> argmax_counts{};
  array<int,16> nae_counts{};
  array<int,6> match_counts{};
  int ground=0;
  for(int s=0;s<(1<<15);s++){
    int neg=__builtin_popcount((unsigned)s);
    int cut=0;
    for(auto [i,j]:line)cut+=((s>>i)^(s>>j))&1;
    if(cut>maxcut[neg]){maxcut[neg]=cut;argmax_counts[neg]=1;}
    else if(cut==maxcut[neg])argmax_counts[neg]++;
    if(cut==20){
      nae_counts[neg]++;ground++;
      for(int i=0;i<15;i++)for(int j=i+1;j<15;j++)
        correlationNumerator[i][j]+=(((s>>i)^(s>>j))&1)?-1:1;
    }
    bool matching=true;
    for(int v=0;v<10;v++){
      int d=0;
      for(int i=0;i<15;i++)if(((s>>i)&1)&&(root[i].first==v||root[i].second==v))d++;
      if(d>1){matching=false;break;}
    }
    if(matching){assert(neg<=5);match_counts[neg]++;}
  }
  assert(ground==1782);
  array<int,4> pairCounts{};
  for(int i=0;i<15;i++)for(int j=i+1;j<15;j++){
    int r=distances[i][j];
    assert(r>=1&&r<=3);
    pairCounts[r]++;
    assert(correlationNumerator[i][j]==((r==1)?-594:(r==2)?190:-290));
  }
  assert((pairCounts==array<int,4>{0,30,60,15}));
  array<int,16> expectedNAE={0,0,0,0,0,6,195,690,690,195,6,0,0,0,0,0};
  assert(nae_counts==expectedNAE);
  array<int,6> expectedMatch={1,15,75,145,90,6};
  assert(match_counts==expectedMatch);
  for(int k=0;k<=15;k++){
    int cap=(k<=5)?4*k:((k<=10)?20:4*(15-k));
    assert(maxcut[k]==cap);
  }
  // In units of J, for h/J in {0,1,4,5}, count the global minima.
  for(int b: {0,1,4,5}){
    int best=1000000, count=0;
    for(int s=0;s<(1<<15);s++){
      int c=0;
      for(auto [i,j]:line)c+=((s>>i)^(s>>j))&1;
      int m=15-2*__builtin_popcount((unsigned)s);
      int e=30-2*c-b*m;
      if(e<best){best=e;count=1;}
      else if(e==best)count++;
    }
    int expectedE=(b<=4)?(-10-5*b):(30-15*b);
    int expectedCount=(b==0)?1782:(b==1)?6:(b==4)?332:1;
    assert(best==expectedE && count==expectedCount);
  }
  cout<<"EXHAUSTIVE_OK spin_masks=32768 ground_states=1782 critical_states=332 pair_correlations=105\n";
  return 0;
}
