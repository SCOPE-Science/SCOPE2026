# Degree-independent exact FA-1f spectral gap on finite stars

## Finding
For every integer \(n\ge 2\) and every vacancy probability \(0<q<1\), the continuous-time one-spin-facilitated Fredrickson–Andersen (FA-1f) heat-bath chain on the star \(K_{1,n}\), restricted to configurations with at least one vacancy, has spectral gap
\[
\operatorname{gap}(-\mathcal L_{K_{1,n}})=1-\sqrt{1-q}.
\]
The gap has multiplicity exactly \(n-1\). In particular, the inverse relaxation rate is independent of the number of leaves, and at high occupancy the gap is \(q/2+O(q^2)\). On the exceptional one-leaf star \(K_{1,1}\), the gap is instead \(q\). Here spectral gap means the smallest strictly positive eigenvalue of the negative generator acting on the unique nontrivial irreducible component; it is not an assertion about total-variation mixing from worst-case configurations.

## Assumptions and scope
Let the hub be vertex \(0\), with leaves \(1,\ldots,n\). Each occupation variable \(\eta_v\) is either \(0\) (vacant) or \(1\) (filled). Independently at rate one, vertex \(v\) attempts to refresh its occupation from Bernoulli\((1-q)\); the refresh occurs only if \(v\) has at least one vacant neighbor. Thus a facilitated filled site becomes vacant at rate \(q\), and a facilitated vacant site becomes filled at rate \(p=1-q\). The fully filled state is isolated and excluded. The remaining \(2^{n+1}-1\) configurations form one irreducible reversible class, with measure the Bernoulli\((p)\) product measure conditioned on this class.

Write \(h=0\) for a vacant hub, \(h=1\) for a filled hub, and let \(\xi=(\eta_1,\ldots,\eta_n)\). Write \(\xi_\star=(1,\ldots,1)\). All leaf configurations occur when \(h=0\), but \(\xi_\star\) is forbidden when \(h=1\). Let \(H_{\rm leaf}\) be the negative generator of \(n\) independent rate-one Bernoulli\((p)\) heat-bath refreshes, acting on the complete leaf cube.

## Proof
**Irreducibility and reversible measure.** A configuration with filled hub and a vacant leaf can make the hub vacant; from a vacant hub, each leaf is freely refreshable, so all states of the form \((0,\xi)\) communicate. From these, configurations \((1,\xi)\) with \(\xi\ne\xi_\star\) are accessible. Detailed balance follows because each allowed flip has the Bernoulli heat-bath ratio; the all-filled state has no allowed edges.

**A lower bound for every nonzero eigenvalue.** Write an eigenfunction of the negative generator as \(f=(g(\xi),b(\xi))\), with \(b\) defined only for \(\xi\ne\xi_\star\). Put \(\lambda_*=1-\sqrt{1-q}\), noting \(0<\lambda_*<q\). Suppose \(0<\lambda<\lambda_*\) were an eigenvalue. On the filled-hub states, the equation is
\[
q\bigl(b(\xi)-g(\xi)\bigr)=\lambda b(\xi),\qquad
b(\xi)=\frac{q}{q-\lambda}g(\xi),\quad \xi\ne\xi_\star.
\]
On the vacant-hub states, leaves refresh independently and the hub becomes filled at rate \(p\) whenever \(\xi\ne\xi_\star\). Hence
\[
H_{\rm leaf}g=\mu(\lambda)g\quad (\xi\ne\xi_\star),\qquad
H_{\rm leaf}g=\lambda g\quad (\xi=\xi_\star),
\]
where
\[
\mu(\lambda)=\frac{\lambda(1-\lambda)}{q-\lambda}.
\]
On \((0,\lambda_*)\), \(0<\lambda<\mu(\lambda)<1\): indeed the derivative of \(\mu\) is \(\big((q-\lambda)^2+q(1-q)\big)/(q-\lambda)^2>0\), \(\mu(0)=0\), and \(\mu(\lambda_*)=1\). Let \(P_\star\) be the orthogonal projection onto the coordinate \(\xi_\star\) in the leaf product-measure Hilbert space (multiplication by its indicator). The last two equations are equivalent to
\[
B_\lambda g=0,\qquad B_\lambda=H_{\rm leaf}-\mu(\lambda)I+\bigl(\mu(\lambda)-\lambda\bigr)P_\star.
\]
The independent-refresh operator \(H_{\rm leaf}\) is self-adjoint with spectrum \(0,1,\ldots,n\), with the eigenspace at zero consisting of constants, and all other eigenvalues at least one. Because \(\mu-\lambda>0\), the rank-one last term in \(B_\lambda\) is positive semidefinite. The min–max principle therefore makes its second-smallest eigenvalue at least \(1-\mu>0\). On the other hand, for the constant test function \(\mathbf1\),
\[
\langle\mathbf1,B_\lambda\mathbf1\rangle
=-\mu+(\mu-\lambda)p^n
=-\mu(1-p^n)-\lambda p^n<0.
\]
Thus the smallest eigenvalue of \(B_\lambda\) is negative and all remaining eigenvalues are positive. In particular, \(B_\lambda\) has no zero eigenvalue, a contradiction. No eigenvalue lies in \((0,\lambda_*)\).

**Sharpness and multiplicity.** For distinct leaves \(i,j\), put \(g_{ij}(\xi)=\eta_i-\eta_j\). Independent heat-bath refresh gives \(H_{\rm leaf}g_{ij}=g_{ij}\) and \(g_{ij}(\xi_\star)=0\). Set
\[
f(0,\xi)=g_{ij}(\xi),\qquad
f(1,\xi)=\frac{q}{q-\lambda_*}g_{ij}(\xi)\quad (\xi\ne\xi_\star).
\]
The two eigen-equations above are then satisfied with \(\lambda=\lambda_*\). The \(n-1\) functions \(g_{1j}\), \(2\le j\le n\), are independent. At \(\lambda_*\), the eliminated operator is \(B_{\lambda_*}=H_{\rm leaf}-I+(1-\lambda_*)P_\star\). The spectrum of \(H_{\rm leaf}-I\) has exactly one negative eigenvalue and an \(n\)-dimensional zero eigenspace. Adding a positive rank-one operator leaves at least \(n-1\) zero eigenvalues. The constant test still gives a strictly negative Rayleigh quotient. To determine the nullspace exactly, let \(B_{\lambda_*}g=0\). Pairing the equation \((H_{\rm leaf}-I)g=-(1-\lambda_*)P_\star g\) with the leaf one-body eigenfunction \(w(\xi)=\sum_{i=1}^n(\eta_i-p)\), which satisfies \(H_{\rm leaf}w=w\) and \(w(\xi_\star)=nq\ne0\), forces \(g(\xi_\star)=0\). Hence \(H_{\rm leaf}g=g\), and the nullspace consists precisely of the mean-zero linear leaf functions vanishing at \(\xi_\star\), a space of dimension \(n-1\). Thus the gap multiplicity is exactly \(n-1\).

**One-leaf boundary.** When \(n=1\) the nontrivial component consists of three configurations forming a birth–death star; its negative-generator eigenvalues are \(0,q,2-q\), giving gap \(q\).

## Verification
The included standalone `verify.py` constructs every allowed generator edge from the stated heat-bath rule, checks reversibility and the explicit contrast eigenfunctions using exact fractions for \(2\le n\le9\) and three rational choices of \(\sqrt{1-q}\), and constructs symmetrized finite generators to compare spectral gaps for \(1\le n\le7\) at three non-rational-gap test values of \(q\). Its exact checks cover 61,254 directed transition-edge comparisons; all 21 finite spectral computations agree with the claimed formula, including the one-leaf exception. These finite checks are supplementary: the min–max and rank-one proof above establishes all integer orders and all real \(0<q<1\).

Run `python3 verify.py` (Python standard library for exact checks; NumPy and SciPy for the optional numerical spectra).

## Relationship to prior work
Fredrickson and Andersen introduced facilitated kinetic spin systems in 1984. Cancrini, Martinelli, Roberto and Toninelli studied spectral-gap scaling for kinetically constrained systems in their 2006 papers. Their 2007 lecture manuscript, Section 6, treats the FA-1f model on general connected graphs, including the same nonempty-vacancy component, and gives graph-uniform comparison bounds via the East model. Shapira (2020) establishes further general upper bounds and lattice estimates. The present result identifies an exact gap and its eigenspace for all finite stars, rather than merely bounding it. The broad theory and model definition are not claimed as new. Searches have not established definitive historical priority; an unindexed or differently phrased star-specific exact diagonalization may exist.

## Limitations
The formula uses unit-rate heat-bath resampling, not Metropolis flipping or a discrete-time clock. The proof concerns \(0<q<1\), the nontrivial component only, and the spectral gap, not the complete spectrum, worst-state total-variation mixing, or higher-order dynamical correlation functions. The all-filled configuration remains an isolated absorbing state in the unrestricted chain; therefore the unrestricted generator has a multiple zero eigenvalue and must not be confused with the stated restricted relaxation problem. Independent scientific auditing and comprehensive priority confirmation have not been undertaken.

## References
1. G. H. Fredrickson and H. C. Andersen, “Kinetic Ising Model of the Glass Transition,” *Physical Review Letters* 53 (1984), 1244, https://doi.org/10.1103/PhysRevLett.53.1244 (published 1984-09-24).
2. N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, “Relaxation times of kinetically constrained spin models with glassy dynamics,” arXiv:cond-mat/0603745 (first submitted 2006-03-28), https://arxiv.org/abs/cond-mat/0603745.
3. N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, “Kinetically constrained spin models,” arXiv:math/0610106 (first submitted 2006-10-03), https://arxiv.org/abs/math/0610106.
4. N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, “Facilitated spin models: recent and new results,” arXiv:0712.1934 (first submitted 2007-12-12), Section 6, https://arxiv.org/abs/0712.1934.
5. A. Shapira, “A Note on the Spectral Gap of the Fredrickson–Andersen One Spin Facilitated Model,” *Journal of Statistical Physics* 181 (2020), 2346–2352, https://doi.org/10.1007/s10955-020-02666-1.
