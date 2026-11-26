# Independent mathematical audit

## correctness

PASS

The exact no-reset survival is (a)_k/k!, and the renewal mass is the coefficient of (1−w)^−b, so at age k the stated weight is its product with (b)_{t−k}/(t−k)!. A reset consumes one step, leaving the gate phase z^k and the claimed off-diagonal element. Differentiating the generating function gives the recurrence; after phase centering at z=e^{2iθ}, division by the leading Legendre normalization gives the stated continuant with positive diagonal D in its imaginary part. Hence for θ in (0,π) and a≠b it cannot have a null vector. At z=1 normalization gives P_t(1)=1. For each fixed t, the leading coefficient stays nonzero on the path from γ=0 through γ<1/2, so the no-crossing argument with P_t=z^t at γ=0 gives t interior roots. Reversal of coefficients swaps a and b and reciprocates nonzero roots, proving the exterior half. At equality the recurrence is Legendre's, with t distinct interior real zeros in the cosine variable and a bijective phase parametrization, giving t simple unit-circle roots. This proves the actual finite-time claim; it does not give a degree-uniform distance from the circle. The supplied checker was inspected but not run.

## originality

FAIL

The claimed asymmetric zero exclusion is a direct specialization of classical Meixner–Pollaczek real-rootedness. In fact write P_t(z;a,b) for the frozen polynomial and take λ=(a+b)/2, ξ=i(a−b)/2. Substitute w=e^(−iθ)v in its generating function. Then e^(−itθ)P_t(e^(2iθ);a,b) is exactly the Meixner–Pollaczek polynomial of degree t and parameters (λ,θ), evaluated at ξ: its factors are (1−e^(iθ)v)^(−λ+iξ) and (1−e^(−iθ)v)^(−λ−iξ). Eq. (1.7.5) of Koekoek–Swarttouw and DLMF 18.23.7 give that generating function. Positive orthogonality on R for λ>0 and 0<θ<π makes every zero in ξ real, so evaluating at the nonreal ξ for unequal shapes already excludes the entire unit circle apart from z=1, which is positive. The degree-preserving continuity and coefficient reversal in the frozen proof then give the full strict side classification. This deduction uses a theorem covering every degree and in fact applies along each fixed positive sum a+b, not just a+b=1. The balanced Legendre case was already explicitly treated in the published reset finding. Failure rests on a verified prior implication, not on search quality or exact wording in the prior sources.

## value

FAIL

Finite-time coherence nodes are a meaningful physical question, but the frozen contribution supplies no independently substantive result once the old polynomial is identified. Its all-degree exclusion is a nonreal evaluation of a real-rooted orthogonal polynomial, and the passage from exclusion to a side of the circle is the elementary degree-preserving homotopy and reversal. The balanced physical nodes and reset setup were already available. The record supplies no new quantitative stability, clock extension or other surviving theorem, and the alternative continuant proof is the directly specialized classical recurrence. This is useful as an exposition, not a new finding under the scientific-value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
