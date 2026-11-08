# Mathematical review

## Correctness

**PASS.** The proof computes the normalized-kernel matrix element from the shift's geometric Taylor coefficients, uses positivity of real kernel overlap to reduce to collinear points, and exploits input/output interchange to exclude the non-dominant branch. The resulting exact rational function has a denominator positive on the full domain. Its derivative numerator is a strictly decreasing quartic with opposite endpoint signs, proving exactly one maximizing root and a closed circular range. The signs at the distinguished point \(k=\sqrt{1-q^2}\) yield the alignment threshold and the envelope derivative yields the complete unique damping optimizer. Singular-endpoint expansions are derived after rescaling the double roots. Exact symbolic algebra and additional finite numerical diagnostics have been executed from the included standard-library checker. Finite experiments are not used as infinite proofs.

## Originality

**PASS, best-knowledge assessment with explicit residual risk.** The closest primary preprint, Bhattacharya–Patra, arXiv:2601.02334v2, Section 3.3, already gives disk geometry and a two-branch optimization expression for precisely these weights. Those statements are treated as prior. Its Remark 3.20 supplies derivative candidates but does not give the unique quartic root, global alignment threshold, sharp \(\beta\)-minimization, or two boundary expansions. The pertinent Sections 1 and 3 of Mahapatra et al., arXiv:2608.21723, concern related \(q\)-Berezin inequalities and a Bergman weighted-shift family. Database comparisons found closer work on ordinary numerical radii of geometric shifts and on \(q\)-numerical ranges, but those invariants use different test-vector constraints. There is still a nonzero risk of older Berezin-radius literature implying the result through an alternate parameterization; the search is not a uniqueness proof.

## Mathematical value

**PASS.** The motivating preprint leaves a natural continuous family of explicit two-branch maximizations. The new structural theorem identifies the only maximizing kernel pair, provides a sharp transition between antipodal and aligned geometry, and solves the natural operator-design problem of choosing geometric damping to minimize a prescribed-overlap Berezin radius. The parameter region where stronger damping initially makes the radius worse is not apparent from circularity of the range or a generic norm bound. Two sharp boundary expansions quantify the endpoint regimes and make the invariant usable without repeated optimization. The results concern a natural compact weighted-composition family, not an arbitrary finite slice.

## Closest literature and limitations

The two fully relevant examined sources are arXiv:2601.02334v2 (Sections 2, 3.3 and conclusion) and arXiv:2608.21723v1 (Introduction and Section 3 weighted shifts). The first is the exact starting family; the second uses Bergman kernels and different coefficient factors. Residual risks include an unlocated general maximization theorem for prescribed-overlap Szegő-kernel tests. The claim excludes complex damping and general real-weight sequences. Independent review is not supplied.

Self-review: passed. Independent audit: not yet performed.
