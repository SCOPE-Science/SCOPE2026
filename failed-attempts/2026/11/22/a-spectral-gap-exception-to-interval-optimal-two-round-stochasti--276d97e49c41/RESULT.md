# A spectral-gap exception to interval-optimal two-round stochastic consensus on bipartite chains

## Finding

**Theorem (Markov-positive two-round minimax law in the clustered-spectrum regime).** Let \(P\) be the transition matrix of a finite irreducible reversible Markov chain with at least three states, no holding transitions, and bipartite transition graph. Its eigenvalues in \(L^2(\pi)\) are real. Write \(s=\lambda_2(P)\) for its second-largest eigenvalue, and assume
\[
0<s<3-2\sqrt2.
\]
Consider **only** homogeneous-in-space, time-dependent laziness: in each of exactly two rounds choose
\[
P_\alpha=(1-\alpha)I+\alpha P,\qquad
P_\beta=(1-\beta)I+\beta P,
\qquad 0\le\alpha,\beta\le1.
\]
Every factor is a nonnegative stochastic kernel with stationary law \(\pi\). Minimize the centered \(L^2(\pi)\) operator norm of the two-round product over all such \((\alpha,\beta)\). Then
\[
\boxed{\{\alpha,\beta\}=\left\{1,\frac1{2-s}\right\}}
\]
is the **unique optimal unordered pair**, and the sharp two-round contraction is
\[
\boxed{R_2^*(P)=\frac{s}{2-s}}.
\]
The best repeated single-round stochastic kernel has parameter \(\alpha=\beta=2/(3-s)\) and larger two-round contraction \(((1+s)/(3-s))^2\). Their exact difference is
\[
\boxed{\left(\frac{1+s}{3-s}\right)^2-\frac{s}{2-s}
=\frac{2(1-s)^3}{(3-s)^2(2-s)}>0.}
\]

The **spectral-gap novelty** is that, precisely in the stated subthreshold regime, the above optimal contraction is also strictly smaller than the optimal two-step *stagewise-nonexpansive* Richardson factor designed robustly for every spectral value in the enclosing interval \([1-s,2]\):
\[
R_{\rm interval}=\frac{(1+s)^2}{s^2-14s+17},\qquad
\boxed{R_{\rm interval}-R_2^*(P)
=\frac{2(1-s)(s^2-6s+1)}{(2-s)(s^2-14s+17)}>0.}
\]
The earlier interval-based theorem covers the complementary high-\(s\) formula; the present result singles out an actual-spectrum exception rather than relabeling that covered case.

**Infinite natural example.** On the crown graph \(\mathrm{Cr}_m=K_{m,m}\setminus M\) with the simple random-walk transition matrix and integer \(m\ge7\), the eigenvalues are \(1,-1,1/(m-1),-1/(m-1)\), with the last two of multiplicity \(m-1\). Hence
\[
\{\alpha,\beta\}=\left\{1,\frac{m-1}{2m-3}\right\},\qquad
R_2^*=\frac1{2m-3},
\]
whereas the best repeated homogeneous step has two-round contraction \((m/(3m-4))^2\). In particular the optimally alternating contraction tends to zero while the repeated optimum tends to \(1/9\) as \(m\to\infty\).

## Assumptions and scope

An irreducible reversible chain has a unique positive stationary distribution \(\pi\), and \(P\) is self-adjoint in the inner product \(\langle x,y\rangle_\pi=\sum_i\pi_i x_i y_i\). The no-holding, bipartite assumption implies the exact spectral symmetry \(\lambda\leftrightarrow-\lambda\), with simple extremal eigenvalues \(1\) and \(-1\). Since the chain has at least three states, \(s\ge0\); the positive subthreshold hypothesis excludes the degenerate exact-two-round-consensus case already discussed in older polynomial-filter work. The objective is
\[
R_2(\alpha,\beta)=\left\|P_\beta P_\alpha-\mathbf1\pi^\top\right\|_{L^2(\pi)\to L^2(\pi)}
=\max_{\lambda\in\sigma(P)\setminus\{1\}}|(1-\alpha+\alpha\lambda)(1-\beta+\beta\lambda)|.
\]
The result does **not** optimize individually chosen graph edge probabilities, different row-dependent holding probabilities, nonreversible kernels, arbitrary two-step polynomial factors with negative entries, or a long-run asymptotic criterion beyond a precisely repeated two-round cycle.

## Proof

**1. Spectral enclosure from bipartiteness.** Writing \(D\) for the diagonal sign matrix of the bipartition gives \(DPD=-P\). Thus if \(\lambda\) is an eigenvalue, so is \(-\lambda\). The irreducible chain has a simple eigenvalue \(1\) and the corresponding simple \(-1\); all remaining eigenvalues belong to \([-s,s]\). As the two factors are affine in the same self-adjoint \(P\), their centered product norm is the scalar spectral maximum displayed above.

**2. The two necessary endpoint modes.** At \(\lambda=s\), each multiplier is positive, giving the endpoint quantity
\[
A(\alpha,\beta)=(1-(1-s)\alpha)(1-(1-s)\beta).
\]
At \(\lambda=-1\), the absolute product is \(B(\alpha,\beta)=|(1-2\alpha)(1-2\beta)|\). Therefore \(R_2\ge\max\{A,B\}\).

Any parameter below \(1/2\) can be increased to \(1/2\) without increasing either endpoint, since \(1-s>0\), and this strictly decreases \(A\) unless a distinct factor is already zero. In our positive-\(s\) regime every factor of \(A\) is at least \(s>0\), so the decrease is strict. Thus no endpoint minimizer lies outside \([1/2,1]^2\).

Put \(u=1-\alpha\), \(v=1-\beta\), \(U=u+v\), \(V=uv\). For \(u,v\in[0,1/2]\), both endpoint values are nonnegative and
\[
A=s^2+s(1-s)U+(1-s)^2V,\qquad
B=1-2U+4V.
\]
When \(U\le1/2\), dropping nonnegative multiples of \(V\) yields
\[
\max\{A,B\}\ge
\max\{s^2+s(1-s)U,1-2U\}.
\]
The first affine function is strictly increasing in \(U\), the second strictly decreasing, and their unique crossing occurs at
\[
U_* =\frac{1-s}{2-s}<\frac12,\qquad
\max\{A,B\}\ge\frac{s}{2-s}.
\]
Equality forces \(U=U_*\) and \(V=0\), whence \(\{u,v\}=\{0,U_*\}\), equivalently the stated unordered gains.

When \(U\ge1/2\), the lower bound \(A\ge s^2+s(1-s)/2\) exceeds \(s/(2-s)\) by \(s^2(1-s)/(2(2-s))>0\). Thus no omitted region supplies another minimizer. This proves a global endpoint lower bound and its rigid equality case for **all** admissible two-round gains.

**3. No hidden interior mode.** At the proposed gains the polynomial multiplier is
\[
f(\lambda)=\lambda\frac{\lambda+1-s}{2-s}.
\]
At \(\lambda=s\) and \(\lambda=-1\), it equals \(s/(2-s)\). For every remaining eigenvalue \(|\lambda|\le s\), we have \(|\lambda+1-s|\le1\), because \(0<s<1\). Hence
\[
|f(\lambda)|\le\frac{s}{2-s}.
\]
The endpoint lower bound is attained on the **entire actual spectrum**, proving global optimality and uniqueness without imposing any symmetry on the underlying graph other than reversible bipartiteness.

**4. Comparison designs and exact gap.** For a repeated gain \(\gamma\), the single-round worst nonconstant modulus is \(\max\{1-(1-s)\gamma,|1-2\gamma|\}\). Balancing these two endpoints gives its unique minimum at \(\gamma=2/(3-s)\); squaring yields the repeated two-round comparator. Subtracting \(s/(2-s)\) and factoring gives the displayed strictly positive difference.

For interval-robust stagewise safety, the established two-stage Richardson formula on \([\mu,L]=[1-s,2]\) has condition number \(\kappa=2/(1-s)\). Its Chebyshev-feasible branch applies exactly when \(0<s<3-2\sqrt2\), giving
\[
\frac{(\kappa-1)^2}{\kappa^2+6\kappa+1}
=\frac{(1+s)^2}{s^2-14s+17}.
\]
Direct subtraction yields the stated difference. The numerator \(s^2-6s+1\) is strictly positive precisely for \(0<s<3-2\sqrt2\) inside \((0,1)\). Thus the true symmetric spectral clusters permit a strict improvement even over the optimal interval-robust stagewise-safe polynomial. This fact is not implied by the prior interval theorem, which optimizes a different and stronger uncertainty requirement.

**5. Crown example.** The cross-part block of the crown random walk is \((J-I)/(m-1)\), with singular/eigenvalues \(1\) and \(-1/(m-1)\). The full bipartite block matrix therefore has eigenvalues \(\pm1\) and \(\pm1/(m-1)\). The condition \(1/(m-1)<3-2\sqrt2\) first holds for integer \(m=7\). Substitution into the universal result gives the displayed exact crown parameters, contraction and limiting comparison.

## Verification

Run `python verify.py` with Python 3 and no external packages. The script tests exact rational crown eigenvectors and spectra on a range of orders, evaluates the endpoint and inner spectral inequalities, checks closed-form gain identities and strict comparator inequalities in the subthreshold regime, and rejects a rational grid of competitor gains by the endpoint bound. The saved checker output was **PASS: 39756 exact finite assertions**. Those finite tests are not an exhaustive search over real parameters and are not used to justify the theorem for arbitrary graph order: the proof above establishes those quantifiers analytically.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) define the fastest-mixing Markov-chain SLEM and optimize a **single** stationary symmetric kernel over graph-edge probabilities; they do not give an exact optimum over a product of two separately stochastic laziness adjustments of a fixed reversible kernel. Apers and Sarlette (2015) derive second-order **unrestricted polynomial** consensus filters and explicitly discuss complete-bipartite two-step consensus; that pre-existing exact-consensus case is omitted from the new positive-\(s\) theorem. Their filters do not require every first-order factor to be stochastic. A published stagewise-safe Richardson frontier proves the best robust two-stage polynomial on **every value in the enclosing interval**; its high-condition-number branch already gives the same formula for \(s\ge3-2\sqrt2\), so this covered parameter range is expressly excluded from the claimed novelty. Its low-condition-number Chebyshev branch is not optimal for the separated actual spectrum addressed here. A published odd-cycle two-round theorem assumes odd order and does not cover bipartite chains. A published crown-graph fastest-mixing theorem determines the **single-step** optimal stochastic kernel (and its rigidity), but not the present time-inhomogeneous two-step optimum.

## Limitations

The optimal pair is unique only within the precisely specified two-gain family; no unrestricted graph-edge reweighting uniqueness is claimed. SLEM in weighted \(L^2(\pi)\) is not total-variation distance, although it controls related mixing estimates. The improvement over robust interval design exploits the actual bipartite spectral gap, not an arbitrary unknown spectrum in that full interval. The low-\(s\) domain is deliberate: outside it the same gain formula follows from stronger published interval-optimality results. Originality is relative to the inspected accessible sources, not a proof of publication priority; unindexed equivalent work may exist. No independent audit or floating-point error guarantee is asserted.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, first published electronically October 29, 2004. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Apers and A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269v1, first public March 4, 2015. https://arxiv.org/html/1503.01269v1
3. *Sharp stagewise-safe Richardson frontier and a no-acceleration barrier*, 2026, full theorem and proof. https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705/RESULT.md
4. *Sharp two-round stochastic consensus on odd cycles*, 2026, full theorem and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-two-round-stochastic-consensus-on-odd-cycles--b2b600a3fbfd/RESULT.md
5. *Rigidity and quantitative near-optimality for fastest mixing on crown graphs*, 2026, full theorem and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-rigidity-and-quantitative-near-optimality-for-fastest-mixing-on--5eef16ab8cf4/RESULT.md
