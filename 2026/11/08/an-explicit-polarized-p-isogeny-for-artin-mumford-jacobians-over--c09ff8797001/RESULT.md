# An explicit polarized \(p\)-isogeny for Artin–Mumford Jacobians over \(\mathbb F_p\)

## Finding
For every odd prime \(p\), the Artin–Mumford curve \(C/\mathbb F_p\), the smooth projective model of
\[
(x^p-x)(y^p-y)=1,
\]
admits a canonical correspondence isogeny of Jacobians associated with its non-axis diagonal translation subgroups. Let \(t\) run over \(\mathbb F_p^\times\). Define \(D_t\) as the smooth projective model of
\[
z^p-z=w^{-1}-tw,
\]
and \(\pi_t:C\to D_t\) by \(w=x^p-x\), \(z=y-tx\). Let \(B=\prod_{t\ne0}J(D_t)\), and define
\[
\Phi((a_t)_t)=\sum_t\pi_t^*a_t,\qquad
\Psi(a)=(\pi_{t*}a)_t.
\]
Then **both** correspondence compositions are multiplication by \(p\):
\[
\Psi\circ\Phi=[p]_B,\qquad\Phi\circ\Psi=[p]_{J(C)}.
\]
For the canonical principal polarizations \(\lambda_C\) and \(\lambda_B\) (the product polarization on \(B\)),
\[
\Phi^*\lambda_C=p\lambda_B,\qquad
\deg(\Phi)=p^{(p-1)^2}.
\]
The scheme-theoretic kernel is a maximal isotropic subgroup scheme of \(B[p]\) of length \(p^{(p-1)^2}\). This is a statement about degree and the polarization pairing, not an identification of the group scheme as étale or multiplicative.

If \(\eta\in\mathbb F_p^\times\) is any nonsquare, writing \(r=(p-1)/2\) gives the \(\mathbb F_p\)-isogeny
\[
J(C)\sim_{\mathbb F_p}J(D_1)^r\times J(D_\eta)^r,
\]
and the two quotient Jacobians appearing here are **not isogenous to one another over \(\mathbb F_p\)**. Accordingly their Hasse–Weil numerator polynomials obey
\[
L_C(T)=L_{D_1}(T)^r L_{D_\eta}(T)^r.
\]
No assertion is made that either quotient Jacobian is geometrically simple or that the two factors share no simple isogeny constituents.

## Assumptions and scope
Here \(p\ge3\) is an odd prime, all curves and morphisms are over \(\mathbb F_p\), and \(J(X)\) denotes the connected degree-zero Picard variety of the smooth projective curve \(X\). For a finite morphism \(\pi\), \(\pi^*\) is pullback on Jacobians and \(\pi_*\) is the norm. Polarizations are the canonical principal ones on Jacobians. The multiplicity \(p\lambda_B\) is multiplication of the polarization morphism, **not** a claim of a separable isogeny. The claim concerns the particular map \(\Phi\), not the minimum possible degree among all isogenies.

## Proof
**1. Quotients and genera.** Let \(G\cong\mathbb F_p^2\) act by translations \((x,y)\mapsto(x+a,y+b)\). Put \(w=x^p-x\). Then \(\mathbb F_p(C)^G=\mathbb F_p(w)\), since \(y^p-y=w^{-1}\), and \(C\to\mathbb P^1_w\) has degree \(p^2\). The only inertia groups arise over \(w=0,\infty\), with respective translation directions the \(y\)- and \(x\)-axes. The two simple-pole Artin–Schreier equations give different exponent \(2(p-1)\) at each of \(p\) points above each pole, hence Riemann–Hurwitz yields
\[
2g(C)-2=-2p^2+4p(p-1),\qquad g(C)=(p-1)^2.
\]
For \(t\ne0\), the diagonal subgroup \(H_t=\langle(1,t)\rangle\) meets both inertia groups trivially. The quotient map \(\pi_t:C\to C/H_t\) is therefore finite étale of degree \(p\). Its invariant field is \(\mathbb F_p(w,z)\), since \(z=y-tx\) and
\[
z^p-z=(y^p-y)-t(x^p-x)=w^{-1}-tw.
\]
The Artin–Schreier equation has two simple poles, so \(g(D_t)=p-1\). Thus \(\dim(B)=(p-1)^2=g(C)\).

**2. Orthogonal norm and pullback.** The standard norm identity for a degree-\(p\) curve cover is \(\pi_{t*}\pi_t^*=[p]\). For \(t\ne s\), the two distinct lines \(H_t,H_s\subset G\) generate \(G\), and the common quotient \(C/\langle H_t,H_s\rangle=C/G\) has genus zero. Equivalently, the fiber-product correspondence for \(C\simeq D_t\times_{\mathbb P^1_w}D_s\) gives
\[
\pi_{t*}\pi_s^*=q_t^*q_{s*}=0,
\]
where \(q_j:D_j\to\mathbb P^1_w\), and the last map is zero because \(J(\mathbb P^1)=0\). It follows that \(\Psi\Phi=[p]_B\).

**3. Exact polarized isogeny.** The identity \(\Psi\Phi=[p]_B\) implies \(\ker\Phi\subseteq B[p]\), hence \(\ker\Phi\) is finite. Since \(\dim B=\dim J(C)\), \(\Phi\) is an isogeny. Cancelling this surjective map in \(\Phi\Psi\Phi=[p]\Phi\) gives \(\Phi\Psi=[p]_{J(C)}\). Pullback and norm are dual with respect to the canonical Jacobian polarizations, so \(\Phi^\dagger=\Psi\) and therefore
\[
\Phi^*\lambda_C=\lambda_B\circ\Phi^\dagger\Phi=p\lambda_B.
\]
Taking degrees of both sides as polarization homomorphisms, using \(\deg[p]_B=p^{2g(C)}\) and the two principal polarizations, gives \((\deg\Phi)^2=p^{2g(C)}\). Thus \(\deg\Phi=p^{g(C)}\). Because \(\Phi^*\lambda_C=p\lambda_B\) and \(\lambda_C\) is principal, the kernel of \(\Phi\) is maximal isotropic for the Weil pairing of \(p\lambda_B\), as a finite subgroup **scheme**, with exactly that length.

**4. Arithmetic square-class splitting.** The automorphism \((x,y)\mapsto(u x,u^{-1}y)\), for \(u\in\mathbb F_p^\times\), sends \(H_t\) to \(H_{t/u^2}\). Consequently the \(p-1\) quotient curves fall into at most two \(\mathbb F_p\)-isomorphism classes, represented by \(D_1,D_\eta\), each appearing \(r=(p-1)/2\) times. To distinguish them, observe that for \(w,z\in\mathbb F_p\), the left side \(z^p-z\) vanishes, so affine rational points require \(w\ne0\) and \(w^{-1}-tw=0\), or \(w^2=t^{-1}\). When \(t\) is square this has two solutions and each allows exactly \(p\) values of \(z\); when \(t\) is nonsquare there are none. The smooth Artin–Schreier completion has one rational point over each pole \(w=0,\infty\). Hence \(\#D_t(\mathbb F_p)=2p+2\) in the square class, and \(2\) in the nonsquare class. Curves with isogenous Jacobians over \(\mathbb F_p\) have equal Frobenius traces and thus equal point counts, so these Jacobians are not \(\mathbb F_p\)-isogenous. Finally the isogeny \(\Phi\) yields the asserted factorization of Frobenius numerator polynomials.

## Verification
The included `verify.py` independently enumerates rational points on \(C\) and each \(D_t\) over \(\mathbb F_p\) and \(\mathbb F_{p^2}\) for \(p=3,5,7,11\), using an explicitly constructed quadratic extension. It verifies the two-square-class point counts and, at both extension degrees, the trace identity
\[
\#C(\mathbb F_{p^e})-(p^e+1)
=\sum_{t\ne0}\big(\#D_t(\mathbb F_{p^e})-(p^e+1)\big).
\]
Its output is recorded in `verification_output.txt`. The finite calculations **do not prove** the all-prime isogeny or scheme-theoretic polarization statements: these follow from the geometric correspondence and duality arguments above.

## Relationship to prior work
The curve, its genus and automorphism group are classical. Arakelian–Korchmáros (2015) treat its automorphism characterization and explicitly discuss order-\(p\) hyperelliptic quotients. General Kani–Rosen idempotent decompositions imply **unpolarized rational isogeny existence** for collections of commuting subgroups with genus-zero pairwise quotients. Neither fact is claimed as new. The contribution assessed here is the particular full family of diagonal-quotient norm/pullback maps, their **two-sided exact multiplication identity**, **degree and polarization of that specific integral correspondence**, and the arithmetic distinction of its two square-class factor representatives. Van der Geer–van der Vlugt (1991) is a plausible historical source on \(p\)-torsion and isogeny decompositions whose complete text could not be inspected; any possible precedence concerning the precise polarized correspondence remains a priority risk.

## Limitations
No classification of the kernel as a product of constant, multiplicative, or local-local group schemes is claimed. The presented isogeny need not be separable. The displayed two quotient Jacobians may possess common simple constituents; the statement only rules out their being isogenous as whole abelian varieties over \(\mathbb F_p\). Publication priority has not been independently certified. The full 1991 article named below was not accessible for a decisive whole-document comparison; the result is therefore best treated as a provisional original refinement subject to expert historical verification.

## References
1. N. Arakelian and G. Korchmáros, *A characterization of the Artin-Mumford curve*, arXiv:1501.02616 (initial public version 12 January 2015). https://arxiv.org/abs/1501.02616
2. E. Kani and M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. **284** (1989), 307–327. General isogeny framework.
3. G. van der Geer and M. van der Vlugt, *Kloosterman sums and the p-torsion of certain Jacobians*, Math. Ann. **290** (1991), 549–563, DOI:10.1007/BF01459260. Full text not inspected; historical-priority risk.
4. S. Reyes-Carocca and R. E. Rodríguez, *A generalisation of Kani-Rosen decomposition theorem for Jacobian varieties*, arXiv:1702.00484. https://arxiv.org/abs/1702.00484
