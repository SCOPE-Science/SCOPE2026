# Independent Audit — 2026/09/16/006

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `49b7c826a392864c7b696d69e285ac144283fd62`  
**Audited current source tree:** `49b7c826a392864c7b696d69e285ac144283fd62`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — PASSED

PASS. For A_n={(x,y,z): x·y=0} in F_2^n x F_2^n x F_2, the density is exactly 1/2+2^{-(n+1)}, each x-fibre is H_y=ker chi_y, and the intersection over nonzero y is {0}. For rho<1/2 a Bohr set is the annihilator of span(Gamma), and B subset H_y iff y lies in span(Gamma); therefore the fraction of y covered is at most 2^{|Gamma|-n}, yielding |Gamma|>=n+log_2 c. These are valid elementary duality calculations. The record’s reproducibility paths are wrong (output/artifacts versus artifacts), but that is not the reason for scientific rejection.

## Originality — FAILED

FAIL. The construction is the canonical bilinear dot-product variety and its fibre hyperplanes/annihilators are immediate linear algebra. More importantly, existing bilinear Bogolyubov proofs already organize fibre annihilators using frequencies that vary affinely with the other coordinate: Bienvenu–Lê explicitly write (V_y)^perp as span(xi_1(y),...,xi_s(y))+U_y. The submitted observation therefore re-expresses a standard structural feature rather than introducing a new obstruction mechanism.

## Scientific value — FAILED

FAIL AS A STANDALONE RESEARCH FINDING. The exact rank lower bound is a one-line consequence of the size of span(Gamma), and the broad conclusion that “any trilinear Bogolyubov proof must use genuinely varying frequencies” does not follow: the example only rules out one fixed-Bohr-set uniformisation step on these raw fibres. At most it is a useful cautionary example for a proof attempt, not a publishable theorem at the claimed level.

## Independent checks

- recomputed the density exactly for general n
- proved B(Gamma;rho<1/2)=ann(span Gamma) and B subset H_y iff y in span Gamma
- derived the coverage bound 2^{|Gamma|-n} and the stated rank lower bound
- compared the claimed mechanism with published bilinear Bogolyubov fibre-annihilator formulas using affine frequency maps
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The rejection is on originality/scientific value, not the elementary finite-field calculation.
- The audit does not claim the exact sentence |Gamma|>=n+log_2(c) was printed verbatim before; the failure is that it is immediate from standard annihilator/fibre structure already central to the literature.
- The example does not exclude other fixed or averaged structures later in a trilinear argument, so the record’s universal methodological conclusion is too broad.
- Open-access full text was sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/16/006
- https://arxiv.org/abs/1711.05349
- https://arxiv.org/abs/1712.00248
- https://home.olemiss.edu/~leth/papers/Bilinear%20Bogolyubov.pdf

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
