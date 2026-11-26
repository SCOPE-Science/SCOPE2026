# A unique worst fractional-heat exponent on strongly regular graphs

## Finding

Let \(G\) be a finite, undirected, simple, connected, noncomplete, unweighted strongly regular graph, and let \(L\) be its combinatorial Laplacian. Write \(0<a<b\) for the two distinct positive eigenvalues of \(L\). For each real \(\alpha>1\), let \(T_G(\alpha)>0\) be the sharp positive-time entrywise-nonnegativity threshold of \(\exp(-tL^\alpha)\): the nonnegative times are \(\{0\}\cup[T_G(\alpha),\infty)\).

**The threshold \(T_G(\alpha)\) has a unique global maximizer over \(\alpha>1\).** Set
\[
q=b/a,\qquad c=\log\frac{q}{q-1},\qquad
\delta=\frac{\log a}{\log q}>0,\qquad
h(z)=-\log(qe^{-z}-q+1)\quad(0<z<c).
\]
There is precisely one \(z_*\in(0,c)\) satisfying \(z_*h'(z_*)/h(z_*)=1+1/\delta\). The maximizing exponent and delay are
\[
\boxed{\alpha_G^*=\frac{\log(h(z_*)/z_*)}{\log q},\qquad
T_G(\alpha_G^*)=\frac{z_*^{1+\delta}}{h(z_*)^\delta}.}
\]
The delay is strictly increasing before \(\alpha_G^*\) and strictly decreasing afterwards. This optimization is over the unrescaled physical-time delays of the specified combinatorial Laplacian, not over delays after dividing out one decay rate.

## Setup and known threshold

Use spectral functional calculus with \(0^\alpha=0\) and entrywise order in the vertex basis. The graph is held fixed when varying \(\alpha\). The sharp positivity law, transient norm and its endpoint regimes on this graph class are given in [1]; they are background here. We recall the threshold argument to make the optimizer proof self-contained.

Writing \(N\) for the vertex count and \(P_0=J/N\), the nonconstant projectors satisfy \(P_a+P_b=I-P_0\) and \(aP_a+bP_b=L\). Thus a nonedge entry equals
\[
K_0(t)=\frac1N\left[1-\frac{be^{-a^\alpha t}-ae^{-b^\alpha t}}{b-a}\right].
\]
An edge entry equals \((1-e^{-b^\alpha t})/N+ (N-b)(e^{-a^\alpha t}-e^{-b^\alpha t})/[N(b-a)]>0\) for \(t>0\), since \(NI-J-L\) is the positive-semidefinite complement Laplacian. Every diagonal is positive by the projector formula. The ratio \((1-e^{-b^\alpha t})/(1-e^{-a^\alpha t})\) decreases strictly from \(q^\alpha\) to 1, because its logarithmic derivative is \([y/(e^y-1)]_{y=b^\alpha t}/t-[y/(e^y-1)]_{y=a^\alpha t}/t<0\). Therefore the positive threshold is the unique time when the ratio is \(q\), and it exists precisely for \(\alpha>1\). For \(0<\alpha\le1\) all entries are positive at every positive time; at zero the matrix is the identity.

The inequality \(a>1\) used below follows from the graph hypotheses. If \(k\) is the degree and \(\lambda,\mu\) the usual adjacent and nonadjacent common-neighbor counts, then \(\lambda\le k-2\) (otherwise adjacent vertices have identical closed neighborhoods, forcing completeness by connectivity), and \(1\le\mu\le k\). The nonprincipal adjacency eigenvalues are the roots \(r>s\) of \(f(u)=u^2-(\lambda-\mu)u-(k-\mu)\); the smaller root is nonpositive. Since \(k\ge2\) and \(f(k-1)\ge\mu k-1>0\), we have \(r<k-1\), hence \(a=k-r>1\).

## Proof of the optimizer

Set \(z=a^\alpha T_G(\alpha)\). The threshold equation reads \(e^{-q^\alpha z}=qe^{-z}-q+1\), forcing \(0<z<c\) and giving \(q^\alpha=h(z)/z\). The function \(h\) has \(h(0)=0\), \(h'(0)=q\), and strictly positive second derivative. It diverges at \(c\), so \(h(z)/z\) strictly increases from \(q\) to infinity. Consequently \(z\) parameterizes all of \(\alpha>1\) in increasing order, and \(a^\alpha=(h(z)/z)^\delta\) gives
\[
T_G(\alpha(z))=\frac{z^{1+\delta}}{h(z)^\delta}.
\]

Write \(f_1(z)=h'(z)=q/[q-(q-1)e^z]\). Its logarithmic derivative \((q-1)e^z/[q-(q-1)e^z]\) is positive and strictly increasing. For every fixed \(0\le u<1\), the logarithmic derivative (in \(z\)) of \(f_1(uz)/f_1(z)\) equals \(u(\log f_1)'(uz)-(\log f_1)'(z)<0\). Hence
\[
\frac{h(z)}{zh'(z)}=\int_0^1\frac{f_1(uz)}{f_1(z)}\,du
\]
strictly decreases. Its limits are 1 at zero and 0 at \(c\); the latter follows since the integrand, bounded by 1, tends to zero at each \(u<1\). Thus \(zh'(z)/h(z)\) is strictly increasing from 1 to infinity. The logarithmic derivative of the delay with respect to \(z\), multiplied by \(z\), is \(1+\delta-\delta zh'(z)/h(z)\); it changes sign from positive to negative exactly once. The delay tends to zero at both endpoints since it is asymptotic to \(q^{-\delta}z\) as \(z\downarrow 0\) and the denominator diverges as \(z\uparrow c\). This proves the formula, strict monotonicity on either side, and global uniqueness.

## Verification and background checks

For the Petersen graph, \(a=2,b=5\), yielding \(\alpha_G^*=1.636435234508\ldots\) and \(T_G(\alpha_G^*)=0.131791058820\ldots\). To reproduce directly, solve \(F(T,\alpha)=\partial_\alpha F(T,\alpha)=0\) near \((0.13,1.64)\), where \(F=b\operatorname{expm1}(-a^\alpha T)-a\operatorname{expm1}(-b^\alpha T)\), or bisect the strictly monotone scalar elasticity equation. The companion `checker.py` (Python 3, NumPy, SciPy and NetworkX) also checks this optimizer and finite parameter grids and matrix comparisons. The grid checks are not a proof of uniqueness.

For clarity about those checks, let \(d=N-k-1\). The earlier sharp counting-measure \(\ell^1\) and \(\ell^\infty\) norm is \(1+2d[-K_0(t)]_+\), since the row sum is one and only nonedge entries can be negative. The time of its peak for \(\alpha>1\) is \((\alpha-1)\log q/(b^\alpha-a^\alpha)\), from \(K_0'(t)=0\). Near \(\alpha=1+\varepsilon\), \(K_0(t)=-ab\log(q)\varepsilon t/[N(b-a)]+ab t^2/(2N)+O_G(\varepsilon^2t+\varepsilon t^2+t^3)\). This gives the positive threshold \(2\log(q)\varepsilon/(b-a)+O_G(\varepsilon^2)\) by dividing by \(t\) and solving near zero, and the peak norm \(1+dab(\log q)^2\varepsilon^2/[N(b-a)^2]+O_G(\varepsilon^3)\) by substitution of the peak time. As \(\alpha\to\infty\), \(a^\alpha T_G(\alpha)\to c\); at the peak the products of its time with \(a^\alpha\) and \(b^\alpha\) tend to zero and infinity, respectively, giving the known limiting peak norm \(1+2da/[N(b-a)]\). None of these per-exponent or limiting norm results is claimed here as a new contribution.

## Relationship to prior work and limitations

The all-strongly-regular threshold, norm, peak time, and asymptotic regimes have exact counterparts in [1]. The complete-multipartite analysis [2] already covers these kinds of quantities for a related class including the balanced imprimitive strongly regular cases. The distinct claim here is uniqueness of the worst exponent and its scalar characterization; the per-exponent equation alone does not give uniqueness without the monotonicity argument. Mixed heat [3] has a different objective: for a fixed mixed coupling, matching its two positive decay rates to fractional ones uses a coupling-dependent common time factor, so an optimizer does not transfer under the match. General eventual-positivity criteria [4] do not optimize fractional order.

This theorem is for the unweighted combinatorial Laplacian on the stated fixed strongly regular graph class; it makes no claim for general graphs, normalized generators or arbitrary spectral filters. Numerical checks are illustrative. The comparison does not establish historical priority or within-day ordering of distinct records.

## References

1. *Sharp positivity recovery for fractional heat on all connected strongly regular graphs*, 2026-11-22, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-positivity-recovery-for-fractional-heat-on-all-connected-s--d37f7dd78e94/RESULT.md).
2. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, 2026-10-26, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1/RESULT.md).
3. *A unique worst positivity delay for mixed heat on every strongly regular graph*, 2026-11-22, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-unique-worst-positivity-delay-for-mixed-heat-on-every-strongly--3c42bf2de9e9/RESULT.md).
4. D. Daners, J. Glück, and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, [arXiv:1511.05294](https://arxiv.org/abs/1511.05294).
