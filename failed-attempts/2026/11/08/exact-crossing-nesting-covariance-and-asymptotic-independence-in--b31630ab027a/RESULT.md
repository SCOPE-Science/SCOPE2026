# Exact crossing–nesting covariance and asymptotic independence in uniform chord diagrams

## Finding

Let \(M_n\) be a uniform perfect matching of \(2n\) cyclically ordered endpoints, with \(n\ge 2\). Let \(X_n\), \(N_n\), and \(A_n\) count, respectively, *crossing*, *nesting*, and *separated (aligned)* unordered pairs of chords. For every \(n\ge2\),

\[
\begin{aligned}
\mathbb E X_n=\mathbb E N_n=\mathbb E A_n&=\frac{n(n-1)}6,\\
\operatorname{Var}(X_n)=\operatorname{Var}(N_n)&=\frac{n(n-1)(n+3)}{45},\\
\operatorname{Cov}(X_n,N_n)&=-\frac{n(n-1)}{18},\\
\operatorname{Corr}(X_n,N_n)&=-\frac5{2(n+3)},\\
\operatorname{Var}(A_n)&=\frac{n(n-1)(2n+1)}{45},\\
\operatorname{Cov}(A_n,X_n)=\operatorname{Cov}(A_n,N_n)&=-\frac{n(n-1)(2n+1)}{90}.
\end{aligned}
\]

In particular, the crossing and nesting counts are strictly negatively correlated at every finite nontrivial size, yet their fluctuations are **asymptotically independent**:

\[
\left(\frac{X_n-\frac{n(n-1)}6}{\sqrt{n^3/45}},\frac{N_n-\frac{n(n-1)}6}{\sqrt{n^3/45}}\right)
\xrightarrow{\mathrm d}(G_1,G_2),
\qquad G_1,G_2\stackrel{\mathrm{iid}}{\sim}N(0,1).
\]

Since \(X_n+N_n+A_n=\binom n2\), the aligned count has the simultaneous limit \((A_n-n(n-1)/6)/\sqrt{n^3/45}\xrightarrow{\mathrm d}-G_1-G_2\). The theorem concerns **numbers of two-chord events**, not the sizes of maximal crossing or nesting families.

## Assumptions and scope

Each matching of \(\{1,\ldots,2n\}\) has probability \(1/(2n-1)!!\). For two chords with sorted endpoints \(a<b\) and \(c<d\), call their pair *crossing* when endpoints alternate, *nesting* when one interval properly contains the other, and *aligned* when the intervals are disjoint in the chosen linearization. These three classes partition all pairs. The counts are invariant under relabeling of the **chords**, and the crossing/nesting definitions use the chosen cyclic ordering of their distinct endpoints. The alignment statistic uses the order \(1,\ldots,2n\); it agrees with being noncrossing and nonnesting.

## Proof

**An independent-chord representation.** Draw \(2n\) independent uniform real numbers in \((0,1)\), group them consecutively into \(n\) labelled pairs, and replace their actual values by their ranks. Almost surely all endpoints are distinct; exchangeability of ranks shows that the resulting unlabelled matching is uniform. Thus the chord pairs \(Q_i=(L_i,R_i)\), where \(L_i<R_i\) are the sorted endpoints of two independent uniforms, form an iid sequence before rank reduction. The density of \((L,R)\) is \(2\) on \(0<l<r<1\).

For distinct \(i,j\), let \(h_X(Q_i,Q_j)\), \(h_N(Q_i,Q_j)\) and \(h_A(Q_i,Q_j)\) be the respective zero-one indicators. Then \(X_n=\sum_{i<j}h_X(Q_i,Q_j)\), and similarly for the other statistics. Given an anchor chord with endpoints \((l,r)\), put \(t=r-l\). Inspecting the two independent endpoints of a second chord gives the conditional probabilities

\[
 p_X(l,r)=2t(1-t),\qquad
 p_N(l,r)=t^2+2l(1-r),\qquad
 p_A(l,r)=l^2+(1-r)^2.
\]

Each unconditional indicator mean is \(1/3\), since the three pairings of four ranked endpoints are equally likely. Integration against density \(2\) on the triangle yields

\[
 \mathbb E[p_X^2]=\mathbb E[p_N^2]=\frac2{15},\quad
 \mathbb E[p_Xp_N]=\frac19,\quad
 \mathbb E[p_A^2]=\frac7{45},\quad
 \mathbb E[p_Xp_A]=\mathbb E[p_Np_A]=\frac4{45}.
\]

These identities can be checked term by term using \(\mathbb E[L^aR^b]=2/((a+1)(a+b+2))\) for nonnegative integers \(a,b\). In particular, the one-chord Hoeffding projections \(g_X=p_X-1/3\) and \(g_N=p_N-1/3\) satisfy

\[
 \mathbb E[g_X^2]=\mathbb E[g_N^2]=\frac1{45},\qquad
 \boxed{\mathbb E[g_Xg_N]=0}.
\]

**Exact covariance.** Indicators on *disjoint* chord-label pairs are independent. Two indicators on the *same* label pair, one crossing and one nesting, have covariance \(-1/9\), because they are mutually exclusive. On two different label pairs sharing exactly one chord, conditioning on the common chord gives covariance \(\mathbb E[g_Xg_N]=0\). Therefore only the \(\binom n2\) coincident pairs contribute:

\[
\operatorname{Cov}(X_n,N_n)=\binom n2\left(-\frac19\right)=-\frac{n(n-1)}{18}.
\]

For two crossing indicators sharing one chord, the covariance is \(\mathbb E[g_X^2]=1/45\); it is the same for two nesting indicators. There are \(6\binom n3=n(n-1)(n-2)\) *ordered* distinct pairs of chord-label pairs with exactly one chord in common. Since one crossing indicator has variance \(2/9\),

\[
 \operatorname{Var}(X_n)=\operatorname{Var}(N_n)
 =\binom n2\frac29+6\binom n3\frac1{45}
 =\frac{n(n-1)(n+3)}{45}.
\]

Dividing gives the claimed correlation. Since \(A_n=\binom n2-X_n-N_n\), the remaining variance and covariance formulas follow by bilinearity.

**Independent Gaussian limit.** The Hoeffding decomposition of the bounded order-two kernels gives

\[
 (X_n-\mathbb E X_n,N_n-\mathbb E N_n)
 =(n-1)\sum_{i=1}^n(g_X(Q_i),g_N(Q_i))+R_n,
 \quad \mathbb E\|R_n\|^2=O(n^2).
\]

The residual consists of degenerate order-two kernels; their covariances vanish between different label pairs, explaining the \(O(n^2)\) bound directly. The iid bivariate projection summands have mean zero and covariance \(I_2/45\), established by the preceding exact integrals. By the usual multivariate iid central limit theorem, dividing the displayed identity by \(\sqrt{n^3/45}\) gives \(N_2(0,I_2)\). A bivariate normal with diagonal identity covariance has independent coordinates. The aligned-count assertion follows from the deterministic sum identity.

## Verification

Run `python3 verify.py` in the directory containing this file. The self-contained Python standard-library checker performs exact rational integration of all projection polynomials and exhaustive independent matching enumeration for all \(2\le n\le7\), checking every stated finite covariance and variance. Its recorded output is `VERIFY_OK 75 exact assertions; exhaustive matchings through seven chords; polynomial integrals exact`. The checker is corroboration, not a substitute for the infinite-order argument, and does not establish literature originality.

## Relationship to prior work

Flajolet and Noy (2000) already established the marginal crossing moments and crossing Gaussian law. Chen, Deng, Du, Stanley and Yan (2005/2007) proved joint symmetry of **maximal crossing and nesting family sizes**; those maxima are different from the **total numbers of pairwise crossings and nestings** treated here. Paguyo (first posted April 2, 2021) studied convergence rates for crossing totals and simple-chord totals, and records the former literature. This finding does not claim the known marginal crossing variance or Gaussian limit as new. Its scoped claim is the exact *mixed* covariance, the rank-two orthogonality mechanism and independent bivariate limit, with the aligned-count consequences.

## Limitations

The exact formulas require uniform matchings, and do not cover biased endpoint orderings, conditioned matchings, or maximal \(k\)-crossing/\(k\)-nesting statistics. The Gaussian independence is a weak-limit statement; the finite counts remain dependent and negatively correlated. No convergence rate for the two-dimensional limit is proved. A more general unpublished or earlier two-chord joint enumerator may imply the mixed covariance; historical priority is not asserted conclusively. The analysis has not received independent mathematical validation.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, first arXiv posting 2021-04-02, https://arxiv.org/abs/2104.01134. Primary MSC2020: 60C05.
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA research report 3914 (2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf.
3. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley and C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230 (2005), https://arxiv.org/abs/math/0501230; Trans. Amer. Math. Soc. 359 (2007), 1555–1575.
4. J. Baik and R. Jenkins, *Limiting distribution of maximal crossing and nesting of Poissonized random matchings*, arXiv:1111.0269 (2011), https://arxiv.org/abs/1111.0269. This treats maximal statistics, not pair-count totals.
