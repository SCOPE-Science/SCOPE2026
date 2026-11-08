// Exhaustive finite certificate for ternary single-insertion covering at source length four.
// Compile: g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
#include <algorithm>
#include <bitset>
#include <cassert>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using Bits=bitset<243>;
static vector<string> words4,words5;
static vector<Bits> cover_sets;
static vector<vector<int>> parents;
static bool eligible[81];
static unordered_map<string,int> memo;
static long long nodes=0;
static int limit=0;
static const string witness31=
 "0000 0011 0012 0021 0022 0100 0111 0122 0210 0220 1000 1011 1022 1100 1102 1111 1120 1122 1201 1220 2001 2002 2110 2112 2120 2121 2200 2211 2212 2221 2222";
static const string witness33=
 "0000 0001 0010 0011 0022 0100 0101 0110 0111 0202 0221 1000 1001 1010 1011 1100 1101 1110 1111 1122 1212 1220 1222 2002 2021 2112 2120 2122 2200 2202 2211 2220 2222";
static string word(int x,int n) {string s(n,'0');for(int k=n-1;k>=0;--k){s[k]=char('0'+x%3);x/=3;}return s;}
static set<string> one_deletions(const string &s){set<string> out;for(int i=0;i<(int)s.size();++i)out.insert(s.substr(0,i)+s.substr(i+1));return out;}
static string state_key(const Bits& b){string s(31,'\0');for(int i=0;i<243;i++)if(b[i])s[i/8]=char((unsigned char)s[i/8]|(1U<<(i%8)));return s;}
static bool search(Bits done,int chosen){
 ++nodes;
 if(done.count()==243)return true;
 if(chosen>=limit)return false;
 vector<pair<int,int>> constraints;
 int uncovered=0,max_gain=0;
 for(int j=0;j<243;++j)if(!done[j]){
   ++uncovered;
   int choices=(int)parents[j].size();
   if(choices==0)return false;
   constraints.emplace_back(choices,j);
 }
 for(int c=0;c<81;++c)if(eligible[c])
   max_gain=max(max_gain,(int)(cover_sets[c]&~done).count());
 if(max_gain==0||chosen+(uncovered+max_gain-1)/max_gain>limit)return false;
 // Greedy packing of constraints with pairwise-disjoint candidate sets.
 // Each constraint in such a packing requires its own distinct selected center.
 sort(constraints.begin(),constraints.end());
 bitset<81> touched;int packing=0;
 for(auto [degree,j]:constraints){
   bool disjoint=true;
   for(int c:parents[j])if(touched[c]){disjoint=false;break;}
   if(disjoint){++packing;for(int c:parents[j])touched[c]=true;}
 }
 if(chosen+packing>limit)return false;
 string key=state_key(done);
 auto it=memo.find(key);
 if(it!=memo.end()&&it->second<=chosen)return false;
 memo[key]=chosen;
 // Every solution covers this uncovered target using one of its parent centers.
 int j=constraints.front().second;
 vector<pair<int,int>> candidates;
 for(int c:parents[j])candidates.emplace_back((int)(cover_sets[c]&~done).count(),c);
 sort(candidates.rbegin(),candidates.rend());
 for(auto [gain,c]:candidates)if(search(done|cover_sets[c],chosen+1))return true;
 return false;
}
static void build(const string& forbidden){
 cover_sets.assign(81,Bits());parents.assign(243,vector<int>());memo.clear();nodes=0;
 for(int i=0;i<81;i++){
   eligible[i]=forbidden.empty()||!one_deletions(words4[i]).count(forbidden);
 }
 for(int j=0;j<243;j++){
   auto subs=one_deletions(words5[j]);
   for(int i=0;i<81;i++)if(eligible[i]&&subs.count(words4[i])){
     parents[j].push_back(i);cover_sets[i][j]=true;
   }
 }
}
static bool exists_cover(int bound,const string& forbidden){
 limit=bound;build(forbidden);
 Bits initial;int forced=0;
 for(int j=0;j<243;j++)if(parents[j].size()==1){
   int c=parents[j][0];
   if(!initial[j]){initial|=cover_sets[c];++forced;}
 }
 bool ok=search(initial,forced);
 cout<<"bound="<<bound<<" forbidden="<<(forbidden.empty()?"none":forbidden)
     <<" feasible="<<ok<<" forced="<<forced<<" nodes="<<nodes
     <<" memo_states="<<memo.size()<<"\n";
 return ok;
}
static void check_witness(const string& literal,int expected,bool avoid_012){
 istringstream in(literal);
 set<string> code;string c;
 while(in>>c){assert(c.size()==4);code.insert(c);}
 assert((int)code.size()==expected);
 for(const string& y:words5){
   bool covered=false;
   for(const string& x:one_deletions(y))if(code.count(x)){covered=true;break;}
   assert(covered);
 }
 if(avoid_012){for(const string& x:code)assert(!one_deletions(x).count("012"));}
 cout<<"witness="<<expected<<" insertion_covered=243"
     <<" avoid_012="<<avoid_012<<"\n";
}
int main(){
 for(int i=0;i<81;i++)words4.push_back(word(i,4));
 for(int i=0;i<243;i++)words5.push_back(word(i,5));
 check_witness(witness31,31,false);
 check_witness(witness33,33,true);
 assert(!exists_cover(30,""));
 assert(!exists_cover(32,"012"));
 cout<<"CERTIFICATE_OK\n";
}
