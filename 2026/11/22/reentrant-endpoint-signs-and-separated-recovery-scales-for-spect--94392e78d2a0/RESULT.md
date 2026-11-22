# Reentrant endpoint signs and separated recovery scales for spectral-power heat on a four-vertex path

## Finding
Let \(P_4\) be the unit-weight path with vertices \(1,2,3,4\), and let \(L\) be its unnormalized combinatorial Laplacian. Define \(K_\alpha(t)=\exp(-tL^\alpha)\) for all real \(\alpha>0\) and \(t\ge0\), using the nonnegative spectral functional calculus. Then:

1. For \(0<\alpha\le1\), every entry of \(K_\alpha(t)\) is strictly positive for every \(t>0\).
2. For every \(\alpha>1\), the distance-two entries \((K_\alpha(t))_{13}=(K_\alpha(t))_{24}\) are negative on one initial interval \((0,t_2(\alpha))\), vanish exactly at \(t_2(\alpha)\), and are positive thereafter. Every adjacent-vertex entry and every diagonal entry remains strictly positive at every \(t>0\).
3. For \(1<\alpha\le2\), the endpoint entry \((K_\alpha(t))_{14}\) is negative on precisely \((0,t_3(\alpha))\), vanishes at \(t_3(\alpha)\), and is positive thereafter. For every \(\alpha>2\), there are **exactly two** positive endpoint zeros \(0<t_-(\alpha)<t_+(\alpha)\): this entry is positive on \((0,t_-)\), negative on \((t_-,t_+)\), and positive on \((t_+,\infty)\). Thus increasing the spectral exponent through \(2\) changes immediate endpoint negativity into a bounded, strictly delayed negativity window, without eliminating the window.
4. Entrywise nonnegativity holds at \(t=0\) and for exactly one final time ray. For \(1<\alpha<2\), the final threshold is \(\max\{t_2(\alpha),t_3(\alpha)\}\). For \(\alpha=2\), it is \(t_3(2)\); for \(\alpha>2\), it is \(t_+(\alpha)\). In the latter range the strict ordering \(t_-<2^{-\alpha}\log2<t_2<2^{1-\alpha}<t_+\) holds.
5. There are sharply separated large-exponent scales. With \(a=2-\sqrt2\),
\[
\lim_{\alpha\to\infty}2^\alpha t_-(\alpha)=\tfrac12\log2,\quad
\lim_{\alpha\to\infty}2^\alpha t_2(\alpha)=-\log(1-1/\sqrt2),\quad
\lim_{\alpha\to\infty}a^\alpha t_+(\alpha)=\log(1+1/\sqrt2).
\]
In particular the initial endpoint positivity window is on the scale \(2^{-\alpha}\), whereas the final recovery occurs on the much longer scale \(a^{-\alpha}\).

All thresholds are the **unique roots in the specified intervals** of the explicit scalar functions below; no numerical root-certification assumption is needed.

## Assumptions and scope
The graph is precisely the simple four-vertex unit-conductance path, with no loops. Write
\[
L=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix},\quad
r=1-1/\sqrt2,\quad q=1+1/\sqrt2,\quad A=(2+\sqrt2)/8,\quad C=(2-\sqrt2)/8.
\]
Its eigenvalues are \(0\), \(a=2-\sqrt2\), \(2\), and \(b=2+\sqrt2\). Use scaled time \(\tau=2^\alpha t\), \(u=r^\alpha\), \(w=q^\alpha\), and abbreviations \(p=e^{-u\tau}\), \(m=e^{-\tau}\), \(h=e^{-w\tau}\). Then \(0<u<1<w\) and
\[
F_2(\tau,\alpha)=(K_\alpha(2^{-\alpha}\tau))_{13}=\tfrac14-\tfrac{\sqrt2}{8}p-\tfrac14m+\tfrac{\sqrt2}{8}h,
\]
\[
F_3(\tau,\alpha)=(K_\alpha(2^{-\alpha}\tau))_{14}=\tfrac14-Ap+\tfrac14m-Ch.
\]
Define \(t_2\) by the positive zero of \(F_2\); for \(1<\alpha\le2\), define \(t_3\) by the positive zero of \(F_3\). For \(\alpha>2\), \(t_-,t_+\) are its first and second positive zeros, all after dividing scaled zero locations by \(2^\alpha\). Equalities in item 4 include the zero matrix-entry boundaries, and do not assert strict entrywise positivity at those boundary times.

## Proof
**Spectral entries and positive classes.** Orthogonal diagonalization of the displayed \(L\) gives the two expressions above. The adjacent entries have the positive decompositions
\[
(K_\alpha)_{12}=\tfrac14(1-m)+\tfrac{\sqrt2}{8}(p-h)>0,
\]
\[
(K_\alpha)_{23}=\tfrac14(1-p)+\tfrac14(m-h)+\tfrac{\sqrt2}{8}(p-h)>0.
\]
Reflection gives the remaining adjacent entries. Every diagonal entry is at least \(1/4\), because the zero-eigenvalue projector equals the all-ones matrix divided by four and all other diagonal spectral projector entries are nonnegative. For \(0<\alpha<1\), the standard integral identity \(L^\alpha=c_\alpha\int_0^\infty(I-e^{-sL})s^{-1-\alpha}\,ds\), with \(c_\alpha>0\), shows that every off-diagonal entry of \(L^\alpha\) is strictly negative: \(e^{-sL}\) is strictly positive for \(s>0\) on a connected path. Thus \(-L^\alpha\) is an irreducible Metzler generator and \(e^{-tL^\alpha}\) has strictly positive entries for \(t>0\). The same conclusion holds for \(\alpha=1\).

**Distance-two entry.** Differentiation gives
\[
F_2'(\tau,\alpha)=\tfrac{\sqrt2}{8}u e^{-u\tau}+\tfrac14e^{-\tau}-\tfrac{\sqrt2}{8}w e^{-w\tau}.
\]
Multiplying by \(e^{w\tau}\) produces the strictly increasing function
\[
\tfrac{\sqrt2}{8}u e^{(w-u)\tau}+\tfrac14e^{(w-1)\tau}-\tfrac{\sqrt2}{8}w.
\]
Its value at zero is negative for every \(\alpha>1\), because \(q^\alpha-r^\alpha>q-r=\sqrt2\): the left side is strictly increasing in \(\alpha\). Hence \(F_2\) first decreases, then increases strictly, starts at zero, and tends to \(1/4\). There is exactly one positive zero and the asserted signs follow.

**Endpoint entry and the exponent-two transition.** Let \(H(\alpha)=Ar^\alpha+Cq^\alpha-1/4\). We have \(H(1)=H(2)=0\) by direct substitution and \(H''(\alpha)=Ar^\alpha(\log r)^2+Cq^\alpha(\log q)^2>0\). Consequently \(H(\alpha)<0\) for \(1<\alpha<2\) and \(H(\alpha)>0\) for \(\alpha>2\). Since \(F_3'(0,\alpha)=H(\alpha)\), the endpoint entry begins negative in the first range and positive in the second. At \(\alpha=2\), its first derivative vanishes and \(F_3''(0,2)=-H(4)<0\), so it begins negative as well.

For all \(\alpha>0\), multiply the derivative of \(F_3\) by \(e^\tau\):
\[
G_\alpha(\tau)=Au e^{(1-u)\tau}+Cw e^{-(w-1)\tau}-\tfrac14.
\]
This function is **strictly convex**, since \(G_\alpha''(\tau)>0\), and diverges to \(+\infty\). For \(1<\alpha<2\), it starts below zero, and for \(\alpha=2\), it starts at zero with strictly negative derivative (as \(F_3''(0,2)<0\)). In each case it has one positive zero; \(F_3\) decreases then increases, proving the unique endpoint crossing.

For \(\alpha>2\), the endpoint is initially positive. It is nevertheless negative at \(\tau=\log2\). Indeed \(u\le r^2\), \(w\ge q^2>5/2\), and \(2^{-u}>1-r^2\). Thus
\[
F_3(\log2,\alpha)<\tfrac38-A(1-r^2)=\frac{4-3\sqrt2}{16}<0.
\]
Since \(F_3(\tau,\alpha)\to1/4>0\) at infinity, it has at least two distinct positive zeros. By Rolle's theorem these force two positive zeros of the derivative; the strict convexity of \(G_\alpha\) permits no more. Therefore there are precisely two, and the sign intervals claimed in item 3 follow.

**Global positivity times and ordering.** For \(\alpha>2\), the distance-two entry is also negative at \(\tau=\log2\). The same elementary bounds, including \(2^{-w}<2^{-5/2}=1/(4\sqrt2)\), yield
\[
F_2(\log2,\alpha)<\frac{-3/4+\sqrt2/2}{8}<0.
\]
At \(\tau=2\), for all \(\alpha\ge2\),
\[
F_2(2,\alpha)>\tfrac14(1-e^{-2})-\tfrac{\sqrt2}{8}>0
\]
and
\[
F_3(2,\alpha)<\tfrac14(1+e^{-2})-A(1-2r^2)
=\tfrac14(1+e^{-2}-\sqrt2)<0.
\]
Here the strict inequalities follow from \(e^{-2}<1/4\), \(\sqrt2<3/2\), and \(\sqrt2>5/4\). Consequently the two entrywise-negative time intervals overlap, with the endpoint's last zero strictly after the distance-two zero. The global nonnegative set is therefore exactly \(\{0\}\cup[t_+,\infty)\) for \(\alpha>2\), and exactly \(\{0\}\cup[t_3(2),\infty)\) at \(\alpha=2\). For \(1<\alpha<2\), both nonedge classes are initially negative and each has one crossing, giving the maximum of their two thresholds.

**Large-exponent scales.** On every compact positive scaled-time interval, \(r^\alpha\to0\) and \(q^\alpha\to\infty\), so
\[
F_3(\tau,\alpha)\to\tfrac14e^{-\tau}-\tfrac{\sqrt2}{8},\qquad
F_2(\tau,\alpha)\to\tfrac14(1-e^{-\tau})-\tfrac{\sqrt2}{8}.
\]
Both limiting functions have one simple positive zero, respectively \((\log2)/2\) and \(-\log(1-1/\sqrt2)\). The just-proved exact zero counts, signs, and ordering force the first endpoint zero and the distance-two zero to converge to them in the \(\tau\) scale. For the late endpoint zero use \(\sigma=r^\alpha\tau=a^\alpha t\). For fixed \(\sigma>0\), the two faster terms vanish and
\[
F_3(\sigma/r^\alpha,\alpha)\longrightarrow\tfrac14-Ae^{-\sigma}.
\]
Its unique simple zero is \(\log(4A)=\log(1+1/\sqrt2)\). Choosing bracketing points on either side of the three simple zeros and applying the proved zero counts yields all three limits without assuming uniform approximation near the singular origin.

## Verification
Run `python checker.py` with NumPy and SciPy. It independently diagonalizes the original four-by-four Laplacian, compares the derived entries against the matrix exponential at multiple exponents/times, checks positivity of adjacent and diagonal entries, numerically brackets the predicted zeros, and checks the separated scaling limits. The checker returned `PASS: 1574 direct spectral, sign, root, and scale comparisons`. No finite grid establishes the sign classification for all \(\alpha\) or \(t\); those quantifiers follow from the derivative and convexity arguments above. The proof uses no computer-generated certificate.

## Relationship to prior work
Riascos and Mateos (2014) introduce spectral fractional graph Laplacians and analyze stochastic diffusion for \(0<\alpha<1\), including rings and mean return times, rather than the superunit-power sign diagram for this path. Daners, Glück and Kennedy (2015) give general eventual-positivity criteria, including finite-dimensional matrix semigroups, but not the exact endpoint sign phases or the two separated large-exponent scales. The published complete-multipartite fractional-heat formula handles a different graph family with only three distinct Laplacian eigenvalues, and does not imply this four-eigenvalue path's delayed loss of positivity. Earlier mixed-heat path results concern the distinct generator \(L+\eta L^2\); a small-superunit-power fixed-graph theorem concerns only exponents sufficiently near one, not the regime \(\alpha>2\). The proof here derives the all-positive-exponent classification directly from exact spectral entries.

## Limitations
The claim is for the unweighted four-vertex path only, the combinatorial Laplacian, and real positive powers. It makes no classification of other weighted paths, arbitrary four-vertex graphs, or negative/complex spectral exponents. Numerical verification is not an infinite proof and cannot establish historical priority. Unindexed equivalent calculations and other graph classes remain a residual priority risk. No assertion of a novel general theorem beyond this natural smallest four-eigenvalue path case is made.

## References
1. A. P. Riascos and J. L. Mateos, "Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights," *Physical Review E* **90**, 032809 (17 September 2014), DOI 10.1103/PhysRevE.90.032809; accessible manuscript arXiv:1506.06167 (19 June 2015), especially pp. 2–6.
2. D. Daners, J. Glück and J. B. Kennedy, "Eventually and asymptotically positive semigroups on Banach lattices," arXiv:1511.05294 (17 November 2015), especially Sections 1 and 9.
3. D. Daners, J. Glück and J. B. Kennedy, "Eventually Positive Semigroups of Linear Operators," arXiv:1511.09020 (29 November 2015), especially Section 6.1.
4. "A sharp positivity transition for fractional graph heat on complete multipartite networks," published published-finding corpus mathematical finding, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1 (RESULT.md inspected for mathematical implication comparison).
