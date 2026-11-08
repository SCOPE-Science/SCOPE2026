# Mathematical review: cyclic Rule 150 inverse-degree law

## Correctness

**PASS.** The fundamental kernel recurrence \(x_{i+1}=x_i\oplus x_{i-1}\) has precisely four three-periodic solutions when \(3\mid n\), and none nonzero otherwise. The three image parity sums provide two independent constraints and match the image dimension. Fixing a target representative turns necklaces over that target into orbits of its four labeled predecessors under the target's rotation stabilizer. For primitive period divisible by three this action is a translation on the four-element fiber (four fixed points or two two-cycles); for primitive period coprime to three it is a fixed point and a three-cycle. Möbius inversion and Burnside yield an exact whole-space census. All boundary lengths, repeat parities, and primitive-period quantifiers were checked against the proof. The standalone verifier independently checked the full transition graph on every ring through length \(18\), as well as the census arithmetic through \(60\). This finite corroboration is distinct from the infinite proof.

## Originality

**PASS, qualified.** The most relevant earlier algebraic analysis is Martin–Odlyzko–Wolfram (1984), which supplies labeled-state polynomial reachability and cycle structure, not this rotation-class predecessor census. Krawczyk (2013) uses a different equivalence relation on phase-space graphs and compares Rule 105 with Rule 150. Frati–Petak–Cheney (2024) specifically motivates necklace networks but does not give an all-size inverse-degree spectrum, primitive-period parity criterion, or exact divisor census. Searches covered the direct Rule 150 formulation, Rule 105 output complement, three-tap polynomial \(1+z+z^2\), orbit quotients, and published mathematical-record claims. The strongest residual risk is that an earlier explicit quotient formula is embedded in a less searchable classical CA source or phase-space atlas; no independent priority validation has occurred.

## Value

**PASS.** The inverse-branching structure of a necklace network is a natural measure of information loss after discarding the indexing origin. This gives the full spectrum and all output-dependent equality cases for a classical elementary rule over unbounded ring sizes, not merely a finite example. The sharp stabilizer criterion explains an otherwise hidden two-versus-four collapse of a uniform four-element labeled fiber, and the census gives the exact graph indegree histogram and a generic four-parent law. It differs structurally from prior work on Rule 90 because the Rule 150 kernel has period three and is absent at coprime ring lengths.

## Closest literature and limitations

The proof inherits the established polynomial representation of additive cellular automata but adds the explicit orbit analysis. The all-length exact inverse-degree census should not be confused with earlier finite-state transition graphs, generalized isomorphism-class partitions, or staggered reversible Rule 150. The result is limited to synchronous one-step evolution and rotation classes; absolute priority and independent verification remain open.

Self-review: passed. Independent audit: not yet performed.
