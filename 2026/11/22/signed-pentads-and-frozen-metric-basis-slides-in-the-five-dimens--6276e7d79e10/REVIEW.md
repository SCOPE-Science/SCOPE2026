# Scientific review: signed metric bases of the five-cube

## Correctness — PASS

The statement is a finite-graph theorem with a complete structural proof, not an inference from sample computations. The sign-difference identity is checked coordinatewise; every nonzero ternary kernel vector corresponds to a genuine unresolved pair of cube vertices. The three-landmark lower bound uses five sign-matrix columns but only four signed column types. Antipodal lifting is justified by row negation and cannot cause collisions between chosen classes. A four-even-vertex resolving set cannot contain a distance-four pair (duplicate-square-signature or checkerboard ternary witness), and among the remaining normalized weight-two triples the triangle and star cases are explicitly separated. In the star case the equation \(\delta_m=2\delta_i\) together with ternarity makes the kernel trivial. Unique pentad completion and exact twelve-choice move classification then give every configuration, every edge, and the shortest-path formula. The absence of slides follows from all allowable replacement distances being two, three, or five.

Two independently implemented verifiers, `code/check_direct.py` and `code/check_quotient.py`, give the recorded figures using respectively direct pairwise Hamming signatures and the ternary-kernel/antipodal model. The direct verifier tests every one of the 35,960 candidate four-sets and performs exact graph BFS; the quotient verifier tests every one of the 1,820 distinct even-class four-sets. The packages do not claim that finite sampling proves an all-dimensional statement; the theorem is exclusively about \(Q_5\).

## Originality — PASS, with historical-priority limitation

The constrained-linear-system test for Hamming resolution, the minimum dimension of \(Q_5\), and antipodal invariance predate this result (Laird et al.; Kelenc et al.; earlier cited sources). An earlier classification on the sixteen-vertex five-regular Clebsch graph already gives eighty projected four-of-five neighborhood bases in sixteen pentads and a \(16K_5\) exchange graph. Those facts are explicitly excluded from the novelty claim. They do not by themselves determine the *32-vertex five-cube* optimum resolving condition, the sixteen independent antipodal choices over each projected four-set, the eighty-state signed relocation geometry, or its componentwise shortest-path metric.

A separately indexed study of ordinary metric-basis slides on the four-cube gives 928 bases and a connected slide graph, a distinct dimension and statement. The closest accessible hypercube primary texts concern criterion/complexity and antipodal invariance, rather than complete reconfiguration distances of five-cube bases. Searches by graph, antipodal aliases, exact count, exchange/slide language and signed pentad formulation did not reveal a dominating five-cube theorem. Search nonappearance is not used as a uniqueness proof. The 2014/2017 Nikolić–Čangalović–Grujičić article on hypercube basis symmetries could not be inspected in full; its publicly accessible abstract focuses on metric-dimension heuristics and upper bounds. This creates a real but not decisive residual priority risk.

## Value — PASS

Minimum resolving sets are natural optimizers for landmark-based network identification, and optimal reconfiguration asks which installations can be changed while maintaining that identifying property. The exact geometry here separates unrestricted reassignment from physical movement: the former has sixteen connected sectors with uniform degree twelve and sharp diameter four, while the latter admits *no move at all*. This contrast also sharply differs from the already determined connected slide graph of \(Q_4\). The 1280-state classification, explicit distance formula, and componentwise profile are complete natural invariants; none is an arbitrary truncated parameter sweep.

## Boundaries and independent validation

The theorem is not extended to higher hypercubes, and existing Clebsch/antipode facts are acknowledged rather than re-presented as discoveries. The cited hypercube-symmetry article remained full-text restricted. Both verification scripts are ordinary finite deterministic checks; no external proof certification or independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
