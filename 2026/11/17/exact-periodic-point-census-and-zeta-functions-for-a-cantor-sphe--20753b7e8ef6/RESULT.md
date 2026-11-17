# Exact periodic-point census and zeta functions for a Cantor-sphere Julia set

## Finding

Let \(d,m\) be integers satisfying \(d,m\ge 2\) and \(1/d+1/m<1\), and let \(f=f_{d,m}:\mathbb S^3\to\mathbb S^3\) be the uniformly quasiregular map constructed by Fletcher and Martin [1], whose Julia set is a Cantor family of round spheres. Put \(D=d^2+m^2\).

**Theorem (complete periodic census).** For every integer \(n\ge1\),
\[
\#\operatorname{Fix}(f^n|_{\mathcal J(f)})=D^n,
\qquad
\#\operatorname{Fix}(f^n)=D^n+1.
\]
More precisely, for each \(0\le r\le n\), the number of Julia-set points fixed by \(f^n\) whose length-\(n\) symbolic itinerary contains exactly \(r\) inner-branch symbols is
\[
\binom nr\bigl(d^{2(n-r)}m^{2r}+(-1)^r\bigr).
\]
In particular, all these fixed-point sets are finite, and their Artin–Mazur zeta functions are
\[
\zeta_{f|_{\mathcal J(f)}}(z)=\frac{1}{1-Dz},
\qquad
\zeta_f(z)=\frac{1}{(1-z)(1-Dz)}.
\]
The number of primitive Julia-set periodic orbits of least period \(n\) equals
\[
\frac1n\sum_{k\mid n}\mu(n/k)D^k,
\]
where \(\mu\) is the Möbius function. The full sphere has exactly one additional primitive orbit, the fixed point at infinity.

## Assumptions and scope

Only the particular three-dimensional maps \(f_{d,m}\) of [1, Theorem 1.1], with the two specified integer parameters, are covered. The result counts *distinct geometric points*, not multiplicity-weighted fixed points. A point fixed by an iterate is counted once for that iterate, even if its least period is smaller. The Artin–Mazur zeta is defined as the formal series
\[
\zeta_g(z)=\exp\left(\sum_{n\ge1}\frac{\#\operatorname{Fix}(g^n)}{n}z^n\right).
\]
The symbolic itinerary uses the two branches of [1, Proposition 6.3], the outer branch labelled \(1\) and the inner branch labelled \(2\); repeated itinerary symbols are counted with their positions.

## Proof

**1. The precise symbolic and angular model.** By [1, Proposition 6.3(i)], the Julia restriction is topologically conjugate to
\[
(\omega,\xi)\longmapsto (\sigma\omega,\Lambda_{\omega_0}\xi)
\quad\text{on }\{1,2\}^{\mathbb N_0}\times\mathbb S^2.
\]
The sphere is the pillow quotient of \(\mathbb T=\mathbb R^2/(2\mathbb Z^2)\) by the involution \(j(y)=-y\). The two angular maps descend from the toral endomorphisms \(y\mapsto dy\) and \(y\mapsto m(y_1,-y_2)\), respectively; these formulas are explicit in [1, Sections 2 and 6].

For each integer \(n\ge1\), a point of the one-sided full shift is fixed by \(\sigma^n\) precisely when it is the infinite repetition of a unique word \(w\in\{1,2\}^n\). Thus distinct length-\(n\) words contribute disjoint fixed-height spheres. If \(w\) has \(r\) inner symbols, its angular return map is induced by
\[
A_w=Q_w\operatorname{diag}(1,(-1)^r),\qquad Q_w=d^{n-r}m^r.
\]
The matrix commutes with \(j\); orientation reversals in the second coordinate cancel in pairs.

**2. Exact fixed points on the pillow.** More generally, let \(A=Q\operatorname{diag}(1,\varepsilon)\), where \(Q\ge2\) is an integer and \(\varepsilon\in\{1,-1\}\). A class \([y]\in\mathbb T/\{\pm1\}\) is fixed by the induced pillow map exactly when \(Ay\equiv y\) or \(Ay\equiv-y\) modulo \(2\mathbb Z^2\). On the torus let
\[
K_-=\ker(A-I),\qquad K_+=\ker(A+I),\qquad U=K_-\cup K_+.
\]
Both kernels are finite, with orders \(|\det(A-I)|\) and \(|\det(A+I)|\). This follows from the elementary index formula for a nonsingular integer matrix acting on the two-torus. The involution \(j\) preserves \(U\), and its fixed points in \(U\) are **exactly** \(K_-\cap K_+\). Indeed, membership in both implies \(2y=0\); conversely, a two-torsion point in either kernel belongs to both. Burnside's two-element orbit formula therefore yields
\[
\#(U/\{\pm1\})
=\frac{|U|+|K_-\cap K_+|}{2}
=\frac{|\det(A-I)|+|\det(A+I)|}{2}.
\]
If \(\varepsilon=1\), the two determinants have absolute values \((Q-1)^2\) and \((Q+1)^2\), giving \(Q^2+1\) pillow fixed points. If \(\varepsilon=-1\), both absolute determinants equal \(Q^2-1\), giving \(Q^2-1\) fixed points. The four branched pillow corners are included without double-counting.

**3. Cancellation across the two symbolic branches.** Each word \(w\) containing \(r\) inner symbols therefore contributes precisely
\[
Q_w^2+(-1)^r=d^{2(n-r)}m^{2r}+(-1)^r
\]
Julia points fixed by \(f^n\). There are \(\binom nr\) words with this count. Summation gives
\[
\sum_{r=0}^n\binom nr\Bigl(d^{2(n-r)}m^{2r}+(-1)^r\Bigr)
=(d^2+m^2)^n+(1-1)^n=D^n,
\]
because \(n\ge1\). This proves both the refined and total Julia census. The cancellation of the positive and negative pillow corrections is exact at every iterate.

**4. Fixed points outside the Julia set.** By [1, Theorem 1.1 and Theorem 6.1], every Fatou component other than the immediate basin of infinity is strictly preperiodic and eventually enters that basin, while all finite points in the immediate basin converge to infinity. Therefore no finite Fatou point can be periodic. The point \(\infty\) is fixed, providing exactly one additional point fixed by every iterate.

**5. Zeta functions and primitive orbits.** Substituting the counts into the defining series and using \(-\log(1-t)=\sum_{n\ge1}t^n/n\) proves the two rational zeta identities. Möbius inversion of \(\#\operatorname{Fix}(f^n|_{\mathcal J})=\sum_{k\mid n}P_k\), where \(P_k\) counts points of least period \(k\), gives \(P_n=\sum_{k\mid n}\mu(n/k)D^k\). Each primitive orbit of period \(n\) contains exactly \(n\) points. Infinity contributes one further period-one orbit and nothing for larger least periods. \(\square\)

## Verification

Run `python3 verify.py` using the included standalone file. It independently enumerates, on a sufficiently fine finite torus grid, the fixed pillow classes for eleven scalar/reflection examples, then checks the binary-word summation and primitive-orbit divisibility over five admissible parameter pairs through period eight. The observed output is:

```text
VERIFY_OK modular_pillow_instances=11 binary_words=2550 primitive_n_up_to=8
EXAMPLE_d2_m3 fixed_J_n_1_to_5 [13, 169, 2197, 28561, 371293]
FINITE_CHECK_ONLY proof_of_all_periods_is_analytical
```

The all-parameter, all-iterate result is established by the determinant/Burnside/binomial proof above, **not** by finite enumeration. The checker does not reproduce the global topological construction of [1], which is taken as the published premise.

## Relationship to prior work

Fletcher and Martin [1] construct the maps, prove the Cantor-sphere Julia model and the angular skew-product conjugacy, determine topological entropy \(\log D\), and establish density of repelling periodic points. The present theorem uses those results and determines the complete distinct-point census, including the itinerary-refined correction and its cancellation, and hence both Artin–Mazur zeta functions. The existence of a partition into \(D^n\) symbolic/toroidal cylinders in [1] does not on its own count geometric fixed points on the branched pillow quotient.

Classical Lattès theory [2] provides the background for torus-to-sphere quotients. Li [3] computes a different object—the proportion of elements of geometric iterated Galois groups fixing a preimage-tree vertex—not the number of geometric periodic points of this two-branch three-dimensional map. The index/determinant and finite-group orbit-count ingredients are standard; the claimed new fact is their exact application to this specific recently constructed system, especially the nontrivial sign cancellation and complete zeta function.

## Limitations

This result covers the explicitly constructed \(f_{d,m}\), not every uniformly quasiregular map of the same degree, all possible Cantor-sphere Julia sets, or the higher-dimensional variant discussed informally in [1]. It is not a statement about multiplicities, local indices, periodic-point equidistribution, or the uniqueness of measures of maximal entropy. Historical priority beyond the inspected material remains provisional; an exhaustive review of all classical orbifold and quasiregular periodic-point literature has not been completed. Independent validation has not been performed.

## References

[1] A. N. Fletcher and G. J. Martin, *Cantor's onion: a uniformly quasiregular map whose Julia set is a Cantor set of spheres*, arXiv:2611.08773v1 (public November 5, 2026), https://arxiv.org/html/2611.08773v1 . Relevant material: Sections 2–3, Theorem 1.1, Theorem 6.1, and Proposition 6.3.

[2] J. Milnor, *On Lattès Maps*, arXiv:math/0402147 (2004), https://arxiv.org/abs/math/0402147 . General Lattès background; only abstract and bibliographic material were accessible in the source comparison.

[3] X. Li, *The fixed-point proportion of Lattès maps*, arXiv:2611.07816v1 (public November 5, 2026), https://arxiv.org/html/2611.07816v1 . Relevant material: introduction and Sections 2–3; studies Galois fixed-point proportions rather than geometrical periodic-point counts.

[4] M. Artin and B. Mazur, *On periodic points*, Annals of Mathematics 81 (1965), 82–99, https://doi.org/10.2307/1970384 . Definition and context for the dynamical zeta function.
