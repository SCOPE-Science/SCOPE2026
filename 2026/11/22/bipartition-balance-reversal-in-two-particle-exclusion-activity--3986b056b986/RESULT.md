# Bipartition-balance reversal in two-particle exclusion activity on complete bipartite graphs

## Finding

**Theorem.** For integers \(r,s\ge1\) with \(n=r+s\ge4\), run symmetric simple exclusion with exactly two indistinguishable particles on the complete bipartite graph \(K_{r,s}\). Every occupied-to-vacant adjacent-site hop occurs at rate one. Start from the uniform stationary distribution over the \(\binom n2\) unordered occupied pairs. Let \(C_T\) count **all successful hops** during \([0,T]\); rejected attempts are not counted. Its exact mean rate \(\mu\) and long-time activity Fano ratio \(F\) are
\[
\boxed{\displaystyle \mu=\lim_{T\to\infty}\frac{\mathbb EC_T}{T}=\frac{4rs(n-2)}{n(n-1)},\qquad
F=\lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{\mathbb EC_T}
=1+\frac{n^2+(r-s)^2(n^2-6n+4)}{n^2(n-1)^2}.}
\]

Fixing the total site count \(n\), the dependence of \(F\) on the shore imbalance **reverses between sizes five and six**:

- For \(n=4\) or \(n=5\), the most balanced shores uniquely maximize \(F\) and the star \(K_{1,n-1}\) uniquely minimizes it (up to interchanging shores).
- For every \(n\ge6\), the most balanced shores uniquely minimize \(F\), and the star \(K_{1,n-1}\) uniquely maximizes it (again up to shore exchange).

The sole Poisson activity case in this family with two particles and \(n\ge4\) is \(K_{1,3}\), for which \(F=1\). All other cases have \(F>1\). At fixed positive macroscopic shore fraction \(r/n\to\alpha\in(0,1)\), the Fano ratio has the limit
\[
\boxed{\displaystyle F\longrightarrow1+(2\alpha-1)^2.}
\]
Thus balanced dense bicliques become asymptotically Poissonian in Fano ratio while dense bicliques with fixed nonzero relative imbalance retain a strictly positive excess. This statement is about the first two long-time cumulants, not a full Poisson-process convergence theorem.

## Assumptions and scope

The underlying graph has \(r\) vertices in one independent shore and \(s\) in the other, with all \(rs\) cross-shore edges present. Each undirected edge having one occupied and one empty endpoint has a rate-one exchange clock, so no extra normalization by vertex degree is used. The process is finite, irreducible and reversible. Uniform occupancy pairs are stationary. Define the total accepted-hop rate from configuration \(S\) by \(\lambda(S)=|\partial S|\). This quantity includes *all* successful jumps, not only those changing the coarse occupancy class. No external reservoirs, density creation, bias, or disorder are present.

## Proof

**1. Stationary classes and intensities.** Group states by the number of occupied vertices in the first shore. Label the classes \(AA,AB,BB\). When a class is physically absent because a shore has size one, it may be omitted; the formulas below remain valid with that class's stationary mass zero. In class order \(AA,AB,BB\), the Markov generator on class-constant test functions, the total successful-hop intensity, and the stationary class probabilities are
\[
Q=\begin{pmatrix}
-2s&2s&0\\
r-1&-(n-2)&s-1\\
0&2r&-2r
\end{pmatrix},\qquad
\lambda=\begin{pmatrix}2s\\n-2\\2r\end{pmatrix},\qquad
\pi=\frac1{n(n-1)}\begin{pmatrix}r(r-1)\\2rs\\s(s-1)\end{pmatrix}.
\]
The rates count each admissible particle hop independently. Detailed balance holds between successive occupancy classes. The stationary mean rate is
\[
\mu=\pi^\mathsf T\lambda=\frac{4rs(n-2)}{n(n-1)}.
\]
Although some microscopic jumps can produce the same class, none are lost in \(\lambda\): for this particular biclique two-particle model every successful hop switches the class by one step.

**2. Exact stationary count-variance identity.** For the full microscopic configuration chain, let \(L\) be its generator and \(B\) its off-diagonal jump-rate matrix. The tilted generator of \(C_T\) is \(L_z=e^z B-\operatorname{diag}(\lambda)\). By irreducibility the maximal eigenvalue is simple and analytic near zero. Differentiating the normalized right-eigenvector equation at zero yields
\[
\Lambda'(0)=\mu,\qquad -Lh=\lambda-\mu,\qquad \langle h\rangle_\pi=0,
\]
and differentiation again gives
\[
\Lambda''(0)=\mu+2\langle\lambda-\mu,h\rangle_\pi.
\]
These are the long-time first and second cumulant rates. The identity follows also from reversibility and the Poisson equation; it is not a claim that the count is a conditionally independent Poisson process.

The forcing \(\lambda-\mu\) is invariant under independent permutations of each shore. Averaging any mean-zero Poisson-equation solution under those permutations gives a class-constant solution, so the three-state reduction is exact for the needed covariance. For \(r,s\ge2\), write the three values of \(h\) as \(h_{AA},h_{AB},h_{BB}\). The first and third rows of \(-Qh=\lambda-\mu\) give
\[
h_{AA}-h_{AB}=\frac{2s-\mu}{2s},\qquad
h_{BB}-h_{AB}=\frac{2r-\mu}{2r}.
\]
The middle row is then consistent by stationarity and detailed balance. For a shore of size one only its accessible difference is needed. Because \(\sum_i\pi_i(\lambda_i-\mu)=0\), subtracting the reference constant \(h_{AB}\) gives the exact covariance
\[
\langle\lambda-\mu,h\rangle_\pi
=\frac{r(r-1)}{n(n-1)}\frac{(2s-\mu)^2}{2s}
+\frac{s(s-1)}{n(n-1)}\frac{(2r-\mu)^2}{2r}.
\]
Consequently \(F=1+2\langle\lambda-\mu,h\rangle_\pi/\mu\). Substituting the displayed mean, collecting over the common denominator and using \(n=r+s\) proves
\[
F-1=\frac{n^2+(r-s)^2(n^2-6n+4)}{n^2(n-1)^2}.
\]
This is a symbolic identity for all positive integers in the stated range; the exact-rational checkers verify it on independent finite cases.

**3. Strict extremizers and the reversal.** For fixed integer \(n\), the denominator is independent of the shore partition, and \((r-s)^2\) strictly decreases as the shores become more balanced. Its coefficient \(n^2-6n+4\) is negative when \(n=4,5\), and positive for every integer \(n\ge6\). Therefore the orientation of the strict order flips precisely between five and six vertices. The minimum feasible imbalance is zero for even \(n\) and one for odd \(n\), while the maximum is \(n-2\); this proves all claimed optimizer equality cases. Explicitly, at the balanced optimum
\[
F=\begin{cases}
1+(n-1)^{-2},&n\text{ even},\\
1+2(n-2)/[n^2(n-1)],&n\text{ odd},
\end{cases}
\]
and at the star
\[
F=\frac{2((n-2)^2+4)}{n^2}.
\]
The explicit formula gives \(F=1\) only at \(n=4\), \(\lvert r-s\rvert=2\), that is, the four-site star. For fixed \(r/n\to\alpha\), the numerator divided by the denominator tends to \((2\alpha-1)^2\), proving the asymptotic statement.

## Verification

Run `python verify_bipartite_activity.py` with Python 3's standard library. It constructs the **original microscopic** \(\binom n2\)-state generator from occupied pairs rather than imposing the three-class reduction, solves the mean-zero Poisson equation using exact rational arithmetic, and checks the analytic mean and Fano formulas for all 18 unordered shore partitions with \(4\le n\le9\). It also verifies the optimizer ordering for each \(4\le n\le89\). Run `python verify_bipartite_symbolic.py` with SymPy for a second, independently coded symbolic three-class Poisson-equation derivation of the rational expression. Both programs completed successfully before packaging.

Selected exact values provide direct cross-checks:
\[
\begin{array}{c|ccc}
 n&\text{star}&\text{intermediate}&\text{balanced}\\\hline
 4&1&\text{--}&10/9\\
 5&26/25&\text{--}&53/50\\
 6&10/9&238/225&26/25
\end{array}
\]
The finite verification range is not an infinite proof; the analytic calculation in the previous section is the general proof.

## Relationship to prior work

Appert-Rolland, Derrida, Lecomte and van Wijland introduced and evaluated the integrated activity count for the symmetric exclusion process on a periodic one-dimensional ring [1]. Their tilted-generator technique is used here without claiming its invention. Lecomte, Garrahan and van Wijland examined the inactive dynamical phase of ring SSEP [2], which does not determine bipartition-dependent activity statistics. Mendonça explicitly diagonalized the ordinary SSEP generator on arbitrary complete bipartite graphs [3], including the stationary distribution and gap, but not its count-tilted generator or the present Fano-optimizer reversal.

A published finite-network activity theorem [4] already gives the general reversible-chain Green identity, strict super-Poisson inequality, and precise graph classification of the Poisson equality case; those statements are explicitly treated as prior knowledge. An exact Hamming-graph activity calculation [5] covers \(K_{2,2}\) as one case. Neither examined result states the two-parameter \(K_{r,s}\) count-variance law or the sharp reversal at total size six. The present quantitative formula **specializes an established general counting framework**, not a new universal fluctuation identity. Searches cannot conclusively exclude an independently published equivalent specialization.

## Limitations

The result concerns the stationary long-time accepted-hop count of **exactly two** hard-core particles, unit rates **per admissible edge**, and complete bipartite graphs. It does not establish full finite-time count distributions, higher cumulants, graph-uniform results for more particles, or Poisson convergence from a Fano-ratio limit. The general spectral perturbation framework and the universal nonnegative Fano correction are pre-existing. Historical priority for the evaluated biclique formula and size-six crossover remains open to a broader literature examination and independent validation.

## References

1. C. Appert-Rolland, B. Derrida, V. Lecomte, F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590, first posted 2008-04-16; https://arxiv.org/abs/0804.2590 (particularly Sections I–II).
2. V. Lecomte, J. P. Garrahan, F. van Wijland, *Inactive dynamical phase of a symmetric exclusion process on a ring*, arXiv:1203.1600, first posted 2012-03-07; https://arxiv.org/abs/1203.1600 (Introduction and Section 2).
3. J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106, first posted 2012-07-17; https://arxiv.org/abs/1207.4106 (Sections 2 and 4–5).
4. *Poisson activity on finite exclusion networks: a complete graph classification*, published research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-poisson-activity-on-finite-exclusion-networks-a-complete-graph-c--016805168b38 (Finding, Proof, and Limitations).
5. *Exact jump-activity noise for two-particle exclusion on Hamming graphs*, published research record, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-jump-activity-noise-for-two-particle-exclusion-on-hamming--9e35afb2f386 (Finding and Proof).
