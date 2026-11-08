# Arithmetic wall crossing in twisted triangular Fermat line divisors

## Finding

Let \(k\) be a field, \(n\geq2\) an integer invertible in \(k\), and \(a,b,c\in k^\times\). Let \(D_{a,b,c}\subset\mathbb P^2_k\) be the reduced degree-\(3n\) divisor
\[
D_{a,b,c}:\quad (X^n-aY^n)(Y^n-bZ^n)(Z^n-cX^n)=0.
\]
Write \(E_v=\operatorname{Spec}k[t]/(t^n-v)\) for \(v\in k^\times\), and \(\mathbb L=[\mathbb A^1_k]\). Products of schemes in brackets denote fiber products over \(k\). The following **arithmetic incidence identity** holds in \(K_0(\operatorname{Var}_k)\):
\[
\boxed{[D_{a,b,c}]=3+\mathbb L([E_a]+[E_b]+[E_c])-\begin{cases}
[E_a\times E_b]+[E_b\times E_c]+[E_c\times E_a],&abc\ne1,\\
2[E_a\times E_b],&abc=1.
\end{cases}}
\]
The reduced geometric divisor comprises \(3n\) lines in three pencils. In the regime \(abc\ne1\), its singularities are exactly three ordinary \(n\)-fold vertices and \(3n^2\) ordinary double points. In the regime \(abc=1\), its singularities are exactly three ordinary \(n\)-fold vertices and \(n^2\) ordinary triple points; the geometric triple-point scheme is the finite étale scheme \(E_a\times E_b\). No other singularities occur. At \(n=2\), an ordinary \(n\)-fold vertex is simply a node.

If \(k=\mathbb F_q\), for each \(r\ge1\) put \(Q=q^r\) and \(N_v(r)=\#\{t\in\mathbb F_Q:t^n=v\}\). Then
\[
\boxed{\#D_{a,b,c}(\mathbb F_Q)=3+Q\bigl(N_a(r)+N_b(r)+N_c(r)\bigr)-\begin{cases}
N_a(r)N_b(r)+N_b(r)N_c(r)+N_c(r)N_a(r),&abc\ne1,\\
2N_a(r)N_b(r),&abc=1.
\end{cases}}
\]
Here \(N_v(r)\) is explicitly \(h_r=\gcd(n,Q-1)\) if \(v^{(Q-1)/h_r}=1\), and zero otherwise. Writing \(Z(Y,T)=\exp(\sum_{r\ge1}\#Y(\mathbb F_{q^r})T^r/r)\) for the Hasse--Weil zeta function of any finite-type \(\mathbb F_q\)-scheme \(Y\), the **complete zeta function** is
\[
\boxed{Z(D_{a,b,c},T)=\frac{Z(E_a,qT)Z(E_b,qT)Z(E_c,qT)}{(1-T)^3}\cdot\begin{cases}
\bigl(Z(E_a\times E_b,T)Z(E_b\times E_c,T)Z(E_c\times E_a,T)\bigr)^{-1},&abc\ne1,\\
Z(E_a\times E_b,T)^{-2},&abc=1.
\end{cases}}
\]
Every zero-dimensional zeta factor is finite and rational, given by its Frobenius orbit lengths.

In particular, over \(\mathbb F_7\), choose \(n=3\) and \((a,b,c)=(2,2,2)\). None of the nine geometric component lines descends to \(\mathbb F_7\), although the divisor has three rational points. Indeed, \(t^3-2\) is irreducible over \(\mathbb F_7\) and
\[
\boxed{\#D_{2,2,2}(\mathbb F_{7^r})=\begin{cases}3,&3\nmid r,\\9\cdot7^r-15,&3\mid r,\end{cases}\qquad
Z(D_{2,2,2},T)=\frac{(1-T^3)^6}{(1-T)^3(1-7^3T^3)^3}.}
\]
Thus the same geometrically nonempty nine-line arrangement has exactly three rational points over infinitely many finite base fields \(\mathbb F_{7^r}\), namely those with \(3\nmid r\).

## Assumptions and scope

The characteristic of \(k\) must not divide \(n\); this ensures that every \(E_v\) is finite étale of degree \(n\) and that the three binomial factors are geometrically reduced into distinct lines. All three parameters are nonzero. Both the arithmetic identities and the geometric singularity classifications hold without assuming that \(k\) contains \(n\)-th roots of unity or the roots of any parameter. The finite-field counts and Hasse--Weil zeta identity are additional conclusions for \(k=\mathbb F_q\). No assertion is made for the nonreduced cases when \(\operatorname{char}(k)\mid n\).

## Proof

**Geometric line families.** Over a separable closure of \(k\), the three factors split into the lines
\[
A_u:\ X=uY\ (u^n=a),\qquad B_v:\ Y=vZ\ (v^n=b),\qquad C_w:\ Z=wX\ (w^n=c).
\]
Each family consists of \(n\) distinct lines through one of the three coordinate vertices, and the three vertices are disjoint. An intersection of one line from each family exists if and only if \(uvw=1\), hence only if \(abc=1\). Conversely, if \(abc=1\), every ordered choice \((u,v)\in E_a\times E_b\) gives the unique compatible \(w=(uv)^{-1}\in E_c\). This identifies the reduced triple-point locus over \(k\) with \(E_a\times E_b\). The remaining intersections of different families are geometrically distinct double points exactly when \(abc\ne1\). All branches are distinct linear forms, so their tangent directions are distinct, giving ordinary multiple points. The three vertices and the stated inner intersections exhaust all pairs of distinct lines.

**Arithmetic form of the normalization.** The normalization is the disjoint union
\[
\widetilde D=(E_a\times\mathbb P^1_k)\sqcup(E_b\times\mathbb P^1_k)\sqcup(E_c\times\mathbb P^1_k),
\]
where each factor parameterizes one of the three geometrically split families. At the coordinate vertex of the \(A\)-pencil, the normalization fiber is \(E_a\) while the vertex itself is \(\operatorname{Spec}k\). Thus that vertex contributes the correction \(1-[E_a]\); similarly for \(b,c\). If \(abc\ne1\), the three disjoint double-point schemes are \(E_a\times E_b\), \(E_b\times E_c\), \(E_c\times E_a\); each double-point locus contributes minus its own Grothendieck class. If \(abc=1\), the only inner singular scheme is \(E_a\times E_b\), whose normalization fiber consists of three copies of that scheme; its correction is minus twice its class. The scissors relation in the Grothendieck ring now gives
\[
[D]=(\mathbb L+1)\sum_v[E_v]+\bigl(3-\sum_v[E_v]\bigr)-\text{inner corrections},
\]
which simplifies to the boxed identity. This identity retains the residue fields of nonrational geometric components and of their nonrational intersection points; replacing \([E_v]\) by the geometric degree \(n\) would be wrong over a nonsplitting ground field.

**Arithmetic realization.** For finite \(k\), the operation \([Y]\mapsto\#Y(\mathbb F_{q^r})\) is a ring homomorphism \(K_0(\operatorname{Var}_k)\to\mathbb Z\). It sends \(\mathbb L\) to \(q^r\), and finite-étale products to products of fixed-point counts, proving the point formula for every \(r\). The multiplicative group of \(\mathbb F_{q^r}\) is cyclic, so the power map \(t\mapsto t^n\) on its nonzero elements has kernel of size \(h_r\); the stated criterion computes every \(N_v(r)\). Applying \(\exp(\sum_{r\ge1}(-)T^r/r)\) to the additive count identity gives exactly the displayed zeta product. The zeta of a finite étale scheme with Frobenius cycles of lengths \(d_i\) is \(\prod_i(1-T^{d_i})^{-1}\), establishing rationality.

**Nonsplit example.** Cubes in \(\mathbb F_7^\times\) are \(1\) and \(-1\). Consequently \(t^3-2\) has no root and is an irreducible cubic. The finite étale scheme \(E_2\) is \(\operatorname{Spec}\mathbb F_{343}\), with one Frobenius 3-cycle, and \(E_2\times E_2\) is the disjoint union of three copies of \(\operatorname{Spec}\mathbb F_{343}\). Since \(2^3=1\) in \(\mathbb F_7\), this is the triple-point regime. Hence \(N_2(r)=0\) unless \(3\mid r\), and \(N_2(r)=3\) otherwise. Substitution yields the claimed point counts and zeta product. In particular, all the geometric component lines have parameter roots of degree three, while the three coordinate vertices are rational.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. The checker independently enumerates every projective point for 11,994 combinations of prime characteristic, admissible degree and nonzero coefficients over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13}\); it compares the direct reduced-divisor equation with the finite-étale formula. It additionally constructs \(\mathbb F_{343}=\mathbb F_7[u]/(u^3-2)\) by exact polynomial arithmetic and independently counts \(3,072\) points of the stated divisor over that field. These exhaustive tests over specified finite fields confirm implementation and edge cases; the proof above, not the tests, justifies all degrees, fields and extensions.

## Relationship to prior work

Szpond, *Fermat-type arrangements* (arXiv:1909.04089, public September 9, 2019), reviews the classical split Fermat/Ceva arrangement, derived point configurations and reflection arrangements over \(\mathbb C\). Marchesi and Vallès, *Triangular arrangements on the projective plane* (arXiv:1903.08885), analyze combinatorial triple-point constraints in three pencils and characterize roots-of-unity arrangements; the concurrence criterion is a known geometric ingredient, not asserted to be new here. Kutler and Usatine, *Motivic zeta functions of hyperplane arrangements*, study Denef--Loeser motivic zeta functions of arrangements over algebraically closed fields; those functions are not the ground-field Hasse--Weil zeta function of the reduced divisor computed here. The contribution assessed here is the exact finite-étale descent formula for all three coefficient torsors, with the two concurrency regimes and the all-extension Hasse--Weil arithmetic. General inclusion--exclusion and standard finite-field Frobenius counting are acknowledged tools, not independent discoveries.

## Limitations

There is no claim of a new geometric classification of split Fermat arrangements, of a new general theorem on Grothendieck rings, or of any nontrivial statement in characteristics dividing \(n\). The result does not compute Jacobian or fundamental-group invariants of the complement. The elementary nature of the normalization argument raises a historical-priority risk: an older arithmetic arrangement treatment might contain an equivalent formula under different notation. The primary sources inspected and the targeted searches did not identify such a statement, but absence from those sources is not proof of global uniqueness.

## References

1. J. Szpond, *Fermat-type arrangements*, arXiv:1909.04089 (first public September 9, 2019), https://arxiv.org/abs/1909.04089.
2. S. Marchesi and J. Vallès, *Triangular arrangements on the projective plane*, arXiv:1903.08885 (first public March 21, 2019), https://arxiv.org/abs/1903.08885.
3. M. Kutler and J. Usatine, *Motivic zeta functions of hyperplane arrangements*, Math. Proc. Cambridge Philos. Soc. 175 (2023), 187--215, doi:10.1017/S0305004123000099.
