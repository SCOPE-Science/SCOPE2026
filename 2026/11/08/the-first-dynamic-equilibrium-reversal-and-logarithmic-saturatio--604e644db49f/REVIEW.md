# Self-review

## Correctness (C): PASS

The claim uses the original ladder definitions, not a one-dimensional surrogate. The published equations (3.9), (4.2) and (4.4) are independently transcribed. The algebraic identity \((1-t)/(1+t)=q(1-q)\) follows exactly from the root polynomial and yields a controlled Lambert function asymptotic, with the normalization \(S_b=2b\rho_\star^{(b)}\). The numerical cutoff is certified through ten strict comparisons of **exact rational intervals**, with analytic trapezoid and Taylor bounds; there is no assumption that rounded numerical signs are exact. The checker was executed from its actual local path. The proof expressly distinguishes the finite cutoff from a global no-recrossing statement. Residual correctness risk is limited to potential unnoticed transcription or mathematical error, not an asserted external proof certification.

## Originality (O): PASS, with historical risk

The 2023 source (arXiv:2312.02747) fully derives and owns the underlying exact density formulas, the limiting values, and the numerical reversal interval implicit in its table (dynamic larger at \(b=5\), equilibrium larger at \(b=10\)). No credit is taken for these. Table 1 omits the close \(b=9\) case and does not prove the least integer crossing. The fully rational separation establishes that missing mathematical boundary. The same source proves only equilibrium convergence to one, without the quantified \(W(2b)\) and logarithmic deficit. The Lambert function asymptotic for the one-dimensional model is known in arXiv:2302.08852, but that article has different governing equations; the distinct ladder asymptotic is proved here. arXiv:2302.08791 is also one-dimensional. Searches of published mathematical records and original literature did not reveal an exact all-ten comparison or a two-row logarithmic rate; a later, unindexed equivalent derivation remains possible. This is a constrained priority judgment, not a claim that a search establishes uniqueness.

## Value (V): PASS

The paper compares two physically motivated probability ensembles and illustrates opposite orderings for separate blockade values, but leaves a narrow finite transition bracket unresolved. Certifying the *first* integer reversal at \(b=10\) is a natural sharp finite cutoff, especially because the difference at \(b=9\) is less than \(10^{-4}\). The independent asymptotic \(1-S_b\sim1/\log b\) quantifies the extremely slow approach to saturation and explains why the equilibrium model can differ markedly from the dynamic parking limit at large blockade. These jointly answer motivated questions directly prompted by the source's comparison, rather than introducing an arbitrary numerical slice.

## Limits and closest prior literature

Došlić–Puljiz–Šebek–Žubrinić (arXiv:2312.02747): known formulas and partial table, closest. Krapivsky–Luck (arXiv:2302.08852): already develops the Lambert-\(W\) mechanism in one dimension, not the two-row density. Došlić et al. (arXiv:2302.08791): earlier one-dimensional model. The current work neither proves a global uniqueness-of-crossing theorem for every \(b\ge10\) nor replaces independent peer assessment.

Self-review: passed. Independent audit: not yet performed.
