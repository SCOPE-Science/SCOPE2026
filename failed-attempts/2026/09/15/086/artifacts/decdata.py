"""Write exact decomposition + Burnside(image-dim mod17) table to artifacts/decomp_data.json (rerun-safe, fast paths only)."""
import sys, json
sys.path.insert(0,'output/artifacts')
from modp import Mof, image_dim
from exactM2 import M_of, decomp, COMBOS
from exact2 import F,ONE,II,ZETA8
Z=ZETA8
reps={"generic (2,3)":(F(2),F(3)),"t=(1,1)":(ONE,ONE),"t=(1,-1)":(ONE,F(-1)),"t=(-1,1)":(F(-1),ONE),
 "t=(i,1)":(II,ONE),"t=(1,i)":(ONE,II),"t=(i,i)":(II,II),"t=(z,1)":(Z,ONE),"t=(z,z)":(Z,Z)}
modmap={"generic (2,3)":(2,3),"t=(1,1)":(1,1),"t=(1,-1)":(1,16),"t=(-1,1)":(16,1),
 "t=(i,1)":(4,1),"t=(1,i)":(1,4),"t=(i,i)":(4,4),"t=(z,1)":(2,1),"t=(z,z)":(2,2)}
out={}
for name,t in reps.items():
    d=sorted(decomp(M_of(t),COMBOS))
    out[name]={"exact_decomp_dims":d,"mod17_image_dim":image_dim(Mof(modmap[name]))}
    print(name,d,out[name]["mod17_image_dim"],flush=True)
json.dump(out,open("output/artifacts/decomp_data.json","w"),indent=1)
print("wrote decomp_data.json")
