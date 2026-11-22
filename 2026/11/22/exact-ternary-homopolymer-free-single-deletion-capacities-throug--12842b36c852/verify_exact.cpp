// Exact maximum independent family of ternary no-adjacent-equal words correcting one deletion.
#include <bits/stdc++.h>
using namespace std;
static constexpr int MAXN=192;
using Bits=bitset<MAXN>;
int N, best=0; long long calls=0;
vector<string> words;
array<Bits,MAXN> compat;
vector<int> champion;
int first(Bits const &b){for(int i=0;i<N;i++)if(b.test(i))return i;return -1;}
void search(Bits cand,vector<int> &clique){
 ++calls;
 if(cand.none()){
  if(int(clique.size())>best){best=clique.size();champion=clique;}
  return;
 }
 vector<int> order, ub;
 Bits remain=cand;
 int color=0;
 while(remain.any()){
   color++;
   Bits q=remain;
   while(q.any()){
     int v=first(q);order.push_back(v);ub.push_back(color);
     remain.reset(v);
     q.reset(v);
     q &= ~compat[v]; // color class independent in compatibility graph
   }
 }
 for(int i=int(order.size())-1;i>=0;i--){
   if(int(clique.size())+ub[i]<=best)return;
   int v=order[i];
   clique.push_back(v);
   Bits next=cand & compat[v];
   if(next.any())search(next,clique);
   else if(int(clique.size())>best){best=clique.size();champion=clique;}
   clique.pop_back();
   cand.reset(v);
 }
}
int main(int argc,char**argv){
 int n= argc>1?stoi(argv[1]):7;
 if(n<2||n>7){cerr<<"n must be 2 to 7\n";return 1;}
 string w(n,'0');function<void(int)> make=[&](int j){if(j==n){words.push_back(w);return;}for(char c='0';c<='2';++c){if(j&&w[j-1]==c)continue;w[j]=c;make(j+1);}};make(0);N=words.size();
 vector<set<string>> shadows(N);
 for(int i=0;i<N;i++)for(int p=0;p<n;p++)shadows[i].insert(words[i].substr(0,p)+words[i].substr(p+1));
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  bool disjoint=true;
  for(auto const &s:shadows[i])if(shadows[j].count(s)){disjoint=false;break;}
  if(disjoint){compat[i].set(j);compat[j].set(i);}
 }
 Bits all; for(int i=0;i<N;i++)all.set(i);
 vector<int> cur;search(all,cur);
 cout<<"n="<<n<<" words="<<N<<" maximum="<<best<<" calls="<<calls<<"\n";
 cout<<"witness:";for(int i:champion)cout<<" "<<words[i];cout<<"\n";
 for(int i=0;i<(int)champion.size();i++)for(int j=i+1;j<(int)champion.size();j++){
  if(!compat[champion[i]].test(champion[j]))return 9;
 }
 return 0;
}
