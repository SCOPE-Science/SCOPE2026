# Sharp centered energy dilation for two-frequency Fourier sums

## Finding

For every \(c\in\mathbb R\), every \(0<r<R\), and every nonzero complex Fourier sum
\[
g(t)=v_1e^{i\lambda_1t}+v_2e^{i\lambda_2t},
\qquad \lambda_1,\lambda_2\in\mathbb R,
\quad\lambda_1\ne\lambda_2,
\]
the following strict inequality holds:
\[
\boxed{\displaystyle
\int_{c-R}^{c+R}|g(t)|^2\,dt
<\left(\frac Rr\right)^3\int_{c-r}^{c+r}|g(t)|^2\,dt.}
\]
The exponent \(3\) and coefficient \(1\) are jointly sharp: for every prescribed pair \(0<r<R\), the supremum of the ratio of the integrals over all such sums equals \((R/r)^3\), but is not attained when the two frequencies are distinct.

In particular, if \(X_\delta=[-1-\delta,-1]\cup[1,1+\delta]\) and the training energy is normalized by the uniform probability law on \([-1,1]\), the exact two-frequency exterior-transfer constant is
\[
\boxed{\displaystyle
\Gamma_2(\delta)=\sup_g\frac{\int_{X_\delta}|g(t)|^2\,dt}{\frac12\int_{-1}^{1}|g(t)|^2\,dt}
=2\bigl((1+\delta)^3-1\bigr),\quad\delta>0.}
\]
The supremum ranges over all nonzero sums of at most two real-frequency complex exponentials, with no frequency separation or bandwidth requirement. This calculates the actual integrated transfer operator norm, rather than the integral of pointwise best leverage values.

## Assumptions and scope

The Fourier frequencies are real; coefficients may be complex. Integrals are Lebesgue integrals with no normalization except the explicit factor of one-half in \(\Gamma_2\). The sum is not zero, and distinct frequencies are required for strictness. At most one nonzero coefficient is permitted. The result concerns **symmetric concentric intervals only**; no assertion is made for an asymmetric exterior set or for three or more frequencies. The outer interval always properly contains the inner interval.

## Proof

**1. Reduction to centered unit radius.** Translating the independent variable by \(c\) multiplies each coefficient by a unit complex phase. Scaling by \(r\) multiplies all integrals by the same factor \(r\) and transforms the outer radius to \(L=R/r>1\). A unimodular common-frequency modulation does not change energy. It therefore suffices to prove the result for the span of \(\cos(ut)\) and \(\sin(ut)\), where \(u=|\lambda_1-\lambda_2|r/2>0\). Any sum may be written
\[
 g(t)=e^{i\nu t}\bigl(a\cos(ut)+b\sin(ut)\bigr)
\]
for suitable \(\nu\in\mathbb R\) and \(a,b\in\mathbb C\), not both zero.

**2. Exact energy decomposition.** By reflection, the mixed cosine-sine term integrates to zero on every symmetric interval. With \(d=2u>0\) and \(\operatorname{sinc}(z)=\sin(z)/z\) for nonzero \(z\),
\[
 I(L):=\int_{-L}^{L}|g(t)|^2\,dt
 =L\Bigl(|a|^2[1+\operatorname{sinc}(dL)]
          +|b|^2[1-\operatorname{sinc}(dL)]\Bigr).
\]
Thus it is enough to show, for both independent parity sectors and every \(d>0,L>1\),
\[
 1\pm\operatorname{sinc}(dL)
 < L^2\bigl[1\pm\operatorname{sinc}(d)\bigr].
\]

**3. Strict monotonicity lemma.** For \(z>0\), define
\[
 F_\pm(z)=\frac{z\pm\sin z}{z^3}.
\]
Both functions are strictly decreasing. Indeed,
\[
 z^4 F_+'(z)=z(\cos z-2)-3\sin z,
\qquad
 z^4 F_-'(z)=3\sin z-z(2+\cos z).
\]
For \(0<z\le\pi\), the first numerator is strictly negative because \(\cos z-2<0\) and \(\sin z\ge0\). For \(z\ge\pi\), it is at most \(-z+3<0\). For the second derivative on \((0,\pi]\), put \(H(z)=z(2+\cos z)-3\sin z\). Then \(H(0)=0\) and
\[
 H'(z)=2\sin(z/2)\,[2\sin(z/2)-z\cos(z/2)]>0,
\]
because \(\sin w-w\cos w>0\) for every \(0<w\le\pi/2\): its derivative is \(w\sin w>0\) and its value at zero is zero. For \(z\ge\pi\), \(3\sin z-z(2+\cos z)\le3-z<0\). This proves the monotonicity on all positive arguments, including beyond every sine oscillation.

Now
\[
 \frac{1\pm\operatorname{sinc}(dL)}{L^2}
 =d^2F_\pm(dL)<d^2F_\pm(d)
 =1\pm\operatorname{sinc}(d),
\]
which proves both parity inequalities and hence \(I(L)<L^3I(1)\).

**4. Sharpness, exact exterior transfer, and unattainment.** Let
\[
 g_\varepsilon(t)=\frac{\sin(\varepsilon(t-c))}{\varepsilon}
 =\frac{e^{i\varepsilon(t-c)}-e^{-i\varepsilon(t-c)}}{2i\varepsilon}.
\]
For every \(\varepsilon>0\) it is a legitimate two-frequency sum. As \(\varepsilon\downarrow0\), it converges uniformly on compact intervals to \(t-c\). Consequently
\[
 \lim_{\varepsilon\downarrow0}
 \frac{\int_{c-R}^{c+R}|g_\varepsilon|^2}
 {\int_{c-r}^{c+r}|g_\varepsilon|^2}
 =\frac{2R^3/3}{2r^3/3}=\left(\frac Rr\right)^3.
\]
Strictness for all positive gaps excludes attainment. Subtraction of the inner integral from the outer gives the sharp exterior-to-inner ratio \((R/r)^3-1\). Finally, with \(r=1\), \(R=1+\delta\), and normalization of the denominator by \(1/2\), it becomes \(\Gamma_2(\delta)=2[(1+\delta)^3-1]\). This completes the proof.

## Verification

The proof is analytic for every positive frequency gap and every radius ratio; numerical enumeration is not used to infer the infinite statement. The accompanying `verify_energy.py` independently evaluates the explicit parity integrals across small and large frequency gaps, tests complex coefficient combinations and the sharp collision limit, and compares the exact integral with midpoint quadrature. Run using `python3 verify_energy.py`. All checks are supplementary to the derivative proof, not a substitute for it.

## Relationship to prior work

Ruizhe Zhang's July 11, 2026 preprint *Optimal Extrapolation Bounds for Sparse Fourier Sums*, Section 5.3, defines the actual \(\Gamma_k(\delta)\) and bounds it at the general \(k\)-frequency Chebyshev scale without giving the exact \(k=2\) profile. Published two-frequency exterior point-evaluation results give sharp pointwise leverage but do not by themselves give this exact integrated constant, because the extremizing Fourier coefficients can depend on the evaluation point. The exact fixed-gap parity calculation follows from the same Gram decomposition; the unrestricted sharp supremum additionally needs the all-gap monotonicity argument. This relationship is about the mathematical statements, not just the titles.

For example, integrating the previously available pointwise exterior bound \((1+3t^2)/2\) over the symmetric exterior region, with unnormalized training energy, yields \((1+\delta)^3+\delta-1\), which exceeds the sharp actual integrated result \((1+\delta)^3-1\) by \(\delta>0\).

## Limitations

No uniform coefficient bound is claimed when frequency gaps tend to zero; the sharpness sequence has diverging individual coefficients. Exact optimality applies only to two frequencies and concentric symmetric intervals. In particular, error between two separately fitted two-frequency models may have four frequencies and need not satisfy this two-frequency bound. The possibility of an older equivalent nested-interval or trigonometric-integral inequality is a bibliographic priority risk. This mathematical statement has not received independent validation.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first public version July 11, 2026, especially Section 5.3, Proposition 5.6. https://arxiv.org/abs/2607.10501
2. Chen and Price, work on continuous Fourier interpolation and gapless cluster extrapolation (2019), as referenced in Zhang's introduction.
3. Classical sine-integral/Cusa–Huygens type inequality, with a direct proof included above.
