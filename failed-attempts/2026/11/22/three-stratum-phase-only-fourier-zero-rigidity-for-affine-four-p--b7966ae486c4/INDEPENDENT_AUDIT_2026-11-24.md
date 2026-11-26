# Independent mathematical audit

## correctness

PASS

For independent u₁,u₂,u₃, the dual restriction ξ↦(−⟨ξ,u_i⟩) is onto, with p^(d−3) lifts per triple. After removing the common nonzero scalar and translation character, the four summands are unit complex numbers. If their sum is zero, the third elementary symmetric sum is the product times the conjugate of the first, so the monic root polynomial is even and the four numbers pair oppositely, including multiplicities. A pair requires a ratio in −μ_p; two disjoint pairs give two independent affine equations in the anchored three coordinates. Three matchings cannot be feasible: two −μ_p ratios along a length-two path force the third ratio into μ_p, disjoint from −μ_p. Two matchings give an alternating four-cycle; fixing the phase at site zero determines every other actual summand and feasibility puts it in its required coset. The two local lines have different directions and meet at one point. This gives all counts and the lifted subspace dimensions. The three listed witnesses give zero, one or two feasible matchings; in the two-matching case the four coefficient cosets are two copies of one coset and two of its negative, giving the equivalence classification. Inspected the frozen exact Gaussian-integer checker (artifacts/verify.py) without executing it; its finite set has 5271 planned checks. In the independently written `python3 /workspace/replay/check_assignments.py 4`, reduction at primes 41,29,89 and evaluation at every primitive p-th root and both signs of the square root of −1 makes an exact test for these bounded coefficient sums. At p=5,7,11 the 64 normalized quarter-turn phase choices give local spectra {0,5,9}, {0,7,13}, {0,11,21}; the witness zero lines and intersections agree. This does not test arbitrary phases; the proof does.

## originality

FAIL

No identical rank-three table was found, but the exact phase-only law and geometry mechanically follow from the explicit unit-torus zero description in the distinct earlier four-point rectangle proof b51ecb1779fe (RESULT.md offset 0, Proof), by freeing its cross phase to range over a third coset. The distinct earlier flat-parabola proof c2e3015b14a6 independently already provides the setting-independent opposite-pair lemma, linear pairing equations and two-feasible-matching bound. Coverage is by the proof-level reduction given below, not by assuming that a rank-two support theorem applies unchanged to rank three.

## value

FAIL

The fixed simplex is a natural support, and its phase-only zero sets are correctly described. But the exact invariant is a direct coset restriction of an existing complete pointwise torus description after one invertible coordinate change. Once those three prior branches are written, their line sizes, intersections and equality case are immediate. No distinct invariant beyond that consequence remains in the frozen claim; the independent finite check does not add substantive value to it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
