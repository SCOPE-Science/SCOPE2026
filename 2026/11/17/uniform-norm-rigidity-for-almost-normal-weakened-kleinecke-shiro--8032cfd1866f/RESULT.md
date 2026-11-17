# Uniform norm rigidity for almost-normal weakened Kleinecke–Shirokov commutators

## Finding

**Theorem (dimension-free rigidity and its essential version).** Fix an integer \(m\ge1\). There is a nondecreasing function \(\omega_m:[0,\infty)\to[0,2]\) with \(\lim_{t\downarrow0}\omega_m(t)=0\), independent of matrix size and of the unital complex \(C^*\)-algebra, having the following property. If \(a,b\) are contractions in any such algebra, and \(y=[a,b]=ab-ba\), then
\[
 \|y\|\le\omega_m\!\left(\max\{\|[y^*,y]\|,\ \|\operatorname{ad}_y^m(a)\|\}\right),\qquad \operatorname{ad}_y(x)=yx-xy.
\]
In particular, for arbitrary \(M>0\) and \(\|a\|,\|b\|\le M\),
\[
 \|y\|\le M^2\omega_m\!\left(\max\{M^{-4}\|[y^*,y]\|,\ M^{-(2m+1)}\|\operatorname{ad}_y^m(a)\|\}\right).
\]
Consequently, if \(A,B\) act on a complex Hilbert space, \(Y=[A,B]\), and both \([Y^*,Y]\) and \(\operatorname{ad}_Y^m(A)\) are compact, then \(Y\) is compact. If, additionally, the iterated commutator is **zero**, then \(Y\) is also quasinilpotent. The bound is necessarily non-effective in the argument given: no explicit rate for \(\omega_m\) is established.

**Factor-bound boundary.** For every \(m\ge3\), there are bounded-operator commutators \(Y_\varepsilon\), \(\varepsilon\downarrow0\), with \(\|Y_\varepsilon\|\ge1\), \(\operatorname{ad}_{Y_\varepsilon}^m(A_\varepsilon)=0\), and \(\|[Y_\varepsilon^*,Y_\varepsilon]\|=\varepsilon^2\); every representation \(Y_\varepsilon=[A_\varepsilon,B_\varepsilon]\) has \(\|A_\varepsilon\|\|B_\varepsilon\|\to\infty\). Thus bounding the factors cannot be dropped from the uniform assertion. This boundary construction reuses the square-zero model and Brown–Pearcy theorem employed in the cited motivating paper, not a newly claimed existence theorem.

## Assumptions and scope

All algebras are unital complex \(C^*\)-algebras. Commutators are associative. In the Hilbert-space corollary the compact ideal is \(\mathcal K(H)\); no separability is assumed for this corollary. The factor-bound boundary example uses a separable infinite-dimensional Hilbert space. The function \(\omega_m\) is universal only at a **fixed** order \(m\) with uniformly bounded factors; it is not a claimed constructive modulus.

## Proof

**Step 1: an exact rigidity lemma.** For a normal operator \(N\) on a complex Hilbert space and \(X\) bounded, \(\operatorname{ad}_N^m(X)=0\) implies \([N,X]=0\). One direct proof uses the spectral measure \(P\) of \(N\). For two disjoint compact spectral sets \(E,F\), the map \(Z\mapsto (N|_{P(E)H})Z-Z(N|_{P(F)H})\) on operators between their spectral ranges is invertible: its spectrum is contained in \(E-F\), which excludes zero (the Lumer–Rosenblum spectral inclusion). Since its \(m\)-th power annihilates \(P(E)XP(F)\), that block vanishes. By regularity of scalar spectral measures, for any two disjoint Borel sets \(E,F\), compact approximations of the corresponding spectral vectors show \(P(E)XP(F)=0\). Choosing \(F\) to be the complement of \(E\) shows \(X\) commutes with every spectral projection of \(N\), hence with \(N\). A faithful Hilbert-space representation gives the same conclusion for normal elements of arbitrary \(C^*\)-algebras. This is an established normal-derivation ascent-one principle; compare Crabb–Spain and Ackermans–van Eijndhoven–Martens. It is included here with proof rather than claimed as a new lemma.

**Step 2: exact normal commutator rigidity.** Let \(y=[a,b]\) be normal and \(\operatorname{ad}_y^m(a)=0\). Step 1 gives \([y,a]=0\), or equivalently \([a,[a,b]]=0\). The classical Kleinecke–Shirokov theorem in unital Banach algebras gives \(r(y)=0\). Since \(y\) is normal in a \(C^*\)-algebra, \(\|y\|=r(y)\), so \(y=0\).

**Step 3: the uniform statement.** Define \(\omega_m(t)\) to be the supremum of \(\|[a,b]\|\) over all pairs of contractions in all unital complex \(C^*\)-algebras for which both defect norms in the displayed maximum do not exceed \(t\). This supremum belongs to \([0,2]\) and is nondecreasing. Suppose \(\omega_m(t)\not\to0\) as \(t\downarrow0\). There are \(t_j\downarrow0\) and unital \(C^*\)-algebras \(\mathcal A_j\) containing contractions \(a_j,b_j\) with defects tending to zero but \(\|[a_j,b_j]\|\ge c>0\). In a norm ultraproduct \(\prod_{\mathcal U}\mathcal A_j\) for any free ultrafilter, the classes \(a,b\) satisfy that \(y=[a,b]\) is normal and \(\operatorname{ad}_y^m(a)=0\), while \(\|y\|\ge c\). This contradicts Step 2. Therefore \(\omega_m(t)\to0\). For the scaled inequality take \(a'=a/M\), \(b'=b/M\), \(y'=y/M^2\), and note the exact defect factors \(M^{-4}\) and \(M^{-(2m+1)}\).

**Step 4: compactness and quasinilpotence.** Let \(\pi:\mathcal B(H)\to\mathcal B(H)/\mathcal K(H)\) be the quotient map. The hypotheses that both displayed defects are compact mean that \(y=\pi(Y)=[\pi(A),\pi(B)]\) is normal and \(\operatorname{ad}_y^m(\pi(A))=0\). Step 2 gives \(y=0\), hence \(Y\) is compact. When the iterated commutator is zero already in \(\mathcal B(H)\), Stanković's Corollary 3.2(ii) proves that this compact \(Y\) is quasinilpotent. Neither exactness nor quasinilpotence can be suppressed silently: if \(A=e_{12}\), \(B=e_{21}\) on \(\ell^2\), then \(Y=e_{11}-e_{22}\) is compact and normal and all its iterated defects are compact, but its spectrum includes \(1\) and \(-1\).

**Step 5: sharp qualitative factor-bound obstruction.** On \(H=H_0\oplus H_0\) with infinite-dimensional separable \(H_0\), set \(N=\begin{pmatrix}0&I\\0&0\end{pmatrix}\) and \(Y_\varepsilon=I+\varepsilon N\). For every \(\varepsilon>0\), \(N\) is noncompact with \(N^2=0\), hence \(Y_\varepsilon\) is not a nonzero scalar plus compact operator. The Brown–Pearcy characterization gives bounded \(A_\varepsilon,B_\varepsilon\) with \(Y_\varepsilon=[A_\varepsilon,B_\varepsilon]\). The binomial commutator identity gives \(\operatorname{ad}_{Y_\varepsilon}^3(X)=\varepsilon^3\operatorname{ad}_N^3(X)=0\) for **every** bounded \(X\), hence for every \(m\ge3\). Also \([Y_\varepsilon^*,Y_\varepsilon]=\varepsilon^2[N^*,N]\) and \(\|[N^*,N]\|=1\), whereas the spectrum of \(Y_\varepsilon\) is \(\{1\}\) and its norm is at least one. If \(\|A_\varepsilon\|\|B_\varepsilon\|\) stayed bounded along any sequence \(\varepsilon\downarrow0\), rescaling factors by reciprocal scalars would give equivalent representations with both factor norms bounded. The scaled rigidity inequality of Step 3 would force \(\|Y_\varepsilon\|\to0\), contradiction. Consequently every such factorization cost diverges.

## Verification

The proof is analytic. Step 1 explicitly checks separated-spectral-block invertibility and regularity of the spectral measure; Step 2 uses the established Kleinecke–Shirokov theorem; Step 3 relies on the norm ultraproduct identity for \(C^*\)-algebras, preserving products, involutions and norms. Step 4 is a quotient calculation, and Step 5 is the exact square-zero block computation with the standard Brown–Pearcy characterization. No finite sampling, experimental convergence, or machine certificate is treated as an infinite-dimensional proof.

## Relationship to prior work

Stanković (2026), Proposition 2.1 and Corollaries 3.2–3.3, proves non-quasinilpotent higher-commutator examples and positive conclusions for compact or Riesz commutators or compact first commutator. The present theorem instead gives a **simultaneous two-defect norm stability property uniformly across all \(C^*\)-algebras**, and a compactness conclusion when only the iterated relation is compact **modulo** the compact ideal. Crabb and Spain (1977) and Ackermans–van Eijndhoven–Martens (1983) supply the classical normal-derivation kernel rigidity. Lauric (2021) studies stability of generalized derivations for fixed normal multipliers in Schatten ideals; it does not establish the nonlinear, generator-varying, \(C^*\)-uniform commutator assertion. The Brown–Pearcy example, already used by Stanković, supplies the boundary after varying its square-zero amplitude. No originality is assigned to these antecedents.

## Limitations

The universal stability modulus is proved to exist but no explicit rate or optimal quantitative exponent is known here. The factor-bound counterexample concerns \(m\ge3\) and does not resolve the open \(m=2\) non-quasinilpotency case. The essential version concludes **compactness**, not quasinilpotence, unless the iterated relation vanishes exactly. The result does not classify general nonnormal commutators. The closest 1983 report on almost-commuting operators could not be retrieved in full; the stated classical assertions are also documented in Lauric's accessible full text. Publication priority is not independently certified.

## References

1. H. Stanković, *Quasinilpotency of commutators under a weakened Kleinecke–Shirokov condition*, arXiv:2611.06423v1, 4 November 2026, Proposition 2.1 and Corollaries 3.2–3.3. https://arxiv.org/abs/2611.06423
2. M. J. Crabb and P. G. Spain, *Commutators and normal operators*, Glasgow Math. J. 18 (1977), 197–198, Proposition 1. https://doi.org/10.1017/S001708950000327X
3. S. T. M. Ackermans, S. J. L. van Eijndhoven, and F. J. L. Martens, *On almost-commuting operators*, Indag. Math. 45 (1983), 385–391 (1983 report cited in Lauric). https://research.tue.nl/en/publications/on-almost-commuting-operators-2/
4. V. Lauric, *On a Kleinecke-Shirokov theorem*, Czechoslovak Math. J. 71 (2021), 817–822, Theorems 1.1–1.2 and 2.3. https://doi.org/10.21136/CMJ.2021.0103-20
5. A. Brown and C. Pearcy, *Structure of commutators of operators*, Ann. Math. 82 (1965), 112–127. https://doi.org/10.2307/1970564
