# Orthogonal-pair stars give degree \(2d-1\) in high-dimensional Gilbert–Steiner geometry

## Finding
Fix a mass-cost exponent \(p\) with \(1/2<p<1\), and put \(\theta=2p-1\). Define
\[
H(\theta)=\max\left\{\frac{1}{2^{-\theta}-1/2},\,\frac{4}{1-\theta}\right\}.
\]
For every integer \(d\ge3\) satisfying \(k^\theta\ge H(\theta)\), where \(k=2(d-1)\), there is an explicitly specified globally minimum-cost Gilbert–Steiner flow in Euclidean \(\mathbb R^d\) with a nonterminal branching point of degree exactly \(2d-1\). The cost of an edge of Euclidean length \(L\) carrying absolute mass \(m\) is \(Lm^p\). Consequently, if \(B_p(d)\) is the supremum of possible branching degrees in finite optimal Gilbert–Steiner flows in \(\mathbb R^d\), then
\[
B_p(d)\ge 2d-1\quad\text{for all sufficiently large }d\text{ at each fixed }p\in(1/2,1).
\]
This improves the previously published general construction of degree \(d+1\) in the stated asymptotic range. No matching upper bound or assertion of optimality of the coefficient two is made.

## Assumptions and scope
Work with the standard finite single-source, multiple-sink Gilbert–Steiner problem with arbitrary Euclidean Steiner vertices and \(0<p<1\). Each of \(k\) distinct sinks requires one unit of mass and the single source supplies \(k\) units. The minimization ranges over finite admissible flows, not just stars. For the explicit construction set \(m=d-1\), \(k=2m\), and choose orthonormal vectors \(e_0,e_1,\ldots,e_m\). Set
\[
a=k^{p-1},\qquad b=\sqrt{1-a^2},\qquad x_{i,\pm}=a e_0\pm b e_i\quad(1\le i\le m).
\]
Take source at \(-e_0\), sinks at the \(2m\) distinct points \(x_{i,\pm}\), and a branching vertex at the origin. Send mass \(k\) from source to origin and mass one from origin to each sink. All \(2m+1=2d-1\) edges have length one and the vertex at the origin is not a terminal.

The explicit sufficient dimension threshold is intentionally conservative and need not be the smallest dimension for which these directions form an optimal star. The endpoint \(p=1/2\) is excluded, as is \(p=1\).

## Proof
**Step 1: exact subset energy.** The direction vectors are unit and satisfy
\[
\sum_{i=1}^m(x_{i,+}+x_{i,-})=ka e_0=k^p e_0.
\]
Thus equilibrium holds with the source direction \(-e_0\). For a subset \(I\) of \(j\) outgoing edges, let \(s(I)\) be the number of coordinate pairs from which precisely one sign is selected. Orthogonality yields the exact identity
\[
\left\|\sum_{v\in I}v\right\|^2=j^2 k^{\theta-1}+s(I)(1-k^{\theta-1}),
\qquad 0\le s(I)\le \min\{j,k-j\}.
\]
Therefore it is sufficient to prove, for every integer \(0\le j\le k\),
\[
j^2 k^{\theta-1}+\min\{j,k-j\}(1-k^{\theta-1})\le j^{1+\theta}=j^{2p}.
\tag{1}
\]
For \(j=0,1,k\) this follows directly.

**Step 2: at most half the sinks.** If \(2\le j\le k/2\), inequality (1) is equivalent to
\[
k^{\theta-1}\le \frac{j^\theta-1}{j-1}.
\]
Since \(0<\theta<1\), the secant slope on the right is decreasing with \(j\); it suffices to check \(j=k/2\). The explicit threshold \(k^\theta(2^{-\theta}-1/2)\ge1\) implies
\[
(k/2)^\theta-1\ge k^\theta/2\ge (k/2-1)k^{\theta-1},
\]
which completes this range.

**Step 3: at least half the sinks.** Put \(t=j/k\in[1/2,1]\). Convexity of \(t\mapsto t^{-(1-\theta)}\) gives
\[
t^{\theta-1}-1\ge (1-\theta)(1-t).
\]
Since \(t^2\ge1/4\),
\[
\begin{aligned}
j^{1+\theta}-j^2k^{\theta-1}
&=k^{1+\theta}t^2(t^{\theta-1}-1)\\
&\ge \frac{(1-\theta)k^\theta}{4}(k-j)\\
&\ge k-j
\end{aligned}
\]
by the other threshold \(k^\theta\ge4/(1-\theta)\). As \(\min\{j,k-j\}=k-j\) here and \(1-k^{\theta-1}\le1\), this proves (1) for all \(j\).

**Step 4: global, not merely local, optimality.** A finite optimal flow for a strictly concave mass cost can be chosen without cycles; for one source it is an oriented tree, with each edge carrying the integer number \(j_e\) of downstream unit sinks. For such an edge write \(S_e\) for those sinks and \(z_e\) for its directed displacement. The verified subset inequalities give
\[
j_e^p\|z_e\|\ge\left\langle\sum_{i\in S_e}x_i,z_e\right\rangle.
\]
Summing over every edge, paths telescope, yielding the universal lower bound
\[
\sum_e j_e^p\|z_e\|\ge
\sum_{i,\pm}\langle x_{i,\pm},x_{i,\pm}+e_0\rangle
=k+k^p.
\]
The stated star has cost exactly \(k+k^p\), hence attains the global minimum. Equivalently, this is the sufficient half of the exact star-optimality criterion in Volz–Brazil–Ras–Swanepoel–Thomas, explicitly reproduced in the 2026 motivating source. The origin has \(2d-1\) distinct incident edges; the claimed lower bound follows. \(\square\)

## Verification
Run the standalone file \(\texttt{verify.py}\) with Python 3. It checks the sufficient thresholds and all possible subset cardinalities for eight exponent values, plus exhaustive literal sign-subsets for several small admissible examples. The actual run returned **PASS: 10772 finite assertions/checks**. The numerical checks are supplementary: Steps 1–4 above establish every quantified dimension and exponent in the claimed range. The code does not verify an unbounded-dimensional statement and is not an independent audit.

## Relationship to prior work
Teplitskaya's 2026 collection explicitly poses lower and upper degree bounds for large dimension and fixed \(p>1/2\), and reproduces the global star-optimality criterion. Cherkashin (2025) constructs a solution with degree \(d+1\) when \(p\ge1/2\); this is a distinct lower-bound construction, not a proof of the present \(2d-1\) bound. Volz and coauthors (arXiv 2009; journal 2013) provide the underlying general characterization for optimal Gilbert arborescences. Their characterization is used, but the paired orthogonal directions and explicit all-subset bound are the asserted new contribution. Searches of aliases such as orthogonal pairs, cross-polytope directions, branching degree \(2d-1\), and Euclidean concave-cost arborescences did not find an equivalent stronger published conclusion. These negative searches are not a guarantee of global novelty.

## Limitations
This gives an existential lower bound, not an upper bound or a determination of \(B_p(d)\). The sufficient dimension threshold may be very large near \(p=1/2\) or \(p=1\). The proof covers finite single-source flows and then the general maximum by inclusion of that special case; it does not classify all optimal branches or prove unique minimizers. Priority against unindexed or non-open-access literature remains provisional. No independent mathematical audit has been performed.

## References
1. Y. Teplitskaya, *Open problems from the Length Optimization event at MDS 2026*, arXiv:2611.03403v1, first public 2026-11-02, https://arxiv.org/abs/2611.03403 ; especially Question 1.2 and Theorem 1.3.
2. D. Cherkashin, *On branching points in the Gilbert–Steiner problem*, arXiv:2507.13532v1, 2025-07-17, https://arxiv.org/abs/2507.13532 ; especially Theorem 2 and Section 4.
3. M. G. Volz, M. Brazil, C. J. Ras, K. J. Swanepoel, D. A. Thomas, *The Gilbert Arborescence Problem*, arXiv:0909.4270, https://arxiv.org/abs/0909.4270 ; especially Euclidean Corollary 3, published in *Networks* 61 (2013), 238–247.
