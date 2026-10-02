# Independent scientific review — 2026-10-01

## Final claim

For every homogeneous quadratic, Euclidean-energy-preserving, cyclically equivariant \(G:\mathbb R^N\to\mathbb R^N\), the uniform equilibrium of \(\dot x=G(x)-x+F e\) is globally asymptotically stable exactly on the closed spectral window \(Fp_+\le1\) and \(Fp_-\le1\), including every finite nonhyperbolic endpoint; the Lorenz-96 forcing interval is the corresponding exact closed Fourier interval.

## Correctness — PASS

The proof reconstructs cleanly. Cyclic equivariance and energy preservation give \(G(e)=0\), and after translating \(w=x-Fe\), the Euclidean energy satisfies \(\dot V=w^T(FS-I)w\). In the strict region this is negative definite. At a finite endpoint the zero-dissipation set is an extreme eigenspace of \(S\); polarizing \((e+sw)^TG(e+sw)=0\) gives \(e^TG(w)=-w^TAw\), so on every nonzero critical vector the mean coordinate has nonzero derivative. Hence the largest invariant subset of \(\{\dot V=0\}\) is \(\{0\}\), and LaSalle gives global asymptotic stability. Outside the window the normal circulant linearization has a positive-real-part eigenvalue.

**Risk:** No correctness defect was found; the record does not quantify endpoint decay rates.

## Originality — FAIL

A published result dated 2026-09-20, “Closed energy-stability boundary for Lorenz-96-like quadratic advection,” was inspected from its actual repository RESULT.md. It states the same general hypothesis, the same closed if-and-only-if stability criterion, the same endpoint conclusion, the same polarization identity \(e^TG(y)=-y^TAy\), the same zero-dissipation transversality argument, and the same finite-\(N\) Lorenz-96 Fourier endpoints. The 2026-09-21 record is therefore directly implied by, and essentially duplicates, that earlier theorem.

**Risk:** The priority comparison is decisive; no access uncertainty affects the earlier published result.

## Value — FAIL

Although the mathematical theorem itself is useful, this record as submitted adds no substantive mathematical gap beyond the already published 2026-09-20 theorem: the final statement and proof mechanism are the same. Under the audit bar, republishing an already-covered result is not an additional valuable contribution.

**Risk:** This value failure concerns the submitted record’s incremental contribution, not the intrinsic interest of the underlying endpoint theorem.

## Overall disposition

**FAILED**
