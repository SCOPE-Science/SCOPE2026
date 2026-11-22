# Sharp reentrant sink-polynomial log-concavity on complete split graphs

## Finding

Let \(G_{k,r}=K_k\vee\overline{K}_r\) for integers \(k\ge2\) and \(r\ge1\). Define \(S^{\mathrm{ac}}_{k,r}(z)\) and \(S^{\mathrm{all}}_{k,r}(z)\) by counting graph orientations by their number of sinks, respectively over acyclic orientations and over all orientations. Then
\[
S^{\mathrm{ac}}_{k,r}(z)=k!\bigl[(z+k)^r+k^r(z-1)\bigr],
\]
\[
S^{\mathrm{all}}_{k,r}(z)=2^{\binom{k}{2}}\bigl[(z+2^k-1)^r+k2^{(k-1)(r-1)}(z-1)\bigr].
\]
For \(r\ge3\), their coefficient sequences (in ascending degree, including the constant coefficient) are log-concave **exactly** under these respective conditions:
\[
\begin{aligned}
S^{\mathrm{ac}}_{k,r}\text{ log-concave}&\iff r(r+1)\ge 2k(r-2),\\
S^{\mathrm{all}}_{k,r}\text{ log-concave}&\iff r(r+1)(2^k-1)^{r-1}\ge 2(r-2)k2^{(k-1)(r-1)}.
\end{aligned}
\]
Both are log-concave for \(r=1,2\). Thus the acyclic sink-polynomial log-concavity is **reentrant** as the independent-class size grows: for the fixed clique size \(k=6\), it holds exactly for \(1\le r\le3\) and \(r\ge8\), and fails exactly for \(4\le r\le7\). In contrast, the all-orientations polynomial at \(r=3\) first fails log-concavity at \(k=24\).

Both polynomials are real-rooted exactly when \(r\le2\). For odd \(r\ge3\) each has exactly one real zero (at \(0\) for the acyclic polynomial, negative for the all-orientations polynomial); for even \(r\ge4\) each has exactly two distinct real zeros (\(0\) and one negative for the acyclic polynomial, two negatives for the all-orientations polynomial). Thus loss and recovery of log-concavity do not coincide with recovery of real-rootedness.

## Assumptions and scope

Graphs are finite, simple and labelled. The graph \(G_{k,r}\) has a clique on \(k\) vertices and an independent set on \(r\) vertices, with every clique vertex adjacent to every independent vertex. Each orientation assigns one direction to each edge. A sink has outdegree zero. Acyclic orientations have no directed cycle. Each distinct edge-orientation configuration is counted once. Log-concavity of \(\sum_{j=0}^{r}a_jz^j\) means \(a_j^2\ge a_{j-1}a_{j+1}\) at every internal index \(j\), including zero coefficients where present. All formulas and classifications require \(k\ge2\), \(r\ge1\); there is no assertion about arbitrary split graphs, weighted orientations, or other graph polynomials.

## Proof

**Acyclic orientations.** The clique edges of any acyclic orientation form a transitive tournament and thus uniquely determine an order \(v_1\to\cdots\to v_k\), in \(k!\) ways. For any independent vertex \(w\), its incident edges must follow a cut in this order: for one integer \(0\le j\le k\), the first \(j\) clique vertices point toward \(w\) and \(w\) points toward the remaining clique vertices. A non-cut pattern contains a directed triangle. Conversely, choosing a cut for every independent vertex gives an acyclic orientation: any directed cycle would have to visit at least two clique vertices and violate a cut, because independent vertices are pairwise nonadjacent. More explicitly, place each independent vertex into the specified gap of the ordered clique, obtaining a topological order.

The \(j=k\) cut makes \(w\) a sink; each of the other \(k\) cuts does not. No clique vertex except \(v_k\) can be a sink. The vertex \(v_k\) becomes a sink if and only if no independent vertex chose its sink cut. Counting sink contributions first from the independent vertices yields \((z+k)^r\); for the \(k^r\) configurations without an independent sink, replace weight \(1\) by \(z\) to mark \(v_k\). Multiplying by \(k!\) gives the first identity.

**All orientations.** The clique has \(2^{\binom{k}{2}}\) tournaments, and each independent vertex admits \(2^k\) incident-edge direction choices, exactly one of which makes it a sink. Hence a provisional sink enumerator is \(2^{\binom{k}{2}}(z+2^k-1)^r\). A tournament on the clique has at most one sink. Exactly \(k2^{\binom{k-1}{2}}\) of its orientations have a sink: choose it and orient all incident clique edges toward it, leaving the others arbitrary. Such a clique sink survives in the full graph precisely when every independent vertex points toward it; the other incident directions remain freely chosen, giving \(2^{(k-1)r}\) choices. In those configurations no independent vertex can be a sink. Replacing the provisional weight \(1\) for the clique sink by \(z\) gives the second identity, after factoring \(2^{\binom{k}{2}}\).

**Sharp coefficient inequalities.** For either normalized polynomial, write
\[
F(z)=(z+A)^r+C(z-1),\qquad A,C>0.
\]
The acyclic case uses \(A=k\), \(C=k^r\), and the all-orientations case uses \(A=2^k-1\), \(C=k2^{(k-1)(r-1)}\). Coefficients of degrees \(j\ge2\) are \(\binom rj A^{r-j}\); the coefficient of degree one is \(rA^{r-1}+C\); and the constant coefficient is \(A^r-C\). In the acyclic case the latter vanishes. For the all-orientations case, it is strictly positive when \(k\ge2\): already \(2^k-1>k\) and \(2^k-1>2^{k-1}\), so \((2^k-1)^r>k2^{(k-1)(r-1)}\).

The binomial coefficient sequence is log-concave. Increasing its degree-one coefficient and decreasing its constant coefficient preserve the inequality at degree one, and all inequalities at degrees \(j\ge3\) are unchanged. Only the inequality at degree two can fail. For \(r\ge3\), after dividing by the positive factor \(\frac{r(r-1)}{12}A^{r-3}\), that inequality is equivalent to
\[
r(r+1)A^{r-1}\ge 2(r-2)C.
\]
Inserting the two choices of \((A,C)\) gives exactly the conditions in the finding. For \(r=1,2\), the coefficient sequences are log-concave directly. When \(k=6\) in the acyclic condition, the difference factors as \((r-3)(r-8)\); this proves the finite failure interval and recovery. For the all-orientations case with \(r=3\), the condition simplifies to \(k\le24(1-2^{-k})^2\). It holds for integers \(2\le k\le23\), but fails for all \(k\ge24\): for the former range the right-hand side is at least \(24(3/4)^2=13.5\) if \(k\le13\), and exceeds \(23\) if \(14\le k\le23\); for the latter range it is strictly less than \(24\). The first failure is therefore exactly \(k=24\).

**Real-zero classification.** In the generic form, substitute \(y=z+A\):
\[
F(z)=y^r+Cy-C(A+1).
\]
For odd \(r\ge3\) its derivative in \(y\) is \(ry^{r-1}+C>0\), so it has precisely one real root. For even \(r\ge4\), the function is strictly convex, tends to \(+\infty\) as \(y\to\pm\infty\), and is negative at \(y=0\). Hence it has exactly two distinct real roots. All coefficients in the original polynomials are nonnegative, so their real roots are nonpositive; in the all-orientations case the constant term is positive, so they are strictly negative. In the acyclic case the constant term is zero, and thus one root is \(0\). For \(r=1\), the polynomial is linear, and for \(r=2\), the discriminant of \((z+A)^2+C(z-1)\) is \(C[C+4(A+1)]>0\). This proves the real-rootedness threshold and precise real-root census.

## Verification

The standalone standard-library checker `artifacts/verify.py` enumerates each oriented edge assignment of \(G_{k,r}\) in 15 cases with at most 15 edges. It counts sinks directly from outdegrees and detects directed cycles independently by topological elimination, then compares both resulting polynomials with the symbolic formulas. Additional integer checks test the two sharp log-concavity conditions over a grid of parameters, their exceptional boundaries, and the sum-of-coefficients identities \(S^{\mathrm{ac}}_{k,r}(1)=k!(k+1)^r\) and \(S^{\mathrm{all}}_{k,r}(1)=2^{\binom{k}{2}+kr}\). Run `python3 artifacts/verify.py`; its successful final line is `VERIFY_OK`. Enumeration is corroboration, not the proof for arbitrary \(k,r\).

## Relationship to prior work

Alexandersson and Saud Maia Leite (2026) prove real-rootedness of the acyclic sink polynomial for chordal claw-free graphs and of the all-orientations sink polynomial for claw-free graphs. Their general sink-set expansions apply to arbitrary graphs, but they do not state the coefficient-shape phase boundaries here. The complete split graphs are chordal, yet have an induced claw for \(r\ge3\), so their real-rootedness results do not cover the new failure and reentrance classification. Hwang, Jung, Lee, Oh and Yu (2019) developed general acyclic orientation polynomials and explicitly computed the four-vertex diamond, which is the \((k,r)=(2,2)\) instance of the acyclic formula; that isolated calculation is not claimed as new. The earlier clique-bouquet classification concerns a single hub linking otherwise disjoint peripheral cliques and proves strict log-concavity for its acyclic sink polynomial. Its graph family overlaps with \(K_1\vee\overline K_r\) but not the \(k\ge2\) complete split family studied here, where reentrant non-log-concavity actually occurs.

The universal sink expansions and basic real-root facts are prior theory; the claimed contribution is the explicit **two-parameter coefficient-shape phase diagram**, notably log-concavity failure and recovery in complete split graphs, together with the exact comparison of acyclic and all-orientations laws.

## Limitations

This class-specific theorem does not classify sink-polynomial log-concavity for all chordal or all split graphs. Its finite small-instance checks do not establish unrestricted correctness; that relies on the given counting bijections and coefficient inequalities. No global smallest counterexample to sink-polynomial log-concavity is asserted. Historical priority remains provisional, particularly for unindexed work on complete split orientations; independent mathematical validation has not been performed.

## References

1. P. Alexandersson and L. Saud Maia Leite, "Sink polynomials of line graphs and weighted matching polynomials", arXiv:2610.41502v1, first submitted 2026-10-30, especially Sections 2–4 and Theorems 3.1 and 4.3. https://arxiv.org/abs/2610.41502
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh, and S.-H. Yu, "Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions", arXiv:1910.10920, 2019, Definition 2.1 and Example 2.4. https://arxiv.org/abs/1910.10920
3. "Sharp sink-polynomial root transitions in clique bouquets", published 2026-11-08, RESULT.md. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-sink-polynomial-root-transitions-in-clique-bouquets--08e915842a75
