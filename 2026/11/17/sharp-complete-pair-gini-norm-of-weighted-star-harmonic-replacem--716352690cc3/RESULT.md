# Sharp complete-pair Gini norm of weighted star harmonic replacement

## Finding
Let a finite star have one hub and \(m\ge1\) leaves, with strictly positive conductances \(c_1,\ldots,c_m\). Put \(p_i=c_i/\sum_{j=1}^m c_j\). The Dirichlet harmonic-replacement operator \(H_p:\mathbb R^{m+1}\to\mathbb R^{m+1}\) preserves each leaf value and replaces the hub value by \(\sum_i p_i x_i\). Equip signals on all \(m+1\) vertices, modulo constants, with complete-pair Gini variation
\[
G(x)=\sum_{0\le u<v\le m}|x_u-x_v|.
\]
Then the exact, attained operator seminorm is
\[
\boxed{\|H_p\|_{G\to G}=1+\frac{m-2}{m}\max_{1\le i\le m}p_i.}
\]
The formula includes the exceptional cases \(m=1\) (norm zero) and \(m=2\) (norm one). For every \(m\ge3\), an indicator of any largest-conductance leaf, with zero hub and other leaves, is an extremizer, and \(H_p\) strictly amplifies some complete-pair variation.

For fixed \(m\ge3\), the uniform conductance vector is the **unique** minimizer of the norm and
\[
\min_{p_i>0,\ \sum_i p_i=1}\|H_p\|_{G\to G}
=1+\frac{m-2}{m^2},\qquad
\sup_{p_i>0,\ \sum_i p_i=1}\|H_p\|_{G\to G}
=2-\frac2m.
\]
The displayed supremum is not attained with strictly positive conductances. Among all positive-conductance stars with uniform normalized conductances, the largest norm is exactly \(9/8\), attained only at four leaves. In contrast, over all conductance vectors and all finite leaf counts, the supremum is \(2\), never attained.

## Assumptions and scope
The star has vertices \(\{o,v_1,\ldots,v_m\}\), edges \(\{o,v_i\}\), and positive edge conductances. The star's Dirichlet energy for prescribed leaf values is \(\sum_{i=1}^m c_i(z-x_i)^2\) as a function of the interior hub value \(z\). Its unique minimizer is \(z=\sum_i p_ix_i\). Thus the operator is an idempotent, positive, constant-preserving linear map on **full vertex signals**: the initial hub value is allowed to be arbitrary, and both input and output variations include the hub. This is not the boundary-only Lipschitz extension norm. The Gini quantity is the unweighted sum of absolute differences across *all* unordered pairs, not variation restricted to graph edges. All inputs are real. There are no hidden scale assumptions on conductances.

## Proof
**1. Binary-cut reduction.** Since \(H_p\mathbf1=\mathbf1\), subtracting a common constant does not change the quotient. For any nonconstant real \(x\), write \(x=\min_u x_u\,\mathbf1+\int_{\min x}^{\max x}\mathbf1_{\{x>t\}}\,dt\). The triangle inequality gives \(G(H_px)\le\int G(H_p\mathbf1_{\{x>t\}})dt\), whereas the exact layer-cake identity gives \(G(x)=\int G(\mathbf1_{\{x>t\}})dt\). Consequently the operator norm is the maximum of \(G(H_p\mathbf1_S)/G(\mathbf1_S)\) over nonempty proper subsets \(S\) of the vertex set. Every such cut is an actual input, so this reduction is exact.

**2. Compute a cut.** Suppose \(k\) of the \(m\) leaves lie in \(S\), and the hub indicator is \(b\in\{0,1\}\). Put \(q=\sum_{i:v_i\in S}p_i\). The leaf-to-leaf contribution to either variation is \(k(m-k)\). The output hub value is \(q\), so its contribution to the output variation is
\[
 k(1-q)+(m-k)q=k+(m-2k)q.
\]
The input hub contribution is \(k\) if \(b=0\) and \(m-k\) if \(b=1\). Thus the cut quotient is exactly
\[
\frac{k(m-k)+k+(m-2k)q}{k(m-k)+\bigl(b(m-k)+(1-b)k\bigr)}.
\]
If \(k=0\) or \(k=m\), the output is constant and the quotient is zero whenever the input cut is nonconstant. Complementing \(S\) does not change the quotient, so it suffices to treat \(1\le k\le\lfloor m/2\rfloor\). In this range the denominator is at least \(k(m-k+1)\), while \(m-2k\ge0\). Write \(p_*=\max_i p_i\). Since \(q\le kp_*\),
\[
\frac{G(H_p\mathbf1_S)}{G(\mathbf1_S)}
\le1+\frac{(m-2k)q}{k(m-k+1)}
\le1+\frac{(m-2k)p_*}{m-k+1}.
\]
For all \(k\ge1\) in this range,
\[
\frac{m-2k}{m-k+1}\le\frac{m-2}{m},
\]
because the cross-multiplied difference is exactly \((k-1)(m+2)\ge0\). This proves the stated upper bound.

**3. Attainment and boundary cases.** For \(m\ge2\) choose a leaf \(v_j\) with \(p_j=p_*\), set \(x(v_j)=1\), and give all other vertices value zero. The input variation is \(m\). The output hub value is \(p_*\); its variation against the leaves is \(1+(m-2)p_*\), while the leaf-to-leaf variation is \(m-1\). Hence \(G(H_px)/G(x)=1+(m-2)p_*/m\). For \(m=1\) the output is constant, so the same formula gives zero. For \(m=2\), the upper bound and explicit cut both equal one. The formula holds for every positive conductance vector and all real inputs.

**4. Conductance design.** For \(m\ge3\), the norm is strictly increasing in \(p_*\). Every strictly positive probability vector has \(p_*\ge1/m\), with equality only for uniform weights. This gives the uniquely attained minimum. Positivity also forces \(p_*<1\), but vectors with one mass tending to one exist, yielding the unattained fixed-size supremum \(2-2/m\). In the uniform case the norm is \(1+(m-2)/m^2\). The exact identity
\[
\frac{m-2}{m^2}\le\frac18
\quad\Longleftrightarrow\quad
(m-4)^2\ge0
\]
shows that the universal uniform-conductance maximum is \(9/8\), uniquely at four leaves. Taking \(m\to\infty\) in the fixed-size envelope yields the unattained global supremum two.

## Verification
The companion `check_star_harmonic_gini.py` uses exact rational arithmetic. It exhaustively evaluates all nonconstant binary cuts for four probability profiles at each leaf count from one through nine and compares their maximum with the theorem's formula; it also checks \(3600\) rational real inputs, the singleton witnesses, the fixed-size envelope, and the uniform-design inequality. Run `python check_star_harmonic_gini.py` with Python 3 and no third-party dependencies. These tests corroborate the analytic argument; no finite enumeration is used as the proof for unrestricted \(m\) or real conductances.

## Relationship to prior work
Bendito, Carmona, and Encinas [1] develop Dirichlet principles and boundary-value problems on weighted networks. Their paper provides the natural variational setting in which the hub becomes the conductance-weighted mean, but their relevant sections do not give the complete-pair Gini operator norm. Sheffield and Smart [2] study optimal Lipschitz extensions on finite graphs; the published abstract uses a different quantity and the full manuscript could not be checked in this comparison.

Gaubert and Qu [4] characterize the Dobrushin coefficient for Hopf oscillation of stochastic maps; oscillation contraction is not the same as complete-pair Gini contraction. The published *Sharp conductance design for Lipschitz-harmonic extension on metric stars* [3] treats the *metric Lipschitz seminorm* of an extension from leaf data, rather than the complete-pair Gini seminorm of a full-signal hub-replacement map. For equal arm lengths its fixed-conductance Lipschitz coefficient is \(2(1-\min_i p_i)\), whereas the coefficient here depends on \(\max_i p_i\). For example, with four leaves the vectors \((1,2,3,4)/10\) and \((1,2,2,5)/10\) give the same Lipschitz coefficient \(9/5\) but different Gini coefficients \(6/5\) and \(5/4\). Thus that stronger-looking metric-star norm result does not determine the claimed Gini formula or its optimizer.

## Limitations
The theorem addresses exactly one interior hub, finite stars, positive edge conductances, real values and unweighted complete-pair variation. It does not treat multiple interior vertices, unequal vertex-pair weights, continuous metric-edge values, graph-edge variation or complex data. A broader unpublished inequality might imply this short exact formula; bibliographic search cannot establish priority definitively. The corresponding full-input Gini question is different from the classical existence and maximum-principle theory of Dirichlet harmonic extension.

## References
[1] E. Bendito, A. Carmona and A. M. Encinas, *Boundary Value Problems on Weighted Networks*, Discrete Applied Mathematics 156 (2008), 3443–3463, DOI:10.1016/j.dam.2008.02.008; author-available full text: https://mapthe.upc.edu/en/publications/docs/publications_2008_boundary-value-problems-on-weighted-networks.pdf . The publication year is verified, but no day-resolved first-posting date was established.

[2] S. Sheffield and C. K. Smart, *Vector-valued optimal Lipschitz extensions*, arXiv:1006.1741v1, first submitted 2010-06-09, https://arxiv.org/abs/1006.1741 . The public submission date is used as the earliest precisely day-dated lead record; an older publication [1] has only year-level verified public evidence here.

[3] *Sharp conductance design for Lipschitz-harmonic extension on metric stars*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-conductance-design-for-lipschitz-harmonic-extension-on-met--5986e803b2b7 . The complete available mathematical statement and proof were compared, not merely its title.

[4] S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226v1, first posted 2013-02-21, https://arxiv.org/abs/1302.5226 .
