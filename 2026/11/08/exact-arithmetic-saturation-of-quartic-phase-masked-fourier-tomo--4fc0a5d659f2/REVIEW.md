# Self-review

## Correctness: PASS
The entire claim is an exact linear map statement, not a nonlinear phase-retrieval statement. The proof first applies character orthogonality in the Fourier-index variable, reducing the rank to the complex Vandermonde rank on each nonzero cyclic diagonal, with Hermitian paired diagonals counted over the reals. The nonzero-phase polynomial identity \(j^4-(j-d)^4=d^4[4(j/d-1/2)^3+(j/d-1/2)]\) is algebraic. The cubic fiber count uses an elementary quadratic-character sum, the diagonal collision count and the critical values, with the case \(p\ge5\) and every boundary \(1\le r\le p\) included. The dimension and full kernel follow without numerical inference. `CHECK.py` performs independent finite examples. Risks: numerical tests are not proof for larger primes; the analytic proof bears that responsibility.

## Originality: PASS relative to inspected evidence
The closest literature concerns randomized coded-diffraction reconstruction, generic polynomial value sets and different finite Fourier/Gabor measurement orbits. The claims of a preceding quadratic-mask rank law, cubic-plus-quadratic offsets and quartic Gabor/window analyses were compared by objects and implications rather than only titles. No inspected statement forces the \(r\)-dependent quartic-slope rank with its exact cubic-fiber kernel. The elementary cubic character identity and generic Vandermonde method are standard and not claimed new. Residual risk: equivalent deterministic-mask linear-algebra or older cubic value-set literature might exist beyond inspected material; independent priority verification remains absent.

## Mathematical value: PASS
A deterministic polynomial phase-mask ensemble can add \(p-1\) independent real matrix directions per full diffraction profile, but stops at the explicit arithmetic index \((2p+\chi_p(-3))/3\), an unavoidable loss of approximately one-third of the Hermitian operator space. Knowing the exact 1/2/3-fold indistinguishable diagonal classes and an explicit nullspace is directly useful for designing and diagnosing structured lifting measurements. This is not merely recomputing a polynomial image: it identifies a sharp, matrix-recovery obstruction for all mask counts and both prime congruence classes.

## Scope and risk
Exact full Fourier profiles, consecutive quartic slopes and prime cyclic length \(p\ge5\). Not a claim about stability, arbitrary slopes, or phase ambiguity of pure signals. Primary sources and comparisons are documented in `RESULT.md` and `AUDIT.json`. Relevant abstract-only sources are not treated as full-text exclusions. The review is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
