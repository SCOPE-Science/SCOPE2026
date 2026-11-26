# The upper-width tail and polar contact law of the unit oloid

## Finding

Let \(K\) be the convex hull of the two circles \(C_1=\{(\cos s,\sin s,0):0\le s<2\pi\}\) and \(C_2=\{(0,1+\cos s,\sin s):0\le s<2\pi\}\). For uniform \(U=(x,y,z)\in S^2\), define the width \(W=h_K(U)+h_K(-U)\). Then
\[
\Pr(W\ge3-\varepsilon)=\frac{\varepsilon}{2}+\frac{\varepsilon^2}{64}+O(\varepsilon^3)\qquad(\varepsilon\downarrow0).
\]
Conditional on this event, the two signs of \(y\) have equal probabilities for every sufficiently small positive \(\varepsilon\). For each sign, \((x,z)/\sqrt{\varepsilon}\) converges in total variation to normalized area measure on the unit disk. Throughout the event for sufficiently small \(\varepsilon\), the two opposing support planes are borne by different generating circles.

## Scope and motivation

Both generating radii and their center separation are one. Width is the distance between parallel support planes, not a chord length. Both orientations are counted with normalized spherical area. The result quantifies the fraction and directional spread of near-maximum caliper readings. The second coefficient is the first correction to the leading polar-cap law; it combines the anisotropic quartic width deficit with the spherical area density.

## Proof

For \(u=(x,y,z)\in S^2\), set \(A=\sqrt{1-z^2}\) and \(B=\sqrt{1-x^2}\). Taking the maximum of the circle supports gives \(h_K(u)=\max(A,y+B)\) and \(h_K(-u)=\max(A,-y+B)\). Hence \(W(u)=\max(2A,2B,A+B+|y|)\). The first two terms are at most two, and the last is at most three with equality only at \((0,\pm1,0)\). Compactness and continuity localize the high-width tail to small neighborhoods of these two points. In those neighborhoods \(|y|>|A-B|\), so the opposing maxima are strict and furnished by different circles. For positive \(y\) they are furnished by \(C_2\) in direction \(u\) and \(C_1\) in direction \(-u\); negative \(y\) reverses the roles.

Write \(x=\sqrt{s}\cos\phi\), \(z=\sqrt{s}\sin\phi\), \(y=\pm\sqrt{1-s}\). Then \(W=\sqrt{1-s\cos^2\phi}+\sqrt{1-s\sin^2\phi}+\sqrt{1-s}\). The deficit \(3-W\) is strictly increasing near \(s=0\), with expansion uniform in \(\phi\):
\[
3-W=s+c(\phi)s^2+O(s^3),\qquad c(\phi)=\frac{1+\cos^4\phi+\sin^4\phi}{8}.
\]
The radial boundary is \(s_\varepsilon(\phi)=\varepsilon-c(\phi)\varepsilon^2+O(\varepsilon^3)\). In each hemisphere the area element is \((1-s)^{-1/2}\,dx\,dz=(1/2)(1-s)^{-1/2}\,ds\,d\phi\). Thus, summing two congruent regions and dividing by \(4\pi\), the probability is
\[
\frac{1}{2\pi}\int_0^{2\pi}\bigl(1-\sqrt{1-s_\varepsilon(\phi)}\bigr)\,d\phi
=\frac{\varepsilon}{2}+\left(\frac18-\frac12\frac7{32}\right)\varepsilon^2+O(\varepsilon^3).
\]
Here \(7/32\) is the angular mean of \(c\), since the two fourth-power averages are each \(3/8\). The coefficient in parentheses is \(1/64\). In each hemisphere the region in \((x,z)/\sqrt{\varepsilon}\) has radial boundary \(1+O(\varepsilon)\) uniformly; its symmetric difference with the unit disk has area \(O(\varepsilon)\). Its unnormalized density with respect to scaled planar area, omitting the constant Jacobian \(\varepsilon\), is \((1-\varepsilon(X^2+Z^2))^{-1/2}=1+O(\varepsilon)\) uniformly on the region. Normalization therefore gives the total-variation limit. Reflection \(y\mapsto-y\) proves equality of hemisphere weights.

## Verification

The uniform expansion and the polar integral above establish the result analytically. The accompanying `check.py` also implements direct polar quadrature (`upper_tail`) and reports finite second-coefficient diagnostics; its unrelated lower-tail checks are not needed here. Such diagnostics do not prove the expansion or the total-variation limit.

## Relationship to prior work and limitations

Bäsel's [mean-width paper, §4](https://arxiv.org/abs/1604.07245) uses the directional support function and computes its mean-width integral. Neither that support setup nor the maximum and its two directions are claimed here as new. The [separated-circle width crossover](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-singular-near-minimum-width-crossover-for-two-separated-orthogon--478c8834f500/RESULT.md) includes the maximum at unit separation and gives small-width laws. Another [orthogonal-disk crossover](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-singular-crossover-in-near-minimal-random-widths-of-two-orthog--a276467e90bf/RESULT.md) explicitly includes the oloid's leading lower-tail law. The distinct assertion here is the two-term *upper* tail and its associated polar contact law at unit separation. No full distribution, other separation, or historical-priority guarantee is asserted.
