# Scientific review

## Correctness

**PASS.** The recurrence map has determinant \(-1\) and is a permutation. The proof computes the exact two-adic Smith valuations of \(A^{2^j}-I\): \((0,1)\) for \(j=0\), \((1,1)\) for \(j=1\), and \((j,j+1)\) for every \(j\ge2\). The only nontrivial input is the sharp valuation \(\nu_2(1+u^2)=1\) when \(u\) is odd; the induction step multiplies by a matrix congruent to the identity modulo \(2\). The modular kernel sizes, exact least-period counts, and orbit counts follow by standard Smith reduction and period inversion. The ranges \(r=1,2\) are handled separately; the formulas cover all positive \(r\) and all \(K\equiv2\pmod4\). The accompanying checker exhaustively verifies 42 finite complete state spaces and 54 matrix valuation tests; finite computations are corroboration, not an infinite proof.

## Originality

**PASS within inspected evidence.** Benfield–Lippard (2024, arXiv:2404.08194) determine periods for the standard initial values, whereas the theorem counts every orbit from every initial pair. Fiebig–Mbirika–Spilker (2024, arXiv:2408.14632) study periods, entry points, order, and special Lucas pairs; the inspected relevant sections do not compute the universal orbit multiplicities. Wall's 1960 paper is cited for a criterion comparing arbitrary-seed periods in the Fibonacci case, not for the proposed \(K\equiv2\pmod4\) all-orbit count; the full original was not accessible here. Searches for all-state Pell or \(K\)-Fibonacci cycle counts, equivalent Smith descriptions, and known integer-cycle tables did not identify a dominating claim. A hidden equivalent theorem remains a residual risk; absence of search hits alone is not novelty proof.

## Mathematical value

**PASS.** This is a natural complete classification of the finite dynamics of a classical recurrence family, rather than an arbitrary finite modulus slice: powers of two are precisely where the two-adic companion matrix changes order upon lifting. The theorem goes beyond the period of the distinguished \((0,1)\) orbit by giving all primitive lengths and their exact multiplicities simultaneously over infinitely many parameters and moduli, with a striking independence of the odd part of \(K/2\). The cycle-count invariant is directly meaningful in recurrence dynamics and in the combinatorics of finite permutations.

## Closest literature and limitations

The standard-seed period in Benfield–Lippard is related but does not imply the number of shorter orbits. The Lucas sequence comparisons of Fiebig–Mbirika–Spilker likewise do not exhaust arbitrary initial pairs. Wall's 1960 full text was not obtained, though its known cited claim concerns seed-period comparison. General finite linear-dynamics classifications could potentially subsume the result under different terminology. No assertion is made for \(K\not\equiv2\pmod4\), odd moduli, or explicit orbit representatives.

Self-review: passed. Independent audit: not yet performed.
