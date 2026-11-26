# Eight-cycle Frobenius splitting of the 58 lines on a characteristic-three quartic

## Finding
Let \(X\subset\mathbb P^3_{\mathbb F_3}\) be the quartic surface
\[
X:\quad x_1^3x_2-x_1x_2^3+x_0^3x_3-x_0x_3^3=x_0^2x_1x_2.
\]
Let \(\mathcal L=\operatorname{Hilb}^{t+1}(X)\) be its scheme of projective lines. Then \(X\) is smooth and \(\mathcal L\) is finite étale of degree \(58\) over \(\mathbb F_3\). Geometric Frobenius on its points has cycle type
\[
\boxed{1^{10}8^6}.
\]
Consequently, for every integer \(n\ge1\), the number of lines defined over \(\mathbb F_{3^n}\) is
\[
\boxed{\#\mathcal L(\mathbb F_{3^n})=10+48\,\mathbf1_{8\mid n}},
\]
and the Hasse–Weil zeta function of this zero-dimensional Fano scheme is
\[
\boxed{Z(\mathcal L/\mathbb F_3,T)=\frac1{(1-T)^{10}(1-T^8)^6}}.
\]
In particular, the smallest finite extension over which all \(58\) geometric lines are defined is \(\mathbb F_{3^8}\), while exactly \(10\) lines are defined over the prime field.

## Assumptions and scope
Everything is over fields of characteristic \(3\). A line is a closed subscheme of \(\mathbb P^3\) geometrically isomorphic to \(\mathbb P^1\) of degree one; it is defined over a finite field precisely when the corresponding point of the Grassmannian is rational. The equation above is the specialization at coefficient \(1\) of the first characteristic-three family of Veniani's Example 5.1 [1]. The theorem counts embedded lines, not line incidence pairs, surface rational points, or isomorphism classes of surfaces.

## Proof
**Smoothness.** With \(F\) the left-hand side minus the right-hand side, its derivatives in characteristic \(3\) are
\[
\begin{aligned}
 F_{x_0}&=-x_3^3+x_0x_1x_2, &F_{x_1}&=-x_2^3-x_0^2x_2,\\
 F_{x_2}&=x_1^3-x_0^2x_1, &F_{x_3}&=x_0^3.
\end{aligned}
\]
If all four derivatives vanish, they force successively \(x_0=x_1=x_2=x_3=0\). Thus \(X\) is projectively smooth.

**All lines.** Every line over an algebraic closure has a unique reduced-row-echelon basis \((u,v)\) of its two-dimensional vector subspace of \(k^4\). For pivot columns \(i<j\), put \((x_0,x_1,x_2,x_3)=uU+vV\) and require all five coefficients of \(F(uU+vV)\) to vanish. The exact coefficient lists (in the order \(U^4,U^3V,U^2V^2,UV^3,V^4\)) are as follows, with \(a,b,c,d\) independent chart coordinates:

| Pivots | Substitution \((x_0,x_1,x_2,x_3)\) | Five coefficients |
| --- | --- | --- |
| \((0,1)\) | \((U,V,aU+cV,bU+dV)\) | \((b-b^3,\ d-a^3-a,\ -c,\ a-d^3,\ c-c^3)\) |
| \((0,2)\) | \((U,aU,V,bU+cV)\) | \((b-b^3,\ a^3-a+c,\ 0,\ -a-c^3,\ 0)\) |
| \((0,3)\) | \((U,aU,bU,V)\) | \((a^3b-ab^3-ab,\ 1,\ 0,\ -1,\ 0)\) |
| \((1,2)\) | \((0,U,V,aU+bV)\) | \((0,1,0,-1,0)\) |
| \((1,3)\) | \((0,U,aU,V)\) | \((a-a^3,0,0,0,0)\) |
| \((2,3)\) | \((0,0,U,V)\) | \((0,0,0,0,0)\) |

Thus the third and fourth charts are empty. The fifth contributes exactly three lines (\(a\in\mathbb F_3\)), and the sixth contributes exactly one. The first chart is exactly
\[
b\in\mathbb F_3,\quad c=0,\quad d=a^3+a,\quad L_+(a):=a^9+a^3-a=0.
\]
The second chart is exactly
\[
b\in\mathbb F_3,\quad c=a-a^3,\quad L_-(a):=a^9-a^3-a=0.
\]
Both \(L_+\) and \(L_-\) are separable monic polynomials of degree \(9\) (their derivatives equal \(-1\)). Each therefore has exactly nine distinct roots over an algebraic closure, yielding \(3\cdot9+3\cdot9+3+1=58\) lines. Uniqueness of echelon form prevents double counting between charts.

**Frobenius cycles.** Write \(\sigma(a)=a^3\). For a root of \(L_+\), the equation is \(\sigma^2+\sigma-1=0\) on the additive root space; for \(L_-\) it is \(\sigma^2-\sigma-1=0\). In either case substitution gives \(\sigma^4=-1\), hence \(\sigma^8=1\). Since \(\sigma^4(a)=-a\ne a\) for every nonzero root, no such root can have a Frobenius orbit of length \(1,2\), or \(4\). Its orbit length is therefore exactly \(8\). The eight nonzero roots of each polynomial form a single eight-cycle. The root \(0\) and the three choices of \(b\in\mathbb F_3\) contribute six fixed lines across the first two charts, while the last two nonempty charts give four further fixed lines. There are six eight-cycles and ten fixed points, as asserted. The line-count and zeta formulas follow from this complete Frobenius cycle decomposition.

**Scheme structure.** For a line \(\ell\subset X\), the normal sequence in the smooth quartic yields a degree-minus-two line bundle \(N_{\ell/X}\cong\mathcal O_{\mathbb P^1}(-2)\). Hence the Zariski tangent space to the Hilbert scheme at \([\ell]\), namely \(H^0(\ell,N_{\ell/X})\), vanishes. The Grassmannian calculation shows that the Hilbert scheme has exactly the listed isolated geometric points. Since its local rings are of finite type over a perfect field and have zero tangent spaces, each is a reduced point. Therefore \(\mathcal L\) is finite étale of degree \(58\).

## Verification
Run `python3 checker.py` from the directory containing this file. The dependency-free checker constructs the six Grassmannian substitutions in a polynomial ring over \(\mathbb F_3\) and independently verifies all thirty coefficient identities. It checks both degree-nine additive polynomials via Euclidean gcd with Frobenius powers for degrees \(1\) through \(8\) and directly enumerates the \(130\) two-dimensional subspaces of \(\mathbb F_3^4\), finding exactly ten contained lines. The finite computations provide independent cross-checks; the proof above establishes the assertions over the algebraic closure and all finite extensions.

## Relationship to prior work
Veniani [1, Example 5.1] gives the one-parameter family, its geometric \(58\)-line count and its line-incidence types. Degtyarev [2, Theorem 1.2 and Section 8.4] classifies the large geometric line configurations in characteristic three. Rams–Schütt [3] discuss the different \(112\)-line Fermat quartic and its \(\mathbb F_9\)-rational lines. The present result fixes a prime-field member of Veniani's \(58\)-line family and computes its entire Frobenius action on the geometric line set, equivalently the arithmetic of its finite étale line scheme. The named sources do not state this particular cycle decomposition or the displayed line-scheme zeta function. This comparison is not an exhaustive novelty guarantee.

## Limitations
The theorem does not claim the corresponding Frobenius decomposition for generic parameters or for either of the other two \(58\)-line families, and it does not determine the zeta function of the quartic surface itself. Literature beyond the identified full texts could contain an equivalent arithmetic computation. The claim is a self-contained exact calculation for the specified natural prime-field member, not a classification of all forms of the geometric surface.

## References
[1] D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (first version 2016-08-15), Example 5.1, https://arxiv.org/abs/1608.04209 .

[2] A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (2016-04-20), Theorem 1.2 and Section 8.4, https://arxiv.org/abs/1604.05836 .

[3] S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (2014-09-26), Example 2.1, https://arxiv.org/abs/1409.7485 .
