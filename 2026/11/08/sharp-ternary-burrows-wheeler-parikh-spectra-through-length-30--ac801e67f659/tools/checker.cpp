// Exhaustive ternary last-column census for the sharp cyclic-run bound.
// Recompile and run with data/parikh_profiles.csv. Uses only the C++17 standard library.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

struct Census {
  int n=0;
  int w[32]={}, frequency[3]={};
  map<array<int,3>, long long> observed;
  long long sharp=0;
  void visit(int pos) {
    if(pos<n) {
      for(int c=0;c<3;c++) if(pos==0 || c!=w[pos-1]) {
        w[pos]=c; ++frequency[c]; visit(pos+1); --frequency[c];
      }
      return;
    }
    // The proven necessary parity restriction for sharp one-cycle
    // images (Kumallagov, arXiv:2606.01267) is only a safe filter.
    int odd=0;
    for(int c=0;c<3;c++) odd+=(frequency[c]&1);
    if(odd!=(n&1))return;
    const int edge0=frequency[0],edge1=frequency[0]+frequency[1];
    int distance=0;
    for(int i=0;i<n;i++) {
      int sorted=(i<edge0?0:i<edge1?1:2);
      distance+=(w[i]!=sorted);
    }
    if(distance!=(n+1)/2)return;
    int offset[3]={0,edge0,edge1}, seen[3]={}, successor[32];
    for(int i=0;i<n;i++)successor[i]=offset[w[i]]+seen[w[i]]++;
    int p=0,steps=0;
    do {p=successor[p];++steps;} while(p!=0 && steps<n);
    if(p!=0 || steps!=n)return;
    array<int,3> key={frequency[0],frequency[1],frequency[2]};
    sort(key.begin(),key.end());
    ++observed[key];++sharp;
  }
};

int main(int argc,char**argv) {
  if(argc!=2 && argc!=4)throw runtime_error("Usage: checker data/parikh_profiles.csv [first_n last_n]");
  int first=argc==4?stoi(argv[2]):13;
  int last=argc==4?stoi(argv[3]):30;
  if(first<13||last>30||first>last)throw runtime_error("Invalid length range");
  ifstream f(argv[1]);if(!f)throw runtime_error("CSV not found");
  string line;getline(f,line);
  if(line!="n,parikh_min,parikh_mid,parikh_max,sharp_images,witness_BWT_L")
    throw runtime_error("Unexpected CSV header");
  map<int,map<array<int,3>,long long>> claimed;
  while(getline(f,line)) {
    if(line.empty())throw runtime_error("Empty CSV line");
    stringstream ss(line);string field;vector<string> fields;
    while(getline(ss,field,','))fields.push_back(field);
    if(fields.size()!=6)throw runtime_error("Bad CSV row");
    int n=stoi(fields[0]),a=stoi(fields[1]),b=stoi(fields[2]),c=stoi(fields[3]);
    long long count=stoll(fields[4]);
    if(n<13||n>30||a<0||a>b||b>c||a+b+c!=n||count<1)
      throw runtime_error("Invalid scope/Parikh vector");
    array<int,3> key={a,b,c};
    if(!claimed[n].emplace(key,count).second)throw runtime_error("Duplicate key");
  }
  for(int n=first;n<=last;n++) {
    Census v;v.n=n;v.visit(0);
    if(v.observed!=claimed[n])throw runtime_error("Enumeration mismatch at n="+to_string(n));
    cout << n << ": " << v.sharp << " sharp outputs across "
         << v.observed.size() << " unordered Parikh types\n";
  }
  cout << "ALL EXACT PROFILE CHECKS PASSED\n";
}
