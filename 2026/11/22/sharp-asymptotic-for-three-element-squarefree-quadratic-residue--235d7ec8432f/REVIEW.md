# Independent mathematical audit

## correctness

PASS

The frozen exact theorem survives, but its displayed infinite-product decimal is wrong and its slogan dropped an essential restriction. A separate integer outward-rounded sieve gives the P=100000 truncated value in [0.07658973138093529,0.07658973138093530] and the P=200000 value in [0.07658953742116363,0.07658953742116364]. Every further factor is strictly below 1, already disproving the original decimal 0.0765897…. Bounding −log(1−t_p) by t_p/(1−t_p), with t_p≤6/p² and p>200000, and summing over odd integers gives the conservative enclosure 0.07658838<κ<0.07658954. Replay: branches/e6e90478-c9e9-4fb2-9a94-793d288e47db/constant_check.py and constant_check_results.txt. The repaired RESULT removes the false decimal and labels the recorded truncation explicitly; the repaired slogan restricts to {2,…,N}, since every set containing 1 is an automatic cover. Independently checked the residue criterion in this domain: over F₂, simultaneous nonresidue prescriptions correspond to a linear system with one row per prime-support vector and right side (1,1,1). Inconsistency requires an odd dependency, and no row is zero, so only the total product being square can obstruct it. For any consistent prescription, CRT and Dirichlet supply infinitely many primes with those symbols: work with p≡1 mod 4, prescribe odd-factor symbols via reciprocity and the residue class modulo each odd factor, and prescribe the symbol at 2 via p≡1 or 5 mod 8. For the converse, Legendre-symbol multiplication covers all odd primes not dividing the product, zero handles the others, and 2 is automatic. The gcd map is a bijection onto 1≤u<v<w, vw≤N, μ²(uvw)=1. Independently, integrating y over 0<y<1 gives volume 2/3 and the z>B cusp has volume 1/(2B); counting each integer vw slice bounds the lattice cusp by O(N^(3/2)/B). In the fixed box the local admissible patterns have density (1−1/p)^3(1+3/p), and their CRT density is valid at each finite cutoff by Jordan measurability. Either p² divides one coordinate or p divides two, with ≤(B√N)^3/p² points per pattern, so removing the prime cutoff at fixed B is justified before extending the box. These are analytic checks of the repaired theorem; the finite counts in check_results.txt were inspected as recorded diagnostics, not taken as infinite proof.

## originality

PASS

Credit the pre-existing residue criterion and standard pairwise-product coordinates. The surviving contribution is the explicit leading asymptotic, including the arithmetic density and unbounded height geometry, for all unordered squarefree triples in the specified box. The frozen checked references, fresh indexed comparison and independent statement-level analysis support that contribution without establishing historical priority.

## value

PASS

The sharp rate and constant quantify how rare the smallest nonsingleton odd-subproduct covers are inside the natural squarefree sampling space. The result contributes an actual distribution estimate beyond the qualitative criterion or existence thresholds; removing the cusp and prime tails is substantive and the height restriction is intrinsic to the counting question. The repaired summary makes the nontrivial exclusion of 1 explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
