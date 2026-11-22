# A sharp third-cumulant sign threshold in triangular-book random-cluster gases

## Finding

Let a *triangular book* \(B_m\) consist of two hub vertices joined by a spine edge and \(m\ge3\) other vertices, each joined to both hubs. Assign the Fortuin–Kasteleyn (FK) bond weight \(q^{k(\omega)}v^{|\omega|}\) to each open-edge set \(\omega\), with real \(q>1\) and \(v>0\), including isolated vertices in the component count \(k(\omega)\). Denote by \(Y_i\) the indicator that *both* hub-to-page edges in page \(i\) are open; the spine is **not** part of this event.

Set
\[
A=q+2v,\quad B=A+v^2,\quad p=\frac{v^2}{B},\quad
\theta=\frac{(1+v)B^m}{(q-1)A^m+(1+v)B^m}.
\]
Then the full joint law of the \(m\) indicators is
\[
(Y_1,\ldots,Y_m)\ \stackrel{d}{=}\ Z(X_1,\ldots,X_m),
\]
where \(Z\) is Bernoulli\((\theta)\) and the \(X_i\) are independent Bernoulli\((p)\), independent of \(Z\). Thus for three distinct pages
\[
\boxed{\kappa(Y_i,Y_j,Y_k)=\theta(1-\theta)(1-2\theta)p^3}
\]
and for two distinct pages \(\operatorname{Cov}(Y_i,Y_j)=\theta(1-\theta)p^2>0\).

There is a sharp *cluster-weight boundary*: for \(1<q\le2\), the third connected correlation is strictly negative at all positive activities. For each \(q>2\) and \(m\ge3\), it is positive at small activity, vanishes at exactly one positive \(v_m\), and is negative above it. Its unique zero is specified by
\[
\boxed{(q-1)(q+2v_m)^m=(1+v_m)(q+2v_m+v_m^2)^m}.
\]
In a large triangular book,
\[
\sqrt m\,v_m\longrightarrow\sqrt{q\log(q-1)}.
\]
More precisely, for fixed \(a>0\), if \(v=a/\sqrt m\), put \(\Theta(a)=[1+(q-1)e^{-a^2/q}]^{-1}\). Then
\[
\lim_{m\to\infty}m^3\kappa(Y_i,Y_j,Y_k)
=\frac{a^6}{q^3}\Theta(a)(1-\Theta(a))(1-2\Theta(a)).
\]
The total number of fully open page bridges converges to a Bernoulli–Poisson mixture: it is zero when a Bernoulli\((\Theta(a))\) variable is zero, and otherwise follows Poisson\((a^2/q)\).

## Assumptions and scope

All \(m\) page vertices and the two hubs are labeled; the graph contains \(2m+1\) edges. Edge activities are identical and strictly positive, cluster weight \(q>1\) is any real number, and three page indices are distinct. The covariance and third cumulant refer to simultaneous equilibrium FK bond-occupation indicators, not sequential deposition, three-site spin correlation, or a thermodynamic singularity. The limiting \(m\to\infty\) statements keep \(q\) and \(a\) fixed and do not claim uniformity in these parameters. At \(q=1\), all bonds are independent and distinct-page cumulants vanish; that excluded limiting case is not a sign transition.

## Proof

**Exact partition.** Remove the spine temporarily and let a page have no occupied spoke, precisely one occupied spoke, or both occupied; their local bond sums are \(q\), \(2v\), and \(v^2\), respectively. If the hubs are disconnected, no page can contain both occupied spokes; the complete bond sum is \(q^2 A^m\). If the hubs are connected without the spine, at least one page is doubly occupied, giving \(q(B^m-A^m)\). When the spine is occupied, its activity contributes \(v\) and the connected-hub weight is \(qvB^m\). Hence
\[
Z_{B_m}(q,v)=q[(q-1)A^m+(1+v)B^m].
\]
These are disjoint exhaustive cases, including all isolated pages.

**Complete bridge-vector law.** For any specific binary pattern \(y\in\{0,1\}^m\) with \(r\ge1\) ones, there is at least one open two-spoke bridge, so the hubs are connected. Summing all other page states and the optional spine yields unnormalized mass \(q(1+v)v^{2r}A^{m-r}\). For the all-zero pattern the mass is \(q(q+v)A^m\). Divide by the partition function. Comparing these two cases with the mixture of an all-zero atom and \(m\) independent Bernoulli variables proves the distributional identity, since \(p=v^2/B\) and \(1-p=A/B\).

**Second- and third-order connected correlations.** For \(r\ge1\) distinct pages, the expectation of the product of their indicators is \(\theta p^r\). The second connected moment is \(\theta p^2-(\theta p)^2=\theta(1-\theta)p^2\). The third joint cumulant is \(\theta p^3-3\theta^2p^3+2\theta^3p^3=\theta(1-\theta)(1-2\theta)p^3\). Because \(q>1\) and \(v>0\), \(0<\theta<1\) and \(p>0\), so these signs are exact.

**Unique threshold and boundary.** Define
\[
R_m(v)=\frac{1-\theta}{\theta}=\frac{q-1}{1+v}\left(\frac{q+2v}{q+2v+v^2}\right)^m.
\]
The factor \((1+v)^{-1}\) and the ratio \((q+2v)/(q+2v+v^2)\) are strictly decreasing in \(v>0\), so \(R_m\) is continuous and strictly decreasing from \(q-1\) to zero. The third cumulant has the sign of \(1-2\theta\), which is the sign of \(R_m(v)-1\). If \(1<q\le2\) this sign is strictly negative. If \(q>2\), it changes exactly once from positive to negative at \(R_m(v_m)=1\), giving the asserted equation.

**Critical scaling and distribution.** For fixed \(a>0\) with \(v=a/\sqrt m\),
\[
m\log\frac{q+2v}{q+2v+v^2}\longrightarrow-\frac{a^2}{q},
\quad mp\longrightarrow\frac{a^2}{q}.
\]
Thus \(R_m(v)\to(q-1)e^{-a^2/q}\), and the displayed limit of the third cumulant follows. To locate the root, fix any \(a\) below and any \(b\) above \(\sqrt{q\log(q-1)}\): the limiting odds lie on opposite sides of one. Strict monotonicity traps \(v_m\) between \(a/\sqrt m\) and \(b/\sqrt m\) for all sufficiently large \(m\), proving the stated limit. Finally the exact mixture has a Binomial\((m,p)\) component with \(mp\to a^2/q\) and \(p\to0\); the binomial-to-Poisson limit proves the final distributional statement.

## Verification

A standalone Python file `verify.py` implements exhaustive exact-fraction FK enumeration for triangular books with \(m=3,4,5\), testing cluster weights \(q=3/2,2,3,4\) and activities \(v=1/5,3/4,2\). It independently compares all one-, two- and three-page moments to the proposed mixture, as well as the predicted covariance, cumulant and sign. Six additional large-book numerical spot-checks confirm the critical-window sign. Running `python3 verify.py` yielded `FK_BOOK_EXACT_CHECKS_PASSED 258`. The all-size statements follow from the proof above, not from finite enumeration.

## Relationship to prior work

Grimmett's 2002 random-cluster survey explains the FK partition convention and its connection to Potts models, but does not state a triangular-book third-cumulant boundary. A relevant later result, *Finite-core Fortuin–Kasteleyn reduction and mixed-Gaussian cluster fluctuations* (2026), proves an exact general fixed-hub FK reduction on \(K_{r,n}\), and asymptotic Poisson bridge counts on \(K_{2,n}\). It is therefore strong prior coverage for the **underlying mechanism** and the sparse Poisson limit. It does **not** give the present finite-activity, all-size signed third-cumulant formula, the special \(q=2\) boundary, or the unique finite-size reversal on a triangular book with an occupied or vacant spine. The Poisson-mixture corollary here is not separately claimed as novel. Exact Tutte polynomial specializations can recover the partition formula; the sign theorem and its unique zero require an additional connected-moment comparison. Searches found no directly equivalent statement but do not establish global novelty.

## Limitations

The theorem is for exactly two hubs, identical activity on every bond, and three distinct double-page events. It does not classify higher cumulant signs, heterogeneous edge weights, or growing cluster weight, and does not claim a thermodynamic phase transition. The finite-core FK theorem gives broad mechanistic prior art, so independent specialist comparison may identify an unnoticed corollary or earlier equivalent finite-volume statement. An exhaustive literature search is not asserted.

## References

[1] G. Grimmett, “The Random-Cluster Model,” first publicly posted 2002-05-23, arXiv:math/0205237v1. https://arxiv.org/abs/math/0205237

[2] “Finite-core Fortuin–Kasteleyn reduction and mixed-Gaussian cluster fluctuations,” public research finding (2026), full proof available at https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-finite-core-fortuin-kasteleyn-reduction-and-mixed-gaussian-clust--a9cbf9d149be/RESULT.md
