# Sharp quadratic-scale Crofton tails and positive moments of cross-polytope sections

## Finding

Let \(d\ge3\), let \(C_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d\), and sample an unoriented affine hyperplane from Euclidean-motion-invariant hyperplane measure **conditioned on intersecting** \(C_d\). Denote the number of vertices of the generic intersection by \(V_d\), and put \(b_d=\sqrt{2\log d}\). For every fixed \(x\in(0,1)\),
\[
\boxed{\lim_{d\to\infty}b_d\Pr\{V_d>xd^2\}=\sqrt2\,\operatorname{erf}^{-1}(\sqrt{1-x}).}
\]
For every fixed real \(s>0\),
\[
\boxed{\lim_{d\to\infty}b_d\,\mathbb E(V_d/d^2)^s
 =\int_0^\infty[1-\operatorname{erf}(t/\sqrt2)^2]^s\,dt.}
\]
These are sharp positive constants and a **quadratic-scale rare-event** regime: the typical section has \(V_d/d^2\to0\) in probability, but its positive moments decay only as \(1/\sqrt{\log d}\). In particular, at \(s=1\) the integral is \(2/\sqrt\pi\), so \(\mathbb EV_d\sim\sqrt{2/\pi}\,d^2/\sqrt{\log d}\). This last mean asymptotic and the exact finite-dimensional face-vector law are *previously known*, not novel claims here. The contributions assessed here are the explicit sharp **quadratic-tail coefficient** for every fixed \(x\) and the **whole positive-moment asymptotic family**, including fractional \(s\), with the necessary uniform-integrability argument.

## Assumptions and normalization

The hyperplane distribution is the invariant measure \(d\sigma(u)\,dt\) on normals and offsets, modulo reversing both signs, conditioned on meeting the polytope. It is not uniform orientation followed by a uniform offset conditional on the given normal: under the conditioned invariant law the orientation is biased by the directional width. Hyperplanes passing through original vertices form a null set. All limits concern \(d\to\infty\), with **fixed** \(x\in(0,1)\) and fixed \(s>0\); neither statement is claimed uniformly near the endpoints or for varying moment order.

## Proof

**1. Known exact Crofton representation.** The full finite-dimensional face-vector distribution and its Gaussian sampling construction were previously established in *A joint Crofton face-vector law and common random exponent for cross-polytope sections* (2026-10-18). We recall only what is needed to derive the new asymptotics. Let \(G_1,\ldots,G_d\) be independent standard normals, let \(H_i=|G_i|\), and write \(H_{(1)}\le\cdots\le H_{(d)}\), \(H_{(0)}=0\), \(m_d=\mathbb E H_{(d)}\). Under the conditioned Crofton measure, the expected measure of offsets at which \(R_d(t):=\#\{i:H_i>t\}\) equals \(k\) is normalized by \(m_d\). A generic section with exactly \(k\) positive-side signed vertices has
\[
V_d=v_d(k):=k(2d-k-1).
\]
Consequently, for every bounded nonnegative function \(f\),
\[
\mathbb E f(V_d)=\frac1{m_d}\int_0^\infty
\mathbb E\big[f(v_d(R_d(t)))\,\mathbf 1_{\{R_d(t)>0\}}\big]dt.
\tag{1}
\]
For any threshold \(h\) with \(v_d(1)\le h<v_d(d)\), letting \(k_*(h)=\min\{k:v_d(k)>h\}\), the known exact law telescopes to
\[
\Pr(V_d>h)=\frac{\mathbb E H_{(d-k_*(h)+1)}}{m_d}.
\tag{2}
\]
The two equal top counts \(v_d(d-1)=v_d(d)\) cause no ambiguity in (2).

**2. Sharp quadratic tail.** Fix \(0<x<1\), put \(h=xd^2\), and let \(k_d=k_*(h)\). Since \(v_d(k)/d^2=(k/d)(2-k/d)+O(d^{-1})\),
\[
\frac{k_d}{d}\to q_x:=1-\sqrt{1-x}\in(0,1).
\]
By the empirical quantile law for the half-normal sample, \(H_{(d-k_d+1)}\to t_x\) in probability, where
\[
\Pr(H_1\le t_x)=1-q_x=\sqrt{1-x},\qquad
 t_x=\sqrt2\,\operatorname{erf}^{-1}(\sqrt{1-x}).
\]
The convergence holds in \(L^1\): choose any fixed \(q\in(0,q_x)\); for all large \(d\), the selected order statistic is bounded by the average of the largest \(\lceil qd\rceil\) observations and hence by \((qd)^{-1}\sum_i H_i\). The latter has uniformly bounded second moment. Finally, standard Gaussian maximum estimates give \(m_d/b_d\to1\). Substituting these results into (2) proves the sharp tail.

**3. All fixed positive moments.** At fixed \(t\ge0\), \(R_d(t)\) is binomial with parameters \(d\) and \(Q(t)=\Pr(H_1>t)=1-\operatorname{erf}(t/\sqrt2)\). By the law of large numbers,
\[
\frac{v_d(R_d(t))}{d^2}\longrightarrow Q(t)(2-Q(t))
=1-\operatorname{erf}(t/\sqrt2)^2
\]
in probability. Since \(0\le v_d(R_d(t))/d^2\le1\), the corresponding \(s\)th moments converge at each fixed \(t\). For global domination, \(v_d(r)/d^2\le 2r/d\) for \(0\le r\le d\); therefore
\[
\mathbb E\big(v_d(R_d(t))/d^2\big)^s
\le 2^sQ(t)^{\min(s,1)}.
\]
For \(s\ge1\) use \((R_d/d)^s\le R_d/d\); for \(0<s<1\) use concavity/Jensen. The bound is integrable over \(t\in[0,\infty)\) by the Gaussian tail. Thus dominated convergence applied to (1) with \(f(v)=(v/d^2)^s\), followed by \(m_d/b_d\to1\), gives the full moment limit. At \(s=1\), the constant is \(\mathbb E\max(H_1,H_2)=2/\sqrt\pi\), by the tail integral and planar Gaussian symmetry.

## Verification and relationship to earlier work

The original independent numerical `check.py` remains a supplementary finite-dimensional test of the Crofton formula for dimensions 3, 4 and 6 and of the octahedral case. It does not certify asymptotic limits. Steps 2–3 above are the mathematical proof of the claimed new asymptotics, using the **previously published** exact Crofton face law as input. In particular, *A joint Crofton face-vector law and common random exponent for cross-polytope sections* (Resultary, 2026-10-18) already proves the exact Gaussian-binomial distribution, the mean formula, and the \(\operatorname{Beta}(1,1/2)\) typical exponent. These are not claimed as new, nor is the standard Gaussian maximum estimate. Donoho–Tanner concern projections; De Loera–Lopez-Campos–Torres concern extremal section vertex counts; Kabluchko–Litvak–Zaporozhets treat Gaussian width and projection expressions. The sharp tail coefficient at positive quadratic thresholds and the full fixed-positive-moment constants are the narrower contributions. A future literature discovery could still limit their priority; negative searches do not establish uniqueness.

## References

1. *A joint Crofton face-vector law and common random exponent for cross-polytope sections* (2026-10-18), https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-joint-crofton-face-vector-law-and-common-random-exponent-for-c--cab78e198ad5 (previous exact face law, expected face counts and common exponent).
2. D. Donoho and J. Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension* (2006), arXiv:math/0607364 (projection model).
3. Z. Kabluchko, A. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables* (2015), arXiv:1511.08479 (Gaussian extrema and widths).
4. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes* (2024), arXiv:2412.12419 (extremal section-vertex counts).
