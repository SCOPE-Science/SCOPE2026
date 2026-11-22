"""Finite exact-factor check for the cyclic repeated-letter substitution.

For a fixed alphabet and repetition, this reconstructs the complete set of
length-three source factors by substitution closure. Every factor shorter
than two second-level block lengths is contained in the second substitution
image of a length-three source factor. The independent mathematical proof
establishes the all-parameter statement; this is a bounded cross-check.
"""

def sigma(word, q, r):
    return tuple(v for a in word for v in ((a,) * r + ((a + 1) % q,)))


def triples(q, r):
    word = (0,)
    for _ in range(q + 2):
        word = sigma(word, q, r)
        if len(word) >= 3:
            break
    seen = {tuple(word[i:i+3]) for i in range(len(word)-2)}
    for step in range(200):
        nxt = set(seen)
        for t in seen:
            s = sigma(t, q, r)
            nxt.update(tuple(s[i:i+3]) for i in range(len(s)-2))
        if nxt == seen:
            return seen,step
        seen = nxt
    raise RuntimeError('triple closure did not stabilize')


def factors_at_lengths(q,r,n_values):
    ts,steps = triples(q,r)
    sizes = {n:set() for n in n_values}
    for tr in ts:
        z = sigma(sigma(tr,q,r),q,r)
        for n in n_values:
            sizes[n].update(z[i:i+n] for i in range(len(z)-n+1))
    return sizes, len(ts), steps

checks=0
for q in range(3,10):
    for r in range(2,9):
        B=r+1; L=B*(B+1)
        F,count,steps=factors_at_lengths(q,r,(r+1,r+2,L-1,L,L+1))
        for n in F:
            two={x for x in F[n] if len(set(x))<=2}
            if n==r+1:
                assert len([x for x in F[n] if len(set(x))==1])==q
            if n==r+2:
                assert len([x for x in F[n] if len(set(x))==1])==0
                assert two
            if n==L:
                expected={ (a,)+sigma((a,)*(r+1),q,r)+((a+1)%q,)*r for a in range(q)}
                assert two == expected,(q,r,len(two),len(expected))
            if n==L+1:
                assert not two,(q,r,n,len(two))
            checks += 1
        print(f'q={q} r={r} triples={count} closure_steps={steps} length={L} maximal_binary={len([x for x in F[L] if len(set(x))<=2])}')
print(f'PASS: {checks} exact length checks across 49 parameter pairs')
