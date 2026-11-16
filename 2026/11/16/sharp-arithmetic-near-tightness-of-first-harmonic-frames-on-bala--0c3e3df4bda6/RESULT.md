# Sharp arithmetic near-tightness of first-harmonic frames on balanced Johnson distance shells

## Finding

For every integer \(k\ge3\), let \(\Omega_k\) be the \(k\)-subsets of \([2k]\) with uniform probability measure, and let \(H_k\) be its first Johnson harmonic space. Fix a \(k\)-set \(R\), and sample one of the distance shells
\[
\Sigma_t=\{X\in\Omega_k:|X\cap R|=t\},\qquad 0\le t\le k,
\]
with its own uniform probability measure. For an injective restriction \(T_{k,t}:H_k\to L^2(\Sigma_t)\), define the squared frame condition number \(\kappa(k,t)\) to be the ratio of the greatest to least eigenvalue of \(T_{k,t}^*T_{k,t}\), using the original uniform \(L^2(\Omega_k)\) norm on \(H_k\). Let \(\mathcal K_k\) be the least such ratio over individual shells.

**Sharp universal arithmetic floor and equality classification:**
\[
\boxed{\mathcal K_k\ge 1+\frac1{2k+1}.}
\]
Equality holds if and only if \(k=2u^2-1\) for an odd integer \(u\ge3\); the only optimal shells in that equality case are \(t=(k-u)/2\) and \(t=(k+u)/2\). No individual shell produces a positive tight frame on all of \(H_k\).

The optimally attainable condition number has two distinct, sharp scales:
\[
\boxed{\liminf_{k\to\infty} k(\mathcal K_k-1)=\frac12,\qquad
\limsup_{k\to\infty}\sqrt{k}(\mathcal K_k-1)=2\sqrt2.}
\]
A fully explicit formula gives \(\mathcal K_k\): for admissible positive integers \(d\equiv k\pmod2\), \(1\le d<k\), put
\[
 r_k(d)=\frac{2(k-1)d^2}{k^2-d^2},\qquad
 \mathcal K_k=\min_d\max\{r_k(d),r_k(d)^{-1}\}.
\]
The optimizing values of \(d\) are among the two parity-compatible integers bracketing \(\alpha_k=k/\sqrt{2k-1}\) (with a missing endpoint ignored). Their shell indices are \(t=(k\pm d)/2\).

## Assumptions and scope

The first harmonic space consists of the functions
\[
 f_a(X)=\sum_{i\in X}a_i,\qquad \sum_{i=1}^{2k}a_i=0,
\]
with complex coefficients \(a_i\); it is the nonconstant first eigenspace of the Johnson graph \(J(2k,k)\) and has complex dimension \(2k-1\). Every expectation and restriction norm is a **probability-normalized** average, not an unnormalized counting sum. The shell \(\Sigma_t\) consists of all \(k\)-sets meeting a fixed reference block in exactly \(t\) elements. For \(0<t<k\), restriction is injective exactly when \(2t\ne k\). End shells and the even middle shell are not included in the condition-number minimum because they fail injectivity. The theorem does not permit combining several shells or changing weights *within* an individual shell.

## Proof

**1. The two frame eigenvalues.** For zero-sum coefficient vectors, the global hypergeometric covariance is
\[
 \mathbb E_{\Omega_k}|f_a|^2=\frac{k}{2(2k-1)}\sum_{i=1}^{2k}|a_i|^2.
\]
Decompose the coefficient hyperplane orthogonally into (i) independent zero-sum contrasts on \(R\) and its complement, total dimension \(2k-2\), and (ii) the line spanned by \(\mathbf1_R-\mathbf1_{R^c}\). On \(\Sigma_t\), the two pieces are orthogonal: the two conditional samples from \(R\) and \(R^c\) are uniform and independent, and each zero-sum contrast has mean zero. The variance of sampling \(t\) elements without replacement from \(k\) entries with zero total is \(t(k-t)/(k(k-1))\) times the squared coefficient norm. On the remaining line, the restricted function is the constant \(2t-k\). Dividing by the displayed global covariance gives precisely
\[
\boxed{
 \lambda_{\mathrm{contrast}}=\frac{2(2k-1)t(k-t)}{k^2(k-1)}\quad[2k-2],
 \qquad \lambda_{\mathrm{normal}}=\frac{(2k-1)(2t-k)^2}{k^2}\quad[1].}
\]
The bracketed numbers are multiplicities. They show both the injectivity criterion and the ratio formula in the finding, using \(d=|2t-k|\) and \(4t(k-t)=k^2-d^2\).

**2. No individual shell is tight.** For a strictly positive tight frame both eigenvalues must agree. That requires \((2k-1)d^2=k^2\). Because \(\gcd(k,2k-1)=1\), the integer \(2k-1\) would divide \(1\), impossible for \(k\ge3\). Noninjective shells cannot produce a positive tight frame.

**3. The sharp lower bound.** Set \(r=r_k(d)\). If \(r\ge1\), then \(d^2\ge k^2/(2k-1)>k/2\), hence the integer \(d^2\) is at least \((k+1)/2\). As a function of \(d^2\),
\[
 r-1=\frac{(2k-1)d^2-k^2}{k^2-d^2}
\]
is strictly increasing. Evaluating at \(d^2=(k+1)/2\) proves \(r-1\ge1/(2k+1)\). Equality forces \(d^2=(k+1)/2\), hence \(k=2u^2-1\) and \(d=u\), and the parity restriction \(d\equiv k\pmod2\) forces \(u\) odd. Conversely each odd \(u\ge3\) gives an admissible pair of equality shells. If \(r<1\), then \(d^2<k^2/(2k-1)<(k+1)/2\), so integer \(d^2\le k/2\). Consequently
\[
 r^{-1}-1=\frac{k^2-(2k-1)d^2}{2(k-1)d^2}
 \ge \frac1{2k-2}>\frac1{2k+1}.
\]
This proves the optimal arithmetic floor and complete equality classification.

**4. The two sharp asymptotic scales.** For \(d>0\), \(r_k(d)\) is strictly increasing and crosses \(1\) at the real value \(\alpha_k=k/\sqrt{2k-1}\). Therefore the optimum comes from one of the two adjacent parity-admissible values around \(\alpha_k\) (or the single available boundary value). Write \(\rho_k\) for the distance of \(\alpha_k\) to its nearest parity-admissible integer. For large \(k\), \(0\le\rho_k\le1\), and expanding the explicit rational function uniformly for bounded \(d-\alpha_k\) yields
\[
 \mathcal K_k-1=\frac{2\sqrt2}{\sqrt k}\,\rho_k+O(k^{-1}).
\]
The universal floor from Step 3 proves \(\liminf k(\mathcal K_k-1)\ge1/2\). Along \(k=2u^2-1\) with odd \(u\to\infty\), equality gives the reverse inequality. The expansion gives \(\limsup\sqrt k(\mathcal K_k-1)\le2\sqrt2\). Along \(k=2s^2\) with odd \(s\to\infty\), one has \(\alpha_k=s+O(s^{-1})\), whereas admissible \(d\) are even; thus \(\rho_k\to1\), establishing equality in the limsup.

## Verification

The standalone standard-library `verify.py` independently constructs exact, rational global and shell covariance matrices from all \(k\)-subsets for \(3\le k\le7\) and every shell. It checks the two stated eigenvalues on an explicit contrast-plus-normal basis, including all noninjective boundaries: 30 exact shell matrix identities. It also enumerates all parity-admissible \(d\) and checks the universal arithmetic bound and equality cases for each \(3\le k\le1500\). The output is `JOHNSON_SHELL_EXACT_PASS`. These computations corroborate the identities; the proof above establishes them for all \(k\ge3\).

## Relationship to prior work

Classical Johnson harmonic decompositions, including the lattice-frame construction of Maldonado and Penazzi [1], supply the ambient eigenfunction framework. Steinerberger [2] studies sampling and spectral designs on graphs, while Vorob'ev [3] studies reconstruction of Johnson eigenfunctions from distance spheres. Iglesias and Natale [4] develop the Johnson Fourier transform. Especially relevant, Bernard, Crampé and Vinet [5, §4.3] give more general Johnson graph single-neighborhood concentration formulas using Clebsch–Gordan coefficients: the **two frame eigenvalues here are obtainable from that established framework and are not claimed as independently new**. The assessed contribution is the global optimization **over all single balanced shells**, the sharp arithmetic non-tightness floor with its infinite equality classification, and the two different sharp asymptotic fluctuation scales. A related published two-coordinate-face Johnson concentration theorem [6] has a different mask and spectral optimization problem.

## Limitations

The result is for the first nonconstant eigenspace of balanced \(J(2k,k)\), one shell at a time, with uniform averaging on that shell and the squared singular-value condition number. Reweighting individual nodes, combining shells, general \(J(n,k)\), or higher Johnson degrees may alter the optimal condition number. The component eigenvalues are closely tied to existing spatio-spectral formulas; the originality claim is confined to the integer-optimization theorem and asymptotics, and older equivalent optimization results could have escaped the identified sources. No independent mathematical audit has been performed.

## References

[1] C. Maldonado and D. Penazzi, *Lattices and Norton algebras of Johnson, Grassmann and Hamming graphs*, arXiv:1204.1947 (2012), https://arxiv.org/abs/1204.1947.

[2] S. Steinerberger, *Generalized Designs on Graphs: Sampling, Spectra, Symmetries*, arXiv:1803.02235 (first public 6 March 2018), https://arxiv.org/abs/1803.02235.

[3] K. Vorob'ev, *On reconstruction of eigenfunctions of Johnson graphs*, arXiv:1812.02424 (2018), https://arxiv.org/abs/1812.02424.

[4] R. Iglesias and M. Natale, *A Fast Fourier Transform for the Johnson graph*, arXiv:1912.09243 (2019), https://arxiv.org/abs/1912.09243.

[5] P.-A. Bernard, N. Crampé and L. Vinet, *Entanglement of free fermions on Johnson graphs*, arXiv:2104.11581 (2021), especially Section 4.3, https://arxiv.org/abs/2104.11581.

[6] *Exact two-coordinate-face concentration spectrum on Johnson slices*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-coordinate-face-concentration-spectrum-on-johnson-slic--d102febb3be1.
