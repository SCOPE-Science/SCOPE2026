# Scientific review: antipodal-occupancy convolution rank on \(Q_8\)

## Correctness — PASS
The exact quaternion decomposition proves \(\operatorname{rank}L_f=K(s)+2r(d)\) with four Walsh scalar blocks and one two-dimensional Fourier block. The sole nontrivial determinant is \(\sum_{t=0}^3d_t^2\). A singleton antipodal pair fixes \(d_t=\pm s_t\ne0\), while a doubled pair imposes \(s_t\ne\pm d_t\); the proof exhausts all possible scalar Walsh support sizes and isotropic/nonisotropic determinant alternatives. The constructive argument supplies all permitted cases, including the cyclotomic and square-root witnesses needed when there are no doubled pairs. The exclusion argument is algebraic, not an inference from exhaustive random examples. Independent in-code implementations, **not independent external auditors**, checked 64 canonical exact witnesses and 1,148 regular-matrix realizations across all 255 supports. The tests include exact group multiplication and explicit rank calculations.

## Originality — PASS under bounded comparison
Alagic–Russell, *Uncertainty Principles for Compact Groups* (arXiv:math/0608702, 2006), gives the general rank-weighted lower bound, not a support-geometric classification. Stanković–Moraga–Astola (AAECC 12, 2001, §2.4, Table 1) provides the Q8 Fourier transform, which is an important prior proof ingredient but not this support/rank census. The published binary-polyhedral spinor coefficient zero-set theorem classifies certain rank-two cases and those outcomes are acknowledged as already covered. Existing exact S3 and D10 Fourier-rank profiles do not imply the Q8 table. Searches for equivalent formulations, stronger results and exact tables in relevant public records and the relevant related research found no dominating result; an older unindexed equivalent calculation remains a priority risk. The new claim is the full fixed-support and full-rank combination of these constraints, not the known transform or individual rank-two cases.

## Value — PASS
This is a complete natural uncertainty/rank profile for the smallest nonabelian Hamiltonian group. It resolves every rank realization for all 255 supports, identifies the intrinsic four-antipodal-pair geometry, and separates supports of equal cardinality whose convolution kernels behave differently. In particular, the rank-two boundary at four and six taps depends on antipodal occupancy, not only the number of nonzero coefficients. This is a substantive structural classification rather than a single arbitrary numerical slice. Limits: complex weights only, no conditioning or larger-group theorem, and no independent external validation.

## Sources and risks
- Alagic–Russell, 2006, https://arxiv.org/abs/math/0608702 ; full-text introduction, Theorem 2 and finite-group consequences checked.
- Stanković–Moraga–Astola, 2001, https://web.cecs.pdx.edu/~mperkows/CAPSTONES/Quaternion/fuxcxlltext.pdf ; §2.4, transform table and rendered page inspected.
- Published binary-polyhedral spinor coefficient classification, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spinor-coefficient-zero-sets-and-projective-rigidity-across-fini--502b53e637a6 ; complete accessible RESULT.md compared.
- Nearby but non-dominating S3 and D10 exact-rank claims compared in the relevant related research. Equivalent unindexed quaternion-convolution calculations remain the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
