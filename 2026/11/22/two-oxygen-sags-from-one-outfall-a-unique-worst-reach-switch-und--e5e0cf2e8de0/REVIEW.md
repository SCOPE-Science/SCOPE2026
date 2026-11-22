# Scientific review

## Correctness — PASS

The governing equation, sign conventions, continuity at the interface, strict rate order and input regularity are explicit. On a constant-rate reach \((e^{rt}D')'=e^{rt}f'<0\), so there can be only one interior local maximum. Nondecreasing fractional decay hazard makes \(U/f\) strictly increasing, yielding one boundary cutoff. Positive-solution comparison makes the downstream peak strictly decrease as the interface moves, while its endpoint limits put it on opposite sides of the unchanged upstream maximum. The exact exponential example and its six-decimal crossover bracket were independently replayed using `verify.py` with rational remainder bounds. General claims are proved analytically, not extrapolated from tests.

## Originality — PASS on inspected evidence

The closest material is the 2021 numerical hydrodynamic and reaeration paper by Wu and Yu, the 2022 reach-based water-quality model by Pathak et al., and the 2025 variable-parameter analysis by D'Agostino and Eberl. Their inspected text does not state the strict log-concave-input phase diagram and unique worst-sag site switch for a single outfall and step decrease of reaeration. Two published mathematical comparisons have different mechanisms: the two-outfall sag paper adds a pollutant source and the aerator-placement paper resets the oxygen-deficit state. No same-claim or stronger covering theorem emerged from the recorded queries. This is a best-knowledge comparison, **not proof of historical uniqueness**. Older reach-by-reach engineering analyses and the inaccessible full text of Arora and Keshari (2022) remain residual risks.

## Value — PASS

The exact classification resolves a natural monitoring issue: the number of observed oxygen minima need not equal the number of pollution sources, and even when two minima persist, the globally worst location can switch back upstream as a low-reaeration reach begins farther downstream. This is not merely recomputation of the classic one-peak formula: it covers a class of nonexponential inputs under a stated hazard condition, proves a sharp double-sag window and identifies the unique global-worst-site crossover. These facts are useful as a structural benchmark for interpreting reach-resolved monitoring, though the idealized model does not replace field calibration.

## Limitations and closest comparisons

Only a single monotone oxygen-demand input and one sharp reaeration-rate drop are covered, not arbitrary catchments, smooth heterogeneous hydraulics or oxygen-limited biochemistry. Comparison sources include DOI:10.1155/2021/6663696, DOI:10.1002/lno.12079, DOI:10.1137/23M1616406 and the two separately identified published oxygen-sag/aerator mathematical results in `RESULT.md`. Other engineering analyses could contain an equivalent special case; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
