# Parity-resolved radial moment transitions for almost-diametral congruent polygon diagonals

## Finding

Let \(P_n\) be the regular \(n\)-gon of circumradius one. For integers \(n\ge5\) and \(2\le k<n/2\), independently choose two uniformly random **undirected** diagonals of span \(k\): the \(n\) chords from vertex \(j\) to vertex \(j+k\) (indices modulo \(n\)). Condition on their crossing *strictly inside both segments*. Write \(R_{n,k}\) for the distance of the intersection from the polygon center and \(\delta=n/2-k\). The exact conditional law is
\[
\boxed{\quad R_{n,k}\ \stackrel{d}{=}\
 \frac{\sin(\pi\delta/n)}{\sin(\pi(\delta+L)/n)},\qquad
 L\sim\operatorname{Unif}\{1,\ldots,k-1\}.\quad}
\]
In particular, the strict-crossing probability before conditioning is \(2(k-1)/n\).

Now fix \(\delta>0\), taking integer values along even \(n\) and half-integer values along odd \(n\), with \(k=n/2-\delta\ge2\). Put \(R_n=R_{n,k}\). Then the *bulk-scaled radial law* is
\[
 nR_n\ \Longrightarrow\ W_\delta=\frac{\pi\delta}{\sin(\pi U)},
 \qquad U\sim\operatorname{Unif}(0,1/2).
\]
Its distribution function is zero for \(y\le\pi\delta\) and, for \(y>\pi\delta\), equals
\[
\Pr(W_\delta\le y)=1-\frac2\pi\arcsin\!\left(\frac{\pi\delta}{y}\right).
\]
It has a Pareto tail \(\Pr(W_\delta>y)\sim2\delta/y\), hence a critical moment order one. Writing \(M_n(q)=\mathbb E R_n^q\), for every fixed \(q>0\),
\[
\boxed{\begin{array}{ll}
 0<q<1:&\displaystyle n^qM_n(q)\longrightarrow
  \pi^{q-1}\delta^q\operatorname{B}\!\left(\frac{1-q}{2},\frac12\right),\\[5pt]
 q=1:&\displaystyle \frac{nM_n(1)}{\log n}\longrightarrow2\delta,\\[5pt]
 q>1:&\displaystyle nM_n(q)\longrightarrow
 2\delta^q\zeta(q,\delta+1).
\end{array}}\]
Here \(\zeta(q,a)=\sum_{j=0}^\infty(j+a)^{-q}\) for \(q>1\). Moreover the critical window is uniform on each compact \(\lambda\)-interval: with \(q_n=1+\lambda/\log n\),
\[
\frac{nM_n(q_n)}{2\delta\log n}\longrightarrow
\frac{1-e^{-\lambda}}{\lambda},
\]
continuously interpreted as one at \(\lambda=0\).

A *second, rare-event radial scale* preserves the discrete lattice structure lost in the weak limit. For every fixed \(r\in(0,1)\), including all equality thresholds,
\[
\boxed{\quad n\Pr(R_n\ge r)\longrightarrow
2\max\!\left\{0,\left\lfloor\delta\left(\frac1r-1\right)\right\rfloor\right\}.\quad}
\]
Consequently even and odd regular polygons have genuinely different limiting rare-event step spectra when one selects their longest non-diametral diagonal span: \(\delta=1\) for even \(n\), and \(\delta=1/2\) for odd \(n\).

## Assumptions and scope

Every span-\(k\) chord is considered once, independent of endpoint order; since \(k<n/2\), there are exactly \(n\) distinct chords. The two sampled chords may initially coincide or share endpoints, but are retained only if their relative interiors intersect. Coincident lines, shared endpoints, and boundary touching are not counted as strict crossings. Radius is measured relative to the circumradius, which is one; a different circumradius multiplies all radii by that factor. The near-diametral limits fix \(\delta\) as the number of *half-vertex steps* below a diameter, not an arbitrary real depending on \(n\): integer \(\delta\ge1\) requires even \(n\), while \(\delta\in\{1/2,3/2,\ldots\}\) requires odd \(n\). The moment orders are positive real numbers.

## Proof

**1. Conditional counting and exact intersection radius.** By rotation take the first chord to join vertices \(0\) and \(k\). The chord with starting vertex \(j\) alternates in cyclic endpoint order with it if and only if \(j\in\{1,\ldots,k-1\}\cup\{n-k+1,\ldots,n-1\}\). There are exactly \(2(k-1)\) such values among the \(n\) equally likely second chords, giving the crossing probability. Under this conditioning, the smaller rotational offset \(J=\min\{j,n-j\}\) is uniform on \(\{1,\ldots,k-1\}\).

The supporting line of chord \(j\) is at signed distance \(h=\cos(\pi k/n)>0\) from the origin and has outward normal at argument \(\pi(2j+k)/n\). For \(1\le J<k<n/2\), the two normal directions differ by \(2\pi J/n\). The intersection lies on their angular bisector, and the scalar equations give
\[
 R_{n,k}=\frac{h}{\cos(\pi J/n)}
 =\frac{\sin(\pi\delta/n)}{\sin(\pi(n/2-J)/n)}.
\]
Substituting \(L=k-J\) produces the asserted exact uniform discrete law. It also proves that the atoms are strictly decreasing as \(L\) increases.

**2. Bulk weak limit.** When \(\delta\) is fixed, \(k=n/2-\delta\). The grid variable \((\delta+L)/n\) converges to a uniform variable \(U\) on \((0,1/2)\), with density two. Also \(n\sin(\pi\delta/n)\to\pi\delta\). Away from zero the inverse-sine map is continuous. Removing a sufficiently short initial interval has arbitrarily small probability, so the continuous-mapping argument gives the claimed weak limit. The event \(W_\delta\le y\) is equivalent to \(U\ge\arcsin(\pi\delta/y)/\pi\) when \(y>\pi\delta\), giving the CDF and its index-one Pareto tail.

**3. Fixed-order moment trichotomy.** The finite exact formula is
\[
 M_n(q)=\frac1{k-1}\sum_{\ell=1}^{k-1}
 \left[\frac{\sin(\pi\delta/n)}{\sin(\pi(\delta+\ell)/n)}\right]^q.
\]
For \(0<q<1\), the endpoint singularity of \(\sin(\pi x)^{-q}\) is integrable. The inequalities \(\sin(\pi x)\ge2x\) on \((0,1/2]\), and a cutoff at small \(x\), justify convergence of the improper Riemann sums, yielding
\[
\lim n^qM_n(q)=2(\pi\delta)^q\int_0^{1/2}\sin(\pi x)^{-q}\,dx
=\pi^{q-1}\delta^q\operatorname{B}((1-q)/2,1/2).
\]
At \(q=1\), use \(\sin(\pi x)^{-1}=(\pi x)^{-1}+O(x)\) uniformly for \(0<x\le1/2\). Summation shows
\(\sum_{\ell=1}^{k-1}\sin(\pi(\delta+\ell)/n)^{-1}=(n/\pi)\log n+O_\delta(n)\).
As \(\sin(\pi\delta/n)\sim\pi\delta/n\) and \(k-1\sim n/2\), the critical limit follows.

For \(q>1\) and each fixed \(\ell\), the corresponding ratio converges to \(\delta/(\delta+\ell)\). Uniformly in \(n\),
\[
\frac{\sin(\pi\delta/n)}{\sin(\pi(\delta+\ell)/n)}\le
\frac{\pi\delta}{2(\delta+\ell)},
\]
using the same sine bound. Its \(q\)-th power is summable in \(\ell\). Dominated convergence for series and \(n/(k-1)\to2\) yield \(nM_n(q)\to2\delta^q\sum_{\ell\ge1}(\delta+\ell)^{-q}\), the stated Hurwitz-zeta constant.

**4. Uniform moving-exponent crossover.** Fix \(|\lambda|\le B\), set \(q=1+\lambda/\log n\), and take \(n\) sufficiently large. Since \(\sin z/z=1+O(z^2)\) uniformly for \(0\le z\le\pi/2\), the exact sum in Step 3 equals
\[
\sum_{\ell=1}^{k-1}\left[\frac{\sin(\pi\delta/n)}{\sin(\pi(\delta+\ell)/n)}\right]^q
=\delta^q\sum_{\ell=1}^{k-1}(\delta+\ell)^{-q}+O_{\delta,B}(1).
\]
The error is bounded by a constant times \(n^{-2}\sum_{\ell\le k}(\delta+\ell)^{2-q}=O_B(n^{1-q})=O_B(1)\); the fixed numerator sine correction is smaller. Monotone sum–integral comparison then gives, uniformly on \(|\lambda|\le B\),
\[
 \sum_{\ell=1}^{k-1}(\delta+\ell)^{-1-\lambda/\log n}
 =\log n\,\frac{1-e^{-\lambda}}{\lambda}+O_{\delta,B}(1).
\]
Here the quotient is continuously one at zero. Since \(\delta^q=\delta+O_{\delta,B}(1/\log n)\), division by \(k-1\) proves the compact-uniform critical crossover.

**5. Exact rare-event staircase.** For a fixed \(r\in(0,1)\), a given term with index \(\ell\) has radius converging to \(\delta/(\delta+\ell)\). Only finitely many fixed \(\ell\) can contribute to the event \(R_n\ge r\), using the preceding \(O(1/\ell)\) bound. When \(r=\delta/(\delta+\ell)\), the finite radius is **strictly larger** than its limit because \(\sin x/x\) is strictly decreasing on \((0,\pi/2]\). Thus the equality index is included. Eventually the number of qualifying indices is exactly \(\max\{0,\lfloor\delta(1/r-1)\rfloor\}\), with each such index carrying probability \(1/(k-1)\). Multiplication by \(n\sim2(k-1)\) proves the staircase at all thresholds.

## Verification

Run `python3 verify_equal_diagonals.py` using the Python standard library. It separately computes Cartesian intersections by solving two line equations, verifies strict interior crossing and every individual radius for all admissible spans and \(5\le n<60\), checks their multiplicities and mean, and probes moment regimes and the finite rare-event staircase along both parity classes. The numerical tests have finite ranges and cannot prove the infinite-sequence statements; Steps 1–5 supply the proofs.

## Relationship to prior work

Inoue and Watanabe (2026) classify rational *areas* of the four regions cut by two congruent intersecting diagonals, using the same family of pairs. Their area classification does not state radial intersection distributions or near-diameter moments. Bortolotto and Souza (2025) determine the *unconditional* radial distribution of intersections of two independently endpoint-sampled random circle chords and treat a continuous random-line model; their equation for intersecting lines explains the elementary first-step geometry but does not provide the fixed-equal-span, parity-conditioned double scaling or the atomic rare-event spectrum. Poonen and Rubinstein (1998) classify counts of distinct intersection points of regular-polygon diagonals, especially concurrency, not conditional radial mass at fixed span. A separately published exact crossing-*angle* distribution for uniformly selected four-vertex crossing pairs has a critical inverse-sine moment order two; it uses different sampling and a different observable, and neither claim implies the present radial order-one transition. The novelty claimed here is the complete parity-resolved near-diametral **two-scale moment and rare-event classification**, not the cosine chord-intersection identity or standard harmonic-sum estimates.

## Limitations

The polygon is exactly regular, the two chord spans are equal, and all crossing pairs are counted by pair multiplicity even if several pairs intersect at the same spatial point. The near-diameter theorem fixes the integer or half-integer deficit \(\delta\); no uniform statement for growing \(\delta\) is claimed. The moving exponent is restricted to bounded \(\lambda\), and independent historical priority has not been established. In particular, the finite intersection-radius identity alone follows from elementary chord-line geometry and is not presented as a new general theorem.

## References

1. S. Inoue and K. Watanabe, *Rational Area Profiles of Regular Polygons Cut by Two Congruent Diagonals*, arXiv:2610.22970, first posted 2026-10-16, https://arxiv.org/abs/2610.22970 (primary MSC 51M04).
2. C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866, first posted 2025-04-17, https://arxiv.org/abs/2504.12866.
3. B. Poonen and M. Rubinstein, *The Number of Intersection Points Made by the Diagonals of a Regular Polygon*, SIAM J. Discrete Math. 11 (1998), 135–156; https://www.math.uwaterloo.ca/~mrubinst/publications/ngon.pdf.
4. *Critical transversality moments for crossings of regular-polygon diagonals*, published research record a53cddea2993 (2026-10-25), specifically its exact crossing-angle law and order-two moment transition.
5. *A critical moment crossover for nearest-vertex distances in regular polygons*, published research record 7901466d060d (2026-10-25), for comparison of the unrelated nearest-vertex order-one window.
