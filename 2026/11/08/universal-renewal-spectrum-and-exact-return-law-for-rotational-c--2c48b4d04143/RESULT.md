# Universal renewal spectrum and exact return law for rotational connect-the-dots maps

## Finding

For every integer \(n\ge3\) and every integer \(t\in\{1,\ldots,n-1\}\) coprime to \(n\), interpolate linearly between the nodes
\[
f_{n,t}(j)=(j+t)\bmod n,\qquad j=0,1,\ldots,n-1,
\]
so that \(f_{n,t}:[0,n-1]\to[0,n-1]\) is continuous. Put \(m=n-1\). The exact Artin--Mazur zeta function, valid as a formal power series, is
\[
\zeta_{f_{n,t}}(z)=\exp\left(\sum_{k\ge1}\frac{\#\operatorname{Fix}(f_{n,t}^{k})}{k}z^k\right)
=\frac{1}{1-z-z^2-\cdots-z^{m}}.
\]
In particular, every least period \(k\ge1\) occurs, and the number of primitive \(k\)-cycles is
\[
P_{n,k}=\frac1k\sum_{d\mid k}\mu(d)\,a_{m,k/d},\qquad
a_{m,r}=\operatorname{tr}(A_m^r),
\]
where \(A_m\) is the explicitly described renewal matrix whose first-return loops have lengths \(1,2,\ldots,m\). Equivalently, for all \(r\ge1\),
\[
a_{m,r}=\sum_{j=1}^{\min(m,r)}a_{m,r-j}
\quad\text{if }r>m,
\]
with initial values \(a_{m,r}=2^r-1\) for \(1\le r\le m\) (the recurrence and initial values suffice for all \(r\)).
The topological entropy is \(\log\rho_m\), where \(1<\rho_m<2\) uniquely solves
\[
\sum_{r=1}^{m}\rho_m^{-r}=1.
\]
There is a unique measure of maximal entropy. Conditional on the unique full-covering basic interval, successive first-return durations under this measure are independent, with
\[
\Pr(R=r)=\rho_m^{-r},\qquad r=1,\ldots,m.
\]
Every quantity above is independent of the coprime step \(t\).

## Assumptions and scope

All assertions concern the explicitly defined continuous piecewise-linear maps on the full compact interval \([0,n-1]\), for integers \(n\ge3\) and \(\gcd(n,t)=1\). Write \(I_j=[j,j+1]\) for \(0\le j\le m-1\). The fold index is \(c=n-t-1\). The map is of slope \(-(n-1)\) on \(I_c\) and of slope \(+1\) on every other basic interval. The term 'return' refers to visits of the Markov itinerary to \(I_c\), with endpoints irrelevant for the non-atomic maximal-entropy measure. Every periodic point is counted as a point, not as an orbit, in the zeta function; \(P_{n,k}\) counts distinct orbits.

## Proof

**The renewal graph.** Let \(A\) be the \(m\)-by-\(m\) covering matrix, with \(A_{ij}=1\) when \(f(I_j)\supseteq I_i\). The interval \(I_c\) maps onto all of \([0,n-1]\) (its endpoint images are \(n-1\) and \(0\)), so its entire column is one. For every \(j\ne c\), the branch is an isometry onto the single interval \(I_{(j+t)\bmod n}\), whose index is always less than \(m\). The permutation \(j\mapsto(j+t)\bmod n\) forms one \(n\)-cycle. Deleting its vertex \(n-1\) and the incoming/outgoing arrows leaves one directed chain of length \(m-1\), whose final vertex is \(c\). Reinstating the full column from \(c\) produces a renewal graph with exactly one first-return loop of each length \(1,\ldots,m\). This graph is mixing (there is a length-one loop) and its combinatorics do not depend on \(t\).

**Characteristic determinant and periodic counts.** For any directed graph formed by a deterministic path ending in a vertex that links to every vertex of the path, expansion of the determinant, or the first-return loop identity, gives
\[
\det(I-zA)=1-\sum_{r=1}^{m}z^r.
\]
For a finite matrix \(A\), the formal identity
\[
\exp\left(\sum_{k\ge1}\frac{\operatorname{tr}(A^k)}kz^k\right)
=\det(I-zA)^{-1}
\]
follows from the matrix logarithm. It remains to show that the number of physical fixed points equals \(\operatorname{tr}(A^k)\), despite shared endpoints. For any closed admissible word of length \(k\), its itinerary visits \(c\): the graph with the outgoing arrows from \(c\) removed is acyclic. The composition of inverse branches along the word maps the initial closed basic interval into itself and is a strict contraction, with Lipschitz factor at most \(1/m\), because all other slopes have modulus one. It has a unique fixed point with that itinerary.

Different words could encode the same fixed point only at a partition boundary. But every boundary is an integer, and these integers form one primitive \(n\)-cycle under \(f\). Its symbolic itinerary is unique: the positions at \(0\) and \(n-1\) have only one containing basic interval, and, proceeding forward from \(0\), an ordinary branch has only one successor interval, while a folding branch sends its boundary endpoint to \(0\) or \(n-1\), again with a unique successor. This determines the entire periodic boundary itinerary. Therefore closed admissible words and physical periodic points are bijective, proving the displayed zeta formula. Expanding the logarithmic derivative gives \(a_{m,r}=2^r-1\) for \(r\le m\) and \(a_{m,r}=\sum_{j=1}^{m}a_{m,r-j}\) for \(r>m\); Möbius inversion gives \(P_{n,k}\).

**All primitive periods.** For \(1\le k\le m\), the one excursion of length \(k\) provides a primitive orbit because it has exactly one visit to \(c\). For \(k>m\), consider a closed word with exactly one return excursion of length two and \(k-2\) excursions of length one. It has total length \(k\) and its ordered excursion list is not a proper repetition, so it is primitive. This covers all \(k\ge1\).

**Entropy and stationary return law.** The renewal graph has a primitive nonnegative adjacency matrix. Its Perron root \(\rho_m\) satisfies \(\sum_{r=1}^{m}\rho_m^{-r}=1\). The stationary one-sided Markov shift maps onto the interval dynamics via inverse-branch coding. All infinite graph paths encounter the folding vertex at gaps of at most \(m\), so inverse cylinders shrink uniformly. The only noninjectivity can occur in the countable backward orbit of the partition endpoints, whose forward orbits lie in the finite boundary cycle. On its complement, the coding is one-to-one. The entropy is consequently the Markov entropy \(\log\rho_m\); since the primitive Markov shift has one Parry maximal-entropy measure, this yields a unique maximal-entropy probability for the interval map (a measure supported on the finite endpoint cycle has zero entropy). In the Parry measure, the probability of a given return loop of length \(r\), conditional on a visit to \(c\), is \(\rho_m^{-r}\), as the Perron eigenvector factors telescope. These probabilities sum to one by the Perron equation. The strong Markov property at the recurrent vertex makes successive excursion lengths independent. Transfer through coding proves the physical return law.

## Verification

Run \(\texttt{python3 check.py}\) with Python 3; no third-party dependencies. It checks all coprime shifts for \(3\le n\le16\), exact covering matrices, every integer coefficient of the characteristic polynomial through Newton identities, and periodic trace recurrences. For \(3\le n\le8\) and \(1\le k\le9\), it independently reconstructs each admissible word's physical fixed point using rational arithmetic and compares the number of distinct points with matrix traces. The checker reports 35,766 exact assertions. This finite testing does not establish the all-parameter theorem, which follows from the proof above.

## Relationship to prior work

Yihan Wang, *On Periodic Points in Covering Systems* (arXiv:2306.10523v1, June 18, 2023), Example 3.6(1), explicitly recognizes the coprime cyclic-step permutations and their characteristic sequences \(1,\ldots,n-1\). Wang's Theorem 4.6 obtains an adjacency-matrix characteristic polynomial **over the two-element field** for general cyclic permutations, not the integral renewal determinant, physical fixed-point counts, exact dynamical zeta function, or maximal-entropy return distribution for this continuous family. Geller and Misiurewicz (2018) study twist permutations and Markov loop graphs in Lorenz-like maps, but their main objects have a discontinuity or different canonical models. Alsedà, Juher, King, and Mañosas (2013) provide the general connect-the-dots/Markov-entropy framework, not the stated step-independent complete spectrum. Standard Markov and Parry theory underlies the entropy-and-return deduction and is not claimed as new.

## Limitations

This theorem concerns the coprime rotational interpolation family only; no claim is made for non-coprime steps, more general cyclic permutations, or arbitrary interpolation between the nodes. The mathematical statement is internally proved, while novelty relative to unidentified or unindexed sources cannot be certified. No independent mathematical audit has been performed.

## References

1. Y. Wang, *On Periodic Points in Covering Systems*, arXiv:2306.10523v1 (June 18, 2023), https://arxiv.org/html/2306.10523v1.
2. W. Geller and M. Misiurewicz, *Farey--Lorenz Permutations for Interval Maps*, International Journal of Bifurcation and Chaos **28** (2018), 1850021, DOI: 10.1142/S0218127418500219. Open author manuscript: https://scholarworks.indianapolis.iu.edu/server/api/core/bitstreams/7244046f-8126-41ac-8517-c6ff5d53918e/content.
3. L. Alsedà, D. Juher, P. King, and F. Mañosas, *Maximizing entropy of cycles on trees*, Discrete and Continuous Dynamical Systems **33** (2013), 3237--3263, DOI: 10.3934/dcds.2013.33.3237.
