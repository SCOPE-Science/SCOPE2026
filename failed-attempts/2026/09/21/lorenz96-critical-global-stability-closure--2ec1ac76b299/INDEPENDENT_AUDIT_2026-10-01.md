# Independent scientific audit — 2026-10-01

**Disposition:** failed

**Final claim:** For every homogeneous quadratic, Euclidean-energy-preserving, cyclically equivariant \(G:\mathbb R^N\to\mathbb R^N\), the uniform equilibrium of \(\dot x=G(x)-x+F e\) is globally asymptotically stable exactly on the closed spectral window \(Fp_+\le1\) and \(Fp_-\le1\), including every finite nonhyperbolic endpoint; the Lorenz-96 forcing interval is the corresponding exact closed Fourier interval.

## C — PASS

The proof reconstructs cleanly. Cyclic equivariance and energy preservation give \(G(e)=0\), and after translating \(w=x-Fe\), the Euclidean energy satisfies \(\dot V=w^T(FS-I)w\). In the strict region this is negative definite. At a finite endpoint the zero-dissipation set is an extreme eigenspace of \(S\); polarizing \((e+sw)^TG(e+sw)=0\) gives \(e^TG(w)=-w^TAw\), so on every nonzero critical vector the mean coordinate has nonzero derivative. Hence the largest invariant subset of \(\{\dot V=0\}\) is \(\{0\}\), and LaSalle gives global asymptotic stability. Outside the window the normal circulant linearization has a positive-real-part eigenvalue.

Residual risk: No correctness defect was found; the record does not quantify endpoint decay rates.

## O — FAIL

A published result dated 2026-09-20, “Closed energy-stability boundary for Lorenz-96-like quadratic advection,” was inspected from its actual repository RESULT.md. It states the same general hypothesis, the same closed if-and-only-if stability criterion, the same endpoint conclusion, the same polarization identity \(e^TG(y)=-y^TAy\), the same zero-dissipation transversality argument, and the same finite-\(N\) Lorenz-96 Fourier endpoints. The 2026-09-21 record is therefore directly implied by, and essentially duplicates, that earlier theorem.

Residual risk: The priority comparison is decisive; no access uncertainty affects the earlier published result.

### Equivalent formulations

**Searches:** Resultary: Lorenz-96 closed endpoint global asymptotic stability energy preserving cyclic quadratic equality threshold; Earlier published record: Closed energy-stability boundary for Lorenz-96-like quadratic advection, 2026-09-20

**Evidence:** The earlier theorem states global asymptotic stability iff \(\max_k(F r_k-1)\le0\) for the same homogeneous energy-preserving cyclic quadratic class. Its proof uses the same identity \(e^TG(y)=-y^TAy\) and endpoint transversality.

**Reasoning:** The formulations are equivalent after identifying \(r_k\) with the eigenvalues of the symmetric part \(S\).

### Broader coverage

**Searches:** Earlier published 2026-09-20 RESULT.md; Kerin–Engler, arXiv:2005.07767 / DOI 10.3934/dcdsb.2021064

**Evidence:** The earlier published result already includes the general quadratic class and the Lorenz-96 corollary. Kerin–Engler supplies the prior strict-interior theorem but is weaker at equality.

**Reasoning:** The decisive earlier result has equal or effectively identical coverage, so no new broader slice survives.

### Exact database or table

**Searches:** Resultary semantic database for Lorenz-96 endpoint stability; Repository inspection of the earlier result

**Evidence:** The semantic database returned the exact earlier theorem as the second highly similar hit.

**Reasoning:** This is theorem coverage, not a numerical database issue; the exact prior record is sufficient.

### Claim versus prior implication

**Searches:** Line-by-line theorem/proof comparison with the 2026-09-20 RESULT.md

**Evidence:** The prior theorem directly implies the full final claim, including equality endpoints and the standard Lorenz-96 interval.

**Reasoning:** The implication is direct, so originality fails regardless of differences in notation or title.

### Source inspections

- **Closed energy-stability boundary for Lorenz-96-like quadratic advection** (published repository record dated 2026-09-20; RESULT.md blob 4b68b336f6f6d135a1b2b9926c9bd6435fadc48f): COVERING. Trigger: Resultary returned it as a highly similar earlier theorem. Material read: Complete RESULT.md including theorem, proof, Lorenz-96 corollary, context, and limitations. Method: Actual Git repository blob inspection. Evidence: It contains the same closed stability criterion and endpoint transversality proof.
- **On the Lorenz '96 model and some generalizations** (arXiv:2005.07767 / DOI 10.3934/dcdsb.2021064): PARTIAL_COVERAGE. Trigger: Background source for the strict-interior theorem. Material read: Accessible preprint/metadata and the comparison stated in both SCOPE results. Method: Primary-source web inspection. Evidence: It is relevant background but not needed for the decisive originality failure because the 2026-09-20 published theorem already covers equality.

### Residual risks

- No unresolved originality-access risk affects the rejection decision.

## V — FAIL

Although the mathematical theorem itself is useful, this record as submitted adds no substantive mathematical gap beyond the already published 2026-09-20 theorem: the final statement and proof mechanism are the same. Under the audit bar, republishing an already-covered result is not an additional valuable contribution.

Residual risk: This value failure concerns the submitted record’s incremental contribution, not the intrinsic interest of the underlying endpoint theorem.

## Overall disposition

**FAILED**
