# First nontrivial Walsh cancellation of the triangle-free graph property: a complete five-vertex spectrum

## Finding

Let \(E_n=E(K_n)\), and let \(\mathcal F_n\subseteq\mathbb F_2^{E_n}\) be the incidence vectors of **all** simple labelled triangle-free graphs on \([n]\). For the unnormalized Walsh coefficient
\[
W_n(S)=\sum_{G\in\mathcal F_n}(-1)^{|S\cap E(G)|},\qquad S\subseteq E_n,
\]
the first nontrivial loss of invertibility for \(n\ge3\) occurs at \(n=5\). At \(n=3,4,6\) every coefficient is nonzero; the respective numbers of admissible graphs are \(7,41,5789\). At \(n=5\), \(|\mathcal F_5|=388\), and exactly \(150\) of the \(1024\) coefficients vanish, partitioned into **three \(S_5\)-orbits** of sizes \(60,60,30\). Their representatives are ten-edge bitmasks \(63,221,255\) under the ordered edge list specified below. The first two orbits have support six; the third has support eight. No support of size at most five vanishes.

Consequently the counting-convolution operator \(T_5:g\mapsto 1_{\mathcal F_5}*g\) on \(\ell^2(\mathbb F_2^{E_5})\) has rank \(874\), nullity \(150\), sharp pseudoinverse norm \(\|T_5^\dagger\|_{2\to2}=1/2\), and positive-spectrum condition number \(194\). If \(P_5\) is its orthogonal range projection, then
\[
\|P_5\|_{\ell^1\to\ell^1}=\|P_5\|_{\ell^\infty\to\ell^\infty}=\frac{1981}{256}.
\]
The complete signed Walsh spectrum, including **all 34 relabelling orbits**, is recorded in `orbit_table.tsv`. Its distinct signed multiplier values with multiplicities, in increasing order, are
\[
\begin{aligned}
&(-26,20),(-22,60),(-20,5),(-12,60),(-10,20),(-8,90),(-6,60),\\
&(-4,20),(-2,40),(0,150),(2,160),(4,91),(6,72),(8,70),\\
&(10,30),(14,30),(16,10),(44,15),(46,10),(106,10),(388,1).
\end{aligned}
\]

## Assumptions and scope

All graphs are simple and labelled, and `triangle-free` means containing no three-vertex clique (not necessarily maximal or bipartite). Arithmetic is over the integers. Edge order at \(n=5\): \((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)\). Bit \(j\) of a decimal mask corresponds to the \(j\)-th listed edge; the permutation group \(S_5\) acts by relabelling endpoints. Convolution is unnormalized. Hilbert norms use counting measure; this does not affect \(2\to2\) multiplier norms. The projection \(P_5\) is the **orthogonal Fourier range projection**, not an arbitrary projection onto the range.

## Proof

Let \(\mathcal T=\binom{[5]}3\) be the ten triangles. Write \(E(t)\subseteq E_5\) for the three edges of triangle \(t\); and for \(A\subseteq\mathcal T\), set \(U_A=\bigcup_{t\in A}E(t)\). Inclusion–exclusion of the condition that no triangle is fully selected gives the **exact finite formula**
\[
W_5(S)=(-1)^{|S|}\sum_{\substack{A\subseteq\mathcal T\\S\subseteq U_A}}(-1)^{|A|}2^{10-|U_A|}.\tag{1}
\]
Indeed the indicator of triangle-freeness expands as the product of the ten factors \(1-\prod_{e\in E(t)}x_e\), where \(x_e\in\{0,1\}\); summing a Walsh character over an edge outside \(U_A\) cancels unless every edge of \(S\) lies inside \(U_A\). When this happens, each of the \(|S|\) selected mandatory edges contributes a negative sign and the \(10-|U_A|\) free edges contribute a power of two.

Formula (1), using at most \(1024\) triangle subsets and exact integer arithmetic, computes all \(1024\) coefficients. It yields precisely \(34\) permutation orbits with the values and multiplicities shown in the included complete table. The only zero orbits have least representatives \(63\), \(221\), and \(255\), of respective orbit sizes \(60\), \(60\), and \(30\). Their edge counts are \(6\), \(6\), and \(8\). The table has orbit-size sum \(1024\) and its values satisfy the exact Parseval check \(\sum_S W_5(S)^2=1024\cdot388\). An independent direct enumeration and Walsh–Hadamard transform verifies the same entire spectrum (see below). These exhaustively evaluated finite identities prove the classification, not just sampled instances.

For all \(n\), character diagonalization of convolution gives the multipliers \(W_n(S)\). At \(n=5\) the smallest positive multiplier magnitude from the full table is \(2\) and the largest is \(W_5(\varnothing)=388\), proving the rank, inverse-on-range norm, and condition number. For the orthogonal range projection, its multiplier is \(1_{W_5(S)\ne0}\). Its translation-invariant kernel is
\[
p_5(g)=2^{-10}\sum_{S:W_5(S)\ne0}(-1)^{|S\cap g|}.
\]
Its \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal \(\sum_g|p_5(g)|\). An exact integer Walsh transform of the \(874\) indicators gives \(\sum_g|1024p_5(g)|=7924\), hence \(7924/1024=1981/256\).

For \(n=3,4,6\), direct complete enumeration of all \(2^{\binom n2}\) edge subsets gives respectively \(7,41,5789\) triangle-free graphs. Every Walsh sum is then odd, hence nonzero. This proves the stated nonsingularity for these three sizes (no claim is made for all larger sizes). The cases \(n<3\) have no triangle constraint and are excluded from the phrase *first nontrivial*.

## Verification

Reproduce using only Python 3 standard library and a C++17 compiler:

```
python3 verify_ie.py
g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
./verify_direct
```

The first program independently evaluates (1), produces the \(34\) vertex-relabeling orbits of every frequency, checks all of `orbit_table.tsv`, finds the three zero orbits, and verifies Parseval and the endpoint norm. The C++ program instead enumerates every triangle-free graph for \(n=3,4,5,6\), takes its Walsh–Hadamard transform, and checks the full signed histogram, cancellation weights, Parseval, and the endpoint norm. They use different coefficient-computation methods and agree on the complete five-vertex spectrum. All computations are exact-integer and have been executed successfully from the packaged files. The finite exhaustive classification rests on the included bounded loops, not on any claimed unexecuted external certificate.

## Relationship to prior work

Triangle-free graph counting, finite graph properties, and Boolean Fourier transforms are well-established subjects. Hatami–Hladký–Král’–Norine–Razborov (2011) study pentagon extremals and triangle-free graph densities; Balogh–Petříčková (2014) count *maximal* triangle-free graphs asymptotically. The later paper *The Spectrum of Triangle-Free Graphs* (2022) studies a graph-matrix eigenvalue invariant rather than the Walsh transform of the indicator of a labelled graph property. None of those inspected works yields the present full \(1024\)-frequency census, the three cancellation-orbit shapes, or the sharp \(1981/256\) projection amplification. The elementary inclusion-exclusion principle and character diagonalization are background, not claimed as new.

## Limitations

This is an exact finite five-vertex spectral classification, not a general invertibility theorem for arbitrary vertex order. The odd-count argument only settles the additional stated orders \(3,4,6\). The work does not assert absolute historical priority against unindexed literature, and no independent mathematical audit has been carried out. The reported endpoint norm concerns the orthogonal range projection specifically; no minimum-among-all-projections assertion is made.

## References

1. H. Hatami, J. Hladký, D. Král’, S. Norine, A. Razborov, *On the Number of Pentagons in Triangle-Free Graphs*, public arXiv posting 2011-02-08, https://arxiv.org/abs/1102.1634 .
2. J. Balogh, N. Petříčková, *The number of the maximal triangle-free graphs*, arXiv:1409.8123, https://arxiv.org/abs/1409.8123 .
3. J. Balogh, F. Clemen, B. Lidický, S. Norin, J. Volec, *The Spectrum of Triangle-Free Graphs*, arXiv:2204.00093, https://arxiv.org/abs/2204.00093 .
