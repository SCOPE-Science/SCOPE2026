# Exact variance and Gaussian fluctuations of binary two-burst deletion spheres

## Finding

Let \(n\ge4\), and let \(X=(X_1,\ldots,X_n)\) be uniformly distributed on \(\{0,1\}^n\). Let \(B_n(X)\) be the number of **distinct** length-\(n-4\) words obtained by deleting exactly two disjoint contiguous blocks of two symbols from \(X\). The number of deletion-position pairs that lead to the same output is not counted with multiplicity. Then

\[
\mathbb E B_n=\frac{n^2-3n+4}{8},\qquad
\operatorname{Var}(B_n)=\frac{(n-4)(2n^2-15n+31)}{32}.
\]

Furthermore, as \(n\to\infty\),

\[
\frac{B_n-\mathbb E B_n}{n^{3/2}/4}\ \Longrightarrow\ N(0,1).
\]

The variance is zero at \(n=4\), and strictly positive for every \(n\ge5\). In particular the order of typical sphere-size fluctuations is \(n^{3/2}\), compared with a mean of order \(n^2\).

## Assumptions and scope

The alphabet is exactly binary; the source letters are independent and uniform. The two length-two deleted blocks are disjoint (adjacent blocks are allowed) and no substitutions or extra errors occur. Deletion positions are considered only to define a **set** of outputs, not a probability distribution on outputs. For clarity, index the source coordinates starting at one. The theorem addresses \(n\ge4\), including the single-output boundary case \(n=4\).

Put \(m=n-2\), and define the delayed comparison indicators

\[
T_i=\mathbf1\{X_i\ne X_{i+2}\},\qquad 1\le i\le m.
\]

The change of variables from \((X_1,\ldots,X_n)\) to \((X_1,X_2,T_1,\ldots,T_m)\) is bijective over binary vectors, because \(X_{i+2}=X_i\oplus T_i\). Thus \(T_1,\ldots,T_m\) are independent Bernoulli variables with parameter \(1/2\).

## Proof

**1. Count distinct outputs using canonical deletion histories.** For \(n=4\), deletion removes the entire source, so \(B_4=1\); the formulas below continue to hold. For \(n\ge5\), a history consists of two disjoint deleted intervals of length two. Two adjacent intervals form one contiguous cluster of length four; nonadjacent intervals form two clusters. The maximal-compact-representation theorem for burst deletions (Wang, Kong, Yaakobi and Duman, arXiv:2606.01245, Propositions 1–2) gives each distinct output exactly one canonical history: a cluster starting at \(i\) with \(c\) consecutive deleted length-two blocks is canonical precisely when the next available symbol \(X_{i+2c}\) differs from every \(X_{i+2r}\), \(0\le r<c\); at the right boundary this requirement is vacuous. This canonicalization is established for all burst lengths and alphabet sizes in the cited work; only its \((2,2)\) specialization is used here.

For a single length-four cluster there is one automatic boundary history, beginning at \(i=n-3\). For its \(m-2\) other possible starts \(1\le i\le m-2\), binary canonicality is equivalent to \(T_i=0\) and \(T_{i+2}=1\). For two separated length-two clusters, write their starting positions as \(i,j\) with \(j\ge i+3\). If the second cluster begins at the last allowed start \(j=n-1\), canonicality requires only \(T_i=1\); otherwise it requires both \(T_i=T_j=1\). Therefore, *pointwise for every binary source*, 

\[
B_n=1+\sum_{i=1}^{m-2}(1-T_i)T_{i+2}
+\sum_{i=1}^{m-2}T_i
+\sum_{\substack{1\le i<j\le m\\j-i\ge3}}T_iT_j.\tag{1}
\]

The final sum is interpreted as zero when its index set is empty. Formula (1) can also be tested without the cited canonicalization by direct enumeration of output sets, as in the standalone checker.

**2. Center the polynomial.** Set \(Z_i=T_i-1/2\), so that independent \(Z_i\) have mean zero, variance \(1/4\), and take values \(\pm1/2\). Expanding (1), the coefficient of \(T_i\) is \(a_i=\mathbf1\{i\le m-2\}+\mathbf1\{i\ge3\}\); the coefficient of \(T_iT_j\), for \(i<j\), is

\[
w_{ij}=\begin{cases}-1,&j-i=2,\\1,&j-i\ge3,\\0,&j-i=1.\end{cases}\]

Let \(d_i\) denote the number of indices among \(i-1,i+1\) that belong to \(\{1,\ldots,m\}\); it is one at the endpoints and two elsewhere (for \(m\ge2\)). The number of indices at distance two from \(i\) is \(a_i\). Consequently the coefficient of \(Z_i\) after centering is

\[
c_i=a_i+\frac12\sum_{j\ne i}w_{\min(i,j),\max(i,j)}
=\frac{m-1-d_i}{2}
=\begin{cases}(m-2)/2,&i\in\{1,m\},\\(m-3)/2,&2\le i\le m-1.\end{cases}\]

Therefore

\[
B_n-\mathbb EB_n=\sum_{i=1}^m c_iZ_i
+\sum_{i<j}w_{ij}Z_iZ_j.\tag{2}
\]

The linear and quadratic monomials in independent centered variables are mutually orthogonal in \(L^2\), as are distinct quadratic monomials.

**3. Compute the moments.** Taking expectations in (1), the first sum contributes \((m-2)/4\), the second \((m-2)/2\), and the last \((m-2)(m-3)/8\). Thus

\[
\mathbb E B_n=1+\frac{(m-2)(m+3)}8
=\frac{n^2-3n+4}{8}.
\]

There are exactly \((m-2)(m-1)/2\) nonzero coefficients \(w_{ij}\), while

\[
\sum_i c_i^2=\frac{(m-2)(m^2-4m+5)}4.
\]

Equation (2) and orthogonality yield

\[
\operatorname{Var}(B_n)
=\frac14\sum_i c_i^2+\frac1{16}\sum_{i<j}w_{ij}^2
=\frac{(m-2)(2m^2-7m+9)}{32}
=\frac{(n-4)(2n^2-15n+31)}{32}.
\]

These formulas include \(m=2\), for which all sums are empty and \(B_4=1\).

**4. Prove asymptotic normality.** The linear term in (2) equals

\[
\frac{m-3}{2}\sum_{i=1}^{m}Z_i+\frac12(Z_1+Z_m),
\]

and the quadratic term has variance \((m-2)(m-1)/32=O(m^2)\). After division by \(n^{3/2}/4\), the quadratic term and the bounded endpoint correction converge to zero in \(L^2\). The remaining linear term satisfies the usual central limit theorem for independent fair Bernoulli variables and converges to \(N(0,1)\) under this normalization. Slutsky's lemma finishes the proof.

## Verification

Run `python3 checker.py` in the directory containing the embedded file. The checker constructs deletion outputs directly from every binary source at lengths four through thirteen (\(16{,}368\) exhaustive sources), compares their distinct-output counts with formula (1), and computes exact rational means and variances. It additionally compares the channel and canonical counts on \(1{,}000\) seeded larger examples, for a total of \(17{,}368\) sources. All tests passed. The infinite-length formulas and limit law are proved above, rather than inferred from these experiments.

## Relationship to prior work

Lan, Sun, Yu and Ge (arXiv:2504.20460, first posted April 29, 2025) determine the **maximum** burst-deletion sphere size and a family attaining it; their result does not present random-center second moments or limiting fluctuation laws. Wang, Kong, Yaakobi and Duman (arXiv:2606.01245, first posted May 31, 2026) prove canonical representations and bounds for arbitrary burst-deletion balls, and specialize to two length-two bursts. Their canonical theorem is an essential input here. The present theorem concerns an explicitly evaluated *average over all binary source words*, its exact variance, and a Gaussian fluctuation limit. These conclusions require exploiting the independence of the interleaved difference indicators and the orthogonality of their quadratic terms. The earlier structural enumeration is not claimed to be new. An earlier result not found in the inspected literature may still exist.

The analogous exact variance for **two single-symbol deletions** is a distinct channel invariant: deleting two individual symbols does not have the same outcome sets as deleting two disjoint two-symbol blocks.

## Limitations

This theorem does not evaluate a nonuniform source model, a nonbinary alphabet, or more than two length-two bursts. It does not determine optimal correcting-code size, nor the complete finite-length probability distribution of sphere sizes. The canonical-history theorem invoked in the proof is a published mathematical input rather than a newly established contribution. The verification program tests finitely many examples and is not an independent proof or an external audit; historical-priority search cannot exclude unindexed results.

## References

1. C. Wang, X. Kong, E. Yaakobi and T. M. Duman, *Bounds on Multiple \(b\)-Burst Deletion-Correcting Codes*, arXiv:2606.01245v2 (2026), Sections II–III, Propositions 1–2; https://arxiv.org/html/2606.01245.
2. Z. Lan, Y. Sun, W. Yu and G. Ge, *Sequence Reconstruction under Channels with Multiple Bursts of Insertions or Deletions*, arXiv:2504.20460v1 (2025), Section IV-A; https://arxiv.org/html/2504.20460v1.
