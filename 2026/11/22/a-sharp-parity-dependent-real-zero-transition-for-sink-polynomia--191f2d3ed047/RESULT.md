# A sharp parity-dependent real-zero transition for sink polynomials of double-star trees

## Finding
Let \(D_{2,b}\) be the labelled tree formed by joining two distinct central vertices, with two pendant leaves on the first center and \(b\) pendant leaves on the second, where \(b\ge 2\) is an integer. Let
\[
S_b(z)=\sum_{\mathcal O} z^{\operatorname{sink}(\mathcal O)},
\]
where the sum is over all orientations of its edges (all acyclic because the graph is a tree), and a sink has out-degree zero.

**Theorem.** For every integer \(b\ge2\),
\[
S_b(z)=2(1+z)^{b+2}+(z-1)\big[(1+z)^2+(1+z)^b\big]. \tag{1}
\]
The zero \(z=-1\) has multiplicity exactly two, and \(z=0\) is simple. Every other real zero is simple and less than \(-2\). The precise classification, including multiplicity, is:

- If \(b\) is even, there is exactly **one** additional real zero, lying in \(( -\infty,-2)\).
- If \(b\) is odd with \(3\le b\le13\), there are **no** additional real zeros.
- If \(b\) is odd with \(b\ge15\), there are exactly **two** additional real zeros, both in \((-1-\rho,-2)\), where \(\rho=(1+\sqrt{17})/4\).

Thus odd orders undergo a sharp creation of two simple negative real zeros at \(b=15\) (equivalently at \(19\) vertices), while even orders have one such zero throughout. As \(b\) tends to infinity through odd integers, the smaller and larger additional zeros tend respectively to \(-1-\rho\) and \(-2\). Within this family, \(S_b\) is real-rooted exactly when \(b=2\).

## Assumptions and scope
All graphs are finite, labelled, simple, undirected trees; every edge orientation is counted separately. The leaves are distinguishable. The polynomial is not the sink polynomial of the **line graph** \(L(D_{2,b})\), which is a different object. The result is for all integer \(b\ge2\), with no asymptotic restriction. Zero multiplicity is counted algebraically, whereas the numbers of additional real zeros in the classification count distinct simple zeros.

## Proof
Write \(u=1+z\). Orient the central edge from the center with two leaves toward the center with \(b\) leaves. The first center then cannot be a sink; its incident leaf edges contribute \(u^2\). The second center is a sink exactly when all its incident leaf edges point into it. Accordingly the contribution on that side is \(u^b-1+z=u^b+z-1\). Reversing the central edge gives the symmetric contribution. Adding yields (1), with the more general identity
\[
S_{a,b}(z)=2u^{a+b}+(z-1)(u^a+u^b)
\]
for a double star with \(a,b\) leaves at the centers.

For \(a=2\), set \(d=b-2\ge0\) and factor
\[
S_b(z)=u^2F_b(u),\qquad F_b(u)=2u^b+(u-2)(1+u^d). \tag{2}
\]
The value \(F_b(0)\) is \(-4\) if \(d=0\) and \(-2\) otherwise. Hence \(z=-1\) has multiplicity exactly two. We have \(F_b(1)=0\) and \(F'_b(1)=b+4>0\), so \(z=0\) is simple.

There are no other roots with \(u\ge0\). For \(0<u<1\), one has \(u^b\le u^d\) and \((2-u)(1+u^d)>2u^d\), so \(F_b(u)<0\). For \(1<u<2\), the reverse inequalities \(u^b\ge u^d\) and \((2-u)(1+u^d)<2u^d\) give \(F_b(u)>0\). For \(u\ge2\), positivity is immediate from (2).

For negative \(u\), write \(u=-t\) with \(t>0\). If \(b\) is even, then \(d\) is even and
\[
F_b(-t)=2t^{d+2}-(t+2)(1+t^d).
\]
It is negative at \(t=1\), positive for sufficiently large \(t\), and its nonzero coefficients, in descending degree order, have exactly one change of sign. Descartes' rule gives exactly one positive \(t\), counted with multiplicity, hence one simple real zero at \(z=-1-t<-2\).

Suppose \(b\) is odd, so \(d\ge1\) is odd. Then
\[
F_b(-t)=H_d(t):=t^d g(t)-(t+2),\qquad g(t)=-2t^2+t+2. \tag{3}
\]
For \(0<t\le1\), \(0<t^d\le1\), \(g(t)>0\), and \(H_d(t)\le g(t)-(t+2)=-2t^2<0\). The positive zero of \(g\) is \(\rho=(1+\sqrt{17})/4\); for \(t\ge\rho\), equation (3) is negative. Only \(1<t<\rho\) can contain roots. Here \(g(t)>0\) and \(H_d(t)\) increases pointwise as odd \(d\) increases.

We prove **the exact last-failing parameter \(d=11\)**. Put \(t=1+x\), \(x\ge0\). Direct binomial expansion gives
\[
-H_{11}(1+x)=p(x)+858x^5+1584x^6+1980x^7+1749x^8+1100x^9+484x^{10}+142x^{11}+25x^{12}+2x^{13},
\]
where \(p(x)=275x^4+22x^3-20x^2-7x+2\). For \(0\le x\le1/4\), expressing \(p(y/4)\) in the Bernstein basis \(\{\binom4j y^j(1-y)^{4-j}\}_{j=0}^4\) gives coefficients
\[
\left(2,\frac{25}{16},\frac{11}{12},\frac{19}{128},\frac{107}{256}\right),
\]
all strictly positive. For \(x\ge1/4\), \(p(1/4)=107/256>0\), \(p'(1/4)=69/16>0\), and \(p''(x)=3300x^2+132x-40>0\); hence \(p\) is increasing and positive there. Therefore \(H_{11}(t)<0\) for every \(t\ge1\). Pointwise monotonicity in \(d\) implies \(H_d(t)<0\) for all odd \(d\le11\) and all \(t>0\).

For \(d=13\), the rational test point \(t=6/5\), strictly between \(1\) and \(\rho\), yields
\[
H_{13}(6/5)=\frac{6829302128}{30517578125}>0.
\]
Since \(g(6/5)>0\), this remains positive for every larger odd \(d\). But \(H_d(1)=-2\) and \(H_d(\rho)=-(\rho+2)<0\). The intermediate value theorem therefore gives at least two roots in \((1,\rho)\). The coefficient-sign sequence of
\[
H_d(t)=-2t^{d+2}+t^{d+1}+2t^d-t-2
\]
has exactly two sign changes, and thus Descartes' rule gives at most two positive roots counted with multiplicity. The two roots are consequently distinct and simple, and no additional real zeros exist.

Finally, for any fixed \(1<t<\rho\), the term \(t^d g(t)\) tends to infinity with odd \(d\), while \(H_d(1)<0\) and \(H_d(\rho)<0\). Thus the two roots tend to \(1\) and \(\rho\), respectively. The real-rootedness statement follows by comparing the total degree \(b+2\) with the counted real-root multiplicities; for \(b=2\), equation (1) reduces to \(2z(z+1)^2(z+3)\), which is real-rooted.

## Verification
The included `verify.py` independently enumerates all \(2^{b+3}\) edge orientations for each \(2\le b\le10\), compares the sink distribution against (1), verifies the integer coefficient total, checks the exact positive-Bernstein certificate, and verifies the rational threshold witness. Run `python3 verify.py` (Python 3.10 or later; standard library only). The script prints `VERIFY_OK` if every check passes. The infinite root classification is established by the proof above, **not** by extrapolating finite computations.

## Relationship to prior work
Alexandersson and Maia Leite (arXiv:2610.41502, first public 2026-10-30) prove real-rootedness for chordal claw-free graphs and develop the sink-polynomial approach. Their Proposition 5.1 explicitly treats \(S^a_{L(D_{p,q})}\), the **line graph of a double star**, not \(S^a_{D_{p,q}}\). For \(b\ge2\), our double-star trees have an induced claw, and that real-rootedness theorem does not apply. Hwang, Jung, Lee, Oh, and Yu (arXiv:1910.10920) develop general sink-enumerator identities but do not state this parity-threshold root census. The new result is the sharp root transition at \(b=15\) and the all-order classification, not the elementary orientation decomposition in isolation.

## Limitations
This is a theorem for the one-parameter subfamily with exactly two leaves at the first center; no comparable sharp threshold for all \(D_{a,b}\) is claimed. The polynomial enumerates unweighted orientations, not a biased-orientation probability law. The originality assessment is a targeted literature comparison and cannot rule out every earlier unpublished or unindexed result. No independent mathematical review is asserted.

## References
- P. Alexandersson and L. Saud Maia Leite, *Sink polynomials of line graphs and weighted matching polynomials*, arXiv:2610.41502v1 (first public 2026-10-30), especially Theorem 3.1 and Proposition 5.1. https://arxiv.org/abs/2610.41502
- B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh, and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920v2 (2020), Definitions 2.1 and Section 3. https://arxiv.org/abs/1910.10920
