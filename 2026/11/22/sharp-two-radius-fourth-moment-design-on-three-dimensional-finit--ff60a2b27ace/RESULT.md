# Sharp two-radius fourth-moment design on three-dimensional finite-field spheres

## Finding

Let \(q\) be an odd prime power, \(G=\mathbb F_q^3\), and \(Q(x)=x_1^2+x_2^2+x_3^2\). For each nonzero field element \(a\), let \(S_a=\{x\in G:Q(x)=a\}\). Choose **distinct nonzero** \(a,b\), put \(S=S_a\cup S_b\), and let \(\mu=\mathbf1_S/|S|\). The normalized fourth Fourier moment

\[
\mathcal R_q(a,b)=q^{-3}\sum_{\xi\in G}|\widehat\mu(\xi)|^4
=\frac{\mathcal E(S)}{|S|^4}
=\mathbb P(X_1+X_2+X_3+X_4=0),
\]

where the independent increments \(X_i\) are uniformly distributed on \(S\), is minimized **exactly** as follows:

\[
\boxed{\min_{a,b\in\mathbb F_q^\times,\ a\ne b}\mathcal R_q(a,b)
=\begin{cases}
353/43200,&q=5,\\
913/648000,&q=9,\\
(8q^2+3q-8)/(8q^5),&q=3,\ q=7,\ \text{or }q\ge11.
\end{cases}}
\]

Here and below, \(\chi\) is the quadratic character, with \(\chi(0)=0\). The complete equality classification is:

- At \(q=5\), the unique unordered minimizing pair has \(\chi(-a)=\chi(-b)=1\), namely \(\{a,b\}=\{1,4\}\).
- At \(q=9\), the minimizing pairs are exactly the six unordered pairs satisfying \(\chi(-a)=\chi(-b)=1\).
- At \(q=3\), \(q=7\), and every odd prime power \(q\ge11\), all and only the pairs with \(\chi(-a)=-\chi(-b)\) minimize. There are \(((q-1)/2)^2\) such unordered pairs.

Thus the optimal two-radius Fourier-flatness/return design switches character types in precisely the two exceptional field orders \(5\) and \(9\). A secondary arithmetic phenomenon is a positive tangency correction when one radius is nine times the other.

## Assumptions and scope

The dimension is three; the quadratic form is the standard nondegenerate sum of three squares over an **odd** field. A radius here means the field value \(a=Q(x)\), not a selected square root. Both radii are required to be nonzero and distinct. The Fourier convention is \(\widehat f(\xi)=\sum_{x\in G}f(x)\psi(-x\cdot\xi)\) for any fixed nontrivial additive character \(\psi\). All finite field orders (including extension fields and characteristic three) are included. The optimization varies only the unordered pair of radii, with the resulting probability measure uniform on the **union**; it does not vary independent weights on the two component spheres or optimize a general Fourier extension operator.

## Proof

**1. Exact pair-convolution from quadratic geometry.** Put \(r=\mathbf1_S*\mathbf1_S\), \(u=\chi(-a)\), \(v=\chi(-b)\), and \(c=u+v\). The standard three-dimensional quadratic count gives \(|S_a|=q^2+qu\), hence \(|S|=2q^2+qc\). For \(x\ne0\) of nonzero norm \(s=Q(x)\), a pair of radii \(i,j\) requires \(y\cdot x=(s+i-j)/2\), leaving a nondegenerate binary quadratic equation on \(x^\perp\) with right-hand side \(-\Delta_{ij}(s)/(4s)\), where

\[\Delta_{ij}(s)=(s+i-j)^2-4is.\]

Its solution count is \(q-\chi(-s)+q\chi(-s)\mathbf1_{\{\Delta_{ij}(s)=0\}}\). In the zero-norm nonzero case, a Witt basis gives \(q\) solutions for \(i\ne j\) and \(q(1+\chi(-i))\) for \(i=j\). Consequently, with \(\sigma_s=\chi(-s)\) and

\[
\alpha_s=\mathbf1_{\{s=4a\}}+\mathbf1_{\{s=4b\}}
+2\mathbf1_{\{(s+a-b)^2=4as\}},
\]

\[
r(x)=\begin{cases}
2q^2+qc,&x=0,\\
q(4+c),&x\ne0,\ Q(x)=0,\\
4(q-\sigma_s)+q\sigma_s\alpha_s,&Q(x)=s\ne0.
\end{cases}
\]

Each nonzero norm \(s\) has \(q^2+q\sigma_s\) vector representatives, and there are \(q^2-1\) nonzero isotropic vectors.

**2. The exact energy and the tangency resonance.** Write \(t=\chi(ab)\) and define

\[
H(a,b)=\mathbf1_{\{b=9a\}}+\mathbf1_{\{a=9b\}}.
\]

When the characteristic is three, \(H=0\); when \(H\ne0\), \(u=v\), since nine is a square. The mixed discriminant \((s+a-b)^2-4as\) has two distinct, nonzero roots precisely if \(t=1\). Its roots coincide with \(4a\) or \(4b\) precisely at the two indicated ninefold relations. Directly summing these finitely supported correction terms gives

\[
\sum_{s\ne0}\sigma_s\alpha_s=3c,\qquad
\sum_{s\ne0}\alpha_s^2=6+4t+4H,\qquad
\sum_{s\ne0}\sigma_s\alpha_s^2=5c+4uH.
\]

Insert the convolution formula into \(\mathcal E(S)=\sum_xr(x)^2\) and use \(\sum_{s\ne0}\sigma_s=0\). This yields the exact identity

\[
\begin{aligned}
\mathcal E(S)={}&16(q-1)(q^4-q^2)+q^2(q^2-1)(4+c)^2+(2q^2+qc)^2\\
&+24q^2(q^2-1)c+q^4(6+4t)+5q^3c+4q^3(q+u)H.
\end{aligned}
\]

In particular, the three quadratic-character regimes simplify to

\[
\mathcal E(S)=\begin{cases}
2q^2(q-1)(8q^2-15q-32)+4q^3(q-1)H,&u=v=-1,\\
2q^3(8q^2+3q-8),&u=-v,\\
2q^2(q+1)(8q^2+33q-32)+4q^3(q+1)H,&u=v=1.
\end{cases}
\]

The ninefold term is nonnegative in every case. It is not discarded in the small-field comparison.

**3. Global minimization and all equality cases.** Divide the three baseline expressions (setting \(H=0\)) by the respective fourth powers \((2q(q-1))^4\), \((2q^2)^4\), and \((2q(q+1))^4\), and denote the results by \(R_-\), \(R_0\), and \(R_+\). A direct exact subtraction gives

\[
R_- -R_0=\frac{6q^4-39q^3-25q^2+27q-8}{8q^5(q-1)^3},
\qquad
R_+ -R_0=\frac{6q^4-57q^3+7q^2+21q+8}{8q^5(q+1)^3}.
\]

Both differences are strictly positive for every \(q\ge11\). Indeed, the two numerator polynomials are positive term-by-term after grouping their first two terms as \(q^3(6q-39)\) and \(q^3(6q-57)\), respectively, and in the former case \(q^3(6q-39)>25q^2\) for \(q\ge11\). Therefore the mixed-character regime wins uniquely in character type for all \(q\ge11\), and its \(H\) is automatically zero.

For the smaller possible odd field orders, exhaustive **symbolic** evaluation of these formulas (not an appeal to finite testing) completes the proof. The field \(\mathbb F_3\) has only one unordered nonzero-radius pair, which is mixed. In \(\mathbb F_5\), the two same-sign radii in either sign class are related in both directions by multiplication by nine, so \(H=2\); the exact minimum is \(353/43200\) in the positive sign class, below mixed value \(207/25000\) and negative value \(113/12800\). In \(\mathbb F_7\), each three-element sign class is cycled by multiplication by nine, so every same-sign pair has \(H=1\); the two same-sign values are \(269/84672\) and \(605/200704\), both strictly above the mixed value \(405/134456\). In \(\mathbb F_9\), characteristic three makes \(H=0\); its positive, mixed, and negative values are respectively \(913/648000\), \(667/472392\), and \(481/331776\), with the positive one strictly smallest. These exhaust the prime-power orders below eleven. This proves the minimum and every equality case.

Finally, since \(S=-S\), Fourier orthogonality gives \(q^{-3}\sum_\xi|\widehat\mu(\xi)|^4=\sum_x(\mu*\mu)(x)^2=(\mu^{*4})(0)\), establishing both interpretations of the optimized quantity.

## Verification

The standalone standard-library script `checker.py` directly enumerates the entire ordered two-sum convolution, checks its value **at every target** against the formula in Step 1, and checks the closed energy in Step 2. It covers every unordered distinct radius pair over prime fields of orders 3, 5, 7, and 11 and every pair over \(\mathbb F_9\), plus one representative of each available character/resonance class in \(\mathbb F_{25}\). It also independently compares the observed small-field minimum and equality character classes with the theorem. Run from the extracted package with `python3 checker.py`. Finite enumerations provide regression tests only; the proof above establishes all odd prime powers.

## Relationship to prior work

Pham and Xue (2026) prove sharp \(L^p\to L^4\) extension exponents for **one** nonzero-radius sphere in odd dimension and discuss additive-energy methods; those exponents do not optimize the normalized constant-input fourth moment over a union of two spheres. Brittenham and Pakianathan (2024) and earlier work on finite Euclidean association schemes provide the **general intersection-number machinery**, so the existence and derivability of component convolution counts are not claimed as new. Their random-walk return application concentrates on one-radius planar walks; neither inspected work states the all-field optimal *pair of nonzero radii*, the exceptional orders five and nine, or the exact ninefold-tangency corrections in the normalized comparison. The claimed contribution is the sharp optimization and equality classification, not a novel general association-scheme convolution formula.

## Limitations

The result is for the standard quadratic form in dimension three and the equal-per-point law on an unweighted union of exactly two **nonzero distinct** spheres. It says nothing about weighted mixtures, three or more radii, general \(L^p\to L^4\) norms, higher dimension, or characteristic two. A previously overlooked special case in historical association-scheme literature could yield the same optimum and remains the principal novelty risk. Computational checks cover the stated finite fields, not the infinite family.

## References

- T. Pham and B. Xue, *Sharp spherical \(L^p\to L^4\) extension estimates over finite fields in odd dimensions*, arXiv:2610.29664v1 (first public 2026-10-21), https://arxiv.org/abs/2610.29664.
- C. Brittenham and J. Pakianathan, *Random walks and the “Euclidean” association scheme in finite vector spaces*, arXiv:2401.04814 (2024), *Canadian Journal of Mathematics* 77 (2025), 1664–1685, https://doi.org/10.4153/S0008414X24000518.
