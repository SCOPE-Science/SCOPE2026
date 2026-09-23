#!/usr/bin/env python3
"""Independent verifier for rectilinear K(5,7) drawing.
Reads coords_K57_rect.json, checks general position (no 3 collinear) with exact
integer arithmetic, counts rectilinear crossings over disjoint edge pairs via
orientation predicates, writes crossing_list.csv, asserts 36.
Usage: python3 verify_rect.py [coords.json] [out_csv]
"""
import json, sys, itertools, csv, pathlib

def orient(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])

def proper_cross(a,b,c,d):
    o1=orient(a,b,c); o2=orient(a,b,d); o3=orient(c,d,a); o4=orient(c,d,b)
    # general position => none zero for triples among vertices; but be strict:
    if o1==0 or o2==0 or o3==0 or o4==0:
        return None  # degenerate (should not happen)
    return ((o1>0)!=(o2>0)) and ((o3>0)!=(o4>0))

def main():
    base = pathlib.Path(__file__).parent
    coords_path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else base/"coords_K57_rect.json"
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv)>2 else base/"crossing_list.csv"
    data=json.loads(pathlib.Path(coords_path).read_text())
    A=[tuple(p) for p in data["A"]]; B=[tuple(p) for p in data["B"]]
    assert len(A)==5 and len(B)==7, (len(A),len(B))
    pts=A+B
    assert len(set(pts))==12, "duplicate points"
    # general position
    bad=[]
    for i,j,k in itertools.combinations(range(12),3):
        if orient(pts[i],pts[j],pts[k])==0:
            bad.append((i,j,k))
    print(f"points: 12 distinct; collinear triples: {len(bad)}")
    if bad:
        print("FAIL general position:", bad[:10]); sys.exit(1)
    # edges: (ai,bj)
    edges=[((i,j),A[i],B[j]) for i in range(5) for j in range(7)]
    assert len(edges)==35
    total_pairs=35*34//2
    print(f"total edge pairs C(35,2)={total_pairs}")
    # disjoint pairs: share no endpoint
    disjoint=0; crossings=[]
    for e1 in range(35):
        for e2 in range(e1+1,35):
            (i1,j1),a1,b1=edges[e1]; (i2,j2),a2,b2=edges[e2]
            if i1==i2 or j1==j2:
                continue
            disjoint+=1
            c=proper_cross(a1,b1,a2,b2)
            if c is None:
                print(f"DEGENERATE pair {e1},{e2}"); sys.exit(1)
            if c:
                crossings.append(((i1,j1),(i2,j2)))
    print(f"disjoint edge pairs = C(5,2)*C(7,2)*2 = 10*21*2 = {disjoint}")
    assert disjoint==420, disjoint
    print(f"2+2 quads C(5,2)*C(7,2)=210; each quad has 2 disjoint pairs, at most 1 crosses")
    print(f"crossing disjoint pairs: {len(crossings)}")
    # write csv
    with open(out_path,"w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["crossing_id","a1","b1","a2","b2"])
        for k,((i1,j1),(i2,j2)) in enumerate(sorted(crossings)):
            w.writerow([k,i1,j1,i2,j2])
    print(f"wrote {out_path} with {len(crossings)} rows")
    expected=data.get("claim_crossings",36)
    if len(crossings)!=expected:
        print(f"FAIL: got {len(crossings)} expected {expected}"); sys.exit(1)
    print(f"PASS: rectilinear crossings = {expected}")
    # Zarankiewicz control
    Z=(5//2)*((5-1)//2)*(7//2)*((7-1)//2)
    print(f"Zarankiewicz Z(5,7)=floor(5/2)*floor(4/2)*floor(7/2)*floor(6/2)=2*2*3*3={Z}")
    assert Z==36

if __name__=="__main__":
    main()
