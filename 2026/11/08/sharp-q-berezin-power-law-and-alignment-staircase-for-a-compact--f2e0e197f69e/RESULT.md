# Sharp \(q\)-Berezin power law and alignment staircase for a compact geometric Hardy shift

## Finding

Let \(H^2(\mathbb D)\) be the classical complex Hardy space and let \(S_\beta f(z)=z f(\beta z)\), where \(0<\beta<1\). Fix \(0<q\le1\). For each integer \(m\ge2\), set \(\alpha=\beta^m\) and \(k=\sqrt{1-q^2}\). The \(q\)-Berezin range of \(S_\beta^m\), formed using normalized Hardy reproducing kernels with inner product exactly \(q\), is the **closed disk** centered at zero with radius
\[
\operatorname{ber}_q(S_\beta^m)=\beta^{m(m-1)/2}\frac{q\,u_m^m(1-u_m^2)}{1-(1-\beta^m)ku_m-\beta^m u_m^2}.
\]
Here \(u_m\) is the **unique** root in \((0,1)\) of
\[
\begin{split}
0={}&m-(m-1)(1-\beta^m)ku
-[m+2+\beta^m(m-2)]u^2\\
&+(m+1)(1-\beta^m)ku^3+m\beta^m u^4.
\end{split}
\]
The root satisfies \(u_m>k/(1+q)\). All norming kernel pairs, up to joint rotation, have second point \(b=u_m\) and first point \(a=(u_m-k)/(1-ku_m)\).

The relative orientation of these points is antipodal, touches the origin, or aligned according as
\[
q^2<\frac{1-\beta^m}{m+1-\beta^m},\qquad
q^2=\frac{1-\beta^m}{m+1-\beta^m},\qquad
q^2>\frac{1-\beta^m}{m+1-\beta^m},
\]
respectively. The threshold on the right is strictly decreasing in \(m\): for fixed \(q\), increasing powers undergo at most one change from antipodal to aligned, with the transitional origin case possible at most once.

Most importantly, there is the sharp **power asymptotic**
\[
\boxed{\lim_{m\to\infty}\frac{m\operatorname{ber}_q(S_\beta^m)}{\|S_\beta^m\|}
=\frac{2q}{e(1-\sqrt{1-q^2})}},\qquad
\|S_\beta^m\|=\beta^{m(m-1)/2}.
\]
The limit is independent of the damping parameter \(\beta\). Equivalently, the \(q\)-Berezin radius loses the sharp factor \(1/m\) relative to the operator norm, even though that norm already decays superexponentially. The maximizing second kernel point obeys \(m(1-u_m)\to1\).

## Assumptions and scope

Fix \(0<\beta<1\), \(0<q\le1\), and integer \(m\ge2\). Let \(K_a(z)=\sqrt{1-|a|^2}/(1-\overline a z)\), \(|a|<1\). The prescribed-overlap \(q\)-Berezin range is
\[
\operatorname{Ber}_q(T)=\{\langle TK_a,K_b\rangle:\ a,b\in\mathbb D,\ \langle K_a,K_b\rangle=q\}.
\]
The inner product is linear in its first variable. The radius is the supremum of the moduli of these values. No claim is made for \(q=0\), \(\beta=1\), or arbitrary weighted shifts.

## Proof

**1. Powers and exact kernel pairing.** The monomial basis gives \(S_\beta z^j=\beta^jz^{j+1}\), whence
\[
S_\beta^m f(z)=\beta^{m(m-1)/2}z^m f(\beta^m z).
\]
Thus the scalar factor is \(\|S_\beta^m\|\). Write \(W_{\alpha,m}f(z)=z^m f(\alpha z)\) with \(\alpha=\beta^m\). For any prescribed-overlap pair,
\[
\langle W_{\alpha,m}K_a,K_b\rangle=q\,b^m\frac{1-\overline a b}{1-\alpha\overline a b}.
\]
The positive-real overlap constraint forces \(\overline a b\) to be real, so the two points are collinear with the origin. Swapping them preserves the constraint and the last fraction while replacing \(|b|^m\) by \(|a|^m\). A norming pair therefore has \(|b|\ge|a|\). Simultaneously rotate both points so \(b=s\ge0\), \(a=r\in(-1,1)\). Solving
\[
q=\frac{\sqrt{(1-r^2)(1-s^2)}}{1-rs}
\]
under \(s\ge|r|\) yields \(s\ge h=k/(1+q)\) and \(r=(s-k)/(1-ks)\). (The other hyperbolic branch has \(|r|>s\).) The modulus is consequently
\[
F(s)=\frac{q\,s^m(1-s^2)}{D(s)},\qquad
D(s)=1-(1-\alpha)ks-\alpha s^2>0,\qquad h\le s<1.
\]
The same formula with \(r=(s-k)/(1-ks)\) defines valid kernel pairs for every \(0\le s<1\), even when \(s<h\); thus it also supplies a continuous path from value zero to any attained maximum.

**2. A unique exact maximum.** Differentiation gives
\[
F'(s)=\frac{q s^{m-1}P(s)}{D(s)^2},
\]
where
\[
P(s)=m-(m-1)(1-\alpha)ks-[m+2+\alpha(m-2)]s^2
+(m+1)(1-\alpha)ks^3+m\alpha s^4.
\]
We have \(P(0)=m>0\), \(P(1)=-2(1-\alpha)(1-k)<0\). Moreover \(P'(0)=-(m-1)(1-\alpha)k\le0\), \(P'(1)=-2(m+2)(1-\alpha)(1-k)<0\), and
\[
P^{(3)}(s)=6(m+1)(1-\alpha)k+24m\alpha s\ge0.
\]
Therefore \(P'\) is convex on \([0,1]\) and lies below its nonpositive endpoint chord, strictly below zero for \(0<s<1\). Hence \(P\) has exactly one zero \(u_m\in(0,1)\). Using \(k=2h/(1+h^2)\), direct simplification gives
\[
P(h)=\frac{m(1-h^2)^2(1+\alpha h^2)}{1+h^2}>0,
\]
so \(u_m>h\). The unique peak is therefore admissible and is the global maximum; swapping and strict increase/decrease show the asserted kernel-pair classification. A joint rotation by \(\theta\) multiplies the value by \(e^{im\theta}\). Along the continuous kernel path \(s\in[0,u_m]\), the radius grows continuously from zero to the peak. It follows that the full range is precisely the closed disk.

**3. The one-way alignment transition.** Substitution gives
\[
P(k)=q^2\big((m+1-\alpha)q^2-(1-\alpha)\big).
\]
As \(P\) is strictly decreasing, the sign of \(u_m-k\), hence of \(a=(u_m-k)/(1-ku_m)\), is the sign of \(q^2-(1-\alpha)/(m+1-\alpha)\). For \(\alpha=\beta^m\), write the critical threshold as
\[
\frac{1-\beta^m}{m+1-\beta^m}
=\frac1{1+m/(1-\beta^m)}.
\]
Since \(t\mapsto1-\beta^t\) is strictly concave on positive \(t\) and vanishes at zero, \((1-\beta^m)/m\) is strictly decreasing; thus the critical threshold decreases strictly to zero. This proves the one-way phase staircase.

**4. Sharp high-power limit.** Put \(\alpha_m=\beta^m\). The denominator \(D_m(s)\) converges uniformly on \([0,1]\) to \(1-ks\), which has positive minimum \(1-k\) for fixed \(q>0\). The trial point \(s=1-1/m\) yields \(F_m(s)\ge c/m\) for all sufficiently large \(m\), whereas \(F_m(s)\) is exponentially small uniformly on \(s\le1-\varepsilon\). Consequently the unique maximizer \(u_m\to1\). At its critical point the logarithmic derivative vanishes:
\[
\frac m{u_m}-\frac{2u_m}{1-u_m^2}-\frac{D'_m(u_m)}{D_m(u_m)}=0.
\]
Here the last fraction stays bounded. Multiply by \(1-u_m\) and take the limit to get \(m(1-u_m)\to1\). It follows that \(u_m^m\to e^{-1}\), \(m(1-u_m^2)\to2\), and \(D_m(u_m)\to1-k\). Hence \(mF_m(u_m)\to2q/[e(1-k)]\), proving the claimed limit after restoring \(\beta^{m(m-1)/2}\).

## Verification

A standalone diagnostic script `checks/checker.py` evaluates the quartic, kernel formula, global scalar maximization against dense finite grids, alignment transition, and convergence to the asymptotic constant across independently selected parameters. It records 8,493 passing finite assertions. Independently, symbolic expansion gives an identically zero residual between \(F' D^2/(qs^{m-1})\) and the stated quartic, and verifies the endpoint, origin-threshold, and third-derivative identities. All universal statements and limits are proved above, not inferred from finite tests.

## Relationship to prior work

Bhattacharya and Patra (2026), Theorem 3.18 and Corollary 3.19, give disk geometry for **one-step** real weighted shifts, including geometric weights; their Remark 3.20 gives a conditional stationary-value prescription for the first power. An existing sharp first-power calculation also determines the first-power quartic and alignment transition. Those facts are prior-covered and are **not** claimed new. The new object is the entire sequence of powers of one fixed compact geometric shift. The exact \(m\)-step maximizer, strictly monotone alignment staircase, and sharp universal limiting ratio of \(q\)-Berezin to operator norm do not follow from the one-step formula or the general disk-geometry statement without the new analysis.

Mahapatra et al. (2026) treat \(q\)-Berezin ranges of weighted shifts on the **Bergman** space and sectorial inequalities; this has a different reproducing kernel and does not establish the present Hardy power law. Nearby numerical-radius research on geometrically weighted shifts concerns ordinary spatial numerical radii or other operator families, not the prescribed-kernel-overlap power asymptotic.

## Limitations

The asymptotic is for fixed \(0<q\le1\) and fixed \(0<\beta<1\); it is **not uniform** as \(q\downarrow0\) or \(\beta\uparrow1\). No assertion is made for arbitrary complex damping, for general weighted shifts, or for unnormalized test vectors. The earlier first-power case is excluded from the new theorem. Novelty remains subject to possible prior work on Berezin powers phrased using another kernel or weighted-composition formalism; absence of a search hit alone does not prove publication priority. No independent mathematical audit has been performed.

## References

1. Debarati Bhattacharya and Arnab Patra, *\(q\)-Berezin Range of Operators in Hardy Space*, arXiv:2601.02334 (first public version 2026-01-05), especially Theorem 3.18, Corollary 3.19, and Remark 3.20; https://arxiv.org/html/2601.02334v2.
2. Saikat Mahapatra, Subhadip Halder, Riddhick Birbonshi, Arnab Patra, and Kallol Paul, *\(q\)-Berezin sectorial operators with applications to \(q\)-Berezin number inequalities and \(q\)-Berezin ranges*, arXiv:2608.21723 (first public version 2026-08-22), Section 3, especially Theorem 3.11; https://arxiv.org/abs/2608.21723.
