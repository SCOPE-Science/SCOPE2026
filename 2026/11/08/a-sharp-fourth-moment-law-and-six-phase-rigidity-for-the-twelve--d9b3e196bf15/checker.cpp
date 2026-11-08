// Exact fourth-moment computations for the type-A3 twelve-root Fourier aperture.
// C++17; compile: g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
#include <array>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using ll=long long;
using Exponent=vector<int>;
struct Range {int q;ll minU,minV,norm_count;string witness;};

// The returned sign is the exact sign of u+v*sqrt(5), with integral inputs.
int sign_radical(ll u,ll v){
    if(v==0)return (u>0)-(u<0);
    if(u==0)return (v>0)-(v<0);
    if((u>0)==(v>0))return (u>0)?1:-1;
    ll delta=u*u-5*v*v; assert(delta!=0);
    return (u>0)?((delta>0)?1:-1):((delta>0)?-1:1);
}
struct Spectrum {
    vector<pair<int,int>> edges;
    vector<array<int,3>> sites;
    map<array<int,3>,vector<pair<int,int>>> correlations;
    vector<int> free_index;
    Spectrum(){
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(i!=j){
            edges.push_back({i,j});array<int,3> v={0,0,0};
            if(i)v[i-1]++;if(j)v[j-1]--;sites.push_back(v);
        }
        for(int i=0;i<12;i++)for(int j=0;j<12;j++){
            array<int,3>d={0,0,0};for(int k=0;k<3;k++)d[k]=sites[i][k]-sites[j][k];
            correlations[d].push_back({i,j});
        }
        vector<pair<int,int>> anchors={{0,1},{0,2},{0,3},{1,2}};
        for(int i=0;i<12;i++)if(find(anchors.begin(),anchors.end(),edges[i])==anchors.end())free_index.push_back(i);
        assert(free_index.size()==8 && correlations.size()==55);
        int hist[13]={};for(const auto &kv:correlations){hist[kv.second.size()]++;}
        assert(hist[12]==1 && hist[1]==12 && hist[2]==24 && hist[4]==18);
    }
    Exponent from_index(ll h,int q)const{
        Exponent x(12,0);for(int i:free_index){x[i]=h%q;h/=q;}assert(h==0);return x;
    }
    // Eisenstein integer a+b*zeta6 with zeta6^2=zeta6-1, or Gaussian a+b*i.
    ll integer_moment(const Exponent& x,int q)const{
        pair<int,int> root[6];
        if(q==2){root[0]={1,0};root[1]={-1,0};}
        if(q==3){root[0]={1,0};root[1]={-1,1};root[2]={0,-1};}
        if(q==4){root[0]={1,0};root[1]={0,1};root[2]={-1,0};root[3]={0,-1};}
        if(q==6){root[0]={1,0};root[1]={0,1};root[2]={-1,1};root[3]={-1,0};root[4]={0,-1};root[5]={1,-1};}
        ll score=0;
        for(const auto &kv:correlations){
            ll a=0,b=0;
            for(auto [i,j]:kv.second){int k=x[i]-x[j];if(k<0)k+=q;a+=root[k].first;b+=root[k].second;}
            score+=a*a+b*b+((q==3||q==6)?a*b:0);
        }
        return score;
    }
    // For zeta5, |sum n_r zeta5^r|^2=(u+v*sqrt(5))/2.
    pair<ll,ll> five_moment(const Exponent& x)const{
        ll c0=0,c1=0,c2=0;
        for(const auto &kv:correlations){
            int n[5]={};for(auto [i,j]:kv.second){int k=x[i]-x[j];if(k<0)k+=5;n[k]++;}
            for(int k=0;k<5;k++){
                c0+=n[k]*n[k];c1+=n[k]*n[(k+1)%5];c2+=n[k]*n[(k+2)%5];
            }
        }
        return {2*c0-c1-c2,c1-c2};
    }
    // Independent convolution formula: M4 is squared coefficient norm of P^2.
    pair<ll,ll> convolution_five(const Exponent &x)const{
        map<array<int,3>,array<int,5>> conv;
        for(int i=0;i<12;i++)for(int j=0;j<12;j++){
            array<int,3>s={0,0,0};for(int k=0;k<3;k++)s[k]=sites[i][k]+sites[j][k];
            conv[s][(x[i]+x[j])%5]++;
        }
        ll c0=0,c1=0,c2=0;
        for(auto [shift,n]:conv)for(int k=0;k<5;k++){
            c0+=n[k]*n[k];c1+=n[k]*n[(k+1)%5];c2+=n[k]*n[(k+2)%5];
        }
        return {2*c0-c1-c2,c1-c2};
    }
    ll convolution_integer(const Exponent &x,int q)const{
        map<array<int,3>,vector<int>> conv;
        for(int i=0;i<12;i++)for(int j=0;j<12;j++){
            array<int,3>s={0,0,0};for(int k=0;k<3;k++)s[k]=sites[i][k]+sites[j][k];
            auto &n=conv[s];if(n.empty())n.resize(q);n[(x[i]+x[j])%q]++;
        }
        pair<int,int> root[6];
        if(q==2){root[0]={1,0};root[1]={-1,0};}
        if(q==3){root[0]={1,0};root[1]={-1,1};root[2]={0,-1};}
        if(q==4){root[0]={1,0};root[1]={0,1};root[2]={-1,0};root[3]={0,-1};}
        if(q==6){root[0]={1,0};root[1]={0,1};root[2]={-1,1};root[3]={-1,0};root[4]={0,-1};root[5]={1,-1};}
        ll score=0;for(auto [shift,n]:conv){ll a=0,b=0;
            for(int k=0;k<q;k++){a+=n[k]*root[k].first;b+=n[k]*root[k].second;}
            score+=a*a+b*b+((q==3||q==6)?a*b:0);
        }
        return score;
    }
};
int main(){
    Spectrum spec;
    const vector<Range> expected={{2,376,0,3,"000000011101"},
                                  {3,432,0,16,"000200011101"},
                                  {4,376,0,9,"000000022202"},
                                  {5,480,-40,24,"000000132312"},
                                  {6,360,0,2,"000101354523"}};
    ll total=0;
    for(const auto &row:expected){
        int q=row.q;ll limit=1;for(int k=0;k<8;k++)limit*=q;
        ll bestU=0,bestV=0,count=0;bool first=true;
        vector<string> optima;
        for(ll i=0;i<limit;i++){
            Exponent x=spec.from_index(i,q);
            ll u=0,v=0;
            if(q==5){tie(u,v)=spec.five_moment(x);}
            else {u=2*spec.integer_moment(x,q);}
            if(first||sign_radical(u-bestU,v-bestV)<0){bestU=u;bestV=v;count=0;optima.clear();first=false;}
            if(u==bestU&&v==bestV){count++;string s;for(int k:x)s+=char('0'+k);optima.push_back(s);}
        }
        assert(bestU==row.minU&&bestV==row.minV&&count==row.norm_count);
        assert(find(optima.begin(),optima.end(),row.witness)!=optima.end());
        if(q==6){assert(optima.size()==2);sort(optima.begin(),optima.end());
            assert(optima[0]=="000101354523"&&optima[1]=="000505312143");}
        Exponent witness;for(char c:row.witness)witness.push_back(c-'0');
        if(q==5){assert(spec.convolution_five(witness)==spec.five_moment(witness));}
        else assert(spec.convolution_integer(witness,q)==spec.integer_moment(witness,q));
        total+=limit;
        cout<<"q="<<q<<" states="<<limit<<" min=";
        if(q==5)cout<<"240-20sqrt(5)";
        else cout<<bestU/2;
        cout<<" normalized="<<count<<" total="<<count*llround(pow((double)q,4))<<"\n";
    }
    // Independent second-path checks on the two normalized global minimizers.
    for(const string& str:{string("000101354523"),string("000505312143")}){
        Exponent x;for(char c:str)x.push_back(c-'0');
        assert(spec.integer_moment(x,6)==180);
        assert(spec.convolution_integer(x,6)==180);
    }
    cout<<"A3_FOURTH_MOMENT_EXACT_PASS normalized_cases="<<total<<"\n";
}
