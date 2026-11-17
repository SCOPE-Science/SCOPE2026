# Scientific assessment

## Correctness — PASS

For the Petersen graph \(KG(5,2)\), the exact local rule and ten-vertex encoding appear in `RESULT.md`. The `verify_kneser.py` certificate visits all \(4^{10}\) configurations for each threshold, explicitly establishes the full-state equalities \(F_1^{31}=F_1^{11}\) and \(F_2^5=0\), and computes the full transient-period table. The independent C++ algorithm constructs the Petersen graph in a distinct vertex representation, computes its full functional graph, removes indegree-zero vertices, and determines periods and transient depths in reverse order. The two counts match. The cycle-class and last-layer symmetry checks use all 120 graph automorphisms, not sample representatives or assumed orbit sizes. There are eleven-step and five-step witnesses. All claimed numerical populations and sharp cutoffs follow from exact integer computations, with no external data dependencies or infinite extrapolation.

## Originality — PASS, subject to historical-source uncertainty

The closest published three-state Petersen finite census works in a different \(3^{10}\)-element phase space, has period spectrum \(1,3,4,5,8\), and a sharp entry time six; it cannot cover the four-state spectrum and eleven-step depth. Four-state complete-tripartite results forbid period five by their graph-family-specific support reduction; Petersen is not complete tripartite. The 1991 full paper discusses arbitrary-color dynamics on square lattices and illustrates wave structures. The 2018 full arbitrary-graph paper gives specific three-color convergence and activity criteria rather than this four-state, labelled Petersen census. Indexed semantic search for the exact graph, refractory count, five-cycle, symmetry classes and two-neighbor extinction did not locate a dominating result. The 1978 original paper was accessible only by abstract and publication metadata. Unindexed finite computations remain a genuine residual priority risk.

## Mathematical value — PASS

Petersen is the unique smallest cubic graph of girth five, hence a canonical nontrivial feedback network for excitable waves. Four-state dynamics is the first refractory extension beyond the widely studied three-state model; comparing one and two contacts is the natural local excitation-threshold change on this degree-three graph. The classification demonstrates three distinct geometric wave types, survival of genuine five-period oscillations at refractory length four, a sharp eleven-step transient, and complete extinction on raising the threshold. It supplies a complete labelled finite-state benchmark for refractory-length/threshold sensitivity, not a routine substitution into the three-state theorem or a narrow unmotivated numerical slice.

## Evidence and limitations

The six-file scientific package plus two independent programs, two captured check outputs and the full census are embedded together. Sources include Greenberg–Hastings (1978); Fisch–Gravner–Griffeath (1991, full text); Durrett–Griffeath (1993); Gravner–Lyu–Sivakoff (2018, full text), public Petersen graph descriptions, and the two closest published finite-state comparisons. Exact enumeration is a finite proof, not a noncomputational structural theory for every cubic graph. Earlier unindexed publications may affect historical priority. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
