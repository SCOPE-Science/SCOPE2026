// Validate explicit depth-five yes/no comparison tree; no search or input generation.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 if(argc!=2)return 2;
 ifstream f(argv[1]);if(!f)return 3;
 map<string,pair<int,int>> nodes; map<string,vector<int>> leaves;
 string line;
 while(getline(f,line)){
  if(line.empty())continue;
  istringstream in(line); char typ;string path;in>>typ>>path;
  if(path=="-")path="";
  if(typ=='N'){
   int a,b; if(!(in>>a>>b)||a<1||a>6||b<=a||b>6)return 4;
   if(!nodes.emplace(path,make_pair(a,b)).second)return 5;
  }else if(typ=='L'){
   vector<int> p(6);for(int&i:p)if(!(in>>i))return 6;
   if(!leaves.emplace(path,p).second)return 7;
  }else return 8;
 }
 if(nodes.size()!=31||leaves.size()!=32)return 9;
 set<vector<int>> used;
 for(const auto & [path,p]:leaves){
  if(path.size()!=5)return 10;
  auto sorted=p;sort(sorted.begin(),sorted.end());
  if(sorted!=vector<int>({1,2,3,4,5,6}))return 11;
  int desc=0;for(int i=0;i<5;i++)desc+=p[i]>p[i+1];
  if(desc>1)return 12;
  for(int d=0;d<5;d++){
   const auto it=nodes.find(path.substr(0,d));
   if(it==nodes.end())return 13;
   auto [a,b]=it->second;
   bool yes=p[a-1]>p[b-1];
   if(yes!=(path[d]=='1'))return 14;
  }
  used.insert(p);
 }
 if(used.size()!=32)return 15;
 cout<<"Certificate valid: 31 internal queries, 32 distinct one-descent leaves.\n";
}
