# Scientific review

## Correctness — PASS

The random-walk increment process is exactly a symmetric swap chain with a boundary spin flip and an inert second-walk choice. Direct conditional expectation yields the finite tridiagonal first-moment operator \(I-L_m/(2m)\), including the terminal coefficient and \(m=1\) case. Its half-integer discrete-cosine eigenvectors diagonalize the operator; orthogonality supplies positive normalized spectral weights. The explicit Green vector solves the full finite difference equation, giving the integrated-correlation identity. Fixed-mode asymptotics plus a summable weight bound prove the cubic scaling limit at all fixed scaled times, including zero; strict decay of the limit proves threshold asymptotics. The code performs 21,378 exact/finite numerical diagnostic assertions, with no use of simulation as a substitute for the infinite proof.

## Originality — PASS (best-knowledge, with residual risk)

The closest source, Wei [1], poses the endpoint exponent \(\beta\) in Conjecture 4 and supplies only numerical fits around \(3\), not the exact finite-time series, exact polynomial sum or limiting profile. The source's own code samples an extra inert position; the finite-time normalization of that convention is handled explicitly by the present theorem. Santos–Schütz [2] treats a related exclusion process but focuses its main exact correlations on a semi-infinite relaxing chain; its statements do not yield this finite-volume stationary discrete-time endpoint result without a separate reduction and diagonalization. The finite-reservoir work [3] concerns different boundary rules and macroscopic limits. Targeted published-research and index searches identified no same-observable coverage. Residual risk: classical finite-chain exclusion spectral methods may contain an equivalent formula under other terminology, and historical uniqueness is not proved.

## Value — PASS

The new quantitative statement resolves the walk-endpoint half of an explicitly posed two-exponent problem arising from simulations of a nontrivial percolation/planar-map representation. Determining \(\beta=3\) together with a full decay curve, explicit endpoint-threshold constants and an exact integrated correlation goes beyond a routine model restatement; it provides a benchmark that separates endpoint transport from the still-open crossing-event behavior. The reduction shows concretely why a single boundary reservoir produces cubic single-update decorrelation despite bulk local swaps.

## Sources and limitations

Wei, arXiv:2610.03730v1 (Sections 4–6, Appendix A, and public implementation); Santos and Schütz, Phys. Rev. E 64 (2001), 036107 (full OA text); Franco, Franco and Gonçalves, arXiv:2604.02579 (abstract and scope). The result assumes the terminal free-end flip, initial fair independent increments, and the precise update clock. It does not prove crossing decorrelation, independent scaling limits or overall mixing. The strongest residual priority risk is an unrecognized classical equivalent stationary SSEP finite-volume mode expansion.

Self-review: passed. Independent audit: not yet performed.
