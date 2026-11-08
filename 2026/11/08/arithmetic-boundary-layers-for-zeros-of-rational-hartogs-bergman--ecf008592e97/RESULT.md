# Arithmetic boundary layers for zeros of rational Hartogs Bergman numerators

## Finding

Fix an integer \(k\ge2\). For every positive integer \(n\) with \(\gcd(n,k)=1\), put \(m=n+k\) and let \(Q_{m,n}\) be the standard reciprocal degree-\(2k\) numerator obtained on the oblique coordinate-product slice of the Bergman kernel of
\[
\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{m/n}<|z_2|<1\}.
\]
The normalization is precisely \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\), where the rational kernel numerator \(P_{m,n}\) is defined in [1, Theorem 1.3], or equivalently by the finite centered formula below. Write
\[
\omega_j=e^{2\pi i j/k},\qquad
h_j(m)\in\{1,\ldots,k-1\},\qquad
m h_j(m)\equiv j\pmod{k},\qquad 1\le j\le k-1.
\]
These inverses exist because \(\gcd(m,k)=1\). Define the positive constants
\[
\boxed{\displaystyle
\delta_{k,j,h}=
\sqrt{\frac{24\sin^4(\pi j/k)}{
[4+2\cos(2\pi j/k)]\sin^2(\pi h/k)}}.}
\]
Then, for all sufficiently large admissible \(n\), the polynomial has exactly \(k\) simple roots in the punctured unit disk. One is real negative and equals \(-2+\sqrt3+O_k(m^{-2})\). Each remaining interior root can be uniquely labeled by \(j=1,\ldots,k-1\) and has the **sharp, residue-dependent complex expansion**
\[
\boxed{\displaystyle
s_{m,j}=\omega_j\left(1-\frac{\delta_{k,j,h_j(m)}}{m}+O_k(m^{-2})\right).}
\]
The error is uniform over the finitely many admissible residue classes of \(m\) modulo \(k\) (for fixed \(k\)). In particular, along any fixed reduced residue class \(m\equiv a\pmod{k}\),
\[
\lim_{\substack{m\to\infty\\m\equiv a\ (\mathrm{mod}\ k)}}
 m(1-|s_{m,j}|)=\delta_{k,j,h},
\qquad ah\equiv j\pmod{k}.
\]
Each interior root is a genuine zero-product level of the Bergman kernel on the oblique slice; this is not a classification of the full two-variable zero variety.

For the first gap exhibiting a nonconstant residue dependence, \(k=5\), the root approaching \(e^{2\pi i/5}\) has two different radial constants: approximately \(1.3399720623\) when \(m\equiv1,4\pmod5\), and \(0.8281482785\) when \(m\equiv2,3\pmod5\). Thus the rate is not a function of the gap and angular index alone; the modular inverse of the denominator data is essential.

## Assumptions and scope

Throughout, \(k\) is fixed before \(n\to\infty\); no uniformity in growing \(k\) is asserted. Let \(W_m(A)=(m-|A|)_+\) for integers \(A\), with values zero outside \(|A|<m\). The exact polynomial, independently computable from [1, Theorem 1.3] and [2, Lemma 2.1], is
\[
Q_{m,n}(s)=\sum_{A,B\in\mathbb Z}W_m(A)W_m(nA+mB)s^{k+A+B}.
\]
The sum is finite; it is a reciprocal polynomial of degree \(2k\), with positive constant and leading terms. The coordinate products on the oblique slice satisfy \(s=t\in\mathbb D^*\); for \(m>n\) every such \(s\) is geometrically admissible and the Bergman-kernel denominator is nonzero there [1, Section 1.2.1]. The theorem concerns the interior zeros of this one-variable numerator for **sufficiently large** \(n\), not every finite case or the whole kernel zero locus.

## Proof

**1. Uniform second-order coefficient limit.** For \(-k\le r\le k\), write \(c_{m,k,r}\) for the coefficient of \(s^{k+r}\). Substituting \(B=r-A\) gives the exact integer sum
\[
c_{m,k,r}=\sum_{A\in\mathbb Z}W_m(A)W_m(mr-kA).
\]
With \(f_{k,r}(x)=(1-|x|)_+(1-|r-kx|)_+\), this becomes \(m^2\sum_A f_{k,r}(A/m)\). This compactly supported function is continuous and piecewise quadratic, and its first derivative has bounded variation, uniformly for each fixed \(k\) and the finitely many \(r\). The composite trapezoidal estimate for functions with derivative of bounded variation follows, for example, by expressing their distributional second derivative as a finite signed measure and applying the bounded trapezoidal-error kernel to each hinge. Because the endpoint values vanish,
\[
\frac1m\sum_A f_{k,r}(A/m)=\int_{\mathbb R}f_{k,r}(x)\,dx+O_k(m^{-2}).
\]
The integral can be evaluated by splitting at \(x=0\) and \(kx=r\pm1\):
\[
6k^2\int_{\mathbb R}f_{k,r}(x)\,dx=
\begin{cases}
1,&|r|=k,\\
6(k-|r|),&1\le|r|<k,\\
6k-2,&r=0.
\end{cases}
\]
The same numbers are precisely the coefficients, centered at degree \(k\), of
\[
P_k(s)=(s^2+4s+1)(1+s+\cdots+s^{k-1})^2.
\]
Indeed, the squared geometric sum has triangular coefficients \(k-|r|\); convolution with \((1,4,1)\) yields the displayed cases. Thus
\[
\boxed{\frac{6k^2}{m^3}Q_{m,n}(s)=P_k(s)+O_k(m^{-2})}
\]
coefficientwise and locally uniformly in \(s\), with the same control for any fixed number of derivatives. This limit also follows by the elementary finite formula in [1], but the quadrature argument is used here to control its **second-order error**, which is essential for the sharp root displacement.

**2. Exact value at each nontrivial root of unity.** Write \(T_m(u)=|\sum_{a=0}^{m-1}e^{iau}|^2\), and let \(F_m(\theta)=e^{-ik\theta}Q_{m,n}(e^{i\theta})\). In the centered coefficient formula replace \(nA+mB\) by \(V\); the relation \(V\equiv nA\pmod m\) can be imposed by finite Fourier orthogonality. Expanding \(T_m\) then gives the exact identity
\[
F_m(\theta)=\frac1m\sum_{\ell=0}^{m-1}
T_m\!\left(\frac{k\theta-2\pi n\ell}{m}\right)
T_m\!\left(\frac{\theta+2\pi\ell}{m}\right).
\]
This Fejér-product formula is also present in [2, Lemma 3.1]; here it follows directly from the definition above, without assuming any unproved zero-location theorem. Put \(\theta_j=2\pi j/k\). The first Fejér factor vanishes except at the unique \(\ell\in\{0,\ldots,m-1\}\) satisfying \(n\ell\equiv j\pmod m\), where its value is \(m^2\). Since \(n=m-k\), one has \(k\ell+j=mh\) for the unique \(h=h_j(m)\in\{1,\ldots,k-1\}\). The geometric-sum identity for the second factor yields
\[
\boxed{\displaystyle
F_m(\theta_j)=m\frac{\sin^2(\pi j/k)}{\sin^2(\pi h_j(m)/k)}.}
\]
This equality is exact for every admissible \(m\), and is the arithmetic information not visible in the leading coefficient limit.

**3. Microscopic splitting.** Normalize \(H_m(\theta)=6k^2 F_m(\theta)/m^3\). By Step 1, this converges with derivatives at rate \(O_k(m^{-2})\), on bounded complex \(\theta\)-sets, to
\[
G_k(\theta)=[4+2\cos\theta]
\left(\frac{\sin(k\theta/2)}{\sin(\theta/2)}\right)^2,
\]
with removable singularities understood. For \(1\le j\le k-1\), \(G_k\) has a double zero at \(\theta_j\), and
\[
G_k(\theta_j+v)=a_{k,j}v^2+O_k(v^3),\qquad
 a_{k,j}=\frac{[4+2\cos(2\pi j/k)]k^2}{4\sin^2(\pi j/k)}>0.
\]
In particular \(H_m'(\theta_j)=O_k(m^{-2})\), while Step 2 gives the **exact** value of \(m^2H_m(\theta_j)\). Therefore, for bounded complex \(u\),
\[
m^2H_m(\theta_j+u/m)
=a_{k,j}u^2+6k^2\frac{\sin^2(\pi j/k)}{\sin^2(\pi h_j(m)/k)}+O_k(m^{-1}),
\]
locally uniformly in \(u\). The quadratic on the right has two simple zeros \(u=\pm i\delta_{k,j,h_j(m)}\). There are finitely many residue classes of \(m\) modulo \(k\), so the complex analytic implicit-root argument (or Rouché's theorem on uniformly small circles about those simple zeros) gives corresponding zeros \(u_{\pm,m}=\pm i\delta_{k,j,h_j(m)}+O_k(m^{-1})\). The upper root \(u_{+,m}\), under \(s=e^{i(\theta_j+u/m)}\), is inside \(|s|<1\) and satisfies
\[
s_{m,j}=\omega_j\left(1-\delta_{k,j,h_j(m)}/m+O_k(m^{-2})\right).
\]
The lower root is outside, and both are simple for large enough \(m\). This proves both the sharp radius and the absence of first-order angular drift.

**4. Counting all interior roots.** The limit polynomial \(P_k\) has two simple roots \(-2\pm\sqrt3\), and has a double root at every nontrivial \(k\)-th root of unity. There are \(2+2(k-1)=2k\) roots, counted with multiplicity. By Step 1 and Rouché's theorem, for large \(m\) the two simple roots persist at \(-2\pm\sqrt3+O_k(m^{-2})\). Step 3 places exactly one simple root inside and one outside near each nontrivial root of unity. These account for all \(2k\) roots of \(Q_{m,n}\). Hence the asserted \(k\) interior roots are simple, including the unique negative real one. No finite numerical root census is used to prove this count.

## Verification

The accompanying `CHECK.py` reconstructs \(Q_{m,n}\) independently from [1, Theorem 1.3] and from the centered tent-product formula, verifies reciprocity and the identity \(Q_{m,n}(1)=m^3\) for finite coprime parameter grids, checks the exact root-of-unity evaluation at high precision, checks the coefficient-limit scaling, and numerically compares the claimed radial coefficients across several modular residue classes. Running `python CHECK.py` with the versions specified in `requirements.txt` produced **1,544 passed finite assertions**. The proof for all fixed \(k\) and sufficiently large \(n\) is Steps 1–4, not the finite checks.

## Relationship to prior work

Edholm and Mathew [1] provide the exact rational Hartogs kernel, reciprocal oblique-slice polynomial, and explicit limiting descriptions for the gaps one and two (especially Remark 4.18). An existing gap-three calculation [3] gives the sharp constant \(\sqrt6\) for that one gap. The previously available fixed-gap coefficient limit gives only \(O_k(m^{-1})\) localization near roots of unity, not the first-order coefficient or its dependence on the residue of \(m\) modulo \(k\). The present theorem obtains the full all-gap sharp first-order formula and uncovers nontrivial residue dependence already at gap five. Deng and Fu [2], first published November 5, 2026, prove positivity and zero counts for all finite coprime gaps. This subsequent work supplies a relevant comparison and the credited Fejér identity. Their full-text theorem and proof do not state the sharp residue-dependent radial boundary layer. The finite Fourier identity in Step 2 is credited to [2], while the limiting and splitting argument is supplied here.

## Limitations

This is a fixed-gap asymptotic; the unspecified \(O_k\) constants need not remain bounded with increasing \(k\). It does not locate all kernel zeros off the oblique slice, classify finite-parameter multiplicities, or determine the next-order drift. The first-order constants are indexed by the actual congruence class; in general a single unrestricted limit as \(m\to\infty\) does not exist for an individual angular label. No independent scientific audit or complete global publication-priority certificate has been performed.

## References

1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489, first public version May 26, 2025; *Mathematische Zeitschrift* 313 (2026), article 43. Relevant: Theorem 1.3, Section 1.2.1, equations (3.21), Sections 4.1–4.3, Remark 4.18. https://arxiv.org/abs/2505.20489
2. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480, November 5, 2026. Relevant: centered coefficient formula (2.5), Fejér product identity (3.5), Theorem 1.1. This later publication is used for comparison and attribution, not as the motivating source. https://arxiv.org/abs/2611.07480
3. *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cubic-root-condensation-of-diagonal-bergman-kernel-zeros-in-gap--78891bb4627f (full RESULT.md inspected).
