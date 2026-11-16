# Canonical near-crystal diffraction on cycles: a complete fixed-defect Fourier limit

## Finding

Let \(m\ge 1\) be a fixed integer, let \(k\to\infty\), and set \(n=2k+m\). Draw an independent set \(I\) of cardinality \(k\) uniformly from the cycle \(C_n\); let \(X_x=\mathbf 1_{\{x\in I\}}\), \(x\in\mathbb Z/n\mathbb Z\), and let \(K_n\) be the \(n\)-by-\(n\) covariance matrix of \(X\). Its Fourier eigenvalues are \(\Lambda_{n,j}\), \(0\le j<n\), with the convention that the discrete Fourier transform has no coefficient-normalizing factor. Define \(\epsilon_m=m\bmod2\), \(\omega_{m,r}=2\pi(r-\epsilon_m/2)\) for \(r\in\mathbb Z\), and \(j_{n,r}=\lfloor n/2\rfloor+r\).

**Theorem (fixed-defect Bragg profile).** For every fixed \(m\ge1\) and integer \(r\),
\[
\lim_{k\to\infty}\frac{\Lambda_{2k+m,j_{2k+m,r}}}{2k+m}
=B_m(\omega_{m,r}),\qquad
B_m(\omega)=\frac12\int_0^1(1-t)(1-2t)^m\cos(\omega t)\,dt.
\]
For fixed \(r\), the frequency index lies in \(\{0,\ldots,n-1\}\) for all sufficiently large \(n\). More strongly, extend \(\Lambda_{n,j_{n,r}}/n\) by zero outside that index range. The resulting sequence indexed by all integers \(r\) converges to \(\{B_m(\omega_{m,r})\}_r\) in \(\ell^1(\mathbb Z)\). In particular,
\[
B_m(\omega_{m,r})\ge0,\qquad \sum_{r\in\mathbb Z}B_m(\omega_{m,r})=\frac14,
\qquad B_m(\omega_{m,r})=\frac{m}{\omega_{m,r}^2}+O_m(|\omega_{m,r}|^{-4})
\]
as \(|r|\to\infty\). For even \(m\), the exact central limiting intensity is \(B_m(0)=1/[4(m+1)]\). The first two defect strata simplify to
\[
B_1((2r-1)\pi)=\frac{1}{(2r-1)^2\pi^2},
\quad B_2(2\pi r)=\begin{cases}1/12,&r=0,\\1/(2\pi^2r^2),&r\ne0.\end{cases}
\]
At every finite size \(n=2k+m\ge3\), the centered covariance \(K_n\) has rank exactly \(n-1\); its only null mode is the constant Fourier character. The complete finite spectrum is given by the binomial formula below.

## Assumptions and scope

The cycle is simple and labeled; for \(n=3\), it is the ordinary triangle. An independent set has no two adjacent occupied vertices, including across the cyclic seam. The distribution is **canonical**: its occupation count is deterministically \(k\), rather than governed by a fugacity. The gap defect \(m=n-2k\) stays fixed while the ring grows. The theorem covers each fixed positive defect count \(m\), with constants allowed to depend on \(m\); it does not assert uniformity when \(m\) increases with \(n\).

Set \(Q_d(t)=\binom{d-t-2}{t}\) when \(t\ge0\) and \(d-t-2\ge t\), and \(Q_d(t)=0\) otherwise. Let
\[
N_{n,k}=\frac{n}{k}\binom{n-k-1}{k-1},\quad p=\frac{k}{n},\quad
H_d=\sum_{t=0}^{k-2}Q_d(t)Q_{n-d}(k-2-t)\quad (1\le d<n).
\]
For \(k=1\), the sum defining \(H_d\) is empty and equals zero. With \(\theta_j=2\pi j/n\), an exact finite-size formula is
\[
\Lambda_{n,0}=0,\qquad
\Lambda_{n,j}=p+\frac1{N_{n,k}}\sum_{d=1}^{n-1}H_d\cos(d\theta_j)\quad(1\le j<n).
\]
Every value is real; the full spectrum is determined without a thermodynamic approximation.

## Proof

**1. Gap enumeration and finite covariance.** Mark one of the \(k\) occupied sites and traverse the ring from that site. Its successive positive cyclic gaps are uniquely \(2+a_1,\ldots,2+a_k\), where the \(a_i\) are nonnegative integers summing to \(m\). Every weak composition arises and all marked independent sets give equal weights to the corresponding compositions. Counting marked configurations in the two ways gives \(kN_{n,k}=n\binom{m+k-1}{k-1}\), which is the stated formula because \(m+k=n-k\). For two prescribed occupied vertices separated clockwise by \(d\), if exactly \(t\) occupied vertices lie strictly inside the clockwise arc, its \(t+1\) gaps, each at least two edges long, have \(Q_d(t)\) possibilities; the other arc contributes \(Q_{n-d}(k-2-t)\). Hence the number of sets containing both prescribed sites is \(H_d\). As all one-point means equal \(p\), the covariance row is \(p(1-p)\) at separation zero and \(H_d/N_{n,k}-p^2\) otherwise. Discrete Fourier diagonalization produces the stated formula. Its constant eigenvalue vanishes because \(\sum_xX_x=k\) deterministically.

**2. No other finite null mode.** If a real coefficient vector \(a\) satisfies \(\operatorname{Var}(\sum_x a_xX_x)=0\), then the sum has the same value for all admissible sets. For \(k\ge2\), compare \(\{0,3,5,\ldots,2k-1\}\) with \(\{1,3,5,\ldots,2k-1\}\); both are independent because \(n\ge2k+1\). This implies \(a_0=a_1\), and cyclic rotation implies equality of every adjacent pair. When \(k=1\), arbitrary singleton sets give the same conclusion. Thus only constant vectors have zero variance. As a real covariance matrix is positive semidefinite, its Fourier rank is \(n-1\).

**3. The continuum phase-slip process.** For a uniformly chosen marked set, \((a_1,\ldots,a_k)\) is a uniform weak composition of \(m\). The probability of any coordinate exceeding one is at most \(O_m(k^{-1})\): using the exact ratio of composition counts, the expected number of coordinates at least two is \(k m(m-1)/[(k+m-1)(k+m-2)]\). Conditional on all \(a_i\in\{0,1\}\), the \(m\) defect coordinates form a uniformly chosen \(m\)-subset of the \(k\) gap indices. Their rescaled locations converge jointly, as an unordered point cloud, to \(m\) independent uniform points \(U_1,\ldots,U_m\) in \([0,1]\). Let \(H_\ell=\sum_{i=1}^\ell a_i\) and let the occupied positions relative to the marked site be \(T_\ell=2\ell+H_\ell\), \(0\le\ell<k\).

Fix integer \(r\). The Fourier angle at \(j_{n,r}\) satisfies the **exact identity** \(\theta_{j_{n,r}}=\pi+\omega_{m,r}/n\), including the odd-\(n\) half-step. Thus
\[
\frac1n\sum_{\ell=0}^{k-1}e^{-i\theta_{j_{n,r}}T_\ell}
=\frac1n\sum_{\ell=0}^{k-1}(-1)^{H_\ell}e^{-2i\omega_{m,r}\ell/n}e^{-i\omega_{m,r}H_\ell/n}.
\]
Since \(0\le H_\ell\le m\), the last exponential tends uniformly to one. The marked-point defect convergence and Riemann sums give convergence in distribution of the displayed expression to
\[
\frac12\int_0^1\sigma_m(t)e^{-i\omega_{m,r}t}\,dt,
\qquad \sigma_m(t)=(-1)^{\sum_{i=1}^m\mathbf1_{\{U_i\le t\}}}.
\]
The expressions are uniformly bounded in modulus by \(k/n\le1/2\), so their squared moduli converge in expectation. The choice of marked origin only changes the original discrete Fourier amplitude by a unit phase, leaving its squared modulus unchanged. For every nonconstant frequency, translation invariance gives
\(\Lambda_{n,j}=n^{-1}\mathbb E|\sum_xX_x e^{-2\pi ijx/n}|^2\).
For \(0\le s\le t\le1\), independence of the \(m\) uniform defect points yields
\(\mathbb E[\sigma_m(s)\sigma_m(t)]=(1-2(t-s))^m\).
Integrating the two-point kernel over the unit square therefore gives the stated integral for \(B_m\). This proves each fixed-offset limit and positivity.

**4. Uniform Fourier-tail control and conservation of intensity.** Write \(Y_x=2X_x-1\), \(S_x=(-1)^xY_x\). Along the ring there are exactly \(m=n-2k\) adjacent vacant pairs (`00` bonds), because every occupied site accounts for two distinct occupied-vacant bonds and there are no `11` bonds. Therefore the modulated sign string \(S_x\) has at most \(m\) sign changes internally and one possible twisted-seam change. For a frequency \(j\ne0\), the constant component of \(X_x=(1+Y_x)/2\) has zero Fourier coefficient. Discrete summation by parts, applied to \(S_x\) at detuning \(\theta_j-\pi\), gives a deterministic amplitude bound \(\left|\sum_x X_xe^{-i\theta_jx}\right|\le C_m/|1-e^{-i(\theta_j-\pi)}|\) away from exact detuning zero, with a constant independent of \(n\). The trivial bound \(k\le n/2\) controls exact detuning zero. On the centered index window \(j=j_{n,r}\), this implies \(\Lambda_{n,j}/n\le C'_m/(1+|r|)^2\) uniformly in \(n\), with the two endpoint cases and the constant mode handled separately. Dominated convergence over the integer index \(r\) proves the stronger \(\ell^1\) limit.

Parseval gives \(\sum_{j=0}^{n-1}\Lambda_{n,j}=\operatorname{tr}K_n=np(1-p)\). Divide by \(n\), apply \(\ell^1\) convergence, and use \(p=k/n\to1/2\): the total limiting intensity is \(\sum_rB_m(\omega_{m,r})=1/4\).

**5. Endpoint constants.** For even \(m\), direct integration gives \(\int_0^1(1-t)(1-2t)^m\,dt=1/[2(m+1)]\), and thus \(B_m(0)=1/[4(m+1)]\). For nonzero \(\omega_{m,r}\), \(e^{i\omega_{m,r}}=(-1)^m\). Twice integrating the polynomial kernel against \(\cos(\omega t)\) shows
\[
\int_0^1(1-t)(1-2t)^m\cos(\omega t)\,dt
=\frac{2m}{\omega^2}+O_m(|\omega|^{-4}).
\]
The precise remainder follows from two more integrations by parts, since the integrand is a polynomial in \(t\), and the endpoint sine terms vanish. For \(m=1\) and \(m=2\), the lower-degree remainder vanishes identically at all nonzero allowed frequencies, giving the displayed closed forms.

## Verification

`verify_diffraction.py` is a standalone Python 3 standard-library checker. It compares the exact gap-count covariance formula to exhaustive enumeration of all canonical independent sets for every admissible \((n,k)\) with \(3\le n\le15\), verifies the one-dimensional covariance nullspace numerically over those sizes, tests explicit finite-size diffraction against the fixed-defect limits at two growing ring sizes, and checks nonnegativity of sampled limiting profiles. It reports 1,678 passing assertions. Its finite checks support the derivation but do not substitute for the infinite-dimensional \(\ell^1\) convergence proof above. Execute `python3 verify_diffraction.py` in the directory containing this file.

## Relationship to prior work

Davies and Perkins (arXiv:2102.04984, first submitted February 9, 2021) establish the importance of uniform sampling of independent sets with prescribed cardinality and examine approximate counting and sampling algorithms. Their main results concern computational thresholds, not fixed-defect harmonic observability. Bakhti, Müller and Maass (arXiv:1312.4142) analyze exact distributions and correlations for one-dimensional lattice hard rods through density-functionals and a Markov description; those general correlations and the hard-core gap encoding are background. Neither inspected source states an \(\ell^1\) near-Bragg Fourier intensity limit for the exact canonical cycle with fixed vacancy excess. The new contribution is the full parity-sensitive discrete harmonic limit, exact conserved intensity and explicit defect-stratum profiles, not the underlying independent-set counting identity or the general principle of renewal correlations.

A related previously recorded result treats fugacity-weighted length-three exclusion with a Poisson number of defects at cubic activity scaling. That is a different ensemble and exclusion distance: its conclusions do not imply the present fixed-number length-two telegraph limit or the \(\ell^1\) convergence theorem. More general lattice-gas structure-factor methods might recover some of the formulas after specialization; historical priority is not independently established.

## Limitations

The defect count remains fixed as the cycle size tends to infinity; no uniform bound for growing defect count is claimed. The theorem concerns the covariance spectrum, not recovery of an individual configuration from its intensity data. Fourier-tail asymptotics hold only along the parity-constrained detuning lattice. A complete historical-priority assertion is not made: an earlier diffraction or telegraph-process formula in different notation could subsume part of the result. Independent mathematical validation is not yet performed.

## References

- E. Davies and W. Perkins, *Approximately Counting Independent Sets of a Given Size in Bounded-Degree Graphs*, arXiv:2102.04984, version 1 publicly submitted February 9, 2021. https://arxiv.org/abs/2102.04984
- B. Bakhti, G. Müller and P. Maass, *Interacting Hard Rods on a Lattice: Distribution of Microstates and Density Functionals*, arXiv:1312.4142 (2013). https://arxiv.org/abs/1312.4142
