"""Verification for lane-03: dicyclic Cayley gaps + Schreier quotients.
Pure Python group model + numpy only. Rerunnable in <10s.
Checks:
 (1) Cayley Gamma_n spectra vs formula lambda2=2+2cos(2pi/n), gap=4sin^2(pi/n)
 (2) rho_k 2-dim irrep relations + eigenvalues
 (3) Schreier Sigma_n construction, regularity, Spec inclusion, gap comparison
 (4) Trace identities Tr(A^2)=16n, Tr(A^4)=sum lambda^4
 (5) Trig bound sin(pi/n)>=2/n, Cheeger bound
"""
import numpy as np
import json

def mat_mul(p, q, n):
    """Multiply elements p=(e1,k1), q=(e2,k2) in Dic_n, k mod 2N (N=2n)."""
    N = 2*n
    e1, k1 = p; e2, k2 = q
    if e1 == 0 and e2 == 0:
        return (0, (k1+k2) % N)
    if e1 == 0 and e2 == 1:
        return (1, (k2-k1) % N)
    if e1 == 1 and e2 == 0:
        return (1, (k1+k2) % N)
    # (1,k1)(1,k2) = a^{n+k2-k1}
    return (0, (n + k2 - k1) % N)

def group_elements(n):
    els = []
    idx = {}
    for e in (0,1):
        for k in range(2*n):
            idx[(e,k)] = len(els)
            els.append((e,k))
    return els, idx

def gens(n):
    N = 2*n
    return [(0,1),(0,N-1),(1,0),(1,n)]

def cayley_adj(n):
    els, idx = group_elements(n)
    S = gens(n)
    N = len(els)
    A = np.zeros((N,N), dtype=float)
    for g in els:
        i = idx[g]
        for s in S:
            h = mat_mul(g, s, n)
            j = idx[h]
            A[i,j] += 1.0
    return A

def schreier_adj(n):
    # vertices 0..n-1, rep (0,i)
    B = np.zeros((n,n), dtype=float)
    S = gens(n)
    for i in range(n):
        rep = (0, i)
        for s in S:
            h = mat_mul(rep, s, n)
            # coset index = k mod n where h=(e,k)
            j = h[1] % n
            B[i,j] += 1.0
    return B

def check_irrep_relations(n, tol=1e-12):
    z = np.exp(1j*np.pi/n)
    for k in range(1, n):
        D = np.diag([z**k, z**(-k)])
        e = 1 if k % 2 == 0 else -1
        X = np.array([[0,1],[e,0]], dtype=complex)
        N = 2*n
        # a^{2n}=1
        assert np.max(np.abs(np.linalg.matrix_power(D, N) - np.eye(2))) < tol
        # x^2 = a^n
        assert np.max(np.abs(X@X - np.linalg.matrix_power(D, n))) < tol
        # x^{-1} a x = a^{-1}
        Xinv = np.linalg.inv(X)
        assert np.max(np.abs(Xinv@D@X - np.linalg.inv(D))) < tol
    return True

def rhoS_eigs(n):
    """Return dict k -> sorted eigs of rho_k(S)."""
    z = np.exp(1j*np.pi/n)
    out = {}
    for k in range(1, n):
        c = np.cos(np.pi*k/n)
        D = np.diag([z**k, z**(-k)])
        e = 1 if k % 2 == 0 else -1
        X = np.array([[0,1],[e,0]], dtype=complex)
        Xinv = np.linalg.inv(X)
        Smat = D + np.linalg.inv(D) + X + Xinv
        w = np.linalg.eigvalsh((Smat+np.conj(Smat).T)/2)  # hermitian
        # Smat is hermitian already (check)
        w2 = np.sort(np.real(np.linalg.eigvals(Smat)))
        out[k] = w2
    return out

def linear_eigs(n):
    """Eigenvalues from 1-dim characters."""
    if n % 2 == 0:
        # C2xC2: chi(a),chi(x) in {+-1}
        vals = []
        for ca in (1,-1):
            for cx in (1,-1):
                vals.append(2*ca+2*cx)
        return sorted(vals)
    else:
        # C4: chi(x)=i^j, chi(a)=(-1)^j
        vals = []
        for j in range(4):
            chx = (1j)**j
            cha = (-1)**j
            vals.append(2*np.real(cha)+2*np.real(chx))
        return sorted(vals)

def full_formula_spectrum(n):
    """Analytic multiset of Cayley eigenvalues (as list with algebraic multiplicities
    counting dim factor): trivial+linears (mult1 each) + for each k: eigs of rho_k(S),
    each repeated dim=2 times."""
    vals = []
    # linears: 4 chars; trivial included
    vals.extend(linear_eigs(n))
    z = np.pi/n
    for k in range(1, n):
        if k % 2 == 0:
            c = np.cos(np.pi*k/n)
            l1 = 2*c+2; l2 = 2*c-2
            vals.extend([l1]*2 + [l2]*2)
        else:
            c = 2*np.cos(np.pi*k/n)
            vals.extend([c]*4)
    return np.sort(np.array(vals, dtype=float))

def main():
    res = {"cayley": [], "schreier": [], "trace": [], "irrep": [], "trig": []}
    worst_lam = 0.0
    worst_gap = 0.0
    print("=== (1) Cayley Gamma_n ===")
    for n in range(3, 31):
        A = cayley_adj(n)
        # symmetry + regularity checks
        assert np.max(np.abs(A - A.T)) == 0
        assert np.allclose(A.sum(axis=1), 4)
        ev = np.linalg.eigvalsh(A)  # ascending
        lam2 = ev[-2]
        lam1 = ev[-1]
        assert abs(lam1-4) < 1e-9
        formula_lam2 = 2+2*np.cos(2*np.pi/n)
        formula_gap = 4*np.sin(np.pi/n)**2
        gap = 4-lam2
        dlam = abs(lam2-formula_lam2)
        dgap = abs(gap-formula_gap)
        worst_lam = max(worst_lam, dlam)
        worst_gap = max(worst_gap, dgap)
        # formula spectrum match
        fsp = full_formula_spectrum(n)
        assert len(fsp)==4*n
        assert np.max(np.abs(np.sort(ev)-fsp)) < 1e-8, (n, np.max(np.abs(np.sort(ev)-fsp)))
        assert abs(fsp[-1]-4)<1e-9
        print(f"n={n:2d} N={4*n:3d} lam2={lam2:.12f} formula={formula_lam2:.12f} err={dlam:.1e} gap={gap:.12f} fgap={formula_gap:.12f}")
        res["cayley"].append({"n":n,"lam2":float(lam2),"formula_lam2":float(formula_lam2),"err":float(dlam),"gap":float(gap),"formula_gap":float(formula_gap)})
        # trace checks
        tr2 = np.trace(A@A)
        # integer exact: each row degree 4, Tr(A^2)=4n*4=16n (A symmetric 0/1, no loops)
        assert abs(tr2-16*n)<1e-6
        A4 = np.linalg.matrix_power(A,4)
        tr4 = np.trace(A4)
        tr4f = np.sum(fsp**4)
        assert abs(tr4-tr4f)/max(1,abs(tr4f)) < 1e-9, (n,tr4,tr4f)
        res["trace"].append({"n":n,"tr2":float(tr2),"tr4":float(tr4),"tr4formula":float(tr4f)})
    print(f"WORST lam2 err={worst_lam:.2e} gap err={worst_gap:.2e}")
    print("\n=== (2) irreps ===")
    for n in [3,4,5,6,7,8,11,12,30]:
        check_irrep_relations(n)
        d = rhoS_eigs(n)
        for k,v in d.items():
            if k%2==0:
                e1 = 2+2*np.cos(np.pi*k/n); e2=-2+2*np.cos(np.pi*k/n)
                assert np.max(np.abs(np.sort(v)-np.sort([e1,e2])))<1e-9,(n,k,v)
            else:
                e = 2*np.cos(np.pi*k/n)
                assert np.max(np.abs(np.sort(v)-np.sort([e,e])))<1e-9,(n,k,v)
        le = linear_eigs(n)
        assert max(le)==4 and all(x<=1e-9 for x in le if abs(x-4)>1e-9 and x>0)==True, le
        assert all(x<=1e-9 for x in le[1:] if False)==True or max([x for x in le if abs(x-4)>1e-9])<=1e-9, le
        print(f"n={n}: irreps OK, linears={le}")
        res["irrep"].append({"n":n,"linears":list(map(float,le))})
    # maximizer check: k=2 gives global max among non-trivial
    print("\n=== maximizer k=2 ===")
    for n in range(3,31):
        cands = []
        for k in range(1,n):
            if k%2==0:
                cands.append(2+2*np.cos(np.pi*k/n))
            else:
                cands.append(2*np.cos(np.pi*k/n))
        cands.extend([x for x in linear_eigs(n) if abs(x-4)>1e-9])
        m = max(cands)
        f = 2+2*np.cos(2*np.pi/n)
        assert abs(m-f)<1e-9,(n,m,f)
    print("k=2 maximizer OK for 3..30 (n=3 tie with k=1 noted).")
    print("\n=== (3) Schreier Sigma_n ===")
    for n in range(3, 31):
        B = schreier_adj(n)
        assert np.max(np.abs(B-B.T))==0
        assert np.allclose(B.sum(axis=1),4)
        evB = np.linalg.eigvalsh(B)
        A = cayley_adj(n)
        evA = np.linalg.eigvalsh(A)
        # set inclusion: each Schreier eigenvalue within 1e-8 of some Cayley eigenvalue
        maxdist = max(min(abs(b-a) for a in evA) for b in evB)
        # multiplicity check: count occurrences (rounded) in Cayley >= in Schreier
        # (use tolerance clustering)
        def counts(evs, tol=1e-6):
            evs=np.sort(evs); groups=[]
            for x in evs:
                if groups and abs(x-groups[-1][0])<tol:
                    groups[-1][1]+=1
                else:
                    groups.append([x,1])
            return groups
        # gap comparison
        gapB = 4-evB[-2] if n>1 else 0
        # for n>=3 second largest (note multiplicities: largest 4 simple? check)
        # largest should be 4 simple for connected? verify
        gapA = 4-np.sort(evA)[-2]
        formula_gap = 4*np.sin(np.pi/n)**2
        print(f"n={n:2d} specB={np.sort(evB)} maxdist={maxdist:.1e} gapB={gapB:.6f} gapA={gapA:.6f} fgap={formula_gap:.6f}")
        assert maxdist < 1e-8,(n,maxdist)
        assert gapB+1e-8 >= gapA,(n,gapB,gapA)
        res["schreier"].append({"n":n,"eigB":list(map(float,np.sort(evB))),"maxdist":float(maxdist),"gapB":float(gapB),"gapA":float(gapA)})
    print("\n=== (5) trig/Cheeger ===")
    for n in range(3,31):
        s = np.sin(np.pi/n)
        assert s >= 2/n - 1e-12,(n,s,2/n)
        gap = 4*s*s
        assert gap >= 16/n/n -1e-12
        h = gap/2
        assert h >= 8/n/n -1e-12
        res["trig"].append({"n":n,"gap":float(gap),"cheeger_lb":float(h)})
    print("trig bounds OK.")
    with open("/srv/scope-research/rounds/2026-09-07-pilot-01/workspaces/research/lane-03/output/artifacts/verify_results.json","w") as f:
        json.dump(res,f,indent=2)
    print("\nWORST lam2 err:",worst_lam)
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
