# A sign-changing pitchfork–external-length dependence law in Kingman's coalescent

## Finding

For the standard Kingman coalescent on \(n\) sampled leaves, let \(P_n\) be the number of rooted pitchforks (three-leaf clades with an internal cherry), \(S_{n,k}\) the number of ancestral lineages still consisting of one original leaf immediately before the transition from \(k\) to \(k-1\) lineages, and \(E_n\) the sum of the original leaves' external branch lengths. For every integer \(n\ge5\) and \(2\le k\le n\),
\[
\operatorname{Cov}(P_n,S_{n,k})=
\frac{k(k-1)(n-k)(n-k-1)(2k-n)}{6(n-1)(n-2)(n-3)(n-4)}.
\]
Consequently the covariance is negative when \(2\le k<n/2\), positive when \(n/2<k\le n-2\), and zero at the intervening equality (when integral), or at \(k=n-1,n\). In particular,
\[
\operatorname{Cov}(P_n,E_n)=-\frac1{18}\qquad(n\ge5).
\]
At the small sizes, \(\operatorname{Cov}(P_2,E_2)=\operatorname{Cov}(P_3,E_3)=0\) and \(\operatorname{Cov}(P_4,E_4)=2/9\). This is a strict finite-size sign reversal between \(n=4\) and \(n=5\).

## Assumptions and scope

Each unordered pair among \(k\) current ancestral lineages merges at rate one, independently of the past. The holding time \(T_k\) at \(k\) lineages is exponential of rate \(\binom{k}{2}\) and is independent of the complete discrete merge history. Therefore \(E_n=\sum_{k=2}^n S_{n,k}T_k\), with \(\mathbb E T_k=2/[k(k-1)]\). A singleton lineage contains exactly one original leaf; a doubleton lineage contains exactly two. A pitchfork arises exactly when a doubleton lineage merges with a singleton lineage, regardless of whether that triple clade is later nested in a larger clade. All statements are exact for integer sample sizes and these specified rate units; changing all pairwise rates uniformly rescales external-length covariance by the reciprocal rate.

## Proof

Write \(S_k=S_{n,k}\) and \(W_k\) for the numbers of singleton and doubleton lineages at \(k\). The remaining \(k-S_k-W_k\) lineages each contain at least three original leaves. A merger of two singletons creates a doubleton, and a merger of a singleton with a doubleton creates exactly one pitchfork. For an integer \(r\ge0\), let \((z)_r=z(z-1)\cdots(z-r+1)\), with \((z)_0=1\), and set \(m_r(k)=\mathbb E[(S_k)_r]\). Following \(r\) marked original leaves through the uniformly chosen merges gives
\[
m_r(k)=\frac{(k)_r(k-1)_r}{(n-1)_r},\qquad 0\le r\le4,
\]
interpreting a falling factorial as zero whenever \(r\) exceeds its nonnegative integer argument. This expression is used for \(n\ge5\), so every denominator is nonzero.

A one-merge conditioning calculation, valid for \(r=0,1,2\), yields
\[
\mathbb E[(S_{k-1})_rW_{k-1}]
=\frac{(k-r-1)(k-r-2)}{k(k-1)}\mathbb E[(S_k)_rW_k]
+\frac{m_{r+2}(k)}{k(k-1)}.
\]
With \(W_n=0\), induction gives
\[
\mathbb E[(S_k)_rW_k]=\frac{m_{r+1}(k)(n-k)}{n-r-2},\qquad r=0,1,2.
\]
In particular, write \(f_k=\mathbb E[S_kW_k]=m_2(k)(n-k)/(n-3)\) and \(g_k=\mathbb E[(S_k)_2W_k]=m_3(k)(n-k)/(n-4)\).

Let \(P^{<k}\) count pitchfork mergers that have already occurred when \(k\) lineages remain. Define \(b_k=\mathbb E[P^{<k}]\) and \(c_k=\mathbb E[S_kP^{<k}]\). Since the next event is a singleton–doubleton merger with conditional probability \(2S_kW_k/[k(k-1)]\), and since the next expected singleton count is \((k-2)S_k/k\), conditioning gives
\[
b_{k-1}=b_k+\frac{2f_k}{k(k-1)},\qquad
c_{k-1}=\frac{k-2}{k}c_k+\frac{2g_k}{k(k-1)},\qquad b_n=c_n=0.
\]
Direct summation (or induction) gives
\[
b_k=\frac{(n-k)(n-k-1)(3k^2+2kn-9k+n^2-5n+6)}{6(n-3)(n-2)(n-1)},
\]
\[
c_k=\frac{k(k-1)(n-k)(n-k-1)(3k^2+2kn-17k+n^2-9n+26)}{6(n-4)(n-3)(n-2)(n-1)}.
\]

To account for pitchforks formed after the \(k\)-lineage state, mark an existing singleton–doubleton pair. The chance that its two lineages merge before meeting anything else is \(u_k=2/[3(k-1)]\) for \(k\ge3\). This follows from \(u_2=1\) and \(u_k=[1+\binom{k-2}{2}u_{k-1}]/\binom{k}{2}\). For three existing singleton lineages, the chance that they coalesce into a three-leaf clade before any outside merger is \(v_k=1/[(k-1)(k-2)]\) for \(k\ge4\); it follows from \(v_3=1\) and \(v_k=[3u_{k-1}+\binom{k-3}{2}v_{k-1}]/\binom{k}{2}\). At \(k=3\), the latter term is automatically absent for \(n\ge5\), as three singleton lineages could only contain three original leaves. Thus for \(3\le k\le n\), the conditional expected future pitchfork count is \(u_k S_kW_k+v_k\binom{S_k}{3}\), using either value for the irrelevant \(v_3\) term.

Since \(\mathbb E[S_k^2W_k]=f_k+g_k\) and \(\mathbb E[S_k\binom{S_k}{3}]=(m_4(k)+3m_3(k))/6\), the covariance of the total pitchfork count and the \(k\)-stage singleton count is
\[
\begin{aligned}
\operatorname{Cov}(P_n,S_k)
={}&c_k-m_1(k)b_k\\
&+u_k\bigl(f_k+g_k-m_1(k)f_k\bigr)\\
&+\frac{v_k}{6}\bigl(m_4(k)+3m_3(k)-m_1(k)m_3(k)\bigr).
\end{aligned}
\]
Substituting the displayed factorial moments and the closed \(b_k,c_k\) expressions, collecting rational factors, yields precisely the stated stagewise covariance formula for \(k\ge3\). For \(k=2\) no further pitchfork can form when \(n\ge5\); the previous formulas give \(c_2-m_1(2)b_2=-1/[3(n-1)]\), equal to the stated formula at \(k=2\). The \(k=n-1,n\) cases also vanish directly. This supplies the full range of stages without assuming any asymptotics.

Finally holding-time independence gives
\[
\begin{aligned}
\operatorname{Cov}(P_n,E_n)
&=\sum_{k=2}^n\frac{2}{k(k-1)}\operatorname{Cov}(P_n,S_k)\\
&=\frac{1}{3(n-1)(n-2)(n-3)(n-4)}
\sum_{k=2}^{n-2}(n-k)(n-k-1)(2k-n)\\
&=-\frac{1}{18},
\end{aligned}
\]
where the finite polynomial sum equals \(-(n-1)(n-2)(n-3)(n-4)/6\). The factor \(2k-n\) proves the sign classification. At \(n=2,3\) the pitchfork count is deterministic; for \(n=4\), direct enumeration of the first two merging steps gives \(\operatorname{Cov}(P_4,S_{4,2})=2/9\), while all other stages have zero covariance, and \(\mathbb E T_2=1\), proving the exceptional case.

## Verification

The standalone `verify_pitchfork_external.py` uses Python standard-library exact fractions. It (i) exhaustively enumerates all labeled unordered binary merge histories through seven leaves, (ii) independently evaluates a Markov-state recursion tracking singleton lineages, doubleton lineages and pitchfork count, and (iii) compares every stage and the total covariance with the claimed exact formulas for all sizes through thirty leaves. Its run completed with 520 exact assertions passing. These finite checks supplement rather than replace the universal algebraic proof above. Execute with `python verify_pitchfork_external.py` in the directory containing this file.

## Relationship to prior work

Janson and Kersting (2010) analyze total external lengths through singleton-lineage processes; their results establish important marginal structure but do not explicitly supply this pitchfork cross-covariance. Disanto and Wiehe (2011/2012) analyze the topology and joint cherry/pitchfork counts of coalescent trees, explicitly separating their tree-shape treatment from branch lengths. Choi, Thompson and Wu (2020) study further joint cherry/pitchfork shape laws. Alimpiev and Rosenberg (2021) catalog correlations among length-related tree statistics, not pitchfork count. Combining separate marginals or the known cherry/external-length covariance does not determine the stated pitchfork/external-length covariance. The present proof uses the additional doubleton-lineage state and mixed factorial moments.

## Limitations

The result assumes the standard neutral binary Kingman topology and constant pair-merger rate; it does not cover time-varying population sizes, simultaneous multiple mergers, or reconstructed tree estimators. The theorem is proved for this specific mixed statistic, not for arbitrary tree-shape indices. The literature comparison cannot establish absolute historical priority; earlier general joint enumerations may contain an implicit consequence. No independent audit has been performed.

## References

1. S. Janson and G. Kersting, *The external lengths in Kingman's coalescent*, arXiv:1004.5011, first posted 2010-04-28, https://arxiv.org/abs/1004.5011.
2. F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295, first posted 2011-12-06, https://arxiv.org/abs/1112.1295.
3. K. P. Choi, A. Thompson and T. Wu, *On cherry and pitchfork distributions of random rooted and unrooted phylogenetic trees*, arXiv:2002.12643, first posted 2020-02-28, https://arxiv.org/abs/2002.12643.
4. E. Alimpiev and N. A. Rosenberg, *A compendium of covariances and correlation coefficients of coalescent tree properties*, arXiv:2103.13467, first posted 2021-03-24, https://arxiv.org/abs/2103.13467.
