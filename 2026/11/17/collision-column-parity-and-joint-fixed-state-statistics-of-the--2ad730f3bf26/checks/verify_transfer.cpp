// Independent local-constraint enumeration for a one-step fixed HPP lattice gas.
// Column states are two four-channel masks (8 bits). No proof classification is used.
#include <bits/stdc++.h>
using namespace std;
inline int row(int col,int r){return (col>>(4*r))&15;}
inline bool fixmid(int a,int b,int c){
    for(int r=0;r<2;r++){
        int br=row(b,r),other=row(b,1-r),ar=row(a,r),cr=row(c,r);
        int incoming=(other&1)|(ar&2)|(other&4)|(cr&8);
        int output=incoming==5?10:incoming==10?5:incoming;
        if(output!=br)return false;
    }
    return true;
}
inline pair<int,int> observables(initializer_list<int> cols){
    int p=0,k=0;
    for(int column:cols){
        int z=row(column,0),w=row(column,1);
        p+=__builtin_popcount(static_cast<unsigned>(z)) + __builtin_popcount(static_cast<unsigned>(w));
        if(z==5||z==10){
            if(w!=(z==5?10:5))throw runtime_error("unpaired collision");
            k++;
        }else if(w==5||w==10)throw runtime_error("unpaired collision");
    }
    return {p,k};
}
int main(){
    vector<vector<uint16_t>>adj(65536);
    size_t edges=0; int maxdeg=0;
    for(int a=0;a<256;a++)for(int b=0;b<256;b++){
        auto &v=adj[a*256+b];
        for(int c=0;c<256;c++)if(fixmid(a,b,c))v.push_back(c);
        edges+=v.size();maxdeg=max(maxdeg,(int)v.size());
    }
    cout<<"vertices=65536 edges="<<edges<<" maxdeg="<<maxdeg<<"\n";
    unsigned long long count3=0,count4=0;
    map<pair<int,int>,unsigned long long>hist4;
    for(int a=0;a<256;a++)for(int b=0;b<256;b++)for(int c:adj[a*256+b]){
        if(fixmid(b,c,a)&&fixmid(c,a,b))count3++;
        for(int d:adj[b*256+c])if(fixmid(c,d,a)&&fixmid(d,a,b)){
            count4++;
            hist4[observables({a,b,c,d})]++;
        }
    }
    cout<<"n=3 fixed="<<count3<<"\n";
    cout<<"n=4 fixed="<<count4<<"\n";
    for(auto const &[key,value]:hist4)
        cout<<"occupancy="<<key.first<<" collision_columns="<<key.second<<" count="<<value<<"\n";
}
