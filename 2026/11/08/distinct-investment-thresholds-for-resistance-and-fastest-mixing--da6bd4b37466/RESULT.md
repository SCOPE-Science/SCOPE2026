# Distinct investment thresholds for resistance and fastest mixing in a two-community complete network

## Finding

For every integer \(m\ge2\), split the vertices of \(K_{2m}\) into two designated communities of \(m\) vertices each. Every intercommunity edge has unit conductance price; every intracommunity edge has price \(c>0\). All individual edge conductances are independently selectable and nonnegative, subject to the exact total cost \(B>0\). Define the unscaled Kirchhoff index \(\mathcal K=\sum_{u<v}R_{uv}=2m\operatorname{tr}(L^+)\) and the algebraic connectivity \(\lambda_2(L)\) of the resulting weighted Laplacian.

Let
\[
 c_R=\frac{4m}{4m-3},\qquad c_M=\frac m{m-1}.
\]

**Resistance optimum.** The globally unique minimizer of \(\mathcal K\) has a common intercommunity conductance \(a_R>0\) and a common intracommunity conductance \(b_R\ge0\). Writing \(r_R=b_R/a_R\), its exact formula is
\[
 r_R=\begin{cases}
 2\sqrt{\dfrac m c-(m-1)}-1,&0<c<c_R,\\[3pt]
 0,&c\ge c_R,
 \end{cases}\qquad
 a_R=\frac{B}{m\bigl(m+c(m-1)r_R\bigr)},\quad b_R=r_Ra_R.
\]
In particular, every intracommunity edge receives zero conductance if and only if \(c\ge c_R\). The minimum is
\[
 \mathcal K_{\min}=
 \begin{cases}
 \dfrac mB\left[m-c(m-1)+4c(m-1)^2+4(m-1)\sqrt{c\bigl(m-c(m-1)\bigr)}\right],&0<c<c_R,\\[4pt]
 \dfrac{m^2(4m-3)}B,&c\ge c_R.
 \end{cases}
\]

**Fastest-mixing optimum.** The maximum algebraic connectivity is
\[
 \lambda_2^{\max}=
 \begin{cases}
 \dfrac{2B}{m+c(m-1)},&0<c<c_M,\\[4pt]
 \dfrac Bm,&c\ge c_M.
 \end{cases}
\]
A globally optimal symmetric allocation exists, whose ratio \(r_M=b_M/a_M\) is uniquely \(1\) for \(c<c_M\), uniquely \(0\) for \(c>c_M\), and may be any \(r_M\in[0,1]\) when \(c=c_M\). In the first case **every** globally optimal allocation (even nonsymmetric) funds some intracommunity edge; in the second, **every** globally optimal allocation funds none. At equality both support patterns have optimal representatives. These statements do not assert uniqueness of arbitrary nonsymmetric fastest-mixing optimizers.

The two price thresholds satisfy the strict inequality
\[
 c_R<c_M,\qquad c_M-c_R=\frac{m}{(m-1)(4m-3)}.
\]
Thus for **every** \(c_R\le c<c_M\), the unique resistance-optimal network purchases no intracommunity edges, while every fastest-mixing network purchases some. A common globally optimal allocation for both objectives exists **exactly** when \(c=1\) or \(c\ge c_M\). In particular, for \(m=3\), \(B=1\), and \(c=7/5\), the resistance optimum is \((a_R,b_R)=(1/9,0)\), giving \((\mathcal K,\lambda_2)=(81,1/3)\); the symmetric fastest-mixing optimum is \((a_M,b_M)=(5/87,5/87)\), giving \((\mathcal K,\lambda_2)=(87,10/29)\).

**Critical window.** If \(\kappa\in\mathbb R\) is fixed and \(c=1+\kappa/m>0\) for sufficiently large \(m\), then
\[
 r_R\longrightarrow \left(2\sqrt{(1-\kappa)_+}-1\right)_+,
 \qquad
 r_M\longrightarrow\begin{cases}1,&\kappa\le1,\\0,&\kappa>1,\end{cases}
\]
where \(t_+=\max\{t,0\}\), and \(r_M\) refers to the symmetric maximizer with the above convention. Hence the resistance support transition has critical coordinate \(\kappa=3/4\), while the fastest-mixing transition has critical coordinate \(\kappa=1\).

## Assumptions and scope

All graphs are finite, simple, undirected, and have exactly \(2m\) vertices. The two labeled parts have equal size \(m\ge2\). Edge prices and the budget are strictly positive. Weight zero is permitted. A disconnected weight assignment has infinite Kirchhoff index; the fastest-mixing objective is its second-smallest combinatorial weighted-Laplacian eigenvalue. The budget is an equality; it would be saturated at any optimum under a non-strict inequality budget. No normalization by the number of vertex pairs, no stochastic holding probabilities, and no change to the underlying permitted edge set are implicit. The results hold for all real \(c,B>0\), not merely integer/rational prices.

## Proof

1. **Reduction to edge orbits without assuming an optimal symmetry.** Let \(N=2m\), \(P_0=\mathbf 1\mathbf 1^\top/N\), and \(A=L+P_0\). Every connected feasible assignment has positive definite \(A\), and \(\mathcal K=N(\operatorname{tr}(A^{-1})-1)\). The map \(A\mapsto\operatorname{tr}(A^{-1})\) is strictly convex on positive-definite symmetric matrices: for any nonzero symmetric \(H\), its second directional derivative is \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). The affine map from conductance vector to \(L\) is injective, since each off-diagonal entry identifies its corresponding conductance. The compact feasible set contains a connected assignment and disconnected approaches have divergent \(\mathcal K\), so the resistance optimum exists and is unique. It is fixed by every price-preserving automorphism, in particular the two community permutations and their swap, and hence is constant on the intercommunity and intracommunity edge orbits. Independently, \(\lambda_2(L)=\min_{x\perp\mathbf 1,\|x\|=1}x^\top Lx\) is concave in the edge weights; averaging any fastest-mixing optimum over the same automorphism group gives an optimum constant on the two orbits. This does not presume that the original fastest-mixing optimum is symmetric.

2. **Exact spectral calculation.** Write \(a\) for the common weight on each of the \(m^2\) intercommunity edges and \(b\) for the common weight on each of the \(m(m-1)\) intracommunity edges. The cost is \(m^2a+c m(m-1)b=B\). On the difference-of-community-constants eigenvector, \(L\) has eigenvalue \(2ma\). On each of the two community-internal zero-sum spaces (total dimension \(2(m-1)\)), it has eigenvalue \(m(a+b)\). The constant vector has eigenvalue zero. Consequently, for connected assignments \(a>0\),
\[
 \mathcal K=\frac1a+\frac{4(m-1)}{a+b},\qquad
 \lambda_2=m\min\{2a,a+b\}.
\]

3. **Resistance minimization and its boundary.** Set \(q=m-1\), \(r=b/a\ge0\). Budget saturation gives \(a=B/[m(m+cqr)]\). Thus
\[
 \mathcal K(r)=\frac mB(m+cqr)\left(1+\frac{4q}{1+r}\right),\qquad
 \mathcal K'(r)=\frac{mq}{B}\frac{c(1+r)^2-4(m-cq)}{(1+r)^2}.
\]
Its derivative has a unique strictly positive zero precisely when \(c<4m/(4m-3)\), and that zero is \(2\sqrt{m/c-q}-1\). Otherwise the derivative is nonnegative for all \(r\ge0\), strictly positive for \(r>0\). Substitution proves the allocation and minimum-value formulas in the finding. Uniqueness from step 1 extends the scalar result to all individual edge allocations, including both thresholds.

4. **Fastest mixing and support of every optimum.** For the same \(r\),
\[
 \lambda_2(r)=\frac{B\min\{2,1+r\}}{m+cqr}.
\]
On \(0\le r\le1\) the derivative has the sign of \(m-cq\); on \(r\ge1\) the function decreases strictly. Therefore the symmetric optimizer is \(r=1\) if \(c<m/q\), any \(r\in[0,1]\) if \(c=m/q\), and \(r=0\) if \(c>m/q\). Concave symmetrization gives the unrestricted optimal value. If \(c<m/q\) and an unrestricted optimum had every intracommunity conductance zero, its average would have symmetric \(r=0\), contradicting the unique symmetric maximizer \(r=1\). If \(c>m/q\) and an unrestricted optimum had a positive intracommunity conductance, its average would have positive symmetric \(r\), contradicting the unique symmetric maximizer \(r=0\). At equality the stated symmetric interval supplies both support patterns.

5. **Disagreement, compatibility, and scaling.** The positive difference \(c_M-c_R=m/[(m-1)(4m-3)]\) proves the disagreement interval. For \(c<c_M\) every symmetric fastest-mixing optimum has \(r=1\). The unique resistance optimum has \(r=1\) only for \(c=1\); for \(c\ge c_M\), its ratio is zero and this ratio is also fastest-mixing-optimal. Hence the exact compatibility classification. Finally, substituting \(c=1+\kappa/m\) into \(2\sqrt{m/c-(m-1)}-1\), enforcing the nonnegative boundary, and comparing \(c\) to the two thresholds yields the critical-window limits; no finite sample is used in this limiting argument.

## Verification

Run `python3 verify.py` from the directory containing the verifier using Python 3. No external library or input file is needed. The verifier reconstructs exact-rational Laplacians, checks their full projector expansions and unscaled Kirchhoff index by an independent Gauss–Jordan inverse, compares scalar optima against many rational competitors, and tests the edgewise Karush–Kuhn–Tucker conditions on exact rational instances. It reports `VERIFY_OK 4699`. These finite checks are reproducibility support, not a proof of the universal real-parameter statement; the analytic argument above supplies that proof.

## Relationship to prior work

Ghosh, Boyd, and Saberi [1] establish convex effective-resistance allocation and analytically solve trees, wheels and a pair of cliques linked by **one** edge; their equal-price complete-graph result is a special case of the present \(c=1\) setting, but their demonstrated topology does not prescribe this full complete-intercommunity price experiment. Sun, Boyd, Xiao, and Diaconis [2] establish the continuous-time fastest-mixing SDP, symmetry method, and examples on paths and cycles; their framework supports the spectral objective but does not state the compared two-objective price thresholds. Ellens and collaborators [3] provide an earlier example where adding a fixed edge optimizes Kirchhoff index differently from optimizing algebraic connectivity, so the qualitative possibility of disagreement is **not** claimed here. The new claim is the explicit complete-family price-window classification, the unrestricted resistance optimizer, all-optimum support statements for mixing, and the two distinct critical-window limits. The generic convex formulations do not directly give these closed thresholds. Related mathematical research records and primary literature were compared by object, invariant, edge-price rule, and implication rather than title alone.

## Limitations

There is no claim about arbitrary partitions of unequal size, unequal per-edge prices within an orbit, discrete-time stochastic transition kernels, or uniqueness of all nonsymmetric fastest-mixing optimizers. Equivalent results in unindexed literature might exist. An earlier July 2006 conference version of [1] is acknowledged, but its exact publicly available calendar day was not established; the first-public-date metadata uses the day-verified focal continuous-time mixing paper [2]. The results do not establish a general rule for arbitrary community topologies.

## References

[1] A. Ghosh, S. Boyd and A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* 50 (2008), 37–66. DOI: 10.1137/050645452. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf. An earlier conference version appeared in July 2006.

[2] J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699. DOI: 10.1137/S0036144504443821; electronic publication November 2, 2006. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[3] W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic and R. E. Kooij, “Effective graph resistance,” *Linear Algebra and its Applications* 435 (2011), 2491–2506. DOI: 10.1016/j.laa.2011.02.024; online March 17, 2011. Full text: https://www.nas.ewi.tudelft.nl/people/Piet/papers/LAA_2011_EffectiveResistance.pdf.
