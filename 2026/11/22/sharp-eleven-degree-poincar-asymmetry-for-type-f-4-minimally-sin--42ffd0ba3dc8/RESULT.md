# Sharp eleven-degree Poincaré asymmetry for type-\(F_4\) minimally singular Schubert varieties

## Finding

Let \(G\) be a simply connected complex algebraic group of type \(F_4\), let \(B\) be a Borel subgroup, and let \(X_w=\overline{BwB/B}\) for \(w\in W=W(F_4)\). Define its ordinary Poincaré polynomial and its Kazhdan–Lusztig polynomial at the identity by
\[
H_w(q)=\sum_{x\le w}q^{\ell(x)}=\sum_{j=0}^{\ell(w)}a_j(w)q^j,
\qquad K_w(q)=P_{e,w}(q).
\]
The minimal nontrivial Kazhdan–Lusztig locus \(\mathcal M=\{w\in W:K_w(1)=2\}\) has exactly \(217\) elements, with precise profile
\[
\#\{K_w(q)=1+q\}=178,\quad
\#\{K_w(q)=1+q^2\}=33,\quad
\#\{K_w(q)=1+q^3\}=6.
\]
For every \(1\le k\le11\), let
\[
M_k=\max_{\substack{w\in\mathcal M\\2k<\ell(w)}}
\bigl(a_{\ell(w)-k}(w)-a_k(w)\bigr).
\]
The complete sharp spectrum, number of equality cases and cardinality of each eligible class are:

| \(k\) | \(M_k\) | Maximizers | Eligible \(w\) | General Weyl-group bound |
|---:|---:|---:|---:|---:|
| 1 | 1 | 178 | 217 | 1 |
| 2 | 4 | 48 | 215 | 4 |
| 3 | 9 | 16 | 177 | 9 |
| 4 | 15 | 4 | 111 | 16 |
| 5 | 18 | 4 | 70 | 25 |
| 6 | 15 | 2 | 36 | 36 |
| 7 | 16 | 2 | 16 | 48 |
| 8 | 14 | 2 | 6 | 60 |
| 9 | 8 | 2 | 6 | 71 |
| 10 | 5 | 2 | 2 | 80 |
| 11 | 2 | 2 | 2 | 87 |

There are no eligible elements at \(k\ge12\). Thus the universal upper bound given by the coefficient of degree \(k-1\) in the length polynomial of \(W(F_4)\) is attained **exactly for \(k=1,2,3\)**, and is strict for every higher eligible degree. The four maximizers at degrees \(4\) and \(5\) have length \(14\); the two at degrees \(6\) through \(9\) have length \(20\); and the two at degrees \(10\) and \(11\) have length \(23\).

## Assumptions and scope

All cohomology is rational ordinary cohomology of complex Schubert varieties, indexed by the full finite Weyl group of type \(F_4\); it is not intersection cohomology. The Kazhdan–Lusztig polynomials use the standard normalization \(P_{w,w}=1\) and constant term one when \(x\le w\). The Cartan matrix is
\[
\begin{pmatrix}
2&-1&0&0\\
-1&2&-2&0\\
0&-1&2&-1\\
0&0&-1&2
\end{pmatrix}.
\]
This is one exact finite family, not an assertion about all exceptional types, parabolic quotients or all rationally singular Schubert varieties.

## Proof

**1. Exhaustive Weyl group and independent length verification.** Represent each simple reflection on the root lattice by its integral \(4\times4\) matrix determined by the displayed Cartan matrix. Breadth-first traversal under right multiplication yields exactly \(1152\) distinct matrices, with largest word length \(24\). Independently, reflection closure of the four simple roots gives \(48\) roots, including \(24\) positive roots. Counting positive roots mapped to negative by each of the \(1152\) matrices reproduces every breadth-first length. Hence no nonreduced word has silently entered the census.

**2. Complete Bruhat intervals.** For each element obtained by multiplying a shorter element \(u\) on the right by a simple reflection \(s\) with \(\ell(us)=\ell(u)+1\), apply the subword theorem:
\[
[e,us]=[e,u]\cup\{vs:v\le u\}.
\]
Induction constructs the entire closed lower interval of every element. Their total cardinality, counting one interval membership per pair, is exactly \(396809\). Counting members at each length gives all the integers \(a_j(w)\).

**3. Complete Kazhdan–Lusztig recursion.** For \(sw<w\), use the standard Kazhdan–Lusztig recursion with the correction terms for \(z<sw\), \(sz<z\). Set \(\mu(z,sw)=[q^{(\ell(sw)-\ell(z)-1)/2}]P_{z,sw}\) when the exponent is integral, and zero otherwise. For \(x\le w\), its uncorrected expression is \(qP_{x,sw}+P_{sx,sw}\) if \(sx<x\), and \(P_{x,sw}+qP_{sx,sw}\) if \(sx>x\); subtract
\[
\sum_{\substack{x\le z<sw\\sz<z}}
\mu(z,sw)q^{(\ell(w)-\ell(z))/2}P_{x,z}.
\]
Terms with an incomparable lower index are zero. Every polynomial is constructed exactly over the integers. A separate implementation using right descents in place of left descents produces **identical polynomials for every one of the \(396809\) comparable pairs**, not merely for the \(217\) selected upper elements. These tests also verify constant terms and degree bounds.

**4. Exhaustive maxima.** Filter the \(1152\) upper elements by the condition \(\sum_j[q^j]P_{e,w}(q)=2\). The \(217\) resulting polynomials divide into the three classes shown. For each \(k\) with \(2k<\ell(w)\), subtract the two ranks of the exact Bruhat interval to obtain \(a_{\ell(w)-k}(w)-a_k(w)\). Exhaustive integer maximization yields the eleven rows above. The comparison column follows independently by expanding the standard length polynomial
\[
H_{w_0}(q)=[2]_q[6]_q[8]_q[12]_q,
\qquad [r]_q=1+q+\cdots+q^{r-1}.
\]
Since \(\ell(w)\le23\) on the selected locus, no \(k\ge12\) is eligible. This completes the proof.

## Verification

Run `python CHECK.py` with a standard Python 3 interpreter. The single standalone file reconstructs the root system, checks all \(1152\) lengths via the root-sign count, enumerates \(396809\) comparable pairs, independently evaluates every Kazhdan–Lusztig polynomial from left and right descents, and verifies the three membership counts plus all eleven rows. It uses exact integer arithmetic and no input files or external packages. The observed output begins `PASS: 1152 Weyl elements; 48 roots; 396809 Bruhat pairs` and ends with the eleven displayed degree records. The finite computation is exhaustive because the program enumerates the whole finite Weyl group, not a random sample.

## Relationship to prior work

Li, Rietsch and Yang (2025) connect ordinary opposite-degree Betti dimensions of Schubert varieties with divisorial factoriality criteria; their results do not classify the minimal nontrivial Kazhdan–Lusztig locus or its coefficientwise defect spectrum in type \(F_4\). Sentinelli and Zatti (2025) construct a weak Lehmer code and a method for rank polynomials of type-\(F_4\) lower Bruhat intervals, but do not impose \(P_{e,w}(1)=2\) or give the maximizer table. Burrull, Li, Zeng and Zhang (2026) establish the general coefficient inequality and exhibit sharp infinite families of types \(A\) and \(B\), but give no exceptional-type equality classification. Their manuscript became public on November 18, 2026, and is used here as subsequent comparative literature, not as the dated initiating source. General Kazhdan–Lusztig and Bruhat algorithms themselves are classical and are not claimed as new.

An existing classification of the **total** opposite-Betti defect over all type-\(F_4\) Schubert varieties, and a separate integral divisor-class census, do not determine these \(217\) conditioned elements, their eleven individual sharp values or their equality multiplicities.

## Limitations

The novelty claim is comparative, not an assertion of a complete global bibliography; equivalent unpublished or unindexed enumerations may exist. This proof provides a fully reproducible finite exact census, not a uniform closed-form theorem for exceptional ranks beyond type \(F_4\). It does not identify geometric equations for the singular loci of all equality cases. The public work cited from November 18, 2026 is later than the initiating June 23, 2025 source and is not used to determine that first public source date.

## References

1. C. Li, K. Rietsch and M. Yang, *An anticanonical perspective on G/P Schubert varieties*, arXiv:2506.18388v1 (first public June 23, 2025), https://arxiv.org/html/2506.18388v1.
2. P. Sentinelli and A. Zatti, *A weak Lehmer code for type \(F_4\)*, arXiv:2509.20981v1 (first public September 25, 2025), https://arxiv.org/html/2509.20981v2.
3. G. Burrull, Z. A. Li, S. Zeng and X. Zhang, *On the asymmetry polynomial of Schubert varieties*, arXiv:2611.24751v1 (first public November 18, 2026), https://arxiv.org/html/2611.24751v1.
4. D. Kazhdan and G. Lusztig, *Representations of Coxeter groups and Hecke algebras*, Invent. Math. 53 (1979), 165–184 (standard recursion).
5. M. Goresky, *Tables of Kazhdan–Lusztig Polynomials*, https://www.math.ias.edu/~goresky/tables.html (index of available classical comparison tables; type \(F_4\) not listed).
