# Ordinary crossing of the bielliptic sextic divisor at a generic two-involution configuration

## Final finding

Work over the complex numbers. Let \(U\subset\mathbb P(\operatorname{Sym}^6\mathbb C^2)\) be the open locus of squarefree binary sextics. For a sextic with six labelled roots, and for each of the fifteen perfect matchings \(\pi\) of those roots into three pairs, let \(\Delta_\pi\) be the determinant of the three coefficient rows of the corresponding degree-two binary forms. Define \(B\), up to a nonzero scalar, as the product of the fifteen determinants. The fact that \(B=0\) describes the classical genus-two bielliptic locus is *background*, not a new result; see Shaska--Völklein (2001), Remark 5 and Theorem 3.

**Theorem (generic ordinary two-branch crossing).** On a nonempty Zariski-open subset of the irreducible family of squarefree sextics with root set projectively equivalent to
\[
\{1,-1,a,-a,a^{-1},-a^{-1}\},
\qquad a\in\mathbb C^*,
\]
subject to pairwise distinctness, the reduced hypersurface \(B=0\) has exactly two local analytic branches meeting transversely. Equivalently, at a generic point of this four-dimensional family in the six-dimensional smooth coefficient space \(U\), its completed local equation is a unit times \(uv\), where \(u,v\) are two members of a regular parameter system. This statement is about the *sextic coefficient space* and does not assert that the coarse genus-two moduli quotient has the same local analytic type.

More concretely, at the ordered root tuple
\[
 (r_1,\ldots,r_6)=(2,-2,\tfrac12,-\tfrac12,1,-1),
\]
exactly the two matchings
\[
\pi_1=(12)(34)(56),\qquad \pi_2=(14)(23)(56)
\]
have zero determinants. In the affine root coordinates \((r_1,\ldots,r_6)\), their gradient vectors have the nonzero minor
\[
 \det\begin{pmatrix}
 \partial_{r_1}\Delta_{\pi_1}&\partial_{r_2}\Delta_{\pi_1}\\
 \partial_{r_1}\Delta_{\pi_2}&\partial_{r_2}\Delta_{\pi_2}
 \end{pmatrix}=\frac98.
\]
The crossing is therefore an ordinary normal crossing of two smooth divisors, not a cusp or a nonreduced doubled component.

## Definitions and scope

For affine roots \(r_i\), the quadratic for a pair \((i,j)\) has coefficient vector \(q_{ij}=(1,-r_i-r_j,r_ir_j)\). For a matching \(\pi=((i,j),(k,l),(m,n))\), take \(\Delta_\pi=\det(q_{ij},q_{kl},q_{mn})\), with rows in the displayed matching order. A different row order changes its sign but not its zero divisor or the transversality claim. The polynomial \(B\) is a symmetric binary-sextic invariant of coefficient degree fifteen, up to scalar: the classical root-pairing description, rather than the production of an original new invariant, is used here as the local equation.

The theorem concerns only generic configurations in the displayed family, the squarefree locus over \(\mathbb C\), and the *reduced* divisor. It neither classifies the entire singular locus, nor handles characteristic two, coincident roots, or local singularities in a GIT quotient.

## Proof

**Classical equation and local coordinates.** A genus-two sextic admits a degree-two elliptic quotient precisely when its six roots admit a fixed-point-free projective involution. For a chosen matching this is equivalent to linear dependence of the three pair quadratics, hence to \(\Delta_\pi=0\); this is the classical equivalence established by Shaska--Völklein (2001, Remark 5 and Theorem 3). The union of these fifteen labelled root divisors descends to the reduced bielliptic divisor in \(U\). Thus, on the ordered squarefree root space, the local equation is a nonzero unit times the product of the vanishing \(\Delta_\pi\). The root-to-coefficient map is étale on this open set, since its Jacobian is the nonzero Vandermonde product. It therefore preserves local analytic intersection types.

**Two branches at an explicit squarefree point.** Substitute the six distinct roots \((2,-2,1/2,-1/2,1,-1)\) into the determinants of all fifteen matchings. Exact arithmetic gives \(\Delta_{\pi_1}=\Delta_{\pi_2}=0\) and \(\Delta_\pi\ne0\) for each of the other thirteen matchings. Differentiate the two determinant polynomials in the six affine-root coordinates. Direct expansion (or differentiation of \(q_{ij}\)) gives the displayed \(9/8\) minor. Thus the differentials of \(\Delta_{\pi_1}\) and \(\Delta_{\pi_2}\) are linearly independent, so both zero divisors are smooth and their intersection is transverse. The remaining thirteen factors are invertible in a neighbourhood of the point. The local reduced divisor is therefore analytically \(uv=0\), with ordinary two-branch crossing.

**Genericity in the asserted family.** For every allowable \(a\), the roots \(\{\pm1,\pm a,\pm a^{-1}\}\) are paired by both the involutions \(t\mapsto-t\) and \(t\mapsto-1/t\). The corresponding determinants vanish identically along the family. The conditions that no third determinant vanishes, and that the two gradients are independent, are Zariski-open conditions, as they are respectively the nonvanishing of finitely many regular functions and of one Jacobian minor in root coordinates. Both hold at the exhibited configuration, which is projectively equivalent to \(\{\pm1,\pm2,\pm1/2\}\). The parameter space \((\mathbb C^*\setminus\{\text{collision values}\})\times\operatorname{PGL}_2\) is irreducible and its image is irreducible. Therefore the two properties hold on a dense nonempty open subset of the stated family. Etaleness of the squarefree root map again transfers the crossing to \(U\). \(\square\)

## Verification and limitations

The source package's `verify.py` explicitly enumerates the fifteen matchings and checks the two vanishing factors and a nonzero gradient minor at the specified witness in exact rational arithmetic. An independent reconstruction using symbolic differentiation of the determinant rows reproduced **exactly two** vanishing determinants and the minor \(9/8\). Those finite calculations certify the witness conditions only; the unrestricted generic assertion follows from the irreducibility and openness argument above. The classical equation of the bielliptic locus comes from the cited published theorem and is not derived solely from finite checks.

The original stronger marketing of the degree-fifteen pairing equation, the genus-two equivalence, and birational elliptic-surface reconstruction as new contributions is withdrawn from the novelty claim. Combining the 2001 genus-two root-pairing criterion with the 2026 split-Weierstrass description already substantially covers those observations. Only the *explicit normal-crossing calculation and its generic family extension* are presented here as the surviving contribution, subject to best-of-knowledge priority risk: earlier local singularity analyses of the genus-two bielliptic divisor may contain equivalent normal-crossing statements.

## References

1. T. Shaska and H. Völklein, *Elliptic subfields and automorphisms of genus 2 function fields*, arXiv:math/0107142 (2001), especially Remark 5, Theorem 3 and the fifteen root-pair factors in the proof of equation (18), https://arxiv.org/pdf/math/0107142.
2. C. Ciliberto, A. Grassi, R. Miranda, A. Verra and R. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725 (2026), especially Sections 2.4 and 2.7, https://arxiv.org/pdf/2602.11725.
