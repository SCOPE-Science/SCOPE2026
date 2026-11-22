#include <bits/stdc++.h>
using namespace std;
const int N=6, E=30;
using Mask=uint32_t;
vector<pair<int,int>> edges;
vector<array<int,N>> concepts;
vector<Mask> face[6];
unordered_set<Mask> present[6];
int number_cycles(const array<int,N>& p){int seen=0,cy=0;for(int i=0;i<N;i++)if(!(seen>>i&1)){cy++;for(int j=i;!(seen>>j&1);j=p[j])seen|=1<<j;}return cy;}
bool shat(Mask m,int k){int seen=0;for(auto p:concepts){int trace=0,b=0;for(int idx=0;idx<E;idx++)if(m>>idx&1){auto [i,j]=edges[idx];if(p[i]==j)trace|=1<<b;b++;}seen|=1<<trace;}return __builtin_popcount((unsigned)seen)==(1<<k);}
void enumerate(int k,int pos,int rows,int cols,Mask m){
 if(k==0){int size=__builtin_popcount(m);if(shat(m,size)){face[size].push_back(m);present[size].insert(m);}return;}
 for(int i=pos;i<=E-k;i++){auto [a,b]=edges[i];if((rows>>a&1)||(cols>>b&1))continue;enumerate(k-1,i+1,rows|(1<<a),cols|(1<<b),m|(1u<<i));}
}
int rank_boundary(int k){ // reduced chain on empty face for k=1
 unordered_map<Mask,int> ind;for(int i=0;i<(int)face[k-1].size();i++)ind[face[k-1][i]]=i;
 unordered_map<int,bitset<2048>> pivots;int rank=0;
 for(auto m:face[k]){bitset<2048> v;for(int e=0;e<E;e++)if(m>>e&1)v.flip(ind.at(m^(1u<<e)));
  for(int top=(int)face[k-1].size()-1;top>=0;top--)if(v[top]){auto it=pivots.find(top);if(it==pivots.end()){pivots[top]=v;rank++;break;}v^=it->second;}
 }
 return rank;
}
int main(){for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j)edges.push_back({i,j});
 array<int,N> p; iota(p.begin(),p.end(),0);do{bool ok=true;for(int i=0;i<N;i++)if(p[i]==i)ok=false;if(ok&&((N-number_cycles(p))%2==0))concepts.push_back(p);}while(next_permutation(p.begin(),p.end()));
 if(concepts.size()!=130){cerr<<"bad number even derangements";return 2;}
 for(int k=0;k<=5;k++)enumerate(k,0,0,0,0);int target[]={1,30,315,1420,1140,0};for(int k=0;k<=5;k++){cout<<"face_"<<k<<"="<<face[k].size()<<"\n";if(face[k].size()!=size_t(target[k]))return 3;}
 int f3=0,f4=0;for(auto m:face[3]){bool extend=false;for(int j=0;j<E;j++)if(!(m>>j&1)&&present[4].count(m|(1u<<j))){extend=true;break;}if(!extend)f3++;}f4=face[4].size();cout<<"facets_3="<<f3<<" facets_4="<<f4<<"\n";if(f3!=360||f4!=1140)return 4;
 int ranks[]={0,1,29,286,750};for(int k=1;k<=4;k++){int r=rank_boundary(k);cout<<"rank_d"<<k-1<<"="<<r<<"\n";if(r!=ranks[k])return 5;}
 cout<<"beta2="<<(1420-286-750)<<" beta3="<<(1140-750)<<"\n";
 cout<<"EVEN_DERANGEMENT_CPP_PASS\n";
}
