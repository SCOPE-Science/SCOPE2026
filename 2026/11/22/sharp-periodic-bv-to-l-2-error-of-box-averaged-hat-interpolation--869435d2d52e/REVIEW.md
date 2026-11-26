# Independent mathematical audit

## correctness

PASS

The Jordan parts of a nonconstant periodic derivative both have mass V/2. A probability coupling represents f, modulo constants, as V/2 times a mean of oriented arc indicators. Thus the squared operator constant is one quarter of the maximal squared arc residual. After rescaling to cell length one and passing to the shorter arc, the complementary gap is ≥N/2≥3. The two residual layers are within 3/2 of their jumps, so the squared error is h times the line integral Q=∥e_s−e_t∥², without wrapping interference. Independent symbolic integration gives J(u)=(6u³−5u²+1)/6 on the first half-cell and J(1−u)=J(u), with J≤1/6. In a single half-cell the bound d−d²/3≤5/12 follows by integrating the one nonzero nodal average and its hat. In a cell-straddling-midpoint arc the exact formula is d−7d²/12−(d−1/4)(a−b)², where a,b are lengths on the two halves. If d≤1/4 use ∣a−b∣≤d to bound by 17/64; otherwise the unique maximum is at d=6/7 and a=b, giving Q=3/7. For different cells, only overlap between the two jumps can increase Q. Cell separation k≥3 gives no such overlap, while k=2 gives at most 1/24, contributing at most 1/12 to Q. At k=1, the ordered half-cell choices give F(s), the no-overlap bound, K(s,v), or G(v) as in the frozen proof: the overlap integrals and exact Bernstein minima 1/672, 47/1792, 47/1792, 1/672, 1/1344 were independently verified from the step residuals. All separated cases are strictly suboptimal. In the Hilbert-space mean, equality requires the residual to be almost surely a fixed maximal vector (use the variance identity). For the maximizing short arc the essential closed support spans three consecutive cells, with no missing interior interval; distinct cell translates have different supports, while complements reverse sign. Thus only one ordered jump pair can occur in an equality coupling, yielding exactly the prescribed arcs modulo affine changes. Squared error of the maximizing arc is 3h/7 and V=2, giving 3/(28N).

## originality

PASS

The periodic centered-box nodal interpolation construction is prior art, and the strongest related indexed result gives exact single-jump real-line L¹/L∞ constants for the same averaging family. Neither that result nor the inspected Q1, sampling-Kantorovich or spline-approximation statements establish the periodic BV-to-L² norm and all its maximizing arcs. The surviving distinct content is the sharp two-jump interaction, constant and phase locations, not the operator construction or a general BV representation principle.

## value

PASS

Centered local averaging and linear-hat reconstruction are natural in TV-diminishing approximation. For the standard full-width choice, the exact circular BV-to-L² norm is a quantitative benchmark. Classifying the equality arcs reveals a specific effect of the interaction of two jumps: the worst case is concentrated in one cell but neither jump is at a knot or midpoint. The result resolves this finite-phase question uniformly across all permitted mesh sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
