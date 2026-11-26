# Exact \(N\)-center covering radii on two-layer metric circles

## Finding

Let \(C_L=\mathbb R/L\mathbb Z\) be the circle of circumference \(L>0\), equipped with its intrinsic shortest-arc distance, and let \(D_s=\{0,1\}\) be the two-point metric space with distance \(s>0\) between its points. On \(X=C_L\times D_s\), use the sum-product metric
\[
d((x,i),(y,j))=\min_{m\in\mathbb Z}|x-y+mL|+s|i-j|.
\]
For every integer \(N\ge1\), define the optimal radius with at most \(N\) centers constrained to lie in \(X\) by
\[
R_N(L,s)=\min_{z_1,\ldots,z_N\in X}\max_{z\in X}\min_{1\le a\le N}d(z,z_a).
\]
Write \(k=\lfloor N/2\rfloor\) and \(h=\lceil N/2\rceil\). Then
\[
\boxed{\displaystyle
R_N(L,s)=\min\left\{\frac{L}{2k},\frac{L+2sh}{2N}\right\},
}
\]
where the first entry is interpreted as \(+\infty\) when \(k=0\). In particular, \(R_1=L/2+s\), and for \(N\ge2\) the transition in \(s\) occurs precisely at \(s=L/(2k)\):
\[
R_N(L,s)=\begin{cases}
\dfrac{L+2sh}{2N},&0<s\le L/(2k),\\[4pt]
\dfrac{L}{2k},&s\ge L/(2k).
\end{cases}
\]
For \(N\ge2\) below the transition, an optimal placement alternates between the two sheets, with one same-sheet adjacency when \(N\) is odd. At and above the transition separate equal-spacing covers on the two sheets are optimal. Both the threshold and the parity-dependent slopes are sharp.

## Assumptions and scope

The circle is the *intrinsic* length-metric circle, not a Euclidean chord circle. The second factor has precisely two points, not the continuous connecting interval; \(s\) is a positive metric separation, not a vertical length available for intermediate centers. All balls are closed, centers must belong to \(X\), and \(N\) counts balls with repetitions allowed, equivalently at most \(N\) distinct centers. The formula holds for all positive real \(L,s\), all integers \(N\ge1\), and all boundary parameter values. It makes no assertion about higher-point second factors or other product norms.

## Proof

**1. Lower bound.** Fix a covering by at most \(N\) closed balls of radius \(r>0\). Let \(n_0,n_1\) denote the numbers of centers in sheets 0 and 1, padding with repeated centers if needed, so \(n_0+n_1=N\). A ball of radius \(t\ge0\) on \(C_L\) has arclength at most \(2t\). If \(r<s\), no ball reaches the opposite sheet, so each sheet requires at least \(\lceil L/(2r)\rceil\) centers. For \(k\ge1\), a radius \(r<L/(2k)\) would require at least \(k+1\) centers in each sheet, more than \(N\) in total. If \(k=0\), a single center cannot cover both sheets at radius \(r<s\).

If \(r\ge s\), a center in sheet \(i\) covers an arc of radius \(r\) in its own sheet and an arc of radius \(r-s\) in the opposite sheet. Comparing arclengths in both target sheets gives
\[
L\le2rn_0+2(r-s)n_1,
\qquad L\le2rn_1+2(r-s)n_0.
\]
Taking the smaller right-hand side and using \(\max(n_0,n_1)\ge h\) yields
\[
L\le2rN-2s\max(n_0,n_1)\le2rN-2sh,
\]
so \(r\ge (L+2sh)/(2N)\). Therefore no radius below both proposed candidates can cover \(X\).

**2. Separate-sheet construction.** If \(N\ge2\), put \(k\) equally spaced centers in each sheet. Every point of either circle lies within circular distance \(L/(2k)\) of a center on its own sheet. An unused extra center is permitted for odd \(N\).

**3. Mixed-sheet construction.** Set
\[
b=\frac{L+2sh}{2N},\qquad a=\frac{L}{2k}\quad(k\ge1).
\]
For \(k\ge1\), \(b<a\) exactly when \(s<a\), and then \(b>s\). It suffices to construct a radius-\(b\) cover in that regime. For \(N=1\), one center in sheet 0 covers its own circle within \(L/2\) and the opposite circle within \(L/2+s=b\).

For a directed gap of length \(g\) between consecutive projected centers, suppose the center at its start covers an arc of radius \(u\) in the target sheet, and the center at its end covers an arc of radius \(v\). A point at length \(x\) along the gap has circular distances at most \(x\) and \(g-x\) from the two projections. Thus \(u+v\ge g\) ensures the entire gap is covered. When \(u+v=g\), the two covered segments of that gap meet at distance \(u\) from its start, not necessarily at the midpoint.

For even \(N\ge2\), put \(N\) cyclically equally spaced centers on \(C_L\), with sheet labels \(0,1,0,1,\ldots\). Consecutive points are separated by \(L/N=2b-s\). In either target sheet the two radii for each gap are \(b\) and \(b-s\), with sum \(2b-s\). The gaps are all covered.

For odd \(N\ge3\), place sheet labels \(0,1,0,1,\ldots,0\) cyclically. Give each gap between unlike labels length \(2b-s\), and the sole gap between two 0 labels length \(2(b-s)\). These numbers are positive in the strict mixed regime and their sum is
\[
(N-1)(2b-s)+2(b-s)=2Nb-(N+1)s=L,
\]
so these gaps define a placement around the circle. In both sheets, the two radii across an unlike-label gap sum to its length. Across the special gap, the radii sum to \(2(b-s)\) in sheet 1 and to \(2b\) in sheet 0. In each sheet and for each gap the gap criterion applies. At \(s=a\) the two candidate radii coincide, and the separate-sheet construction attains that radius.

Combining the lower bound and both constructions proves the formula and the transition. \(\square\)

## Verification

The attached standalone `checker.py` uses exact rational arithmetic. It constructed covers for 7,200 rational parameter triples \((L,s,N)\) with \(1\le N\le15\); checked both sheet arcs cover the entire circle without sampling individual points; and checked strict lower-bound certificates for two slightly smaller radii in each case. Run with `python checker.py`; it uses only Python's standard library. These tests are finite consistency checks; the universal real-parameter theorem is proved by the arc-length argument and explicit constructions above.

## Relationship to prior work

Cieliebak and Cieliebak formulate a sum-product covering-number conjecture and prove a tree-factor bound. The latter applies to the two-point factor, which embeds isometrically in a segment. It recovers the separated-sheet counting obstruction for \(r<s\); for \(r\ge s\) the covering number of \(D_s\) is one and that product bound does not give the sharper sheet-balance bound above. Their graph-cycle and continuous Finsler results do not give the all-radius spectrum for this circle with a discrete fiber. Allagan studies the domination number and minimum-dominating-set enumeration of finite unit-edge prism graphs, not the continuous circle with arbitrary radius and separation. The classical one-circle radius and elementary arc-length bounds are standard ingredients.

## Limitations

The product has a discrete two-point fiber. Permitting intermediate centers in a geometric cylinder or metric ladder changes the problem. The formula gives explicit optimal placements but does not characterize all minimizing placements or resolve the general product-covering conjecture. The prior-work comparison is limited to the sources inspected and does not certify publication priority.

## References

1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, first public version 2026-11-11. https://arxiv.org/abs/2611.15599
2. J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488v1, first public version 2026-01-07. https://arxiv.org/abs/2601.03488
