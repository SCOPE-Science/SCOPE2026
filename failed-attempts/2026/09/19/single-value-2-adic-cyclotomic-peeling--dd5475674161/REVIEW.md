# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **failed**.

- Correctness: **PASS**. The Möbius product gives \(C^\varepsilon=H_a(P)\), with \(a=\nu_2(C-1)=n/\operatorname{rad}(n)\). After dividing by a known prefix fingerprint, the unique smallest omitted singleton contributes first at exponent \(a p_{j+1}\), so the residual valuation equals \(a p_{j+1}\). The startup comparisons follow from the same first nonzero binary term; independent exact checks on representative squarefree and nonsquarefree indices reproduce the fingerprint identity and boundary cases.
- Originality: **FAIL**. Two earlier 18 September results already imply the complete binary prime-support recovery claimed here. One handles every nonsquarefree binary index from a single value; the other handles squarefree binary indices by prefix residuals and explicitly resolves the only even-squarefree \(2,3\) collision. The present \(H_a\) fingerprints are an algebraically equivalent Möbius-product normalization, not a new extractor.
- Scientific value: **FAIL**. Once the earlier nonsquarefree and squarefree recursions are credited, the remaining difference is a change of algebraic normalization from prefix cyclotomic factors to their Möbius-product fingerprints. That is a routine equivalent formulation rather than a separately valuable mathematical gap.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
