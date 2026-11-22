# Continuous spectral-order allocation on rectangular rook networks

## Finding
Let \(2\le m\le n\) be integers and \(G=K_m\square K_n\). With a unit total conductance budget over independently adjustable nonnegative edges, the unique minimizer of
\[
\Phi_p(L)=\sum_{j=2}^{mn}\lambda_j(L)^{-p}\quad(p>0),
\]
and of \(\Phi_0(L)=-\sum_{j=2}^{mn}\log\lambda_j(L)\), has one positive edge conductance \(x\) in every \(K_m\) coordinate direction and one positive conductance \(y\) in every \(K_n\) direction. Disconnected assignments have objective \(+\infty\).

Write \(a=mx\), \(b=ny\), \(q=a/b\), and \(s=p+1\). For every real \(p\ge0\), \(q\) is the unique root in \((0,1]\) of
\[
mq^{-s}+(n-m)(1+q)^{-s}=n.
\]
The unique optimal weights are
\[
b=\frac{2}{n(m-1)q+m(n-1)},\qquad a=qb,\qquad x=\frac{a}{m},\qquad y=\frac{b}{n}.
\]
For equal factors \(m=n\), one has \(q=1\). For every strictly rectangular factor pair \(m<n\), \(0<q<1\). At the determinant endpoint \(p=0\), the exact solution is \(q=\sqrt{m/n}\).

For each fixed integer \(m\ge2\) and each fixed real \(p\ge0\), as \(n\to\infty\),
\[
q\sim\left(\frac{m}{(p+1)n}\right)^{1/(p+2)},\qquad
\frac{x}{y}\sim \frac{n^{(p+1)/(p+2)}}{m^{(p+1)/(p+2)}(p+1)^{1/(p+2)}}.
\]
If \(\theta_m\) denotes the budget fraction spent on \(K_m\)-direction edges, then
\[
\theta_m\sim\frac{m-1}{m}\left(\frac{m}{(p+1)n}\right)^{1/(p+2)}\longrightarrow0.
\]
Thus an asymptotically vanishing *aggregate* budget share coexists with an unbounded *per-edge* conductance ratio \(x/y\), whose exponent moves continuously from \(1/2\) at the determinant endpoint through \(2/3\) for inverse-trace coherence and \(3/4\) for squared-inverse-trace coherence.

There is also a sharp **logarithmic spectral-order crossover**. If the spectral order is permitted to vary with \(n\) so that \(p_n/\log n\to\alpha\in[0,\infty]\), then the *normalized Laplacian-rate ratio* has the exact limiting law
\[
\lim_{n\to\infty}q_{m,n,p_n}=\begin{cases}0,&\alpha=0,\\e^{-1/\alpha},&0<\alpha<\infty,\\1,&\alpha=\infty.\end{cases}
\]
Consequently the limits in network size and spectral order do not commute: \(\lim_{p\to\infty}\lim_{n\to\infty}q=0\) but \(\lim_{n\to\infty}\lim_{p\to\infty}q=1\).

## Assumptions and scope
The Cartesian product has vertices \((i,j)\) with \(1\le i\le m\), \(1\le j\le n\). Each edge changes exactly one coordinate, and each of the \(mn(m+n-2)/2\) edges is independently controllable. Budget is the unpriced sum of all conductances equal to \(1\). Eigenvalues are of the unnormalized weighted combinatorial Laplacian, and the sum excludes the single zero eigenvalue in connected cases. Both factor sizes are at least two, and the spectral order is any fixed finite real \(p\ge0\).

## Proof
**Global uniqueness and symmetry.** On the positive definite restriction of the Laplacian to the orthogonal complement of constants, the scalar functions \(t^{-p}\) for \(p>0\), and \(-\log t\) for \(p=0\), have strictly positive second derivatives. For any symmetric perturbation \(H\ne0\), the Hessian of \(\operatorname{tr}f(A)\) is a sum \(\sum_{i,j} f'^{[1]}(\lambda_i,\lambda_j)|H_{ij}|^2\) with strictly positive divided differences of \(f'\). Hence the objective is strictly convex in the weighted Laplacian. Distinct edge-conductance vectors produce distinct Laplacians by their off-diagonal entries. A connected feasible point exists; compactness of the budget simplex and blowup at disconnected limits give an optimal connected point. It is unique. The coordinate-permutation automorphism group acts transitively on edges of each of two classes; uniqueness forces the optimizer to be class-constant. Neither class can have zero weight, because that disconnects the Cartesian product. This establishes global optimality without assuming class symmetry initially.

**Spectrum and optimality equation.** The two complete-graph factor Laplacians have eigenvalues \(0,mx\) and \(0,ny\), with multiplicities \((1,m-1)\) and \((1,n-1)\), respectively. The nonzero product spectrum is therefore \(a\) with multiplicity \(m-1\), \(b\) with multiplicity \(n-1\), and \(a+b\) with multiplicity \((m-1)(n-1)\). The budget is
\[
\frac{n(m-1)}2a+\frac{m(n-1)}2b=1.
\]
For \(p>0\), the objective becomes
\[
(m-1)a^{-p}+(n-1)b^{-p}+(m-1)(n-1)(a+b)^{-p}.
\]
For \(p=0\) it is the negative logarithm of \(a^{m-1}b^{n-1}(a+b)^{(m-1)(n-1)}\). At every interior optimum the two cost-normalized marginal derivatives agree. Cancelling a common positive factor gives
\[
\frac{a^{-s}+(n-1)(a+b)^{-s}}{n}
=\frac{b^{-s}+(m-1)(a+b)^{-s}}{m},
\]
where \(s=p+1\) for all \(p\ge0\). Substitute \(q=a/b\) to obtain the displayed root equation. Its left side is continuous and strictly decreasing from infinity to a value below \(n\) as \(q\) runs from zero to one when \(n>m\); it equals \(n\) at \(q=1\) if \(n=m\). Hence there is exactly one root. The budget then determines \(a,b,x,y\) as stated. At \(p=0\), multiplying \(m/q+(n-m)/(1+q)=n\) by \(q(1+q)\) yields \(nq^2=m\).

**Large-rectangle scaling.** Fix \(m,p\), and set \(s=p+1\ge1\). Divide the root equation by \(n\). Every subsequential positive limit of \(q\) would require \((1+q)^{-s}=1\); thus \(q\to0\). For \(s>1\), the bound \(mq^{-s}\le n\) gives \(q\ge(m/n)^{1/s}\gg n^{-1}\). Therefore the root equation rearranges to
\[
\frac mn q^{-s}=1-\left(1-\frac mn\right)(1+q)^{-s}
=sq+o(q),
\]
so \(q^{s+1}\sim m/(sn)\). For \(s=1\), the exact determinant solution \(q=\sqrt{m/n}\) gives the same formula. Finally \(x/y=(n/m)q\), and the budget fraction is exactly \(\theta_m=n(m-1)q/[n(m-1)q+m(n-1)]\); the remaining asymptotics follow.

**Logarithmic crossover.** Let \(s_n=p_n+1\ge1\). For \(0<\alpha<\infty\), the exact bound \(q\ge(m/n)^{1/s_n}\to e^{-1/\alpha}>0\) keeps the ratio away from zero, while \((1+q)^{-s_n}\to0\). Divide the root equation by \(n\); its second term vanishes and its first tends to one, forcing \(q^{s_n}\sim m/n\) and hence \(q\to e^{-1/\alpha}\). For \(\alpha=\infty\), the same lower bound tends to one and \(q\le1\), giving \(q\to1\). For \(\alpha=0\), if \(q\ge\varepsilon>0\) on a subsequence, then the first term of the divided root equation is at most \((m/n)\varepsilon^{-s_n}=n^{-1+o(1)}\to0\), while the second is at most \((1+\varepsilon)^{-1}<1\), a contradiction. Thus \(q\to0\). The noncommutation follows by taking the two endpoint regimes in their respective sequential orders.

## Verification
The supplementary `verify.py` uses only the Python standard library. It independently assembles weighted Cartesian-product Laplacians and exactly compares their full rational inverse traces, inverse-square traces, and determinants with the three-eigenvalue formulas for several small rectangular networks. It also checks the finite-root condition, the exact determinant square-root identity, unit-budget normalization, and numerical convergence of the asymptotic constants. These finite checks do not constitute proof for infinite factor sizes or arbitrary real order; the analytic argument above supplies those quantifiers.

## Relationship to prior work
Ghosh, Boyd, and Saberi (2006/2008) established the general effective-resistance conductance optimization framework and global convexity; the inspected 2006 paper's exact worked family is a barbell, not a rectangular rook product. Bamieh, Jovanović, Mitra, and Patterson (2011) and Patterson and Bamieh (2013) study first- and second-order noisy-consensus spectral objectives, especially lattice/fractal scalings, without this exact two-factor conductance-allocation law. A published result on *priced complete prisms* covers the narrower special case \(m=2\), \(p=1\), unit relative edge prices, including its \(n^{2/3}\) ratio scale; that special case is not presented as new here. The present claim concerns the full continuous real spectral-order family, determinant endpoint, all rectangular product dimensions, the exact scalar equation, the continuously variable large-rectangle allocation exponent, and the logarithmic spectral-order crossover.

## Limitations
This result is for exactly two complete factors with uniform price per edge, and fixes \(m\) and \(p\) before sending \(n\) to infinity. The fixed-order power law is not asserted uniformly for spectral orders growing with \(n\); the separate joint-order crossover applies only in the stated logarithmic regime. Originality is assessed against the inspected accessible literature and returned research indexes; equivalent work outside those sources may exist. No independent mathematical audit has been performed.

## References
- A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS, Kyoto, July 24–28, 2006: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; expanded version SIAM Review 50 (2008), DOI:10.1137/050645452.
- B. Bamieh, M. R. Jovanović, P. Mitra, S. Patterson, *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback*, arXiv:1112.4011v1, December 17, 2011: https://arxiv.org/abs/1112.4011.
- S. Patterson, B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1, October 9, 2013: https://arxiv.org/abs/1310.2592.
- *Three allocation scales in priced complete prisms*, research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-allocation-scales-in-priced-complete-prisms--ab8d476367b2 (indexed abstract; primary full text inaccessible in this review).
