---
audit_date_utc: 2026-10-01
status: failed
record_id: SCOPE-20260915-012
---

# Scientific audit

## Final claim

Every smooth manifold homeomorphic to \(\mathbb H P^4\) is diffeomorphic to exactly one of \(\mathbb H P^4\) and \(\mathbb H P^4\#\Sigma^{16}\); the two are distinct, every self-homeomorphism is orientation preserving, and the inertia group is trivial.

## Correctness — PASS

The published concordance calculation gives two classes represented by \(\mathbb H P^4\#\Sigma\). For any self-homeomorphism, a generator \(u\in H^4\) maps to \(\pm u\), so \(u^4\) is fixed and the degree is \(+1\). Obstruction theory identifies maps \(\mathbb H P^4	o S^{16}\) by top degree, hence precomposition fixes the collapse-map smoothing class. Therefore the homeomorphism action on the two concordance classes is trivial; the two underlying diffeomorphism types remain distinct and \(I(\mathbb H P^4)=0\).

Checked sources: Basu--Kasilingam, arXiv:1708.06582, Theorems 3.1 and 5.7; artifacts/verify_orbits.py

Residual risk: The concordance classification itself is taken from the published theorem, not re-proved from stable homotopy calculations.

## Originality — FAIL

Basu--Kasilingam already prove that \(C(\mathbb H P^4)\) has exactly two classes represented by connected sums with \(\Theta_{16}\), and Theorem 5.7/Corollary 5.8 identify the tangential smooth structures and diffeomorphism representatives. The remaining passage to unordered diffeomorphism types is an elementary action check using \(H^*(\mathbb H P^4)=\mathbb Z[u]/(u^5)\): every self-homeomorphism has degree \(+1\), so it acts trivially on the top-cell collapse class. Thus the final classification is mechanically implied by the primary paper plus standard cohomology.

### Equivalent Formulations

Searches: HP4 smooth structures inertia group diffeomorphism types homotopy 16 sphere; C(HP4) Theta16

Evidence: Theorem 3.1(ii) gives exactly two concordance classes; Theorem 5.7(ii) gives their tangential smooth representatives.

Reasoning: The only possible further identification is by self-homeomorphism action.

### Broader Coverage

Searches: manifolds homeomorphic HP4 diffeomorphism classification Basu Kasilingam

Evidence: Corollary 5.8 already states every tangentially homotopy equivalent manifold is diffeomorphic to \(\mathbb H P^4\#\Sigma\).

Reasoning: The primary source supplies essentially the full classification framework.

### Exact Database Or Table

Searches: Theta16 HP4 smooth structure

Evidence: No table is needed because the source theorem explicitly lists the two classes.

Reasoning: Coverage is theorem-level.

### Claim Vs Prior Implication

Searches: self homeomorphism HP4 degree orientation

Evidence: A self-homeomorphism sends \(u\) to \(\pm u\), hence fixes \(u^4\) and has degree \(+1\).

Reasoning: This elementary fact makes the source's two smoothing classes separate diffeomorphism orbits.


### Source inspections

- **COVERING** — 1708.06582 (https://arxiv.org/pdf/1708.06582): Full primary PDF, including Theorem 3.1(ii), Theorem 5.5, Theorem 5.7(ii), and Corollary 5.8. Evidence: It gives exactly two concordance classes and identifies all tangentially homotopy equivalent manifolds with connected sums by homotopy 16-spheres.
- **CONTEXT** — 0505621 (https://arxiv.org/pdf/math/0505621): Primary background on projective-plane-like manifolds and inertia phenomena. Evidence: Useful background but not needed for the decisive implication.

Checked sources: https://arxiv.org/pdf/1708.06582; https://arxiv.org/pdf/math/0505621; artifacts/verify_orbits.py

Residual risks: The paper distinguishes concordance, homotopy inertia, and inertia groups; the triviality of the final self-homeomorphism action is not stated there verbatim, but follows immediately from the cohomology ring and top-cell class.

## Value — FAIL

The final statement closes an orientation/action bookkeeping point left implicit in a published two-class smoothing theorem. That clarification is correct, but after the source theorem the remaining argument is routine and does not constitute a separately motivated mathematical gap under the stated value bar.

Checked sources: https://arxiv.org/pdf/1708.06582

Residual risk: A broader theorem describing mapping-class actions on smoothing sets for a family of projective spaces could be valuable; this isolated case does not provide that.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and value.
