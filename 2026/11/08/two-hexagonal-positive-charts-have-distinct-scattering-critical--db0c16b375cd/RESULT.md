# Two hexagonal positive charts have distinct scattering critical-point degrees

## Finding

For the two positive charts of one smooth hexagonal toric surface constructed in Calvo Cortes–Telen, *Positive Charts of Toric Varieties*, Example 4.2, let their very affine loci be \(V_{\mathrm I}\) and \(V_{\mathrm{II}}\). Their topological Euler characteristics and generic logarithmic critical-point counts are
\[
\chi(V_{\mathrm I})=\operatorname{MLdeg}(V_{\mathrm I})=5,\qquad
\chi(V_{\mathrm{II}})=\operatorname{MLdeg}(V_{\mathrm{II}})=4.
\]
Here \(\operatorname{MLdeg}\) means the number of reduced critical points of a generic logarithmic one-form induced by monomial functions in the six Cox coordinates (equivalently, by a generic master function in the parametrization below). In particular, their generic scattering equations have five and four solutions, respectively. Although both charts have the same smooth hexagonal fan and the same positive-polytope combinatorics, their very affine loci are not isomorphic because their Euler characteristics differ. This does *not* assert that the full affine chart varieties are nonisomorphic as abstract varieties.

## Assumptions and scope

Work over \(\mathbb C\). Set \(T=(\mathbb C^*)^2\), with coordinates \((x,y)\), and define
\[
A=1+x,\quad B=1+y,\quad C=1+x+xy,\quad D=1+y+xy,\quad E=1+xy.
\]
The two smooth very affine surfaces are
\[
V_{\mathrm I}=T\setminus V(ABCD),\qquad
V_{\mathrm{II}}=T\setminus V(ABCE).
\]
These are exactly the torus-intersection loci \(U^\circ\) in the two constructions of Example 4.2, where the four Newton polynomials are \((A,B,C,D)\) and \((A,B,C,E)\), respectively. The last polynomial \(E\) follows from the source's alternative Cox equation \(u_1u_2+u_3u_4=1\): in the source's torus coordinates \(x=u_3u_6/(u_2u_5)\), \(y=u_4u_5/(u_1u_6)\), one has \(xy=u_3u_4/(u_1u_2)\). Corresponding positive charts are defined over \(\mathbb C\) and contain the same nonnegative toric hexagon.

For any \(H\in\{D,E\}\) consider the multivalued master function
\[
\Phi_H=x^{\alpha}y^{\beta}A^{\gamma}B^{\delta}C^{\epsilon}H^{\zeta},
\]
where the six exponents are independent generic complex parameters. Only the logarithmic differential \(d\log\Phi_H\) is used; its number of critical points does not depend on branch choices. The unimodular toric parametrization identifies the parameter space of these forms with the space arising from the six Cox exponents.

## Proof

**1. Euler characteristics of the deleted curves.** Write \(A_0,B_0,C_0,D_0,E_0\) for their zero curves inside \(T\). We use the topological Euler characteristic and finite additivity for complex algebraic varieties. The curves \(A_0\) and \(B_0\) are each isomorphic to \(\mathbb C^*\), so have Euler characteristic zero. The curve \(E_0\), given by \(xy=-1\), is also isomorphic to \(\mathbb C^*\).

On \(C_0\) one has \(y=-(1+x)/x\); the constraints \(x,y\ne0\) identify \(C_0\) with \(\mathbb C^*\setminus\{-1\}\). Similarly \(D_0\) is the locus \(x=-(1+y)/y\), parametrized by \(y\in\mathbb C^*\setminus\{-1\}\). Consequently
\[
\chi(A_0)=\chi(B_0)=\chi(E_0)=0,
\qquad \chi(C_0)=\chi(D_0)=-1.
\]

**2. All intersections, first chart.** Direct substitution in the defining equations shows that the only nonempty intersections of *distinct* curves among \(A_0,B_0,C_0,D_0\) are
\[
A_0\cap B_0=\{(-1,-1)\},\qquad
C_0\cap D_0=\{(\omega,\omega),(\omega^2,\omega^2)\},
\]
where \(\omega\) is a primitive cubic root of unity. In the second intersection \(C-D=x-y\), so \(x=y\) and \(x^2+x+1=0\). Every other pair is disjoint *in the torus*, and there are no triple intersections. Hence inclusion–exclusion gives
\[
\chi(A_0\cup B_0\cup C_0\cup D_0)
=(0+0-1-1)-(1+2)=-5.
\]
As \(\chi(T)=0\), this yields \(\chi(V_{\mathrm I})=5\).

**3. All intersections, second chart.** For \(A_0,B_0,C_0,E_0\), the only nonempty intersections are the three singletons
\[
A_0\cap B_0=\{(-1,-1)\},\quad
A_0\cap E_0=\{(-1,1)\},\quad
B_0\cap E_0=\{(1,-1)\}.
\]
The equation \(C=0=E\) would force \(x=0\), excluded by the torus; the remaining pairs involving \(C_0\) likewise have no torus points. There are no triple intersections. Therefore
\[
\chi(A_0\cup B_0\cup C_0\cup E_0)
=(0+0-1+0)-3=-4,
\]
and \(\chi(V_{\mathrm{II}})=4\).

**4. Generic logarithmic critical points.** Each \(V_H\) is a smooth, two-dimensional very affine variety (an open subset of the algebraic torus). The logarithmic one-forms of the above master functions are induced from generic linear combinations of the six coordinate logarithms on the Cox torus, because the torus parametrization is a unimodular monomial change of coordinates followed by inversion of \(A,B,C,H\). In particular the parameter family is the generic family needed in Huh's maximum-likelihood-degree theorem. That theorem states that on a smooth very affine variety of complex dimension \(d\), a generic logarithmic form has \((-1)^d\chi\) reduced zeros. Here \(d=2\), so these counts are \(5\) and \(4\). The same critical equations are identified with the scattering equations in Calvo Cortes–Telen, Section 5. As the two Euler characteristics differ, the two very affine loci cannot be isomorphic as algebraic varieties.

## Verification

The standalone script `verify_hexagon_ml.py` uses exact rational arithmetic in SymPy. For the specific exponent vector \((\alpha,\beta,\gamma,\delta,\epsilon,\zeta)=(2,3,5,7,11,13)\), it forms the two logarithmic critical-point equations, clears denominators, and saturates by \(xyABCH\) using an inverse variable \(z\). With lexicographic order \(z>y>x\), the leading monomials of the resulting Gröbner basis are exactly \(z,y,x^5\) in case I and \(z,y,x^4\) in case II. The univariate eliminants are squarefree:
\[
\begin{split}
p_{\mathrm I}(x)&=6045x^5+12908x^4-979x^3-13807x^2-8409x-924,\\
p_{\mathrm{II}}(x)&=6045x^4+8189x^3+4634x^2+1796x+256.
\end{split}
\]
Thus these explicit parameter choices already have the claimed reduced critical-point counts, including the prescribed exclusions. The general result uses the preceding topological argument, not extrapolation from these test cases. Run `python verify_hexagon_ml.py` with SymPy installed; no external data are required.

## Relationship to prior work

Calvo Cortes and Telen, Example 4.2, explicitly construct both positive charts, giving degrees \(10\) and \(7\) as affine complete intersections. Their Section 5 (via Huh's theorem) explains that generic scattering solutions are counted by the Euler characteristic of the very affine locus, and evaluates a *different pentagonal* example. The present calculation evaluates the **two hexagonal** Euler characteristics and exhibits the difference \(5\ne4\), a stronger comparison than the already-known difference of their affine embedding degrees. The earlier representation-theoretic construction of Arkani-Hamed and collaborators includes the first hexagonal chart; it does not state the paired scattering counts. Neither the general ML-degree theorem nor the known chart presentations numerically determines these two specific invariants without the intersection analysis.

## Limitations

This is an exact calculation for the two specified positive charts, not a formula for arbitrary positive charts of a fixed fan. The nonisomorphism conclusion applies to their **very affine loci**, not automatically to the entire chart varieties. Equality of the nonnegative polytope combinatorics does not imply equality of complex-complement topology. The formula counts zeros of a *generic* logarithmic one-form; exceptional exponents can produce fewer distinct critical points or degenerate critical schemes. Published priority beyond the inspected sources is not independently certified.

## References

1. V. Calvo Cortes and S. Telen, *Positive Charts of Toric Varieties*, arXiv:2602.16414 (first submitted 2026-02-18), Example 4.2 and Section 5. https://arxiv.org/abs/2602.16414
2. N. Arkani-Hamed, H. Frost, P.-G. Plamondon, G. Salvatori, and H. Thomas, *Configuration Spaces of Finite Representation Type Algebras*, arXiv:2512.24870 (2025), Example 13.2. https://arxiv.org/abs/2512.24870
3. J. Huh, *The maximum likelihood degree of a very affine variety*, Compositio Math. 149 (2013), 1245–1266, Theorem 1 (also cited in reference 1).
