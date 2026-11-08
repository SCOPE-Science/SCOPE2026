# Review of the three-line Heisenberg theorem

## Correctness
**PASS.** The group law, projection normalization, one-dimensional character count, and degree-\(p\) regular multiplicities give an exact dimension ledger. The nontrivial triple trace is reduced to the explicit quadratic central phase \(At^2+Bt\), and the cubic follows from a rank-three Gram determinant. Gershgorin gives strictly positive cubic roots for \(p\ge5\), while all six characteristic-three quadratic residues yield the stated real Gauss phases. The characteristic-three census counts every triple of cyclic subgroups with distinct projected directions, not individual generators. Standalone finite regular matrices and exact representative ranks agree. No finite calculation is treated as an infinite proof.

## Originality
**PASS under bounded primary-literature and indexed-record comparison.** Prior mutually unbiased basis results already provide the pairwise overlap; general finite Radon theory already supplies the Fourier-block language. The claim is the specific complete three-direction regular spectrum, the sharp rank transition, and its exhaustive \(36/72\) subgroup-triple count. The closest primary sources inspected were Šulc–Tolar (Heisenberg MUB construction), Ilmavirta (general finite-group Radon transform), and Blanchfield (dependent MUB configurations). The latter provides the most material risk around the characteristic-three geometry; dependence in small dimension alone is not asserted to be newly discovered. A possibly dominating general stabilizer-Gram theorem remains a residual historical-priority risk.

## Value
**PASS.** Three chosen noncommuting line directions define a natural limited-angle finite-group tomography problem. The theorem gives its complete normal-operator spectrum, precisely which Fourier information is recoverable, and an exceptional six-dimensional extra information loss at the smallest odd prime. The subgroup-triple census is complete over the natural parameter space; it is not an arbitrarily selected slice. No general multi-direction or optimal-conditioning result is claimed.

## Scope and independent checks
The precise statement, proof, and finite verification are in `RESULT.md`; `check_heisenberg.py` is executable. Independent validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
