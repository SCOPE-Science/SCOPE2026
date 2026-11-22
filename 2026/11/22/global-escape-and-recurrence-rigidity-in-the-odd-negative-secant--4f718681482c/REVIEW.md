# Scientific review

## Correctness — PASS
The exact linear coordinates \(s=x+y\) and \(z=y-x\) reduce the polynomial map to \(s'=s+z+3cs^d,\ z'=cs^d\). With \(V(s)=cs^{d+1}/(d+1)\), convexity for odd \(d\) yields the exact positive sum \(L(T)-L=B_V+(z+cs^d/2)^2+7c^2s^{2d}/4\). Any bounded subsequence bounds the increasing \(L\), so square-summability forces convergence to the origin. The complementary orbits escape and eventually enter one of two invariant cones; inside the cones, a controlled scalar recurrence yields both the signed ray and the positive escape height with its exact prefactor. Strict increase excludes all nonzero nonwandering points and Poincaré recurrence excludes all other invariant probabilities. The packaged checker passed 441 Lyapunov, 222 cone and 48 coordinate transformations; the all-degree conclusions are analytic, not experimentally inferred.

## Originality — PASS within inspected material
The source paper's Theorem A(c) classifies the **basin** as a stable manifold and proves that manifold unbounded, without asserting the dynamics of the basin's complement, unique invariant probability, global nonwandering set, or superexponential signed escape. Its companion homoclinic paper treats the opposite coefficient in odd degrees. The closest published same-model quantitative escape theorem is restricted to even degree and gives a single oriented escape ray, so it cannot imply an all-odd-degree negative-sign statement. Specific searches of the literature and mathematical findings index returned no equal or stronger odd-negative theorem. Novelty is assessed relative to inspected material, not proved by search failure; equivalent uncatalogued work remains a risk.

## Value — PASS
The original study explicitly motivates understanding the fate of initial points in a secant root-finding model and resolves the stable basin, leaving the complementary global dynamics open at the statement level. A *complete* bounded-versus-escaping dichotomy, global recurrence rigidity, two explicit absorbing channels, and a sharp escape-height law resolve that natural dynamics question for an entire sign-and-parity regime. In contrast to the odd-positive homoclinic regime, this branch supports no nonzero compact recurrent statistics. This is structural information beyond a routine numerical parameter slice or a restatement of the known basin geometry.

## Closest literature and limitations
The Fontich–Garijo–Jarque source (arXiv:2405.08791v1, Theorem A(c), Section 6), its positive-sign companion (arXiv:2405.08812v1), and the published even-degree escape theorem are the closest inspected works. The result does not apply to the untruncated secant algorithm or general perturbations. The Lyapunov function is not globally coercive, but the proof avoids needing coercivity by using monotonicity and bounded subsequences. Unindexed equivalent results cannot be ruled out by the completed search.

Self-review: passed. Independent audit: not yet performed.
