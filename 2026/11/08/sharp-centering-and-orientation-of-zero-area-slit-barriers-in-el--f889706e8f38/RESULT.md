# Sharp centering and orientation of zero-area slit barriers in elliptical Beer indices

## Finding

A line segment removed from a convex disk has area zero but has a strictly positive effect on the probability that two independent uniformly sampled interior points can see one another. Among all placements of a slit of prescribed vector in an ellipse, the **unique** visibility-minimizing placement is centered. Among all orientations and positions of a fixed Euclidean slit length shorter than the minor diameter, the unique direction for a noncircular ellipse is the **minor axis**. This is a global statement rather than a local variation.

Write \(B_2=\{u\in\mathbb R^2:\|u\|\le1\}\) and consider an ellipse \(E=z+L B_2\), for an invertible real \(2\times2\) matrix \(L\). Its semiaxes are the singular values \(A\ge B>0\). For a closed slit \(S_{c,v}=\{c+tv:-1\le t\le1\}\subset\operatorname{int}(E)\), with \(v\ne0\), take independent area-uniform \(X,Y\) from \(E\setminus S_{c,v}\). Define the blocked probability \(P_E(c,v)=\Pr([X,Y]\cap S_{c,v}\ne\varnothing)\); the Beer index is \(b(E\setminus S_{c,v})=1-P_E(c,v)\). Define \(a=\|L^{-1}v\|\), which satisfies \(0<a<1\), and

\[
\Phi(a)=\frac4{\pi^2}\int_0^a (1-s^2)\left(1+\frac{1-s^2}{s}\operatorname{arctanh}s\right)ds,\qquad 0<a<1.
\]

At \(s=0\), the bracket is defined by continuity and has value \(2\).

**Sharp placement theorem:** for every allowed slit, \(P_E(c,v)\le\Phi(a)\), with equality **exactly** when \(c=z\). Thus the unique minimizer of the Beer index for a fixed slit vector is its center.

**Sharp fixed-length theorem:** for every Euclidean slit length \(0<\ell<2B\), among all such slits of length \(\ell\) wholly within the ellipse,

\[
\min b(E\setminus S_{c,v})=1-\Phi\left(\frac{\ell}{2B}\right).
\]

The minimizing slits are precisely the centered minor-axis slits when \(A>B\); if \(A=B\), they are precisely all centered slits. No dependence on the major semiaxis remains in the extremal value. Moreover \(\Phi\) is strictly increasing and strictly concave on \((0,1)\), with

\[
\Phi(a)=\frac{8a}{\pi^2}-\frac{32a^3}{9\pi^2}+O(a^5),\quad
\Phi(1-)=\frac12,\quad
\frac12-\Phi(a)\sim\frac4{\pi^2}(1-a)^2.
\]

Consequently a strictly interior slit in any ellipse makes **fewer than half** of independent area-uniform point pairs invisible; this bound is approached by centered slits tending to a full diameter.

## Assumptions and scope

All sets are planar and all probabilities use **independent normalized Euclidean area measure on the domain with the slit removed**. The slit is closed, has positive length, and both endpoints lie strictly inside the ellipse. Its removed area is zero, so sampling from the slit-free ellipse is equivalent almost surely to sampling from the original ellipse. The event is failure of the **entire closed connecting segment** to stay in the slit domain, not intersection of the full infinite line with the slit. The affine map \(x\mapsto L^{-1}(x-z)\) preserves normalized area sampling and straight-segment intersection events. It need not preserve Euclidean lengths, and the fixed physical length optimization explicitly accounts for this distinction. Endpoint-touching and tangent events are null in the sampling model. The restriction \(\ell<2B\) guarantees the admissible centered segment exists in every direction and that the sharp optimum is attained by an interior slit.

## Proof

**1. Reduction to a disk.** Affine invariance sends the ellipse to the unit disk and the slit to a segment of half-length \(a=\|L^{-1}v\|\). A rotation makes its endpoints \((c-a,h)\) and \((c+a,h)\), where \((|c|+a)^2+h^2<1\). We use \(c,h\) for these disk coordinates only.

**2. Exact disk event integral.** Write a line in normal coordinates as \(r=p n_\theta+t u_\theta\), with \(u_\theta=(\cos\theta,\sin\theta)\), \(n_\theta=(-\sin\theta,\cos\theta)\) and \(0\le\theta<\pi\). For two points \(x=p n_\theta+t u_\theta\), \(y=p n_\theta+q u_\theta\), the change-of-variables Jacobian is \(|t-q|\). A line crossing the slit at \(r=(s,h)\) has normal coordinate \(p=h\cos\theta-s\sin\theta\) and \(|dp|=\sin\theta\,ds\) for fixed \(\theta\).

The chord of the unit disk through \(r\) has distances \(L_+,L_->0\) to its ends along opposite directions of \(u_\theta\). Elementary substitution into \(\|r+t u_\theta\|=1\) gives

\[
L_+L_-=1-s^2-h^2,\qquad L_++L_-=2\sqrt{1-p^2}.
\]

The ordered pairs of endpoints with the connecting **segment** containing \(r\) correspond precisely to points on opposite sides of \(r\). Their integrated Jacobian equals

\[
2\int_0^{L_+}\int_0^{L_-}(t+q)\,dq\,dt=L_+L_-(L_++L_-).
\]

Since the disk area is \(\pi\), normalized by \(\pi^2\), the exact blocked probability is

\[
P_{B_2}(c,h;a)=\frac{2}{\pi^2}\int_{c-a}^{c+a}(1-s^2-h^2)J(s,h)\,ds,
\quad J(s,h)=\int_0^\pi\sin\theta\sqrt{1-(h\cos\theta-s\sin\theta)^2}\,d\theta.
\]

This exact representation is valid for every wholly interior slit, not just for centered ones. In particular, its integral is of nonnegative bounded continuous functions for every feasible configuration; the oblique line convention counts each unoriented line exactly once.

**3. Strict centering perpendicular to the slit.** The function \(f(t)=\sqrt{1-t^2}\) is strictly concave on \((-1,1)\). Pair \(\theta\) and \(\pi-\theta\). Their normal coordinates are \(h\cos\theta-s\sin\theta\) and \(-h\cos\theta-s\sin\theta\); their arithmetic mean is \(-s\sin\theta\). The concavity inequality yields \(J(s,h)\le J(s,0)\), strictly for \(h\ne0\) because \(\cos\theta\ne0\) on a set of positive angular measure. The positive factor \(1-s^2-h^2\) is at most \(1-s^2\), again strictly when \(h\ne0\). Hence \(P_{B_2}(c,h;a)<P_{B_2}(c,0;a)\) for all \(h\ne0\).

**4. Strict centering along the slit.** Set \(w(s)=(1-s^2)J(s,0)\). This is positive and even for \(|s|<1\). Its angular integrand is \((1-s^2)\sin\theta\sqrt{1-s^2\sin^2\theta}\), which is strictly decreasing in \(|s|\in(0,1)\) on a positive-measure set of angles. Therefore \(w\) is strictly decreasing on \((0,1)\). For any allowed shift \(c\),

\[
\int_{c-a}^{c+a}w(s)\,ds\le\int_{-a}^{a}w(s)\,ds,
\]

with equality only if \(c=0\). For example, the derivative of the left side in \(c\) is \(w(c+a)-w(c-a)<0\) when \(c>0\) (using evenness and strict radial monotonicity), and opposite when \(c<0\). Combined with Step 3, the **only** maximizing center is \((c,h)=(0,0)\).

**5. Evaluation of centered profile.** At \(h=0\), set \(u=\cos\theta\); then

\[
J(s,0)=\int_{-1}^1\sqrt{1-s^2+s^2u^2}\,du=1+\frac{1-s^2}{s}\operatorname{arctanh}s,
\]

for \(0<s<1\), with \(J(0,0)=2\). Substitution into Step 2 and evenness give \(P_{B_2}(0,0;a)=\Phi(a)\). In particular \(\Phi'(a)=4w(a)/\pi^2>0\) and \(\Phi''(a)=4w'(a)/\pi^2<0\) for \(0<a<1\).

**6. Affine orientation optimization.** A physical slit of length \(\ell\) and unit direction \(e\) has \(v=\ell e/2\). Thus its disk-normalized half-length is \(a=(\ell/2)\|L^{-1}e\|\). The spectral theorem gives \(\|L^{-1}e\|\le 1/B\), with equality exactly for a minor-semiaxis direction if \(A>B\), and for every unit direction in the circular case. Strict increase of \(\Phi\) together with Steps 3–4 proves the uniqueness and sharp fixed-length formula.

**7. Endpoints of the profile.** Taylor expansion of the integrand yields \(w(s)=2-8s^2/3+O(s^4)\), which integrates to the stated short-slit expansion. At \(a=1\), the limiting slit is a full diameter, separating the disk into two equal halves. Almost surely a random connecting segment crosses that diameter exactly when its two endpoints lie on opposite sides, so \(\Phi(1-)=2(1/2)(1/2)=1/2\). Finally \(J(s,0)\to1\) as \(s\uparrow1\) and \(w(s)\sim2(1-s)\). Integrating \(\Phi'(s)=4w(s)/\pi^2\) from \(a\) to one yields \(1/2-\Phi(a)\sim4(1-a)^2/\pi^2\). This establishes every claim.

## Verification

The accompanying `check_slit.py` computes the two-dimensional chord-coordinate integral using adaptive quadrature, independently computes the centered one-dimensional formula, and compares both against direct Monte Carlo simulation of two independent area-uniform disk points with explicit segment–slit intersection testing. It checks multiple displaced and centered slits and three elliptical aspect-ratio examples. Dependencies and a seed are specified by `requirements.txt` and the script. The exact analytic proof above does not rely on this finite simulation or on any convergence assumption for the numerical quadrature.

Representative numeric values: \(\Phi(0.1)\approx0.0806971266\), \(\Phi(0.3)\approx0.2335500450\), \(\Phi(0.6)\approx0.4120254748\). At \(a=0.3\), moving the horizontal slit by \(0.3\) along its axis reduces the crossing probability to approximately \(0.2060127374\); moving by \(0.4\) perpendicular to its axis reduces it to approximately \(0.1895448349\). These are checks, not proof of global optimality.

## Relationship to prior work

Beer (1973) established the visibility function and the normalized index for general measurable sets, together with compact-set semicontinuity and structural results. The hypotheses and conclusions there do not furnish an exact centered-slitting probability or an all-ellipse length/orientation optimizer. Balko, Jelínek, Valtr and Walczak (first publicly available as an arXiv preprint on 2014-12-04) introduced the terminology Beer index and proved general comparisons between Beer index and convexity ratios, including higher-order variants. These are general inequalities and do not determine the sharp slit problem. Existing calculations for sampled boundary chords or for infinite-line incidence use different sampling measures or different intersection events; their conclusions cannot be transplanted to the independent area-uniform endpoint model. Classical line-coordinate changes provide the general integral-geometric method, but the global strict centering, minor-axis orientation and exact \(\Phi\) profile require the chord-weight calculation and concavity comparison here.

## Limitations

This theorem is only about one **straight zero-area closed slit** inside a **planar ellipse**. It does not cover multiple slits, fat obstacles of positive area, curved barriers, higher-dimensional ellipsoids, or random chord conventions based on boundary endpoints or motion-invariant lines. The explicit optimizer at fixed physical length is asserted for \(0<\ell<2B\); no maximizer statement is made for longer lengths that cannot fit centered in every orientation. Unindexed literature in geometric probability may contain overlapping conclusions; numerical experiments are not a substitute for the analytical proof.

## References

1. G. Beer, “The index of convexity and the visibility function”, *Pacific Journal of Mathematics* **44** (1973), 59–67. https://msp.org/pjm/1973/44-1/pjm-v44-n1-p05-s.pdf .
2. M. Balko, V. Jelínek, P. Valtr, B. Walczak, “On the Beer Index of Convexity and Its Variants”, arXiv:1412.1769, publicly posted 2014-12-04; *Discrete & Computational Geometry* **57** (2017), 179–214. https://arxiv.org/abs/1412.1769 ; https://doi.org/10.1007/s00454-016-9821-3 .
3. G. Egan, “Pick Two Points” (2025), subsection “Two Points in a Disk”, an independent boundary-chord density calculation for area-uniform interior sampling, not a slit-barrier optimization. https://www.gregegan.net/SCIENCE/PickTwoPoints/PickTwoPoints.html .
