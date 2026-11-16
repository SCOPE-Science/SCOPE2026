#include <bits/stdc++.h>
using namespace std;
using ll=long long;
static const int N=10,M=15,L=1<<M;
static const array<pair<int,int>,M> edges={{{0,1},{0,4},{0,5},{1,2},{1,6},{2,3},{2,7},{3,4},{3,8},{4,9},{5,7},{5,8},{6,8},{6,9},{7,9}}};
static int idx[N][N];
static vector<pair<int,int>> cycles;
static vector<int> paths;
void traverse(int start,int u,int seen){
    for(int v=0;v<N;v++) if(idx[u][v]>=0){
        if(v==start){
            if(paths.size()<5 || paths[1]>paths.back())continue;
            int mask=0,direction=0;
            for(int i=0;i<(int)paths.size();i++){
                int a=paths[i], b=paths[(i+1)%paths.size()],j=idx[a][b];
                mask|=1<<j;
                if(a>b)direction|=1<<j;
            }
            cycles.emplace_back(mask,direction);
        }else if(v>start && !(seen&(1<<v))){
            paths.push_back(v);traverse(start,v,seen|(1<<v));paths.pop_back();
        }
    }
}
bool kahn(int m){
    int indeg[N]={},out[N]={};
    for(int j=0;j<M;j++){
        auto[a,b]=edges[j];if(m&(1<<j))swap(a,b);
        indeg[b]++;out[a]|=1<<b;
    }
    int q[N]={},head=0,tail=0;
    for(int v=0;v<N;v++)if(!indeg[v])q[tail++]=v;
    while(head<tail){int u=q[head++];for(int v=0;v<N;v++)if(out[u]&(1<<v))if(--indeg[v]==0)q[tail++]=v;}
    return tail==N;
}
bool nocycle(int m){
    for(auto[sel,d]:cycles)if((m&sel)==d || (m&sel)==(sel^d))return false;
    return true;
}
void walsh(vector<ll>&a){for(int j=1;j<L;j<<=1)for(int i=0;i<L;i+=2*j)for(int k=0;k<j;k++){
    ll x=a[i+k],y=a[i+k+j];a[i+k]=x+y;a[i+k+j]=x-y;
}}
int dist_edges(int i,int j){
    if(i==j)return 0;
    int d[M];fill(d,d+M,999);d[i]=0;queue<int>q;q.push(i);
    while(!q.empty()){
        int k=q.front();q.pop();
        for(int x=0;x<M;x++) if(d[x]==999 && (edges[k].first==edges[x].first ||edges[k].first==edges[x].second ||edges[k].second==edges[x].first||edges[k].second==edges[x].second)){
            d[x]=d[k]+1;q.push(x);
        }
    }
    return d[j];
}
int main(){
    for(auto &row:idx)fill(row,row+N,-1);
    for(int i=0;i<M;i++){auto[a,b]=edges[i];idx[a][b]=idx[b][a]=i;}
    for(int s=0;s<N;s++){paths={s};traverse(s,s,1<<s);}
    sort(cycles.begin(),cycles.end());cycles.erase(unique(cycles.begin(),cycles.end()),cycles.end());
    vector<ll>a(L);vector<int>valid;
    for(int m=0;m<L;m++){
        bool c=kahn(m),d=nocycle(m);
        if(c!=d)throw runtime_error("acyclicity methods disagree");
        if(c){a[m]=1;valid.push_back(m);}
    }
    if(valid.size()!=16680)throw runtime_error("orientation total");
    auto W=a;walsh(W);
    for(int t=0;t<L;t++){
        ll direct=0;
        if(__builtin_parity((unsigned)t)==0){for(int m:valid)direct+=__builtin_parity((unsigned)(t&m))?-1:1;}
        if(W[t]!=direct)throw runtime_error("direct character sum mismatch");
    }
    map<ll,int> hist,abs_hist,kernel_hist;
    int zeros=0,oddzeros=0;ll sq=0;
    for(int t=0;t<L;t++){
        hist[W[t]]++;abs_hist[llabs(W[t])]++;sq+=W[t]*W[t];
        if(W[t]==0){zeros++;oddzeros+=__builtin_parity((unsigned)t);}
    }
    if(sq!=1LL*L*valid.size() || zeros!=19112 || oddzeros!=L/2 || L-zeros!=13656)throw runtime_error("spectral invariants");
    if(abs_hist.size()!=31||abs_hist[0]!=19112||abs_hist[1944]!=30||abs_hist[1080]!=60)throw runtime_error("absolute histogram");
    vector<ll>H(L);for(int t=0;t<L;t++)H[t]=(W[t]!=0);
    walsh(H);ll total_abs=0,ksq=0;
    for(ll h:H){kernel_hist[h]++;total_abs+=llabs(h);ksq+=h*h;}
    if(total_abs!=1113888 || ksq!=1LL*L*13656)throw runtime_error("projection invariants");
    int pair_count[4]={};for(int i=0;i<M;i++)for(int j=i+1;j<M;j++){
        int d=dist_edges(i,j);pair_count[d]++;
        ll magnitude=d==1?1944:d==2?1080:d==3?0:-1;
        if(llabs(W[(1<<i)|(1<<j)])!=magnitude)throw runtime_error("pair correlation shells");
    }
    if(pair_count[1]!=30||pair_count[2]!=60||pair_count[3]!=15)throw runtime_error("line graph distances");
    ifstream hfile("walsh_histogram.csv");if(!hfile)throw runtime_error("missing spectral certificate");
    string line;getline(hfile,line);if(line!="multiplier,multiplicity")throw runtime_error("spectral header");
    for(auto [v,c]:hist){getline(hfile,line);if(line!=to_string(v)+","+to_string(c))throw runtime_error("spectral certificate mismatch");}
    if(getline(hfile,line))throw runtime_error("spectral trailing data");
    ifstream kfile("projection_kernel_histogram.csv");if(!kfile)throw runtime_error("missing kernel certificate");
    getline(kfile,line);if(line!="unnormalized_kernel,multiplicity")throw runtime_error("kernel header");
    for(auto [v,c]:kernel_hist){getline(kfile,line);if(line!=to_string(v)+","+to_string(c))throw runtime_error("kernel certificate mismatch");}
    if(getline(kfile,line))throw runtime_error("kernel trailing data");
    cout<<"PETERSEN_ACYCLIC_FOURIER_PASS cycles="<<cycles.size()<<" orientations="<<valid.size()<<" zeros="<<zeros<<" rank="<<L-zeros<<" pair_shells="<<pair_count[1]<<","<<pair_count[2]<<","<<pair_count[3]<<" abs_kernel="<<total_abs<<"\n";
}
