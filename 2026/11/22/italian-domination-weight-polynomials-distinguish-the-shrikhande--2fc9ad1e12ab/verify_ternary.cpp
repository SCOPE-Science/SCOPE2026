#include <bits/stdc++.h>
using namespace std;
struct Stats {array<unsigned long long,33> ways{};array<unsigned long long,33> binary{};};
Stats analyze(int graph_type){
    array<unsigned int,16> nb{};
    auto add=[&](int u,int v){nb[u]|=1u<<v;};
    for(int a=0;a<4;a++)for(int b=0;b<4;b++){
        int i=4*a+b;
        for(int c=0;c<4;c++)for(int d=0;d<4;d++){
            int j=4*c+d;if(i==j)continue;
            int da=(c-a+4)%4,db=(d-b+4)%4;
            bool adjacent =graph_type==0 ? ((a==c)!=(b==d)) :
                ((da==1&&db==0)||(da==3&&db==0)||(da==0&&db==1)||(da==0&&db==3)||(da==1&&db==1)||(da==3&&db==3));
            if(adjacent)add(i,j);
        }
    }
    for(int i=0;i<16;i++){assert(__builtin_popcount(nb[i])==6);for(int j=0;j<16;j++)if(nb[i]>>j&1)assert(nb[j]>>i&1);}
    Stats out;
    function<void(int,int,unsigned int,unsigned int)> recur=[&](int idx,int wt,unsigned int ones,unsigned int twos){
        if(idx==16){
           unsigned int zero=(~(ones|twos))&65535u;
           while(zero){int i=__builtin_ctz(zero);zero&=zero-1;
               if(!(nb[i]&twos)&&__builtin_popcount(nb[i]&ones)<2)return;
           }
           out.ways[wt]++;
           if(!twos)out.binary[wt]++;
           return;
        }
        recur(idx+1,wt,ones,twos);
        recur(idx+1,wt+1,ones|(1u<<idx),twos);
        recur(idx+1,wt+2,ones,twos|(1u<<idx));
    };
    recur(0,0,0,0);
    return out;
}
int main(){
    auto r=analyze(0),s=analyze(1);
    array<unsigned long long,33> expected{};
    expected[4]=8;expected[5]=224;expected[6]=1184;expected[7]=1408;
    expected[8]=1176;expected[9]=832;expected[10]=640;expected[11]=256;
    for(int i=0;i<=32;i++){
        assert(r.ways[i]>=s.ways[i]);
        assert(r.ways[i]-s.ways[i]==expected[i]);
    }
    assert(r.ways[4]==24&&s.ways[4]==16);
    for(int kind=0;kind<2;kind++){
        const auto &a=(kind==0?r:s);
        cout<<(kind==0?"ROOK_COEFFICIENTS ":"SHRIKHANDE_COEFFICIENTS ");
        for(int k=0;k<=32;k++)cout<<a.ways[k]<<(k==32?"\n":" ");
    }
    cout<<"TERNARY_EXHAUSTION_OK\n";
}
