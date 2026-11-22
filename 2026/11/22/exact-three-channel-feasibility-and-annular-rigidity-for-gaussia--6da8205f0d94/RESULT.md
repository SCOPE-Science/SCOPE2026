# Exact three-channel feasibility and annular rigidity for Gaussian Gabor concentration

## Finding

Fix the unit Gaussian short-time Fourier transform and its first three normalized Hermite inputs. Among **all** measurable radial attenuators taking values in \([0,1]\), the set of their three *labelled* captured energies is given below in elementary implicit form, with unique bang–bang boundary attenuators and exact stability identities. This is a simultaneous three-channel statement, not an assertion about the ordered eigenvalues of a single localization operator.

Write the radial attenuator as \(M(z)=h(\pi|z|^2)\), where \(h:[0,\infty)\to[0,1]\) is measurable, and put
\[
\lambda_j(h)=\int_0^\infty h(x)e^{-x}\frac{x^j}{j!}\,dx,\qquad j=0,1,2.
\]
Every feasible triple \((p,q,r)=(\lambda_0,\lambda_1,\lambda_2)\) is precisely as follows.

At the endpoints, \(p=0\) gives \((0,0,0)\) and \(p=1\) gives \((1,1,1)\). For \(0<p<1\), define
\[
q_-(p)=p+(1-p)\log(1-p),\qquad q_+(p)=p(1-\log p).
\]
Then \(q_-\le q\le q_+\) is necessary and sufficient for a first-two-channel pair. For any such pair, let \(u=u(p,q)\in[p,1]\) be the **unique** solution of
\[
u(1-\log u)-(u-p)(1-\log(u-p))=q,
\]
with the continuous convention \(0\log0=0\). Set \(a=-\log u\) and \(b=-\log(u-p)\), allowing \(b=+\infty\) if \(u=p\). Define the single-interval third-channel functional
\[
R(p,q)=\frac12\left[e^{-a}(a^2+2a+2)-e^{-b}(b^2+2b+2)\right],
\]
where the \(+\infty\) endpoint contributes zero. **The full feasible set** is
\[
\boxed{\quad R(p,q)\le r\le 1-R(1-p,1-q).\quad}
\]
Every \(r\) in this closed interval is attained by a radial \([0,1]\)-valued attenuator.

The **unique** minimizer (up to measure-zero changes) at fixed \((p,q)\) is \(h_-=\mathbf1_{[a,b]}\), i.e. one circular annulus, with a disk and an exterior region allowed as boundary cases. The **unique** maximizer is \(h_+=1-\mathbf1_{[c,d]}\), where \([c,d]\) is the interval corresponding to \((1-p,1-q)\); geometrically, it is the union of a central disk and an exterior region (with degenerate boundary cases). For \(q_-<q<q_+\), both intervals are finite with strictly positive endpoints and all two boundaries are simple, and one has the **exact sharp stability identities**
\[
\begin{aligned}
r-R(p,q)&=\frac12\int_0^\infty |(x-a)(x-b)|\,|h(x)-h_-(x)|e^{-x}\,dx,\\
1-R(1-p,1-q)-r&=\frac12\int_0^\infty |(x-c)(x-d)|\,|h(x)-h_+(x)|e^{-x}\,dx.
\end{aligned}
\]
The identities hold for every measurable \(0\le h\le1\) with the prescribed \((p,q)\); they give exact weighted distances to the unique boundary masks. On the two edges of the feasible \((p,q)\)-lens the allowable \(r\)-interval collapses to a point.

For instance, at \(p=q=1/2\) one has \(a=0.4355516736868111\ldots\), \(b=1.9179508713019047\ldots\), and
\[
0.2911583219888445\ldots\le r\le0.7088416780111555\ldots.
\]

## Assumptions and scope

Use the normalized Gaussian \(\varphi(t)=2^{1/4}e^{-\pi t^2}\), normalized Hermite functions \(h_j\) (with \(h_0=\varphi\)), and the short-time Fourier transform \(V_\varphi h_j\). Their squared magnitudes are \(e^{-\pi|z|^2}(\pi|z|^2)^j/j!\). A radial attenuator \(M:\mathbb R^2\to[0,1]\) has no fixed-area condition; the first two responses \((p,q)\) supply its two constraints. Traces are labelled by the input \(h_j\), not sorted by size. Equalities and uniqueness are understood modulo Gaussian measure-zero changes.

## Proof

**Step 1 (exact reduction).** In the Bargmann transform, the normalized Hermite \(h_j\) corresponds to \(z^j/\sqrt{j!}\). The Gaussian spectrogram identity and polar substitution \(x=\pi|z|^2\), \(dx=2\pi|z|\,d|z|\) (equivalently the plane-area element integrated over the polar angle is \(dx\)), give the stated Gamma-density moments. Consequently \(\lambda_j(1)=1\) for each \(j\).

**Step 2 (two-channel lens).** Let \(p=\int he^{-x}\,dx\in(0,1)\). Among all \(0\le h\le1\) with mass \(p\), the first moment \(q=\int xhe^{-x}\,dx\) is minimized by the disk profile \(h=\mathbf1_{[0,T]}\) with \(T=-\log(1-p)\), and maximized by the tail profile \(h=\mathbf1_{[S,\infty)}\) with \(S=-\log p\). Indeed, the signed integrands \((x-T)(h-\mathbf1_{[0,T]})\) and \((x-S)(\mathbf1_{[S,\infty)}-h)\) are pointwise nonnegative; their constant parts integrate to zero because masses agree. Integrating gives exactly \(q_-\) and \(q_+\). Equality forces the respective profile almost everywhere.

**Step 3 (annulus interpolates all feasible pairs).** Fix \(p\) and let \(u=e^{-a}\in[p,1]\), \(v=e^{-b}=u-p\). The interval \([a,b]\) has zero-th moment \(u-v=p\) and first moment
\[
q=u(1-\log u)-v(1-\log v).
\]
The derivative with respect to \(u\) in \((p,1)\) is \(\log(v/u)<0\). At \(u=p\), this equals \(q_+\); at \(u=1\), it equals \(q_-\). Thus there is exactly one interval realizing every admissible pair, including endpoints by continuity.

**Step 4 (sharp third moment and rigidity).** For the interval \([a,b]\), put \(P(x)=(x-a)(x-b)\). It is nonpositive inside the interval and nonnegative outside. For any competing \(h\) with the same zero-th and first moments, the affine terms in \(P\) vanish on integration, so
\[
\begin{aligned}
\lambda_2(h)-\lambda_2(h_-)
&=\tfrac12\int_0^\infty (h-h_-)P(x)e^{-x}\,dx\\
&=\tfrac12\int_0^\infty |h-h_-|\,|P(x)|e^{-x}\,dx\ge0.
\end{aligned}
\]
At interior \((p,q)\), both roots are finite and distinct, so equality forces \(h=h_-\) almost everywhere. Evaluating \(\frac12\int_a^b x^2e^{-x}\,dx\) gives \(R(p,q)\). For boundary pairs, the unique masks from Step 2 give the same result by continuity.

**Step 5 (upper boundary).** The complementary profile \(g=1-h\) has \((\lambda_0(g),\lambda_1(g),\lambda_2(g))=(1-p,1-q,1-r)\). Applying Step 4 to \(g\) gives \(1-r\ge R(1-p,1-q)\), yielding the upper bound with unique maximizer \(h_+=1-\mathbf1_{[c,d]}\). Applying the exact equality in Step 4 to \(g\) gives the second stated gap identity. The minimum and maximum have the same \((p,q)\), and every intermediate value \(r\) is obtained from the convex interpolation \((1-\theta)h_-+\theta h_+\), \(0\le\theta\le1\). This finishes the necessity, sufficiency, and both rigidity assertions.

## Verification

`checker.py` is standalone Python 3 code (standard library only). It integrates elementary exponential tail moments of 147 explicitly specified bounded step masks, tests the necessary and sufficient inequalities, and evaluates both exact weighted gap identities for 146 interior masks. The maximal gap-identity discrepancy in IEEE double precision was \(7.50\times10^{-16}\). The script also independently checks the symmetric numerical example. These are finite diagnostics, not substitutes for the all-measurable-mask proof in Steps 1–5.

## Relationship to prior work

Nicola–Tilli (2021) prove the Faber–Krahn inequality for Gaussian short-time Fourier localization, optimizing over sets and signals with a single concentration objective. Nicola–Riccardi–Tilli (2025) study ordered Toeplitz eigenvalues and their partial sums for prescribed area, including optimal annuli for the second *ordered* eigenvalue. Neither comparison supplies the conditional three-dimensional feasible set of the first three *labelled* Hermite channels when the first two responses are fixed, nor the two exact stability identities. Esmeral García–Maximenko (2025) develop approximation of radial Fock Toeplitz eigenvalue sequences, with no positive bounded-mask conditional three-channel region. The interval/complement extremizer mechanism is compatible with classical constrained-moment or bathtub principles; **the general bang–bang mechanism is not claimed as new**. The contribution is the complete specialized exponential-moment region, its explicit unique boundary parametrization, and its exact two-sided rigidity deficits.

## Limitations

The theorem concerns radial masks \(0\le M\le1\), not arbitrary nonradial masks, signed masks or fixed-area subsets. Its channels are labelled Hermite responses, not the three largest eigenvalues. The formulas involve one unique scalar inverse rather than an elementary closed form for the inverse. The quadratic gap identities require interior \((p,q)\); boundary pairs have unique masks instead. The full historical-priority check is best-knowledge, with general moment-space literature and partly inaccessible indexed results as residual risks. No independent mathematical audit has been performed.

## References

- F. Nicola and P. Tilli, *The Faber–Krahn inequality for the Short-time Fourier Transform*, arXiv:2106.03423v1 (7 June 2021), https://arxiv.org/abs/2106.03423.
- F. Nicola, F. Riccardi, and P. Tilli, *The Isoperimetric Inequality for Partial Sums of Toeplitz Eigenvalues in the Fock Space*, arXiv:2503.07069 (10 March 2025), https://arxiv.org/abs/2503.07069.
- M. Esmeral García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276 (2025), https://arxiv.org/abs/2503.23276.
- G. Winkler, *Moment Sets of Bell–Shaped Distributions: Extreme Points, Extremal Decomposition and Chebysheff Inequalities*, Mathematische Nachrichten **215** (2000), 161–184, https://doi.org/10.1002/1522-2616(200007)215:1%3C161::AID-MANA161%3E3.0.CO;2-A (background constrained-moment framework; abstract inspected).
