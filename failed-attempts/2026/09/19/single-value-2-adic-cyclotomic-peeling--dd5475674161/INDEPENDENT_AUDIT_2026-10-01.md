# Independent audit — Exact 2-adic peeling from a single cyclotomic value

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The Möbius product gives \(C^\varepsilon=H_a(P)\), with \(a=\nu_2(C-1)=n/\operatorname{rad}(n)\). After dividing by a known prefix fingerprint, the unique smallest omitted singleton contributes first at exponent \(a p_{j+1}\), so the residual valuation equals \(a p_{j+1}\). The startup comparisons follow from the same first nonzero binary term; independent exact checks on representative squarefree and nonsquarefree indices reproduce the fingerprint identity and boundary cases.

## Originality

**FAIL** — Two earlier 18 September results already imply the complete binary prime-support recovery claimed here. One handles every nonsquarefree binary index from a single value; the other handles squarefree binary indices by prefix residuals and explicitly resolves the only even-squarefree \(2,3\) collision. The present \(H_a\) fingerprints are an algebraically equivalent Möbius-product normalization, not a new extractor.

### Equivalent formulations

Together the two earlier theorems cover every \(n>1\), the quantifier of the present claim.

Evidence: The first earlier result gives single-value binary peeling for every nonsquarefree index. The second gives complete binary prefix peeling for odd squarefree indices and states the even-squarefree rule, with only the initial \(2,3\) collision and the explicit observation that testing \(3\mid n\) resolves it.

### Broader coverage

The claimed 'no further cyclotomic evaluation' changes the representation of a known-prefix factor but not the mathematical information or the prime-recovery implication.

Evidence: For squarefree \(a=1\), the current fingerprint is exactly a Möbius-product representation of the cyclotomic prefix factor used in the earlier residual recursion, up to the orientation sign. For even squarefree indices, the earlier theorem already identifies the false-branch baseline \(3\), the only \(2,3\) collision, and how to resolve it from the known index.

### Exact database or table

The chronology and theorem text establish prior coverage.

Evidence: The higher-local theorem was committed 18 September 2026 and the general single-value p-adic theorem later that day; the current exact binary fingerprint record was added on 19 September 2026.

### Claim versus prior implication

No surviving final claim escapes the prior implications.

Evidence: The nonsquarefree part is a direct specialization of the earlier single-value p-adic theorem. The squarefree part is the earlier higher-local recursion with the known-prefix cyclotomic factor written as its Möbius product; the even \(2,3\) startup is explicitly addressed there.

### Source inspections

- **Single-value p-adic peeling of cyclotomic index radicals** — COVERING_NONSQUAREFREE.
  Identifier: published record SCOPE-20260918-08dfc55c58fd
  Material read: complete result and proof.
  Evidence: It recovers the full radical from one \(\Phi_n(2)\) for every nonsquarefree \(n\), with the same local Möbius-dominance mechanism.
- **Higher local cyclotomic prime extraction** — COVERING_SQUAREFREE.
  Identifier: published record SCOPE-20260918-01e648b0fd33
  Material read: complete result and proof.
  Evidence: It gives exact binary prefix residual valuations for squarefree indices and explicitly describes the even case and the unique \(2,3\) collision.
- **Cyclotomic Prime Extractors** — ACCESS_RISK.
  Identifier: arXiv:2609.18480
  Material read: abstract and accessible metadata only.
  Evidence: The accessible material confirms the prime-extractor setting. No whole-document noncoverage conclusion is drawn.

### Residual risks

- The very recent Shunia full text was not obtained through the lawful routes attempted; this access limitation cannot override the decisive earlier published theorem coverage.

## Scientific value

**FAIL** — Once the earlier nonsquarefree and squarefree recursions are credited, the remaining difference is a change of algebraic normalization from prefix cyclotomic factors to their Möbius-product fingerprints. That is a routine equivalent formulation rather than a separately valuable mathematical gap.

## Final assessment

The mathematical calculation survives, but the research claim is rejected because prior coverage leaves no distinct original and valuable final claim. The original research package is retained as failed evidence.

This assessment is mathematical review evidence, not formal proof-assistant verification or a guarantee against undiscovered prior art.
