// Reconstructs proper coloring reconfiguration graphs of the Petersen graph.
// Compile: g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;

int main() {
    vector<array<int,2>> vertices;
    for (int a=0; a<5; ++a) for(int b=a+1;b<5;++b) vertices.push_back({a,b});
    vector<pair<int,int>> edges;
    vector<vector<int>> ngh(10);
    for(int i=0;i<10;++i)for(int j=i+1;j<10;++j){
        auto a=vertices[i],b=vertices[j];
        if(a[0]!=b[0]&&a[0]!=b[1]&&a[1]!=b[0]&&a[1]!=b[1]){
            edges.emplace_back(i,j);ngh[i].push_back(j);ngh[j].push_back(i);
        }
    }
    if(edges.size()!=15)throw runtime_error("wrong Petersen graph");
    for(int k: {3,4}){
        int total=1<<(2*10); // all assignments in four base-four digits per vertex
        vector<int> configurations, inverse(total,-1);
        for(int mask=0;mask<total;++mask){
            int c[10];bool okay=true;
            for(int i=0;i<10;++i){c[i]=(mask>>(2*i))&3; if(c[i]>=k)okay=false;}
            if(!okay)continue;
            for(auto [i,j]:edges)if(c[i]==c[j]){okay=false;break;}
            if(okay){inverse[mask]=(int)configurations.size();configurations.push_back(mask);}
        }
        int N=(int)configurations.size();
        vector<vector<int>> adj(N);
        long long sumDegree=0;
        for(int z=0;z<N;++z){
            int mask=configurations[z];
            for(int i=0;i<10;++i){
                int current=(mask>>(2*i))&3,used=0;
                for(int j:ngh[i])used|=1<<((mask>>(2*j))&3);
                for(int c=0;c<k;++c){
                    if(c==current || (used>>c&1))continue;
                    int alt=(mask&~(3<<(2*i)))|(c<<(2*i));
                    int newIndex=inverse[alt];
                    if(newIndex<0)throw runtime_error("bad edge");
                    adj[z].push_back(newIndex);
                }
            }
            sumDegree+=adj[z].size();
        }
        if(sumDegree%2)throw runtime_error("noninteger edge count");
        for(int i=0;i<N;++i)for(int j:adj[i])
           if(find(adj[j].begin(),adj[j].end(),i)==adj[j].end())throw runtime_error("edge not symmetric");
        vector<int> component(N,-1), sizes;
        for(int start=0;start<N;++start){
            if(component[start]>=0)continue;
            int label=sizes.size(),sz=0;queue<int>q;q.push(start);component[start]=label;
            while(!q.empty()){
                int v=q.front();q.pop();++sz;
                for(int w:adj[v])if(component[w]<0){component[w]=label;q.push(w);}
            }
            sizes.push_back(sz);
        }
        sort(sizes.begin(),sizes.end());
        cout<<"k="<<k<<" states="<<N<<" edges="<<sumDegree/2
            <<" components="<<sizes.size()<<" sizes=";
        for(int z:sizes)cout<<z<<",";
        cout<<"\n";
        if(k==3){
            if(N!=120||sumDegree/2!=60||sizes.size()!=60||sizes.front()!=2||sizes.back()!=2)
                throw runtime_error("three-color graph mismatch");
            continue;
        }
        if(N!=12960 || sumDegree/2!=53280 || sizes.size()!=1)
            throw runtime_error("four-color graph mismatch");
        vector<int> dist(N),Q(N),eccCount(25,0);
        vector<long long> pairs(25,0);
        int witnessA=-1,witnessB=-1,diam=0;
        for(int source=0;source<N;++source){
            fill(dist.begin(),dist.end(),-1);dist[source]=0;
            int head=0,tail=0;Q[tail++]=source;int ecc=0;
            while(head<tail){
                int u=Q[head++];
                for(int v:adj[u])if(dist[v]<0){
                    dist[v]=dist[u]+1;ecc=max(ecc,dist[v]);Q[tail++]=v;
                }
            }
            if(tail!=N)throw runtime_error("disconnected four-color graph");
            ++eccCount[ecc];
            for(int t=source+1;t<N;++t){
                ++pairs[dist[t]];
                if(dist[t]>diam){diam=dist[t];witnessA=configurations[source];witnessB=configurations[t];}
            }
        }
        long long allpairs=accumulate(pairs.begin(),pairs.end(),0LL);
        if(allpairs!=1LL*N*(N-1)/2)throw runtime_error("pair count mismatch");
        if(diam!=14||eccCount[13]!=3360||eccCount[14]!=9600)throw runtime_error("eccentricities mismatch");
        cout<<"radius=13 diameter="<<diam<<" eccentricities=";
        for(int k=0;k<(int)eccCount.size();++k)if(eccCount[k])cout<<k<<":"<<eccCount[k]<<",";
        cout<<" pair_distances=";
        for(int d=1;d<=diam;++d)cout<<d<<":"<<pairs[d]<<",";
        cout<<" witnessA="<<witnessA<<" witnessB="<<witnessB<<"\n";
        cout<<"ALL_EXHAUSTIVE_CHECKS_PASSED\n";
    }
}
