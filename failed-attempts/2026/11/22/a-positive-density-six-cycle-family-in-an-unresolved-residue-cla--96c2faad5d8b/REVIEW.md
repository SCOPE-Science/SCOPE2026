# Independent mathematical audit

## correctness

PASS

The exact identity g³−X=−X²P and P(0)=3 give least period three at every root for p>3 (only 1 and 3 can divide its return time, and the sole fixed point is zero). The supplied second-iterate identity and resultant 1 are also correct. Starting at (−1,y), even iterates follow g and odd iterates have first coordinate g^j(y)−1, never −1 since the g-cycle is nonzero. Each three-root block thus gives one distinct primitive six-cycle. Over Q the squarefree sextic has two such blocks, and the Galois group centralizes their rotations. Irreducibility mod 5 and the distinct 1+1+1+3 factorization mod 11 yield a 6-cycle that swaps the blocks and a one-block rotation; conjugating by the swap generates the other rotation, giving the full order-18 wreath group. Its only quadratic subfield is the discriminant field Q(√−2), contained in Q(ζ_8) and hence in Q(ζ_24). The intersection has degree dividing gcd(18,8)=2, so the compositum has degree 72. Frobenius at 19 mod 24 is trivial on Q(√−2); among the nine rotations in its fiber, both blocks move for four elements, exactly one moves for four, and neither moves for one. Those are conjugacy-invariant sets in the fiber, so Chebotarev gives the stated densities, and functional-graph components each contain one cycle. A six-cycle is additional to the p fixed-point components. Independent exact polynomial, factorization and example-orbit checks agree; replay: python3 /workspace/branches/2043cce8-62ac-4764-958c-f39997638274/ordinal3_arithmetic_check.py. The uploaded checker was inspected, not executed. This is a proof of the witness density and finite certificates only, not a count of every six-cycle, a solution for the whole residue class, or a finite-sample inference.

## originality

FAIL

The decisive arithmetic of the exact sextic is already covered by Morton's explicit period-three classification and discriminant formula, not merely by a generic wreath-product heuristic. With the earlier graph-lift lemma, the density and multiplicity statements are mechanically implied by these specialized data and the standard Chebotarev count in a cyclotomic fiber. The particular fraction need not have been printed to be covered.

## value

FAIL

The open congruence class and the canonical-cycle statistic are natural and the presentation is useful as an explicit worked example. However, the exact statistic is mechanically obtained from a stronger period-three classification at the same parameter and an already published cycle-lift lemma, followed by a degree gcd and a two-block Chebotarev count. It does not treat the remainder of the class, classify any further cycles, or introduce an independently useful new exact fact under the stated standard. The correct self-contained certificate does not cure that limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
