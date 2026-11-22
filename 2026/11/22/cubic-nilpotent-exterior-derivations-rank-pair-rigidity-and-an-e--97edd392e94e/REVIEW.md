# Scientific review: cubic-nilpotent exterior derivations

## Correctness — PASS

The result follows from explicit, independently reconstructible steps. Exterior-degree preserving derivations are exactly generator-linear derivations; in characteristic three the third iterate is again a derivation, giving the exact cube-zero criterion. The exterior modules for all three possible generator Jordan blocks are computed by signed wedge bases. Their tensor products reduce to a two-dimensional quotient of the restricted-module Green ring, with all projective summands accounted for by total dimension. The rank-pair inverse recovers the generator block multiplicities without any statistical or genericity assumption. The finite-field orbit count follows from the centralizer algebra's dimension, reductive quotient, and unit group. The accompanying checker directly tests the original wedge Leibniz matrices, rather than a formula-only implementation.

## Originality — PASS relative to the inspected evidence

Korhonen's 2021 work analyzes the second exterior/symmetric powers in characteristic two, not the characteristic-three full exterior-algebra derivative or its inverse rank rigidity. Briggs–Rubio y Degrassi address restricted Lie algebras of integrable derivations, not Jordan spectra of exterior-induced operators. Armstrong–Sigg treat related exterior actions in complex Lie cohomology, and Norman's earlier modular Kronecker-sum work supplies general tensor tools but not the full exterior functor plus rank recovery and arithmetic census. Complete published research results about bivector multiplication, all-element multiplication in four generators, and matrix-power differentials concern distinct operators. Index searches and accessible historical claims did not identify a stronger theorem directly implying this entire statement. Historical priority remains provisional, especially since Norman's full journal article was not recovered.

## Mathematical value — PASS

Two rank measurements on an exponentially large induced space recover the entire generator Jordan partition, uniformly in the dimension. This is a structural rigidity statement rather than a finite list of examples or a rephrased nilpotent-orbit formula. The exact joint finite-field rank polynomial gives the arithmetic distribution of the recovered types, and the characteristic-three projective tensor cancellation explains why the reconstruction can be so simple. Such rank-pair data are natural invariants in modular exterior representation theory and facilitate detecting generator nilpotence types without reconstructing matrices from the induced representation.

## Limitations and closest comparisons

The conclusion excludes non-degree-preserving derivations, other characteristic values, higher nilpotency exponents, and multiplicative group actions. The full historical tensor-algebra corpus cannot be certified as exhausted. The reproducibility tests are finite and not a substitute for the proof. See `RESULT.md` and `AUDIT.json` for exact claims and scientific comparisons.

Self-review: passed. Independent audit: not yet performed.
