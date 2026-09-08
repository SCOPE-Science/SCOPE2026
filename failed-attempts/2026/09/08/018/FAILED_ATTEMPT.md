# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Stabilized trailing triple and gap criterion for Jones polynomials of alternating links under twist-region lengthening to 12 crossings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 83
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Knot Theory
- **Method:** skein-recurrence computation and diagrammatic induction

## Problem

For prime alternating links with crossing number <=12, tabulate normalized Jones trailing triples by twist-region structure and prove one closed-form stabilization fragment. Normalize V_L(t)=a0*t^min+a1*t^(min+1)+a2*t^(min+2)+...+an*t^max with a0!=0 (lowest-degree tail). For each reduced alternating diagram D with maximal twist-region decomposition, consider one-region full-twist extension families D_m obtained by inserting m>=0 full twists (pairs of half-twists preserving alternating type) into a distinguished maximal twist region, keeping total crossing <=12, and two-region families D_{p,q} extending two disjoint regions. Determine thresholds beyond which (a0,a1,a2) stabilize and give the closed form in the target claim, with every computed value independently recomputable from public PD/KnotInfo tables via a Kauffman-bracket script.

## Attempted claim

Let D_m be a one-region full-twist extension family as above with reduced checkerboard graphs. Then up to overall sign, a0=1 for all m, a1(m)=a1* is constant for m>=1 with a1*=-(k-1) where k>=1 is an explicit integer computed from the reduced checkerboard graph (number of twist-region equivalence classes incident to the extended region, minus isolated degeneracies), and a2(m)=a2* is constant for m>=2 with a2*=C(k,2)-s+delta where s is the explicit number of triangular faces / 2-paths joining neighboring regions in the reduced checkerboard graph and delta in {0,1} records whether the extended region abuts a length-1 region. For two-region families D_{p,q} with p,q>=2 the same holds jointly with a2* a quadratic polynomial in the two local k-values. The proof is by two-step Kauffman-bracket skein recurrence across the inserted full twist; the formula is verified on all such families with total crossing <=12, including classification of tail gaps a1*=0 or a2*=0.

## Research outcome

Proved (skein induction + machine-checked recurrence) one-region full-twist stabilization of Jones trailing triples with thresholds m1<=1, m2<=2 on alternating pretzel/torus families, and found+verified the exact count rule |a2|=#{length>=2 twist boxes} on 140/140 rows with full gap classification; general graph closed form left as conjecture.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Numerical fragment checks out on the supplied CSV, but the 'proved' claim overstates what is proved and reproducibility from supplied artifacts is incomplete. (1) Tangle decomposition <D_n>=A^n X+b_n Y with b_n=sum_{k<n}(-1)^k A^{n-2-4k} and one-step b_{n+1}=A^{n-1}-A^{-3}b_n is standard Temperley-Lieb calculus and algebraically correct. However the stated two-step form b_{n+2}=A^{n+1}-A^{n-4}+A^{-6}b_n has an exponent typo: direct expansion gives b_{n+2}=A^{n}-A^{n-4}+A^{-6}b_n (verified n=1..4; claimed A^{n+1} version is false). (2) Theorem A(iii) 'proved stabilization' is not a proof: the degree-gap argument depends on measured top-combs top(X)={(M,1),(M-8,2)}, top(Y)={(M-2,-1),(M-10,-1)} described as 'rigid (n-independent shape up to uniform shift)' and 'measured per family (exact, from aux state sums)'. No skein-theoretic derivation of that rigidity is given; it is an empirical observation on the pretzel subcensus plus verification. Proof and experiment are thus conflated. (3) Theorem B count rule |a2|=#{boxes length>=2} is explicitly empirical ('no proof in full generality is claimed'); on the supplied CSV it verifies exactly (122/122 P-knots + 18/18 integer-V P-links + 5/5 torus tails (1,0,1); span==c on all 122 knots; gaps exactly 5 torus a1=0 rows plus P(1,1,1) a2=0). Parity-subclass re-grouping confirms constancy except the n=1 seed anomaly, consistent with thresholds m1<=1,m2<=2. So the computation is internally consistent but Theorem B remains an unexplained enumeration, not a theorem. (4) Reproducibility gap: inputs/artifacts contains only recompute_jones.py (builders for torus + double-twist K(m,n) + E-closures), PROOF_LEDGER.md, and the CSV. It does NOT contain the 3-box-pretzel P(a,b,n) builders or output/work/final_census.py / checks.log cited as the reproduction route, so the 206-row pretzel census cannot be recomputed from the supplied verification-critical files. Anchors (trefoil V=t+t^3-t^4 up to mirror; Hopf/R1/delta checks) and span sanity pass, but full independent recomputation was not possible for the auditor. value: Even taking correctness at its best and novelty narrowly, the result as actually delivered is not independently worth finding later. What was promised (target claim): a proved graph-combinatorial closed form a2*=C(k,2)-s+delta with (k,s,delta) from reduced checkerboard graphs for all prime alternating links with c<=12, plus two-region bivariate form and gap criterion. What is delivered (DRAFT Sec.5 honesty section): torus + 3-box-pretzel subcensus only (206 rows, 145 integer-V), standard skein lemma, empirical count rule with values 0..3 (|a2| in {0,1,2,3}), and the general formula explicitly 'NOT proved... stated as a conjecture'. The remaining datum is: on this tiny series-parallel family |a0|=|a1|=1 (pretzels), torus tails (1,0,1), and |a2| counts long boxes; stabilization holds trivially after the shortest seed (n=1 anomaly only). No volume-ish bound improvement is derived, no thinness/cate…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Subcensus (torus + 3-box pretzels), NOT all prime alternating links <=12; the target's general C(k,2)-s+delta graph formula is downgraded to conjecture with supporting data; half-integer-V links recorded via f-heads only; signs reported raw (writhe-side dependent).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
