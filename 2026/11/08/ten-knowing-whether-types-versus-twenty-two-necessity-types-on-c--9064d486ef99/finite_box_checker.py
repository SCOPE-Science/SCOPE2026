"""Direct finite-model census of one-atom ordinary-box modal language on K_{a,b}."""

def enumerate_types(a,b):
    n=a+b
    E=[tuple(range(a,n)) if w<a else tuple(range(a)) for w in range(n)]
    seen=[set(),set(),set()]
    for val in range(1<<n):
        p=[(val>>w)&1 for w in range(n)]
        box=lambda q:[int(all(q[j] for j in E[w])) for w in range(n)]
        B=box(p)
        notp=[1-x for x in p]
        C=box(notp)
        BB=box(B)
        BC=box(C)
        for w in range(n):
            seen[0].add((p[w],))
            seen[1].add((p[w],B[w],C[w]))
            seen[2].add((p[w],B[w],C[w],BB[w],BC[w]))
    return [2**len(x) for x in seen], [len(x) for x in seen]

for a,b,profile in [
 (1,1,[4,16,16]),
 (1,2,[4,64,1024]),
 (1,4,[4,64,1024]),
 (2,2,[4,64,4096]),
 (2,3,[4,64,4096]),
 (3,3,[4,64,4096])
]:
    p,k=enumerate_types(a,b)
    assert p==profile,(a,b,p,profile)
    print(f'K_{{{a},{b}}}: box-modal depth 0,1,2 meanings {p}, pointed types {k}')
print('PASS: ordinary modal separation and sharp comparative counts')
