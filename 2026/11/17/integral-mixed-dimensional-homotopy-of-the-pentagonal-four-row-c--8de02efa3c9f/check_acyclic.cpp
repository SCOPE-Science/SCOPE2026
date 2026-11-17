#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
int main(){ifstream in("complex.txt");string s;int R,C,E;size_t total,pm;in>>s>>R>>s>>C>>s>>E>>s>>total>>s>>pm;vector<pair<int,int>> edges(E);for(auto& x:edges)in>>x.first>>x.second;in>>s;while(in>>s&&s!="masks"){};while(in>>s&&s!="pairs"){};vector<pair<U,U>> pairs;U a,b;while(in>>a>>b)pairs.push_back({a,b});cerr<<"pairs "<<pairs.size()<<" total "<<total<<"\n";
vector<U> faces;faces.reserve(total);vector<U> vm(E);for(int i=0;i<E;i++)vm[i]=(1ULL<<edges[i].first)|(1ULL<<edges[i].second);
auto rec=[&](auto&& self,int e,U used,U m)->void{if(e==E){faces.push_back(m);return;}self(self,e+1,used,m);if(!(used&vm[e]))self(self,e+1,used|vm[e],m|(1ULL<<e));};rec(rec,0,0,0);
unordered_map<U,int> ids;ids.reserve(total*2);for(int i=0;i<faces.size();i++)ids[faces[i]]=i;
unordered_map<U,U> pairmap;pairmap.reserve(pairs.size()*2);for(auto [lo,up]:pairs)pairmap[lo]=up;
vector<int> indeg(faces.size());size_t hasse=0;
for(int i=0;i<faces.size();i++){U face=faces[i];while(face){U bit=face&-face;face-=bit;U lo=faces[i]^bit;int j=ids.at(lo);if(pairmap.count(lo)&&pairmap.at(lo)==faces[i])indeg[i]++;else indeg[j]++;hasse++;}}
vector<int> todo;todo.reserve(total);for(int i=0;i<faces.size();i++)if(indeg[i]==0)todo.push_back(i);
for(int p=0;p<todo.size();p++){int i=todo[p];U face=faces[i];if(pairmap.count(face)){int j=ids.at(pairmap.at(face));if(--indeg[j]==0)todo.push_back(j);}while(face){U bit=face&-face;face-=bit;U lo=faces[i]^bit;if(pairmap.count(lo)&&pairmap.at(lo)==faces[i])continue;int j=ids.at(lo);if(--indeg[j]==0)todo.push_back(j);}}
cout<<"faces="<<total<<" matching_pairs="<<pairs.size()<<" cover_relations="<<hasse<<" topological_sorted="<<todo.size()<<" acyclic="<<(todo.size()==faces.size())<<"\n";
}
