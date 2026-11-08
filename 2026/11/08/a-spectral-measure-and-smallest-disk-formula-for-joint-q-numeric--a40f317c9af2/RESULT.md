# A spectral measure and smallest-disk formula for joint \(q\)-numerical ranges of commuting normal fields

## Finding

A norm-continuous pairwise commuting normal operator field has an exact compact, convex, spectral description of its **closed joint \(q\)-numerical range**, even for an arbitrary compact Hausdorff parameter space. Unlike the general noncommuting case, the geometry is a complex-measure slice with one prescribed total mass and a total-variation budget. In finite Hilbert dimension the range itself, rather than only its closure, is described by an elementary coefficient body. Every real supporting functional has a two-real-variable smallest-enclosing-disk formula.

Let \(K\) be the compact set of common spectral profiles defined below. For every \(|q|\le1\),

\[
\overline{\mathcal W_q(F)}^{\|\cdot\|_\infty}
=\left\{\int_K f\,d\nu(f):
\nu\in M(K),\ \|\nu\|_{\mathrm{TV}}\le1,\ \nu(K)=q\right\}.
\]

If \(H=\mathbb C^n\) and \(n\ge2\), the commuting normal operators are simultaneously unitarily diagonalizable, with spectral profiles \(f_1,\ldots,f_n\). In this case

\[
\mathcal W_q(F)=\left\{\sum_{j=1}^n a_j f_j:
\sum_{j=1}^n a_j=q,\quad\sum_{j=1}^n|a_j|\le1\right\}.
\]

Moreover, for any bounded complex-linear functional \(\lambda\) on \(C(\Omega)\) and \(|q|<1\), the support value in the real direction \(g\mapsto\operatorname{Re}\lambda(g)\) is

\[
\max_{g\in\overline{\mathcal W_q(F)}}\operatorname{Re}\lambda(g)
=\min_{z\in\mathbb C}
\left(\operatorname{Re}(qz)+\max_{f\in K}|\lambda(f)-z|\right).
\]

The minimum exists when \(|q|<1\). At \(q=0\) it is exactly the minimum enclosing-circle radius of \(\lambda(K)\subset\mathbb C\).

## Assumptions and scope

Let \(\Omega\ne\varnothing\) be compact Hausdorff and \(H\) a complex Hilbert space of dimension at least two; the inner product is **linear in its first argument**. Fix a norm-continuous \(F:\Omega\to B(H)\) such that all \(F(s)\) are normal and commute pairwise. The unital abelian \(C^*\)-algebra \(A=C^*(I,F(s):s\in\Omega)\) has compact character space \(X\). Via Gelfand duality each \(F(s)\) corresponds to the function \(\widehat{F(s)}\in C(X)\). For \(\chi\in X\), define the **common spectral profile** \(f_\chi(s)=\chi(F(s))\). The map \(X\to C(\Omega)\), \(\chi\mapsto f_\chi\), is norm-continuous: norm continuity of \(F\) gives uniform finite nets in \(\Omega\). Consequently \(K=\{f_\chi:\chi\in X\}\) is compact in the supremum norm.

For complex \(q\) with \(|q|\le1\), define

\[
\mathcal W_q(F)=\{g_{x,y}:\|x\|=\|y\|=1,\ \langle x,y\rangle=q,\quad
 g_{x,y}(s)=\langle F(s)x,y\rangle\}.
\]

The measure integral in the finding is a Bochner integral in \(C(\Omega)\) (equivalently, the pointwise integral), since \(K\) is compact metric in its norm topology. A finite complex regular Borel measure has total variation \(\|\nu\|_{\mathrm{TV}}\). All uniform closures are in the supremum norm.

## Proof

**1. A coefficient-lifting lemma.** Suppose \(m\ge2\) and \(a_1,\ldots,a_m\in\mathbb C\) satisfy \(\sum_j|a_j|\le1\). Then there exist unit vectors \(u,v\in\mathbb C^m\) with \(u_j\overline{v_j}=a_j\) for all \(j\). If at least two coefficients are nonzero, write \(b_j=|a_j|\) on the positive coordinates and \(B=\sum b_j\). For positive \(r_j\) summing to one, Cauchy–Schwarz gives \(\sum b_j^2/r_j\ge B^2\), with equality at \(r_j=b_j/B\); approaching the simplex boundary makes the expression tend to infinity. Because \(B\le1\), continuity yields positive \(r_j\) with \(\sum b_j^2/r_j=1\). Set \(u_j=\sqrt{r_j}\) and \(v_j=\overline{a_j}/\sqrt{r_j}\) on those coordinates, and zero elsewhere. Then both norms are one and each product is \(a_j\). If exactly one coefficient \(a_i\) is nonzero, choose a different index \(k\), put \(u=e_i\) and \(v=\overline{a_i}e_i+\sqrt{1-|a_i|^2}e_k\). If all coefficients vanish, take \(u=e_1\), \(v=e_2\). This proves the lemma, including every boundary case.

**2. Inclusion in the measure slice.** The rule \(a\mapsto\langle ax,y\rangle\), for unit vectors \(x,y\) of inner product \(q\), defines a complex-linear functional on \(A\) of norm at most one and takes the value \(q\) on \(I\). The Gelfand transform and the Riesz representation theorem yield a complex measure \(\widetilde\nu\in M(X)\) with \(\|\widetilde\nu\|_{\mathrm{TV}}\le1\) and \(\widetilde\nu(X)=q\). Push it forward under \(\chi\mapsto f_\chi\) to obtain \(\nu\in M(K)\). Then for every \(s\in\Omega\),

\[
\langle F(s)x,y\rangle
=\int_X\chi(F(s))\,d\widetilde\nu(\chi)
=\int_K f(s)\,d\nu(f).
\]

**3. Reverse inclusion in uniform closure.** Start with an arbitrary feasible \(\nu\in M(K)\). For each \(\varepsilon>0\), partition the compact metric space \(K\) into finitely many disjoint Borel pieces of diameter below \(\varepsilon\). Choose one \(f_j\) in each nonempty piece and \(a_j=\nu(E_j)\). Then \(\sum_j a_j=q\), \(\sum_j|a_j|\le1\), and

\[
\left\|\int_K f\,d\nu(f)-\sum_j a_j f_j\right\|_\infty
\le\varepsilon\|\nu\|_{\mathrm{TV}}\le\varepsilon.
\]

If \(K\) contains at least two profiles, ensure that the finite list has at least two **distinct** profiles, adding a profile with coefficient zero if needed. Pick their characters \(\chi_j\in X\). Since the profiles are distinct, the characters are distinct. Uniform continuity of \(\chi\mapsto f_\chi\) gives pairwise disjoint open neighborhoods \(U_j\) in \(X\) on which \(\sup_{s\in\Omega}|\chi(F(s))-f_j(s)|<\varepsilon\). Choose nonzero continuous scalar functions supported in these neighborhoods. Faithful functional calculus provides mutually orthogonal, nonzero invariant spectral subspaces \(H_j\subset H\), on each of which

\[
\|(F(s)-f_j(s)I)|_{H_j}\|\le\varepsilon
\qquad(s\in\Omega).
\]

Take a unit vector \(e_j\in H_j\). By step 1, choose unit \(u=(u_j)\), \(v=(v_j)\in\mathbb C^m\) such that \(u_j\overline{v_j}=a_j\). Put \(x=\sum_j u_je_j\) and \(y=\sum_j v_je_j\). Then \(\|x\|=\|y\|=1\), \(\langle x,y\rangle=q\), and all off-diagonal terms \(\langle F(s)e_i,e_j\rangle\) vanish for \(i\ne j\). Therefore

\[
\sup_s\left|\langle F(s)x,y\rangle-\sum_j a_jf_j(s)\right|
\le\varepsilon\sum_j|a_j|\le\varepsilon.
\]

If \(K\) has only one profile \(f\), the representation is scalar, \(F(s)=f(s)I\). Because \(\dim H\ge2\), any admissible \(q\) has unit vectors of inner product \(q\), giving exactly \(qf\). This handles the degenerate case. Combining estimates proves the reverse inclusion.

**4. Compactness, convexity and exact finite-dimensional result.** The measure ball \(\{\nu:\|\nu\|_{\mathrm{TV}}\le1,\nu(K)=q\}\) is weak-star compact and convex in \(M(K)=C(K)^*\). Its image under \(\nu\mapsto\int_K f\,d\nu\) is norm compact: finite small-diameter partitions of \(K\) approximate this image uniformly by bounded subsets of finite-dimensional spans, so it is totally bounded; weak-star compactness supplies norm closure via pointwise limits. Thus the proven closure is compact and convex. If \(H\) is finite-dimensional, simultaneous diagonalization makes \(\langle F(s)x,y\rangle=\sum_j x_j\overline{y_j}f_j(s)\). Cauchy–Schwarz gives the coefficient constraints, and step 1 realizes every feasible coefficient vector exactly. No closure is needed.

**5. Exact real-support duality.** Let \(\lambda\in C(\Omega)^*\) be complex-linear and put \(c(f)=\lambda(f)\). The support is the maximum of \(\operatorname{Re}\int_K c(f)\,d\nu(f)\) over all feasible measures. For every \(z\in\mathbb C\), the prescribed mass gives

\[
\operatorname{Re}\int_K c(f)\,d\nu(f)
\le\operatorname{Re}(qz)+\max_{f\in K}|c(f)-z|.
\]

For the reverse bound, consider the weak-star compact unit ball of measures and the affine Lagrangian \(\operatorname{Re}\int c\,d\nu+\operatorname{Re}(z(q-\nu(K)))\). The compact-convex minimax theorem applies to its measure variable and the real two-dimensional variable \(z\); minimizing over \(z\) enforces exactly \(\nu(K)=q\). Maximizing over the unrestricted total-variation ball instead yields \(\max_{f\in K}|c(f)-z|\). Thus the displayed upper bound is sharp after the infimum over \(z\). If \(|q|<1\), the objective is at least \((1-|q|)|z|-\|c\|_\infty\), so its infimum is attained. At \(q=0\), the minimum \(\min_z\max_{f\in K}|\lambda(f)-z|\) is exactly the smallest enclosing-circle radius of the complex spectral image.

## Verification

The result has a complete analytical proof, including the coefficient-lifting lemma, the spectral localization step, the compactness argument and the support-function minimax. The supplementary standard-library checker `CHECK.py` independently exercises coefficient lifting for random complex vectors and prescribed complex overlaps, verifies the constrained normalization numerically, and verifies the basic primal-versus-dual support inequality on sampled finite spectral lists. These finite diagnostics are **not** substitutes for the uniform infinite-dimensional proof, and they do not certify originality or independent correctness.

A concrete closure-only boundary is given by a non-atomic multiplication operator: on \(L^2(0,1)\), take \(\Omega\) to be one point and \(F\) multiplication by the independent variable. Its operator norm is one but is not attained, so the boundary point \(1\) is absent from the ordinary numerical range at \(q=1\), while it belongs to the spectral-measure envelope. Thus removing the closure in arbitrary infinite dimension would be false.

## Relationship to prior work

Azadi, arXiv:2610.32504v1 (23 October 2026), develops the same joint \(q\)-range for continuous fields, proves total boundedness and finite-dimensional compactness, and proves a **realization theorem for \(|q|=1\)**. Its Theorem 2.16 treats a freely constructed diagonal field whose admissible coefficients become a positive convex combination at the unit-overlap endpoint. It does not give the measure slice, exact simultaneous-normal finite-dimensional formula, arbitrary-dimensional normal-family convexity, or interior-overlap smallest-circle duality proved here. Those interior-overlap conclusions are the contribution; the unit-overlap convex-hull specialization is classical context.

Feki–Patra–Rani–Taki, arXiv:2410.03669, Theorem 6 and Corollary 8, establish a convexity criterion for joint \(q\)-numerical ranges in **Hilbert dimension two** under a commutativity condition. Their results do not classify arbitrary-dimensional commuting normal fields or their spectral-profile measure bodies. Chien–Nakazato (2005), DOI 10.1080/03081080500156888, investigate \(q\)-ranges of a **single** normal operator and circumscribed-circle formulas; the available abstract does not establish the present joint-profile result. The full article was not available for a decisive exhaustive comparison. Chan–Li–Poon, arXiv:2108.05414, study joint **\(k\)-numerical** ranges (sums over orthonormal \(k\)-frames), a distinct invariant. The general nonconvexity of joint numerical ranges of commuting operator families in Müller–Tomilov, arXiv:2010.09129, underlines the importance of the normality assumption.

No assertion of publication-priority certification is made. A more general older convexity or complex-measure theorem might imply some or all of the result under different language and remains a residual risk.

## Limitations

The operators must be normal and commute pairwise; the proof does not extend to arbitrary commuting nonnormal families. Infinite-dimensional equality is for the **norm closure**, not necessarily the range itself. The smallest-circle dual computes supporting functionals of the resulting convex compact set, not a pointwise membership algorithm without further optimization. The supplemental checker samples finite-dimensional identities, not all operator fields. Independent mathematical validation and a comprehensive publication-priority audit have not been performed.

## References

1. Amin Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1, first public 23 October 2026, https://arxiv.org/html/2610.32504v1.
2. Kais Feki, Arnab Patra, Jyoti Rani and Zakaria Taki, *Joint q-Numerical Ranges of Operators in Hilbert and Semi-Hilbert Spaces*, arXiv:2410.03669, https://arxiv.org/abs/2410.03669.
3. Mao-Ting Chien and Hiroshi Nakazato, *The q-numerical ranges of normal operators*, Linear and Multilinear Algebra 53 (2005), 393–416, DOI 10.1080/03081080500156888.
4. Jor-Ting Chan, Chi-Kwong Li and Yiu-Tung Poon, *Commuting normal operators and joint numerical range*, arXiv:2108.05414.
5. Vladimir Müller and Yuri Tomilov, *In search of convexity: diagonals and numerical ranges*, arXiv:2010.09129.
