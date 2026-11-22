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
The first regime is realized by alternating the centers between the two sheets, with one necessary repeated sheet adjacency when \(N\) is odd. The second regime is realized by separate equal-spacing covers of the two sheets. Thus both the threshold and the parity-dependent slopes are sharp.

## Assumptions and scope

The circle is the *intrinsic* length-metric circle, not a Euclidean chord circle. The second factor has precisely two points, not the continuous connecting interval; \(s\) is a positive metric separation, not a vertical length available for intermediate centers. All balls are closed, centers must belong to \(X\), and \(N\) counts balls with repetitions allowed, equivalently at most \(N\) distinct centers. The formula holds for all positive real \(L,s\), all integers \(N\ge1\), and all boundary parameter values. It makes no assertion about higher-point second factors or other product norms.

## Proof

**1. The lower bound.** Fix a covering by at most \(N\) closed balls of radius \(r>0\). Let \(n_0,n_1\) denote the numbers of centers in sheets 0 and 1, padding with repeated centers if needed, so \(n_0+n_1=N\). For an ordinary radius-\(t\) arc on \(C_L\), its arclength is at most \(2t\). If \(r<s\), no ball reaches the opposite sheet; every sheet consequently requires at least \(\lceil L/(2r)\rceil\) centers. If \(k=\lfloor N/2\rfloor\) and \(r<L/(2k)\), then each sheet would require at least \(k+1\) centers, more than \(N\) in total. If \(k=0\), there is only one center and at least one sheet has none, so \(r<s\) is impossible. This counting argument for the numerical bound \(r<L/(2k)\) is needed only when \(k\ge1\).

If \(r\ge s\), a center in sheet \(i\) projects to an arc of radius \(r\) in its own sheet and radius \(r-s\) in the opposite sheet. Comparing arclengths in both target sheets gives
\[
L\le2rn_0+2(r-s)n_1,
\qquad L\le2rn_1+2(r-s)n_0.
\]
Taking the smaller right-hand side and using \(\max(n_0,n_1)\ge h\) yields
\[
L\le2rN-2s\max(n_0,n_1)\le2rN-2sh,
\]
so \(r\ge (L+2sh)/(2N)\). Therefore no radius below both proposed candidates can cover \(X\).

**2. Separate-sheet construction.** If \(N\ge2\), put \(k\) equally spaced centers in each sheet. Every point of either circle lies within circular distance \(L/(2k)\) of a center on its own sheet. Thus \(R_N\le L/(2k)\) without any condition on \(s\). An unused extra center is permitted for odd \(N\).

**3. Mixed-sheet construction.** Set
\[
b=\frac{L+2sh}{2N},\qquad a=\frac{L}{2k}\quad(k\ge1).
\]
For \(k\ge1\), direct subtraction shows \(b<a\) exactly when \(s<a\), and then \(b>s\). It suffices to construct a radius-\(b\) cover in that regime. For \(N=1\), one center in sheet 0 covers its own circle within \(L/2\) and the opposite circle within \(L/2+s=b\).

For even \(N\ge2\), put \(N\) cyclically equally spaced centers on \(C_L\), with sheet labels \(0,1,0,1,\ldots\). Consecutive points are separated by \(L/N=2b-s\). On each sheet the corresponding covering arcs have consecutive radii \(b\) and \(b-s\), whose sum is exactly this gap. They therefore cover that sheet, including endpoints.

For odd \(N\ge3\), place sheet labels \(0,1,0,1,\ldots,0\) cyclically. Give each gap between unlike labels length \(2b-s\), and the sole gap between two 0 labels length \(2(b-s)\). These numbers are positive in the strict mixed regime and their sum is
\[
(N-1)(2b-s)+2(b-s)=2Nb-(N+1)s=L,
\]
so these gaps define a legitimate placement around the circle. In sheet 1, the coverage radii in cyclic order are alternately \(b-s\) and \(b\), with two consecutive \(b-s\) arcs at the special gap. Every adjacent pair of arcs therefore touches exactly at the midpoint of its gap, and covers the circle. In sheet 0, radii are exchanged; the ordinary gaps are still exactly covered and the special gap has two radius-\(b\) arcs which overlap. Hence both sheets are covered. At \(b=a\) the separate-sheet construction already proves the required bound.

Combining the lower bound and both constructions proves the asserted formula. The inequality \(b\le a\iff s\le a\) also gives the sharp parameter transition and the claimed parity-dependent slopes. \(\square\)

## Verification

The attached standalone \(\texttt{checker.py}\) uses exact rational arithmetic. It constructed covers for 7,200 rational parameter triples \((L,s,N)\) with \(1\le N\le15\); checked both sheet arcs cover the entire circle without sampling individual points; and checked strict lower-bound certificates for two slightly smaller radii in each case. Run with `python checker.py`; it uses only Python's standard library. These tests are finite consistency checks; the universal real-parameter theorem is proved by the preceding arc-length argument and explicit constructions, not by the tests.

## Relationship to prior work

Cieliebak and Cieliebak (arXiv:2611.15599v1, 11 November 2026) formulate a sum-product covering-number conjecture, prove tree-factor special cases, and analyze graph cycles and Finsler limits. Their results neither state nor imply this complete continuous-circle-by-two-point \(N\)-center radius formula: their graph-circle argument covers discrete vertices with a fixed graph-ball radius, whereas this theorem covers every point of the intrinsic metric circle, for every real separation and every \(N\). Their conjecture is a motivation, not claimed as solved generally. Allagan (arXiv:2601.03488v1, 7 January 2026) treats the domination number and minimum-dominating-set enumeration of *finite* prism graphs, not the continuous two-sheet product metric or its arbitrary-radius spectrum. The classical one-circle radius \(L/(2N)\) and elementary arc-length bounds are standard ingredients, not claimed as new.

## Limitations

The product has a *discrete* two-point fiber; replacing it by a geometric cylinder or metric ladder changes the location of allowed centers and does not preserve the theorem. The result is deterministic and exact, but does not characterize *all* minimizing placements; it supplies explicit optimal placements. Originality is assessed against identified sources rather than independently certified exhaustively; unnoticed published priority remains possible. No claim is made about the general product-covering conjecture.

## References

1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (first public version 2026-11-11), https://arxiv.org/abs/2611.15599.
2. J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488v1 (2026-01-07), https://arxiv.org/abs/2601.03488.
