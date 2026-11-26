# Exact leading constant for seven-one prefix-normal binary words

## Finding

Let \(a_7(n)\) be the number of binary words of length \(n\) containing exactly seven ones and satisfying 1-prefix normality: for every length \(1\le k\le n\), the length-\(k\) prefix has at least as many ones as any length-\(k\) contiguous factor. Then

\[
 a_7(n)=\frac{289}{2488320}\,n^6+O(n^5)\qquad(n\to\infty).
\]

Equivalently, among length-\(n\) binary words with seven ones and first symbol one, the limiting fraction that are prefix normal is

\[
 \lim_{n\to\infty}\frac{a_7(n)}{\binom{n-1}{6}}=\frac{289}{3456}.
\]

Both formulas constitute one leading-coefficient theorem, not separate unrelated claims.

## Assumptions and scope

Words are finite, binary, labeled by their positions, and have exactly seven occurrences of one. The word is 1-prefix normal, not 0-prefix normal. The asymptotic is for integer lengths tending to infinity with the number of ones fixed at seven. The first letter must be one. For \(n<7\), \(a_7(n)=0\).

Write the seven one-positions as \(1=p_1<p_2<\dots<p_7\le n\). Put \(r_i=p_{i+1}-p_i\) and \(s_i=r_i-1\ge0\) for \(1\le i\le6\), and put \(t=n-p_7\ge0\). Thus \(n=7+t+\sum_{i=1}^6s_i\). The trailing zeros are unconstrained once the six internal gaps are fixed.

## Proof

**Step 1: exact gap characterization.** For \(k\in\{1,2,3,4,5\}\), a run of \(k+1\) consecutive ones beginning at the \(j\)-th one spans \(1+\sum_{i=j}^{j+k-1}r_i\) positions. The word is 1-prefix normal exactly when the earliest \(k+1\) ones have minimum span among all runs of \(k+1\) consecutive ones. Otherwise the shorter later run is a factor containing more ones than the prefix of that factor's length. Conversely, if the first run has minimum span for every run size, every length permitting \(k+1\) ones anywhere also permits that many in its prefix. Hence the defining conditions are exactly

\[
 \sum_{i=1}^ks_i\le \sum_{i=j}^{j+k-1}s_i,
 \quad 1\le k\le5,\quad 2\le j\le7-k.
\]

There are fifteen such inequalities. This is the fixed-density form of the gap criterion in Lemma 8 of Burcsi–Fici–Lipták–Ruskey–Sawada [1], but the numerical volume computation below is additional.

**Step 2: lattice-polytope reduction.** Define the bounded rational polytope

\[
 P=\left\{s\in\mathbb R_{\ge0}^6:\sum_{i=1}^6s_i\le1,
 \ \sum_{i=1}^ks_i\le\sum_{i=j}^{j+k-1}s_i
 \ (1\le k\le5,\ 2\le j\le7-k)\right\}.
\]

For every integer \(n\ge7\), the map from a word to its internal zero gaps is a bijection between the words counted by \(a_7(n)\) and lattice points of \((n-7)P\). The trailing zeros are uniquely recovered as \(t=n-7-\sum_i s_i\). Therefore

\[
 a_7(n)=\#\bigl((n-7)P\cap\mathbb Z^6\bigr).
\]

The polytope is full dimensional: vectors with strictly increasing internal gaps satisfy the fifteen inequalities strictly, and they can be scaled to have total below one. Ehrhart's theorem for rational polytopes gives

\[
 a_7(n)=\operatorname{vol}_6(P)(n-7)^6+O(n^5)
 =\operatorname{vol}_6(P)n^6+O(n^5).
\]

**Step 3: exact rational volume.** The homogeneous cone has 21 defining nonnegative linear forms: the six coordinates and the fifteen comparison forms from Step 1. Every extreme ray lies in the nullspace of five independent active forms. Exhaustively enumerating the \(\binom{21}{5}=20349\) possible five-tuples by exact minors, and retaining orientations satisfying all 21 inequalities, gives exactly the following 14 primitive nonnegative rays:

```
(0,0,0,0,0,1)  (0,0,0,0,1,0)  (0,0,0,1,0,0)
(0,0,1,0,0,1)  (0,0,1,0,1,0)  (0,0,1,1,0,0)
(0,1,0,1,0,1)  (0,1,0,1,1,0)  (0,1,1,0,1,1)
(0,1,1,0,2,0)  (0,1,1,1,0,1)  (0,2,1,1,1,1)
(0,2,1,1,2,0)  (1,1,1,1,1,1)
```

Intersect each ray with the hyperplane \(\sum_i s_i=1\), dividing its coordinates by their sum. These fourteen points are all vertices of the five-dimensional cross-section. Enumerating supporting affine hyperplanes with exact rational normals gives its complete face lattice (155 nonempty faces, including vertices and the whole polytope). Fan-triangulating faces recursively from their rational vertex barycenters and coning each resulting five-simplex to the origin gives exactly 2184 six-simplices. The signed-orientation-free coordinate volumes sum by the exact determinant formula

\[
 \operatorname{vol}_6(P)=\frac1{6!}
 \sum_{\Delta}\left|\det(v_{\Delta,1},\ldots,v_{\Delta,6})\right|
 =\boxed{\frac{289}{2488320}},
\]

where the six vectors in each determinant are the consecutive barycenters of a maximal nested flag of nonempty faces, starting from the whole cross-section down to a vertex. The complete rational-integer procedure, including enumeration of active sets, orientation tests, face constraints, flags, and all determinants, is executable as the standalone `verify.py` supplied with this result. No floating-point tolerance enters the exact proof. Combining with Step 2 proves the theorem. Since \(\binom{n-1}{6}=n^6/720+O(n^5)\), the equivalent probability limit equals \(720\cdot289/2488320=289/3456\).

## Verification

Run `python3 verify.py` using Python 3 standard libraries only. It recomputes the cone's 14 extreme rays from all 20349 possible active sets, enumerates the 155 exact faces and 2184 simplex flags, and verifies the rational volume \(289/2488320\) without numerical geometry software. Independently it enumerates all length-\(n\) seven-one binary words directly, tests every contiguous factor for prefix normality, and compares against six-gap lattice enumeration for every integer \(7\le n\le17\). Counts at lengths 7 through 17 are respectively

```
1, 4, 13, 31, 71, 134, 249, 417, 688, 1062, 1628
```

These finite checks provide corroboration, while the all-length asymptotic follows from the exact polytope bijection, rational volume certificate, and Ehrhart's theorem, not from extrapolating these counts.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada [1] introduced the fixed-density generating functions, proved a general rationality statement, and gave explicit generating functions only for densities at most six (Proposition 16, Section 4.2). Their subsequent discussion explicitly reports that computation did not extend their list to densities above six. The gap criterion of their Lemma 8 is an input here. The present result treats the first density beyond that explicit list, but only its exact leading constant: it **does not** give the full density-seven generating function. Balister and Gerke [2] prove growth bounds for prefix-normal words across all densities; those bounds do not determine the density-seven coefficient. The generation algorithms of [3] do not yield this reported volume or coefficient. The general sequence OEIS A194850 [4] counts all densities pooled, so its finite values are not an explicit seven-one asymptotic.

## Limitations

No full rational generating function, lower-order quasi-polynomial terms, or uniform asymptotic as density grows with word length is established. The numerical coefficient comes from a finite exact-arithmetic polyhedral computation supplied in full, rather than a compact manual symbolic closed-form triangulation. The computations are reproducible but have not undergone independent audit. A later or unindexed equivalent computation cannot be categorically excluded by literature searches.

## References

[1] P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017v1 (first publicly posted 2016-11-28), especially Lemma 8 and Proposition 16. https://arxiv.org/abs/1611.09017

[2] P. Balister, S. Gerke, *The asymptotic number of prefix normal words*, arXiv:1903.07957 (2019). https://arxiv.org/abs/1903.07957

[3] P. Burcsi, G. Fici, Z. Lipták, R. Raman, J. Sawada, *Generating a Gray code for prefix normal words in amortized polylogarithmic time per word*, arXiv:2003.03222 (2020). https://arxiv.org/abs/2003.03222

[4] OEIS Foundation, *A194850: Number of prefix normal words of length n*. https://oeis.org/A194850
