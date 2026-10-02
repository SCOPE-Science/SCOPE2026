# Independent mathematical audit — 2026-10-01

## No transfer-killed 2-torsion at five points on Theta_(2,3,4): ordered H2 torsion-free with rank between 3 and 189

**Disposition:** failed.

The no-torsion headline is mathematically correct but already follows from a published general two-dimensional model; the additional ordered-rank interval was not freshly reconstructed from actual generated matrices.

## Correctness

**UNRESOLVED** — The structural no-torsion conclusion is independently sound: Świątkowski constructs a 2-dimensional cube-complex deformation retract for the unmarked five-point configuration of a theta graph with two branched vertices, and the marked/ordered configuration is a finite cover of that 2-complex, so its top H2 is a subgroup of a free cellular C2 and hence torsion-free. However, the additional package statement 3 <= rank H2 <= 189 was not independently reconstructed from the actual chain matrices this round: the committed scripts generate intermediate mats.pkl, collapse_state.pkl and ordered matrices that are not themselves deposited, while HOMOLOGY.txt records an obsolete exact-rank assertion. A saved modular-rank log is not enough under this audit standard.

## Originality

**FAIL** — The headline absence of 2-torsion is mechanically implied by Świątkowski's earlier general 2-dimensional deformation-retract theorem for graph configuration spaces, pulled back to the ordered finite cover.

## Scientific value

**FAIL** — The principal negative answer—no ordered H2 2-torsion on this theta graph—is a routine consequence of the already-published two-dimensional model. The remaining rank statement is only a broad interval and was not freshly certified, so it does not supply a separately motivated exact invariant.

## Sources checked

- Jacek Świątkowski, Estimates for homological dimension of configuration spaces of graphs, Colloquium Mathematicum 89 (2001), Theorem 0.1.
- An and Knudsen, On the second homology of planar graph braid groups, Journal of Topology 15 (2022).
- An, Drummond-Cole and Knudsen, Subdivisional Spaces and Graph Braid Groups, Doc. Math. 24 (2019).
- Resultary search including the earlier theta-graph H2 record and the audited record.

## Residual risks

- The rank interval remains unverified in this round; the scientific rejection rests independently on decisive prior coverage of the main no-torsion claim.
