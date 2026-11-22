# Scientific review: trace-zero character-variety boundary

## Correctness — PASS

Cayley–Hamilton and the matrix relation imply \(A^2B^2=-I\). If \(\operatorname{tr}A\ne0\), recovering \(A\) from \(A^2\) forces commutativity with \(B\); in the zero-trace case \(B=\pm I\). The product \(AB\) is regular semisimple with eigenvalues \(i,-i\), giving an **exhaustive** normal form with parameters \(t,u,v,w\) and \(u^2+vw+1=0\). The residual torus has weights \(+2,-2\) on \(v,w\); its invariant ring is the Laurent polynomial ring in \(t,u\). Formula-by-formula trace computations and the explicit Laurent inverse prove the embedding. Exact SymPy checks passed, including a nongeneric parameter. The finite checks corroborate, but do not replace, these universal arguments.

## Originality — PASS, with residual priority risk

The source's §5.2 gives only the boundary matrix identity and explicitly leaves its GIT classification open. The new surface isomorphism, ideal in **all seven traces**, and positive-dimensional fibers of the four-trace map are not stated or implied by the source's open-locus equation alone. The 1997 study supplies qualitative component/rationality results; the 2016 study supplies global \(E\)-polynomials, neither the same boundary trace equations. Semantic-record comparisons for the claimed group, equation, aliases and cylinder found no covering result. Residual risk: an unindexed or differently formulated special-slice calculation may precede the explicit statement.

## Value — PASS

An explicit open problem asked for complete matrix and quotient geometry at precisely this hypersurface boundary. The answer determines the actual smooth irreducible reduced divisor rather than mistaking its smaller projected curve for the full two-dimensional formal four-trace slice; it computes its coordinate ring, all seven trace coordinates, and the exact fibers of the deficient coordinate projection. These are structural geometric invariants required to describe the marked character variety, not a substitution or arbitrary one-point calculation.

## Closest literature and restrictions

Chen, arXiv:2611.08513, §5.2, is the immediate unresolved boundary problem. Benyash-Krivets–Chernousov (1997) covers global representation geometry; Baraglia–Hekmati, arXiv:1602.06996, covers whole-variety arithmetic and \(E\)-polynomials. No claim is made about an embedded nonreduced structure, positive characteristic or independently certified priority. The calculation is self-contained in the complex reduced GIT setting.

Self-review: passed. Independent audit: not yet performed.
