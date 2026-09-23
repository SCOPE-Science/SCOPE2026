# Census of clean degree-8 dessins, passport black 2^4 / white 3^2 2^1.
# Stdlib only, no network. Rerunnable in seconds on a single core.
import itertools, json, os

N = 8
S0_CAN = (1,0,3,2,5,4,7,6)  # (0 1)(2 3)(4 5)(6 7), 0-indexed image list

def compose(p,q):
    return tuple(p[q[i]] for i in range(N))
def inv(p):
    q=[0]*N
    for i,pi in enumerate(p):
        q[pi]=i
    return tuple(q)
def cycle_type(p):
    vis=[False]*N
    lens=[]
    for i in range(N):
        if not vis[i]:
            j=i; l=0
            while not vis[j]:
                vis[j]=True; j=p[j]; l+=1
            lens.append(l)
    lens.sort(reverse=True)
    return tuple(lens)
def cycles_str(p):
    # 1-indexed disjoint cycle notation, omit 1-cycles unless identity
    vis=[False]*N
    parts=[]
    for i in range(N):
        if not vis[i]:
            cyc=[]; j=i
            while not vis[j]:
                vis[j]=True; cyc.append(j+1); j=p[j]
            if len(cyc)>1:
                parts.append("("+ " ".join(map(str,cyc)) +")")
    return "".join(parts) if parts else "(id)"
def is_transitive(a,b):
    ai=inv(a); bi=inv(b)
    seen={0}; stack=[0]
    while stack:
        x=stack.pop()
        for y in (a[x],b[x],ai[x],bi[x]):
            if y not in seen:
                seen.add(y); stack.append(y)
    return len(seen)==N

def all_perms_of_type(typ):
    out=[]
    for p in itertools.permutations(range(N)):
        if cycle_type(p)==typ:
            out.append(p)
    return out

def main():
    print("== clean degree-8 passport (2^4 ; 3^2 2^1) census ==")
    print("s0_can =", cycles_str(S0_CAN), "imagelist", list(S0_CAN))
    S1_ALL = all_perms_of_type((3,3,2))
    print("count s1 type (3,3,2):", len(S1_ALL))
    assert len(S1_ALL)==1120, "expected 1120"
    S0_ALL = all_perms_of_type((2,2,2,2))
    print("count s0 type (2^4):", len(S0_ALL))
    assert len(S0_ALL)==105, "expected 105"
    print("total pairs 105*1120 =", len(S0_ALL)*len(S1_ALL))
    assert len(S0_ALL)*len(S1_ALL)==117600
    # centralizer of s0_can by brute force over S8
    cent=[]
    for p in itertools.permutations(range(N)):
        if compose(p,S0_CAN)==compose(S0_CAN,p):
            cent.append(p)
    print("centralizer size:", len(cent))
    assert len(cent)==384
    # transitive with fixed s0_can
    trans=[p for p in S1_ALL if is_transitive(S0_CAN,p)]
    print("transitive s1 with s0_can:", len(trans))
    assert len(trans)==960
    # full 117600-pair transitive count (global check)
    full_trans=0
    for s0 in S0_ALL:
        for s1 in S1_ALL:
            if is_transitive(s0,s1):
                full_trans+=1
    print("global transitive pairs (105 x 1120):", full_trans)
    assert full_trans==100800, "expected 100800"
    print("check 100800/105 =", full_trans//105, "(should equal 960)")
    assert full_trans//105==960
    # centralizer orbits on trans
    seen=set(); reps=[]
    for s1 in sorted(trans):
        if s1 in seen:
            continue
        orb=set()
        for c in cent:
            orb.add(compose(compose(c,s1),inv(c)))
        assert orb.issubset(set(trans)), "orbit leaves transitive set"
        reps.append((s1,sorted(orb)))
        seen|=orb
    print("num centralizer classes:", len(reps))
    assert len(reps)==4
    # per-class data
    face_types_seen=set()
    total_orbit=0
    for idx,(rep,orb) in enumerate(sorted(reps, key=lambda r: (cycle_type(inv(compose(S0_CAN,r[0]))), r[0]))):
        s1=rep
        s01=compose(S0_CAN,s1)
        sInf=inv(s01)
        assert compose(compose(S0_CAN,s1),sInf)==tuple(range(N)), "s0*s1*sInf != 1"
        ft=cycle_type(sInf)
        face_types_seen.add(ft)
        F=len(ft)
        chi=7-8+F
        assert (2-chi)%2==0
        g=(2-chi)//2
        stab=sum(1 for c in cent if compose(compose(c,s1),inv(c))==s1)
        assert len(orb)*stab==384, "orbit-stabilizer"
        total_orbit+=len(orb)
        print(f"--- class {idx} ---")
        print("  s1 imagelist:", list(s1), "cycles:", cycles_str(s1))
        print("  sInf imagelist:", list(sInf), "cycles:", cycles_str(sInf))
        print("  face type:", ft, "F=",F,"chi=",chi,"g=",g)
        print("  orbit size:", len(orb), "stabilizer(aut):", stab)
        # transitivity recheck
        assert is_transitive(S0_CAN,s1)
    print("face types seen:", sorted(face_types_seen))
    assert total_orbit==960
    # required face distribution
    assert set(face_types_seen)=={(6,1,1),(5,2,1),(3,3,2),(8,)}, face_types_seen
    # empty-face checks
    assert (4,3,1) not in face_types_seen, "(4,3,1) should be empty"
    assert (4,2,2) not in face_types_seen, "(4,2,2) should be empty"
    print("EMPTY-FACE CHECK: (4,3,1) absent: True; (4,2,2) absent: True")
    # genera / aut check as multisets
    print("ALL CHECKS PASSED")
    # emit machine-readable table
    table=[]
    for rep,orb in sorted(reps, key=lambda r: (cycle_type(inv(compose(S0_CAN,r[0]))), r[0])):
        s1=rep; sInf=inv(compose(S0_CAN,s1))
        ft=cycle_type(sInf); F=len(ft); g=(2-(7-8+F))//2
        stab=sum(1 for c in cent if compose(compose(c,s1),inv(c))==s1)
        table.append({"s1_imagelist":list(s1),"s1_cycles":cycles_str(s1),
          "sInf_imagelist":list(sInf),"sInf_cycles":cycles_str(sInf),
          "face_type":list(ft),"F":F,"genus":g,"aut":stab,"orbit":len(orb)})
    with open(os.path.join(os.path.dirname(__file__),"triples.json"),"w") as f:
        json.dump({"s0_can_imagelist":list(S0_CAN),"s0_can_cycles":cycles_str(S0_CAN),
          "classes":table},f,indent=2)
    print("wrote triples.json")

if __name__=="__main__":
    main()
