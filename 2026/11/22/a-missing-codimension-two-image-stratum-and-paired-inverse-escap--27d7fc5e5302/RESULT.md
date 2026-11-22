# A missing codimension-two image stratum and paired inverse escape in a four-dimensional memristive map

## Finding

The four-dimensional parabolic discrete-memristor map of Wang et al. admits a complete global one-step inverse-fiber classification. It is generically two-to-one, but the image omits a codimension-two family **inside** its natural positive-output half-space. Those omitted targets are not critical values: both algebraic inverse branches escape to infinity with the same first-order pole as a target approaches the missing family.

Specifically, for every \(a,b,c>0\),
\[
F_{a,b,c}(x,y,z,w)=\left(ay^2,\ b\left(1-\frac{w^2}{2}\right)y(1-z),\ c(1-x),\ w+y\right).
\]
With output coordinates \((X,Y,Z,W)\), put
\[
\mathcal H=\{(2a,Y,Z,0):Y\ne0,\ Z\in\mathbb R\}.
\]
Then the **exact** global image and closure are
\[
F_{a,b,c}(\mathbb R^4)
=\bigl(\{X>0\}\setminus\mathcal H\bigr)
\cup\{X=0,Y=0\},\qquad
\overline{F_{a,b,c}(\mathbb R^4)}=\{X\ge0\},
\]
where unlisted output coordinates are arbitrary.

## Assumptions and scope

All initial and output coordinates are real; \(a,b,c\) are strictly positive. The discrete memristance is precisely \(M(w)=1-w^2/2\), corresponding to the paper's stated \(\epsilon=1,\eta=-1/2\). The theorem concerns **one-step inverse geometry** of the map on all of \(\mathbb R^4\), rather than a bounded physical observation box or a forward attractor.

For a target with \(X>0\), define
\[
r=\sqrt{X/a},\qquad m_\sigma=1-\frac{(W-\sigma r)^2}{2},
\quad \sigma\in\{-1,+1\}.
\]
The fiber is the disjoint union of the following branch contributions:

- If \(m_\sigma\ne0\), **one point**
\[
\left(1-\frac Zc,\ \sigma r,\ 1-\frac{Y}{b\sigma r m_\sigma},\ W-\sigma r\right).
\]
- If \(m_\sigma=0\) and \(Y=0\), **one complete affine line**
\[
\left\{\left(1-\frac Zc,\ \sigma r,\ s,\ W-\sigma r\right):s\in\mathbb R\right\}.
\]
- If \(m_\sigma=0\) and \(Y\ne0\), **no point**.

When \(X=0\), the fiber is exactly the line \(\{(1-Z/c,0,s,W):s\in\mathbb R\}\) for \(Y=0\), and empty otherwise. For \(X<0\), it is empty. These rules classify all cardinalities including singletons, two points, one or two full affine lines, a line plus a point, and empty fibers. In particular, for \(X>0,Y\ne0\), the fiber cardinality is the number of nonzero terms among \(m_{-1},m_{+1}\).

## Proof

**Step 1 (exhaustive inverse reduction).** The first and fourth output equations impose \(X=ay^2\) and \(W=w+y\). If \(X<0\) there is no real solution. If \(X=0\), strict positivity of \(a\) forces \(y=0\), which in turn forces \(Y=0\), fixes \(x=1-Z/c,w=W\), and leaves \(z\) free. If \(X>0\), necessarily \(y=\sigma\sqrt{X/a}\) with exactly two distinct signs. The other equations fix \(x=1-Z/c\), \(w=W-\sigma r\), and
\[
Y=b\sigma r\,m_\sigma(1-z).
\]
Solving this final scalar equation gives precisely the three alternatives above. Substitution into each original output component verifies sufficiency; every inverse belongs to one of those branches by the square equation, giving completeness.

**Step 2 (unique hole inside the positive half-space).** If \(X>0,Y\ne0\), a target is omitted exactly when \(m_{-1}=m_{+1}=0\). The equations are \((W-r)^2=2\) and \((W+r)^2=2\). Subtraction yields \(4Wr=0\); since \(r>0\), necessarily \(W=0\). Either equation then yields \(r=\sqrt2\), equivalently \(X=2a\). Conversely these values make both factors vanish, proving the claimed omission set \(\mathcal H\). When \(Y=0\), each branch contributes at least one point or a line, so there are no other missing points with \(X>0\). The exact image follows with the \(X=0\) analysis. Every target with \(X=0\) is a limit of image points with \(X>0\), including those with \(Y\ne0\), because one may perturb \(X\) and if necessary \(W\) to avoid \(\mathcal H\). Every omitted point in \(\mathcal H\) is similarly a limit through \(W\ne0\). Thus the closure is \(\{X\ge0\}\) and the image is not closed.

**Step 3 (critical images versus missing images).** The Jacobian determinant is the exact polynomial
\[
\det DF_{a,b,c}(x,y,z,w)=abc\,y^2(2-w^2).
\]
Consequently the full critical locus is \(\{y=0\}\cup\{w=\pm\sqrt2\}\). The first piece maps onto \(\{X=Y=0\}\). On the other two pieces \(Y=0\) and \(X=a(W\mp\sqrt2)^2\), and for each such output every \(Z\) can be realized by choosing \(x=1-Z/c\). Therefore the critical-value set is exactly
\[
\mathcal C=\{X=Y=0\}\ \cup\!
\bigcup_{\tau=\pm1}\{Y=0,\ X=a(W-\tau\sqrt2)^2\}.
\]
In particular \(\mathcal C\cap\mathcal H=\varnothing\), since \(Y\ne0\) on \(\mathcal H\).

**Step 4 (a common inverse pole at the hole).** Fix \(Y\ne0\) and \(Z\). Approach a hole target by \(T_\delta=(2a,Y,Z,\delta)\), where \(0<|\delta|<\sqrt2\). Then \(r=\sqrt2\), and for either sign
\[
m_\sigma=\sigma\sqrt2\,\delta-\frac{\delta^2}{2},
\qquad
b\sigma r\,m_\sigma=b\delta\left(2-\frac{\sigma\delta}{\sqrt2}\right).
\]
Both factors are nonzero, so there are two regular inverse points. Their \(z\)-coordinates are exactly
\[
z_\sigma(\delta)=1-\frac{Y}{b\delta(2-\sigma\delta/\sqrt2)}
=-\frac{Y}{2b\delta}+O(1).
\]
The remaining input coordinates \(x=1-Z/c\), \(y=\sigma\sqrt2\), \(w=\delta-\sigma\sqrt2\) remain bounded. Hence both inverse branches diverge, with identical leading poles, while their images converge to the omitted value. This is an explicit failure of properness, not a Jacobian fold at a finite inverse point.

## Verification

The included standalone `check.py` uses SymPy to recompute the Jacobian determinant, verify both inverse branches algebraically, test the exact inverse cases, confirm the simultaneous-zero criterion, and calculate the two common pole residues. The proof above, not finite testing, establishes the unrestricted real-parameter statement. Reproduce with `python check.py` and SymPy installed.

## Relationship to prior work

Wang, Tong, Li, Zhang, Iu and Li (2023) introduce exactly this map in their Equation (14), set the memristance constants in their Equation (13), and study equilibrium-line stability, Lyapunov spectra, numerical bifurcations, attractor coexistence and hardware implementation. Their article does not state the global one-step image, full inverse fibers, the interior omitted-output stratum, its separation from the critical values, or the common two-branch inverse pole. Related results about 3D parabolic maps and other memristive maps do not imply an inverse theorem for this four-dimensional memory-coupled polynomial. The calculations use elementary algebra but the global inverse geometry is a new map-specific statement within inspected sources.

## Limitations

No assertion is made about typical forward orbits, positive-measure attractor basins, cryptographic security, or a bounded-state restriction. The two-branch pole concerns targets approaching \(\mathcal H\) along the specified path; no universal blow-up rate is asserted for all possible target paths. The comparison with accessible literature cannot rule out unindexed equivalent prior results. Independent mathematical validation remains unperformed.

## References

1. M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu, and Z. Li, "A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor," *Symmetry* **15** (2023), 1879, published 6 October 2023. https://doi.org/10.3390/sym15101879
2. Published mathematical result: "A golden-ratio sink boundary and complete primitive two-cycle census for a three-dimensional parabolic map" (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-golden-ratio-sink-boundary-and-complete-primitive-two-cycle-ce--37fa6309f5c1 (comparison only; different three-dimensional system).
3. Published mathematical result: "Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map" (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-singular-zero-to-infinite-inverse-valence-transition-in-a-cosine--8b96b0ec53ba (comparison only; different two-dimensional system).
