---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the final theorem for every integer r>=2 and all real thresholds X->infinity. Accepted positive canonical words are exactly 1(1|0^r)*. The rightmost complete 0^r tile is the least valid lexicographic carry in any non-all-ones word U0^r1^t; its replacement U1 0^{r floor((r-1+t)/r)}1^{(r-1+t) mod r} gives the exact gap H_r(t)=(2^{r-1}-1)2^t+2^{(r-1+t) mod r}. The all-ones word 1^n has cross-length successor gap 2^{n mod r}, and 0->1 contributes 1. The wrap case for a=(r-1+t) mod r=r-1 yields H(t+1)-H(t)=(2^{r-1}-1)(2^t-1), zero only at t=0; other cases have strictly positive increments. Every H(t) occurs using U=1^m. For each n, rightmost-block factorization with nonempty accepted prefix U gives exactly T_r(n-r-t-1) starting words of class t, and the single all-ones exception; summing gives T_r(n-1). Primitive 1/r-tile renewal recurrence has Perron root lambda^r=lambda^{r-1}+1. The fixed terminal-suffix class has complete-shell ratio lambda^{-(r+t)}. For arbitrary prefix-restricted subtrees (including a partial zero tile) only finitely many residual states exist; completing a residual tile costs a fixed state-dependent c bits before both the unrestricted and fixed terminal-suffix tiling counts. Thus their ratio has the same lambda^{-(r+t)} limit, with uniformly bounded PF error; binary initial intervals partition into at most n such subtrees, while all preceding complete shells give Omega(lambda^n) points. This extends the limit to arbitrary X, not merely powers of two. Boundary power gaps have O(n) occurrences. Both t=0 and 1 yield 2^r-1; the remaining masses are lambda^{-(r+t)} and sum to 1 by lambda^{r-1}(lambda-1)=1. The proof does not claim ordinary spatial density or a distribution conditioned on all integer sites.

## originality

PASS

Best-of-knowledge originality for the all-r (especially r>=3) exact successor/gap spectrum, every finite binary shell and normalized all-cutoff return law. Prior published October 25, November 2 and November 8 Baum-Sweet findings give strong overlapping complete solutions for r=2, including its gap spectrum, exact dyadic histograms and dyadic limit, so that special case is not novel and is explicitly not credited. Those statements do not contain or imply the r>=3 formulas or the arbitrary-X convergence. Merta 2018 defines precisely b_r and studies l_n^(r), but his Theorems 5.1/5.2 concern run bounds and nonregularity, while Theorem 5.10 classifies differences of u_n^(r), the positions in a formal composition inverse, not l_n^(r). Allouche-Yao Example 9 computes an unrelated opacity invariant. OEIS A060142/A086747 give the r=2 index set and recurrence, not all-r gap laws. Generic PF renewal methods supply a technique but not a pre-existing explicit target theorem. No inspected work covers the complete all-r final statement; inaccessible/unindexed historical sources remain a risk.

## value

PASS

The generalized Baum–Sweet family is a canonical, naturally parameterized collection of sparse automatic indicator words already studied in Merta 2018. For the support of each member, the precise recurrence-gap set, every finite digit-shell multiplicity and normalized return-time distribution are natural invariants, especially because the ordinary symbol-1 spatial density vanishes. Extending the complete r=2 solution to all zero-run moduli r>=3 requires a genuine r-dependent carry formula and primitive order-r tiling/Perron calculation rather than a mere renaming of the Fibonacci constants; the all-real-cutoff law also establishes robust relative frequencies beyond dyadic windows. These exact data can be used in further work on sparse automatic-word recurrence and regular-language renewal. No claim of a broad mixing theorem or major downstream application is needed. The previously published r=2 slice alone has no independent value as a new contribution; the mathematical value resides in the uniform full-family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
