# Scientific review: one-way crossing and sliding capture

## Correctness — PASS

The exact interface normal components are \(1-y\) on the left and \(a+y\) on the right. Strict left-to-right and strict right-to-left crossings require disjoint parameter ranges \(a>-1\) and \(a<-1\). No orbit consisting solely of crossing segments can close; each affine half-plane vector field is a saddle and has no nonconstant periodic orbit on its own. At the advertised example parameters, exact diagonalizations yield left and right arcs both traveling from upper to lower contacts in times \(6\log\varphi\) and \(4\log\varphi\). The lower contact has inward one-sided normals, and the upper has outward normals. The Filippov sliding field has an exact rational expression and exactly one attracting root in the entire attracting sliding region. The symbolic checker and additional interior diagnostics passed. Tangency and sliding-cycle questions are explicitly excluded from the nonexistence theorem.

## Originality — PASS within inspected evidence

The 2023 originating paper displays a closed algebraic two-arc level-set loop, identifies a region where it calls that loop a limit cycle, and explicitly uses the Filippov convention. The new claim checks the previously unaddressed necessary orientation of normal velocities and proves there is no **crossing** periodic orbit anywhere in that entire two-parameter example family. The originating upper-bound theorem remains untouched; only its sharpness example is at issue. Llibre–Valls (2021) exclude crossing cycles in two-zone **Hamiltonian–Hamiltonian** saddle systems; that does not cover this Hamiltonian–non-Hamiltonian pair because the right trace is \(1\). Phatangare–Masalkar–Kendre (2024) study nilpotent centers with saddles rather than this pair. The indexed closest three-zone Hamiltonian cycle and two-zone focus-annulus results do not imply the one-way normal barrier in the exact published family. Relevant publication text and scientific claims, not title similarity, were compared. Unindexed discussions and subsequently issued corrections that were not found remain a priority risk.

## Value — PASS

This is not merely another parameter example or a restatement of the published upper bound. It identifies a physically decisive dynamical obstruction: matching two invariant algebraic curves can create a closed geometric loop whose two halves are both oriented the same way. The result distinguishes an actual Filippov crossing orbit from an algebraic construction presented as a sharpness witness, proves an entire parameter family cannot contain such cycles, and identifies the exact alternative sliding-capture mechanism at the stated numerical witness. The two distinct exact flight clocks make the obstruction reproducible in original time. Such orientation checks are necessary when proving existence of cycles in nonsmooth differential equations.

## Primary sources and limitations

- García, Llibre, Pérez del Río and Pérez-González, *Axioms* 12 (2023), 342, equations (36)–(38) and Section 4: full online text of the relevant result and its example inspected.
- Llibre and Valls, *Symmetry* 13 (2021), 1128: the two-Hamiltonian-saddles hypothesis of Theorem 3 is inapplicable.
- Phatangare, Masalkar and Kendre, arXiv:2407.15163 (2024): the investigated nilpotent-center/saddle systems have different dynamics.

No conclusion is made for general sliding limit cycles, for fold points, or for two-zone affine systems with other off-diagonal sign patterns. The global sliding attraction statement is confined to the indicated sliding half-line at the specific benchmark parameters. Independent assessment is pending.

Self-review: passed. Independent audit: not yet performed.
