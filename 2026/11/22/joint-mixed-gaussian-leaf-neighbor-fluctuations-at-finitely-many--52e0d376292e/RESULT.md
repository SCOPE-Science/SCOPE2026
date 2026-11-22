# Joint mixed-Gaussian leaf-neighbor fluctuations at finitely many preferential-attachment hubs

## Finding

In a degree-proportional preferential-attachment tree grown from one edge, take any fixed number \(r\ge1\) of distinct birth-labelled vertices \(v_1,\ldots,v_r\). Write \(D_{v,n}\) for degree and \(L_{v,n}\) for the number of neighboring leaves at tree size \(n\). There are positive, finite, possibly dependent random variables \(W_{v_1},\ldots,W_{v_r}\) such that \(D_{v,n}/\sqrt n\to W_v\) almost surely. Jointly with those limits, the centered leaf-neighbor counts obey

\[
\left(\frac{L_{v_i,n}-D_{v_i,n}/2}{n^{1/4}}\right)_{i=1}^r
\Longrightarrow
\left(\frac{\sqrt{W_{v_i}}}{2} Z_i\right)_{i=1}^r,
\]

where the \(Z_i\) are independent standard normals independent of the entire vector of \(W\)'s. In fact the conditional Gaussian convergence is stable relative to the tree's infinite-growth sigma field. Consequently,

\[
\left(\frac{L_{v_i,n}-D_{v_i,n}/2}{\sqrt{D_{v_i,n}}}\right)_{i=1}^r
\Longrightarrow \mathcal N_r(0,\tfrac14 I_r).
\]

In particular, at finitely many specified old hubs, the centered leaf fraction has a universal variance \(1/4\) when standardized by the actual degree. The growing hub sizes remain dependent, but their limiting studentized fluctuations are independent.

## Assumptions and scope

Start at \(n=2\) with the edge joining vertices \(1\) and \(2\). For every integer \(n\ge2\), attach vertex \(n+1\) to a unique existing vertex \(u\), independently of future steps, with conditional probability \(D_{u,n}/[2(n-1)]\). There are no loops, parallel edges, additional edges per arrival, offsets, or changes of attachment rule. A marked vertex is born at a fixed deterministic label, not selected uniformly from all vertices of the final graph. The number \(r\) of marked vertices is fixed as \(n\to\infty\); the statement does not assert uniformity for a growing set of marks or a functional central limit theorem.

Set \(A_{v,n}=L_{v,n}-D_{v,n}/2\), and let \(\mathcal F_n\) be the tree-history filtration. For a mark already present at time \(n\), put \(T_n=2(n-1)\). The conditional transition table is:

| Attachment event | Conditional probability | \(\Delta D_{v,n}\) | \(\Delta L_{v,n}\) | \(\Delta A_{v,n}\) |
|---|---:|---:|---:|---:|
| Parent is \(v\) | \(D_{v,n}/T_n\) | \(1\) | \(1\) | \(1/2\) |
| Parent is a leaf neighbor of \(v\) | \(L_{v,n}/T_n\) | \(0\) | \(-1\) | \(-1\) |
| All other parents | \(1-(D_{v,n}+L_{v,n})/T_n\) | \(0\) | \(0\) | \(0\) |

The table applies already for the two-vertex initial edge. Its first two events are disjoint, because a vertex is not its own neighbor.

## Proof

**1. Exact drift and square moment.** Conditional on \(\mathcal F_n\), the transition table gives

\[
\mathbb E[\Delta A_{v,n}\mid\mathcal F_n]=-A_{v,n}/T_n,
\qquad
\mathbb E[(\Delta A_{v,n})^2\mid\mathcal F_n]
=(D_{v,n}/4+L_{v,n})/T_n.
\]

Thus

\[
\mathbb E[A_{v,n+1}\mid\mathcal F_n]
=\left(1-\frac{1}{2(n-1)}\right)A_{v,n},
\]

\[
\mathbb E[A_{v,n+1}^{2}\mid\mathcal F_n]
=\left(1-\frac{1}{n-1}\right)A_{v,n}^{2}
+\frac{D_{v,n}/4+L_{v,n}}{2(n-1)}.
\]

The degree first-moment recursion is \(\mathbb E[D_{v,n+1}\mid\mathcal F_n]=D_{v,n}(1+1/T_n)\). From finite initial degree, \(\mathbb E D_{v,n}=O(\sqrt n)\). Using \(0\le L_{v,n}\le D_{v,n}\) in the square-moment recurrence yields \(\mathbb E A_{v,n}^{2}=O(\sqrt n)\). One way to check this bound is to iterate the contraction coefficient \((n-2)/(n-1)\); the summed inhomogeneity is \(O(\sum_{j\le n}\sqrt j)/n=O(\sqrt n)\). In particular \(A_{v,n}/\sqrt n\to0\) in \(L^2\).

**2. Positive marked-degree limits.** Give each vertex of current degree \(d\) an independent exponential waiting clock of rate \(d\), resetting its clock whenever its degree changes. The next clock to ring selects exactly the prescribed preferential-attachment parent. In this continuous-time embedding the global count of edges \(K(t)\) is a Yule pure-birth process with transition rate \(2k\) from \(k\) to \(k+1\); after the fixed birth time \(\tau_v\), the marked degree \(D_v(t)\) is a Yule pure-birth process with transition rate \(d\) from \(d\) to \(d+1\). The standard exponential Yule martingales have strictly positive, finite almost-sure limits: \(e^{-2t}K(t)\to B>0\) and \(e^{-t}D_v(t)\to V_v>0\). The latter process starts with degree one at the mark's finite birth time; both properties hold simultaneously for finitely many marks. At the stopping time when the tree contains \(n\) vertices, \(K=n-1\), hence \(D_{v,n}/\sqrt n\to W_v:=V_v/\sqrt B>0\) almost surely. The degree moment recursion additionally gives the square-integrability bounds used below. Combining this with step 1 gives \(L_{v,n}/\sqrt n\to W_v/2\) in probability.

**3. Individual predictable quadratic variations.** Let \(s_v=2\) for initial vertices, and \(s_v=v\) otherwise. Set

\[
 b_{v,n}=\prod_{j=s_v}^{n-1}\left(1-\frac1{2(j-1)}\right),\qquad
 c_v=\frac{\Gamma(s_v-1)}{\Gamma(s_v-3/2)}>0.
\]

Then \(b_{v,n}\sim c_v n^{-1/2}\), and \(M_{v,n}=A_{v,n}/b_{v,n}\) is an integrable martingale. Its increment is \(\eta_{v,n+1}/b_{v,n+1}\), where \(\eta=\Delta A+A/T_n\) is a bounded martingale difference. The predictable bracket equals

\[
\langle M_v\rangle_n
=\sum_{j=s_v}^{n-1}b_{v,j+1}^{-2}
\left[\frac{D_{v,j}/4+L_{v,j}}{2(j-1)}
-\frac{A_{v,j}^{2}}{4(j-1)^2}\right].
\]

Write \(L_{v,j}=D_{v,j}/2+A_{v,j}\). Using the degree limit and the estimate \(\mathbb E A_{v,j}^2=O(\sqrt j)\), weighted Cesàro summation gives

\[
 n^{-3/2}\langle M_v\rangle_n\ \xrightarrow{\mathbb P}\ \frac{W_v}{4c_v^2}.
\]

Indeed the leading bracket summand is \(3W_v\sqrt j/(8c_v^2)\), whose sum is \(W_v n^{3/2}/(4c_v^2)+o_{\mathbb P}(n^{3/2})\). The linear-\(A\) remainder has expected absolute sum \(O(n^{5/4})\), and the negative quadratic correction has expected absolute sum \(O(\sqrt n)\); both are negligible after division by \(n^{3/2}\).

**4. The cross-brackets vanish.** For any two distinct fixed marks \(u,v\), their degrees eventually exceed one almost surely by step 2. Beyond that finite random time, no attachment can change both \(A_{u,n}\) and \(A_{v,n}\): direct attachment to one marked vertex cannot remove a leaf from the other, and a leaf has only one neighbor. Their simultaneous raw increment therefore vanishes. Consequently the post-threshold conditional covariance of the innovations is exactly \(-A_{u,n}A_{v,n}/T_n^2\). The finitely many earlier increments contribute negligibly. Cauchy–Schwarz and the square-moment estimates imply that the expected absolute sum of all subsequent normalized cross-bracket summands, after the \(n^{-3/2}\) normalization, is \(O(n^{-1})\). Hence all normalized off-diagonal brackets converge to zero in probability.

**5. Joint stable martingale central limit theorem.** For every fixed coordinate, \(|\eta_{v,j+1}|\le 2\), and \(b_{v,j+1}^{-1}=O(\sqrt j)\); thus the maximal jump of \(n^{-3/4}M_{v,n}\) is \(O(n^{-1/4})\). Conditional Lindeberg therefore holds deterministically. The multivariate martingale central limit theorem with an \(\mathcal F_\infty\)-measurable limiting bracket, applied to the vector \(n^{-3/4}(M_{v_i,n})\), gives stable mixed-normal convergence with diagonal conditional covariance \(\operatorname{diag}(W_{v_i}/[4c_{v_i}^2])\). Multiplication by \(n^{1/2}b_{v_i,n}\to c_{v_i}\) yields the \(n^{-1/4}A_{v_i,n}\) limit. Dividing by \(\sqrt{D_{v_i,n}/\sqrt n}\to\sqrt{W_{v_i}}>0\) gives independent \(\mathcal N(0,1/4)\) limits for the degree-studentized counts. This completes the proof.

## Verification

A standalone Python checker `verify.py` uses exact rational arithmetic to test the marked-vertex transition/drift/second-moment identities through size \(22\) and independently enumerates all attachment histories through size \(8\). It also exhaustively tests the key nonsimultaneous-increment lemma on all eight-vertex histories, at all nonleaf marked pairs and all possible attachments. A separate finite-distribution calculation checks that \(\mathbb E A_{1,n}^2/\mathbb E D_{1,n}\) approaches \(1/4\), with reported values at sizes \(50\), \(150\), and \(350\). These are diagnostics for finite identities, not substitutes for the Yule limit or the martingale central limit theorem. Execute `python3 verify.py` with Python's standard library.

## Relationship to prior work

Hartle and Krapivsky (2026), *Leaves of preferential attachment trees*, derive the empirical joint degree–leafdegree frequencies, the limiting typical-vertex leafdegree conditional mean and variance at large degree, and fluctuations of aggregate finite-degree class counts. Their large-degree variance \(one quarter of degree\) is consistent with the present normalization but does not imply a temporal fluctuation theorem for a fixed birth-labelled vertex, let alone joint stable independence across finitely many old hubs. A published result titled *A uniform half-degree law for leaves in preferential-attachment trees* bounds the maximum centered leafdegree simultaneously over vertices and implies an extremal ratio limit; the available statement does not identify the fixed-hub Gaussian fluctuation law at its \(n^{1/4}\) scale. These comparisons distinguish population counts, uniform concentration, and the age-marked conditional fluctuation law.

## Limitations

The theorem applies only to the classical one-edge, zero-offset preferential-attachment tree and a fixed finite family of deterministic birth labels. It does not assert conditional independence of the finite-size counts, Gaussianity for a typical uniformly sampled vertex, universality under altered attachment kernels, or a joint functional limit indexed by a growing family of hubs. The stable-limit statement is mathematical, not an independent numerical certification. Closely relevant published work is not all accessible in complete text, so historical priority cannot be established by search alone. No independent mathematical audit has been performed.

## References

- H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1, first public 2026-02-01, https://arxiv.org/html/2602.01021v1 (Sections II, III.5, IV; relevant full text inspected).
- *A uniform half-degree law for leaves in preferential-attachment trees*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-uniform-half-degree-law-for-leaves-in-preferential-attachment--309f47c597b3 (public summary examined; complete text inaccessible in this inspection).
- B. Bollobás, O. Riordan, J. Spencer and G. Tusnády, *The degree sequence of a scale-free random graph process*, Random Structures & Algorithms 18 (2001), 279–290; general classical preferential-attachment degree context.
