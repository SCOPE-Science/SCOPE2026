# Scientific review

**Correctness: PASS (same-model).** The source RKL2 polynomial, direct graph-matrix entry classification, Laplacian spectral bound and triangular-graph incidence spectrum constitute a complete analytic proof. A negative edge entry is calculated exactly at the stable step \(h=7/30\) for \(J(5,2)\). A sign input proves the nonlinear cube failure. The standalone exact-rational checker is a finite diagnostic, not an infinite proof.

**Originality: PASS (qualified).** The original stabilized method and its one-dimensional maximum-principle proof are prior work. Full published comparisons show that an earlier degree-two Taylor theorem is restricted to complete multipartite graphs, and a broader triangle-count theorem concerns products of *real* Euler factors, which cannot equal the RKL2 second-order polynomial. The new exact all-regular spectral-to-positivity criterion and triangular-graph all-n ratio are not logical corollaries of those statements. A related 2025 full text and unindexed specialist literature remain historical-priority risks.

**Value: PASS.** Positivity and energy stability govern different numerical safety properties. The precise \(3/2\) asymptotic gap on natural strongly regular graphs, the finite witness and the exact Allen–Cahn Strang counterexample help identify how a stable explicit solver may violate a discrete maximum principle. Applicability is limited to the stated two-stage network setting; no efficiency or general PDE claim is made.

Closest comparisons: Tan–Aslam–Bertozzi (2026 and 2025), exact degree-two Taylor positivity on complete multipartite graphs (2026), and optimized two-forward-Euler positivity on regular graphs (2026). See `RESULT.md` and `AUDIT.json` for source URLs, material inspected, implications and residual risks.

Self-review: passed. Independent audit: not yet performed.
