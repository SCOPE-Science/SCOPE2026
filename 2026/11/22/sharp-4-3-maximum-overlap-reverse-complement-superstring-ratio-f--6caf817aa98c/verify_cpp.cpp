#include <bits/stdc++.h>
using namespace std;
string rc(string a){reverse(a.begin(),a.end());for(char &c:a)c=(c=='0'?'1':'0');return a;}
string cn(string a){return min(a,rc(a));}
int overlap(const string&a,const string&b){for(int k=min(a.size(),b.size())-1;k>=1;--k)if(a.substr(a.size()-k)==b.substr(0,k))return k;return 0;}
vector<string> clean(vector<string> s){for(auto &a:s)a=cn(a);sort(s.begin(),s.end());s.erase(unique(s.begin(),s.end()),s.end());vector<string>o;for(auto &a:s){bool contained=false;for(auto &b:s)if(a!=b && (b.find(a)!=string::npos || b.find(rc(a))!=string::npos)){contained=true;break;}if(!contained)o.push_back(a);}return o;}
string key(const vector<string>& v){string s;for(auto &a:v){s+=a;s+='|';}return s;}
unordered_map<string,int> memo;
int Greedy(vector<string>s){s=clean(s);if(s.size()==1)return (int)s[0].size();string k=key(s);auto it=memo.find(k);if(it!=memo.end())return it->second;
 int bestov=-1;vector<tuple<int,int,string>> opts;int n=s.size();
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)for(int u=0;u<2;u++)for(int v=0;v<2;v++){
  string a=u?rc(s[i]):s[i], b=v?rc(s[j]):s[j]; int z=overlap(a,b);
  if(z>bestov){bestov=z;opts.clear();}if(z==bestov)opts.emplace_back(i,j,a+b.substr(z));
 }
 int res=0;set<string>seen;
 for(auto &[i,j,z]:opts){vector<string>nx;for(int t=0;t<n;t++)if(t!=i&&t!=j)nx.push_back(s[t]);nx.push_back(z);nx=clean(nx);string x=key(nx);if(seen.insert(x).second)res=max(res,Greedy(nx));}
 return memo[k]=res;
}
int main(){vector<string> reps;for(int x=0;x<16;x++){string s;for(int j=3;j>=0;j--)s+=((x>>j)&1)?'1':'0';reps.push_back(cn(s));}sort(reps.begin(),reps.end());reps.erase(unique(reps.begin(),reps.end()),reps.end());assert(reps.size()==10);
 const int LIM=1<<10;int opt[LIM];fill(opt,opt+LIM,100);int all=0;
 for(int n=4;n<=13;n++)for(int z=0;z<(1<<n);z++){
  string s;for(int i=n-1;i>=0;i--)s+=((z>>i)&1)?'1':'0';int mask=0;
  for(int j=0;j<=n-4;j++){
   string w=cn(s.substr(j,4));int id=lower_bound(reps.begin(),reps.end(),w)-reps.begin();mask|=(1<<id);
  }
  int sub=mask;for(;;){opt[sub]=min(opt[sub],n);if(sub==0)break;sub=(sub-1)&mask;}
 }
 map<pair<int,int>,int> joint;vector<int> eq;int fullworst=0;int maxNumer=0,maxDenom=1;
 for(int m=1;m<LIM;m++){
  vector<string> words;for(int i=0;i<10;i++)if(m&(1<<i))words.push_back(reps[i]);int g=Greedy(words), o=opt[m];assert(o<100);
  joint[{o,g}]++;
  if(g*maxDenom>maxNumer*o){maxNumer=g;maxDenom=o;eq.clear();}if(g*maxDenom==maxNumer*o)eq.push_back(m);
  if(m==1023)fullworst=g;
 }
 int gg=std::gcd(maxNumer,maxDenom);maxNumer/=gg;maxDenom/=gg;
 cout<<"reps";for(auto &s:reps)cout<<' '<<s;cout<<"\n";
 cout<<"cases 1023\n"<<"ratio "<<maxNumer<<'/'<<maxDenom<<"\n";
 cout<<"maximizer masks";for(int x:eq)cout<<' '<<x;cout<<"\n";
 cout<<"full worst "<<fullworst<<" optimum "<<opt[1023]<<"\n";
 cout<<"states "<<memo.size()<<"\n";
 cout<<"joint";for(auto &[p,num]:joint)cout<<" ("<<p.first<<','<<p.second<<':'<<num<<')';cout<<'\n';
}
