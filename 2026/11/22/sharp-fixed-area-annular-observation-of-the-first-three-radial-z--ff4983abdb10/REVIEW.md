# Independent mathematical audit

## correctness

PASS

Polar integration makes u=|z|² uniform on [0,1]; the area normalization cancels in the quotient. In y=u−1/2, the odd mode has eigenvalue q³ and the even characteristic polynomial is z²−T(q)z+q⁶. Since T−2q³=(9q/4)(1−q²)²>0 for 0<q<1, the two roots strictly straddle q³ and the minimum is simple and even. It is nonconstant by the nonzero centered even cross entry. Its constant-test equation gives β=(q³−λ)/(12(q−λ)), in fact 0<β<q²/12. Translating y²−β with the annulus keeps its observed norm unchanged and increases its full norm by (1/2−2β)δ²+δ⁴, strictly positive for all nonzero allowable displacements, including boundary annuli. The Rayleigh quotient proves the claimed upper bound and uniqueness without discretization. The trace and determinant give λ−∼(4/9)q⁵, λ+∼(9/4)q and the squared condition-number ratio. An independent symbolic reproduction using raw monomial moments confirmed the generalized characteristic polynomial, both translated norm identities and the exact q=1/2 example (`python3 /workspace/review_checks.py 2`).

## originality

PASS

The strongest inspected overlap is the two-annulus record in exactly the same three-mode space. It establishes an asymptotic improvement with two intervals and knows the single-interval O(q⁵) order, but gives neither the all-width unique one-interval placement nor its sharp spectrum and strict displacement bound. No inspected equivalent or stronger result yielding these conclusions was found.

## value

PASS

A single fixed-area detector ring for the first three axisymmetric modes has a natural worst-mode stability objective. The uniqueness and explicit off-center loss answer a design question that computing only the centered moment matrix would not answer. The exact least-energy and conditioning scales quantify the information lost for a narrow detector; they do not imply optimality among arbitrary masks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
