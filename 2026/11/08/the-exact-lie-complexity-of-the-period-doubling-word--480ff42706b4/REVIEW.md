# Scientific review

## Correctness — PASS
The valuation representation \(p(i)=\nu_2(i+1)\bmod2\) yields exact parity identities and the forbidden words \(11\) and \(0000\). In a hypothetical rotation-complete circle of odd length at least five, successive one-spacing is always even, contradicting odd circumference; circles with fewer than two ones require forbidden long zero runs. At even lengths the complete factor language consists of both phase insertions of factors of the complement; rotations correspond to source rotations, yielding an exact bijection of Lie classes and the identity \(L(2m)=L(m)\). Together with the checked length-one and length-three cases this proves the full formula. The standalone finite exact-factor verifier confirms lengths 1 through 160 but is not used to justify infinitely many lengths.

## Originality — PASS (subject to bibliographic risk)
Bell–Shallit, *Lie Complexity of Words*, arXiv:2102.03821, is the closest primary source: it defines the invariant, proves automaticity and bounds it for linear-complexity words, and examines other named examples, not an exact period-doubling law. De Luca–Fici, arXiv:2206.00995, give an exact formula for Sturmian words, a disjoint word class. Cassaigne–Fici–Sciortino–Zamboni, arXiv:1402.5843, study cyclic complexity, which counts a larger collection of rotation classes and thus does not settle the exact all-rotations Lie count. Searches for period doubling, cyclic conjugacy, Lie complexity, and the parameter support \(2^a\) and \(3\cdot2^a\) did not locate an equivalent result. An unindexed or differently titled exact computation remains a live risk; lack of a search hit is not uniqueness evidence.

## Mathematical value — PASS
The theorem supplies the complete Lie-complexity function, including all zero and nonzero lengths, for a canonical binary automatic fixed point. The exact geometric support and the structural halving bijection go beyond a finite table or generic automatic-computability algorithm. The contrast with cyclic complexity and the unlike odd bases for other standard automatic words provide an intrinsically motivated invariant classification.

## Verification and limitations
The accompanying `verify.py` reconstructs complete factor sets from substituted two-letter source blocks and checked all lengths 1 through 160; every conclusion for arbitrary length is separately established in the proof. The result does not classify other automatic words. It has not received independent validation.

Self-review: passed. Independent audit: not yet performed.
