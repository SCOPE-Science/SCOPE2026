// Exhaustive forcing census for two 16-vertex strongly regular graphs.
// C++17; no third-party dependencies. Every 16-bit subset is examined.
#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cassert>
using namespace std;
static constexpr int N=16, FULL=(1<<N)-1;
using Neighbors=array<int,N>;
int pop(int x){return __builtin_popcount((unsigned)x);}
Neighbors make_graph(bool shrikhande){
    Neighbors a{};
    for(int v=0;v<N;++v){
        int r=v/4,c=v%4;
        for(int u=0;u<N;++u){
            if(u==v)continue;
            int s=u/4,t=u%4;
            bool edge=false;
            if(!shrikhande)edge=(r==s || c==t);
            else{
                int dx=(s-r+4)%4,dy=(t-c+4)%4;
                edge=(dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||(dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3);
            }
            if(edge)a[v]|=1<<u;
        }
    }
    return a;
}
bool is_fort(int white, const Neighbors& a){
    if(!white)return false;
    for(int v=0;v<N;++v)if(pop(white&a[v])==1)return false;
    return true;
}
bool succeeds(int blue, const Neighbors& a, bool skew){
    int white=FULL^blue;
    for(int step=0;step<N;++step){
        if(!white)return true;
        int forces=0;
        for(int v=0;v<N;++v){
            if(!skew && !((blue>>v)&1))continue;
            int w=white&a[v];
            if(w && !(w&(w-1)))forces|=w;
        }
        if(!forces)break;
        white&=~forces;
        blue|=forces;
    }
    return white==0;
}
void analyze(const string& label,bool sh){
    auto a=make_graph(sh);
    for(int u=0;u<N;++u){
        assert(pop(a[u])==6);
        for(int v=0;v<N;++v){
            assert(bool(a[u]&(1<<v)) == bool(a[v]&(1<<u)));
            if(u==v)continue;
            assert(pop(a[u]&a[v])==2);
        }
    }
    array<int,N+1> skew{},ord{},allfort{};
    vector<int> forts, minfort;
    for(int white=0;white<=FULL;++white){
        int blue=FULL^white,k=pop(blue);
        skew[k]+=succeeds(blue,a,true);
        ord[k]+=succeeds(blue,a,false);
        if(is_fort(white,a)){forts.push_back(white);allfort[pop(white)]++;}
    }
    for(int W:forts){
        bool minimal=true;
        for(int U:forts){
            if(U!=W && (U&W)==U){minimal=false;break;}
        }
        if(minimal)minfort.push_back(W);
    }
    // Fort characterization independently certifies all forcing outcomes.
    for(int W=0;W<=FULL;++W){
        bool contains_fort=false;
        for(int F:minfort)if((W&F)==F){contains_fort=true;break;}
        assert(contains_fort == !succeeds(FULL^W,a,true));
    }
    array<int,N+1> mf{};
    map<string,int> types4;
    for(int W:minfort){
        mf[pop(W)]++;
        if(pop(W)==4){
            array<int,5> degree{};
            for(int v=0;v<N;++v)if(W&(1<<v))degree[pop(W&a[v])]++;
            string typ;
            for(int d=0;d<=4;++d)typ+=to_string(d)+":"+to_string(degree[d])+";";
            types4[typ]++;
        }
    }
    cout<<label<<"\n";
    auto output=[&](string tag,auto &xs){cout<<tag;for(auto x:xs)cout<<" "<<x;cout<<"\n";};
    output("skew",skew); output("ordinary",ord);output("minimal_fort_by_size",mf);
    for(auto& [typ,num]:types4)cout<<"four_fort_type "<<typ<<" "<<num<<"\n";
    assert(minfort.size()==316 && mf[4]==60 && mf[6]==256);
    assert(skew[10]==4032 && skew[11]==3648 && skew[12]==1760);
    assert(ord[10]==(sh?3616:3456) && ord[11]==(sh?3600:3504));
}
int main(){analyze("rook",false);analyze("shrikhande",true);}
