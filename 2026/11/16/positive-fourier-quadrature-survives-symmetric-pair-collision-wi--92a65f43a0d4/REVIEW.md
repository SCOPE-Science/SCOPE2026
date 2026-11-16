# Scientific review

## Correctness: PASS

The theorem is established for every odd \(N\ge3\) and \(\alpha\in[0,1/2]\), distinguishing the unique interpolatory weights below collision from their canonical merged limit at collision. Inverse cyclic Fourier summation derives all weights and exact moments; explicit cosecant inequalities establish positivity; a one-dimensional nullspace perturbation of the sampled Fourier matrix yields the exact singular slope. Supplemental execution of `check.py` returned 1,226 passed finite assertions. Finite checks are consistency evidence only, not a substitute for the infinite proof.

## Originality: PASS, with historical-priority risk

Closest inspected source: Yu–Townsend (2022), Section 4.1 and Theorems 4.1–4.2, treats general jitter and multi-site alternating constructions producing negative weights, plus broad norm estimates. Austin–Trefethen (2016/2017), Theorems 1–2 and Sections 3–4, treats general perturbed-grid convergence and confluent sampling, not this all-size positive two-site collision family or its singular slope. Direct scientific claim comparisons and semantic research-record searches found no covering statement. A general historic exact-quadrature or rank-two Vandermonde identity could imply this specialization and remains a risk; absolute historical originality has not been independently established.

## Mathematical value: PASS

The precise two-node deformation is a natural minimal stress test of general jitter-induced negative quadrature weights: it identifies a nontrivial family with exact positive integration through rank loss, all grid sizes, and quantifies the separating loss of Fourier reconstruction stability. The result is not a general interpolation convergence theorem and does not require one to be useful.

## Limitations

The statements apply to odd Fourier grids and symmetric inward motion of exactly two adjacent nodes; fixed-size singular asymptotics are not uniform in a joint limit. External historical priority and independent audit remain open.

Self-review: passed. Independent audit: not yet performed.
