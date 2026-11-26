# Independent mathematical audit

## correctness

PASS

For consistent data the entire solution set is the intersection of an open box with the affine system c_j f_e + Q_ej d_j = 1. Use differences of any two solutions and set z_e=Δf_e, z_j=−Δd_j: each edge gives z_e=(Q_ej/c_j)z_j. In a component, all values are determined by one root value using nonzero edge multipliers. On a cycle the multiplier is exactly H_C, so any nonunit gain forces all differences to zero. Conversely if all simple cycles have unit gain, all non-tree edge constraints hold for any propagated root value, by the fundamental cycles; an isolated epoch or band contributes a free coordinate as well. Thus the kernel dimension is exactly the number of components having no nonunit cycle, including isolated vertices. Strict inequalities permit small nonzero perturbations in any kernel direction. For fixed contrasts, a monochromatic cycle telescopes. In a mixed simple cycle choose an epoch between two differently contrasted consecutive bands. Setting all other epochs to f0 and varying that epoch alone to f0+s gives an H_C with two factors whose ratio is 1 at s=0 but not for s≠0: the two slopes c/(1−cf0) differ. Hence each selected mixed cycle supplies a nonzero polynomial after clearing positive denominators; taking one per component and the product proves the generic result. This handles repeated labels, including differently labeled monochromatic cycles connected only at an articulation. Any successful component needs a cycle and at least as many edges as vertices, and the mixed K2,2 with pendant attachments is a spanning unicyclic witness with exactly the lower-bound count. Deleting any edge leaves a forest; a singleton side cannot support any cycle. Recomputed Q=(95/2,45,34,28) and H=153/133 for the witness; in the four-cycle the root denominator r1−r2 has numerator (c2−c1)(f2−f1) over the positive product (1−c1f1)(1−c2f1). Independent replay `python3 /workspace/reviews/1-check.py`: exact Fraction elimination versus directly enumerated cycles for all 512 masks of K3,3 under each of nine coverage/contrast regimes (4608 cases), three disconnected two-component observations, and the rational witness. Correctness rests on the algebra, not finite enumeration. No identifiability for out-of-model data, boundary parameters, or noisy conditioning is certified. Frozen script inspected, not executed.

## originality

PASS

Best of knowledge, the original contribution here is the model-specific mixed-contrast criterion on the unweighted schedule before data are taken, and the resulting sharp sparse design. The forward law, conversion of some calibration problems to linear solves, and the fixed-data unbalanced-cycle rank test as mathematics are prior art. In particular, part (i) is a direct application of two-term gain-graph rank to the difference variables and is covered as a general method; do not claim an independent new gain-graph theorem or new general inversion method. The fixed-data theorem does not identify which cycles are generically balanced when all gains obey the constrained starspot law, and it does not supply the bichromatic optimal design without that step. A future revision should explicitly credit the gain-graph equivalence beside the forward-model citation. Wider astronomical originality remains qualified.

## value

PASS

A scheduler can decide generic uniqueness before seeing any depths, even with missing bands, repeated contrast labels and disconnected observation patterns. The result distinguishes separated monochromatic cycles from a genuinely mixed cycle, finds an attainable count rather than only counting unknowns, and specifies why the measurement-minimal design has no one-measurement redundancy. This is a useful exact design boundary for the stipulated model, not a new general rank theorem, a field validation, or an endorsement of using the least number of observations with noisy data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
