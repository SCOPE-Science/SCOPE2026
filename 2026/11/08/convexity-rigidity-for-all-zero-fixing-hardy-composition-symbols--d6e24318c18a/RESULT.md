# Convexity rigidity for all zero-fixing Hardy composition symbols

## Finding

**Theorem (complete convexity classification).** Let \(\phi:\mathbb D\to\mathbb D\) be holomorphic with \(\phi(0)=0\). Let \(C_\phi f=f\circ\phi\) act on the classical Hardy space \(H^2(\mathbb D)\), and let its normalized-kernel Berezin transform and range be
\[
\mathcal B_\phi(z)=\frac{1-|z|^2}{1-\overline z\phi(z)},\qquad \operatorname{Ber}(C_\phi)=\mathcal B_\phi(\mathbb D).
\]
Then
\[
\boxed{\operatorname{Ber}(C_\phi)\text{ is convex}\iff\phi(z)=cz\text{ for some real }-1\le c\le1.}
\]
For \(c=1\) the range is \(\{1\}\), and for all real \(-1\le c<1\) it is exactly \((0,1]\).

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The standard Szegő kernel is \(k_z(w)=(1-\overline zw)^{-1}\), normalized by \(\widehat k_z=\sqrt{1-|z|^2}\,k_z\). The chosen inner product is linear in the first variable; this gives the displayed formula. The symbol fixes zero, so Littlewood subordination makes \(C_\phi\) bounded. Convexity is literal convexity of the image set, not of its closure.

## Proof

**1. Ratio function and localization at the distinguished endpoint.** Schwarz's lemma gives \(|\phi(z)|\le|z|\). Thus \(A(z)=\phi(z)/z\), analytically continued at zero by \(A(0)=b=\phi'(0)\), is a holomorphic disk-valued function with \(|A|\le1\). Writing \(t=|z|^2\),
\[
\mathcal B_\phi(z)=\frac{1-t}{1-tA(z)},\qquad 1-\mathcal B_\phi(z)=\frac{t(1-A(z))}{1-tA(z)}.
\]
Also \(|\mathcal B_\phi(z)|\le (1-t)/(1-t|A(z)|)\le1\).

We first show that for \(b\ne1\), \(\mathcal B_\phi(z_j)\to1\) forces \(z_j\to0\). If \(|b|<1\), Schwarz–Pick gives, at \(r=|z|\),
\[
1-|A(z)|\ge\frac{(1-|b|)(1-r)}{1+|b|r},\qquad
\frac{|1-A(z)|}{1-r^2}\ge c_b:=\frac{1-|b|}{2(1+|b|)}>0.
\]
The denominator estimate \(|1-tA|\le(1-t)+t|1-A|\) therefore yields
\[
|1-\mathcal B_\phi(z)|\ge\frac{tc_b}{1+tc_b}.
\]
If \(|b|=1\) and \(b\ne1\), the maximum-modulus principle yields \(A\equiv b\) and instead \(|1-\mathcal B_\phi(z)|\ge t|1-b|/2\). These estimates prove the localization assertion. If \(b=1\), Schwarz's lemma directly gives \(\phi(z)=z\), settling that case.

**2. Convexity forces a single line, then a linear symbol.** Suppose \(b\ne1\) and the Berezin range is convex. Uniformly in the angle as \(z\to0\),
\[
\mathcal B_\phi(z)=1+(b-1)|z|^2+O(|z|^3).
\]
Take any \(w\in\operatorname{Ber}(C_\phi)\setminus\{1\}\). Every \(1+s(w-1)\), \(0<s<1\), lies in the range by convexity. Such values converge to one as \(s\downarrow0\); by step 1 their preimages converge to zero. Comparing the normalized direction with the local expansion forces \((w-1)/(b-1)\) to be a nonnegative real number. Hence the entire Berezin range is contained in a fixed real affine line \(L=1+\mathbb R(b-1)\).

Fix \(0<r<1\). The function \(F_r(\zeta)=(1-r^2)/(1-r^2A(\zeta))\) is holomorphic on the disk. On \(|\zeta|=r\), it equals \(\mathcal B_\phi(\zeta)\), which belongs to \(L\). A real-linear functional perpendicular to \(L\) is harmonic when applied to \(F_r\); its boundary values on this circle are constant. The harmonic maximum principle makes it constant throughout \(|\zeta|<r\). By the open mapping theorem, \(F_r\) must be constant there, and therefore \(A\) is constant on that disk. Analytic continuation gives \(A\equiv b\), i.e. \(\phi(z)=bz\).

For such a linear symbol with \(b\ne1\), \(\mathcal B_\phi(z)=(1-t)/(1-bt)\to0\) as \(t\uparrow1\). Because the range lies in \(L\) and its closure contains both zero and one, \(L\) must be the real axis, so \(b\) is real. Conversely, if \(b=c\in[-1,1)\) is real, the displayed function of \(t\in[0,1)\) decreases continuously from one to zero, giving precisely \((0,1]\). The identity case gives \(\{1\}\). This completes the convexity classification.

This completes the proof. \(\square\)

## Verification

The proof explicitly verifies Szegő-kernel normalization, quantitative localization at the attained boundary point one, rigidity from convexity of radial segments, and the harmonic maximum principle on each fixed-radius circle. The companion `verify_berezin_convexity.py` checks exact rational transform identities for polynomial disk selfmaps, samples the decisive failure of collinearity for a range of nonlinear cases, and checks real linear symbols. These finite tests are supplementary; the universal conclusion follows from the analytic proof.

## Relationship to prior work

Cowen and Felder established convexity results for Hardy composition operators with disk-automorphism symbols. Augustine, Garayev, and Shankar studied Hardy automorphisms and linear dilations, together with Bergman cases. Bourdon, Le, and Thompson's 2026 paper announces an exact convexity classification **for linear symbols**. That linear result is credited and explicitly excluded from the claimed novelty. An earlier sharp vertical-section cusp asymptotic for nonlinear symbols with real derivative inside \((-1,1)\) also implies nonconvexity in that particular subcase. The new theorem treats *every* analytic zero-fixing disk selfmap, without requiring either a real derivative or a specified first nonlinear jet, and supplies a uniform analytic-geometric proof of the entire classification. Inaccessible full text of the motivating paper leaves residual priority risk for an unstated more general theorem.

## Limitations

The classification is confined to classical Hardy space and holomorphic disk selfmaps fixing zero. It does not treat \(\phi(0)\ne0\), Bergman spaces, or weighted composition operators. The established real-linear case and the previously known real-multiplier cusp obstruction are not new. The motivating 2026 paper's abstract and first-public date were verified, but its complete text could not be retrieved; an equivalent result there or in other unindexed literature remains a real priority risk.

## References

1. P. Bourdon, T. Le, and D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634v1, first publicly submitted 2026-10-13, https://arxiv.org/abs/2610.17634 (abstract accessible).
2. C. C. Cowen and C. Felder, *Convexity of the Berezin Range*, Linear Algebra and its Applications **647** (2022), 47–63; authors' manuscript arXiv:2109.12095v1, https://scholarworks.indianapolis.iu.edu/bitstreams/54cd2540-51a0-4f22-ad5e-7482808650fd/download (Section 4 inspected).
3. A. Augustine, M. Garayev, and P. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547v2, https://arxiv.org/pdf/2302.12547 (Hardy and Bergman composition sections inspected).
4. Schwarz lemma, Schwarz–Pick inequality, the maximum principle for harmonic functions, and the open mapping theorem (standard analytic facts used in the proof).
