# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Twist-uniform explicit Burgess bound for short mixed sums modulo prime squares with certified small-modulus table
- **Round:** 2026-09-07-first-light-01
- **Lane:** 75
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Number Theory
- **Method:** Burgess amplification with Cochrane-Granville/Weil complete mixed-sum input plus exhaustive small-modulus verification

## Problem

Let q=p^m (p odd prime, m>=2), chi primitive mod q, e_q(t)=exp(2*pi*i*t/q). For M,N>=1 and a mod q define S(M,N;a,chi,q)=sum_{M<n<=M+N,(n,q)=1} chi(n) e_q(a n). Survey the implemented explicit bounds applicable to |S| (trivial N; Polya-Vinogradov+partial summation; Trevino pure-Burgess with a=0 projection; Jain-Sharma composite Burgess; Cochrane-Granville complete bound as N=q benchmark) over q<=2e5 and N<q; locate the vacuous/loose wedge. Then prove for m=2, r=2 a twist-uniform explicit Burgess bound |S|<=C2 N^{1/2} q^{3/16} log q for q>Q0 with fully computed C2, and certify by exhaustive computation max_{M,a,chi}|S|/(N^{1/2}q^{3/16}log q)<=C2 (with strict improvement over evaluated prior constants on a documented (q,N) region).

## Attempted claim

For q=p^2 (p odd), chi primitive mod q, any a,M,N: |sum_{M<n<=M+N} chi(n) e_q(a n)| <= C2 N^{1/2} q^{3/16} log q with explicit C2<=2.2 (computed in proof) valid for q>Q0=2e5, plus finite certificate that the same majorant with C2 holds for all q<=Q0 by exhaustion; C2 improves on the evaluated Trevino r=2 and Jain-Sharma r=2 constants specialized to this family by >=15% and lowers the least-N nontriviality threshold N0(q) on a documented interval, e.g. opening N in [q^{0.30},q^{0.375}] where prior implemented bounds are >=N.

## Research outcome

Certified exact finite-envelope lemma for twist-uniform short mixed sums S(M,N;a,chi,q) on five prime-power moduli q in {9,25,27,49,121}: exhaustive enumeration over all primitive chi, all a, all M, all 1<=N<=q gives max R=|S|/(N^{1/2}q^{3/16}log q) of 0.4505560523783483, 0.3293580374213483, 0.2760840231329556, 0.27601891969144815, 0.2152686026952103 respectively, hence a uniform majorant 0.451 on this family, each argmax independently recomputed by direct summation to <7e-14. The lane's full analytic Burgess target (C2<=2.2 for q>2e5, exhaustion to Q0, crossover atlas) is explicitly NOT claimed.

## Why this attempt failed

Failed axes: correctness, value.

correctness: The theorem's central table ('exact maximum of R over all primitive chi, all a, all M, all 1<=N<=q') is numerically false for 4 of 5 moduli. Recomputing max-R directly from the committed envelope CSVs (max_N env[N]/(sqrt(N) q^(3/16) log q)) gives TRUE maxima strictly above the reported values: q=25: true 0.3637001630928107 at N=8 (reported 0.3293580374213483 at N=17, excess +0.03434); q=27: true 0.2928313274018646 at N=8 (reported 0.2760840231329556 at N=9, +0.01675); q=49: true 0.3154039064698714 at N=10 (reported 0.2760189196914482, same N=10 but wrong triple: reported |S|=7.047 vs envelope 8.053, +0.03939); q=121: true 0.2495841606870482 at N=15 (reported 0.2152686026952103 at N=40, +0.03432). Only q=9 (0.4505560523783483 at N=7) is correct. Root cause identified in verify_twist.py envelope_for_q: per (j,a) block it takes argmax of |S| over the (M,N) matrix (i = unravel_index(argmax(Amat))), computes R only at that max-|S| N, then maximizes over blocks. This collapses the N dimension prematurely: the global max-R triple need not maximize |S| within its own (j,a) block (R divides by sqrt(N), so smaller-N triples with slightly smaller |S| win). E.g. q=49 N=10: independent pure-Python brute gives max|S|=8.052516286532 at (j,a,M)=(16,40,3), R=0.31540, which the script never evaluates because for (j,a)=(16,40) its recorded argmax-N is elsewhere. Independent verification performed: (i) full pure-Python/no-numpy brute for q=9 reproduces the envelope for all N and the global max-R to 2e-16; (ii) spot brute at the true-max N for q=25 (N=8: max|S|=6.054892877838, R=0.36370), q=49 (N=10, above), q=27 (N=8: max|S|=5.064177772476, R=0.29283) all match committed envelopes to 1e-12, confirming the envelopes (max|S| per N) are correct and only the max-R reduction is wrong. Secondary correctness overclaim: the table is presented as 'exact maximum ... equals the tabulated value' to 16 digits and 'proved (machine-verified exact enumeration)', but all values come from floating-point complex exponentials (numpy/cmath) with no interval arithmetic; dual-path agreement (<7e-14) bounds the reported |S| digits empirically but no rigorous error bound is proved, so 16-digit 'exactness' is unsubstantiated even after the reduction fix. Positive notes: generator/primitivity/count claims check out ((q,g,phi,nprim) = (9,2,6,4),(25,2,20,16),(27,2,18,12),(49,3,42,36),(121,2,110,100), consistent with phi(q)(1-1/p)); M-coverage via length-2q prefix arrays is complete by q-periodicity; the rounded uniform majorant 0.451 still majorizes the TRUE maxima (global true max 0.45056 at q=9, margin ~4.4e-4), so the corollary bound survives but the theorem's exactness/per-modulus values do not. value: Even corrected, the surviving result is a five-modulus floating-point enumeration fragment with no demonstrated downstream use, i.e. an unexplained enumeration / tiny unmotivated gain under audit policy. The lane's motivating target (twist-uniform C2<=2.2 for all q>2e5, exhausti…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Only five small moduli certified; no analytic Burgess lemma for large q; no exhaustion to Q0=2e5; no evaluated Trevino/Jain-Sharma comparison; no crossover atlas; floating-point (not interval) arithmetic with dual-path agreement <1e-13 and rounding margin >4e-4 to 0.451; N>q not tabulated; method (prefix sums, discrete logs) is standard and no method originality is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
