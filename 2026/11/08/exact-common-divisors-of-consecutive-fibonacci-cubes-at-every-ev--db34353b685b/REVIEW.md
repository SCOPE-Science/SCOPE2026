# Review of the exact even-length Fibonacci-cube gcd theorem

## Correctness

**PASS.** The proof independently derives the finite period gcd \(G=\gcd(F_{2m+1}-1,F_{2m+2}-1)\), proves a cubic Cassini gcd lemma for all primes including two and three, and establishes \(\gcd_{n\ge1}(F_{n+2m}^3-F_n^3)=D\). The telescoping first-sum identity then shows \(\gcd(D,S_0)\) is \(D\) or \(D/2\), with the second case exactly when \(3\mid m\). Every step applies for every integer \(m\ge1\). The integer formula was checked by an independent recurrence-based enumeration at 120 even lengths; this is corroboration, not proof.

## Originality

**PASS within inspected evidence.** Section 6.1 (page 14) of the full accessible Mbirika–Spilker paper, arXiv:2204.12626v2, raises the cubic problem and suggests the opposite factor-of-two split. The new statement does not follow from the earlier first- and second-power gcd formulas. The 2021 Guyer–Mbirika paper (first powers) and the 2018 Frontczak paper (cubic power-sum identities) were inspected in their accessible full versions; neither supplies the shifted-window cubic gcd classification. Focused literature and published mathematical-record searches found no equivalently covering result. A nonindexed theorem or an implicit consequence of historical cubic-sum identities remains possible and should be considered at independent priority review.

## Mathematical value

**PASS.** The result gives a complete infinite classification of a natural number-theoretic invariant that was explicitly raised in published literature. The primewise cubic Cassini lemma explains a nontrivial extra factor of three, while a telescoping parity argument pinpoints the exact loss of a factor of two. It replaces a conjectural but incorrect residue-class split with a proved formula for all even lengths, not merely isolated numerical counterexamples.

## Residual scientific limitations

The theorem covers ordinary Fibonacci cubes at even lengths only. It does not resolve the Lucas counterpart, generalized initial conditions, odd lengths, or higher powers. Historical summation formulas may furnish alternative derivations; novelty is relative to the inspected material.

Self-review: passed. Independent audit: not yet performed.
