# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `SCOPE-20260912-053`

An independent scientific audit on 2026-10-01 rejected the final claim for publication as a validated finding.

- Correctness: **FAIL** — The central local Hopf computation is reproducible: independently solving the filed fixed-point equations gives the stated branch values at rho=1,2,2.545339,3,4 and the critical eigenvalue approximately +0.217293 i/ms (34.5833 Hz); a fresh RK4 replay at rho=4 reproduces means 60.217/32.497 Hz, amplitudes 39.302/53.901 Hz, frequency 36.6667 Hz and phase -1.2902 rad. However, the final claim is stronger: uniqueness of the physical branch over the full continuum [0.1,10] is supported only by finitely many Newton starts/probed points, and asymptotic stability of the limit cycle is inferred from persistent integration without Floquet or an equivalent basin/stability certificate. Those methods do not prove the stated global uniqueness/stability assertions.
- Originality: **PASS** — The exact fixed-budget heterogeneity-ratio threshold and parameter tuple were not found in Resultary or the inspected primary MPR literature. The general MPR reduction and QIF bifurcation framework are established, but the stated numeric threshold requires a separate computation. Best-of-knowledge exact-instance originality therefore passes, subject to normal search limitations.
- Scientific value: **FAIL** — The source tree shows that the final parameter vector was selected after scanning a grid of JEI, JIE, etaE and etaI candidates for the desired baseline/Hopf behavior. The exact rho threshold is therefore a post-selected parameter slice without an independent argument that this tuple, fixed-sum path, or threshold is a natural classification boundary or broadly needed invariant. It is useful exploratory modeling, but not a sufficiently motivated mathematical gap under the shared value standard.

The original research files and computational evidence are retained for reproducibility and historical inspection. Their presence does not constitute validation. See the dated independent-audit files for the full source comparison and residual risks.
