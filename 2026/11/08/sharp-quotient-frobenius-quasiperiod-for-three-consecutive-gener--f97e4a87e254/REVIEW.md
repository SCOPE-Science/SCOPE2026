# Independent mathematical audit

## correctness

PASS

For N=qa+r with 0≤r<a, q generators realize precisely the offsets 0,…,2q. When r>2q, (q−1)(a+2)<qa, and q+1 generators exceed N. This gives exactly the stated intervals. Their top index at a=2t+ε is t−1. At index t−1−j the right endpoint H=(t−j)a−1 is ε+2j above the left one, and H−(H mod p) lies in the interval iff its remainder passes the stated inequality. At j_max the width is at least p−1 and a≥2p+4 ensures t−1−j_max≥0. Disjoint ordered intervals then prove the formula and the branch period 2p. For any eventual period T, CRT and equality of polynomials on infinite progressions force the signature (B,R) to be invariant under gcd(T,2p). For p=2k+1, the signature (p−1,p−1) forces ε=0,J=k; R_(k−1)>p−3 and R_(k−1)≡R_k+a (mod p) force residues 0 and p−1 modulo 2p, both attained. This pair cannot be exchanged by a cyclic translation. For p=2k the signature (p,p−1) occurs precisely at 0,p by the same preceding-remainder test, so only p could remain as a smaller period. At 1 and p+1 the bounds on j become 3j≥2k−2 and 3j≥k−2 respectively before remainder wraparound, giving unequal minimal indices for k≥2. At p=2 the two indices are zero but the remainders differ (1 and 0). Thus no smaller eventual period exists. Independent replay /workspace/quotient_replay.py finds minimal attainable residues by shortest paths and checks 9,936 exact Frobenius evaluations, with fitted branch signatures checked against all shifts for p=2,…,70. This is finite corroboration, not evidence by extrapolation. Frozen scripts and logs were inspected, not executed.

## originality

PASS

Pass for the unrestricted three-generator quotient branch theorem and in particular the noncollapse to any eventual period smaller than 2p. The exact interval decomposition is shared with the same-day genus article, and the highest nonempty interval formula is immediate from that decomposition; neither is credited as independent novelty on its own. The least Frobenius period is not an implication of the genus period or of the earlier divisor-restricted Frobenius formulas.

## value

PASS

The Frobenius number is a canonical quotient invariant. A uniform least-period theorem determines which residue information cannot be discarded even for arbitrarily large a. In particular the smallest p has a genuine distinction from the closely related genus behaviour. This is stronger than computing examples or proving the existence of an unspecified eventual period, and does not purport to optimize the stabilization cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
