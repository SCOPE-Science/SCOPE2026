"""Naive-basis DP counts (LOWER BOUNDS) for the normalized BP-cobar in fixed degree.
BP side: |t1|=2,|t2|=6,|t3|=14,|t4|=30 (|t5|=62 excluded, >38).
v side: |v2|=6,|v3|=14,|v4|=30. gens G = [0,2,4,6,6,8,10,12].
C^s_T = sum_g sum_vd Nv(vd)*Ntup[s][T-g-vd], Ntup ordered s-tuples nonempty t-mons.
Pure combinatorics (no eta_R). LOWER BOUNDS ONLY: the true normalized cobar
also admits mixed (v2,t1,t2) slot monomials via the left unit, which this
count excludes (found via a d^2=0 self-test failure of a fuller implementation).
Only the scale verdict (machine-scale, not hand work) is relied upon."""
TDEG = [2,6,14,30]; VDEG = [6,14,30]; GDEG = [0,2,4,6,6,8,10,12]
TMAX = 40

def part_counts(degs, tmax):
    """N[d] = # monomials (any, incl. empty) of degree d."""
    N = [0]*(tmax+1); N[0]=1
    for d in degs:
        for n in range(d, tmax+1):
            N[n]+=N[n-d]
    return N

def nonempty_t_counts(tmax):
    N = part_counts(TDEG, tmax)
    M = [0]*(tmax+1)
    for d in range(tmax+1):
        M[d]=N[d]-(1 if d==0 else 0)
    return M  # M[0]=0

def tup_counts(M, smax, tmax):
    """Nt[s][d]: ordered s-tuples of nonempty t-mons totaling d."""
    Nt=[[0]*(tmax+1) for _ in range(smax+1)]
    Nt[0][0]=1
    for s in range(1,smax+1):
        for d in range(tmax+1):
            Nt[s][d]=sum(M[k]*Nt[s-1][d-k] for k in range(2,d+1) if M[k])
    return Nt

if __name__=='__main__':
    M = nonempty_t_counts(TMAX)
    Nv_all = part_counts(VDEG, TMAX)
    Nt = tup_counts(M, 6, TMAX)
    print("nonempty t-monomial counts deg 0..16:", M[:17])
    for (s,T) in [(0,36),(1,36),(2,36),(3,36),(0,38),(1,38),(2,38),(3,38),(4,38),(5,38)]:
        tot=0
        for g in GDEG:
            for vd in range(T-g+1):
                td=T-g-vd
                tot+=Nv_all[vd]*Nt[s][td]
        print(f"C^{s} deg{T}: {tot}")
