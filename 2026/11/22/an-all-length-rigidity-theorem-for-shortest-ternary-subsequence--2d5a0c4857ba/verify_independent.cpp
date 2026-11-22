#include <bits/stdc++.h>
using namespace std;
// Direct positional-subsequence census. Does not use the DFA transition proof.
map<string, unsigned> all_occurrences(const string &s){
  map<string,unsigned> mask_union;
  int n=s.size();
  for(unsigned mask=1;mask<(1u<<n);++mask){
    string t;
    for(int i=0;i<n;i++) if(mask>>i&1u)t+=s[i];
    if(t.size()<=8)mask_union[t]|=mask;
  }
  return mask_union;
}
string contract(const string&s){string r;for(char x:s)if(r.empty()||x!=r.back())r+=x;return r;}
vector<string> shortest(const string&s){
 auto m=all_occurrences(s);
 int best=s.size()+1;vector<string> ans;
 for(auto [w,mask]:m)if(mask==((1u<<s.size())-1)){
   if((int)w.size()<best){best=w.size();ans={w};}
   else if((int)w.size()==best)ans.push_back(w);
 }
 return ans;
}
vector<string> cand;void gen(string s,int len){if((int)s.size()==len){cand.push_back(s);return;}for(char x='0';x<='2';x++)if(x!=s.back())gen(s+x,len);}
int main(){for(int m=1;m<=8;m++)gen("0",m);
 unsigned long long tested=0,ambiguous=0;
 // Every canonical run-free ternary word through 12 letters.
 for(int n=2;n<=12;n++) for(int mask=0;mask<(1<<(n-2));mask++){
   string s="01";for(int j=2;j<n;j++){
    int choice=(mask>>(j-2))&1;
    for(char x='0';x<='2';x++)if(x!=s.back()){
      if(!choice){s+=x;break;}--choice;
    }
   }
   // An entirely different test: collect every positional subsequence.
   auto all=all_occurrences(s);
   auto observed=shortest(s);
   if(observed.empty()){cerr<<"empty "<<s<<"\n";return 2;}
   string run=s;
   if(observed.size()>1)++ambiguous;
   bool predicted=false;
   // DFA-independent finite check of the regular expression.
   for(int a=2;a<=n/2;a++)for(int b=1;b<=n/2;b++){
    int t=n-1-2*a-2*b;if(t<4||t%2)continue;
    int c=t/2;
    string w;for(int i=0;i<a;i++)w+="01";w+="2";for(int i=0;i<b;i++)w+="02";for(int i=0;i<c;i++)w+="10";
    if(w==s)predicted=true;
   }
   if((observed.size()==2)!=predicted||observed.size()>2|| (predicted && observed!=vector<string>{"010210","012010"})){
    cerr<<"mismatch "<<s<<" count "<<observed.size()<<"\n";return 3;
   }
   // Explicit greedy anchored membership, independent of all-occurrences.
   for(const auto& c:cand){
     if(c.size()>s.size())continue;
     int m=c.size(), p=0;vector<int> first(m),last(m);bool emb=true;
     for(int j=0,i=0;j<m;j++){while(i<n&&s[i]!=c[j])i++;if(i==n){emb=false;break;}first[j]=i++;}
     if(!emb){if(all.count(c)&&all.at(c)==((1u<<n)-1))return 4;continue;}
     for(int j=m-1,i=n-1;j>=0;j--){while(i>=0&&s[i]!=c[j])i--;if(i<0){emb=false;break;}last[j]=i--;}
     bool covered=emb;
     for(int i=0;i<n && covered;i++){
       bool ok=false;
       for(int j=0;j<m;j++)if(c[j]==s[i]&&(j==0||first[j-1]<i)&&(j==m-1||last[j+1]>i))ok=true;
       if(!ok)covered=false;
     }
     bool brute=all.count(c) && all.at(c)==((1u<<n)-1);
     if(covered!=brute){cerr<<"greedy mismatch "<<s<<" "<<c<<"\n";return 5;}
   }
   tested++;
 }
 cout<<"DIRECT PASS: "<<tested<<" canonical run-free inputs of lengths 2..12; "<<ambiguous<<" ambiguous inputs.\n";
}
