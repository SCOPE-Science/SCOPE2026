// Independent finite check using the twelve Cartesian icosahedron vertices.
// Build: g++ -std=c++17 -O2 check_coordinates.cpp -o check_coordinates
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
int main(){
    const double phi=(1+sqrt(5.0))/2;
    vector<array<double,3>> p;
    for(int a:{-1,1})for(int b:{-1,1})p.push_back({0.0,double(a),b*phi});
    for(int a:{-1,1})for(int b:{-1,1})p.push_back({double(a),b*phi,0.0});
    for(int a:{-1,1})for(int b:{-1,1})p.push_back({a*phi,0.0,double(b)});
    assert(p.size()==12);
    int A[12][12]={};int edges=0;
    for(int i=0;i<12;i++)for(int j=i+1;j<12;j++){
        double d2=0;for(int k=0;k<3;k++)d2+=(p[i][k]-p[j][k])*(p[i][k]-p[j][k]);
        if(abs(d2-4)<1e-8)A[i][j]=A[j][i]=1,edges++;
    }
    assert(edges==30);
    int ant[12]={};
    for(int i=0;i<12;i++){
      int count=0;
      for(int j=0;j<12;j++){
        bool opposite=true;
        for(int k=0;k<3;k++)if(abs(p[i][k]+p[j][k])>1e-8)opposite=false;
        if(opposite)ant[i]=j,count++;
      }
      assert(count==1);
    }
    auto covers=[&](int mask){
      for(int i=0;i<12;i++){
        bool ok=(mask>>i)&1;
        for(int j=0;j<12;j++)if((mask>>j&1)&&A[i][j])ok=true;
        if(!ok)return false;
      }return true;
    };
    auto paired=[&](int mask){
      int x[4],k=0;
      for(int i=0;i<12;i++)if(mask>>i&1)x[k++]=i;
      if(k!=4)return false;
      return (A[x[0]][x[1]]&&A[x[2]][x[3]]) ||
        (A[x[0]][x[2]]&&A[x[1]][x[3]]) ||
        (A[x[0]][x[3]]&&A[x[1]][x[2]]);
    };
    for(int mask=0;mask<(1<<12);mask++)if(__builtin_popcount((unsigned)mask)==2){
      if(covers(mask))assert(!A[__builtin_ctz((unsigned)mask)][31-__builtin_clz((unsigned)mask)]);
    }
    vector<int> states;
    for(int mask=0;mask<(1<<12);mask++)if(__builtin_popcount((unsigned)mask)==4)
      if(covers(mask)&&paired(mask))states.push_back(mask);
    assert(states.size()==135);
    int type12=0,type13=0,type22=0;
    for(int s:states){
      int op=0,iedges=0;
      for(int i=0;i<12;i++)if(s>>i&1){
        if(s>>ant[i]&1)op++;
        for(int j=i+1;j<12;j++)if((s>>j&1)&&A[i][j])iedges++;
      }
      op/=2;
      if(op==1&&iedges==2)type12++;
      else if(op==1&&iedges==3)type13++;
      else if(op==2&&iedges==2)type22++;
      else assert(false);
    }
    assert(type12==60&&type13==60&&type22==15);
    map<int,int> index;
    for(int i=0;i<(int)states.size();i++)index[states[i]]=i;
    cout<<"order=12 host_edges="<<edges<<" min=4 states="<<states.size()
      <<" types(1/2,1/3,2/2)="<<type12<<","<<type13<<","<<type22<<"\n";
    for(int slide=0;slide<2;slide++){
      vector<set<int>> graph(states.size());
      for(int k=0;k<(int)states.size();k++)for(int u=0;u<12;u++)if(states[k]>>u&1)
       for(int v=0;v<12;v++)if(!(states[k]>>v&1)&&(!slide||A[u][v])){
         auto j=index.find(states[k]^(1<<u)^(1<<v));
         if(j!=index.end())graph[k].insert(j->second);
       }
      int comps=0;vector<int> seen(states.size());
      for(int i=0;i<(int)states.size();i++)if(!seen[i]){
        comps++;queue<int> q;q.push(i);seen[i]=1;
        while(!q.empty()){
          int x=q.front();q.pop();
          for(int y:graph[x])if(!seen[y])seen[y]=1,q.push(y);
        }
      }
      int rad=1000,diam=0;map<int,int> ecc,degree;int ne=0;
      for(int i=0;i<(int)states.size();i++){
        ne+=(int)graph[i].size();degree[(int)graph[i].size()]++;
        vector<int> dist(states.size(),-1);queue<int> q;dist[i]=0;q.push(i);
        while(!q.empty()){
          int x=q.front();q.pop();
          for(int y:graph[x])if(dist[y]<0)dist[y]=dist[x]+1,q.push(y);
        }
        assert(all_of(dist.begin(),dist.end(),[](int x){return x>=0;}));
        int a=*max_element(dist.begin(),dist.end());rad=min(rad,a);diam=max(diam,a);ecc[a]++;
      }
      cout<<(slide?"slide":"jump")<<" edges="<<ne/2<<" components="<<comps
        <<" radius="<<rad<<" diameter="<<diam<<" degree={";
      for(auto [k,v]:degree)cout<<k<<":"<<v<<",";
      cout<<"} eccentricity={";
      for(auto [k,v]:ecc)cout<<k<<":"<<v<<",";
      cout<<"}\n";
      if(slide){assert((ne==720&&comps==1&&rad==6&&diam==6&&degree==std::map<int,int>({{4,60},{6,60},{8,15}})));}
      else{assert((ne==1440&&comps==1&&rad==4&&diam==4&&degree==std::map<int,int>({{10,120},{16,15}})));}
    }
    cout<<"PASS\n";
}
