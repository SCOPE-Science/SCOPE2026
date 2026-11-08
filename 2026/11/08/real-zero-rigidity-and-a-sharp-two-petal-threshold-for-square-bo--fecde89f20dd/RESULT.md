# Real-zero rigidity and a sharp two-petal threshold for square bouquets

## Finding

For every integer \(r\ge1\), let \(Q_r\) be the simple graph obtained by identifying one vertex \(h\) of each of \(r\) otherwise disjoint copies of \(C_4\). The graph has \(3r+1\) vertices and \(4r\) edges. Define its *acyclic sink polynomial* by
\[
S_r(z)=\sum_{\mathcal O\in\operatorname{AO}(Q_r)}z^{|\operatorname{Sink}(\mathcal O)|},
\]
where each acyclic edge orientation contributes once and a sink has outdegree zero. Then
\[
\boxed{S_r(z)=(z^2+10z+3)^r+(z-1)(z+3)^r.}
\]
All real zeros of \(S_r\) are simple. There are exactly **two real zeros** for odd \(r\), and exactly **four real zeros** for even \(r\). Consequently, \(S_r\) is real-rooted exactly for \(r=1,2\), and it has nonreal zeros for every \(r\ge3\).

More precisely, put \(\alpha=-5-\sqrt{22}\) and \(\beta=-5+\sqrt{22}\). For odd \(r\), the real zeros are \(0\) and one zero in \((\alpha,-3)\). For even \(r\), they are \(0\) and one zero in each of \(( -\infty,\alpha)\), \((\alpha,-3)\), and \((-3,\beta)\). The degree is \(2r\). Hence the exact number of nonreal zeros, counted with multiplicity, is \(2r-2\) for odd \(r\ge3\) and \(2r-4\) for even \(r\ge4\). The number of orientations with a unique sink is \((3r+1)3^r\).

## Assumptions and scope

All graphs are finite, simple and labelled by their displayed vertices. Write each square as \(h,a_i,b_i,c_i,h\); no vertices or edges of different squares overlap except for the common hub \(h\). An orientation is acyclic if it has no directed cycle. All zeros refer to complex zeros counted with algebraic multiplicity unless declared distinct.

The result is about *acyclic* sink polynomials, not the polynomial of all orientations. No restriction on the number of sinks is imposed in the enumeration. The one-square endpoint \(r=1\) is included, but the graph acquires an induced claw when \(r\ge2\).

## Proof

**1. Local orientation counts.** A copy of \(C_4\) has \(2^4-2=14\) acyclic orientations: only its two directed cycles must be excluded. Ignore the sink status of the hub \(h\) and count sinks among the other three vertices. An exact enumeration of the four edge directions gives the counts \(3,10,1\) for respectively \(0,1,2\) peripheral sinks. Thus the local polynomial is
\[
T(z)=3+10z+z^2.
\]
Among the same 14 orientations, exactly four make \(h\) a sink. Three of these have no peripheral sink, and one has one peripheral sink, giving
\[
B(z)=3+z.
\]
For a direct derivation of the second table, orient the two edges incident with \(h\) toward \(h\); the remaining two edges may independently point either way. The unique arrangement with the middle vertex \(b_i\) also a sink has the two middle edges pointing into \(b_i\).

**2. Gluing at the hub.** Every simple cycle of \(Q_r\) lies entirely inside one square, so an orientation of \(Q_r\) is acyclic if and only if its restriction to every square is acyclic. The orientations of distinct squares can therefore be chosen independently. Counting peripheral sinks contributes \(T(z)^r\). In this product the hub is initially ignored; it is a sink of the entire graph exactly when it is a sink of every square. For precisely these orientations, the weight needs to be multiplied by \(z\) rather than \(1\). Their peripheral-sink polynomial is \(B(z)^r\), and the adjustment is \((z-1)B(z)^r\). This proves the displayed formula without double counting.

**3. Reduction to a monotone rational function.** Set
\[
\alpha=-5-\sqrt{22},\quad \beta=-5+\sqrt{22},\quad
R(z)=\frac{z^2+10z+3}{z+3}=z+7-\frac{18}{z+3}.
\]
We have \(\alpha<-3<\beta<0\), and \(R'(z)=1+18/(z+3)^2>1\) wherever defined. Since \(S_r(-3)=(-18)^r\ne0\), every real zero satisfies
\[
R(z)^r=1-z.
\]
For \(z\ge0\), the equality holds only at \(z=0\): on \([0,1)\), \(R(z)\ge R(0)=1\) while \(1-z\le1\), with equality only at \(0\); for \(z\ge1\), the left-hand side is positive and the right-hand side is nonpositive.

On \(( -\infty,1)\), put \(H_r(z)=(1-z)^{1/r}>0\). The rational function \(R\) is positive exactly on \((\alpha,-3)\) and \((\beta,1)\) within this domain, and is negative on \((-\infty,\alpha)\) and \((-3,\beta)\). In either positive interval, \(R-H_r\) is strictly increasing, since \(R'>0\) while \(H_r'<0\). On \((\alpha,-3)\), it changes from a negative value to \(+\infty\); on \((\beta,1)\), its unique zero is \(0\) because \(R(0)=H_r(0)=1\). Thus \(R=H_r\) has exactly these two simple solutions.

**4. Parity of the number of petals.** For odd \(r\), \(R(z)^r=1-z>0\) requires \(R=H_r\). Hence there are precisely the two real zeros already found. For even \(r\), there are also solutions to \(R=-H_r\), necessarily in \((-\infty,\alpha)\) or \((-3,\beta)\). Set \(J_r(z)=R(z)+H_r(z)\). On both intervals \(z<0\), and
\[
J_r'(z)=1+\frac{18}{(z+3)^2}-\frac1r(1-z)^{1/r-1}>1-\frac1r>0.
\]
The inequality uses \(r\ge2\), \(1-z>1\), and \(1/r-1<0\). As \(z\) goes from \(-\infty\) to \(\alpha\), \(J_r\) increases from \(-\infty\) to a positive value. As \(z\) goes from \(-3\) on the right to \(\beta\), it increases from \(-\infty\) to a positive value. There is exactly one simple zero in each interval. These four zeros exhaust the possibilities.

The strict monotonicity also establishes that each crossing is transverse, so all real zeros are simple (including \(0\)). The polynomial has degree \(2r\): for \(r\ge2\), the first term has degree \(2r\) whereas the second has degree \(r+1\), with no cancellation of the leading term; for \(r=1\), the polynomial is \(2z(z+6)\). The exact real-rootedness and nonreal-root counts follow.

**5. Unique sinks.** Differentiating at zero and using \(T(0)=B(0)=3\), \(T'(0)=10\), and \(B'(0)=1\) gives
\[
S_r'(0)=10r3^{r-1}+3^r-r3^{r-1}=(3r+1)3^r.
\]
Since \(S_r(0)=0\), this coefficient counts precisely the one-sink orientations.

## Verification

The accompanying standalone script `artifacts/verify.py` independently builds the graph, enumerates all \(2^{4r}\) edge directions for \(1\le r\le4\), discards cyclic orientations via a topological-sort test, and counts sinks from actual outdegrees. It checks the local \(C_4\) tables, every coefficient for these four cases, the identity \(S_r(1)=14^r\), the unique-sink coefficient, degree and coefficient positivity for \(1\le r\le100\). Its successful output ends in `VERIFY_OK`. Additional exact symbolic root counting for \(1\le r\le10\) agrees with the proof (one negative root when \(r\) is odd; three when even, besides zero). Finite checks are not substituted for the root-count proof.

## Relationship to prior work

Alexandersson and Maia Leite (arXiv:2610.41502v1, first public version 2026-10-30) prove real-rootedness for acyclic sink polynomials of chordal claw-free graphs and enumerate sinks on a single cycle (Proposition 3.21). Their all-orientations real-rootedness theorem concerns a different polynomial. A square bouquet with at least two petals is nonchordal and contains an induced claw, so neither stated hypothesis covers it. Their paper also gives a non-real-rooted example among line graphs of unicyclic graphs, different from the present explicit family and root-count classification. Hwang, Jung, Lee, Oh and Yu (arXiv:1910.10920) develop general acyclic-orientation-polynomial formulas and deletion-contraction recurrences. These provide a framework but do not directly state this two-/four-real-root law.

The separate family of *clique* bouquets has a different local factorization and does not contain a four-cycle block: a result for clique bouquets does not imply the present root count. The contribution here is the exact \(C_4\)-bouquet formula together with the sharp threshold at two petals and the complete parity-dependent real-root classification. This historical comparison is not an assertion of global priority.

## Limitations

The theorem treats squares sharing one vertex. It does not classify heterogeneous cycle lengths, cycles attached at multiple articulation points, or arbitrary cactus graphs. For \(r\ge3\), the exact nonreal-root count is proved, but no closed radical formula for the individual nonreal zeros is claimed. The mathematical derivation and finite checks are not an independent audit; historical priority remains provisional.

## References

1. P. Alexandersson and L. S. Maia Leite, *Sink Polynomials of Line Graphs and Weighted Matching Polynomials*, arXiv:2610.41502v1 (2026-10-30), Sections 2, 3.1, 3.4, 5.1. https://arxiv.org/html/2610.41502v1
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh, and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920 (2019), Sections 2–5. https://arxiv.org/abs/1910.10920
