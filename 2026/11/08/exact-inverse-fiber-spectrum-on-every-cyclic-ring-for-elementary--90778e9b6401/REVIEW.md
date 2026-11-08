# Scientific assessment

## Correctness — PASS

The claim specifies a single deterministic cellular-automaton update, indexed rings including lengths one and two, and exactly one time step. The four pair states are exhaustive, and each output bit has a unique continuation because Rule 106 is right-permutive. Therefore the predecessor count is a fixed-point count, not an approximation. The closure has exactly \(41\) maps and is constructed from two explicit generators, whose noninjectivity excludes four fixed points at any positive length. A transfer identity gives all output-class counts. The rational identities are established for *all* lengths by verifying the exact low-degree coefficients and \(41\) consecutive zeros in the residual, then applying Cayley–Hamilton to the \(41\)-dimensional orbit. A second implementation uses the Wolfram truth table and direct enumeration through length \(12\), including all wraparound cases. This second check corroborates but is not substituted for the infinite proof. Both embedded verifiers passed using their actual source files. No unproved lemma is needed beyond standard Cayley–Hamilton and simple-pole coefficient asymptotics.

## Originality — PASS, with residual priority risk

The 2014 Rule 106 study proves symbolic-dynamical chaos on invariant subsystems rather than counting one-step inverse degrees of all finite-ring targets. The 2009 cellular automaton transition-graph paper computes graph automorphism groups, not these degree histograms. The 2010 preimage paper counts homogeneous targets rather than all targets. The 2017 periodic-preimage study shares the four-state labeled de Bruijn method and examines Rule 106 directly, so it is the closest technical antecedent; its theorem about least periods of predecessors does not imply the displayed rational generating functions without substantial new enumeration. A general construction algorithm does not automatically imply an explicitly determined invariant. Semantic research-record searches using Rule 106, cyclic inverse fibers, aliases, recurrent counts, and finite-ring uniqueness did not surface a matching all-length spectrum. Prior first-step laws for other Wolfram rules were reviewed for overlap; they have different local maps and do not determine this instance. Lack of a hit is not proof of uniqueness. An overlooked earlier all-rule or symmetry-equivalent enumeration remains a genuine risk.

## Value — PASS

The exact distribution answers a natural measurable question about invertibility of a classical surjective-on-the-full-shift cellular automaton when restricted to finite cyclic rings: how many outputs are Garden-of-Eden outputs, how many have each positive inverse degree, and which targets are maximally ambiguous? The unexpected uniform inverse-degree bound of three, the period-three exceptional output, and exponentially rare nonunique inversion provide structure unavailable from simply knowing surjectivity or one homogeneous-target count. The result is an all-ring classification with reproducible arithmetic certificates, not a small ad hoc numerical increment or a renamed prior formula.

## Closest prior sources and limitations

- Zhao, Chen, Jin (2014), Rule 106 invariant chaotic subsystems: full HTML sections 1–5 inspected.
- Powley and Stepney (2009), finite transition-graph automorphism classification: full author PDF inspected.
- Powley and Stepney (2010), homogeneous-configuration preimage counts: full author PDF sections including method, examples, conclusion inspected.
- Mariot, Leporati, Dennunzio, Formenti (2017), spatial periods of preimages: full lawful author postprint introduction, labeled de Bruijn construction, and algorithm inspected.

One-step cyclic counts only; not a multistep inversion theorem. Possible broader equivalent all-rule tables remain a residual originality risk. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
