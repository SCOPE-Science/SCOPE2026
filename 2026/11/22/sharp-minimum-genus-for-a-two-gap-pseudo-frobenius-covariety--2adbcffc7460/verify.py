from collections import Counter

def brute(F):
    forbidden={2,F-2,F}
    levels=[frozenset()]
    best_genus=F
    best=set()
    while levels:
        nxt=[]
        for A in levels:
            if F-len(A)<best_genus:
                best_genus=F-len(A);best={A}
            elif F-len(A)==best_genus:
                best.add(A)
            m=min(A) if A else F+1
            for v in range(3,m):
                if v in forbidden: continue
                B=A|{v}
                if all(x+y>F or x+y in B for x in B for y in B):nxt.append(B)
        levels=nxt
    return best_genus,best

def formula(k):
    F=2*k+1
    a=[]
    for t in range(max(0,(k-3+2)//3),k-1):
        A=frozenset({2*k}|{2*k-2-2*j for j in range(t)}|{3+2*j for j in range(t,k-2)})
        a.append(A)
    return frozenset(a)
if __name__=='__main__':
 for k in range(2,16):
    F=2*k+1;g,B=brute(F);P=formula(k);print(k,F,g,len(B),len(P),B==P,flush=True)
    assert g==k+2 and B==P
 print('EXACT_MINIMUM_GENUS_OK')
