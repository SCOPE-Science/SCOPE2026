# Scientific review: Four-residue extinction and two-cycle phases on complete triple-incidence graphs

## Correctness — PASS

The direct incidence-column difference argument proves full point rank for every \(n\ge4\). Four parity evaluations of the point Gram matrix yield \(BB^{\mathsf T}\in\{I,I+J,0,J\}\), all idempotent. The block iterate-rank filtration establishes the exact nilpotent three-chains and the recurrent involution, and the fixed-state equations establish its full Jordan structure. Counting the kernels on the nilpotent component gives every periodic-entry layer; an equal-fiber Fitting decomposition gives all individual basins. The attached executable independently constructs graph matrices and checks ranks through \(n=16\), exhaustively enumerating the two smallest systems. These checks corroborate, not replace, the universal proof.

## Originality — PASS with historical-priority limitation

The closest published graph-dynamics records concern edge subdivisions of ordinary complete graphs (even incidence-column weights and rank defect one) and symmetric projective-plane point–line incidences (square block matrices). Neither published full result contains or implies the full rectangular point–triple incidence four-residue family. Ghorbani et al. cover classical subset-inclusion matrix rank tools; Moreno et al. cover finite linear dynamics in general; Rowland and Yassawi concern automatic sequence columns. Their general theory and matrix foundations are credited rather than claimed new. Equivalence outside the examined literature remains a risk, and no independent novelty certification has been performed.

## Mathematical value — PASS

The object is the complete three-uniform set system, not an arbitrary selected graph. Its temporal evolution displays an exact four-residue structural phase transition: for \(n\equiv2\pmod4\) every state dies in three steps; for \(n\equiv3\pmod4\) only \(q^2\) states recur; and the two other residues support much larger involutive recurrent spaces with different transient dimensions. The calculation determines full Jordan types, all temporal orbits and basin populations, and sharp asymptotic proportions of states requiring the last update. This is a meaningful complete dynamical classification distinct from the classical rank computation alone.

## Closest literature and limits

The complete primary texts inspected were Moreno–Bollman–Aviño-Díaz (arXiv:math/0604534), Ghorbani et al. (arXiv:0709.3144), and Rowland–Yassawi (arXiv:1209.6008), along with two full published graph-incidence results cited in RESULT.md. The work is limited to full triple systems, characteristic-two fields, unweighted open-neighbor synchronous updating. Historical priority and independent validation are not established.

Self-review: passed. Independent audit: not yet performed.
