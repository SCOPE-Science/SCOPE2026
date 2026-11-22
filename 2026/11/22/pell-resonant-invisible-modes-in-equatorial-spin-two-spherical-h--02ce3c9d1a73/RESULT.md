# Pell-resonant invisible modes in equatorial spin-two spherical-harmonic sampling

## Finding

Let \(\mathcal H^{(2)}_\ell\) be the complex \((2\ell+1)\)-dimensional space of pure-degree-\(\ell\), spin-weight \(+2\) spherical harmonics on the unit two-sphere, where \(\ell\) is an integer at least \(2\). Sample any \(f\in\mathcal H^{(2)}_\ell\) in the standard equatorial tangent frame at the \(2\ell+1\) longitudes \(\phi_j=2\pi j/(2\ell+1)\). Write \(R_\ell f\) for this equatorial sample vector.

Define a sequence of integers \((\ell_k,m_k)\) by
\[
2\ell_k+1+m_k\sqrt8=(3+\sqrt8)^k,\qquad k\ge1.
\]
Its first terms are \((\ell_1,m_1)=(1,1)\), \((\ell_2,m_2)=(8,6)\), \((\ell_3,m_3)=(49,35)\), and \((\ell_4,m_4)=(288,204)\). For each \(\ell\ge2\), the **complete nullspace** is
\[
\ker R_\ell=\operatorname{span}_{\mathbb C}\!\left(\{{}_2Y_{\ell0}:\ell\text{ odd}\}\,\cup\,\{{}_2Y_{\ell,m_k},{}_2Y_{\ell,-m_k}:\ell=\ell_k,\ k\ge2\}\right).
\]
Consequently,
\[
\operatorname{rank}R_\ell=2\ell+1-\mathbf 1_{\ell\text{ odd}}-2\mathbf1_{\ell\in\{\ell_k:k\ge2\}}.
\]
In particular, equatorial samples are injective at every positive even degree except an **infinite** sequence \(\ell=8,288,\ldots\), while all odd degrees lose the zonal mode and infinitely many odd degrees \(\ell=49,\ldots\) lose two further modes. The first rank defects are \(\operatorname{rank}R_2=5\), \(\operatorname{rank}R_3=6\), \(\operatorname{rank}R_8=15\), and \(\operatorname{rank}R_{49}=96\).

## Assumptions and scope

The scalar harmonics \(Y_{\ell m}\) and spin harmonics \({}_2Y_{\ell m}\) are orthonormal in surface-area \(L^2(S^2)\), with the usual Condon–Shortley phase; differences in nonzero basis phases do not alter the theorem. Fix the standard local frame \((e_\theta,e_\phi)\) along the equator \(\theta=\pi/2\). In this frame \({}_2Y_{\ell m}(\theta,\phi)=A_{\ell m}(\theta)e^{im\phi}\), with \(A_{\ell m}\) independent of \(\phi\). The result concerns a *single exact angular degree* and the \(2\ell+1\) indicated equally spaced azimuths, not recovery of a mixed-degree bandlimit. Samples of spin-weighted sections are represented as complex numbers only after fixing this local frame.

## Proof

**1. Exact spectral diagonalization.** In the spin raising convention
\[
\eth_s f=-\bigl(\partial_\theta+i\csc\theta\,\partial_\phi-s\cot\theta\bigr)f,
\]
we have \({}_2Y_{\ell m}=c_\ell\eth_1\eth_0Y_{\ell m}\), where \(c_\ell=\sqrt{(\ell-2)!/(\ell+2)!}>0\). On the equator the spin frame is smooth and fixed. If \(f=\sum_{m=-\ell}^{\ell}a_m{}_2Y_{\ell m}\), discrete Fourier orthogonality at \(M=2\ell+1\) nodes gives exactly
\[
\frac1M\sum_{j=0}^{M-1}|f(\pi/2,2\pi j/M)|^2
=\sum_{m=-\ell}^{\ell}|a_m|^2|{}_2Y_{\ell m}(\pi/2,0)|^2.
\]
Thus the nullspace consists of precisely the basis modes whose equatorial amplitude vanishes; no cancellations between distinct modes are possible.

**2. The equatorial coefficient.** For \(r=|m|\), the scalar mode is \(Y_{\ell m}(\theta,\phi)=C_{\ell m}P_\ell^r(\cos\theta)e^{im\phi}\), with \(C_{\ell m}\ne0\). Differentiating \(\eth_1\eth_0\) at the equator and using the associated Legendre differential equation at zero gives, up to a nonzero factor,
\[
{}_2Y_{\ell m}(\pi/2,0)\sim
\bigl(2m^2-\ell(\ell+1)\bigr)P_\ell^r(0)+2m\,(P_\ell^r)'(0).
\]
The parity identity \(P_\ell^r(-x)=(-1)^{\ell+r}P_\ell^r(x)\), together with the explicit nonzero double-factorial values at zero, implies: if \(\ell+r\) is even, \(P_\ell^r(0)\ne0\) and \((P_\ell^r)'(0)=0\); if it is odd, \(P_\ell^r(0)=0\) and \((P_\ell^r)'(0)\ne0\). Therefore the amplitude vanishes exactly when either
\[
(\ell+r\text{ even and }\ell(\ell+1)=2m^2),
\quad\text{or}\quad
(\ell+r\text{ odd and }m=0).
\]
The second case is just \(m=0\) at odd \(\ell\).

**3. Solving the arithmetic case.** The equation \(\ell(\ell+1)=2m^2\) is equivalent to \((2\ell+1)^2-8m^2=1\). All positive solutions of this Pell equation have
\[
(2\ell+1)+|m|\sqrt8=(3+\sqrt8)^k,\quad k\ge1.
\]
Its recurrence \(\ell_{k+1}=3\ell_k+4m_k+1\), \(m_{k+1}=2\ell_k+3m_k+1\) shows inductively that \(\ell_k\) and \(m_k\) have equal parity. Hence the required \(\ell+|m|\) even condition is automatic. For \(\ell\ge2\), \(m_k\le\ell_k\), and \(k=1\) is excluded by spin-weight \(2\). The two nonzero signed orders are \(\pm m_k\). The Pell degrees strictly increase, so at most one positive \(m_k\) occurs per degree. Combining this enumeration with steps 1–2 proves both the full nullspace and rank formula. The parity recurrence also shows that even- and odd-degree Pell exceptions each occur infinitely often.

## Verification

The accompanying standard-library Python checker evaluates the factorial Wigner small-\(d\) expansion at angle \(\pi/2\) as an **exact rational sum**, independently of the Legendre differential-equation proof. It compares the predicted zero mask with all \(\sum_{\ell=2}^{64}(2\ell+1)=4221\) harmonics, checks the higher Pell modes at degrees \(8\), \(49\), \(288\), and compares seven complete nullspaces. Running `python3 verify_spin2.py` returns `PASS: 4240 exact rational Wigner and Pell assertions` (the assertion counter also counts the nonzero signed-mode checks). This finite test checks calculations, not the all-degree proof; the latter is supplied above.

## Relationship to prior work

Elahi, Khalid, Kennedy and McEwen [1] develop multidimensional near-optimal spin-\(s\) sphere sampling and introduce the Wigner-\(d\) harmonic formula used here. Bangun, Behboodi and Mathar [2] analyze coherence and regular grids for Wigner functions. Zhong, Zhou, Zhang and Sheng [3] develop even/odd Wigner-\(D\) orthogonality identities. None of those inspected analyses classifies which individual spin-two modes vanish on a *single equator*, gives this Pell nullspace sequence, or derives the resulting exact degree-by-degree sampling ranks. General scalar spherical-harmonic and full-band spin transform results do not imply the fixed-degree spin-two rank law without the nontrivial second spin-raising calculation and the Pell classification.

## Limitations

This is an exact single-degree injectivity theorem; it provides neither a lower bound on the smallest **nonzero** singular value nor a stable all-degree frame. Infinite even-degree exceptions do not mean that all high-degree sampling fails. This is a best-knowledge originality assessment, not a proof that an equivalent older representation-theoretic identity has never been stated. The separate checker evaluates finitely many degrees and is not an exhaustive proof of infinitely many Pell exceptions.

## References

1. U. Elahi, Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321v1, publicly submitted 5 September 2018. https://arxiv.org/html/1809.01321v1
2. A. Bangun, B. Behboodi and R. Mathar, *Tight bounds on the mutual coherence of sensing matrices for Wigner D-functions on regular grids*, arXiv:2010.02344 (2020). https://arxiv.org/abs/2010.02344
3. Z. Zhong, Y. Zhou, Z. Zhang and Y. Sheng, *Even- and odd-orthogonality properties of the Wigner D-matrix and their metrological applications*, arXiv:2301.08166 (2023). https://arxiv.org/abs/2301.08166
