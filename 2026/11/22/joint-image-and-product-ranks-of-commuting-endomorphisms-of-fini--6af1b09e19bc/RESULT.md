# Joint image and product ranks of commuting endomorphisms of finite dihedral quandles

## Finding
For a prime \(p\), positive integers \(e,t\), and the dihedral quandle \(R_{p^e}=(\mathbb Z/p^e\mathbb Z,\ x*y=2y-x)\), consider ordered \(t\)-tuples \((f_1,\ldots,f_t)\) of **all** quandle endomorphisms that commute pairwise under composition. Let \(r_i=|f_i(R_{p^e})|\), and let \(r_*=|(f_t\circ\cdots\circ f_1)(R_{p^e})|\). The following finite multivariate polynomial counts every joint rank profile exactly:

\[
\boxed{\mathcal J_{p,e,t}(z_1,\ldots,z_t;w)=p^e\sum_{\nu_1,\ldots,\nu_t=0}^{e}\left(\prod_{i=1}^t c_{\nu_i}\,z_i^{p^{e-\nu_i}}\right)w^{p^{e-\min(e,\sum_i\nu_i)}}+\Delta_{p,e,t}\,w^{p^e}\prod_{i=1}^t z_i^{p^e}.}
\]
Here \(c_\nu=(p-1)p^{e-\nu-1}\) for \(0\le\nu<e\), \(c_e=1\), and
\[
\Delta_{p,e,t}=S_e(p)p^{et}-(S_e(p)-1)p^{(e-1)t}-p^{e(t+1)},\qquad S_e(p)=1+p+\cdots+p^e.
\]
In particular, the exact count for **every joint image-rank profile with at least one nonbijective coordinate** is
\[
\boxed{p^e\prod_{i=1}^t c_{\nu_i},\qquad \nu_i=e-\log_p r_i,\quad \max_i\nu_i>0,}
\]
and its composite-image rank is forced to be \(p^{e-\min(e,\sum_i\nu_i)}\). Thus singular-coordinate rank statistics decouple multiplicatively across every tuple length, while all extra commutation weight lies entirely in the all-automorphism stratum. The all-bijective rank profile has exact multiplicity \(p^e c_0^t+\Delta_{p,e,t}\). In the example \(p=3,e=2,t=3\), there are \(9,153\) commuting ordered triples, of which \(4,536\) have all three maps bijective, and exactly \(324\) have individual image ranks \((1,9,9)\) and composite image rank \(1\).

The all-arity **unweighted** identity \(\mathcal J_{p,e,t}(1,\ldots,1;1)=S_e(p)p^{et}-(S_e(p)-1)p^{(e-1)t}\) is prior work in its equivalent determinantal-matrix form; it is reproduced here only as the necessary normalization of the new joint-rank polynomial, not claimed as a discovery.

## Assumptions and scope
The domain is the finite cyclic dihedral quandle of order \(p^e\), including \(p=2\). The maps are **all** quandle endomorphisms (not necessarily invertible), and pairwise commuting allows repeated maps. Rank means cardinality of a map's image as a set, not matrix rank. Product order is as displayed; all tuple members commute, so its order does not change the product. \(p\) is any prime; \(e,t\ge1\) are arbitrary integers. The variables are formal commuting variables with ordinary integer coefficients.

The prime-power calculation also determines the complete analogous polynomial for any \(n\ge1\): the Chinese remainder theorem decomposes \(\operatorname{End}(R_n)\) into the direct product of the prime-power monoids, and the image sizes of each coordinate map and their composite multiply across prime powers. Thus, in multiplying local monomial terms, **multiply** their rank exponents rather than add them. The special case \(n=1\) has one endomorphism and one ordered tuple of any length.

## Proof
**1. Every quandle endomorphism is affine.** Write residues modulo \(m=p^e\). A quandle endomorphism \(f\) satisfies \(f(2y-x)=2f(y)-f(x)\) for all \(x,y\). Put \(g(k)=f(k)-f(0)\). Substituting \(x=k-1,y=k\) yields \(g(k+1)=2g(k)-g(k-1)\) for all integers \(k\). With \(g(0)=0\), induction gives \(g(k)=k g(1)\), including the consistency at \(k=m\) in \(\mathbb Z/m\mathbb Z\). Conversely each \(f_{a,b}(x)=ax+b\), \(a,b\in\mathbb Z/m\mathbb Z\), preserves \(2y-x\). Evaluations at \(0,1\) make the affine parameters unique. Thus the endomorphism monoid has precisely \(m^2\) elements. The same argument works for every cyclic order.

**2. The pairwise commutation congruences.** Composition gives \(f_{a,b}\circ f_{c,d}=f_{ac,ad+b}\), so \(f_{a_i,b_i}\) and \(f_{a_j,b_j}\) commute precisely when \((a_i-1)b_j=(a_j-1)b_i\pmod{p^e}\). Write \(u_i=a_i-1\). This is the vanishing of all two-by-two minors of the matrix whose columns are \((u_i,b_i)\). It is necessary and sufficient for the entire tuple.

**3. Fixed multiplier fiber.** Fix \(u_1,\ldots,u_t\) and put \(h=\min_i v_p(u_i)\), with \(v_p(0)=e\) and all valuations truncated at \(e\). When \(h=e\), each translation tuple \((b_i)\) is allowed, giving \(p^{et}\) possibilities. Otherwise divide the \(u_i\) by \(p^h\), interpreted in \(\mathbb Z/p^{e-h}\mathbb Z\); the resulting vector \(v=(v_i)\) contains a unit. Reducing the minor equations modulo \(p^{e-h}\), they say \(v_ib_j=v_jb_i\). Taking a unit index \(j\) forces the reduced translation vector to be the unique scalar multiple \(b_i=\lambda v_i\), with \(p^{e-h}\) choices of \(\lambda\). Each reduced coordinate lifts to exactly \(p^h\) residues modulo \(p^e\). Therefore the fixed-multiplier translation fiber has exactly
\[
\boxed{p^{e+(t-1)h}}
\]
points, also valid for \(h=e\). This is a direct bijective count; it does not assume a field or invertible multipliers.

**4. Rank-profile separation.** For a multiplier \(a\) of exact valuation \(\nu\), the image of \(x\mapsto ax+b\) has size \(p^{e-\nu}\), regardless of \(b\). Exactly \(c_\nu=(p-1)p^{e-\nu-1}\) elements have \(\nu<e\), and \(c_e=1\) has \(\nu=e\). If some \(a_i\) is nonunit, then \(u_i=a_i-1\) is a unit and hence \(h=0\). Part 3 gives exactly \(p^e\) translation tuples *for each fixed multiplier tuple*. Thus every profile with at least one nonunit receives the first displayed formula without correction.

**5. The all-unit correction.** The only missing case has all \(a_i\) units, so each individual image rank is \(p^e\). First count the unweighted commuting tuples by grouping the \(u\)-tuples according to \(h\): for \(0\le h<e\), exactly \(p^{(e-h)t}-p^{(e-h-1)t}\) have minimum valuation \(h\), and precisely one has \(h=e\). Using Part 3 yields
\[
\begin{aligned}
T_{p,e,t}&=p^{et}+\sum_{h=0}^{e-1}\bigl(p^{(e-h)t}-p^{(e-h-1)t}\bigr)p^{e+(t-1)h}\\
&=S_e(p)p^{et}-(S_e(p)-1)p^{(e-1)t}.
\end{aligned}
\]
The baseline \(p^e\sum_{\nu_1,\ldots,\nu_t}\prod_i c_{\nu_i}\) totals \(p^{e(t+1)}\), because \(\sum_{\nu=0}^e c_\nu=p^e\). All nonunit-multiplier profiles have already been counted correctly. Therefore **all** of the difference \(\Delta=T_{p,e,t}-p^{e(t+1)}\) belongs to the all-unit profile. It is nonnegative because all fixed-multiplier fibers are at least \(p^e\). This proves the multivariate image-rank formula.

**6. Composition rank.** Multiplication of affine maps multiplies their coefficients \(a_i\), independently of the translation coordinates. If their valuations are \(\nu_1,\ldots,\nu_t\), the product coefficient has valuation \(\min(e,\sum_i\nu_i)\), giving image size \(p^{e-\min(e,\sum_i\nu_i)}\). The correction profile has all \(\nu_i=0\), hence full image. This establishes the exponent of \(w\) in every term and finishes the proof. The Chinese remainder extension follows because the ring and maps decompose coordinatewise and images have multiplicative cardinality.

## Verification
The standalone standard-library script `rankcheck.py` independently enumerates all pairs \((a,b)\) modulo \(p^e\), checks commutation directly by the affine composition congruences, evaluates each map on the whole cyclic set to obtain its actual image cardinality, and composes every tuple to compute its product rank. It compares the full sparse coefficient dictionary with the theorem for seven configurations: \((p,e,t)=(2,1,3),(3,1,3),(5,1,2),(2,2,3),(3,2,2),(2,3,2),(3,2,3)\). It prints `ALL_RANK_CHECKS_PASSED`. An additional standalone checker `verify.py` compares independent unweighted brute-force tuple counts and clique coefficients, including prime-power and non-prime-power moduli, and verifies the affine quandle-endomorphism classification by exhaustive function testing through five elements; it prints `ALL_CHECKS_PASSED`. These finite checks corroborate, but do not replace, the proof for arbitrary \(p,e,t\).

## Relationship to prior work
Elhamdadi, MacQuarrie and Restrepo's archival paper establishes the dihedral-quandle **automorphism group** as the affine group. Their argument supplies the affine coordinate model, but the present theorem counts singular endomorphisms and their simultaneous image and product ranks. Shahzamanian and Steinberg analyze the representation-theoretic quiver of the affine **monoid**, not this rank-refined commuting-tuple invariant.

The published *Two-pole commuting-tuple and clique enumerators for triangular algebras over finite chain rings* proves the **unweighted** two-by-many determinantal count \(T_{p,e,t}\) in its proof as an intermediate object. That identity is expressly **prior coverage**, including the maximum clique counts it implies: neither is claimed new. The rank-marked variables in \(\mathcal J_{p,e,t}\) count the *shifted coefficient* \(a_i=1+u_i\), individually and after multiplication. That information is lost by the unweighted determinant-cone count and by the triangular-algebra clique polynomial. A second published result, *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, classifies **single-element centralizer sizes** and commuting pair totals, not all-length joint image/composite-image strata. Its ideal-size correspondence alone does not assert or yield the displayed full joint-rank coefficients without the separate fixed-multiplier analysis. Cheraghpour and collaborators' complete preprint studies the commuting graph of the entire upper triangular ring, including field cliques, edge counts and diameter; its analyzed statements do not furnish the joint quandle-endomorphism rank census.

The new statement is precisely the multiplicative rank-profile decomposition and its singular-versus-unit boundary. A prior general **rank-weighted** determinantal-congruence theorem could subsume it; publication priority is not independently established.

## Limitations
The polynomial is for *cyclic dihedral quandles*, whose endomorphisms have scalar affine coefficients. It does not assert an analogous formula for multidimensional or general Alexander quandles, where the coefficient ring becomes a matrix centralizer. The all-arity unweighted count and clique polynomial are previously published and are not new contributions. Product-rank information is determined by the individual valuations; this theorem counts every joint stratum, not an additional independent variable of geometric freedom. Direct computations are finite; the proof handles arbitrary positive \(e,t\). Historical-priority risk remains for unlocated rank-weighted determinant formulas. No independent mathematical audit was conducted.

## References
1. M. Elhamdadi, J. MacQuarrie and R. Restrepo, *Automorphism groups of Quandles*, arXiv:1012.5291v1, first public 2010-12-23. https://arxiv.org/abs/1012.5291
2. M. H. Shahzamanian and B. Steinberg, *The quiver of an affine monoid*, arXiv:2009.12340, first public 2020-09-25. https://arxiv.org/html/2009.12340v2
3. H. Cheraghpour, M. N. Ghosseiri, M. Jafari and F. Seyfpour, *On Commuting graphs of triangular rings*, arXiv:2402.12619v1, first public 2024-02-20. https://arxiv.org/html/2402.12619v1
4. *Two-pole commuting-tuple and clique enumerators for triangular algebras over finite chain rings*, full published result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-two-pole-commuting-tuple-and-clique-enumerators-for-triangular-a--8fae3394a05c/RESULT.md
5. *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, full published result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d/RESULT.md
