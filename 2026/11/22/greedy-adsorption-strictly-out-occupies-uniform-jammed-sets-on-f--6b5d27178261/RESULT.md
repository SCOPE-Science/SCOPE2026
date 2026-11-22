# Greedy adsorption strictly out-occupies uniform jammed sets on finite paths

## Finding

For every integer \(n\ge1\), let \(P_n\) be the path on the labeled vertices \(1,\ldots,n\). Two probability laws on its *inclusion-maximal independent sets* are natural:

- **Greedy (kinetic) law:** process vertices in a uniformly random permutation and select each vertex if neither neighbor was previously selected; call the output size \(G_n\).
- **Uniform (flat) law:** choose an inclusion-maximal independent set uniformly among all such sets, and call its size \(U_n\).

The expected cardinalities satisfy the sharp all-size classification
\[
\mathbb E G_n\ge\mathbb E U_n,
\qquad
\mathbb E G_n=\mathbb E U_n\iff n\in\{1,2,4\}.
\]
Furthermore, the expected kinetic excess is extensive:
\[
\mathbb E G_n-\mathbb E U_n=\delta n+O(1),\qquad
\delta=\frac{1-e^{-2}}2-\frac{1+\rho}{2+3\rho}
=0.0208367697190\ldots>0,
\]
where \(\rho\in(0,1)\) is the unique solution of \(\rho^2(1+\rho)=1\).

## Assumptions and scope

The graph is a finite, unweighted path; the greedy order is uniformly random with no ties. The uniform comparator is **not** a uniformly sampled arbitrary independent set, a maximum-cardinality independent set, or a random greedy output. An independent set is *maximal* when every unoccupied vertex has an occupied neighbor. All assertions concern every integer \(n\ge1\). No stochastic ordering of the complete size distributions is asserted.

Let \(f_{n,k}\) count maximal independent sets of size \(k\), \(F_n=\sum_k f_{n,k}\), \(A_n=\sum_k kf_{n,k}\), and \(u_n=A_n/F_n=\mathbb E U_n\). Set \(g_n=\mathbb E G_n\). For convenience set \(g_0=0\), and extend negative-index terms as zero where they occur.

## Proof

**1. Enumeration of the flat ensemble.** A maximal independent set containing \(k\) selected vertices has either zero or one unselected vertex before its first selected vertex and after its last; consecutive selected vertices have exactly one or two unselected vertices between them. Starting with \(k\) selections and \(k-1\) compulsory internal unselected vertices, the remaining \(n-2k+1\) unselected vertices may occupy any of the \(k+1\) optional slots. Hence, with the binomial coefficient understood as zero outside its natural range,
\[
f_{n,k}=\binom{k+1}{n-2k+1},\quad
\sum_{n\ge1}\sum_{k\ge1}f_{n,k}z^kx^n=
\frac{zx(1+x)^2}{1-zx^2(1+x)}.
\]
Differentiating with respect to \(z\) at \(z=1\) gives
\[
\sum_{n\ge1}F_nx^n=\frac{x(1+x)^2}{1-x^2-x^3},\quad
\sum_{n\ge1}A_nx^n=\frac{x(1+x)^2}{(1-x^2-x^3)^2}.
\]
Thus for \(n\ge5\),
\[
F_n=F_{n-2}+F_{n-3},\qquad
A_n=A_{n-2}+A_{n-3}+F_n.
\]
The initial triples are \((F_1,F_2,F_3,F_4)=(1,2,2,3)\) and \((A_1,A_2,A_3,A_4)=(1,2,3,6)\). These relations imply
\[
u_n=1+\frac{F_{n-2}}{F_n}u_{n-2}
+\frac{F_{n-3}}{F_n}u_{n-3}\quad(n\ge5).
\]

**2. Uniform upper bound for the flat mean.** For every \(j\ge3\),
\(F_j\le\tfrac32F_{j-1}\). It holds at \(j=3,4,5\). For \(j\ge6\), apply the recurrence and the two prior ratio bounds:
\[
F_j\le\tfrac52F_{j-3},\qquad
F_{j-1}=F_{j-3}+F_{j-4}\ge\tfrac53F_{j-3}.
\]
Therefore the weight \(w_3=F_{n-3}/F_n\) in the previous mean recurrence satisfies \(w_3\ge2/5\) for \(n\ge5\). Directly at \(n=2,3,4\), \(u_n\le(5n+6)/12\). Induction gives
\[
\begin{aligned}
u_n&\le1+\frac{5n+6}{12}
-\frac5{12}\left(2\frac{F_{n-2}}{F_n}+3\frac{F_{n-3}}{F_n}\right)\\
&=\frac{5n+6}{12}+\frac{2-5w_3}{12}
\le\frac{5n+6}{12},\qquad n\ge2.
\end{aligned}
\]

**3. Exact kinetic mean.** Conditional on the first inspected vertex, the two surviving sides are independent smaller random paths. Summing over its uniformly random position yields
\[
g_n=1+\frac2n\sum_{j=0}^{n-2}g_j,\qquad
\sum_{n\ge0}g_nx^n=\frac{1-e^{-2x}}{2(1-x)^2}.
\]
Consequently,
\[
g_n=\frac12\sum_{k=1}^n\frac{(-1)^{k+1}2^k}{k!}(n-k+1).
\]
Define \(L_n=(n+1-(n+3)e^{-2})/2\) by extending this finite alternating sum to infinity. The term at \(k=n+1\) vanishes; terms from \(k=n+2\) onward alternate with strictly decreasing magnitudes for \(n\ge2\). The standard alternating-series estimate thus gives
\[
\left|g_n-L_n\right|\le\frac{2^{n+1}}{(n+2)!}\qquad(n\ge2).
\]

**4. Strict all-size comparison.** The positive exponential series proves the rational inequality
\(e^2>\sum_{k=0}^{8}2^k/k!=2327/315\). Therefore, for every \(n\ge13\),
\[
L_n-\frac{5n+6}{12}
=\frac{n-(6n+18)e^{-2}}{12}
>\frac{437n-5670}{27924}\ge\frac{11}{27924}
>\frac{2^{14}}{15!}
\ge\frac{2^{n+1}}{(n+2)!}.
\]
Together with Steps 2–3 this yields \(g_n>u_n\) for every \(n\ge13\). For \(n=1,\ldots,12\), exact rational evaluation using the displayed recurrences gives the differences
\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\\hline
g_n-u_n&0&0&1/6&0&13/60&4/45
\end{array}
\]
and
\[
\begin{array}{c|rrrrrr}
n&7&8&9&10&11&12\\\hline
g_n-u_n&19/105&1/5&533/2835&3091/12600&7582/31185&3289/12150.
\end{array}
\]
This completes the finite classification without relying on numerical extrapolation.

**5. Extensive excess.** Let \(\rho\in(0,1)\) solve \(\rho^2(1+\rho)=1\). The positive, aperiodic rational generating function for \(F_n\) has a unique dominant simple pole at \(x=\rho\). Differentiation with respect to the size-marking parameter \(z\) gives
\[
u_n=\frac{1+\rho}{2+3\rho}n+O(1).
\]
The kinetic generating function instead gives \(g_n=(1-e^{-2})n/2+O(1)\). Their difference yields the stated \(\delta>0\), with positivity also independently guaranteed by the strict lower bound above.

## Verification

The accompanying standalone `check.py` uses exact integer and rational arithmetic. It checks the counting and mean recurrences through \(n=120\), directly enumerates every maximal independent set and every vertex order for \(n\le8\), tests the full sign/equality pattern through \(n=120\), and checks the rational constants used in the infinite-size proof. All checks completed successfully. The finite computations supplement; they do not replace the general proof in Steps 1–5.

## Relationship to prior work

Brightwell–Janson–Luczak (2015) analyze the greedy process on random graphs with prescribed degrees and summarize Flory's classic one-dimensional greedy density; their model does not uniformly sample all maximal independent sets of a fixed path. Krivelevich–Mészáros–Michaeli–Shikhelman (2019 preprint; 2024 journal) analyze the random greedy law, derive its path asymptotic, and compare tree *shapes*, not the greedy and flat ensembles on the same path. Classical enumeration supplies the flat path recurrence. The present conclusion is the **sharp all-finite-size comparison between two measures on precisely the same maximal configurations**, including its exceptional equality set; neither the separate densities nor a known tree-shape extremum implies that comparison.

## Limitations

The result is restricted to finite paths and expected output size. It does not establish tailwise stochastic domination, total variation, variance order, an extension to cycles, or any general graph ordering. The proof gives a quantitative all-size sign law but does not claim a wholly new formula for either individual sampling model. Literature comparisons are subject to the possibility of an overlooked equivalent result in older statistical-physics treatments of flat jammed-state ensembles. An independent mathematical audit has not been performed.

## References

1. G. Brightwell, S. Janson, M. Luczak, *The greedy independent set in a random graph with given degrees* (first public arXiv version 19 October 2015), https://arxiv.org/abs/1510.05560.
2. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits* (preprint 2019; journal publication 2024), https://arxiv.org/abs/1907.07216 and https://doi.org/10.1002/rsa.21200.
