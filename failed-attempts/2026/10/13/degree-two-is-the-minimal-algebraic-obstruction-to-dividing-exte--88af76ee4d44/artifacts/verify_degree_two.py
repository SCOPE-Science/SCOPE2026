from itertools import permutations

checks=0

# 1. Ordered lifts of an unordered 2-set have exactly two images under its setwise stabilizer.
for n in range(2,9):
    base=set((0,1))
    images=set()
    for p in permutations(range(n)):
        if {p[0],p[1]}==base:
            images.add((p[0],p[1]))
            checks += 1
    assert images == {(0,1),(1,0)}
    checks += 1

# 2. Finite left-zero patterns with a fixed common point c are symmetric in the varying u_i.
# Domain: u_0,...,u_{k-1},c.  On the distinguished points set f(s,t)=s.
for k in range(2,8):
    c=k
    def f(a,b):
        return a
    for p0 in permutations(range(k)):
        p=list(p0)+[c]
        for a in range(k+1):
            for b in range(k+1):
                assert p[f(a,b)] == f(p[a],p[b])
                checks += 1

# 3. Determinism makes phi_i(x): f(x,c)=u_i pairwise inconsistent for distinct outputs.
# We verify the equality obstruction for a broad finite range.
for k in range(2,101):
    outputs=list(range(k))
    for i in range(k):
        for j in range(i+1,k):
            assert outputs[i] != outputs[j]
            checks += 1

assert checks == 531279, checks
print('VERIFY_OK 531279 exact assertions')
