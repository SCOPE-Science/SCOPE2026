# A dimension-five Hilbert–Schmidt threshold for mixed coordinate Cesàro commutators

## Finding
For every integer \(d\ge 2\), let \(H_d^2\) be the complex Drury–Arveson space on the unit ball of \(\mathbb C^d\), and let \(C_j\) denote the coordinate Cesàro operators introduced by Pilla. For distinct coordinates \(j,k\), put \(K_{jk}=C_jC_k-C_kC_j\). Then
\[
K_{jk}\in\mathcal S_2(H_d^2)\quad\Longleftrightarrow\quad 2\le d\le5.
\]
In every dimension the operators \(C_j\) and \(C_k\) fail to commute.

Let \(\Pi_n\) project orthogonally onto all homogeneous polynomials of degree \(n\), and define the finite shell energy \(h_d(n)=\|K_{jk}\Pi_n\|_{\mathcal S_2}^2\). For each integer \(d\ge5\), the positive, finite constant
\[
\kappa_d=\sum_{p,q\ge0}\frac{(p-q)^2p!q!}{(d+p+q-1)!}\in(0,\infty)
\]
gives the exact asymptotic
\[
\lim_{n\to\infty}(n+1)^{7-d}h_d(n)=\kappa_d.
\]
Consequently, if \(S_d(N)=\sum_{n=0}^Nh_d(n)\), then
\[
S_6(N)\sim\kappa_6\log N,\qquad
S_d(N)\sim\frac{\kappa_d}{d-6}N^{d-6}\quad(d\ge7).
\]
In dimension \(5\), the shell energy satisfies \(h_5(n)\sim\kappa_5(n+1)^{-2}\); for dimensions \(2,3,4\), summability follows from a uniform degree bound. These are ordinary Hilbert–Schmidt statements, not assertions about operator-norm compactness or any other Schatten exponent.

## Assumptions and scope
The monomials \(z^\alpha\), indexed by \(\alpha\in\mathbb N_0^d\), are orthogonal in \(H_d^2\) with squared norm
\[
w_\alpha=\frac{\alpha_1!\cdots\alpha_d!}{(|\alpha|)!}.
\]
For \(1\le j\le d\), Pilla's bounded coordinate Cesàro operator is determined on monomials by
\[
C_jz^\alpha=\sum_{r=0}^\infty\frac{z^{\alpha+r e_j}}{|\alpha|+r+1}.
\]
Here \(e_j\) is the \(j\)-th coordinate vector. The result concerns the *mixed, non-adjoint* commutator for distinct coordinates. The complex dimension \(d\) is fixed when the homogeneous degree tends to infinity. All infinite claims follow from the calculations below; truncated tests are supplementary.

## Proof
**1. The exact mixed coefficient.** Write \(m=|\alpha|\), and let \(p,q\) be nonnegative integers. The unique coefficient of \(z^{\alpha+p e_j+q e_k}\) in \(C_jC_kz^\alpha\) equals \(1/((m+q+1)(m+p+q+1))\); the reversed product has \(m+p+1\) in place of \(m+q+1\). Thus
\[
K_{jk}z^\alpha=\sum_{p,q\ge0}
\frac{p-q}{(m+p+1)(m+q+1)(m+p+q+1)}
 z^{\alpha+p e_j+q e_k}.
\]
The coefficient identity holds first for polynomial truncations and then in the Hilbert space because both Cesàro operators are bounded. Distinct pairs \((p,q)\) produce distinct output monomials for each fixed input monomial. In particular, the coefficient of \(z_j\) in \(K_{jk}1\) is \(1/4\), so the commutator is nonzero.

**2. Sum over the entire homogeneous shell.** Put \(s=p+q\) and use the normalized basis \(w_\alpha^{-1/2}z^\alpha\). For each input degree \(m\), the sum of the norm-weight ratios is exactly
\[
\begin{aligned}
F_d(m,p,q)
&=\sum_{|\alpha|=m}\frac{w_{\alpha+p e_j+q e_k}}{w_\alpha}\\
&=\frac{p!q!(m+d+s-1)!}{(d+s-1)!(m+s)!}\\
&=\frac{1}{\binom{s}{p}}\prod_{r=1}^{d-1}\frac{m+s+r}{s+r}.
\end{aligned}
\]
To verify this, note that each weight ratio equals \((\alpha_j+1)_p(\alpha_k+1)_q/(m+1)_s\), where \((a)_r\) denotes the rising factorial. Summing over all multi-indices of degree \(m\) gives the coefficient of \(t^m\) in \(p!q!(1-t)^{-(d+s)}\), followed by division by \((m+1)_s\). No restriction to symmetric inputs is involved.

Therefore the *exact* squared Hilbert–Schmidt energy from the input degree \(m\) is
\[
h_d(m)=\sum_{p,q\ge0}
\frac{(p-q)^2 F_d(m,p,q)}{(m+p+1)^2(m+q+1)^2(m+s+1)^2}.
\]
All terms are nonnegative, so rearrangements and subsequent sums use Tonelli's theorem.

**3. The summable domination.** Let the displayed summand be \(E_{d,m}(p,q)\). Since
\[
(m+p+1)(m+q+1)=(m+1)(m+s+1)+pq
\]
and since \((m+s+r)/(s+r)\le(m+s+1)/(s+1)\), we have
\[
E_{d,m}(p,q)\le\frac{s^2}{\binom{s}{p}}
\frac{(m+s+1)^{d-5}}{(m+1)^2(s+1)^{d-1}}.
\]
For \(d\ge5\), use \(m+s+1\le(m+1)(s+1)\). For \(2\le d\le5\), use \(m+s+1\ge s+1\) with the nonpositive exponent. Hence
\[
E_{d,m}(p,q)\le
\frac{s^2}{(s+1)^4\binom{s}{p}}
\begin{cases}
(m+1)^{-2},&2\le d\le5,\\
(m+1)^{d-7},&d\ge5.
\end{cases}
\]
At \(d=5\), the two expressions agree. The \(s=0\) term vanishes. For \(s\ge1\),
\[
\sum_{p=0}^s\binom{s}{p}^{-1}\le 2+\frac{s-1}{s}<3,
\]
with the elementary separate interpretation for \(s=1\). Since \(\sum_{s\ge1}s^2/(s+1)^4<\infty\), the homogeneous energies are bounded by a constant times \((m+1)^{-2}\) for \(2\le d\le5\). Summing over \(m\) proves the asserted Hilbert–Schmidt membership.

**4. Exact shell constant and necessity.** For fixed \(p,q\) and \(d\ge5\), factorial cancellation gives
\[
\lim_{m\to\infty}(m+1)^{7-d}E_{d,m}(p,q)
=\frac{(p-q)^2p!q!}{(d+p+q-1)!}.
\]
The \(d\ge5\) bound in Step 3, after multiplication by \((m+1)^{7-d}\), is a single summable majorant independent of \(m\). Dominated convergence proves the exact limit with \(\kappa_d\); the terms \((p,q)=(1,0),(0,1)\) show \(\kappa_d>0\). For \(d=5\), the positive limit and a summable \((m+1)^{-2}\) bound are consistent.

For \(d=6\), \(h_6(m)\sim\kappa_6/(m+1)\), so summing gives \(S_6(N)\sim\kappa_6\log N\). For \(d\ge7\), \(h_d(m)\sim\kappa_d(m+1)^{d-7}\), and the integral comparison of positive powers yields \(S_d(N)\sim\kappa_d N^{d-6}/(d-6)\). Both diverge, so \(K_{jk}\notin\mathcal S_2\) for every \(d\ge6\). This completes the two-sided threshold proof.

## Verification
The supplementary standalone checker `check_commutator.py` uses exact rational arithmetic. It independently sums monomial norm ratios over finite multi-index shells, verifies the factorial identity, checks individual domination inequalities for sample dimensions and degrees, and checks positivity of the one-step lower contributions. Its successful execution returns `EXACT_COMMUTATOR_CHECK_OK 11591`. These checks test finite identities only; the proof of the infinite-dimensional criterion is Steps 1–4.

## Relationship to prior work
Pilla's 2026 introduction of the coordinate Cesàro tuple establishes the defining formula, boundedness, integral description, and single-coordinate spectral information (arXiv:2606.24710). His companion paper (arXiv:2606.25885) concerns operator norms and Rhaly-type coordinate generalizations. The present assertion instead identifies the Hilbert–Schmidt membership of **mixed products in different coordinates**, with the sharp dimension cutoff and homogeneous-degree divergence law. Single-coordinate spectrum or norm bounds do not imply these mixed commutator estimates. Classical Schatten results for adjoint commutators of Drury–Arveson coordinate *multipliers* concern different operators; they do not provide the stated factorial energy identity. The available source searches identified no equivalent or stronger published specialization, but publication priority is not independently certified.

## Limitations
The theorem treats the mixed non-adjoint commutator only, for fixed finite complex dimension \(d\ge2\). It neither classifies its spectrum nor determines its compactness, full singular-value asymptotics, or membership in \(\mathcal S_p\) for \(p\ne2\). The secondary Pilla preprint was accessible through its abstract and descriptive indexing, not its complete manuscript; an implicit prior equivalent computation there or elsewhere remains a residual literature risk. The checker is not a substitute for independent validation.

## References
1. M. R. Pilla, *Cesàro-Type Operators Acting on the Drury-Arveson Space*, arXiv:2606.24710, first posted June 23, 2026; especially Definition 2.3 and Section 3.
2. M. R. Pilla, *Rhaly-Type Operators in Several Complex Variables*, arXiv:2606.25885, first posted June 24, 2026; abstract and indexed description consulted.
3. W. Arveson, *Subalgebras of C*-algebras III: Multivariable operator theory*, Acta Mathematica 181 (1998), 159–228; background for the distinct theory of coordinate-multiplier commutators.
