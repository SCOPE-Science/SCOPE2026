# Poisson attractor selection and a sharp density window for NOR dynamics on Boolean cubes

## Finding

Synchronous open-neighborhood NOR on a Boolean cube turns independent random initial activations into a sharply selected population of two-cycle attractors. The number of occupied sites in the first updated phase has an exact variance, a quantitative Poisson approximation, and a critical initial-density window of width \(1/d\). At this window, the eventual two-cycle almost surely has finitely many isolated active sites in one phase and nearly every vertex active in the other. The probability of selecting the universal zero/full oscillation tends to \(\exp(-e^{-2c})\) when the initial activation density is \(p_d=1/2+c/d\).

## Assumptions and scope

For each integer \(d\ge3\), write \(Q_d\) for the undirected graph on \(V_d=\{0,1\}^d\), with two vertices adjacent exactly when their Hamming distance is one. Let \(N=2^d\) and \(D=\binom d2\). Identify a Boolean state with its set \(A\subseteq V_d\) of active vertices and define the synchronous, self-excluding NOR map
\[
T(A)=\{v\in V_d:N_{Q_d}(v)\cap A=\varnothing\}=V_d\setminus N_{Q_d}(A).
\]
There are no self-input loops. Initial activations are independent Bernoulli\((p)\), \(0<p<1\). Put \(r=1-p\), \(q=r^d\), \(\lambda=Nq\), and \(U=T(A)\), \(W=|U|\). The total-variation distance uses \(\sup_E|\Pr(Y\in E)-\Pr(Z\in E)|\). The attraction basin includes transient and already periodic states.

## Proof

**Undirected NOR polarity.** For any undirected graph, \(T\) is order-reversing and \(A\subseteq T^2(A)\): each neighbor of a site in \(A\) is excluded by \(T(A)\). Applying order reversal twice gives both \(T^3(A)\subseteq T(A)\) and \(T(A)\subseteq T^3(A)\), so \(T^3=T\). Thus every trajectory is periodic after at most one update, and the only possible periods are one and two. This general periodicity observation is not asserted as novel.

**Exact random first-image law.** Let \(I_v=\mathbf1_{\{v\in U\}}\). Its value is one exactly when all \(d\) neighbors of \(v\) were initially zero, so \(\Pr(I_v=1)=r^d=q\). In \(Q_d\), two *distinct* open neighborhoods intersect in exactly two vertices when the centers are at Hamming distance two, and are disjoint at all other distinct distances. Consequently
\[
\mathbb E[I_uI_v]=\begin{cases}r^{2d-2},&\operatorname{dist}(u,v)=2,\\r^{2d},&\operatorname{dist}(u,v)\ne2,\end{cases}\quad(u\ne v).
\]
There are \(ND\) ordered pairs at distance two. Hence
\[
\mathbb EW=Nr^d,\qquad
\operatorname{Var}W=Nr^d(1-r^d)+ND(r^{2d-2}-r^{2d}).
\]
In particular, at \(p=1/2\), \(\mathbb EW=1\) and \(\operatorname{Var}W=1+(3D-1)/N\).

**Quantitative Poisson and independent-location estimates.** The indicator \(I_v\) depends only on initial bits on \(N(v)\). It is independent of the entire family of indicators with centers outside \(B(v)=\{v\}\cup\{u:\operatorname{dist}(u,v)=2\}\). The Arratia–Goldstein–Gordon local-dependence quantities are therefore exactly
\[
b_1=N(1+D)r^{2d},\qquad b_2=ND r^{2d-2},\qquad b_3=0.
\]
Their count theorem gives the conservative bound
\[
d_{\mathrm{TV}}\bigl(W,\mathrm{Poisson}(\lambda)\bigr)\le2(b_1+b_2).
\]
Their indicator-process theorem also bounds the total-variation distance from the independent Bernoulli\((q)\) field by \(2(b_1+b_2)+Nq^2\). Thus the location field, not merely the number of defects, is asymptotically independent whenever the displayed right-hand side vanishes.

**Geometric separation and genuine two-cycles.** By a union bound over pairs at Hamming distance at most four,
\[
\Pr(\exists u\ne v\in U:\operatorname{dist}(u,v)\le4)
\le\frac{N}{2}\left[D r^{2d-2}+\Bigl(\sum_{j=1}^4\binom dj-D\Bigr)r^{2d}\right],
\]
where binomial coefficients with \(j>d\) are zero. If \(U\) has pairwise distances at least five, its vertex neighborhoods are disjoint. Therefore \(T^2(A)=T(U)=V_d\setminus N(U)\) and the two phases contain exactly \(W\) and \(N-dW\) active sites. For any \(v\notin U\), at most two of its neighbors can belong to \(N(u)\) for one \(u\in U\), and pairwise separation prevents additional coverage by any other codeword; hence \(T^2(U)=U\) for \(d\ge3\). In particular each singleton \(\{u\}\) is the sparse phase of a primitive two-cycle \((\{u\},V_d\setminus N(u))\), giving \(N\) distinct orbits. For fixed \(m\) and sufficiently large \(d\), every \(m\)-set of minimum distance at least five likewise forms a distinct primitive two-cycle, since \(N-dm>m\). A random \(m\)-subset violates this separation with probability \(O_m(d^4/N)\), giving \(\binom Nm(1+O_m(d^4/N))\) such orbits.

**Critical window and basin probabilities.** For \(p_d=1/2+c/d\) with fixed real \(c\), \(\lambda=N(1-p_d)^d=(1-2c/d)^d\to\lambda_c=e^{-2c}\), whereas \(b_1+b_2=O_c(d^2/N)\) and the pair-separation failure probability is \(O_c(d^4/N)\). Thus \(W\) converges in total variation to \(\mathrm{Poisson}(\lambda_c)\); each fixed \(m\) has limiting probability \(e^{-\lambda_c}\lambda_c^m/m!\). The complete zero/full orbit is reached exactly if \(U=\varnothing\) or if the initial state is all zero (for then \(U=V_d\)); these events are disjoint. Its basin probability is therefore exactly \(\Pr(W=0)+r^N\), converging to \(e^{-\lambda_c}\). A trajectory with an \(m\)-defect sparse phase but \(|U|\ne m\) must have \(|U|\ge N-dm\), an event of probability at most \(\lambda/(N-dm)\) by Markov's inequality; the other discrepancy is bounded by the separation-failure probability. Hence the same Poisson limit gives the complete asymptotic distribution of the sparse-phase defect count among the selected two-cycles. Since a Bernoulli\((p_d)\) initial state has about \(N/2\) active vertices, while the two phases on the separation event have \(O_{\Pr}(1)\) and \(N-O_{\Pr}(d)\) active vertices, the probability of already being on the orbit at update zero vanishes; the first periodic update is one with high probability.

For fixed \(p>1/2\), \(\lambda\to0\) and \(\Pr(W=0)\to1\). For fixed \(0<p<1/2\), \(\lambda\to\infty\) and the exact variance gives \(\operatorname{Var}(W)/\lambda^2\le1/\lambda+3D/N\to0\); Chebyshev yields \(\Pr(W=0)\to0\), and \(r^N\to0\). The sharp transition is thus centered at density one-half with window \(1/d\).

## Verification

The accompanying standard-library-only program `verify_nor_cube.py` independently enumerates every binary initial configuration for dimensions \(1\le d\le4\) (\(4+16+256+65{,}536=65{,}812\) states). It checks \(T^3=T\), the universal-orbit basin formula and exact moments, and reproduces the entire first-image histogram using a separate neighborhood-union inclusion–exclusion polynomial. It also verifies singleton two-cycles for \(d=3,4\). Run with `python3 verify_nor_cube.py`; the last output line should begin with `PASS`. These finite tests do not establish asymptotic statements, which rest on the analytic argument above and the cited published Poisson approximation theorem.

## Relationship to prior work

Aledo, Martínez and Valverde's 2015 graph-dynamical systems analysis and contemporaneous survey discuss the established fixed/two-cycle restriction for undirected NOR networks; this general dynamical fact is used here, not claimed as new. Arratia, Goldstein and Gordon's 1990 Poisson approximation theorems supply the general local-dependence method, and Chen and Xia provide a general point-process framework. The present cube-specific contribution is the exact dependent-field covariance calculation, its explicit critical scaling, and the resulting quantitative attractor-selection law and sparse-code orbit census. General statements about Poisson approximation do not state the cube NOR orbit populations or identify their basin transition. No claim is made that the Stein–Chen method or the general period bound is new.

## Limitations

The result describes the asymptotic basin distribution for independent Bernoulli initial states, not the complete deterministic attractor census or exact individual basin sizes for each finite cube. The code-based checks are finite only. The uniform density limits exclude the deterministic endpoint \(p=0\), which starts directly on the universal orbit. Priority against inaccessible, unindexed, or non-English historical results remains uncertain; no independent mathematical validation has been performed.

## References

1. R. Arratia, L. Goldstein and L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science 5 (1990), 403–434, doi:10.1214/ss/1177012015. See Section 3, Theorems 1–3. https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/pacs-1.pdf
2. L. H. Y. Chen and A. Xia, *Stein's Method, Palm Theory and Poisson Process Approximation*, arXiv:math/0410169, first submitted 2004-10-06. https://arxiv.org/abs/math/0410169
3. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), 594294; first published 2015-03-24, doi:10.1155/2015/594294. https://onlinelibrary.wiley.com/doi/10.1155/2015/594294
4. J. A. Aledo, S. Martínez and J. C. Valverde, *Graph Dynamical Systems with General Boolean States*, Applied Mathematics & Information Sciences 9 (2015), 1803–1808; published online 2015-07-01, doi:10.12785/amis/090417. https://www.naturalspublishing.com/files/published/8t0q772e3y35g7.pdf
