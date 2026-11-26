# Independent mathematical audit

## correctness

PASS

In a primitive rank-one factorization A=cuvᵀ, use the primitive generator u of the rational image line and divide the coordinate row by its content c. Then AXA=c(vᵀXu)A, so AXA=A forces c=1; conversely primitivity of u and v allows Xu=w with vᵀw=1. A unimodular basis with first vector u gives B(t,b) with primitive row. Any intertwinor preserves its primitive image line, so its form [ε,m;0,δ] gives b′=εtm+εδb, both necessary and sufficient; t=0 gives b=±1 and one class. Independently, a nonzero nilpotent N has the form ℓ(r,s)ᵀ(−s,r) with gcd(r,s)=1 and ℓ integral. Then det(B−N)=−ℓs(tr+bs); unimodularity is possible exactly for b≡±1 mod |t|, or |b|=1 at t=0. N=0 cannot work since B is singular. Thus the criterion does select one orbit, including moduli 1 and 2. For n>2 the sign action on units has no fixed points. Totient multiplicativity and the prime-power formula give φ(n)≤2 precisely at n=1,2,3,4,6; along primes p≥5 the proportion is 2/(p−1). I inspected the frozen code and its recorded CHECK_OK: it only tests the conjugation formula on a finite box and sign orbits through modulus 100, not fineness or unbounded statements.

## originality

FAIL

The 2006 integral-similarity classification already gives the bare residue/sign classes (including the repeated-root classification at trace zero). The 2016 fine-ring paper already determines fineness on every triangular representative, and its Example 5.6 already exhibits the exact trace-five matrix. Imposing content one and counting the sign-orbits, of which exactly the distinguished orbit meets the fine congruence, is a direct conjunction of these results; no remaining new stratum computation is needed.

## value

FAIL

The regular-fine question motivates the stratum, but the claimed refinement only filters an earlier canonical table by coprimality and selects the already known fine parameter. The totient counts and limiting proportion are immediate; no new classification step or independently useful noncovered invariant is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
