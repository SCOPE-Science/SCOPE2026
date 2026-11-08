# Self-review

## Correctness: PASS

The declared domain is \(d\ge2\), \(\alpha>0\), \(\lambda=(d+1)/2+\alpha\), \(\mu>\lambda+2\), \(\varepsilon>0\), with area-normalized harmonic eigenvalues. The two-term Euclidean transform is obtained from the algebraic residues of \({}_1F_2\) (DLMF 16.11.2, 16.11.8); the condition on \(\mu\) makes its competing oscillatory branch negligible at relative order \(z^{-2}\). The radial-to-spherical identity, exact Weber–Schafheitlin Bessel-square integral, exponential smallness of \(J_\nu\) below \(\nu/2\), and gamma-ratio expansion yield the stated coefficient, not merely its leading decay. The strict unique calibration scale follows from positive factors and monotonic dependence on \(\varepsilon^2\). Independent numerical tests compare the two radial transform terms, Bessel integrals, gamma ratios, and explicit circle Fourier coefficients at generic and tuned scales. Finite tests are corroboration only.

## Originality: PASS, subject to historical priority risk

The 2021 arXiv version of Hubbert–Jäger already *states* the all-dimensional first-order coefficient, so **no** novelty is ascribed to that leading term; the 2023 version places its even-dimensional proof as an open question. Neither full text gives the relative \(\nu^{-2}\) coefficient or its unique cancellation as a function of scale. Narcowich–Sun–Ward 2007 gives the general RBF/SBF transform and Sobolev comparison but not this exact two-term spectral law. DLMF gives the two universal special-function identities employed, not the parameter-specific assembled spectral cancellation. Searches of the public mathematical literature and related published research records did not identify a theorem with the same normalized second-order statement. Remaining risk: unsearched numerical kernel-calibration literature or an all-order special-function treatment might yield an equivalent formula implicitly.

## Mathematical value: PASS

The problem is to quantify finite-frequency bias in a widely used, compactly supported positive-definite spherical kernel relative to its leading Sobolev spectral power law. The result reveals an *identically absent* linear correction, computes the exact next coefficient for a continuous family of sphere dimensions and kernel smoothness parameters, and proves a unique geometric scale that suppresses the first nonzero curvature-frequency bias. This gives a directly interpretable criterion for kernel scale selection in high-degree spherical approximation and simulation. It is not merely a table of coefficients or a numerical fit; the cancellation has a complete exact parameter classification. No guarantee of finite-mode optimality or numerical performance is made.

## Sources and residual limits

Key primary inspections: Hubbert–Jäger arXiv v1 §§2–5 (especially 3.12, 3.17, 5.9 and its even-dimensional discussion), the 2023 open-access journal proof and concluding open question; Narcowich–Sun–Ward 2007 §§3–4; DLMF §16.11 and §10.22. The historical comparison distinguishes first-order coverage from the presently asserted two-term coefficient. Mathematical assumptions and the fixed-parameter nature of the remainder are part of the claim. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
