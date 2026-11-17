# A logarithmic endpoint cusp and marked limit for random crossing chords

## Finding

Independently and uniformly choose four points \(A,B,C,D\) on a circle and form the directed chord \(AB\) and chord \(CD\). Condition on their interior intersection \(P\), an event of probability \(1/3\). Let \(U=|AP|/|AB|\in(0,1)\). Then

\[\lim_{t\downarrow0}\frac{\Pr(U<t\mid AB\cap CD\ne\varnothing)}{t\log(1/t)}=\frac{3}{\pi^2}.\]

The same law holds at \(U>1-t\); hence, with \(V=\min(U,1-U)\),

\[\Pr(V<t\mid\mathrm{crossing})\sim\frac{6}{\pi^2}t\log(1/t).\]

In particular, for any \(p>0\),

\[\mathbb E\bigl[V^{-p}\mid\mathrm{crossing}\bigr]<\infty\quad\Longleftrightarrow\quad p<1.\]

There is a marked rare-event law. Choose the circle orientation (clockwise or counterclockwise) in which the four points occur in cyclic order \(A,C,B,D\), and write their successive arc fractions (relative to the full circumference) as \((X,Y,Z,W)\). On \(U<t\), define \(T_t=\log X/\log t\) and \(B_t=U/t\). Conditionally on crossing and \(U<t\), the law of \((T_t,B_t,Y)\) converges in **total variation** to the product of two independent uniform distributions on \((0,1)\) and a third independent density \(2\sin^2(\pi y)\,dy\) on \((0,1)\).

All statements remain true for affine images of the circle (ellipses) when endpoints are sampled by uniformly distributed eccentric anomaly: the directed intersection fraction \(U\) is affine invariant. Uniform arclength sampling on a noncircular ellipse is **not** asserted.

## Assumptions and scope

The four points are independent, each uniform in angular measure, and almost surely pairwise distinct. The chords are finite closed segments; crossings at endpoints have probability zero. The fraction is measured in ordinary Euclidean length along the first chord. Because affine transformations preserve fractions of collinear segments, the ellipse extension uses the affine pushforward of angular measure, not ellipse arclength measure.

Conditional on crossing, after choosing the circle orientation in which the points occur in cyclic order \(A,C,B,D\), the three free arc fractions \((x,y,w)\) have constant joint density \(6\) on the simplex \(x>0,y>0,w>0,x+y+w<1\), with \(z=1-x-y-w\). The first-chord endpoint swap maps \(U\) to \(1-U\).

## Proof

**1. Exact chord fraction.** The intersecting-chord sine rule, or similarity of the four subtriangles with vertex \(P\), gives

\[ U=\frac{\sin(\pi x)\sin(\pi w)}{\sin(\pi x)\sin(\pi w)+\sin(\pi y)\sin(\pi z)}. \tag{1}\]

This identity can also be obtained by intersecting the straight lines through \(e^{2\pi i\theta}\) at cumulative angles \(0,x,x+y,x+y+z\). It holds for every positive simplex point, so there is no approximation involved.

**2. Exact integral.** For \(0<t<1/2\), let \(q=t/(1-t)\), \(h=x+y\), and \(c=q\sin(\pi y)/\sin(\pi x)\). Inequality \(U<t\) is \(\sin(\pi w)<c\sin(\pi(h+w))\), with \(0<w<1-h\). It has exactly the interval of solutions \(0<w<w_*(x,y;t)\), where

\[w_* =\frac1\pi\operatorname{atan2}\!\bigl(c\sin(\pi h),\,1-c\cos(\pi h)\bigr),\]

with the angle chosen in \((0,\pi)\). Thus the **exact conditional distribution function** is

\[F(t)=6\int_0^1\int_0^{1-x}w_*(x,y;t)\,dy\,dx.\tag{2}\]

This is an exact convergent integral with no sampling or asymptotic qualification.

**3. Logarithmic boundary layer.** Fix \(M>1\) large and \(0<\varepsilon<1/2\) small. The region \(x\le Mt\) has volume \(O_M(t)\), because the simplex density is bounded. On \(x\ge\varepsilon\), use the explicit cutoff in (2), \(\sin(\pi y)\le\sin(\pi x)\,C_\varepsilon\) when \(x\) is near \(1\) (and boundedness elsewhere), to obtain an \(O_\varepsilon(t)\) contribution. For \(Mt\le x\le\varepsilon\), the quantity \(c=O(1/M)\) uniformly; expansion of the exact cutoff gives

\[w_*=\frac{t}{\pi}\frac{\sin(\pi y)\sin(\pi(x+y))}{\sin(\pi x)}\bigl(1+O(M^{-1})+O(t)\bigr).\]

The integrable inner factor is explicitly

\[\int_0^{1-x}\sin(\pi y)\sin(\pi(x+y))\,dy=\frac{1-x}{2}\cos(\pi x)+\frac{\sin(\pi x)}{2\pi}=\frac12+O(x).\]

Therefore the middle region contributes

\[\frac{6t}{\pi}\int_{Mt}^{\varepsilon}\frac{(1/2+O(x))\,dx}{\sin(\pi x)}\bigl(1+O(M^{-1})+O(t)\bigr)
=\frac{3t}{\pi^2}\log(1/t)\bigl(1+O(M^{-1})+o_t(1)\bigr).\]

Divide by \(t\log(1/t)\), send \(t\downarrow0\), then \(M\uparrow\infty\), yielding the stated constant. The first- and last-region errors vanish after normalization. Swapping the endpoints of \(AB\) establishes the other cusp. For \(V\), the two endpoint events are disjoint for \(t<1/2\). The inverse-moment threshold follows from the layer-cake identity \(\mathbb E[V^{-p}]=2^p+p\int_0^{1/2}s^{-p-1}\Pr(V<s)\,ds\) and integration of \(s^{-p}\log(1/s)\).

**4. Marked total-variation limit.** Write \(x=t^a\), \(u=tb\) on the event \(0<u=U<t\), and solve (1) for \(w=w(x,y,u)\). The transformed unnormalized density for \((a,b,y)\) is exactly

\[6\,|\log t|\,x\,t\,\partial_u w(x,y,tb)\]

on the admissible domain. For each fixed \(0<a<1\), \(0<b<1\), and \(0<y<1\), one has \(x\to0\), \(u/x\to0\), and

\[w=\frac{u\sin^2(\pi y)}{\pi^2x}(1+o(1)),\qquad \partial_u w=\frac{\sin^2(\pi y)}{\pi^2x}(1+o(1)).\]

For fixed \(a>1\), the normalized density tends to zero: the admissible intersection lies close instead to the opposite boundary \(z=0\), and the Jacobian is of lower order. After dividing by \(F(t)\sim 3t\log(1/t)/\pi^2\), the resulting density converges almost everywhere to

\[\mathbf1_{(0,1)}(a)\mathbf1_{(0,1)}(b)\,2\sin^2(\pi y)\mathbf1_{(0,1)}(y).\]

This limiting density integrates to \(1\). Since the prelimit conditional densities also integrate to \(1\), Scheffé's lemma gives total-variation convergence on the common coordinate space. This proves the claimed factorization without assuming uniform integrability of unbounded observables.

## Verification

The standalone `chord_fraction_verifier.py` checks (1) against direct Cartesian line intersections for 128 fixed-seed Dirichlet samples, confirms endpoint symmetry, evaluates the exact cutoff (2) by high-order deterministic quadrature, and compares its small-threshold behavior with \(3/\pi^2\). Run `python chord_fraction_verifier.py` with Python 3, NumPy and SciPy. Finite numerical checks corroborate the exact geometry and asymptotic constant; the infinite-limit theorem and total-variation statement rely on the analytic proof above.

## Relationship to prior work

Classical work by David and Fix (1964) treats intersections of random chords; its full text could not be inspected, so there remains a historical-priority uncertainty. Gates (1982) studied the distribution of the **count** of chord intersections, a different observable. Bortolotto and Souza (arXiv:2504.12866, first posted 2025) derive radial intersection-point laws and line-intersection analogues; their inspected article does not give the fraction of a specified chord lying before the crossing, its logarithmic endpoint tail, or the marked conditional factorization. Likewise, crossing-angle distributions and counting results do not imply the directed chord division ratio merely from their published marginals.

## Limitations

The result uses four independent angular-uniform endpoints conditioned on alternating cyclic order; it does not apply unchanged to invariant-line chords, endpoints sampled by nonuniform arclength on ellipses, or correlated endpoints. No rate of total-variation convergence or full elementary density of \(U\) is claimed. Historical priority, especially relative to the inaccessible David–Fix 1964 full text, remains provisional. Independent validation has not been performed.

## References

1. F. N. David and E. Fix, “Intersections of random chords of a circle,” *Biometrika* **51** (1964), 373–379; published December 1, 1964. https://doi.org/10.1093/biomet/51.3-4.373 (bibliographic record available; full article not inspected).
2. J. Gates, “The number of intersections of random chords to a circle—third and fourth moments,” *Journal of Applied Probability* **19** (1982), 355–372. https://doi.org/10.2307/3213487 (abstract and references inspected).
3. C. Bortolotto and V. Souza, “Intersections of random chords of a circle,” arXiv:2504.12866 (first posted April 17, 2025), https://arxiv.org/abs/2504.12866 (public full text inspected).
