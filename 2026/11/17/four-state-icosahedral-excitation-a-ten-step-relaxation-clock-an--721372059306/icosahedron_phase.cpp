#include <iostream>
#include <cstdint>
using namespace std;
int main(){
 // Graph given by vertex-neighbor bit masks, independently tabulated.
 constexpr uint16_t N[12]={0x03e,0x465,0x0cb,0x195,0x329,0x613,0xc86,0x94c,0xa98,0xd30,0xa62,0x7c0};
 uint64_t rotating=0;
 for(uint32_t code=0;code<(1u<<24);++code){
  uint16_t class_mask[4]={0,0,0,0};
  uint32_t y=code;
  for(int v=0;v<12;v++,y>>=2) class_mask[y&3] |= 1u<<v;
  bool good=true;
  for(int k=0;k<4&&good;k++){
   uint16_t todo=class_mask[k],successor=class_mask[(k+1)&3];
   while(todo){int i=__builtin_ctz((unsigned)todo);todo&=todo-1;
     if((N[i]&successor)==0){good=false;break;}
   }
  }
  rotating += good;
 }
 cout<<"four_phase_state_count="<<rotating<<"\n";
 cout<<"four_phase_orbits="<<rotating/4<<"\n";
 if(rotating!=835400) return 3;
}
