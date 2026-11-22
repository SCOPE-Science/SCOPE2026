# Scientific review

## Correctness — PASS

The statement uses precisely the minimum-cardinality *ordinary* dominating sets of the Pappus point–line incidence graph. The coverage inequalities force each optimum five-set to have point/line split \((3,2)\) or \((2,3)\), and equality forces exactly nine geometric configurations of each type. The point/line concurrence table is proved case-by-case; it supplies the shattering criterion, exact polynomial, zero-concurrence reconstruction and two-level homology. A five-versus-thirteen first-query split bounds online dimension by three, and a geometrically explicit complete tree attains three. Independent Python and C++17 exhaustive programs reproduce the classification and trace counts. No infinite-graph extrapolation is asserted.

## Originality — PASS within inspected evidence

The closest primary texts address Pappus configurations and affine completion (Stroppel 2018), cyclic-cover automorphisms of the Pappus graph (Potočnik–Toledo 2020), and generalized Pappus graphs (Biswas–Das 2022). They establish the underlying graph but do not assert its exact optimum-domination membership design or shattering dimensions. Published work on the Pappus graph's minimum locating-dominating six-sets reconstructs the graph by *code-code intersections*, a different class and relation from the present ordinary dominating five-sets and vertex-pair zero concurrence. Results on minimum dominating sets of forests do not apply to this cubic graph. An unindexed equivalent theorem remains possible; no independent historical-priority certification is claimed.

## Value — PASS

The theorem connects three motivated invariants of a distinguished symmetric incidence graph: a complete optimum-domination classification, exact self-reconstruction by the optimum design, and a sharp strict static–adaptive membership-query gap with integral shattering topology. The classification is structural and self-contained, not merely a numerically recomputed domination value; it gives explicit explanations for all 27 forbidden pairs, all 126 shattered pairs, and the no-triple obstruction. The finite scope is stated plainly.

## Closest literature and limitations

- Stroppel, *Generalizing the Pappus and Reye configurations*, Australas. J. Combin. 72 (2018), 249–272: affine completion, automorphisms and polarities, not these dominators.
- Potočnik–Toledo, *Finite cubic graphs admitting a cyclic group of automorphisms with at most three orbits on vertices*, arXiv:2003.05186 (2020-03-11): cubic symmetry classification, not domination membership traces.
- Biswas–Das, *A generalization of Pappus graph*, EJGTA 10 (2022), 345–356: generalized graph definition and automorphisms, not this concept family.
- Petr–Portier–Versteegen, *On the number of minimum dominating sets and total dominating sets in forests*, JGT 106 (2024): forest-specific bounds, logically inapplicable to this cubic graph.

The proof and checks establish this one graph only. Potential historical overlap in unindexed material remains unresolved, and no independent audit has been completed.

Self-review: passed. Independent audit: not yet performed.
