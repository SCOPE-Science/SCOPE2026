# Independent mathematical audit

## correctness

PASS

Inspected RESULT.md and CHECK.py; reconstructed the 2m-cycle hat Gram matrix G_jj=(a+b)/3 and G_j,j+1=h_j/6, its sign-gauged positive inverse, and the recurrence H u_k-ab(u_(k-1)+u_(k+1))=12(a+b)delta_k0. The unique cyclic Green row U_k=(12s/Delta)(q^k+q^(m-k))/(1-q^m), V_k=(aU_k+bU_(k+1))/(2s) is the periodization of the decaying recurrence with q=(H-Delta)/(2ab). Exact absolute integral of a signed linear segment equals h(u²+v²)/(2(u+v)), giving the asserted finite formula. Strict convexity/strict triangle inequality excludes interior evaluation points because adjacent kernel rows cross signs; reproduction of 1 yields defect -(Lambda_m-1)/2. Independent exact rational Gram inversions and norm sums agreed for m=2,3,4,5,6 and a:b=1:1,1:2,2:5,7:3 (20 cases); the limit follows from geometric tail bounds and reduces to 2-(a-b)²/((3a+b)(a+3b)). Tests support, but do not replace, the cyclic recurrence proof.

## originality

PASS

The rational infinite-line norm 2-(a-b)²/((3a+b)(a+3b)), the sharp bound over all finite periodic repeats, their strict finite inequality and limit were ALREADY proved in October 18 and October 26, with another exact November 2 published theorem. None of the complete published sources supplies the exact L-infinity value at every fixed finite m for arbitrary a,b, its explicit periodized two-cell Green-sum formula or the all-and-only norming-knot classification. The accepted surviving contribution is strictly the natural full finite-cycle exact sequence and exact extremizers, NOT the covered limiting contrast law or basic positivity identity. Periodization is standard but evaluating the signed absolute cyclic kernel is nontrivial. Best-of-knowledge qualification remains.

## value

PASS

A fixed finite periodic mesh is a natural projection object; its exact sharp amplification, norming sites and worst negativity are not determined by the previously known optimal uniform-in-repeat bound. The all-m formula supplies any desired finite mesh stability constant rather than merely the asymptotic envelope, a meaningful independently usable exact invariant. The limiting contrast effect is already known and is NOT used to inflate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
