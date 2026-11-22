# Countably many exterior spectral components from an arbitrarily small square-zero perturbation of the unilateral shift

## Finding

Let \(S e_j=e_{j+1}\) be the unweighted unilateral shift on \(H=\ell^2(\mathbb N_0;\mathbb C)\). There is one explicit rank-one operator \(K_1\) with \(K_1^2=0\), such that for **every** real \(c>0\), \(K_c=cK_1\) has \(\|K_c\|=c\|K_1\|\) and

\[
\sigma(S+K_c)=\overline{\mathbb D}\ \cup\ \{z:\ |z|>1,\ c h(1/z)=1\},
\qquad h(w)=w(1-w)^{-1/4}\sin(\log(1-w)).
\]

Here the logarithm is the holomorphic branch on \(\mathbb D\) with \(\log 1=0\). The exterior set comprises infinitely many isolated eigenvalues and accumulates only at \(z=1\). Thus \(\sigma(S+K_c)\) has **countably infinitely many connected components**, despite \(S\) being a fixed noncompact isometry and \(K_c\) having arbitrarily small operator norm and square zero.

More sharply, for

\[
N_c(\delta)=\#\big(\sigma(S+K_c)\cap(1+\delta,\infty)\big),
\]

counting distinct *real* eigenvalues, one has

\[
\boxed{\displaystyle N_c(\delta)=\frac{1}{\pi}\log\frac1\delta+O_c(1)}\qquad (\delta\downarrow0).
\]

For all sufficiently large integers \(k\), exactly two such eigenvalues have the coordinates \(z=(1-e^{-t})^{-1}\) with \((2k+1)\pi<t<(2k+2)\pi\). Their respective coordinates satisfy

\[
\begin{aligned}
t_{k,-}&=(2k+1)\pi+c^{-1}e^{-(2k+1)\pi/4}(1+o(1)),\\
t_{k,+}&=(2k+2)\pi-c^{-1}e^{-(2k+2)\pi/4}(1+o(1)).
\end{aligned}
\]

The statement does **not** assert that every exterior eigenvalue is real.

## Assumptions and scope

All operators act on complex \(\ell^2(\mathbb N_0)\). Define the Taylor coefficients \(h(w)=\sum_{n\ge0}h_n w^n\); then \(h_0=h_1=0\) and \(h_2=-1\). Let

\[
K_c(x_0,x_1,\ldots)=c\left(\sum_{j=0}^{\infty}h_{j+1}x_j\right)e_0.
\]

The branch of \((1-w)^{-1/4}\) is consistent with the branch of \(\log(1-w)\) specified above. The series defining \(K_c\) is absolutely convergent by Cauchy–Schwarz because \(h\in H^2(\mathbb D)\), as shown below. The coupling \(c\) is any fixed positive real number; the estimates implied by \(O_c(1)\) need not be uniform as \(c\to0\).

## Proof

**1. The coefficient functional is bounded and nilpotent.** For \(|w|<1\), \(\operatorname{Re}(1-w)>0\) and therefore \(|\operatorname{Im}\log(1-w)|<\pi/2\). The inequality \(|\sin(x+iy)|\le\cosh|y|\) gives

\[
|h(w)|\le \cosh(\pi/2)|1-w|^{-1/4}.
\]

Since \(\sup_{0<r<1}\int_{-\pi}^{\pi}|1-re^{i\theta}|^{-1/2}\,d\theta<\infty\), the standard radial characterization of the Hardy space yields \(h\in H^2(\mathbb D)\), equivalently \(\sum_n|h_n|^2<\infty\). (For an elementary bound, \(|1-re^{i\theta}|^2=(1-r)^2+2r(1-\cos\theta)\), and split into \(r\le1/2\) and \(r>1/2\), using \(1-\cos\theta\gtrsim\theta^2\).) Thus \(K_c\) is bounded and rank one, because \(h_2=-1\). Its only range direction is \(e_0\), but \(K_c e_0=c h_1 e_0=0\). Hence \(K_c^2=0\). Parseval gives \(\|K_c\|=c\|h\|_{H^2}\), so its norm tends to zero with \(c\).

**2. Exact spectrum.** For \(|z|>1\), the Neumann series implies

\[
(zI-S)^{-1}e_0=\sum_{j\ge0}z^{-j-1}e_j.
\]

Hence \(K_c(zI-S)^{-1}e_0=c h(1/z)e_0\). The rank-one inversion criterion, equivalently the factorization of \(zI-S-K_c\), implies that \(z\) belongs to \(\sigma(S+K_c)\) if and only if \(c h(1/z)=1\); each such exterior spectral point is an eigenvalue. For \(|z|<1\), \(zI-S\) is Fredholm of index \(-1\), a value unchanged by finite-rank perturbations, and thus \(zI-(S+K_c)\) is not invertible. At \(|z|=1\), the shift is not Fredholm, and finite-rank perturbations preserve this property. Consequently the entire closed unit disk remains in the spectrum and the displayed formula is exact.

**3. Localization of exterior zeros.** The function \(h\) extends holomorphically through every boundary point \(w\in\partial\mathbb D\setminus\{1\}\), since the factor \(1-w\) does not vanish there and a local branch of its logarithm exists. The function \(c h-1\) is nonzero at \(w=0\) and is not identically zero. Its zeros in \(\mathbb D\) are discrete and can accumulate on \(\partial\mathbb D\) only at \(w=1\). Passing to \(z=1/w\) proves that exterior eigenvalues are isolated, bounded, and have no exterior accumulation point and no boundary accumulation other than \(z=1\). Each is a singleton connected component, while the closed disk is a connected component of the spectrum.

**4. Exactly two roots per late negative-sine lobe.** On the positive real axis parameterize \(w=1-e^{-t}\), \(t>0\), hence \(z=(1-e^{-t})^{-1}>1\). The exterior eigenvalue equation becomes

\[
 c(1-e^{-t})e^{t/4}(-\sin t)=1.
\]

It has no roots where \(\sin t\ge0\). On each negative-sine interval \(I_k=((2k+1)\pi,(2k+2)\pi)\), the positive function

\[
H_c(t)=c(1-e^{-t})e^{t/4}(-\sin t)
\]

vanishes at both endpoints. Its logarithmic derivative is

\[
\frac{H_c'(t)}{H_c(t)}=\frac{e^{-t}}{1-e^{-t}}+\frac14+\cot t,
\]

whose derivative is strictly negative:

\[
-\frac{e^{-t}}{(1-e^{-t})^2}-\csc^2t<0.
\]

The logarithmic derivative tends from \(+\infty\) to \(-\infty\) across \(I_k\). Thus \(H_c\) has exactly one maximum on \(I_k\), and this maximum exceeds \(1\) for every sufficiently large \(k\) (evaluate at \((2k+3/2)\pi\)). Hence \(H_c=1\) has exactly two distinct, simple solutions in each sufficiently late \(I_k\).

**5. Sharp locations and count.** Put \(L_k=(2k+1)\pi\), \(R_k=(2k+2)\pi\). On the rising edge write \(t=L_k+\eta\). The preceding equation gives

\[
1=c(1-e^{-L_k-\eta})e^{(L_k+\eta)/4}\sin\eta.
\]

For the first root \(\eta\to0\); dividing by \(\eta c e^{L_k/4}\) gives \(\eta=c^{-1}e^{-L_k/4}(1+o(1))\). On the descending edge, \(t=R_k-\eta\), the same argument yields \(\eta=c^{-1}e^{-R_k/4}(1+o(1))\). There are no other positive real roots outside the negative-sine intervals, and only finitely many roots in the finitely many early intervals. The condition \(z>1+\delta\) is equivalent to

\[
t<\log\left(\frac{1+\delta}{\delta}\right)=\log(1/\delta)+O(\delta).
\]

Every interval of length \(2\pi\) eventually contributes exactly two roots, and at most two are affected by the last partial interval. Therefore \(N_c(\delta)=\pi^{-1}\log(1/\delta)+O_c(1)\). This also supplies infinitely many exterior spectral points converging to \(1\), completing the component count.

## Verification

The proof is analytic and does not rely on finite enumeration or numerical data. It admits the following exact local checks: \(h(w)=-w^2+O(w^3)\), the rank-one resolvent scalar is \(c h(1/z)\), the logarithmic derivative has derivative strictly less than \(-\csc^2t\), and every sufficiently large negative-sine interval has precisely two crossings. The corresponding counting slope is two roots per \(2\pi\) logarithmic length. These checks give the complete infinite-family conclusion, not a finite approximation.

## Relationship to prior work

Bračič and Kandić (2026), *On operators with many spectral components*, establish general density of spectral-component classes and a square-zero rank-one construction for a **compact quasinilpotent weighted shift with summable weights**. Their construction does not, by itself, give the result for the fixed **noncompact, unweighted** isometry. Ko and Lee (2011) establish rank-one eigenvalue criteria and examples for the unweighted unilateral shift; the rank-one determinant itself is an established technique, not claimed as new here. Hansmann (2026), *Prescribed spectral configurations under rank-one perturbations*, realizes arbitrary compatible spectral configurations while **choosing the unperturbed operator**, even when the perturbation is prescribed; it does not prescribe the base to be the standard unilateral shift. The present contribution is the explicit fixed-base, arbitrarily-small square-zero example together with its sharp real counting law.

## Limitations

This theorem asserts neither exact locations nor multiplicities of **nonreal** exterior eigenvalues. The formula \(N_c(\delta)\) counts only distinct positive real exterior eigenvalues; it does not count all complex eigenvalues with \(|z|>1+\delta\). No claim is made about general shift weights, arbitrary rank-one perturbations, or universality of the counting coefficient. The literature comparison does not exclude implicit coverage by older rank-one spectral or Hardy-space interpolation results. An independent mathematical audit has not been performed.

## References

1. J. Bračič and M. Kandić, *On operators with many spectral components*, arXiv:2611.12208, first posted 9 November 2026. https://arxiv.org/abs/2611.12208
2. E. Ko and J. E. Lee, *On rank one perturbations of the unilateral shift*, Communications of the Korean Mathematical Society **26** (2011), 79–88. https://doi.org/10.4134/CKMS.2011.26.1.079
3. M. Hansmann, *Prescribed spectral configurations under rank-one perturbations*, arXiv:2610.33630, first posted 24 October 2026. https://arxiv.org/abs/2610.33630
