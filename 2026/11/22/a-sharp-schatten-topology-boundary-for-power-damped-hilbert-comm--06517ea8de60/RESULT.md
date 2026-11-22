# A sharp Schatten-topology boundary for power-damped Hilbert commutators

## Finding
Let \(H\) be the classical Hilbert matrix on \(\ell^2(\mathbb N)\), let \(D_s e_n=n^{-s}e_n\) for \(s>0\), and write \(K_s=D_sH-HD_s\). For every \(s>0\), \(K_s\) is trace class, has infinite rank, and the compact selfadjoint operator \(iK_s\) has infinitely many positive and infinitely many negative eigenvalues. As \(s\downarrow0\), the following sharp distinction among Schatten topologies holds:
\[
\|K_s\|_{\mathcal S_p}\longrightarrow0\quad\text{for every }1<p\le\infty,
\qquad 0<\liminf_{s\downarrow0}\|K_s\|_{\mathcal S_1}\le\limsup_{s\downarrow0}\|K_s\|_{\mathcal S_1}<\infty.
\]
More precisely, for every \(s>0\),
\[
\|K_s\|_{\mathcal S_1}\ge
\frac{2^{-2s}\big((5/4)^{-s}-(7/4)^{-s}\big)}{8(1-2^{-s})},
\qquad
\liminf_{s\downarrow0}\|K_s\|_{\mathcal S_1}\ge\frac{\log(7/5)}{8\log2}>0.
\]
For \(0<s\le1/4\), there is an absolute constant \(C\) such that \(\|K_s\|_{\mathcal S_1}\le C\). Quantitatively, for \(0<s\le1\),
\[
\|K_s\|_{\mathcal S_2}^2\le
\frac{23s^2(\log2)^2}{1-2^{-2s}}.
\]
Thus \(\|K_s\|_{\mathcal S_p}=O_p(s^{1-1/p})\) when \(1<p<2\) and \(O(s^{1/2})\) when \(2\le p\le\infty\). The exponents in these upper bounds are not asserted optimal. The exact limit of the trace norm is not determined.

## Assumptions and scope
The matrix entries are \(H_{mn}=(m+n-1)^{-1}\) for integers \(m,n\ge1\), with the usual complex Hilbert-space inner product. The classical Hilbert inequality ensures that \(H\) is bounded. All Schatten norms are the norms of the full infinite-dimensional operators. The endpoint \(s=0\) is assigned \(D_0=I\), so \(K_0=0\); the theorem says that this endpoint is continuous in every \(\mathcal S_p\) topology with \(p>1\), but not in trace norm. No claim of optimal trace-norm constant, complete singular-value asymptotics, or general moment-sequence extension is made.

## Proof
**1. Trace-class membership.** For \(0<t<1\) set \(v_t=(1,t,t^2,\ldots)\) and \(u_{s,t}=D_sv_t\). The Hilbert matrix has the weak rank-one representation \(H=\int_0^1v_t\otimes v_t\,dt\), hence
\[
D_sH=\int_0^1u_{s,t}\otimes v_t\,dt,
\qquad
K_s=\int_0^1(u_{s,t}\otimes v_t-v_t\otimes u_{s,t})\,dt.
\]
Here \(\|v_t\|_2^2=(1-t^2)^{-1}\) and \(\|u_{s,t}\|_2^2=\sum_{n\ge1}n^{-2s}t^{2n-2}\). With \(q=1-t^2\), the latter sum is \(O_s(q^{2s-1})\) if \(0<s<1/2\), \(O(1+|\log q|)\) if \(s=1/2\), and \(O_s(1)\) if \(s>1/2\). Consequently \(\int_0^1\|u_{s,t}\|\|v_t\|dt<\infty\) for each \(s>0\). Both \(D_sH\) and its adjoint \(HD_s\) therefore are Bochner trace-class integrals. In particular \(K_s\) is trace class, real skew-symmetric, and \(K_s^*=-K_s\).

**2. Uniform trace-norm control as \(s\downarrow0\).** For real vectors \(u,v\) the rank-two antisymmetric operator \(u\otimes v-v\otimes u\) has trace norm \(2\sqrt{\|u\|^2\|v\|^2-|\langle u,v\rangle|^2}\). Let \(N\) have the geometric distribution \(\Pr(N=n)=q(1-q)^{n-1}\) with \(q=1-t^2\). The integrand in the preceding representation has trace norm exactly
\[
\frac2q\sqrt{\operatorname{Var}_q(N^{-s})}.
\]
Put \(Y=qN\). If \(0<s\le1/4\), the elementary mean-value inequality gives, for every \(y>0\),
\[
|y^{-s}-1|^2\le s^2(1+y^{-1/2})\log^2y.
\]
The absolute constant
\[
M:=\sup_{0<q\le1}\mathbb E_q\big[(1+(qN)^{-1/2})\log^2(qN)\big]
\]
is finite. Indeed \(q(1-q)^{n-1}\le e q e^{-qn}\). On \(qn\le1\), the function \((1+y^{-1/2})\log^2y\) decreases, allowing integral comparison with its integrable singularity at zero (and the finite bound \(\sup_{0<q\le1}q(1+q^{-1/2})\log^2q<\infty\)). On \(qn>1\), use \(e^{-y}(1+y^{-1/2})\log^2y\le C e^{-y/2}\) and the uniformly bounded geometric sum \(q\sum_{n\ge1}e^{-qn/2}\). Since variance is no larger than the squared distance from any constant, taking \(q^s\) as that constant shows
\[
\sqrt{\operatorname{Var}_q(N^{-s})}\le \sqrt M\,s q^s.
\]
The Bochner triangle inequality and the beta integral yield
\[
\|K_s\|_{\mathcal S_1}
\le2\sqrt M\,s\int_0^1(1-t^2)^{s-1}dt
=\sqrt M\,s B(1/2,s)
=\sqrt{\pi M}\,\frac{\Gamma(s+1)}{\Gamma(s+1/2)}.
\]
The right-hand side is bounded uniformly for \(0<s\le1/4\).

**3. Convergence in Hilbert–Schmidt and larger ideals.** Partition \(\mathbb N\) into dyadic shells \(S_k=[2^k,2^{k+1})\cap\mathbb N\). For entries with both indices in \(S_k\),
\[
|m^{-s}-n^{-s}|\le s(\log2)2^{-sk},
\]
and the sum of their squared kernel entries is at most \(s^2(\log2)^2 2^{-2sk}\). For \(m\in S_k\), \(n\in S_{k+j}\), \(j\ge1\), the squared-block contribution is at most
\[
2^{-j}2^{-2sk}(1-2^{-s(j+1)})^2
\le 2^{-j}2^{-2sk}s^2(j+1)^2(\log2)^2.
\]
Summing both orientations and using \(\sum_{j\ge1}2^{-j}(j+1)^2=11\) proves
\[
\|K_s\|_{\mathcal S_2}^2\le
\frac{(1+2\cdot11)s^2(\log2)^2}{1-2^{-2s}}=O(s).
\]
The uniformly bounded trace norm from Step 2 and Schatten interpolation give convergence in every \(\mathcal S_p\) for \(1<p<2\), with the stated rate. For \(p\ge2\), monotonicity of Schatten norms gives the \(O(\sqrt s)\) estimate.

**4. A persistent trace-norm obstruction.** For \(k\ge2\) put \(n_k=2^k\) and choose disjoint index intervals
\[
A_k=[n_k,5n_k/4)\cap\mathbb N,\qquad
B_k=[7n_k/4,2n_k)\cap\mathbb N.
\]
Their cardinalities both equal \(n_k/4\). Let \(u_k,v_k\) be the normalized indicator vectors of these intervals. Every \(m\in A_k\), \(n\in B_k\) satisfies
\[
K_s(m,n)\ge \frac{n_k^{-s}\big((5/4)^{-s}-(7/4)^{-s}\big)}{4n_k}>0.
\]
Thus \(\langle u_k,K_sv_k\rangle\ge n_k^{-s}\Delta_s/16\) with \(\Delta_s=(5/4)^{-s}-(7/4)^{-s}\). Each two-dimensional compression onto \(\operatorname{span}\{u_k,v_k\}\) is skew with trace norm at least \(n_k^{-s}\Delta_s/8\). The compression spaces are pairwise orthogonal. Finite orthogonal pinching cannot increase trace norm, so for every \(J\ge2\)
\[
\|K_s\|_{\mathcal S_1}\ge\frac{\Delta_s}{8}\sum_{k=2}^{J}2^{-ks}.
\]
Letting \(J\to\infty\) gives the displayed lower bound, and the limit follows from \(\Delta_s=s\log(7/5)+O(s^2)\) and \(1-2^{-s}=s\log2+O(s^2)\). This proves the trace-ideal topology separation.

**5. Infinite positive and negative spectra.** Fix any \(N\ge1\) and suppose the first \(N\) columns of \(K_s\) were dependent, with coefficients \(c_1,\dots,c_N\). Define rational functions
\[
A(z)=\sum_{j=1}^N\frac{c_j}{z+j-1},\qquad
B(z)=\sum_{j=1}^N\frac{c_jj^{-s}}{z+j-1}.
\]
Column dependence gives \(m^{-s}A(m)=B(m)\) for every sufficiently large integer \(m\). If \(s\) is not an integer, the rational ratio \(A/B\) cannot agree with \(m^s\) along all large integers: any nonzero rational function has an integer power leading asymptotic as \(m\to\infty\). If \(s=p\ge1\) is an integer, the rational function \(A(z)-z^pB(z)\) has infinitely many zeros and hence vanishes identically. Comparing residues at \(z=1-j\) gives \(c_j[1-((1-j)/j)^p]=0\). Since \(|(1-j)/j|<1\), every \(c_j=0\), a contradiction. Thus \(K_s\) has infinite rank. Finally, \(iK_s\) is compact selfadjoint and complex conjugation sends it to its negative, so its nonzero eigenvalues occur in opposite pairs with equal multiplicity. Infinite rank forces infinitely many strictly positive and strictly negative eigenvalues.

## Verification
A standalone standard-library checker, `check.py`, verifies the stated dyadic estimates on explicit finite blocks, the pinching witnesses on multiple integer shells, the sharp positive lower-limit constant by independent finite-parameter evaluations, and the exact matrix skew-symmetry and finite-rank diagnostics. Run `python3 check.py`. A further independent finite-section check used numerical singular-value decomposition on dimensions \(32\), \(128\) and \(256\) and verified positive nuclear norms alongside shrinking quadratic norms for small damping. The finite checks are illustrations and do not prove the infinite-dimensional statements; Steps 1–5 supply their proofs.

## Relationship to prior work
Frank, Sukochev and Zanin (2024) develop endpoint Schatten theory for commutators of fractional Laplacians with multipliers in Euclidean spaces. Their operators and limiting regimes differ from the discrete Hilbert-matrix power-damping family here. Chatzifountas, Girela and Peláez (2013) characterize Schatten behavior of generalized Hilbert/Hankel moment matrices themselves, rather than these commutators. The 2026 published result *A universal square-root Hilbert–Schmidt cusp for power-damped Hankel moments* treats exactly the same Hilbert commutator and establishes \(\|K_s\|_{\mathcal S_2}^2=\pi^2s/6+O(s^2)\); it expressly does not assert trace-class membership, trace-norm behavior, or an all-\(p\) Schatten topology classification. The present theorem addresses those distinct trace-ideal and inertia conclusions. Known abstract trace-ideal estimates do not by themselves establish the quantitative nonzero lower endpoint obstruction without a comparison to this particular matrix.

## Limitations
The positive lower bound is not asserted sharp, and neither the existence nor the value of \(\lim_{s\downarrow0}\|K_s\|_{\mathcal S_1}\) is established. The stated rates for \(p>1\) are upper bounds, not matched asymptotics. The proof is specific to the classical Hilbert kernel; it does not directly establish the same boundary for arbitrary Hankel moments. An equivalent result under a different Mellin or paracommutator formulation could exist in literature not indexed by the searches. Independent mathematical validation has not been performed.

## References
1. R. L. Frank, F. Sukochev and D. Zanin, *Endpoint Schatten class properties of commutators*, arXiv:2405.10652, first public 2024-05-17. https://arxiv.org/html/2405.10652v1
2. C. Chatzifountas, D. Girela and J. Á. Peláez, *A generalized Hilbert matrix acting on Hardy spaces*, arXiv:1309.6125, first public 2013-09-24. https://arxiv.org/abs/1309.6125
3. *A universal square-root Hilbert–Schmidt cusp for power-damped Hankel moments* (2026), publicly available mathematical research result. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-universal-square-root-hilbert-schmidt-cusp-for-power-damped-ha--04e588d68667
