# Half-density Gabor frames for linear Gaussian windows: complete phase and sharp anisotropic stability

## Finding

For every \(\beta>0\), \(a,b>0\) with \(ab=1/2\), and \(c\in\mathbb C\), let \(g_{\beta,c}(t)=(t-c)e^{-\beta t^2}\) and \(\mathcal G(g_{\beta,c};a,b)=\{e^{2\pi i mbt}g_{\beta,c}(t-na):m,n\in\mathbb Z\}\). Then

\[
\mathcal G(g_{\beta,c};a,b)\text{ is a frame for }L^2(\mathbb R)\quad\Longleftrightarrow\quad c\ne0.
\]

Thus any nonzero Gaussian component removes the first-Hermite failure at the exact exceptional redundancy-two lattice product, for every rectangular shape and Gaussian width.

There is a sharp quantitative refinement. Fix \(\beta=\pi\), \(a=1/2\), \(b=1\), and use the *unnormalized* window \(g_c(t)=(t-c)e^{-\pi t^2}\). If \(A(c)\) is the optimal lower Gabor frame bound, then, as \(c\to0\) in \(\mathbb C\),

\[
A(c)=C_R(\operatorname{Re}c)^2+C_I(\operatorname{Im}c)^2+O(|c|^4),
\]

where the following absolutely convergent series determine exact constants. For \(s\in\{0,1/2\}\), set
\[
E_s=\sum_{k\in\mathbb Z}e^{-\pi(k-s)^2},\qquad M_s=\sum_{k\in\mathbb Z}(k-s)^2e^{-\pi(k-s)^2},
\]
\[
f=(E_0,E_{1/2}),\quad u=(E_0-2\pi M_0,E_{1/2}-2\pi M_{1/2}),\quad
v=(-2\pi M_0,-2\pi M_{1/2}),\quad
\Delta=2\pi(E_{1/2}M_0-E_0M_{1/2}).
\]
Then
\[
C_R=\frac{\Delta^2}{\|u\|_2^2}=1.999916096270648\ldots,\qquad
C_I=\frac{\Delta^2}{\|v\|_2^2}=0.488151235193804\ldots.
\]
Both coefficients are strictly positive and unequal: instability at the odd-window boundary is phase sensitive.

## Assumptions and scope

Throughout, time and frequency modulations are \((T_x f)(t)=f(t-x)\) and \((M_\omega f)(t)=e^{2\pi i\omega t}f(t)\), and a frame has inequalities \(A\|f\|_2^2\le\sum_{m,n}|\langle f,M_{mb}T_{na}g\rangle|^2\le B\|f\|_2^2\) with \(0<A\le B<\infty\). The frame/no-frame statement applies for every real \(\beta>0\), every rectangular lattice with \(ab=1/2\), and every complex \(c\), without assuming smallness. The numerical leading coefficients refer only to \(\beta=\pi,a=1/2,b=1\) and the displayed unnormalized window. The order-four error is uniform with respect to the direction of \(c\) near zero.

## Proof

**1. Reduction and the exact Zak multiplier.** The unitary dilation replacing \(y=bt\) sends a lattice \((a,b)\) of product \(1/2\) to \((1/2,1)\), replacing \(\beta,c\) by \(\beta/b^2,bc\) and multiplying the window by a harmless nonzero scalar. It suffices to decide the frame property on the latter lattice. Define
\[
Zg(x,w)=\sum_{k\in\mathbb Z}g(x-k)e^{2\pi ikw}.
\]
Zak unitarity and Parseval in the two translation cosets show, with no omitted scalar factor, that its frame operator is multiplication by
\[
S_{\beta,c}(x,w)=|Zg_{\beta,c}(x,w)|^2+|Zg_{\beta,c}(x+1/2,w)|^2.
\]
The second term may use \(x-1/2\) instead, by quasi-periodicity. Since the window is Schwartz, this expression is continuous on the compact torus \((x\bmod1/2,w\bmod1)\). Consequently the frame property is equivalent to the absence of simultaneous zeros of its two Zak entries.

**2. Theta zero count.** Write \(F=Z(e^{-\beta t^2})\), \(P=Z(te^{-\beta t^2})\), and
\[
\Theta_\beta(u)=\sum_{k\in\mathbb Z}e^{-\beta k^2+2\beta ku},\qquad u=x+\frac{\pi i}{\beta}w.
\]
Then
\[
F(x,w)=e^{-\beta x^2}\Theta_\beta(u),\quad
P(x,w)=e^{-\beta x^2}\left(x\Theta_\beta(u)-\frac{\Theta_\beta'(u)}{2\beta}\right).
\]
The entire theta function satisfies \(\Theta_\beta(u+1)=e^{\beta+2\beta u}\Theta_\beta(u)\) and \(\Theta_\beta(u+\pi i/\beta)=\Theta_\beta(u)\). On a fundamental period rectangle whose boundary avoids zeros, the argument-principle integral of \(\Theta_\beta'/\Theta_\beta\) is \(2\pi i\): horizontal contributions cancel and the right-minus-left vertical contributions give \(2\beta(\pi i/\beta)\). Thus the function has exactly one zero per period cell, with multiplicity. Pairing terms indexed by \(k\) and \(1-k\) shows that this zero is \(u_*=1/2+\pi i/(2\beta)\). It is therefore simple. The zero of \(\Theta_\beta(u+1/2)\) is \(u=u_*-1/2\), a distinct point modulo the full period lattice.

**3. Complete common-zero classification.** If one of \(F(x,w)\), \(F(x+1/2,w)\) vanishes, its corresponding \(P\) does *not* vanish, because the theta zero is simple. Hence a common zero of \(P-cF\) at the two Zak sampling points can occur only when both Gaussian Zak values are nonzero. In this case both ratios \(P/F\) equal \(c\), which is equivalent to
\[
H_\beta(u):=\frac{\Theta_\beta'(u+1/2)}{\Theta_\beta(u+1/2)}-\frac{\Theta_\beta'(u)}{\Theta_\beta(u)}-\beta=0.
\]
This is elliptic with periods \(1\) and \(\pi i/\beta\). Its only two poles on the torus are simple, at the two distinct theta-zero classes, with opposite nonzero residues. Thus it has precisely two zeros on the torus counted with multiplicity. By evenness \(\Theta_\beta'(0)=0\), and by index reflection \(\Theta_\beta'(1/2)/\Theta_\beta(1/2)=\beta\). The quasi-periodic law gives \(\Theta_\beta'(1)/\Theta_\beta(1)=2\beta\). Hence \(H_\beta(0)=H_\beta(1/2)=0\), and these are its *only* zeros, both simple. At each of these two classes the corresponding ratio \(P/F\) equals zero. Therefore a simultaneous Zak zero is possible only for \(c=0\). Conversely for \(c=0\) both \(P(0,0)\) and \(P(1/2,0)\) vanish by symmetry. This proves the equivalence. In particular positivity and compactness of \(S_{\beta,c}\) give actual positive frame bounds for every \(c\ne0\), not only a pointwise nonvanishing assertion.

**4. Sharp stability near the singular window.** Now put \(\beta=\pi\), and let \(A(c)=\min_{x,w}S_{\pi,c}(x,w)\). The preceding classification shows that \(S_{\pi,0}\) has exactly one zero on the smaller torus, at \((x,w)=(0,0)\). Differentiating the Zak series at that point gives the vectors \(f,u,v\) defined in the finding and the Taylor expansion, for real \(x,w\) and complex \(c\),
\[
\binom{Zg_c(x,w)}{Zg_c(x+1/2,w)}=ux+ivw-cf+O((|x|+|w|+|c|)^2).
\]
The Hessian of \(S_{\pi,0}\) in \((x,w)\) is \(2\operatorname{diag}(\|u\|_2^2,\|v\|_2^2)\). Both diagonal entries are positive. Thus the implicit-function theorem and the unique isolated global zero give a unique real-analytic minimizer near zero, modulo torus periods, for all sufficiently small \(c\). Minimizing the quadratic part independently in \(x\) and \(w\) yields
\[
\bigl(\|f\|_2^2-(f\cdot u)^2/\|u\|_2^2\bigr)(\operatorname{Re}c)^2
+\bigl(\|f\|_2^2-(f\cdot v)^2/\|v\|_2^2\bigr)(\operatorname{Im}c)^2.
\]
In two real coordinates, both Schur complements equal the square of the corresponding determinant divided by the squared direction norm, and \(\det(f,u)=\det(f,v)=\Delta\). Positivity follows, for instance, from the strict estimates \(E_0>1\), \(E_{1/2}<1\), \(M_0<1/10\), \(M_{1/2}>1/5\), obtained by bounding the two-sided Gaussian tails; they force \(\Delta<0\). Reflection of the window satisfies \(g_{-c}(-t)=-g_c(t)\); since the lattice is reflection invariant, \(A(-c)=A(c)\). The real-analytic Taylor series therefore has no odd total-degree terms, sharpening the cubic remainder to \(O(|c|^4)\). This proves the sharp anisotropic expansion.

## Verification

The accompanying `CHECK.py` uses only the Python standard library. It tests finite theta quasi-period relations, the simple theta-zero location numerically, Zak-theta identities, reflection and half-period invariances, the exact moment-series coefficients, and the predicted leading quadratic values for small real and imaginary perturbations. The captured test program passed 162 finite numerical assertions. These checks support the bookkeeping and constant normalization; the infinite theta-zero count and the full frame statement are proved analytically above, not by numerical sampling.

## Relationship to prior work

Lemvig (arXiv:2611.05337, first posted 2026-11-03) gives a degree-dependent sufficient criterion for polynomial–Gaussian Gabor frames: at reduced rational lattice product \(p/q\), the guarantee requires \(q-p>\deg P\). The present degree-one case has \(p=1,q=2\), exactly the excluded boundary of that criterion. The paper does not give a quantitative lower-frame-bound expansion of the type above.

Lyubarskii and Nes (arXiv:1108.2684) prove the nonframe obstruction for odd windows on \(ab=(q-1)/q\), supplying the \(c=0\) direction. Liehr, Shafkulovska and Taylor (arXiv:2609.27846, Corollary 5.1) prove sufficiency for linear combinations of low Hermite functions under \(q\ge np+2\); for degree one at \(p=1,q=2\), their assumption fails. Ulanovskii and Zlotnikov (arXiv:2606.31450) establish the existence of nonframe polynomial–Gaussian windows at exactly this density; that existential statement does not classify nonzero constant terms or determine perturbation stability. The first-Hermite frame classification by Faulhuber and Petersen (arXiv:2609.02610) treats the pure Hermite window. The new assertion is the complete frame/nonframe phase along the first excluded hyperbola together with its exact anisotropic lower-bound leading term, not the underlying Zak criterion or the known odd-window obstruction.

## Limitations

No claims are made about products \(ab=(q-1)/q\) with \(q>2\), general polynomial degree above one, nonrectangular lattices, or global exact frame bounds at arbitrary nonzero \(c\). The stability constants apply solely to the explicitly normalized canonical rectangular lattice and Gaussian rate, and their numerical values are approximations to the exact moment-series definitions. As with any literature comparison, an equivalent older formulation under unsearched terminology cannot be entirely excluded; independent external scientific review has not been performed.

## References

1. J. Lemvig, *On the Gabor frame set of polynomial–Gaussian windows*, arXiv:2611.05337 (2026-11-03), https://arxiv.org/abs/2611.05337.
2. L. Liehr, I. Shafkulovska, and M. A. Taylor, *Derivatives of Theta Functions and a Problem of Lyubarskii and Nes*, arXiv:2609.27846 (2026-08-27), https://arxiv.org/abs/2609.27846.
3. A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450 (2026-06-30), https://arxiv.org/abs/2606.31450.
4. Y. Lyubarskii and P. G. Nes, *Gabor frames with rational density*, arXiv:1108.2684 (2011-08-12), https://arxiv.org/abs/1108.2684.
5. M. Faulhuber and F. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610 (2026-09-02), https://arxiv.org/abs/2609.02610.
