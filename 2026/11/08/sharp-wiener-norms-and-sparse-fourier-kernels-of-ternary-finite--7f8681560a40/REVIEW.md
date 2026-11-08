# Scientific review: sharp ternary quadratic-shell Fourier projection norms

## Correctness — PASS

The theorem fixes \(q=p^s\) with odd \(p\), any nondegenerate symmetric three-variable quadratic form, and a nonzero radius. The proof uses the exact three-dimensional Gauss completion, proves the requisite Salié identity by Fourier transforms in its free parameter, counts the dual quadratic-value fibers, and sums absolute values without replacing exact expressions by bounds. Both operator-norm equalities are attained, by a point mass and a conjugate-phase input. The Hermitian specialization checks its trace-one affine quadratic parameterization and the scalar Fourier multiplicity. The independent full-spectrum finite-field implementation checks both discriminant signs for seven fields, including nonprime fields, with complete multiplicity and Parseval checks. Computation corroborates the general proof rather than establishing it.

## Originality — PASS under bounded comparison

The closest primary source is Iosevich and Koh, *Extension theorems for spheres in the finite field setting* (arXiv:0712.1627), whose Lemma 4 states a general transform in terms of a Salié-type sum, not the absolute Fourier sum or sharp spectral projection norm. Their related paper on nondegenerate quadratic surfaces (arXiv:0804.4505) proves Fourier decay and extension estimates, not this endpoint idempotent norm. Green and Sanders (arXiv:math/0605524) develop the spectral-norm framework for Boolean functions in characteristic two, not the present odd-field quadratic-shell formulas. The closest examined public research results concerning exact projection norms address different harmonic spaces; results on small finite-field sphere extension extremizers instead optimize \(L^2\to L^4\), not \(\ell^1\to\ell^1\). The new claim is not the classical transform or Salié evaluation: it is the explicit two-type global absolute sum and kernel-zero classification, including prime-field trace fibers and Hermitian projector specialization.

**Residual originality risk:** An earlier source may have already summed the Salié amplitudes for three-dimensional finite quadrics. No exhaustive historical-priority certification is asserted. The classical transform plus Salié evaluation makes the result accessible, but the inspected theorems do not supply the claimed exact endpoint norms as their stated conclusions.

## Mathematical value — PASS

The Wiener norm of an idempotent is the exact \(\ell^1\) and \(\ell^\infty\) amplification of a spectral projection, a canonical harmonic invariant. Obtaining its exact dependence on the discriminant type, field characteristic and extension size is more than a finite table: it gives a two-class classification over all odd finite fields, an exact sparse-kernel count, a unitary-projector corollary, and asymptotic constants \(C_p/p\) and \(2/\pi\). These precise facts can inform stability and sharp operator estimates even without a claimed downstream theorem. A generic Fourier decay bound does not determine an absolute Fourier sum.

## Limits and reviewed evidence

The statement is restricted to three variables, odd characteristic, nonzero radius, and nondegenerate forms. Relevant full-text materials reviewed are Iosevich–Koh 2007 Section 3/Lemma 4, Iosevich–Koh 2008 Section 2/Lemma 9, and Green–Sanders 2006 introduction/Theorem 1.3. The explicit computational checks are described in `VERIFICATION.md` and implemented in `checker.py`. The classical quadratic Gauss and Salié identities are acknowledged; no claim of independent validation or exhaustive priority is made.

Self-review: passed. Independent audit: not yet performed.
