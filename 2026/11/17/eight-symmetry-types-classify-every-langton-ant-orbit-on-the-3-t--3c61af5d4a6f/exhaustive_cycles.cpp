// Exhaustive orbit decomposition for standard turn-flip-move Langton ant on 3x3 torus.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int W = 3, H = 3, L = W*H, S = (1<<L)*L*4;

int successor(int state) {
  int dir=state%4, q=state/4, pos=q%L, bits=q/L;
  int col=pos%W, row=pos/W;
  bool black=((bits>>pos)&1)!=0;
  bits ^= (1<<pos);
  // Direction order north, east, south, west.
  dir=(dir+(black?3:1))%4;
  if(dir==0) row=(row+H-1)%H;
  if(dir==1) col=(col+1)%W;
  if(dir==2) row=(row+1)%H;
  if(dir==3) col=(col+W-1)%W;
  return 4*(L*bits+W*row+col)+dir;
}

int predecessor(int state) {
  int dir=state%4, q=state/4, pos=q%L, bits=q/L;
  int col=pos%W, row=pos/W;
  if(dir==0) row=(row+1)%H;
  if(dir==1) col=(col+W-1)%W;
  if(dir==2) row=(row+H-1)%H;
  if(dir==3) col=(col+1)%W;
  int previous_pos=W*row+col;
  int original_bits=bits^(1<<previous_pos);
  bool previous_black=((original_bits>>previous_pos)&1)!=0;
  int previous_dir=(dir+(previous_black?1:3))%4;
  return 4*(L*original_bits+previous_pos)+previous_dir;
}
int main() {
 vector<bool> visited(S,false);
 for(int state=0;state<S;state++) {
   int forward=successor(state);
   assert(0<=forward && forward<S);
   assert(predecessor(forward)==state);
   assert(successor(predecessor(state))==state);
 }
 map<int,int> cycles;
 for(int state=0;state<S;state++) {
   if(visited[state])continue;
   int current=state, count=0;
   do {
     assert(!visited[current]);
     visited[current]=true;
     current=successor(current);
     ++count;
     assert(count<=S);
   } while(current!=state);
   cycles[count]++;
 }
 const map<int,int> expected={{18,24},{30,24},{42,24},{66,24},
                               {70,72},{74,72},{78,24},{102,24}};
 assert(cycles==expected);
 int states=0,orbits=0;
 for(auto [period,number]:cycles){
   states+=period*number;orbits+=number;
   cout<<"period="<<period<<", cycles="<<number<<", states="<<period*number<<'\n';
 }
 assert(states==S && orbits==288);
 cout<<"FULL_ENUMERATION_OK states="<<states<<" cycles="<<orbits<<'\n';
}
