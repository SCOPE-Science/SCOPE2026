# Independent Audit — 2026/09/12/087

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `f5f9d3fc06c7aab47cbe864c905d21957f238ebb`
- Disposition: **FAILED**

## Correctness

**PASS** — The disproof mechanism is sound. Ferrari-Fontes compute a positive fixed-point current diffusion coefficient |p-q| rho(1-rho)|1-2rho| away from density 1/2, giving linear-in-time variance on the infinite line. For t_m=floor(log(m+1)) and a coupling window R_m of order log^2 m, the record's hypergeometric/binomial initial mismatch and finite-propagation error both vanish, while the fourth-moment truncation error is o(1). Thus the torus fixed-bond variance inherits a positive linear lower bound along the displayed sequence, which indeed violates any uniform C t^(2/3) estimate.

## Originality

**FAIL** — The decisive off-characteristic fixed-bond linear variance is already the main content of Ferrari-Fontes. Once that theorem is known, transferring it to a growing torus for logarithmic times by a finite-speed/local coupling is a standard approximation argument. The record does not identify a new KPZ crossover or finite-size law.

## Scientific value

**FAIL** — The construction correctly diagnoses that the proposed uniform theorem forgot the distinction between fixed-bond and characteristic current. That is a useful target sanity check, but scientifically it is a direct corollary of the classical fixed-point diffusion result combined with routine local convergence, not a substantial new finding.

## Sources

- Current fluctuations for the asymmetric simple exclusion process (P. A. Ferrari; L. R. Fontes): https://doi.org/10.1214/aop/1176988731 — Computes the equilibrium current diffusion coefficient through a fixed point as |p-q| rho(1-rho)|1-2rho|.

## Limitations

- The audit did not attempt to optimize the torus coupling constants; only their asymptotic decay is needed for the counterexample.
- The correctness pass concerns falsity of the proposed uniform bound, not a sharp finite-volume crossover theorem.

Repository evidence was read only. Open-access/preprint literature was checked first; no Oxford Download was required. No GitHub write or dispatcher completion/report action was performed by this audit chat.
