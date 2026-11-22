# Exact Fourier-algebra norm of two affine cosets and its parity-ordered quotient law

## Finding
Let \(G\) be an arbitrary finite abelian group and \(H,K\leq G\). Write \(J=H\cap K\), \(L=H+K\), and
\[
\alpha=\frac{|J|}{|K|}=\frac{|H|}{|L|},\qquad
\beta=\frac{|J|}{|H|}=\frac{|K|}{|L|}.
\]
For two affine cosets \(A=x+H\) and \(B=y+K\), define
\[
\|\mathbf1_{A\cup B}\|_{A(G)}
=\sum_{\chi\in\widehat G}
\left|\frac1{|G|}\sum_{g\in G}\mathbf1_{A\cup B}(g)\overline{\chi(g)}\right|.
\]
If \(A\cap B\ne\varnothing\), the norm is exactly
\[
1+2(1-\alpha)(1-\beta).
\]
If \(A\cap B=\varnothing\), put \(m=\operatorname{ord}_{G/L}(x-y+L)\geq2\). Then the norm is exactly
\[
2-\alpha-\beta+\mathcal M_m(\alpha,\beta),\qquad
\mathcal M_m(a,b)=\frac1m\sum_{j=0}^{m-1}\left|a+b e^{2\pi i j/m}\right|.
\]
For every \(a,b>0\), the values satisfy the **sharp universal order envelope**
\[
\mathcal M_2(a,b)=\max(a,b)\leq\mathcal M_m(a,b)
\leq\mathcal M_3(a,b)=\frac{a+b+2\sqrt{a^2-ab+b^2}}3.
\]
The left equality occurs only at \(m=2\), and the right equality only at \(m=3\). More precisely, the even sequence \(\mathcal M_2<\mathcal M_4<\cdots\) increases strictly and the odd sequence \(\mathcal M_3>\mathcal M_5>\cdots\) decreases strictly to the same continuous mean
\[
\mathcal M_\infty(a,b)=\frac1{2\pi}\int_0^{2\pi}|a+b e^{i\theta}|\,d\theta.
\]
The endpoints \(m=2,3\) are realizable by disjoint affine cosets for fixed \(H,K\) after adjoining an appropriate cyclic factor to their ambient group.

There is a sharp parity-dependent convergence law. Put \(b_*=\max(a,b)\) and \(r=\min(a,b)/b_*\). For each fixed \(0<r<1\),
\[
\mathcal M_m(a,b)-\mathcal M_\infty(a,b)
=(-1)^{m+1}\frac{b_*\sqrt{1-r^2}}{\sqrt\pi}\,
\frac{r^m}{m^{3/2}}\bigl(1+o(1)\bigr).
\]
For equal amplitudes \(a=b>0\), the behavior changes to the two algebraic laws
\[
\mathcal M_m(a,a)-\mathcal M_\infty(a,a)=
\begin{cases}
-\dfrac{a\pi}{3m^2}+O(a m^{-4}),&m\ \text{even},\\[2pt]
+\dfrac{a\pi}{6m^2}+O(a m^{-4}),&m\ \text{odd}.
\end{cases}
\]

## Assumptions and scope
The group \(G\) is finite abelian, and \(H,K\) are nonempty subgroups (the trivial subgroup and the entire group are allowed). The cosets may coincide, meet, or be disjoint. Fourier coefficients use Haar probability measure, and the Fourier-algebra norm is the unweighted \(\ell^1\)-sum of these normalized coefficients. In the disjoint case the quotient element \(x-y+L\) is nonzero, making its order \(m\ge2\). The strict polygon inequalities assume \(a,b>0\); no assertion of strictness is made when an amplitude vanishes. The asymptotic estimates hold with \(a,b\) fixed as \(m\to\infty\).

## Proof
**The intersection regime.** Since \(A\cap B\ne\varnothing\), translate the common point to zero. The indicator is \(\mathbf1_H+\mathbf1_K-\mathbf1_J\). If \(N=|G|\) and \(h=|H|\), \(k=|K|\), \(j=|J|\), each subgroup indicator has normalized Fourier coefficients \(|H|/N\) on its annihilator and zero elsewhere. As \(J^\perp\) contains both \(H^\perp\) and \(K^\perp\), the only strictly negative coefficients of the union indicator occur on \(J^\perp\setminus(H^\perp\cup K^\perp)\), each with value \(-j/N\). The signed sum of coefficients equals the value of the indicator at zero, namely one. As \(H^\perp\cap K^\perp=L^\perp\), the extra contribution to the absolute sum is
\[
2\frac jN\left(\frac Nj-\frac Nh-\frac Nk+\frac N{|L|}\right)
=2\left(1-\frac jh\right)\left(1-\frac jk\right).
\]
This proves the intersecting formula, including all nested-subgroup limits.

**The disjoint regime.** Here \(\mathbf1_{A\cup B}=\mathbf1_A+\mathbf1_B\). Outside \(L^\perp\), the annihilators \(H^\perp\) and \(K^\perp\) have disjoint contributions of absolute total mass \(2-\alpha-\beta\). On \(L^\perp\), the Fourier coefficient has modulus
\[
\frac{|L|}{N}\big|\alpha+\beta\chi(x-y)\big|.
\]
The restriction \(\chi\mapsto\chi(x-y)\) on \(L^\perp\cong\widehat{G/L}\) has image precisely the \(m\)-th roots of unity, each with multiplicity \(|L^\perp|/m\). Thus this contribution is exactly \(\mathcal M_m(\alpha,\beta)\).

**Strict polygon order law.** By homogeneity and symmetry set \(a=1\), \(b=r\), \(0<r\le1\). The periodic even function \(g_r(\theta)=|1+r e^{i\theta}|\) has absolutely summable complex Fourier coefficients \(c_n\). For every positive integer \(n\),
\[
c_n=(-1)^{n+1}b_n(r),\qquad
b_n(r)=\frac1\pi\int_0^r u^{n-3/2}\sqrt{(r-u)(1-ru)}\,du>0.
\]
To establish this identity for \(0<r<1\), write the Laurent coefficient as the unit-circle contour integral of \(z^{-n-1}\sqrt{(1+rz)(1+r/z)}\), using the branch positive at \(z=1\). Deform the contour outward across the branch cut \(( -\infty,-1/r]\); its jump is \(2i\sqrt{(rt-1)(1-r/t)}\) at \(z=-t\). The outer-circle integral tends to zero for \(n\ge1\). Substitution \(u=1/t\) gives the displayed formula, with sign \((-1)^{n+1}\). The case \(r=1\) follows by continuous limiting of the Fourier coefficients and the integral. The corresponding series is absolutely convergent, including at \(r=1\).

Let \(d\mu_r(u)=\pi^{-1}u^{-3/2}\sqrt{(r-u)(1-ru)}\,du\) on \((0,r)\). This positive measure has finite moments \(\int u^n d\mu_r=b_n\) for each \(n\ge1\). Sampling the absolutely convergent Fourier series at \(m\)-th roots of unity yields
\[
\mathcal M_m(1,r)-c_0=
\begin{cases}
-2\displaystyle\int_0^r\frac{u^m}{1-u^m}\,d\mu_r(u),&m\ \mathrm{even},\\
+2\displaystyle\int_0^r\frac{u^m}{1+u^m}\,d\mu_r(u),&m\ \mathrm{odd},
\end{cases}
\]
where \(c_0=\mathcal M_\infty(1,r)\). Both positive integrands strictly decrease with \(m\) for every \(0<u<r\le1\), proving the strict even increase and odd decrease. All values lie between their first terms \(m=2\) and \(m=3\). Direct root-of-unity evaluation yields \(\mathcal M_2(1,r)=1\) and \(\mathcal M_3(1,r)=(1+r+2\sqrt{1-r+r^2})/3\). The construction \(G=L\times\mathbb Z/m\mathbb Z\), with the cosets separated by a quotient generator, realizes each order without changing the subgroup ratios.

**Sharp convergence.** When \(0<r<1\), substitution \(u=r(1-t/n)\) near the right endpoint of the moment integral, followed by dominated Laplace asymptotics, gives
\[
b_n(r)=\frac{\sqrt{1-r^2}}{2\sqrt\pi}\frac{r^n}{n^{3/2}}(1+o(1)).
\]
The root-of-unity filter then has leading term \(2(-1)^{m+1}b_m(r)\); terms with indices at least \(2m\) are exponentially smaller. For \(r=1\), exact elementary evaluation of the moment integral gives
\[
b_n(1)=\frac4{\pi(4n^2-1)}.
\]
Summing \(2\sum_{k\ge1}(-1)^{km+1}b_{km}(1)\) and expanding \((4k^2m^2-1)^{-1}\) produces \(-2\zeta(2)/(\pi m^2)+O(m^{-4})=-\pi/(3m^2)+O(m^{-4})\) for even \(m\), and \(2\eta(2)/(\pi m^2)+O(m^{-4})=\pi/(6m^2)+O(m^{-4})\) for odd \(m\). This proves the stated rates.

## Verification
The accompanying `checks/checker.py` independently forms finite-group character transforms and compares their \(\ell^1\) sums against both exact coset formulas, spanning cyclic and product groups, nested and transverse subgroups, and intersecting and disjoint cosets. It also checks the finite polygon inequalities and the two equal-radius parity constants numerically. Run with Python 3: `python checks/checker.py`. The recorded run passed **5,594** direct-transform and polygon assertions. These finite numerical comparisons supplement but do not replace the general group-theoretic and analytic proof above.

## Relationship to prior work
Carenini's 2026 group-idempotent theorem gives structural signed coset decompositions controlled by harmonic-analysis norms, motivating the question of exact norms for minimal unions. Sanders's 2020 quantitative form of Cohen's theorem gives general decomposition estimates and the normalized subgroup-indicator norm one. Neither result, in the inspected passages, states the above complete two-coset formula, strict quotient-order envelope, or sharp equal-radius convergence transition. Known Fourier transform identities for individual coset indicators are used as ingredients and are not presented as novel. The precise polygon-order law may also be viewed as an exact two-phase root-of-unity sampling statement; equivalences in older polygonal potential literature cannot be excluded from indexed searches alone.

## Limitations
This is a result for **two** affine cosets in finite abelian groups; it does not classify norms of arbitrary unions of three or more cosets, infinite groups, or nonabelian representations. The asymptotic constants in the unequal-radius case are for fixed radius ratio below one and are not uniform as that ratio approaches one. A bibliographic search and comparisons of accessible source material do not establish absolute uniqueness; a nonindexed older polygon-average identity or coset-union norm formula remains possible.

## References
1. Gaia Carenini, *Blocky Matrices and Group Idempotents*, ECCC TR26-153, first publicly posted August 22, 2026. https://eccc.weizmann.ac.il/report/2026/153/ ; arXiv:2609.27951, https://arxiv.org/abs/2609.27951.
2. Tom Sanders, *Bounds in Cohen's Idempotent Theorem*, Journal of Fourier Analysis and Applications **26**, article 25 (2020). https://doi.org/10.1007/s00041-020-09732-y.
