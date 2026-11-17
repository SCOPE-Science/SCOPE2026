# Sharp mean-square geodesic distance on flat Klein bottles

## Finding

Let \(a,b>0\). Form the flat Klein bottle
\[
K_{a,b}=\mathbb R^2/\langle T,G\rangle,\qquad
T(x,y)=(x+a,y),\quad G(x,y)=(-x,y+b).
\]
It has area \(A=ab\). If \(P,Q\) are independent area-uniform points and \(D=d_{K_{a,b}}(P,Q)\) is their intrinsic shortest-path distance, the **entire distance law** is
\[
 D\ \stackrel{\mathrm d}=\
 \min\!\left\{\sqrt{X^2+U^2},\sqrt{Y^2+(b-U)^2}\right\},
\]
where \(X,Y\) are independent uniform variables on \([0,a/2]\) and \(U\) is an independent uniform variable on \([0,b]\). In particular, with
\[
 q_r(z)=\min\!\left\{1,\frac{2}{a}\sqrt{(r^2-z^2)_+}\right\},\qquad (w)_+=\max\{w,0\},
\]
the exact all-radius cumulative distribution function is
\[
 F_{a,b}(r)=1-\frac1b\int_0^b (1-q_r(u))(1-q_r(b-u))\,du\quad(r\geq0),
\]
and its support endpoint, the intrinsic diameter, is \(\sqrt{a^2+b^2}/2\).

Define \(t=a/b\) and the scale-free pair-distance energy \(\mathcal E(t)=\mathbb E[D^2]/A\). For every \(0<t\leq2\),
\[
 \mathcal E(t)=\frac{t+t^{-1}}{12}-\frac{t^3}{360}.
\]
**Globally, for every \(t>0\), this energy has exactly one minimizer**:
\[
 t_* = \sqrt{5-\sqrt{15}}=1.061610405842267\ldots,
 \qquad
 \min_{t>0}\mathcal E(t)=\frac{(10+\sqrt{15})\sqrt{5-\sqrt{15}}}{90}
 =0.163641149782336\ldots .
\]
Thus the area-normalized squared distance is optimized by a slightly nonsquare fundamental rectangle, not by the visually square presentation. The ratio \(t\) refers specifically to the translation period \(a\) and glide height \(b\) in the displayed deck-group normal form.

## Assumptions and scope

The quotient has the Euclidean length metric, not the extrinsic distance of an immersion in three-space. The chosen fundamental rectangle is \([0,a)\times[0,b)\), with normalized Euclidean area measure; the two points are sampled independently. The displayed deck group acts freely and properly discontinuously for every \(a,b>0\). Its normal form covers the rectangular two-parameter family of all flat Klein-bottle metrics, up to swapping the axes of the more usual gliding-reflection presentation. Distances are nonnegative and all distributional equalities include their endpoints, with null-set ambiguity irrelevant to the CDF.

## Proof

**1. Deck-orbit minimization.** Write representatives \(P=(x,y)\), \(Q=(x',y')\) in the fundamental rectangle. Every image of \(Q\) under the deck group is of one of the two forms
\[
 (x'+ka,y'+2mb),\qquad (-x'+ka,y'+(2m+1)b),\qquad k,m\in\mathbb Z.
\]
Let \(s=|y-y'|\in[0,b]\), and write \(\operatorname{dist}_a(v)=\min_{k\in\mathbb Z}|v-ka|\). Minimizing over each orbit and using the Euclidean distance formula gives exactly
\[
 D^2=\min\!\left\{\operatorname{dist}_a(x-x')^2+s^2,
 \operatorname{dist}_a(x+x')^2+(b-s)^2\right\}.
\]
Indeed, the closest even vertical translate is at displacement \(s\), and the closest odd vertical translate is at displacement \(b-s\); horizontal and vertical translate indices can be minimized separately.

**2. Independence and the uniform-offset reduction.** The coordinates \(x,x'\), modulo \(a\), are independent Haar-uniform on the circle. The integer torus endomorphism \((x,x')\mapsto(x-x',x+x')\bmod a\) has nonzero determinant and is surjective. Its pushforward of Haar measure is Haar measure on the product circle, so the two circular distances
\[
 X=\operatorname{dist}_a(x-x'),\qquad Y=\operatorname{dist}_a(x+x')
\]
are independent and each uniform on \([0,a/2]\). They are independent of \(s\), whose density from independent \(y,y'\) is \(2(b-s)/b^2\) for \(0<s<b\). Given \(s\), the conditional survival probability at radius \(r\) equals \((1-q_r(s))(1-q_r(b-s))\), a function symmetric under \(s\mapsto b-s\). Its integral against the triangular density equals its integral against the uniform density \(1/b\), since
\[
 \int_0^b \frac{2(b-s)}{b^2}H(s)\,ds
 =\frac1b\int_0^b H(s)\,ds\quad\text{whenever }H(s)=H(b-s).
\]
This proves the complete distributional identity and the CDF formula, not just an equality of moments. The diameter follows by maximizing the minimum in the law: it is at most \(\sqrt{(a/2)^2+(b/2)^2}\), and this upper bound is attained at \(X=Y=a/2\), \(U=b/2\) (or approached with positive measure in neighborhoods).

**3. The exact energy functional.** Set \(X=aS/2\), \(Y=aT/2\), \(U=bV\) with independent \(S,T,V\sim\mathrm{Uniform}[0,1]\). Using \(\min\{c,d\}=(c+d-|c-d|)/2\), and \(Z=S^2-T^2\), yields
\[
 \mathcal E(t)=\frac{t}{12}+\frac{1}{3t}
 -\frac{1}{2t}\,\mathbb E\left[H\left(\frac{t^2|Z|}{4}\right)\right],
 \quad
 H(w)=\mathbb E_{W\sim\mathrm{Uniform}[-1,1]}|w+W|
 =\begin{cases}(1+w^2)/2,&0\leq w\leq1,\\w,&w\geq1.\end{cases}
\]
The independent elementary identities
\[
 \mathbb E Z^2=2\left(\frac15-\frac19\right)=\frac8{45},
 \qquad \mathbb E|Z|=2\int_0^1\int_0^s(s^2-u^2)\,du\,ds=\frac13
\]
are exact. If \(t\le2\), the input of \(H\) never exceeds one, and substitution gives \(\mathcal E(t)=(t+t^{-1})/12-t^3/360\).

**4. Global strict optimality beyond the polynomial regime.** The function \(H\) is continuously differentiable on \([0,\infty)\). Differentiation under the finite expectation is valid for each \(t>0\) by local bounded domination. Define
\[
 K(w)=H(w)-2wH'(w)=\begin{cases}(1-3w^2)/2,&0\leq w\leq1,\\-w,&w\geq1.\end{cases}
\]
Writing \(w=t^2|Z|/4\), one gets
\[
 t^2\mathcal E'(t)=\frac{t^2}{12}-\frac13+\frac12\mathbb E K(w).
\]
Two pointwise inequalities, valid for all \(w\geq0\), are
\[
 K(w)\geq\frac{1-3w^2}{2},\qquad K(w)\geq-w.
\]
For the first, the difference for \(w\ge1\) is \((w-1)(3w+1)/2\ge0\); for the second, the difference for \(w\le1\) is \((1-w)(1+3w)/2\ge0\). Therefore, with \(g(t)=(t+t^{-1})/12-t^3/360\),
\[
 \mathcal E'(t)\geq g'(t)
 =\frac1{12}-\frac1{12t^2}-\frac{t^2}{120},
 \qquad
 t^2\mathcal E'(t)\geq\frac{t^2}{24}-\frac13.
\]
The derivative \(g'(t)\) vanishes precisely when \(t^2=5\pm\sqrt{15}\). It is negative on \(0<t<t_*\) and positive on \(t_*<t<\sqrt{5+\sqrt{15}}\). Since \(\mathcal E=g\) on \(0<t\le2\), \(\mathcal E\) decreases strictly up to \(t_*\). For \(t_*<t\le\sqrt8\), the first lower bound gives \(\mathcal E'(t)>0\); for \(t>\sqrt8\), the second gives \(\mathcal E'(t)>0\). These ranges cover all larger \(t\), proving the unique global minimizer. Substitution and \(t_*^4-10t_*^2+10=0\) simplify the minimum to the stated radical.

## Verification

The standalone `check_klein.py` tests the deck-image distance identity against a direct finite deck-orbit enumeration, compares independent Monte Carlo area sampling with the exact energy at seven distinct shapes, checks deterministic quadrature of the complete CDF against empirical frequencies, and independently integrates the general aspect-ratio energy representation. These are numerical consistency checks only: the group-action and derivative inequalities above constitute the proof for all positive parameters. Run with `python3 check_klein.py` using Python 3.10 or later and the standard library only.

## Relationship to prior work

El Mir and Lafontaine, arXiv:0804.1419 (first posted 2008-04-09), Section 2.2, give the usual flat Klein-bottle deck-group normal form and study systolic geometry, not random pair-distance laws. El Mir, arXiv:1007.0877 (2010-07-06), studies conformally extremal singular metrics based on Klein-bottle geometry, not the present area-normalized intrinsic distance moment. Hubard, Kaluža, de Mesmay and Tancer, arXiv:1602.06778 (2016-02-22), study shortest-path graph embeddings on flat Klein bottles; their Section 4 uses deck-orbit Voronoi cells but does not integrate a distance distribution or optimize a pairwise squared-distance energy. Davis and Recio-Mitter, arXiv:1912.07411 (2019-12-16), study cut-locus topology and geodesic motion-planning complexity, not pair-distance probability. Benedetto et al., DOI:10.1007/s10955-021-02768-4 (2021-05-12), optimize a spectral regularization constant for random many-point assignment on flat Klein bottles; it is a different statistic with a different shape optimizer. Related arclength-pair statistics for Möbius strips, tori and pillowcase quotients do not furnish this two-image uniform-offset identity or its global sharp minimizer. None of these sources is asserted to establish historical uniqueness of the present result.

## Limitations

The result concerns the intrinsic flat metric and independent area-uniform points; it does not concern Euclidean distances in a self-intersecting immersion. The complete CDF is supplied as an exact one-dimensional integral, not asserted to have an elementary closed form for every aspect ratio and radius. The fixed-area uniqueness theorem is for the squared geodesic distance, not automatically for mean distance or stochastic order. Historical priority remains open to unindexed stereological and metric-geometry literature. Independent mathematical validation has not been performed.

## References

1. C. El Mir and J. Lafontaine, *Sur la géométrie systolique des variétés de Bieberbach*, arXiv:0804.1419, first posted 2008-04-09, Section 2.2, https://arxiv.org/abs/0804.1419.
2. C. El Mir, *Bavard's systolically extremal Klein bottles and three dimensional applications*, arXiv:1007.0877, first posted 2010-07-06, Section 2.1, https://arxiv.org/abs/1007.0877.
3. A. Hubard, V. Kaluža, A. de Mesmay and M. Tancer, *Shortest path embeddings of graphs on surfaces*, arXiv:1602.06778, first posted 2016-02-22, Section 4, https://arxiv.org/abs/1602.06778.
4. D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411, first posted 2019-12-16, Sections 1–2, https://arxiv.org/abs/1912.07411.
5. D. Benedetto et al., *Random Assignment Problems on 2d Manifolds*, Journal of Statistical Physics 183, article 34 (2021), Section 5.3.3, https://doi.org/10.1007/s10955-021-02768-4.
