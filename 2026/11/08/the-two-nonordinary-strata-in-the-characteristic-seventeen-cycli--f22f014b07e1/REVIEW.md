# Scientific review

## Correctness — PASS

For the smooth genus-six superelliptic model \(y^4=x(x^2-1)(x^2-t)\), the six regular differentials are explicitly listed. The Cartier coefficient rule follows by taking seventeenth powers and extracting exponents congruent to \(16\) modulo \(17\). Each of the three coefficient matrices is derived from a bounded binomial sum over \(\mathbb F_{17}[t]\). The two diagonal entries of the \(2\times2\) block, the middle entry of the \(3\times3\) block, and its invertible parity-even minor identify every possible rank drop. The same decomposition proves stable rank, not merely first Cartier rank, because all subblocks are either invertible or identically zero at each parameter. The reciprocal-parameter relation establishes exactly two distinct geometric isomorphism classes. The standard-library verifier reproduces all polynomial identities and the finite-field root exclusions. The proof is all-parameter in \(t\) over the algebraic closure of \(\mathbb F_{17}\).

## Originality — PASS (qualified)

The closest source is Ohashi, arXiv:2605.29624v1, Sections 2 and 3.3. It formulates superspeciality via hypergeometric and Cartier coefficient equations and enumerates superspecial curves, but the inspected material does not supply the exact \(17\)-rank and \(a\)-number at every member in characteristic \(17\). Badr--Bars, arXiv:1510.06190, Section 3, provides the automorphism-group classification in characteristic zero and not positive-characteristic Cartier strata. Searches for this exact family, its alternative plane equation, the characteristic-seventeen exceptional parameters, and analogous numerical invariants did not reveal an equivalent result. That negative search does not establish historical uniqueness. The known general Cartier coefficient methods are openly used; they do not themselves state the two special isomorphism classes and their ranks. Residual risk: other specialized genus-six or superelliptic-rank tables could contain the same full classification implicitly.

## Mathematical value — PASS

The motivating family is a natural one-dimensional automorphism stratum of genus-six plane curves. Knowing that it contains no superspecial member does not answer where ordinarity fails or how strongly the Cartier operator degenerates. Here the **entire** nonordinary locus in the smallest allowed characteristic is determined, with exactly two isolated geometric classes carrying two different simultaneous pairs of \(p\)-rank and \(a\)-number; the stronger exceptional member has \(a=4\) without being superspecial. These are intrinsic Jacobian invariants relevant to finite-characteristic moduli stratification, rather than an arbitrary evaluated coefficient or a routine restatement of a superspeciality table. The result is confined to characteristic seventeen; no all-prime pattern is asserted.

## Verification and limitations

Replay `python3 verify.py`. The code checks the polynomial identities over the entire parameter line, and validates the exceptional finite-field parameter arithmetic. The mathematical argument, rather than sample enumeration, supplies the claimed classification. The result does not determine Newton polygons or full \(p\)-torsion group schemes. Independent specialist confirmation and broader historical-priority checks remain outstanding.

Self-review: passed. Independent audit: not yet performed.
