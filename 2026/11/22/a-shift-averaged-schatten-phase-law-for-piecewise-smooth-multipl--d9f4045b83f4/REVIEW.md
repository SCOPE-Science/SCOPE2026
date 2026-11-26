# Independent mathematical audit

## correctness

PASS

Reconstructed the proof for complex symbols: on a cell, with unit constant e and w=(f−mean f)e, the off-diagonal blocks of the commutator are e⟨conjugate(w),·⟩ and −w⟨e,·⟩. Both have singular value ‖w‖ and their input and output spaces are mutually orthogonal. The direct sum over cells proves the exact paired spectrum for all h and p>0, including zero blocks. The phase average converts the cell sum to 2/h times the integral over all starting points x of the centered standard deviation on [x,x+h) to power p. Uniform continuity of the finitely many one-sided derivatives gives σ/h=|f'|/√12+o(1) on smooth cells, uniformly; continuity of t^p on a compact interval is enough even at derivative zero. The omitted continuous breakpoints contribute O(h^p). For h below breakpoint separation, the other cells each have one jump, so in normalized cell L² they differ by O(h) from two constants with fractions θ,1−θ. The centered L² norm is Lipschitz; uniform phase gives the beta integral with multiplicity two. These contributions scale as h^(p−1) versus 1, giving exactly the three limits (including β(3/2,3/2)=π/8). If there are no true jumps, the jump term is zero, not a nonzero leading term. Independently, on a sawtooth crossing cell, writing the symbol as affine slope one minus a unit step gives the cross covariance hθ(1−θ)/2 and the stated variance and F₂. Replay: RESULT.md §§1–4 and the all-starting-points representation above. VERIFICATION.md and verify.py were inspected, not executed. The checker is finite-grid evidence; no claim of a general BV law or a fixed-shift trace law is supported.

## originality

PASS

Pass for the quantitative shift-averaged phase law, not for the elementary rank-one decomposition by itself nor for Schatten/Besov ideas in general. The closest underlying oscillation and martingale formulations were compared; no inspected theorem yields the whole matching law and its exact constants.

## value

PASS

The phase law identifies which regularity features survive in Schatten mass across the trace index and quantifies them without grid alignment. At the critical exponent a finite jump term and the derivative integral coexist with different constants. The result is an exact reusable model calculation; the rank-two cell observation alone would be routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
