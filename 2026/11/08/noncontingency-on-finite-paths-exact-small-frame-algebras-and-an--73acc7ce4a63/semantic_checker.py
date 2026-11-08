"""Independent truth-vector checker of complete formula algebra over P4.
At depth k, generates every Boolean-valued truth vector on the computed
semantic atoms, applies the modal operation, then recomputes semantic atoms.
Not dependent on the recursive color definitions of refinement_checker.py.
"""
n=4
states=[(mask,r) for mask in range(1<<n) for r in range(n)]
N=len(states)
allbits=(1<<N)-1
pbits=sum(((mask>>r)&1)<<i for i,(mask,r) in enumerate(states))

def delta(f):
    z=0
    for i,(mask,r) in enumerate(states):
        left=(f>>(states.index((mask,r-1))))&1 if r else None
        right=(f>>(states.index((mask,r+1))))&1 if r<n-1 else None
        if left is None or right is None or left==right:
            z|=1<<i
    return z

def formula_vectors(parts):
    out=[]
    for subset in range(1<<len(parts)):
        v=0
        for i,a in enumerate(parts):
            if subset>>i&1:v|=a
        out.append(v)
    return out

def atom_partition(formulas):
    groups={tuple(f>>i&1 for f in formulas):0 for i in range(N)}
    for i in range(N):groups[tuple(f>>i&1 for f in formulas)]|=1<<i
    return sorted(groups.values())

parts=atom_partition([pbits]);counts=[len(parts)]
assert counts==[2]
for d in range(1,5):
    Fs=formula_vectors(parts)
    # Every depth-(d-1) formula is represented in Fs.
    modalities=[delta(f) for f in Fs]
    parts=atom_partition(Fs+modalities)
    counts.append(len(parts))
    print('depth',d,'formula vectors',len(Fs),'modal vectors',len(modalities),'types',len(parts))
assert counts==[2,4,12,14,14],counts
# The endpoints have no observational power except their own atom.
for mask in range(16):
    for r in (0,3):
        i=states.index((mask,r))
        j=states.index((1<<r,r)) if mask>>r&1 else states.index((0,r))
        assert all(bool(a>>i&1)==bool(a>>j&1) for a in parts)
print('SEMANTIC_OK')
