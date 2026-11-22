# Mathematical assessment: complex-activity circle rigidity for a hard-core cycle

## Correctness — PASS

The claim has exact quantifiers: every \(n\ge2\), every strictly positive vector of background activities on one shore of \(C_{2n}\), and one complex fugacity shared by the other shore. The transfer representation is obtained by summing independent odd-site occupancies conditional on even-site occupancies. Its extreme coefficients are \(c_n=1\), \(c_{n-1}=n\), \(c_0=\prod_j(1+b_j)\) and \(c_1=c_0\sum_j[(1+b_{j-1})(1+b_j)]^{-1}\). Circle roots force the reciprocal coefficient identity, and the arithmetic–geometric mean equality case forces two-periodicity of activities. Exact factorizations for odd and even \(n\) prove the converse, with strict quadratic discriminants and distinct cosines proving simplicity. No inference from finite enumeration to all sizes is made. `verify_circle.py` ran successfully on 9,965 exact/numerical cases, independently checking the coefficient derivation and factors.

## Originality — PASS on examined evidence

The strongest relevant inspected publication is Jerrum–Patel (2026), Section 5.1: its two alternated fugacity transfer product is structurally close and already supports a homogeneous-shore special case, but its examined statement neither allows an arbitrary \(n\)-component positive background vector nor proves the strict **only-if** circle criterion. Lebowitz–Ruelle–Speer (2012), arXiv:1204.0558, treat Ising Lee–Yang zeros and hard-object limits and do not establish this weighted even-cycle circle-rigidity equivalence in the inspected relevant portions. The classical monomer–dimer negative-real-root theorem concerns a different fugacity specialization. Published semantic records for nearby Ising impurity Lee–Yang circle transitions and an irreversible alternating-rate adsorption model concern distinct partition functions or nonequilibrium processes. Current primary-literature and published-record searches did not reveal a stronger statement implying the precise iff theorem. Priority is provisional because an unindexed earlier derivation or a general self-inversive-polynomial characterization might implicitly cover it.

## Mathematical value — PASS

A nontrivial **rigidity/exception classification** for complex partition zeros is more informative than reproducing a known transfer identity: arbitrary positive frozen disorder destroys exact circle localization, while every period-two disorder, including unequal alternating weights when permitted by parity, restores it. The proof yields a readily checked global coefficient certificate; complete simple-root location and a persistent angular exclusion interval quantify the zero geometry for an infinite system-size family. This matters directly to robustness of Lee–Yang-style zero localization under spatial inhomogeneity, while not claiming a thermodynamic transition.

## Closest literature and limitations

- Lebowitz, Ruelle and Speer (2012), arXiv:1204.0558, introductory Lee–Yang and monomer–dimer discussion.
- Jerrum and Patel (2026), DOI:10.1112/jlms.70458, full HTML, especially §5.1 on cycles with two alternating fugacities.
- Unindexed work or a hidden implication of an already known general polynomial theorem could diminish priority. No independent audit has been performed; no arbitrary complex background activity or general graph extension is claimed.

Self-review: passed. Independent audit: not yet performed.
