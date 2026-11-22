# Parity-rigid real-zero counts for acyclic sink polynomials of \(K_{2,n}\)

## Finding
For every integer \(n\ge2\), consider the labelled complete bipartite graph \(K_{2,n}\), with two distinguished vertices on one shore and \(n\) distinct vertices on the other. Write
\[
S_n(z)=\sum_{\mathcal O\in\operatorname{AO}(K_{2,n})}z^{|\operatorname{Sink}(\mathcal O)|},
\]
where \(\operatorname{AO}\) denotes the set of acyclic orientations and a sink has outdegree zero. Then
\[
\boxed{S_n(z)=2(z+2)^n-(z+1)^n-(2^{n+1}-1)+(2^{n+1}-2)z+z^2.}
\]
All real zeros are simple. For even \(n\ge2\), the real zeros are precisely \(0\) and one root in \(( -\infty,-2)\). For \(n=3\), the only real zero is \(0\). For every odd \(n\ge5\), the real zeros are precisely \(0\), one root in \((-5,-2)\) and one root in \((-\infty,-5)\). In particular, except at the smallest parameter, the number of real roots is determined by parameter parity and never grows with the polynomial degree.

## Assumptions and scope
All graphs are finite, simple and labelled. Each edge receives exactly one of its two possible directions, and no two distinct orientation assignments are identified by symmetry. An acyclic orientation has no directed cycle. The variable \(z\) counts sink vertices, not sink sets or strongly connected components. The theorem concerns the *acyclic* sink polynomial, not the polynomial over all orientations. The integer range is exactly \(n\ge2\). We count roots of the polynomial over the real numbers with their usual algebraic multiplicities; simplicity is established below.

## Proof
Write the two-vertex shore as \(\{a,b\}\). Every vertex \(v\) on the other shore has exactly four possible local direction states:

- \(A\): \(v\to a\) and \(v\to b\).
- \(B\): \(a\to v\) and \(b\to v\).
- \(C\): \(a\to v\to b\).
- \(D\): \(b\to v\to a\).

An orientation contains a directed cycle if and only if at least one vertex has type \(C\) and at least one has type \(D\). Sufficiency follows from the directed four-cycle they create. Necessity follows because a directed cycle in this bipartite graph must alternate between shores, and the only two vertices on the smaller shore are \(a,b\); its length is therefore four and it requires both opposite directed two-step paths. Thus the acyclic state words are exactly the union of \(\{A,B,C\}^n\) and \(\{A,B,D\}^n\), intersecting in \(\{A,B\}^n\).

When a state \(B\) occurs, neither \(a\) nor \(b\) can be a sink. Exactly the type-\(B\) vertices are sinks. If each \(B\) receives weight \(z\), inclusion-exclusion over the two acyclic alphabets gives the preliminary weighted polynomial
\[
2(z+2)^n-(z+1)^n.
\]
When no type \(B\) occurs, the \(2^{n+1}-1\) acyclic words are instead miscounted with weight one. The all-\(A\) word has both \(a\) and \(b\) as sinks, hence weight \(z^2\). Every other word without \(B\) has precisely one of \(a,b\) as a sink, hence weight \(z\). Replacing these weights yields the displayed closed polynomial. Its value at \(z=1\) is \(2\cdot3^n-2^n\), as expected from the acyclic state words.

The constant coefficient vanishes and the coefficient of \(z\) is \(n2^n-n+2^{n+1}-2>0\), so \(z=0\) is a simple root. All nonconstant coefficients are strictly positive: for degrees \(3\le j\le n\), the coefficient is \(\binom nj(2^{n-j+1}-1)>0\), with analogous positive formulas at degrees one and two. Therefore no positive real root exists.

For \(-2\le z<0\), write \(z=-t\) with \(0<t\le2\). Since \((2-t)^n\le2^n\) and
\[
1-(1-t)^n=t\sum_{j=0}^{n-1}(1-t)^j\le nt
\]
(the summands are each at most one), we have
\[
S_n(-t)\le t\bigl[n-(2^{n+1}-2)+t\bigr]<0.
\]
The last inequality holds for all \(n\ge2\) because \(n+2<2^{n+1}-2\). There is thus no nonzero real root at or to the right of \(-2\).

For \(x>0\), substitute \(z=-x-2\). Put \(A_n=2^{n+1}-6\) and \(B_n=3\cdot2^{n+1}-9\), both positive. Direct expansion yields
\[
Q_n(x):=S_n(-x-2)=(-1)^n\bigl[2x^n-(x+1)^n\bigr]+x^2-A_nx-B_n.
\]
If \(n\ge4\) is even, the leading coefficient of \(Q_n\) is positive, while every coefficient of lower degree is negative: the coefficient at degree two is \(1-\binom n2<0\), that at degree one is \(-n-A_n<0\), and the constant is \(-1-B_n<0\). Descartes' rule of signs allows precisely one positive root counting multiplicity, since \(Q_n(0)<0\) but \(Q_n(x)\to+\infty\). That root is simple. At the even boundary \(n=2\), the polynomial is \(S_2(z)=2z(z+6)\), giving the same two-root conclusion.

If \(n\ge5\) is odd, the leading coefficient of \(Q_n\) is negative, all coefficients of degrees \(2,3,\ldots,n-1\) are positive (the coefficient at degree two is \(1+\binom n2\)), and its coefficients of degrees one and zero are negative because \(n-A_n<0\) and \(1-B_n<0\). Descending degree order therefore has exactly two sign variations, allowing at most two positive roots counting multiplicity. We have \(Q_n(0)<0\) and \(Q_n(x)\to-\infty\), but
\[
Q_n(3)=4^n-2\cdot3^n-6\cdot2^{n+1}+36>0.
\]
Indeed this quantity is \(190\) at \(n=5\), and its value at \(n+1\) minus four times its value at \(n\) equals \(2\cdot3^n+24\cdot2^n-108>0\) for \(n\ge5\). There must be one simple root in each interval \((0,3)\) and \((3,\infty)\), and the sign-variation bound excludes any others. Translating back gives one root in \((-5,-2)\) and one in \((-\infty,-5)\).

Finally, at the odd boundary \(n=3\),
\[
S_3(z)=z(z^2+10z+35).
\]
The quadratic factor has negative discriminant, so \(0\) is its sole real zero. This completes the proof for every integer \(n\ge2\).

## Verification
The accompanying standalone `verify.py` independently loops over all \(4^n\) directions of the \(2n\) labelled edges for each \(2\le n\le8\). It detects directed cycles by Kahn topological elimination, tallies sinks from outdegrees, and compares every coefficient against the formula. Additional exact-integer checks verify the sign patterns and the witness inequality for \(2\le n\le200\). The checker prints `VERIFY_OK` upon success. The infinite theorem is established by the symbolic argument above, not by finite enumeration.

## Relationship to prior work
Alexandersson and Maia Leite (arXiv:2610.41502, initially public 2026-10-30) establish real-rootedness of the acyclic sink polynomial for chordal claw-free graphs and of the all-orientation sink polynomial for claw-free graphs. The family \(K_{2,n}\) for \(n\ge3\) contains induced claws and is not chordal, so neither theorem determines its acyclic real-zero census. Hwang, Jung, Lee, Oh and Yu (arXiv:1910.10920) give general acyclic orientation sink generating formulas for arbitrary graphs, but do not state the above parity-root classification. Ayyer, Hathcock and Tetali (arXiv:2010.11236) count acyclic orientations and orientations with a unique sink of complete bipartite graphs; counting one coefficient or the total does not imply the full complex-root geometry. The novelty asserted here is the explicit **all-order real-root classification** and its sharp exceptional boundary, not the invention of sink generating functions or acyclic-orientation counting.

## Limitations
Historical priority is qualified: algebraically equivalent root classifications could be hidden in an older unindexed graph-polynomial source. General algorithms for evaluating sink polynomials are not excluded as antecedents, but their existence is distinct from proving the sign-variation boundary here. Nothing is claimed for complete bipartite graphs with both shores larger than two or for all-orientation sink polynomials. The finite checker is independent corroboration of the counted coefficients, not a certificate of the infinite root statement. No independent external mathematical validation has been performed.

## References
1. P. Alexandersson and L. S. Maia Leite, *Sink Polynomials of Line Graphs and Weighted Matching Polynomials*, arXiv:2610.41502 (first public 2026-10-30), https://arxiv.org/html/2610.41502v1.
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic Orientation Polynomials and the Sink Theorem for Chromatic Symmetric Functions*, arXiv:1910.10920, https://arxiv.org/abs/1910.10920.
3. A. Ayyer, D. Hathcock and P. Tetali, *Toppleable Permutations, Excedances and Acyclic Orientations*, arXiv:2010.11236, https://arxiv.org/abs/2010.11236.
