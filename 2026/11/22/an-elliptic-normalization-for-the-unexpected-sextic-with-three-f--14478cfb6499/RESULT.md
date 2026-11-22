# An elliptic normalization for the unexpected sextic with three fat base points

## Finding

Let \(P_1,\ldots,P_{13}\subset\mathbb P^2_{\mathbb C}\) be the thirteen points in Malara's Example 6.1 (specified below), and let \(Z=2P_1+2P_3+2P_{11}+\sum_{i\notin\{1,3,11\}}P_i\). For a general \(Q\in\mathbb P^2\), the unique unexpected sextic \(C_Q\) in \([I_Z\cap I_Q^4]_6\) is geometrically integral, has exactly four singularities, and has **no additional singularity**:

\[
\operatorname{Sing}(C_Q)_{\mathrm{red}}=\{P_1,P_3,P_{11},Q\}.
\]

The first three points are ordinary nodes and \(Q\) is an ordinary quadruple point (four smooth branches with distinct tangents). Consequently its smooth projective normalization has **genus one**, and its dual plane curve has **degree twelve**:

\[
\delta(C_Q)=3+\binom42=9,\qquad g(\widetilde C_Q)=10-9=1,\qquad \deg(C_Q^\vee)=6\cdot5-3(2)-4(3)=12.
\]

This is a generic-parameter statement, not a classification of exceptional positions of \(Q\).

## Assumptions and scope

Work over \(\mathbb C\). In homogeneous coordinates \((x:y:z)\), the fixed points, in order, are

\[
\begin{aligned}
&P_1=(1:0:0),\ P_2=(-1:1:0),\ P_3=(0:1:0),\ P_4=(1:1:0),\\
&P_5=(-1:-1:1),\ P_6=(1:-1:1),\ P_7=(-1:1:1),\ P_8=(1:1:1),\\
&P_9=(0:-1:1),\ P_{10}=(-1:0:1),\ P_{11}=(0:0:1),\\
&P_{12}=(1:0:1),\ P_{13}=(0:1:1).
\end{aligned}
\]

Here an ordinary \(r\)-fold point means a multiplicity-\(r\) plane-curve germ with \(r\) distinct tangent lines. Malara proves that the degree-six interpolation space has dimension one for general \(Q\); the new assertion concerns the entire geometric singularity basket, genus and dual class of that sextic.

## Proof

**1. A finite, exact witness.** Fix \(Q_0=(-31:-9:15)\), which is distinct from every fixed point. Put the 28 degree-six monomials in three variables into a column vector. The conditions of vanishing at each simple \(P_i\), of order at least two at \(P_1,P_3,P_{11}\), and of order at least four at \(Q_0\), give a \(29\times28\) rational jet matrix, using 2-dimensional affine charts at the marked points. Its rank is exactly 27, so its nullspace determines a unique nonzero homogeneous sextic \(F_0\). The exact construction (rather than a copied equation) is provided in `verify.py`.

**2. No other geometric singularities.** Write \(f_0(x,y)=F_0(x,y,1)\). A lexicographic rational Gröbner basis for the ideal \((f_0,\partial_x f_0,\partial_y f_0)\) has terminal eliminant

\[
\frac{y(5y+3)^5}{3125}.
\]

At \(y=0\), specializing the full Gröbner basis yields common polynomial \(x\). At \(y=-3/5\), its common polynomial is a nonzero multiple of \((15x+31)^3\). Thus the singular support in \(z\ne0\) is exactly \((0:0:1)\) and \((-31:-9:15)\). On the line at infinity the exact identity

\[
F_0(x,y,0)=50625x^2y^2(x-y)(x+y)
\]

and the gradients show that the only other singular points are \((1:0:0)\) and \((0:1:0)\).

**3. Ordinary tangent cones.** The three marked fixed singularities have multiplicity two, and the marked moving point has multiplicity four. In local coordinates at \(Q_0\), the degree-four initial form is, up to nonzero scalar,

\[
230U^4+276U^3V-330UV^3-99V^4.
\]

Its dehomogenized discriminant is \(-8274020159477952\ne0\). The three quadratic tangent discriminants are \(432900\), \(655525872900\), and \(265357166724\), all nonzero, so all four germs are ordinary. These exact equalities are checked independently by `verify.py` using derivatives of the reconstructed polynomial.

**4. Absolute irreducibility.** The four points are isolated singularities, so \(F_0\) has no repeated irreducible factor. Suppose it were reducible, and let an irreducible component of degree \(e\le3\) meet the residual curve of degree \(6-e\). Every intersection lies among the four singular points. Because all local tangent directions at each singularity are distinct, local intersection multiplicities between distinct components equal products of their local multiplicities. At the ordinary quadruple point their total is at most 4, and the three nodes contribute at most 3 in total. Bézout would give \(e(6-e)\le7\). As \(2\cdot4=8\) and \(3\cdot3=9\), a reducible sextic must therefore have a **line** component. Such a line must pass through \(Q_0\), since otherwise its intersections would total at most three, less than five. It must also meet \(z=0\) at one of the four roots of \(F_0(x,y,0)\); hence it is one of

\[
5y+3z=0,\quad15x+31z=0,\quad15x-15y+22z=0,\quad3x+3y+8z=0.
\]

Direct substitution into \(F_0\) rules out all four factors, as in the checker. Thus \(C_{Q_0}\) is geometrically integral.

**5. Passing to the general member.** The rank-27 interpolation condition holds on a nonempty open parameter set, giving a rational algebraic family of unique sextics (also established in Malara's Proposition 6.1). Blow up the four disjoint moving and fixed sections \(P_1,P_3,P_{11},Q\) of the relative projective plane. At \(Q_0\) the strict transform is smooth everywhere, including above the four marked points, since their tangent cones are reduced. Smoothness of this proper family of strict transforms, together with the distinct-tangent condition, holds on a nonempty Zariski-open neighborhood of \(Q_0\). The closed locus of reducible sextics does not contain the example, and can be removed from this open set. Thus a general member is integral with precisely the four asserted ordinary singularities.

**6. Genus and dual degree.** A degree-six integral plane curve has arithmetic genus ten. Its three nodes contribute delta one each, while an ordinary quadruple contributes \(\binom42=6\), hence its normalization has genus one. The characteristic-zero polar formula for ordinary multiple points gives class \(6(6-1)-\sum r(r-1)=30-6-12=12\), the degree of the dual curve.

## Verification

Run `python3 verify.py` with SymPy. The checker reconstitutes all fixed and moving jet constraints, confirms the exact rank and all vanishing conditions, calculates the complete projective singular support via a Gröbner basis and the chart at infinity, checks the four initial-form discriminants, and tests the only four possible line factors. The exact certificate is for \(Q_0\); algebraic openness and the proof above, not sample enumeration, justify the generic conclusion.

## Relationship to prior work

Malara, *Fat base schemes and unexpected hypersurfaces of type \((d+k,d)\)*, arXiv:2611.04564v1, Proposition 6.1, establishes the surprising dimension of the interpolation system and exhibits geometric irreducibility at \(Q_0\). It does not assert the completed singularity census, elliptic normalization, or dual degree. The older general unexpected-hypersurface methodology controls dimensions rather than these precise invariants. Previously reported quartic singularity examples concern different fixed schemes and do not imply this genus-one sextic result.

## Limitations

This theorem describes only a nonempty Zariski-open subset of moving points \(Q\). It does not classify the discriminant of exceptional positions, an explicit elliptic Weierstrass model or the variation of the elliptic \(j\)-invariant. The proof uses characteristic zero; special reductions modulo primes are not analyzed. The normalization is identified as a smooth genus-one curve but no distinguished rational origin is imposed.

## References

1. G. Malara, *Fat base schemes and unexpected hypersurfaces of type \((d+k,d)\)*, arXiv:2611.04564v1 (first public November 3, 2026), https://arxiv.org/html/2611.04564v1, especially Section 6.1.
2. M. Janasz, G. Malara and H. Tutaj-Gasińska, *Unexpected hypersurfaces of type \((d+k,d)\)*, arXiv:2511.10772 (general background; source text not fully retrieved).
3. B. Harbourne, J. Migliore and U. Nagel, *Unexpected hypersurfaces and their consequences: a survey* (2024), cited in Malara, reference [11].
