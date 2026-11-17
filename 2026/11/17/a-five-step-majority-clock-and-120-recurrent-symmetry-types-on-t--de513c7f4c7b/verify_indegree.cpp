#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int W=stoi(argv[1]), H=stoi(argv[2]);int V=W*H,S=1<<V;vector<int> nxt(S),deg(S),entry(S,-1),period(S,0),cycleid(S,-1);vector<array<int,4>>nb(V);
for(int y=0;y<H;y++)for(int x=0;x<W;x++){int i=W*y+x; nb[i]={W*y+(x+1)%W,W*y+(x+W-1)%W,W*((y+1)%H)+x,W*((y+H-1)%H)+x};}
for(int s=0;s<S;s++){int out=0;for(int i=0;i<V;i++){int votes=0;for(int j:nb[i])votes+=(s>>j)&1;int b=votes>2?1:votes<2?0:((s>>i)&1);out|=b<<i;}nxt[s]=out;deg[out]++;}
deque<int>q;for(int s=0;s<S;s++)if(deg[s]==0)q.push_back(s);vector<int>order;order.reserve(S);while(!q.empty()){int s=q.front();q.pop_front();order.push_back(s);if(--deg[nxt[s]]==0)q.push_back(nxt[s]);}
int cycles=0;map<int,int>cyclicstate,orbitcount,basinbyperiod;vector<int>rep;for(int s=0;s<S;s++)if(deg[s]>0&&cycleid[s]<0){int t=s,len=0;do{cycleid[t]=cycles;entry[t]=0;len++;t=nxt[t];}while(t!=s);t=s;do{period[t]=len;t=nxt[t];}while(t!=s);rep.push_back(s);orbitcount[len]++;cyclicstate[len]+=len;cycles++;}
for(int i=(int)order.size()-1;i>=0;i--){int s=order[i],t=nxt[s];cycleid[s]=cycleid[t];period[s]=period[t];entry[s]=entry[t]+1;}
map<int,int>shell,byPeriod;int maxe=0;map<pair<int,int>,int>cross;vector<int>basin(cycles);
for(int s=0;s<S;s++){shell[entry[s]]++;byPeriod[period[s]]++;cross[{period[s],entry[s]}]++;basin[cycleid[s]]++;maxe=max(maxe,entry[s]);}
vector<vector<int>>perms;for(int rx=0;rx<2;rx++)for(int ry=0;ry<2;ry++)for(int a=0;a<W;a++)for(int b=0;b<H;b++){vector<int>p(V);for(int y=0;y<H;y++)for(int x=0;x<W;x++){int u=(rx?W-x:x)%W,v=(ry?H-y:y)%H;p[W*y+x]=W*((v+b)%H)+(u+a)%W;}perms.push_back(p);}
auto move=[&](int s,const vector<int>&p){int t=0;for(int i=0;i<V;i++)if((s>>i)&1)t|=1<<p[i];return t;};
for(int s=0;s<S;s++){if(move(nxt[s],perms[W*H])!=nxt[move(s,perms[W*H])]){cerr<<"not equivariant!";return 1;}}
vector<int>parent(cycles);iota(parent.begin(),parent.end(),0);function<int(int)>find=[&](int x){return parent[x]==x?x:parent[x]=find(parent[x]);};auto uni=[&](int a,int b){a=find(a);b=find(b);if(a!=b)parent[b]=a;};
for(int c=0;c<cycles;c++){int s=rep[c];for(auto&p:perms)uni(c,cycleid[move(s,p)]);uni(c,cycleid[s^(S-1)]);}map<int,set<int>>geom;for(int c=0;c<cycles;c++)geom[period[rep[c]]].insert(find(c));
cout<<"W "<<W<<" H "<<H<<" cycles "<<cycles<<" maxentry "<<maxe<<" sym "<<perms.size()*2<<"\n";
cout<<"period-orbits-states-basin-classes\n";for(auto [p,oc]:orbitcount)cout<<p<<" "<<oc<<" "<<cyclicstate[p]<<" "<<byPeriod[p]<<" "<<geom[p].size()<<"\n";
cout<<"entry-shells\n";for(auto [i,num]:shell)cout<<i<<" "<<num<<"\n";
cout<<"cycles_by_period_and_entry\n";for(auto [key,n]:cross)cout<<key.first<<","<<key.second<<":"<<n<<" ";cout<<"\n";
cout<<"basin histogram\n";map<pair<int,int>,int>basins;for(int c=0;c<cycles;c++)basins[{period[rep[c]],basin[c]}]++;for(auto [key,n]:basins)cout<<key.first<<","<<key.second<<":"<<n<<" ";cout<<"\n";
}
