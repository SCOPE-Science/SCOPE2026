# Review of cyclotomic generalized Paley neighbor-sum dynamics

## Correctness — PASS

The exact graph and state-field assumptions are specified in `RESULT.md`. Translating by one on \(\mathbb F_p\) produces a single nilpotent chain for \(Z=S-I\); subgroup power-sum orthogonality forces the first nonzero nonconstant coefficient of the adjacency connection polynomial to occur at degree \(d\), with nonzero coefficient \(d/d!\). The resulting rank filtration is \(\dim\ker((A-dI)^t)=\min(dt,p)\), proving the Jordan block multiset. The iterate identity \(A^p=dI\) and the first derivative of \((d+X)^t-1\) supply every fixed-point count and the exact period spectrum. Three separately implemented finite checks passed: 15 adjacency matrix families, 89 subgroup-moment parameter families and an exhaustive \(7^7\)-state test on the seven-cycle endpoint. The proof, not finite enumeration, supplies all-parameter validity.

## Originality — PASS, with historical-priority risk

Lim–Praeger, arXiv:math/0605252 (2006), define the same graph family and analyze automorphisms and connectivity. Chandler–Sin–Xiang, arXiv:1401.8260 (2014), establish Smith groups only for ordinary quadratic-residue index two, explicitly excluded here. Podestá–Videla, arXiv:2310.15378 (2023), classify complex adjacency spectra of generalized Paley graphs using Gaussian periods; those data do not imply Jordan blocks after modular specialization. Targeted searches for cyclotomic modular adjacency, orbit counts, Jordan forms and equivalent circulant forms produced no controlling prior implication in the inspected material. A general modular circulant result not surfaced in the searches could still cover parts of this theorem, and independent priority review remains desirable.

## Mathematical value — PASS

The graph family is canonical in cyclotomic graph theory and includes connected noncycle members in infinitely many permissible parameters. The exact Jordan chain lengths, maximum period and two complete nonzero orbit populations explain how a prime-characteristic degeneracy controls the dynamics despite high graph symmetry. This is a complete natural family classification, not an arbitrary numerical slice or a direct restatement of a pre-existing graph spectrum.

## Limitations

The theorem does not classify generalized Paley graphs on extension-degree vertex sets or dynamics over state fields of another characteristic, and does not identify graph-automorphism orbits. Historical-priority completeness remains uncertain. Verification programs enumerate finite families and do not replace the proof. External independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
