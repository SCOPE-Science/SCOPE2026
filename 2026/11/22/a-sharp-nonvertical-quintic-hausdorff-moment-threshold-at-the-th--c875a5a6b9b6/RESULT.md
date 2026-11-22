# A sharp nonvertical quintic Hausdorff-moment threshold at the three-to-two frequency ratio

## Finding

For every \(a,b,c>0\), put
\[
P(x)=(x+a)\big((x+b)^2+c^2\big)\big((x+b)^2+9c^2/4\big),
\qquad We_n=\sqrt{P(n+1)/P(n)}\,e_{n+1}.
\]
The positive unilateral weighted shift \(W\) is a bounded, expansive, strict \(6\)-isometry. Its Cauchy dual \(W'=W(W^*W)^{-1}\) is subnormal precisely when
\[
\frac{b-a}{c}\ge\lambda_*,\qquad
(8\lambda_*^2+13)e^{-2\pi\lambda_*}=5,
\qquad \lambda_*=0.1543920340043248\ldots.
\]
The equation defines one positive root. At equality the unique Berger density has exactly one zero in the open unit interval, at \(e^{-2\pi/c}\); above equality it is positive throughout that interval.

## Assumptions and scope

Parameters \(a,b,c\) are strictly positive real numbers. Indices start at \(n=0\). The operator acts on the complex Hilbert space \(\ell^2(\mathbb N_0)\). Subnormal means admitting a normal extension; for positive unilateral shifts it is equivalent to the existence of a positive Borel measure on \([0,1]\) representing all squared moments, since the Cauchy-dual weights are at most one. There is no claim of a classification for arbitrary quintics or arbitrary noncommensurate frequencies.

## Proof

**1. Polynomial shift and its moment sequence.** Each factor of \(P(x)\) is positive and strictly increasing for \(x\ge0\), so \(P(n+1)>P(n)\), and the ratio \(P(n+1)/P(n)\) approaches one. Consequently \(W\) is bounded and expansive, and its Cauchy dual has positive contractive weights \(\sqrt{P(n)/P(n+1)}\). Telescoping gives
\[
\|W^n e_k\|^2=\frac{P(n+k)}{P(k)},\qquad
\|(W')^n e_0\|^2=\frac{P(0)}{P(n)}.
\]
Because \(P\) has exact degree five with positive leading coefficient, its sixth forward difference vanishes identically while its fifth forward difference does not. This is exactly the strict \(6\)-isometry identity for the diagonal shift moments.

**2. Explicit signed moment representation.** Write \(\delta=b-a\) and \(d=3c/2\). The inverse Laplace transform of the two quadratic factors is
\[
G_c(t)=\frac{\sin(ct)/c-\sin(dt)/d}{d^2-c^2}
=\frac4{5c^3}\left(\sin(ct)-\frac23\sin(3ct/2)\right).
\]
Convolving with \(e^{-at}\) gives the unique integrable signed inverse-Laplace density
\[
H(t)=e^{-at}\int_0^t e^{-\delta u}G_c(u)\,du
=\frac4{5c^4}e^{-at}F_\lambda(ct),
\quad \lambda=\frac{\delta}{c},\quad
F_\lambda(y)=\int_0^y e^{-\lambda v}
\left(\sin v-\frac23\sin(3v/2)\right)dv.
\]
All factors are of exponential order with \(a,b>0\); in particular \(H\) is absolutely integrable. Laplace convolution yields \(\int_0^\infty e^{-nt}H(t)\,dt=1/P(n)\) for every nonnegative integer \(n\). Under \(x=e^{-t}\), the representing signed measure has density
\[
\rho(x)=\frac{4P(0)}{5c^4}x^{a-1}F_\lambda(-c\log x),
\qquad 0<x<1.
\]
The measure is finite, with total mass one and no endpoint atoms. Polynomials are dense in \(C([0,1])\), so two finite signed measures with these moments must coincide. Thus a positive representing measure exists if and only if \(F_\lambda(y)\ge0\) for all \(y\ge0\). This also gives necessity: a negative open interval in the explicit density cannot be replaced by another positive measure having the same moments.

**3. A global sign test reduces to one interior minimum.** Set
\[
g(y)=\sin y-\frac23\sin(3y/2)
=\frac23\sin(y/2)(1-\cos(y/2))(4\cos(y/2)+1).
\]
The function is \(4\pi\)-periodic. Its four successive sign regions on one period are \(+,-,+,-\); the nonendpoint sign-change zeros are \(2\arccos(-1/4)\), \(2\pi\), and \(4\pi-2\arccos(-1/4)\). Hence the only possible minima of \(F_\lambda\) on the closed first period are \(0,2\pi,4\pi\). The exact endpoint expression is
\[
F_\lambda(2\pi)
=\frac{1-e^{-2\pi\lambda}}{\lambda^2+1}
-\frac{1+e^{-2\pi\lambda}}{\lambda^2+9/4}
=\frac{5-(8\lambda^2+13)e^{-2\pi\lambda}}
{4(\lambda^2+1)(\lambda^2+9/4)}.
\]
For \(\lambda\le0\) this is strictly negative. For \(\lambda>0\), the integral over one full period is
\[
F_\lambda(4\pi)
=\big(1-e^{-4\pi\lambda}\big)
\frac{5}{4(\lambda^2+1)(\lambda^2+9/4)}>0.
\]
Put \(L_\lambda=5/[4(\lambda^2+1)(\lambda^2+9/4)]\). Periodicity and geometric summation give, for every integer \(m\ge0\) and \(u\in[0,4\pi]\),
\[
F_\lambda(4\pi m+u)
=L_\lambda\big(1-e^{-4\pi m\lambda}\big)
+e^{-4\pi m\lambda}F_\lambda(u).
\]
Thus, for \(\lambda>0\), the global nonnegativity condition is exactly \(F_\lambda(2\pi)\ge0\). The strictly increasing function
\[
\Phi(\lambda)=2\pi\lambda-\log((8\lambda^2+13)/5),
\quad \Phi'(\lambda)=2\pi-\frac{16\lambda}{8\lambda^2+13}>0
\]
starts negative at zero and tends to infinity. This proves the existence and uniqueness of \(\lambda_*\), the stated subnormality criterion, and the exact density-zero conclusion. Indeed \(F_\lambda\) has strictly signed derivative between its finitely many first-period critical points, while in later periods the positive first term in the preceding recurrence prevents another zero at the critical value.

## Verification

The standalone \(check.py\) uses only the Python standard library. It checks the inverse-Laplace antiderivative and endpoint formulas, the periodic recurrence, the trigonometric sign factorization, exact rational finite differences and moment telescoping, and numerical sign samples on both sides of the threshold. Run `python3 check.py`. All global-sign and infinite-moment conclusions follow from the displayed analytic identities; sampling is diagnostic, not an exhaustive positivity proof.

## Relationship to prior work

Reza and Zhang, *Hausdorff moment sequences induced by rational functions*, arXiv:1903.00116 (first public version 1 March 2019), establish general rational-moment machinery and classify lower-degree polynomials and selected quintic cases. Those theorems and the signed-density reduction are prior work. The present claim is a different, nonvertical quintic family with two distinct complex frequencies in the noninteger ratio \(3:2\), together with a necessary-and-sufficient sharp real-pole displacement threshold. Buchała, *\(m\)-isometric weighted shifts with operator weights*, arXiv:2407.17233 (first public version 24 July 2024), provides the broader polynomial-shift setting, not this threshold. Other exact subnormality thresholds for repeated complex factors do not imply this distinct-factor result.

## Limitations

The theorem is confined to two quadratic factors with a common real part and imaginary-frequency ratio \(3:2\), with strictly positive pole shifts. It neither classifies all quintic reciprocal-moment sequences nor handles general irrational frequency ratios. The analytic argument has not received independent mathematical validation. The literature comparison does not exclude a previously unindexed equivalent sharp threshold.

## References

1. Md. Ramiz Reza and Genkai Zhang, *Hausdorff moment sequences induced by rational functions*, arXiv:1903.00116, first version 1 March 2019. https://arxiv.org/abs/1903.00116
2. Michał Buchała, *\(m\)-isometric weighted shifts with operator weights*, arXiv:2407.17233, first version 24 July 2024. https://arxiv.org/abs/2407.17233
