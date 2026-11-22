#include <bits/stdc++.h>
using namespace std;
const int N=6, V=32; 
vector<int> E, outs[V],to(64),lab(64); int deg[V];
uint64_t total=0,fc=0,fr=0,fcr=0;
int seq[54];
bool period6(int i){for(int d: {1,2,3}){bool yes=true;for(int j=0;j<6;j++){if(((i>>(5-j))&1) != ((i>>(5-j%d))&1)){yes=false;break;}}if(yes)return false;} return true;}
string normalized(const string &s) {int m=s.size();for(int k=0;k<m;k++){bool yes=true;for(int j=0;j<6;j++)if(s[(k+j)%m] != "000001"[j]){yes=false;break;}if(yes)return s.substr(k)+s.substr(0,k);}throw runtime_error("not found");}
void visit(uint64_t mask, int v,int k){
 if(k==54){if(v!=0)return;total++;string s(54,'0');for(int j=0;j<54;j++)s[(j+5)%54]=char('0'+lab[seq[j]]);
   if(s.substr(0,6)!="000001"){cerr<<"bad start "<<s.substr(0,6)<<"\n";exit(1);}
   string c=s;for(char &ch:c)ch= (ch=='0'?'1':'0');
   string r=s;reverse(r.begin(),r.end());
   string cr=r;for(char &ch:cr)ch=(ch=='0'?'1':'0');
   if(normalized(c)==s)fc++;
   if(normalized(r)==s)fr++;
   if(normalized(cr)==s)fcr++;
   return;
 }
 for(int e:outs[v])if(!(mask&(1ULL<<e))){seq[k]=e;visit(mask|(1ULL<<e),to[e],k+1);}
}
int main(){for(int e=0;e<64;e++)if(period6(e)){int u=e>>1,v=e&31;int i=E.size();E.push_back(e);outs[u].push_back(i);to[i]=v;lab[i]=e&1;}
 cerr<<"edges "<<E.size()<<"\n";
 int first=-1;for(int i=0;i<54;i++)if(E[i]==1) first=i;seq[0]=first;
 visit(1ULL<<first,to[first],1);
 cout<<"total="<<total<<" F_C="<<fc<<" F_R="<<fr<<" F_CR="<<fcr<<" orbits="<<(total+fc+fr+fcr)/4<<"\n";
}
