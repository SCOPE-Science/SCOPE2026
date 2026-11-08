# Logarithmic pendant matches in random greedy matching on clique coronas

## Finding

For each integer \(n\ge1\), let \(H_n\) be a complete graph on \(n\) core vertices with one distinct pendant vertex joined to each core vertex (the complete-graph corona). Inspect all edges in a uniformly random order, accepting an edge exactly when both its endpoints remain unmatched. Let \(X_n\) be the number of accepted pendant edges and \(M_n\) the total accepted edges. Put \(X_0=0\) for the generating-function convention. For \(|t|<1\) and \(z\ne0\), with continuous extension at \(z=0\), the exact probability generating function is

\[
\sum_{n\ge0}\mathbb E[z^{X_n}]t^n
=\frac{1}{2zt}\left[\left(\frac{1+t}{1-t}\right)^z-1\right].
\]

Every core vertex is matched, so \(M_n=(n+X_n)/2\). As \(n\to\infty\), uniformly for complex \(s\) in a sufficiently small fixed neighborhood of zero,

\[
\mathbb E[e^{sX_n}]
=\frac{2^{e^s-1}}{\Gamma(1+e^s)}
 n^{e^s-1}\bigl(1+O(n^{-1})\bigr).
\]

Consequently, writing \(\gamma\) for Euler's constant,

\[
\begin{aligned}
\mathbb E[X_n]&=\log n+\log2+\gamma-1+O(n^{-1}),\\
\operatorname{Var}(X_n)&=\log n+\log2+\gamma-\pi^2/6+O(n^{-1}),\\
\frac{X_n-\log n}{\sqrt{\log n}}&\xrightarrow{d}N(0,1).
\end{aligned}
\]

The maximum matching on \(H_n\) has size \(n\), whereas \(M_n/n\) converges in probability to \(1/2\), with \(\mathbb E[M_n]=n/2+(\log n+\log 2+\gamma-1)/2+O(n^{-1})\). An exact boundary probability is \(\Pr(X_n=0)=1/(n+1)\) for even \(n\), and zero for odd \(n\).

## Assumptions and scope

The graph is finite, simple and unweighted. Each original edge appears once; the edge ordering is uniformly distributed over all permutations. An inspected edge is accepted if and only if no earlier accepted edge shares an endpoint with it. All \(n\ge1\) are included in the exact formula, and the asymptotics concern integer \(n\to\infty\). No adaptive recoloring, repeated edge trials, vertex-priority selection or alternative matching algorithm is assumed. The displayed asymptotic expansion uses the analytic branch of the logarithm near positive real \(z=1\).

## Proof

**State reduction.** In the residual graph, if \(k\) core vertices are unmatched then their \(k\) private pendant edges remain and every pair of these cores remains joined. All other pendant vertices are isolated. There are \(k\) available pendant edges and \(\binom{k}{2}\) available core-core edges. The earliest such edge among those not yet excluded is uniform, by exchangeability of the original random ordering (equivalently by independent exponential edge priorities). Thus the next accepted edge is pendant with probability \(2/(k+1)\), removing one core; otherwise it removes two cores. Defining \(F_k(z)=\mathbb E[z^{X_k}]\), for \(k\ge2\),

\[
(k+1)F_k(z)=2zF_{k-1}(z)+(k-1)F_{k-2}(z),
\qquad F_0(z)=1,\quad F_1(z)=z.
\]

Every core is consumed by one of those edge choices. This gives \(M_n=(n+X_n)/2\), while the \(n\) pendant edges themselves form a perfect matching and hence give maximum matching size \(n\).

**Exact generating function.** Write \(H(t,z)=\sum_{k\ge0}F_k(z)t^k\) and \(J(t,z)=tH(t,z)\). Multiplying the recurrence by \(t^k\), summing and including the two initial terms gives

\[
(1-t^2)\frac{\partial J}{\partial t}-2zJ=1,
\qquad J(0,z)=0.
\]

Multiplication by \(((1-t)/(1+t))^z\) makes the left-hand side an exact derivative. Direct integration yields

\[
J(t,z)=\frac{((1+t)/(1-t))^z-1}{2z}.
\]

Division by \(t\) proves the claimed identity. In particular \(H(t,0)=\operatorname{artanh}(t)/t\); reading even and odd coefficients gives the stated exact zero-pendant probability.

**Asymptotics.** For \(z\) near \(1\), coefficient extraction from the preceding formula gives

\[
F_n(z)=\frac{1}{2z}[t^{n+1}](1+t)^z(1-t)^{-z}.
\]

Near \(t=1\), the analytic factor \((1+t)^z=2^z(1+O(1-t))\). The transfer estimate for \((1-t)^{-z}\) and the smaller contribution from the other singularity at \(t=-1\) give uniformly in a compact complex neighborhood of \(z=1\),

\[
F_n(z)=\frac{2^{z-1}}{\Gamma(z+1)}n^{z-1}(1+O(n^{-1})).
\]

Substitute \(z=e^s\). Uniform analyticity permits differentiation at \(s=0\), giving the mean and variance through the digamma identities \(\psi(2)=1-\gamma\) and \(\psi_1(2)=\pi^2/6-1\). Taking \(s=iu/\sqrt{\log n}\) and centering by \(\log n\) shows the characteristic functions tend to \(e^{-u^2/2}\) for every fixed real \(u\), proving the central limit theorem. Finally \(X_n/n\to0\) in probability by its mean asymptotic and nonnegativity, giving the matching-ratio limit.

## Verification

The accompanying `verify.py` independently computes the full labeled-vertex random-edge recursion for \(n=1,\ldots,7\), exhausts all edge permutations for \(n=1,2,3\), checks nineteen exact generating-function coefficients against the recurrence, and checks normalization/parity and large-index moment asymptotics. The checker passes when run with Python 3 and SymPy. These are finite consistency checks; the infinite-family distributional result follows from the proof above.

## Relationship to prior work

Random-edge greedy matching and its one-half worst-case approximation guarantee are classical. Bernstein (2020) studies stronger algorithms for random-order matching streams on arbitrary graphs, not the exact output law of the basic greedy algorithm on these coronas. Arnosti (2021) studies RANDOM-EDGE versus vertex-priority matching on random bipartite graphs; this fixed non-bipartite family and its edge-output generating function are outside its model and main theorems. A public result concerning general-position polynomials of complete-graph coronas addresses a distinct invariant; its full text was unavailable for inspection. The present claim is about the exact distribution and logarithmic fluctuation of *pendant edges selected* by random-order greedy matching, not the universal one-half bound alone.

## Limitations

This result covers only \(H_n\) with exactly one private leaf per clique vertex and uniform random edge order. The full distribution formula relies on that structural symmetry. It does not imply a comparable logarithmic correction for arbitrary coronas, general dense graphs, weighted edge priorities, or random-vertex-order matching. An unlocated earlier explicit treatment of this family remains a historical-priority possibility; no independent audit has been performed.

## References

1. A. Bernstein, *Improved Bounds for Matching in Random-Order Streams*, arXiv:2005.00417v1, first public 2020-05-01, https://arxiv.org/abs/2005.00417.
2. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, first published online 2021-11-02, DOI:10.1287/stsy.2021.0082, https://doi.org/10.1287/stsy.2021.0082.
