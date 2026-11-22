#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

bool embedded(const string& a, const string& w){
    int j=0;
    for(char c:w) if(j<int(a.size()) && c==a[j]) ++j;
    return j==int(a.size());
}
bool minimal(const string& a, const string& b, const string& w){
    if(!embedded(a,w)||!embedded(b,w))return false;
    for(int p=0;p<int(w.size());++p){
        string t=w.substr(0,p)+w.substr(p+1);
        if(embedded(a,t)&&embedded(b,t))return false;
    }
    return true;
}
void gen(const string& a,const string& b,int i,int j,string& w,set<string>& full){
    if(i==int(a.size())&&j==int(b.size())){full.insert(w);return;}
    if(i<int(a.size())){w.push_back(a[i]);gen(a,b,i+1,j,w,full);w.pop_back();}
    if(j<int(b.size())){w.push_back(b[j]);gen(a,b,i,j+1,w,full);w.pop_back();}
}
int main(){
 for(auto [q,k]:vector<pair<int,int>>{{3,1},{3,2},{3,3},{4,1},{4,2},{5,1},{5,2}}){
    string a,b;
    for(int rep=0;rep<k;++rep){for(int j=0;j<q;++j)a+=char('0'+j);for(int j=1;j<q;++j)b+=char('0'+j);b+='0';}
    set<string> ws;string cur;gen(a,b,0,0,cur,ws);
    int good=0;
    for(const auto& w:ws)good+=minimal(a,b,w);
    int expected=0;
    if(q==3)expected=1;
    if(q==4)expected=1<<(4*k-1);
    if(q==5){int x=0,y=1;for(int j=0;j<10*k-1;++j){int z=x+y;x=y;y=z;}expected=x;}
    cout<<"q="<<q<<" k="<<k<<" shuffled_distinct="<<ws.size()<<" full_length_minimal="<<good<<" expected="<<expected<<"\n";
    if(good!=expected)return 1;
 }
 cout<<"EXHAUSTIVE: PASS\n";
}
