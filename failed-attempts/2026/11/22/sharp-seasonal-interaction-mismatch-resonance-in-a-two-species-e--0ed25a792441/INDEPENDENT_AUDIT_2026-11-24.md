# Independent mathematical audit

## correctness

PASS

For ε<min(b/p,c/q) the two reciprocal magnitudes stay positive, giving eigenvalues −κε±i√[(b+εp cos)(c+εq cos)]. The commutator is (pc−bq)diag(1,−1). Diagonal similarity makes the baseline ΩJ and the forcing αJ+DK, with J²=−I, K²=I, JK=−KJ. Removing scalar damping and rotating by exp[(ωt/2)J] gives mean (DK−δJ)/2 over a period: the J modulation and the sine term integrate to zero, and the rotated K produces mean DK/2. The rotated monodromy is I+εT C+O(ε²) in norm; the error bound follows from the bounded transformed generator on a bounded period, not an eigenvalue perturbation assumption. Spectral continuity of (Y−I)/(εT) and log|1+εTλ|=εT Re λ+O(ε²) for bounded λ justify the limit even at defective C. C²=(D²−δ²)I/4, giving both strict regions and no conclusion at δ²+4κ²=D². For D=0 the integrated undamped rotation has unit spectral radius at any positive frequency/amplitude. In the stated example the resonant slow eigenvalues are simple, giving ε/8+O(ε²); ω=4 instead starts from trace zero and determinant one, so its undamped pair remains on the unit circle at small ε. The supplied script was inspected, not executed.

## originality

FAIL

The mathematical claim is a routine specialization of the classical first Mathieu tongue. Remove damping exactly and write u′=a(t)v, v′=−d(t)u with a=b+εp cos ωt and d=c+εq cos ωt. Eliminate v and set u=√a y; the coefficient of y in the scalar oscillator is ad+a″/(2a)−3(a′/a)²/4. Its first harmonic is ε(cp+bq−pω²/(2b))cos ωt=−2εΩD cos ωt+O(ε²). This invertible periodic state change preserves the multipliers. With τ=ωt/2 the coefficient is 1−εδ/Ω−2εD cos(2τ)/Ω+O(ε²), i.e. Mathieu parameters A−1=−εδ/Ω, Q=εD/Ω. For w″+(A−2Q cos 2τ)w=0 near A=1, the classical first-order resonant pair has square (Q²−(A−1)²)/4 per unit τ; projecting onto e^{±iτ} leaves only the coupling ±iQ/2 and diagonal detuning ±i(A−1)/2. The periodic O(ε²) term changes one-period monodromy by O(ε²), hence cannot affect the rescaled spectral limit even at coalescence. Conversion to physical time and subtraction of damping give exactly the finding. Frozen stability, proportional forcing, and the stable off-resonance example are immediate matrix/spectral checks, not a distinct surviving theorem. This is an implication judgment, not a claim that an earlier ecology text literally prints D or that an inaccessible paper duplicates it.

## value

FAIL

The check usefully illustrates parametric resonance in ecological notation, but it solves no additional mathematical gap beyond the classical two-dimensional primary resonance after a one-variable elimination. Frozen pointwise stability is immediate from the signs, commuting modulation integrates exactly, and the off-frequency damping example is open ellipticity plus the scalar damping factor. No separate new threshold, invariant, or higher-order analysis survives the reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
