# Scientific review: sharp three-branch boundary feedback

## Correctness — PASS

The claim concerns exactly the regularized all-defector boundary fixed-point problem of Betz–Fu–Masuda (2026), not the original finite stochastic population. Rewriting their boundary Eqs. (52)–(54) produces a fractional-linear conditional environment \(c(r)\) and a logistic equation \(G(r)=d\). The derivative has a quadratic numerator with discriminant \(K[K-4a(a+b)]\); the minimum ratio is exactly \(4a(a+b)\). This proves both the maximum of three roots and the full sharp classification, including tangencies. The auxiliary stability identity is differentiated independently. The rational example checks every model constraint and has an exact middle root with negative scalar-logit derivative. Rational verification and supplementary numerical roots were reproduced from the included `verify.py`. No finite simulation is used as an infinite proof.

## Originality — PASS (bounded to inspected literature)

The closest primary paper [1] provides the implicit boundary equations and explicitly says multiple candidate solutions might occur; it does not derive a multiplicity criterion or exhibit opposite-signed stable auxiliary boundary candidates. Its remaining mean-field bifurcation and oscillation results concern different states. Betz–Fu–Masuda (2024) [2] studies continuous environmental variables on two communities; Su et al. (2019) [3] treats game transitions with weak-selection fixation criteria; Ito–Yamamichi (2024) [4] considers a different continuously varying environmental-resource model. Available scientific searches and previously indexed related claims did not reveal an implication covering this exact binary-edge conditional-environment classification. Searches cannot establish global priority. The Ito–Yamamichi mathematical exposition and Su et al. full text were not inspected, although their documented models differ materially; a general sigmoid–rational fixed-point theorem might contain the algebra abstractly.

## Value — PASS

The originating article leaves the number of regularized rare-invader candidates undetermined and explicitly calls for stronger justification of its boundary treatment. A universal sharp threshold and a legal example with two environmentally attracting candidates whose transverse growth tests have opposite signs address a substantive ambiguity in applying that boundary approximation. This is a natural complete classification of a specific implicit scientific criterion, not merely a numerical fixed point or an arbitrary parameter cut. It identifies when auxiliary boundary initialization matters, while refraining from asserting actual ecological bistability or multiple invasion probabilities.

## Scientific limitations

The result applies to the auxiliary all-defector boundary of the infinite-population mean-field approximation, with \(\beta>0\) and the strict switching order. It does not prove branch selection by a genuinely rare mutant, fixation, full-dimensional basins, or empirical outcomes. Some additional historical coverage remains possible; independent assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
