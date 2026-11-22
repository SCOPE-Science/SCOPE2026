// Standalone literal single-deletion profile verifier; independent of Euler construction.
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
vector<int> profile(const string& s,int q){
 vector<int> c(q*q,0); for(int i=0;i+1<(int)s.size();i++) c[(s[i]-'0')*q+s[i+1]-'0']++; return c;
}
int outcomes(const string& s,int q){
 set<vector<int>> seen; for(int i=0;i<(int)s.size();i++){
  string d=s.substr(0,i)+s.substr(i+1);seen.insert(profile(d,q));
 }return (int)seen.size();
}
int main(){
 const string ternary="01011200201210212202";
 const string quaternary="0101120121020212230023103013031232032131323302";
 if(ternary.size()!=20||outcomes(ternary,3)!=17)return 1;
 if(quaternary.size()!=46||outcomes(quaternary,4)!=42)return 2;
 cout<<"ternary_witness 20 17\nquaternary_witness 46 42\n";
 for(int q=2;q<=4;q++){
   int maxn=(q==2?10:(q==3?11:7));
   for(int n=2;n<=maxn;n++){
     long long total=1; for(int i=0;i<n;i++)total*=q;
     int best=0;
     for(long long t=0;t<total;t++){
       long long x=t; string s(n,'0');for(int i=n-1;i>=0;i--){s[i]='0'+(x%q);x/=q;}
       int v=outcomes(s,q);best=max(best,v);
       int cap=q*(q-1)*(q-1)+q+2;
       if(v>cap)return 3;
     }
     cout<<"q="<<q<<" n="<<n<<" max="<<best<<" examined="<<total<<"\n";
   }
 }
 cout<<"PASS\n";
}
