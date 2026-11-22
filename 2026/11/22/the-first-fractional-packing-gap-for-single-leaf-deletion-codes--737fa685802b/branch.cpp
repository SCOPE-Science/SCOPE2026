#include <bits/stdc++.h>
using namespace std;
int Nsrc,Nout,cols[1000][7];vector<vector<int>> parents,exclude_src;
vector<unsigned char>alive,uncovered;vector<int>sz;vector<int>choice;
unsigned long long nodes=0;
bool dfs(){nodes++;int best=-1,k=10;for(int c=0;c<Nout;c++) if(uncovered[c]){int s=sz[c];if(s==0)return false;if(s<k){k=s;best=c;if(s==1)break;}}if(best<0)return true;
 for(int j:parents[best])if(alive[j]){vector<int>dead;int uc[7];for(int i=0;i<7;i++){uc[i]=cols[j][i];uncovered[uc[i]]=false;}
  for(int t:exclude_src[j])if(alive[t]){alive[t]=false;dead.push_back(t);for(int i=0;i<7;i++)sz[cols[t][i]]--;}
  choice.push_back(j);if(dfs())return true;choice.pop_back();
  for(int t:dead){alive[t]=true;for(int i=0;i<7;i++)sz[cols[t][i]]++;}
  for(int c:uc)uncovered[c]=true;
 }
 return false;
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);cin>>Nsrc>>Nout;parents.resize(Nout);for(int s=0;s<Nsrc;s++)for(int k=0;k<7;k++){cin>>cols[s][k];parents[cols[s][k]].push_back(s);}exclude_src.resize(Nsrc);for(int s=0;s<Nsrc;s++){set<int>z;for(int k=0;k<7;k++)for(int j:parents[cols[s][k]])z.insert(j);exclude_src[s]=vector<int>(z.begin(),z.end());}alive.assign(Nsrc,true);uncovered.assign(Nout,true);sz.assign(Nout,9);for(int c=0;c<Nout;c++)sz[c]=parents[c].size();
 bool res=dfs();cout<<(res?"FOUND ":"UNSAT ")<<"nodes="<<nodes<<" selected="<<choice.size()<<"\n";if(res)for(int s:choice)cout<<s<<" ";cout<<"\n";
}
