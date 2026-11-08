"""Finite flat strict-implication sharpness: two independent tests."""
from itertools import product
import random

def preorder(n,bits):
    le = [[(bits>>(i*n+j))&1 for j in range(n)] for i in range(n)]
    return all(le[i][i] for i in range(n)) and all(not (le[i][j] and le[j][k]) or le[i][k] for i in range(n) for j in range(n) for k in range(n))

def upsets(le):
    n=len(le); allup=[]
    for mask in range(1<<n):
        if all(not ((mask>>i)&1) or not le[i][j] or ((mask>>j)&1) for i in range(n) for j in range(n)):
            allup.append(mask)
    return allup

def up_rows(le,rbits):
    n=len(le);rows=[]
    for i in range(n):
        row=0
        for j in range(n):
            if (rbits>>(i*n+j))&1:
                for k in range(n):
                    if le[j][k]:row |= 1<<k
        rows.append(row)
    return rows

def criterion(le,rows):
    n=len(le)
    prin={sum((1<<j) for j in range(n) if le[i][j]) for i in range(n)}
    for w in range(n):
        futures=[rows[x] for x in range(n) if le[w][x]]
        for t in range(n):
            contain=[r for r in futures if (r>>t)&1]
            minimal=[r for r in contain if not any((s != r) and ((s|r)==r) for s in contain)]
            if any(r not in prin for r in minimal):return False
    return True

def semantically_valid(le,rows,ups):
    n=len(le)
    # For each w, A, B, C, look directly at the two strict arrows
    for w in range(n):
        futures=[rows[x] for x in range(n) if le[w][x]]
        for a in ups:
            for b in ups:
                union=a|b
                for c in ups:
                    pa=all((r&a)!=r or (r&c)==r for r in futures)
                    pb=all((r&b)!=r or (r&c)==r for r in futures)
                    if pa and pb:
                        pc=all((r&union)!=r or (r&c)==r for r in futures)
                        if not pc:return False
    return True

def run():
    total=0; sharp=0; byn={}
    for n in range(1,4):
        preorders=[[[bool((p>>(i*n+j))&1) for j in range(n)] for i in range(n)] for p in range(1<<(n*n)) if preorder(n,p)]
        count=0;countgood=0
        for le in preorders:
            us=upsets(le)
            for rb in range(1<<(n*n)):
                rows=up_rows(le,rb)
                new=criterion(le,rows)
                old=semantically_valid(le,rows,us)
                if old != new:
                    raise AssertionError((n,le,rb,rows,old,new))
                count += 1;countgood += int(old)
        byn[n]=(len(preorders),count,countgood)
        total+=count;sharp+=countgood
    # Four-world random preorders and raw modal relations; independent direct truth-table comparison.
    rng=random.Random(260328402)
    for _ in range(600):
        while True:
            n=4;p=rng.randrange(1<<(n*n))
            if preorder(n,p):break
        le=[[bool((p>>(i*n+j))&1) for j in range(n)] for i in range(n)]
        rows=up_rows(le,rng.randrange(1<<(n*n)))
        assert criterion(le,rows)==semantically_valid(le,rows,upsets(le))
    # Poset 0<=1, 0<=2, R[0]={1,2}, R[1]={1}, R[2]={2}, not rowwise directed.
    le=[[1,1,1],[0,1,0],[0,0,1]]
    rows=[0b110,0b010,0b100]
    assert criterion(le,rows) and semantically_valid(le,rows,upsets(le))
    assert not any(le[k][1] and le[k][2] and ((rows[0]>>k)&1) for k in range(3))
    # Same poset with R[1]=R[2]=empty refutes sharpness and gives a decisive countervaluation.
    assert not criterion(le,[0b110,0,0])
    print('FINITE_FLAT_DI_PRINCIPAL_REFINEMENT_OK',byn,'total_frames',total,'valid',sharp,'four_world_random',600)
if __name__=='__main__':run()
