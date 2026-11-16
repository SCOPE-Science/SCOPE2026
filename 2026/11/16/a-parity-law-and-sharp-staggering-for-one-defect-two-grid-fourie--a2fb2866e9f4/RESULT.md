# A parity law and sharp staggering for one-defect two-grid Fourier interpolation

## Finding

For every integer \(q\ge2\), every integer replacement height \(m\ge2\), every residue \(b\in\{0,\ldots,q-1\}\), and every \(0<\theta<1\), consider two shifted regular sampling grids
\[
X_{q,\theta}=\left\{\frac{j}{q}:0\le j<q\right\}\cup\left\{\frac{j+\theta}{q}:0\le j<q\right\}\subset\mathbb T,
\]
and the \(2q\) distinct integer frequencies
\[
F_{q,m,b}=\bigl(\{0,\ldots,2q-1\}\setminus\{q+b\}\bigr)\cup\{mq+b\}.
\]
The normalized square Fourier interpolation matrix is \(A=(2q)^{-1/2}(e^{2\pi i kx})_{k\in F_{q,m,b},\,x\in X_{q,\theta}}\), with each set ordered arbitrarily. The **entire multiset of squared singular values** is
\[
\boxed{\left\{1\pm|\cos(\pi\theta)|\;\text{each repeated }q-1\text{ times},\quad 1\pm|\cos(\pi m\theta)|\right\}.}
\]
It does not depend on the replaced residue \(b\). The matrix is singular exactly at the \(m-1\) internal offsets \(\theta=r/m\), \(1\le r<m\), and has nullity exactly one at each.

For invertible matrices, let \(\kappa\) be the Euclidean spectral condition number. The sharp global minimizers and optimum are
\[
\boxed{\begin{array}{ll}
 m\text{ odd}: &\displaystyle\min_{0<\theta<1}\kappa=1,\quad \theta=\frac12\ \text{uniquely};\\[2mm]
 m\text{ even}:&\displaystyle\min_{0<\theta<1}\kappa=
 \sqrt{\frac{1+\sin\bigl(\pi/[2(m+1)]\bigr)}{1-\sin\bigl(\pi/[2(m+1)]\bigr)}},\\[2mm]
 &\displaystyle\theta\in\left\{\frac{m}{2(m+1)},\frac{m+2}{2(m+1)}\right\}\ \text{exactly}.
\end{array}}
\]
In particular, a *single* replaced frequency with an even band-jump prevents perfectly conditioned interpolation in every grid size, whereas every odd band-jump admits an exactly unitary sampler. At either even-jump optimum the squared singular values are \(1\pm\sin(\pi/[2(m+1)])\), each with multiplicity \(q\). For fixed even \(m\to\infty\), the optimum condition number is \(1+\pi/[2(m+1)]+O(m^{-2})\). At any singular offset \(\theta_0=r/m\),
\[
\boxed{\kappa(A_{q,m,b,\theta})\sim\frac{2}{\pi m|\theta-\theta_0|}\quad(\theta\to\theta_0,\ \theta\ne\theta_0).}
\]

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/\mathbb Z\), sampled at the \(2q\) distinct sites above. Both the frequency-band replacement and the spatial staggering are deterministic. The rows are integer Fourier characters, and the matrix is square. All singular values use the displayed \((2q)^{-1/2}\) normalization. The condition number is the ratio of largest to smallest singular value and is defined only where the latter is positive. The optimum ranges over every real \(0<\theta<1\), with \(q,m,b\) fixed; no optimization over arbitrary sample sites or frequency sets is asserted. The central statements hold for all \(q\ge2\) and all \(m\ge2\), not just asymptotically.

## Proof

**Fourier block reduction.** Index each site by a grid label \(s\in\{0,1\}\) and position \(j\in\{0,\ldots,q-1\}\), so \(x_{j,s}=(j+s\theta)/q\). Every frequency has the unique form \(k=r+\ell q\), where \(0\le r<q\), and there are exactly two frequency rows for each \(r\): \(\ell=0\) and \(\ell=d_r\), with \(d_r=1\) except \(d_b=m\). The identity
\[
 e^{2\pi i(r+\ell q)x_{j,s}}=e^{2\pi irj/q}e^{2\pi i(r/q+\ell)s\theta}
\]
shows that applying a unitary \(q\)-point discrete Fourier transform separately to the two site grids and permuting the rows makes \(A\) unitarily equivalent to the direct sum over \(r\) of
\[
 B_r=\frac1{\sqrt2}\begin{pmatrix}
 1&e^{2\pi ir\theta/q}\\
 1&e^{2\pi i(r/q+d_r)\theta}
 \end{pmatrix}.
\]
Its Gram matrix has diagonal entries one and an off-diagonal entry of modulus
\[
\frac12\left|1+e^{2\pi i d_r\theta}\right|=|\cos(\pi d_r\theta)|.
\]
The two squared singular values are exactly \(1\pm|\cos(\pi d_r\theta)|\). Taking all \(r\) proves the stated spectrum and independence from \(b\).

**Rank and condition number.** A block is singular if and only if \(d_r\theta\in\mathbb Z\). For \(0<\theta<1\), no ordinary block (\(d_r=1\)) is singular. The exceptional block is singular precisely when \(\theta=r/m\), \(1\le r<m\), with one zero eigenvalue. Setting \(M_m(\theta)=\max\{|\cos(\pi\theta)|,|\cos(\pi m\theta)|\}\) gives the two global extremal squared singular values \(1\pm M_m(\theta)\) and hence \(\kappa=\sqrt{(1+M_m)/(1-M_m)}\) whenever the matrix is invertible.

**Sharp minimax, odd case.** Since \(M_m\ge0\), perfect conditioning requires both cosines to vanish. The first vanishes only for \(\theta=1/2\) in the open interval. Then \(\cos(\pi m/2)=0\) if and only if \(m\) is odd. This proves the optimum and uniqueness for every odd replacement height.

**Sharp minimax, even case.** Let \(m\) be even and put \(u=|\cos(\pi\theta)|\). Then \(0\le u<1\) and, by reflection about \(\theta=1/2\),
\[
 M_m(\theta)=\max\{u,|\cos(m\arcsin u)|\}.
\]
Set \(u_*=\sin\bigl(\pi/[2(m+1)]\bigr)\), so \(\alpha_*=\arcsin u_*=\pi/[2(m+1)]\). For \(u\ge u_*\), the maximum is at least \(u_*\), with a strict inequality when \(u>u_*\). For \(0\le u<u_*\), one has \(0\le m\arcsin u<m\alpha_*<\pi/2\), hence
\[
 |\cos(m\arcsin u)|=\cos(m\arcsin u)>
 \cos(m\alpha_*)=\cos(\pi/2-\alpha_*)=u_*.
\]
At \(u=u_*\), both entries of the maximum are exactly \(u_*\). Thus it is the unique minimizing \(u\); the only corresponding offsets are \(\theta=1/2\pm1/[2(m+1)]\). Substituting \(M_m=u_*\) yields the optimal condition number, the two-level spectrum and its equal multiplicities. Taylor expansion of the sine and square root gives the displayed asymptotic expansion.

**Sharp singularity profile.** Fix \(1\le r<m\) and \(\theta_0=r/m\). The ordinary-block coherence \(|\cos(\pi\theta_0)|\) is strictly less than one. Consequently the exceptional block determines both extreme singular levels sufficiently near \(\theta_0\). Writing \(\varepsilon=\theta-\theta_0\) yields
\[
 1-|\cos(\pi m\theta)|=\tfrac12\pi^2m^2\varepsilon^2+O(\varepsilon^4),\qquad
 1+|\cos(\pi m\theta)|=2+O(\varepsilon^2).
\]
Their ratio has square root asymptotic to \(2/(\pi m|\varepsilon|)\), independently of the other parameters and of \(r\).

## Verification

The standalone `CHECK.py` independently constructs each full complex sampling matrix and diagonalizes its numerical Gram matrix, rather than implementing the Fourier block reduction as its primary matrix construction. It compares those eigenvalues against the exact formulas for \(2\le q\le10\), \(2\le m\le11\), several replaced residues and five offsets; checks the claimed optimum for every \(2\le m<40\); checks ranks at the half-step for \(2\le q\le8\), \(2\le m<20\); and checks the asymptotic blow-up near all internal resonances for seven replacement heights. The check completed with `CHECKS_PASSED 1597`. This finite verification corroborates but does not prove the universal claims; the complete analytical proof is above. Run `python CHECK.py` with Python 3 and NumPy.

## Relationship to prior work

Finite nonuniform Fourier and clustered Vandermonde stability is a well-developed topic. Batenkov and Goldman (2021) derive singular-value bounds for clustered nodes and prolate matrices, including the entire-spectrum scaling (their Section 7); those estimates neither involve a single replaced integer frequency in paired cyclic sample grids nor determine an optimal stagger. Lai and Sheynis (2023) develop qualitative multi-tiling exponential Riesz-basis criteria. The present block decomposition is elementary Fourier aliasing and is **not** claimed as a new general method.

Published results for two-coset Riesz bases on separated intervals determine the minimax of two *consecutive* cosine frequencies and include the same scalar \(\max(|\cos t|,|\cos2t|)\) at one parameter. That special scalar minimax is prior art, not a separate novelty claim here. The current contribution is the all-replacement-height odd/even law, its exact \(m\)-dependent optimizers, the all-grid-size spectral classification and singularity profiles for a different periodic two-grid interpolation object. A result for a three-displacement planar double tile likewise uses finite cosine maximization but does not cover this family of arbitrary replacement heights. These comparisons leave a risk that an earlier general two-grid aliasing treatment contains the full specialized result.

## Limitations

The statement concerns one replaced Fourier frequency and two equally sized uniform grids. It does not prove optimality among general nonuniform node configurations, multiple simultaneous replacements, or arbitrary nonuniform weights. Although the final formulas hold exactly for all dimensions, their derivation uses standard DFT block diagonalization and elementary trigonometric minimax; no new general Fourier inequality or recovery algorithm is claimed. Historical priority is supported by the comparisons described, but has not been independently certified.

## References

1. D. Batenkov and G. Goldman, *Single-exponential bounds for the smallest singular value of Vandermonde matrices in the sub-Rayleigh regime*, arXiv:2107.09326v1, first posted 2021-07-20; *Applied and Computational Harmonic Analysis* **55** (2021), 426–439.
2. C.-K. Lai and A. Sheynis, *Riesz bases of exponentials for multi-tiling measures*, arXiv:2309.14625v1, first posted 2023-09-26.
3. L. Guo, C. W. Kok, H. C. So, and W. S. Tam, *Fast and \(L^2\)-optimal recovery for periodic nonuniformly sampled bandlimited signal*, *Signal Processing* **180** (2021), 107856, DOI:10.1016/j.sigpro.2020.107856.
4. *Optimal two-coset Fourier conditioning on separated unit intervals*, publicly available mathematical result (2026), identifier `1e706b439add`.
5. *Optimal vertical two-coset exponential bases for a tent-roof double tile*, publicly available mathematical result (2026), identifier `89421d123299`.
