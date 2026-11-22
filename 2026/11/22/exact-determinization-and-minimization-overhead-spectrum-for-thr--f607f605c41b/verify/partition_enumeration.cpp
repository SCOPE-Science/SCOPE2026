// Exact enumeration of three-state, two-letter epsilon-free NFAs.
// Run: g++ -std=c++17 -O2 verify/partition_enumeration.cpp -o /tmp/partition
//      /tmp/partition data/joint_spectrum.csv
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
using namespace std;

using Key=tuple<int,int,int>;  // final-case index, reachable states, quotient states
using Counts=map<Key,array<long long,2>>;

int main(int argc,char**argv){
    if(argc!=2){cerr<<"Pass expected CSV path\n";return 2;}
    array<array<unsigned char,8>,512> action{};
    for(int code=0;code<512;++code){
        int row[3]={code&7,(code>>3)&7,(code>>6)&7};
        for(int mask=0;mask<8;++mask){
            int image=0;
            for(int state=0;state<3;++state)if(mask&(1<<state))image|=row[state];
            action[code][mask]=static_cast<unsigned char>(image);
        }
    }
    Counts hist;
    for(int a=0;a<512;++a)for(int b=0;b<512;++b){
        for(int which=0;which<2;++which){
            const int finalMask=(which==0)?1:4;  // coincident / distinct
            unsigned char wordNext[8][2];
            for(int s=0;s<8;++s){wordNext[s][0]=action[a][s];wordNext[s][1]=action[b][s];}
            int list[8],sz=0;bool seen[8]={};
            list[sz++]=1;seen[1]=true;
            for(int i=0;i<sz;++i)for(int letter=0;letter<2;++letter){
                int image=wordNext[list[i]][letter];
                if(!seen[image]){seen[image]=true;list[sz++]=image;}
            }
            // Myhill--Nerode partition refinement on reachable subsets.
            int oldClass[8],newClass[8];
            for(int i=0;i<sz;++i)oldClass[i]=(list[i]&finalMask)?1:0;
            int quotient=0;
            while(true){
                map<array<int,3>,int> classes;
                for(int i=0;i<sz;++i){
                    array<int,3> sig={oldClass[i],-1,-1};
                    for(int letter=0;letter<2;++letter){
                        int target=wordNext[list[i]][letter];
                        for(int j=0;j<sz;++j)if(list[j]==target){sig[letter+1]=oldClass[j];break;}
                    }
                    auto it=classes.find(sig);
                    if(it==classes.end()){
                        int id=static_cast<int>(classes.size());
                        classes.emplace(sig,id);newClass[i]=id;
                    }else newClass[i]=it->second;
                }
                quotient=static_cast<int>(classes.size());
                bool done=true;
                // Equal partitions, not merely identical class numbers, imply stability.
                for(int i=0;i<sz;++i)for(int j=0;j<i;++j){
                    if((oldClass[i]==oldClass[j])!=(newClass[i]==newClass[j]))done=false;
                }
                for(int i=0;i<sz;++i)oldClass[i]=newClass[i];
                if(done)break;
            }
            // Trim exactly when all states are accessible and co-accessible.
            int forward=0;for(int i=0;i<sz;++i)forward|=list[i];
            int reverse=finalMask;
            for(;;){
                int next=reverse;
                for(int s=0;s<3;++s)if((wordNext[1<<s][0]|wordNext[1<<s][1])&reverse)next|=1<<s;
                if(next==reverse)break;
                reverse=next;
            }
            bool trim=(forward==7 && reverse==7);
            auto &c=hist[make_tuple(which,sz,quotient)];
            ++c[0];if(trim)++c[1];
        }
    }
    ifstream in(argv[1]);if(!in){cerr<<"Cannot open reference table\n";return 2;}
    string line;getline(in,line); // CSV header
    int lines=0; long long total[2]={},trimTotal[2]={};
    while(getline(in,line)){
        string seg[5];int at=0;
        for(char ch:line){if(ch==',')++at;else if(at<5)seg[at]+=ch;}
        if(at!=4){cerr<<"Malformed CSV\n";return 1;}
        int which=seg[0]=="coincident"?0:seg[0]=="distinct"?1:-1;
        if(which<0){cerr<<"Bad case\n";return 1;}
        int r=stoi(seg[1]),m=stoi(seg[2]);
        auto it=hist.find(make_tuple(which,r,m));
        if(it==hist.end()||it->second[0]!=stoll(seg[3])||it->second[1]!=stoll(seg[4])){
            cerr<<"Mismatch "<<line<<"\n";return 1;
        }
        total[which]+=it->second[0];trimTotal[which]+=it->second[1];
        hist.erase(it);++lines;
    }
    if(!hist.empty()||lines!=62||total[0]!=262144||total[1]!=262144||
       trimTotal[0]!=190080||trimTotal[1]!=209664){cerr<<"Incomplete census\n";return 1;}
    cout<<"PASS partition census: 62 cells, two 262144-machine families, trim "
        <<trimTotal[0]<<" and "<<trimTotal[1]<<"\n";
    return 0;
}
