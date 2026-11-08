#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;
struct Graph {
    vector<vector<int>> adj;
    Graph(){adj.resize(1);}
    void add_edge(int a,int b){adj[a].push_back(b);adj[b].push_back(a);}
    void triangle(int anchor, int h){
        int a=adj.size();adj.resize(a+2);int b=a+1;
        add_edge(anchor,a);add_edge(anchor,b);add_edge(a,b);
        if(h>0){triangle(a,h-1);triangle(b,h-1);}
    }
};
static bool is_period3(const int *x, const vector<vector<int>>&adj){
    int a[15],b[15],c[15];int n=adj.size();
    auto update=[&](const int *s,int *o){
        for(int i=0;i<n;i++){
            if(s[i]==1)o[i]=2;
            else if(s[i]==2)o[i]=0;
            else {o[i]=0;for(int j:adj[i]) if(s[j]==1){o[i]=1;break;}}
        }
    };
    update(x,a);update(a,b);update(b,c);
    bool unchanged=true,return3=true;
    for(int i=0;i<n;i++){
        if(a[i]!=x[i]) unchanged=false;
        if(c[i]!=x[i]) return3=false;
    }
    return return3&&!unchanged;
}
int main(){
    for(int h=0;h<=2;h++){
        Graph g;g.triangle(0,h);
        auto n=g.adj.size();assert(n<=15);
        uint64_t max_state=1;for(size_t i=0;i<n;i++)max_state*=3;
        uint64_t result=0;int state[15];
        for(uint64_t id=0;id<max_state;id++){
            uint64_t k=id;for(size_t i=0;i<n;i++){state[i]=k%3;k/=3;}
            if(is_period3(state,g.adj)) result++;
        }
        printf("height=%d vertices=%zu all_states=%llu primitive_three=%llu\n",h,n,(unsigned long long)max_state,(unsigned long long)result);
        assert(result==(h==0?6:h==1?102:36390));
    }
    puts("DIRECT_GHM_OK");
}
