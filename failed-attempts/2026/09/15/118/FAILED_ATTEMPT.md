# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified geodesic growth rate of the compact tetrahedral Coxeter group [3,5,3]
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20340
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Geometric Group Theory
- **Method:** certified automatic-structure computation

## Problem

Let W_[3,5,3] = <s1,s2,s3,s4 | si^2=1, (s1 s2)^3=(s2 s3)^5=(s3 s4)^3=1, (s1 s3)^2=(s1 s4)^2=(s2 s4)^2=1> with standard generating set S={s1,s2,s3,s4} (the cocompact tetrahedral reflection group of minimal word growth in Isom H^3). Construct the Brink-Howlett geodesic automaton Geo(W,S), compute in certified exact integer arithmetic the rational geodesic growth series gamma(t)=N(t)/D(t) in Z(t), and certify that its geodesic growth rate gamma(W,S)=1/R, where R<1 is the smallest positive root of D, is a Perron number with an explicit rigorous isolating interval, and determine rigorously whether gamma(W,S) > omega(W,S) (the known word growth rate).

## Attempted claim

Let W_[3,5,3] = <s1,s2,s3,s4 | si^2=1, (s1 s2)^3=(s2 s3)^5=(s3 s4)^3=1, (s1 s3)^2=(s1 s4)^2=(s2 s4)^2=1> with standard generating set S={s1,s2,s3,s4} (the cocompact tetrahedral reflection group of minimal word growth in Isom H^3). Construct the Brink-Howlett geodesic automaton Geo(W,S), compute in certified exact integer arithmetic the rational geodesic growth series gamma(t)=N(t)/D(t) in Z(t), and certify that its geodesic growth rate gamma(W,S)=1/R, where R<1 is the smallest positive root of D, is a Perron number with an explicit rigorous isolating interval, and determine rigorously whether gamma(W,S) > omega(W,S) (the known word growth rate).

## Research outcome

Certified geodesic growth rate of the [3,5,3] Coxeter group: 687-state Brink-Howlett automaton, exact rational series with degree-148 denominator, growth rate 2.0312734181... (Perron) rigorously exceeding corrected word growth 1.350980337716237....

## Why this attempt failed

Failed axes: correctness.

correctness: Independently re-verified exactly: BM recurrence holds for all 750 equations n=151..900; automaton walk counts match counts900; 687 states/1560 transitions with no dangling edges; D(lo)>0 and D(hi)<0 exactly; N(R)!=0 exactly; gcd(D,N)=1; SCC decomposition is one 518-state block plus 169 transient singletons without self-loops with period gcd 1; Collatz-Wielandt bounds confirm spectral radius in [2.031273417,2.031273419]; Sturm certificate V0=6,Vlo=6,Vhi=5 and Steinberg factorisation with corrected q(t) confirm omega=1.350980337716237.... However the submitted smallest-root uniqueness certificate is invalid as documented: stated majorants M1=3.398/M2=3.127 are false (exact sup|D'| is ~18.03 on [0,1000/2048] and ~19.35 on [1000/2048,lo]), and the 131-cell part-2 cover fails exactly in its last three cells even under sharpest local Lipschitz bounds (at least ~133 cells needed). Hence 'unique smallest positive root R' is true numerically but unsupported by the submitted certificate; bounded evidence fix available.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The Brink-Howlett transition rule delta(D,s)={alpha_s} U s(D) cap Sigma is implemented as the standard construction and validated on A2 and I2(inf) controls, but its general correctness relative to the literature is assumed rather than re-proved here. The BM-discovered recurrence is certified as satisfied (750 exact equations) rather than proved minimal from first principles; rationality itself follows from the closed finite 687-state BFS. The Perron conclusion invokes the classical Frobenius t…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
