#include <bits/stdc++.h>
using namespace std;
struct Pat {string w;int m;};vector<Pat> pats;
void gen(string w,int m){if((int)w.size()==m){pats.push_back({w,m});return;}for(char x='0';x<='2';x++)if(x!=w.back())gen(w+x,m);}
string update(string v,char x){for(size_t i=0;i<pats.size();++i){unsigned q=(unsigned char)v[i]; if(q==255)continue;int p=q>>4,r=q&15,m=pats[i].m;const string&w=pats[i].w;
 if(r && w[m-r]==x)--r;
 int j=-1;for(int t=0;t<=p && t<m;t++)if(w[t]==x)j=t;
 if(j<0){v[i]=char(255);continue;}
 r=max(r,m-j-1);if(p<m && w[p]==x)++p;
 v[i]=char((p<<4)|r);
 }return v;}
int reg(int s,char x){switch(s){
 case 0:return x=='0'?1:13;case 1:return x=='1'?2:13;
 case 2:return x=='0'?3:13;case 3:return x=='1'?4:13;
 case 4:return x=='0'?5:x=='2'?6:13;
 case 5:return x=='1'?4:13;case 6:return x=='0'?7:13;
 case 7:return x=='2'?8:13;case 8:return x=='0'?7:x=='1'?9:13;
 case 9:return x=='0'?10:13;case 10:return x=='1'?11:13;
 case 11:return x=='0'?12:13;case 12:return x=='1'?11:13;
 default:return 13;
 }}
struct Node{string v;char last;unsigned char reg;};
int main(){for(int m=1;m<=8;m++)gen("0",m);if(pats.size()!=255)return 2;
 string v(pats.size(),0);v=update(update(v,'0'),'1');
 vector<Node> nodes;unordered_map<string,int> ids;nodes.reserve(200000);ids.reserve(200000);
 Node start={v,'1',2};nodes.push_back(start);ids.emplace(start.v+start.last+char(start.reg),0);
 size_t edges=0;int max_shortest=0, amb_states=0, nonreg=0, wrong=0;
 for(size_t h=0;h<nodes.size();++h){Node nd=nodes[h];int best=9,num=0;vector<string> winning;
 for(size_t j=0;j<pats.size();j++){
  int q=(unsigned char)nd.v[j];if(q==255||(q&15))continue;
  int m=pats[j].m;
  if(m<best){best=m;num=1;winning={pats[j].w};}
  else if(m==best){num++;winning.push_back(pats[j].w);}
 }
 bool regok=nd.reg==12;
 bool truth= (num==2 && best==6 && winning.size()==2 && winning[0]=="010210"&& winning[1]=="012010");
 if(num<1 || (regok!=truth) || (!regok && num!=1)){
  cerr<<"FAILED at node "<<h<<" best="<<best<<" num="<<num<<" reg="<<int(nd.reg)<<" candidates=";for(auto&w:winning)cerr<<w<<",";cerr<<"\n";return 3;
 }
 max_shortest=max(max_shortest,best);if(num==2)amb_states++;
 for(char c='0';c<='2';c++)if(c!=nd.last){
  Node nt={update(nd.v,c),c,(unsigned char)reg(nd.reg,c)};
  string key=nt.v+nt.last+char(nt.reg);
  if(ids.find(key)==ids.end()){int id=nodes.size();ids.emplace(move(key),id);nodes.push_back(move(nt));}
  ++edges;
 }
 }
 cout<<"CHECK PASS. states="<<nodes.size()<<" edges="<<edges<<" patterns="<<pats.size()<<" max_shortest="<<max_shortest<<" ambiguity_states="<<amb_states<<"\n";
}
