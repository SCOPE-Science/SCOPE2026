# Exact reciprocal-integer Zak zero geometry for centered cardinal B-splines

## Finding

**Theorem.** Fix integers \(n\ge 3\) and \(m\ge 3\). For the centered order-\(n\) cardinal B-spline, the complete real Zak-zero set in the fundamental square is

\[
\left\{(x,\nu)\in[0,1)^2:Z_{1/m}B_n(x,\nu)=0\right\}
=\bigcup_{r=1}^{m-1}\left([0,1)\times\{r/m\}\right)
\;\cup\;
\begin{cases}\{(1/2,1/2)\},&m\text{ odd},\\\varnothing,&m\text{ even}.\end{cases}
\]

For every horizontal line with \(r/m\ne1/2\), its zero has *exact transverse multiplicity* \(n\) at every spatial point. When \(m\) is even, the same holds along \(\nu=1/2\) except at one intersection with the unit-scale zero: \(x\equiv (1-n(m-1))/2\pmod{1}\). No order is asserted at that exceptional intersection.

## Assumptions and scope

Let \(B_1=\mathbf1_{[-1/2,1/2]}\) (endpoint values immaterial), and let \(B_n=B_1^{*n}\), so \(B_n\) is real, even, compactly supported on \([-n/2,n/2]\), and continuous for \(n\ge2\). We use the normalized Zak convention

\[
Z_\lambda f(x,\nu)=\sqrt\lambda\sum_{k\in\mathbb Z} f(\lambda(x-k))e^{2\pi i k\nu},\qquad \lambda>0.
\]

The sum is finite for each \(x\). The spatial coordinate is considered modulo one for zero-set purposes (the Zak transform is quasi-periodic), and the frequency coordinate is modulo one. The statement concerns precisely the reciprocal-integer scales \(\lambda=1/m\), not general rational or continuously varying scales.

## Proof

**1. Centered refinement.** Let \(S_m(z)=\sum_{j=0}^{m-1}z^j\), and define integer coefficients \(c_j\) by \(S_m(z)^n=\sum_{j=0}^{n(m-1)}c_jz^j\). Partitioning \([-1/2,1/2]\) into \(m\) equal subintervals gives, almost everywhere,

\[
B_1(t)=\sum_{j=0}^{m-1}B_1\bigl(mt+(m-1)/2-j\bigr).
\]

Taking the \(n\)-fold convolution, with the scaling factor \(m^{1-n}\), yields the continuous identity for \(n\ge2\):

\[
B_n(t)=m^{1-n}\sum_{j=0}^{n(m-1)}c_j
 B_n\bigl(mt+n(m-1)/2-j\bigr).
\]

This is independently derivable from \(\widehat B_n(\xi)=\operatorname{sinc}(\xi)^n\) and the Dirichlet-kernel factorization of \(\sin(\pi\xi)\).

**2. Exact Zak factorization.** Put \(s=n(m-1)/2\) and \(z=e^{2\pi i\nu}\). Substitute \(t=(x-k)/m\) into the refinement identity and set \(\ell=k+j\). Then

\[
\begin{aligned}
Z_{1/m}B_n(x,\nu)
&=m^{1/2-n}\sum_j c_jz^{-j}
\sum_\ell B_n(x+s-\ell)z^\ell\\
&=m^{1/2-n}z^{-n(m-1)}S_m(z)^n
Z_1B_n(x+s,\nu).
\end{aligned}
\tag{1}
\]

All rearrangements are finite. The factor outside \(S_m(z)^n Z_1B_n\) never vanishes on the unit circle.

**3. Zeros.** The finite geometric polynomial \(S_m(z)=(z^m-1)/(z-1)\) has precisely the nontrivial \(m\)-th roots of unity as zeros, all simple. Thus its Zak factor gives every horizontal line \(\nu=r/m\), \(1\le r<m\). A classical theorem on exponential Euler/cardinal spline functions states that for every \(n\ge2\) the unit-scale centered transform \(Z_1B_n\) has **exactly one zero modulo the unit square**, namely \((1/2,1/2)\); see the primary references below. Consequently, no other zeros are possible except those with \(\nu=1/2\) and \(x+s\equiv 1/2\pmod{1}\). If \(m\) is even, \(1/2=(m/2)/m\) is already a mask-zero frequency. If \(m\) is odd, \(s\) is an integer, so the sole additional zero in the fundamental square is \((1/2,1/2)\). This proves the classification with no numerical completeness assumption.

**4. Exact transverse multiplicity.** For \(\zeta=e^{2\pi ir/m}\ne1\),

\[
S_m'(\zeta)=\frac{m\zeta^{m-1}}{\zeta-1},\qquad
S_m(e^{2\pi i(r/m+\varepsilon)})
=\frac{2\pi im}{\zeta-1}\varepsilon+O(\varepsilon^2).
\]

If \(r/m\ne1/2\), the unit-scale factor in (1) does not vanish for any \(x\). Its product with the simple mask zero raised to the \(n\)-th power gives an exact order-\(n\) zero. At \(r/m=1/2\) with even \(m\), the unit-scale factor can vanish only at \(x+s\equiv1/2\pmod{1}\), which is the stated single exception.

## Verification

The included `zak_refinement_checker.py` verifies the unnormalized polynomial-mask identity with exact rational arithmetic at 126 choices: \(2\le n\le8\), \(2\le m\le7\), and three rational spatial coordinates, plus mask-index checks. The symbolic identity in (1) is proved for *all* stated integers independently of this finite calculation. Reproduce with `python3 zak_refinement_checker.py` using only the Python standard library. The unit-scale uniqueness premise is a cited classical theorem, not inferred from the tests.

## Relationship to prior work

Hasannasab and Lemvig (2026) prove the universal horizontal zero lines at integer reciprocal scales via an aliasing lemma and give complete zero sets for the second-order spline at all scales and for all spline orders above unit scale. They do not give the all-order **complete** subunit reciprocal-integer zero set or its transverse multiplicity in the inspected main results. Kloos and Stöckler (2014, preprint 2013) state and prove uniqueness of the unit-scale spline Zak zero; the present theorem couples that established input to a new exact refinement-mask factorization at infinitely many smaller scales. The special second-order case is already covered by the 2026 paper and is excluded from the claimed new range. Previously studied continuous subunit intervals near \(\lambda=1\) do not contain \(\lambda=1/m\) for \(m\ge3\).

## Limitations

Only centered cardinal B-splines with integer reciprocal spatial scales are classified. The proof does not determine the zero set at arbitrary nonintegral reciprocal scales, does not supply optimal Gabor frame bounds, and does not calculate the transverse order at the one exceptional intersection when \(m\) is even. The underlying refinement relation and the unit-scale uniqueness theorem are classical; whether this exact combined statement has appeared in earlier spline literature remains a publication-priority risk. No independent mathematical validation is claimed.

## References

1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116, first posted 2026-09-11. https://arxiv.org/abs/2609.13116
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013); J. Approx. Theory 184 (2014), 209–237. https://arxiv.org/abs/1311.7359
3. I. J. Schoenberg, *Cardinal Spline Interpolation*, SIAM, 1973 (classical unit-scale exponential Euler-spline zero theorem).
