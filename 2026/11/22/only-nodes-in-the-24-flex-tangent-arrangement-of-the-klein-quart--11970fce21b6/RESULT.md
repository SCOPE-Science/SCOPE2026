# Only nodes in the 24-flex-tangent arrangement of the Klein quartic

## Finding
Let \(C\) be the complex smooth Klein plane quartic
\[
C:\quad X^3Y+Y^3Z+Z^3X=0.
\]
Its \(24\) ordinary inflection points determine \(24\) distinct tangent lines. Let \(\mathcal A\) be their reduced union. Then **no three lines of \(\mathcal A\) meet at one point**. Hence its complete singularity basket consists of
\[
\boxed{\binom{24}{2}=276\text{ ordinary double points},\qquad t_r=0\ (r\ge3).}
\]
In particular, each tangent contains exactly \(23\) distinct intersections with the other tangents. This describes the characteristic-zero arrangement; the arithmetic certificate uses reduction at one good prime, not an assertion about all positive characteristics.

## Assumptions and scope
Work with the stated plane model over \(\mathbb Q\), then base change to an algebraically closed characteristic-zero field. The tangent at a smooth point is the line with coefficients \((F_X,F_Y,F_Z)\), where \(F=X^3Y+Y^3Z+Z^3X\). A flex is a point of the scheme-theoretic Hessian intersection. For this model the normalized Hessian is
\[
H_0=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5,
\]
and the full Hessian determinant is \(-54H_0\). The prime \(29\) is a good characteristic for this model and its flex scheme, as verified below.

## Proof
**1. A finite-étale lifting lemma.** Let \(R=\mathbb Z_{29}\) (the \(29\)-adic integers). On \(\mathbb P^2_R\), consider the common-zero scheme \(W=V(F,H_0)\). The complete projective enumeration in the supplied checker shows that the special fiber \(W_{\mathbb F_{29}}\) contains precisely \(24\) distinct points and that each is a simple intersection. The simplicity also follows without a derivative computation: the curve and sextic share no component, their projective intersection number is \(4\cdot6=24\), and the \(24\) distinct rational points already exhaust it with multiplicity one. Thus, in neighborhoods of these points, the Jacobian criterion and Hensel's lemma give \(24\) unique unramified sections after passage to a suitable strictly henselian extension of \(R\). Properness and the intersection-degree bound exclude additional geometric points in the generic fiber. The geometric generic Hessian intersection therefore has exactly \(24\) points, specializing bijectively to these \(24\) special-fiber points. Equivalently, \(W\) is finite étale of degree \(24\) over \(R\).

**2. Exact census at the good prime.** The checker iterates the complete projective plane \(\mathbb P^2(\mathbb F_{29})\) of \(29^2+29+1=871\) points in the disjoint normalized charts
\[
(1:a:b),\quad(0:1:a),\quad(0:0:1).
\]
It evaluates \(F\) and \(H_0\) at all these points. Exactly \(24\) satisfy both equations. At every such point the gradient
\[
(F_X,F_Y,F_Z)=(3X^2Y+Z^3,\,X^3+3Y^2Z,\,Y^3+3Z^2X)
\]
is nonzero. Normalizing these gradients yields exactly \(24\) distinct projective lines.

For all unordered pairs of these \(24\) line-coefficient triples, the program computes their cross products as intersection points in \(\mathbb P^2(\mathbb F_{29})\), normalizes the resulting vectors, and checks every point against all \(24\) lines. There are \(276\) distinct pair intersections, **each on exactly two of the lines**. All assertions are verified by modular integer arithmetic over the full finite projective plane; the checker does not assume the answer.

**3. Descent of nonconcurrence.** The tangent coefficients are polynomial in the coordinates of the flex sections and reduce compatibly modulo \(29\). If two characteristic-zero tangent lines coincided, their reductions would coincide. If three characteristic-zero tangent lines were concurrent, the determinant of their coefficient vectors would be zero over a finite extension of \(\mathbb Q_{29}\) and hence its reduction would be zero. Their respective reductions would therefore be three concurrent lines, contradicting the distinct \(276\)-intersection census. (Nonzero gradient reduction ensures no coefficient vector vanishes and no line degenerates.) Therefore all \(24\) generic tangents are distinct and pairwise intersections are distinct for different pairs. Each is an ordinary node of the reduced union of lines; there are no higher-order intersections.

## Verification
Execute `python3 VERIFY.py` using only the Python 3 standard library. It exhaustively enumerates all \(871\) rational projective points modulo \(29\), constructs and normalizes exactly \(24\) flex tangents, computes the cross product for each of their \(276\) distinct pairs, and checks that the \(276\) intersection points are pairwise distinct and lie on exactly two tangents. The independent sample primes \(43\) and \(71\) produce the same counts, but are corroboration only, not a second proof of the characteristic-zero assertion. The characteristic-zero conclusion rests on the rigorously justified good-reduction specialization in the proof above.

## Relationship to prior work
Elkies establishes that the Klein quartic has exactly \(24\) Weierstrass points, each an ordinary flex; that geometric count is **not new here**. Poonen–Schaefer–Stoll establish the eight triples of flexes linked by the residual tangent map and use them for descent; those tangent-residual triples are distinct from concurrence of the **tangent lines themselves**. A separate previously published calculation gives Frobenius splitting of the flex and residual-triangle schemes in characteristic five; this is not a classification of pair intersections among the \(24\) tangent lines. Dimca–Ilardi–Pokora–Sticlaru determine that the \(12\) inflection tangents of the *different* quartic in the Ciani pencil at parameter \(3\) have only double intersections; they do not state the corresponding assertion for the \(24\) Klein quartic flex tangents. Nearby literature on the Klein configuration and bitangent arrangements concerns other line collections.

## Limitations
This concerns the literal Klein plane model over characteristic zero. The modulo-29 certificate does not classify bad or exceptional reduction primes for the tangent arrangement; exceptional positive characteristics may change the incidence lattice. A reduction test could not prove that *some* concurrence exists in characteristic zero, but here a good prime with **no** concurrence proves the negative assertion via specialization. The result is a complete incidence classification of one natural line arrangement, not a claim of a general theorem on arbitrary quartics. The historical literature comparison is substantial but not a certified exhaustive priority determination. No independent mathematical audit has been performed.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998/1999), section 2, including the proposition on all 24 ordinary Weierstrass points. https://library.slmath.org/books/Book35/files/elkies.pdf
2. B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, arXiv:math/0508174, first publicly submitted 2005-08-10; sections 4.3 and 11.1–11.2. https://arxiv.org/abs/math/0508174
3. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of Free Curves by Adding Lines to a Given Curve*, published 2023-11-09, section 5 and remark 5.1. https://link.springer.com/article/10.1007/s00025-023-02036-9
4. *Frobenius splitting of the characteristic-five Klein quartic's flex triangles*, published finite-field computation, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-frobenius-splitting-of-the-characteristic-five-klein-quartic-s-f--07295989c49b/RESULT.md
