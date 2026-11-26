# Independent mathematical audit

## correctness

PASS

The period is exact: M^8=I+4D, with D nonzero modulo two; squaring gives D_{s+1}=D_s+2^{s−2}D_s², so M^{2^{k+1}} is the identity modulo 2^k and M^{2^k} is not. The determinant of [v,Mv,M²v] is −1; any return of the state therefore forces a matrix return, and a scalar period returns all three entries of the state. For the nonsingular branches, D₃v≡(1,0,1) mod 2 and D₄v≡(1,2,3) mod 4 give the stated leading residues under eM^n. Factoring an odd power preserves them. Each even branch is an isometry after division by 4; the two branches in each of 0 and 1 modulo 4 therefore contribute two preimages. For r=1,3, split t into its two parities. Each normalized branch is an isometry after division by 16; t ranges modulo 2^{k−2}, so for each parity there are two lifts of each solution modulo 2^{k−4}. The r=1 targets are 1 mod 16 and the r=3 targets 2 mod 16. For r=5,7 the first five binomial coefficients and ν₂(c_j)≥2j−3 for j≥5 give an 8-divisible restricted remainder in the ordinary power basis (subtract at most ν₂(j!)≤j−1). H′/2 has odd affine coefficient and a 4-divisible integral Lipschitz perturbation, so it has a unique root. Taylor expansion there factors H−κ into (t−α)² times a unit U(t)≡1 mod 8, with ν₂(U(t)−U(w))≥3+ν₂(t−w). The unique square root B≡1 mod 4 satisfies ν₂(B(t)−B(w))≥2+ν₂(t−w) since B(t)+B(w) has valuation one. Thus (t−α)B(t) induces a bijective isometry at every finite level, and the square condition is modulo 2^{k−3}, leaving two lifts in the period. The root formula follows by separating the zero target, odd valuation, and even valuation 2h; odd squares have 1, 2, or 4 roots at the indicated levels, with the extra factor 2^h. In particular k=4 uses m=1 and the normalized r=1,3 modulus can be 1. Independent exact modular lifting and direct recurrence histograms verify both constants (1264 and 1791 modulo 2048) and all 32,752 targets at k=4,…,14. For the derivative calculation, a step h with high valuation gives (H(t+h)−H(t))/(2h)≡H′(t)/2 mod 2^{ν₂(h)−1}, by the restricted integral series; this explains the precision of the independent modular check. The bounded tests do not establish the infinite conjugacy or period.

## originality

PASS

The strongest prior record gives the full dyadic image, least period, and enough proof to recover the even-branch counts and the r=5 square-branch counts. The r=3 nonsingular contribution is also closely implied by its displayed valuation/lifting argument. These are not the supported distinct contribution. The r=7 branch was previously placed inside an already-covered ball; its new exact square-coordinate law and its contribution to the simultaneous all-target multiplicities are not supplied by that image proof or by the inspected zero-target and period literature.

## value

PASS

A full-period residue histogram for a natural linear recurrence resolves exact collisions and multiplicities, information the output image and zero valuations cannot supply. In particular the second singularity produces large fibers inside a ball already known to be covered; its geometry is invisible to a support-only law. The explicit square-root expression enables computation for any allowed target and level without enumerating a period.

The dated certificate retains the supplied scientific assessment, sources and limitations.
