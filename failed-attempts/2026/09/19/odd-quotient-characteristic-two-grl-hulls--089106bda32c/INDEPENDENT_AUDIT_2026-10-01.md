---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

When \(q=2^e\) and \(e/\gcd(e,\ell)\) is odd, every generalized Roth--Lempel evaluation/extension skeleton in the stated low-degree range can realize every \(\ell\)-Galois hull dimension \(0,\ldots,k-s\) by changing only nonzero coordinate multipliers, hence without changing the classical weight distribution.

## Correctness — PASS

The power-map lemma is correct: writing \(e=db\), \(\ell=da\) with \(b\) odd shows \(\gcd(2^\ell+1,2^e-1)=1\), so every nonzero Lagrange coefficient has a unique \((2^\ell+1)\)-st root. Substituting those roots into the cited GRL dual equations, equality on the unscaled coordinates forces \(g=f^{2^\ell}\) by the degree bound; the extension equation kills the top \(s\) coefficients, and the scaled coordinates force exactly \(k-s-h\) prescribed roots. The converse gives an \(h\)-dimensional polynomial space. The inspected verifier independently checks the gcd identity and hundreds of generator-matrix hull dimensions, including \((e,\ell)=(5,2)\).

**Checked sources.** assigned RESULT.md at the frozen tree; artifacts/verify.py and verification.txt; Wu--Liu--Chen--Zhou, arXiv:2609.20453; Wan--Zhu, arXiv:2412.05011

**Residual risks.** The audited theorem uses a slightly different degree endpoint notation, but the full primary Proposition II.8/III.2 confirms the dual equations and root-count construction on which the proof depends.

## Originality — FAIL

The primary GRL paper was inspected in full. Its Proposition III.2 already proves every hull dimension for arbitrary extension matrix whenever normalized Lagrange coefficients lie in the relevant power-root class, using exactly the multiplier scaling and root-count argument reproduced by the audited proof. In the odd-quotient binary regime, the sole extra step is the elementary identity \(\gcd(2^\ell+1,2^e-1)=1\), which makes that root condition automatic for every nonzero coefficient. Wan--Zhu already treat the same finite-field regime for GRS/EGRS hulls. Under the implication standard, this is covered.

### Equivalent formulations

The audited theorem is the source construction in the parameter regime where the needed power roots exist for every coefficient.

### Broader coverage

These broader results do not literally state arbitrary evaluation sets, but together with power-map surjectivity they expose the audited statement as the routine general condition becoming automatic.

### Exact database or table

The exact_database_or_table check is inapplicable because the decisive coverage is symbolic and theorem-level.

### Claim versus prior implication

The audited theorem is therefore Proposition III.2 with its coefficient-root hypothesis discharged by an elementary field identity; the distance-neutral corollary is immediate from diagonal coordinate scaling.

**Source inspections.**
- Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs: Full 29-page primary PDF, including Proposition II.8 and the common construction Proposition III.2. Assessment: Directly supplies the multiplier/root-count proof under a normalized-coefficient power-root condition; the audited field lemma makes that condition automatic.
- Full-field generalized Roth--Lempel Galois hulls for arbitrary indices: Complete RESULT.md from the public repository. Assessment: Covers the full evaluation set for every Galois index; it does not alone cover arbitrary evaluation sets but confirms that power-root obstructions are the key issue.
- Galois self-orthogonal MDS codes with large dimensions: Abstract and indexed theorem description. Assessment: Prior art for the field regime and arbitrary hull propagation in GRS/EGRS codes.

**Checked sources.** Wu--Liu--Chen--Zhou, arXiv:2609.20453, full PDF Proposition II.8 and III.2; https://arxiv.org/abs/2412.05011; public GRL result dated 2026-09-18; published-results semantic search

**Residual risks.** No residual access blocker remains for the decisive primary GRL comparison. A future reformulation could present the odd-quotient regime explicitly, but it would not change the implication-level coverage conclusion.

## Value — FAIL

The parameter observation is useful for practitioners, but the mathematical work is essentially a substitution: a standard cyclic-group gcd identity makes every multiplier root exist, after which the published GRL hull construction runs unchanged. The distance-neutral statement is then a routine monomial-isometry fact. This is too mechanical to qualify as a separate valued finding under the stated bar.

**Checked sources.** Wu et al. 2026 GRL construction; Wan--Zhu 2024 Galois-hull regime; earlier full-field GRL arbitrary-index result

**Residual risks.** The resulting code families may still be practically useful; the rejection concerns standalone scientific value/originality of this theorem.

## Limitations

- The algebraic statement is correct.
- The rejection is scientific coverage/value, not a correctness or access failure.
- The primary GRL paper was inspected in full; its Proposition III.2 is the same multiplier/root-count construction under a coefficient-root condition, so the odd-quotient binary result is obtained by making that condition automatic via an elementary power-map bijection.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
