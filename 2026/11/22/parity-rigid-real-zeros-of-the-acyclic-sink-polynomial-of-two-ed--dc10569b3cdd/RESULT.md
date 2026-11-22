# Parity-rigid real zeros of the acyclic sink polynomial of two-edge spiders

## Finding

Let \(T_m\) be the finite simple tree consisting of a central vertex \(h\) and \(m\ge1\) internally disjoint pendant paths \(h-u_i-w_i\) of length two. Let
\[
S_m(z)=\sum_{\mathcal O\in\operatorname{AO}(T_m)}z^{s(\mathcal O)},
\]
where the sum is over distinct orientations of its \(2m\) edges, and \(s(\mathcal O)\) counts vertices of outdegree zero. Every orientation is acyclic. Then
\[
\boxed{S_m(z)=(1+3z)^m+(z-1)(1+z)^m.}
\]
Its coefficients are \(a_{m,k}=\binom{m}{k}(3^k-1)+\binom{m}{k-1}\), with binomial coefficients understood to vanish outside \(0\le k\le m\). In particular, \(S_m\) has degree \(m+1\), is divisible by \(z\) but not \(z^2\), and \(a_{m,1}=2m+1\).

**Complete real-zero census.** If \(m\) is odd, the only real zeros are \(0\) and one simple zero \(-y_m<-1\). If \(m\) is even, the only real zeros are \(0\), one simple zero \(-x_m\in(-1,-1/2)\), and one simple zero \(-y_m<-1\). Thus \(S_m\) is real-rooted exactly when \(m\in\{1,2\}\). For \(m\ge3\), its number of nonreal zeros, counted with algebraic multiplicity, is \(m-1\) if \(m\) is odd and \(m-2\) if \(m\) is even. The two negative-root branches obey
\[
\boxed{\lim_{m\to\infty}y_m/3^m=1,\qquad
\lim_{\substack{m\to\infty\\m\ \mathrm{even}}}x_m=1/2.}
\]
Only the first limit is defined for both parities. These are statements about the *acyclic orientation sink polynomial* (which equals the all-orientations sink polynomial on a tree), not about directed-star-cover polynomials.

## Assumptions and scope

The graph \(T_m\) has the distinct labelled vertices \(h,u_1,w_1,\ldots,u_m,w_m\) and exactly the edges \(hu_i,u_iw_i\) for \(1\le i\le m\). Orientations are distinguished by the direction of each labelled edge; a sink means outdegree zero. All complex roots are counted with algebraic multiplicity. A *real zero* means a distinct real root unless the statement specifies multiplicity. The cases \(m=1\) and \(m=2\) are the paths \(P_3\) and \(P_5\), respectively; for \(m\ge3\), the tree has an induced claw at \(h\).

## Proof

**Step 1: exact orientation enumerator.** Temporarily ignore whether the hub \(h\) is a sink. If the edge \(h-u_i\) points away from \(h\), the second edge may be oriented in either direction, and in both choices exactly one of \(u_i,w_i\) is a sink. Its local contribution is therefore \(2z\). If \(u_i\to h\), directing \(u_i\to w_i\) creates a sink at \(w_i\), while directing \(w_i\to u_i\) creates no sink among \(u_i,w_i\), giving \(1+z\). Choices for different arms are independent, so counting sinks away from \(h\) produces \((1+3z)^m\). The hub itself is a sink exactly when every edge incident with it is directed toward it. Those orientations have peripheral generating polynomial \((1+z)^m\) and have been counted with hub weight one rather than \(z\). Correcting their weight contributes \((z-1)(1+z)^m\). This proves the formula. Binomial expansion gives the coefficient expression; \(S_m(0)=0\), \(S_m'(0)=2m+1\), \(S_m(1)=4^m\), and the leading coefficient is one.

**Step 2: negative zero equation.** Every nonzero coefficient is positive, so \(S_m(z)>0\) for \(z>0\). Put \(z=-y\), \(y>0\). The equation for a negative zero is
\[
(1-3y)^m=(1+y)(1-y)^m.\tag{1}
\]
There is no solution with \(0<y\le1/3\): on the open interval the nonnegative quotient \((1-3y)/(1-y)\) is strictly below one, while \(1+y>1\), and the endpoint \(y=1/3\) does not satisfy (1). Also \(y=1\) is not a solution, since \(S_m(-1)=(-2)^m\ne0\).

For \(1/3<y<1\), the right side of (1) is positive. If \(m\) is odd, the left side is negative, and there is no root. If \(m\) is even, equation (1) becomes
\[
F_m(y):=\frac{1}{1+y}\left(\frac{3y-1}{1-y}\right)^m=1.
\]
Here \(F_m\) rises strictly from zero to infinity. Indeed,
\[
\frac{d}{dy}\log F_m(y)=\frac{2m}{(3y-1)(1-y)}-\frac{1}{1+y}>0,
\]
because \((3y-1)(1-y)\le1/3\) on this interval, whereas \((1+y)^{-1}<1\). Therefore there is exactly one simple solution \(x_m\in(1/3,1)\) for even \(m\). At \(y=1/2\), \(F_m(y)=2/3<1\), so in fact \(x_m\in(1/2,1)\).

For \(y>1\), both sides of (1) have the same sign \((-1)^m\), and their equality is equivalent to
\[
H_m(y):=\frac{(3+2/(y-1))^m}{1+y}=1.
\]
The numerator decreases strictly from infinity to \(3^m\), while the denominator increases strictly from two to infinity. Thus \(H_m\) decreases strictly from infinity to zero, attaining one at exactly one simple root \(y_m>1\) for every \(m\). These cases exhaust all real zeros except \(0\), which is simple by Step 1. Since the degree is \(m+1\), the stated nonreal-root counts and the exact real-rootedness boundary follow.

**Step 3: escaping and bounded negative branches.** The equation for \(y_m\) implies
\[
y_m+1=3^m\left(1+\frac{2}{3(y_m-1)}\right)^m>3^m,
\]
so \(y_m>3^m-1\). For \(m\ge2\), taking logarithms and using \(\log(1+t)\le t\) gives
\[
0<\log\frac{y_m+1}{3^m}
\le\frac{2m}{3(y_m-1)}
<\frac{2m}{3(3^m-2)}\longrightarrow0.
\]
Hence \(y_m/3^m\to1\). For even \(m\), the equation for \(x_m\) can be written
\[
\frac{3x_m-1}{1-x_m}=(1+x_m)^{1/m}.
\]
The right side tends uniformly to one for \(x_m\in(1/2,1)\), and the strictly increasing function on the left equals one only at \(x=1/2\); therefore \(x_m\to1/2\) along even integers. This proves the limits.

## Verification

The standalone standard-library script `artifacts/verify.py` independently enumerates orientations of the actual \(2m\) labelled edges for \(1\le m\le7\), counts sinks from outdegrees, and compares every coefficient against the formula. It checks \(S_m(1)=4^m\), \(S_m'(0)=2m+1\), positive coefficients, and exact rational sign witnesses for the real-root intervals for \(1\le m\le40\). The all-order real-root classification and limits are proved symbolically in Steps 2–3, not inferred from these finite computations. Execute with `python3 artifacts/verify.py` from the extracted package root.

## Relationship to prior work

Alexandersson and Maia Leite, arXiv:2610.41502v1 (first public 2026-10-30), prove acyclic sink real-rootedness for **chordal claw-free** graphs (Theorem 3.1), and all-orientations sink real-rootedness for claw-free graphs (Theorem 4.3). The graph \(T_m\) is chordal but not claw-free for \(m\ge3\), so neither theorem provides this real-root classification. Their general sink-set expansion (Proposition 2.4) defines a method for computing graph-specific coefficients, not a root-count theorem for this family. Hwang, Jung, Lee, Oh and Yu (arXiv:1910.10920) provide foundational acyclic-orientation polynomial recurrences and general combinatorial expansions, not this family-specific zero geometry.

Two related published results concern clique bouquets and square bouquets with a common hub. Their hub-gluing mechanisms and parity-dependent root counts provide close analogies, but their graph families contain neither a subdivided star with two-edge arms nor a reduction establishing this polynomial. The complete factorization, two-/three-real-zero classification, negative-root intervals, and exponentially escaping branch here concern a distinct tree family. This comparison is a best-knowledge priority assessment, not a proof that no earlier unindexed source exists.

## Limitations

The theorem concerns equal-length, two-edge arms. It does not classify unequal-length spiders, arbitrary trees, or complex-root locations beyond the exact count of nonreal zeros. The negative roots are characterized implicitly, not in radicals. The finite checker is corroborative only; it does not provide independent mathematical certification. Historical priority remains provisional, including possible graph-specific results outside searchable records.

## References

1. P. Alexandersson and L. S. Maia Leite, *Sink polynomials of line graphs and weighted matching polynomials*, arXiv:2610.41502v1 (2026-10-30), Proposition 2.4 and Theorems 3.1, 4.3. https://arxiv.org/abs/2610.41502
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh, and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920 (first public 2019-10-24), Definitions 2.1 and Sections 2–5. https://arxiv.org/abs/1910.10920
3. *Real-zero rigidity and a sharp two-petal threshold for square bouquets* (2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-real-zero-rigidity-and-a-sharp-two-petal-threshold-for-square-bo--fecde89f20dd/RESULT.md
4. *Sharp sink-polynomial root transitions in clique bouquets* (2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-sink-polynomial-root-transitions-in-clique-bouquets--08e915842a75/RESULT.md
