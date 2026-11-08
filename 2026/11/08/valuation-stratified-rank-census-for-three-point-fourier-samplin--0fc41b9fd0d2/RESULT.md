# Valuation-stratified rank census for three-point Fourier sampling on prime-power cycles
## Finding
For any prime \(p\), integer \(k\ge1\), and \(N=p^k\), write \(F_N=(\exp(2\pi i rc/N))_{r,c\in\mathbb Z_N}\). Given any three-element set \(R\), define \(t(R)\) and \(u(R)\) to be respectively the minimum and maximum \(p\)-adic valuations of its three pairwise differences, truncated at \(k\); since the points are distinct, these valuations are smaller than \(k\). Define \(t(C),u(C)\) similarly for any three-element column set \(C\).

The complex rank of the Fourier minor \(F_N[R,C]\) is exactly
\[
\operatorname{rank}F_N[R,C]=\begin{cases}
1,&t(R)+t(C)\ge k,\\
2,&t(R)+t(C)<k\text{ and }(u(R)+t(C)\ge k\text{ or }t(R)+u(C)\ge k),\\
3,&\text{otherwise.}
\end{cases}
\]
In particular, every singular three-point Fourier minor arises from two proportional restricted rows or two proportional restricted columns; there is no additional three-term cancellation mechanism.

For \(0\le t\le u<k\), the number of unordered three-element subsets with \((t(R),u(R))=(t,u)\) is
\[
A_{t,u}=\begin{cases}
\dfrac{N(p-1)(p-2)p^{2(k-t-1)}}6,&t=u,\\[5pt]
\dfrac{N(p-1)^2p^{2k-t-u-2}}2,&t<u.
\end{cases}
\]
Consequently, setting \(T_t=\sum_{u=t}^{k-1}A_{t,u}\), the numbers \(H_1,H_2,H_3\) of rank-one, rank-two, and rank-three minors among the ordered pairs of unordered index triples satisfy
\[
H_1=\sum_{t+s\ge k}T_tT_s,\qquad
H_{\le2}=\sum_{0\le t\le u<k}\sum_{0\le s\le v<k}A_{t,u}A_{s,v}\mathbf1_{\{u+s\ge k\ \mathrm{or}\ v+t\ge k\}},
\]
\[
H_2=H_{\le2}-H_1,\qquad H_3=\binom N3^2-H_{\le2}.
\]
The formulas include all prime-power orders, even the small cases with fewer than three points (where all totals are zero). For each fixed prime \(p\), the exact singular-minor fraction has the limiting law
\[
\lim_{k\to\infty}p^{k+1}\frac{H_{\le2}}{\binom{p^k}3^2}=6.
\]
For example, \(p=3,k=3\) gives \((H_1,H_2,H_3)=(4455,323676,8227494)\), while \(p=5,k=3\) gives \((5687500,725000000,100234375000)\).

## Assumptions and scope
All matrices and ranks are over \(\mathbb C\). Index triples consist of distinct residues in \(\mathbb Z_N\), without ordering within either set; a pair \((R,C)\) is ordered in the row-versus-column sense. The valuation of a nonzero difference is the largest integer \(j<k\) for which \(p^j\) divides any integer representative. All sums over empty index ranges are zero. No assertion about higher-order minors is made.

## Proof
**Cyclotomic rigidity for three-by-three determinants.** Translate each index triple to include zero. Translation only introduces nonzero row and column factors, preserving rank and vanishing. Write the row set as \(\{0,a,b\}\) and column set as \(\{0,c,d\}\). The three positive determinant monomials have exponents, modulo \(N\),
\[
P=(ac+bd,\ ad,\ bc),
\]
and the three negative monomials have exponents
\[
Q=(ad+bc,\ ac,\ bd).
\]
Let \(f_j\) be the signed count (positive minus negative) at residue \(j\), and \(f(X)=\sum_{j=0}^{N-1}f_jX^j\). If \(f(\zeta)=0\) for a primitive \(N\)-th root \(\zeta\), then the irreducible cyclotomic polynomial \(\Phi_{p^k}(X)=\sum_{h=0}^{p-1}X^{hp^{k-1}}\) divides \(f(X)\). With \(m=p^{k-1}\), this implies \(f_{r+hm}=q_r\) independent of \(h\), for each \(0\le r<m\). There are exactly three positive and three negative terms, so for \(p\ge5\) every \(q_r=0\). For \(p=2,3\), a nonzero \(q\) can only have one \(+1\) and one \(-1\), located at different residues \(r,s\) modulo \(m\) (because \(\sum_rq_r=0\)). But the formal sum of the positive exponents equals the formal sum of the negative exponents, both equal to \((a+b)(c+d)\). Reducing this first-moment equality modulo \(N=pm\) would give \(p(r-s)\equiv0\pmod {pm}\), forcing \(r=s\pmod m\), a contradiction. Thus \(f_j=0\) for all \(j\) in every characteristic: the two triples \(P,Q\) of exponent residues must coincide as multisets.

Match the three positive exponents to the three negative ones. There are exactly six bijections, listed below.

For precision, the complete six matching cases in \(P_i=Q_{\sigma(i)}\), with \(P=(ac+bd,ad,bc)\) and \(Q=(ad+bc,ac,bd)\), are:
\[
\begin{array}{c|c}
\sigma&\text{equivalent nontrivial congruences modulo }N\\ \hline
(0,1,2)&a(c-d)=b(c-d)=0\\
(0,2,1)&(a-b)c=(a-b)d=0\\
(1,0,2)&bc=bd=0\\
(1,2,0)&ad=bd=0\\
(2,0,1)&ac=bc=0\\
(2,1,0)&ac=ad=0
\end{array}
\]
Each case says two selected rows or two selected columns are proportional as vectors on the other triple. Conversely, proportional selected rows or columns trivially force determinant zero. A row pair \(r,r'\) is proportional on \(C\) exactly when \((r-r')(c-c')\equiv0\pmod N\) for every \(c,c'\in C\). Taking the difference with smallest \(p\)-valuation shows this is equivalent to \(v_p(r-r')+t(C)\ge k\). Existence of such a pair is equivalent to \(u(R)+t(C)\ge k\); the dual statement is \(u(C)+t(R)\ge k\). Every two-by-two minor vanishes if and only if \(t(R)+t(C)\ge k\). This establishes all three ranks and the absence of an unaccounted cancellation case.

**Counting valuation strata.** When \(t=u\), each selected pair has the same valuation \(t\). Choose an anchor point in \(N\) ways and two lifts whose quotients modulo \(p^{k-t}\) have distinct nonzero residues modulo \(p\). There are \((p-1)(p-2)p^{2(k-t-1)}\) such ordered choices, and each three-set occurs with six anchor/orderings. This gives \(A_{t,t}\). When \(t<u\), precisely one pair has valuation \(u\). Its unordered choices number \(N(p-1)p^{k-u-1}/2\). Choose the third point at valuation \(t\) from either member of that pair: \((p-1)p^{k-t-1}\) choices. Multiplication yields \(A_{t,u}\). Counting all \((R,C)\) by these mutually exclusive strata and applying the rank test gives the displayed exact incidence formulas.

**Sparse-minor asymptotics.** For uniformly sampled independent unordered triples \(R,C\), let \(E_1\) be \(\{u(R)+t(C)\ge k\}\) and \(E_2\) its transposed counterpart. The singularity event is exactly \(E_1\cup E_2\). For any fixed \(s\ge1\), as \(k\to\infty\),
\[
\Pr[t(C)=s]\longrightarrow(1-p^{-2})p^{-2s},\qquad
N\Pr[u(R)\ge k-s]\longrightarrow3(p^s-1).
\]
The first formula counts triples in one residue class modulo \(p^s\) but not modulo \(p^{s+1}\); the second uses the three possible close pairs, whose multiple intersections have negligible probability. The uniform bounds \(\Pr[t(C)=s]\le K_pp^{-2s}\) and \(N\Pr[u(R)\ge k-s]\le K_pp^s\) permit dominated summation, giving
\[
\lim_{k\to\infty}N\Pr(E_1)
=3(1-p^{-2})\sum_{s\ge1}(p^s-1)p^{-2s}=\frac3p.
\]
The same holds for \(E_2\). Their intersection is \(O_p(k^2/N^2)\): for \(t(R)+t(C)\ge k\), use \(\Pr[t(R)=h]\le K_pp^{-2h}\); otherwise the joint conditions demand both an unusually close pair in \(R\) and an unusually close pair in \(C\). The stratum counts give \(\Pr[t(R)=h,u(R)\ge k-s]\le K_pp^{-h-k+s}\), with the dual bound \(\Pr[t(C)=s,u(C)\ge k-h]\le K_pp^{-s-k+h}\); their product is at most \(K_p^2/N^2\), summed over at most \(k^2\) choices of \((h,s)\). Thus \(N\Pr(E_1\cap E_2)\to0\), and \(N\Pr(E_1\cup E_2)\to6/p\), as claimed.

## Verification
The included standalone Python verifier uses only integer arithmetic. It independently reduces three-by-three determinant monomial counts modulo \(\Phi_{p^k}\), checks every two-by-two minor exactly for rank one, and enumerates all index triples after row and column translation. It compares these independently obtained ranks against the valuation criterion and the exact counting formulas for \((p,k)\) equal to \((2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(5,2),(7,1)\). For larger examples \((3,4),(5,3),(7,3),(11,4)\), it checks the integral stratum formula and the complete rank partition without exhaustive determinant enumeration. The successful marker is `PRIME_POWER_TRIPLE_FOURIER_EXACT_CHECKS_PASS`. Exact finite tests corroborate but do not replace the general proof above.

## Relationship to prior work
Chebotarev's theorem on prime Fourier minors, as used in Tao's prime-order uncertainty principle, establishes the nonsingularity baseline at \(k=1\). Alexeev–Cahill–Mixon and Osgood–Siripuram–Wu characterize *universal* prime-power Fourier row sets, meaning sets whose every same-size minor is nonsingular; these results do not give the present rank of every individual pair of triples or its full valuation census. Earlier published work on all three-by-three Fourier minors at odd prime-square order gives precisely the \(k=2\) specialization; previously published work on dyadic cyclic orders treats \(p=2\). The newly determined odd-prime strata at \(k\ge3\), exact all-rank counts, and common asymptotic \(6/(pN)\) are not implied by these more restricted statements. The classification of principal three-point minors at arbitrary composite modulus applies only when the two index sets coincide, not to arbitrary \((R,C)\). The present result makes no historical exclusivity claim beyond the literature comparisons undertaken.

## Limitations
The statement is restricted to complex three-by-three Fourier minors on cyclic prime-power groups. It does not establish analogous formulas for larger minors or general composite cyclic orders. Exact checker tests cover finitely many small prime-power orders; the infinite result rests on the cyclotomic argument, counting, and asymptotic estimates. Broader generalized-Vandermonde classification literature could contain an equivalent theorem not identified in this bounded comparison. The asymptotic is for fixed \(p\) as \(k\to\infty\), not a uniform bound over simultaneous growth of \(p,k\).

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first public 2003-08-29.
2. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public 2011-10-17; see Theorem 9.
3. B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992, first public 2012-04-04; see Theorem 4.
4. *All singular three-by-three minors of prime-square Fourier matrices*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b.
5. *Exact singularity criterion for three-point principal Fourier minors*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-singularity-criterion-for-three-point-principal-fourier-mi--1482c28703d6.
