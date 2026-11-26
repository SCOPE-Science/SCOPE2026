# Independent mathematical audit

## correctness

PASS

The corrected complete RESULT.md under repairs/1 replaces a false sharpness witness: in the frozen proof, support {0} maps to the complement of {−1,0,1}, not to the empty set for n≥4, and is itself periodic for n≥5. The replacement support V\{0} has a selected neighbor at every vertex for every n≥3, so its first iterate is empty and its second is V; it proves sharpness. The symmetric-polarity identity Φ³=Φ proves the upper bound independently. The repair also states the fixed-point condition directly in the ordinary cycle: exactly its maximal independent sets omitting 0, since the additional input is zero on all such supports and vertex 0 must still be dominated. Subtracting the cycle sets containing 0 gives H_(n−3), with the empty path at n=3. The repaired theorem has unchanged formulas and scope. A separately built transfer matrix reproduced the exact zero annihilator and h_0 through h_9 = (0,−1,−1,1,−2,0,−1,−8,−7,−21), giving the numerator by convolution and proving the all-coefficient recurrence thereafter. Direct state enumeration corroborated the examples. Independently, the defective double cover is a cycle with an antipodal chord for odd n or two cycles joined by a bridge for even n. Lost maximal independent sets contain both added-edge endpoints and number H_(n−3)². Gained ones have exactly one selected endpoint and the other endpoint previously undominated; along their respective remaining paths this gives 2H_(n−5)² for odd n≥5 (zero at n=3), or 2H_(n−3)H_(n−7) for even n≥8 (the latter path count replaced by one for n=4 and n=6). These reproduce the correction coefficients by an independent combinatorial count. For each parity R_n∼λ^n, and the simple dominant pole at 1/λ gives the stated retention 0.940639467358146. The two exceptional series indices are formal, not dynamics of small rings. VERIFICATION.md and verify_feedback.py were inspected, not executed; the original verifier remains the replay entry point for the matrix identity, and the repaired analytic witness proves sharpness beyond finite sizes.

## originality

PASS

The repaired proof preserves the exact distinct claim: the inhomogeneous one-self-input recurrent-state correction and its limiting proportion. The polarity argument, the ordinary cycle Perrin count, and the unmarked odd NOR census are available ingredients/baselines, not novelty claims. No inspected claim covers the chorded or bridge-joined double-cover enumeration underlying the corrected theorem, and the indicated limitations remain. This is a bounded best-of-knowledge assessment, not priority certification.

## value

PASS

This is a motivated sensitivity calculation on a natural synchronous network; it answers precisely how one added inhibitory input changes the entire labelled recurrent census, not just the existence or length of attractors. The exact formula detects a small-size increase despite a persistent asymptotic loss, so no simple monotonicity in the added input explains the result. The proof repair preserves these contributions and avoids claiming originality for the general one-step polarity bound or the Perrin baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
