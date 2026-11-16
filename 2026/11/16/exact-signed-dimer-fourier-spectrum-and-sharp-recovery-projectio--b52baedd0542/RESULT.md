# Exact signed-dimer Fourier spectrum and sharp recovery projection on the four-cube

## Finding
Let \(Q_4\) be the graph on \(\mathbb F_2^4\), with edges between vertices of Hamming distance one, and let \(E\) be its 32 labelled edges. Write \(\mathcal M\subseteq\mathbb F_2^E\) for the incidence vectors of its 272 perfect matchings. For the unnormalized Walsh transform
\[
W(s)=\sum_{M\in\mathcal M}(-1)^{\sum_{e\in M}s_e},\qquad s\in\mathbb F_2^E,
\]
the complete absolute-value distribution is given by the following table. Multiplicities are for a gauge-normalized set of \(2^{17}\) frequencies; each must be multiplied by \(2^{15}\) to obtain the multiplicity on the full 32-coordinate frequency group.

| \(|W|\) | Reduced multiplicity |
|---:|---:|
| 0 | 44230 |
| 8 | 44896 |
| 16 | 20299 |
| 24 | 9152 |
| 32 | 7472 |
| 40 | 2784 |
| 48 | 568 |
| 56 | 96 |
| 64 | 980 |
| 72 | 288 |
| 80 | 124 |
| 88 | 96 |
| 128 | 54 |
| 136 | 32 |
| 272 | 1 |

In particular, the counting-convolution operator \(Tg=1_{\mathcal M}*g\) on \(\ell^2(\mathbb F_2^E)\) has exact rank \(2,845,638,656\) and nullity \(1,449,328,640\). Its least nonzero singular value is \(8\), so
\[
\|T^\dagger\|_{2\to2}=\frac18,
\qquad
\frac{\max_s|W(s)|}{\min_{W(s)\ne0}|W(s)|}=34.
\]
Every multiplier is divisible by \(8\), and \(8\) occurs. The first vanishing frequencies have support size two; exactly 96 two-edge frequencies vanish, precisely those supported on adjacent edges of \(Q_4\). For the orthogonal projection \(P\) onto the range of \(T\), the **sharp** endpoint norm is
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}
=\frac{2,597,417}{32,768}.
\]
It is also the smallest possible endpoint operator norm among *all* linear projections onto that translation-invariant range, on either \(\ell^1\) or \(\ell^\infty\).

## Assumptions and scope
The vertex labels are integers \(0,\ldots,15\), interpreted as binary four-tuples; the 32 undirected edges are sorted lexicographically by their integer endpoints. A perfect matching covers all 16 vertices once and therefore consists of eight edges. The Walsh transform and counting convolution are **unnormalized**, while the inverse Fourier transform has the usual factor \(2^{-32}\). The norm on finite \(\ell^p\) is the standard counting-measure norm. In particular, \(T^\dagger\) means the Moore--Penrose inverse, which acts as reciprocal multiplication by \(W(s)\) on nonzero Fourier frequencies and as zero on the Fourier kernel.

The claim is an exact, finite classification for the **four-dimensional** hypercube, equivalently the four-by-four *toroidal* square grid \(C_4\square C_4\). This is not the 16-vertex *open* grid \(P_4\square P_4\), whose edge set and perfect matchings differ. No claims are made for larger hypercubes.

## Proof
**1. Spanning-tree gauge reduction.** For a vertex-label vector \(a\in\mathbb F_2^{16}\), define its edge coboundary \((\delta a)_{uv}=a_u+a_v\). Every perfect matching covers each vertex exactly once. Therefore
\[
W(s+\delta a)=(-1)^{\sum_v a_v}W(s).
\]
The graph is connected, so the space of coboundaries has dimension \(15\). Fix a spanning tree \(R\) consisting of 15 edges, and use vertex switches to set all frequency coordinates on \(R\) equal to zero. Every coboundary coset has a unique representative in this gauge. The complement \(C=E\setminus R\) has 17 edges, giving \(2^{17}\) reduced frequency assignments, each corresponding to \(2^{15}\) full assignments with the same multiplier magnitude and vanishing status.

**2. Exact full reduced spectrum.** Enumerate matchings recursively by taking the least uncovered vertex \(u\), matching it to each still-uncovered neighbour, and recursing. These branches are disjoint, and every perfect matching follows a unique branch, so this exhaustive procedure yields precisely the 272 matchings. Record for each matching its 17-bit restriction to \(C\); these restrictions are distinct because the symmetric difference of two matchings is a union of cycles, and any nonempty cycle cannot lie entirely in the spanning tree. Let \(h\) be the indicator of the 272 restrictions on \(\mathbb F_2^{17}\). Then the reduced multipliers are exactly \(W=H_{17}h\), where \(H_{17}\) is the integer Walsh--Hadamard matrix. The 17 exact butterfly stages implemented in `verify_walsh.py` yield the displayed complete table, with \(44,230\) zeros and minimum positive absolute value \(8\). The checker's exact Parseval certificate is
\[
\sum_{s\in\mathbb F_2^{17}}W(s)^2=2^{17}\cdot272=35,651,584.
\]
An independently implemented verifier `verify_permanent.cpp` uses the other exact formula for every signed partition function: the permanent of the signed \(8\times8\) bipartite adjacency matrix. A subset recurrence evaluates **each** of the \(131,072\) signed permanents, independently reproducing the entire absolute-value table and the Parseval total. These methods agree entry for entry on the table, including all zero and nonzero values. Thus the finite calculations are exhaustive, not samples.

**3. First vanishing support.** Symmetry of the four-cube acts transitively on its 32 edges. Every matching uses eight edges, so each edge belongs to \(272\cdot8/32=68\) matchings. A singleton Walsh character consequently has multiplier \(272-2\cdot68=136\), never zero. For two distinct edges \(e,f\), inclusion--exclusion gives
\[
W(1_e+1_f)=272-2\cdot68-2\cdot68+4N(e,f)=4N(e,f),
\]
where \(N(e,f)\) is the number of perfect matchings containing both edges. An adjacent pair cannot coexist, hence has zero multiplier. The exact pair enumeration in `verify_walsh.py` shows that every disjoint pair can coexist, so there are precisely \(16\binom42=96\) vanishing pairs and no others.

**4. Rank and inversion constants.** Since convolution is diagonal in the Walsh basis, the full rank is \((131072-44230)2^{15}=2,845,638,656\); the other \(44,230\cdot2^{15}=1,449,328,640\) characters form its nullspace. Singular values are \(|W(s)|\); the displayed extremal values \(8\) and \(272\) therefore prove the pseudoinverse norm and condition number without further approximation.

**5. Sharp range-projection norm.** The range projection has Fourier multiplier \(1_{W\ne0}\). Since this support is invariant under the coboundary space, its inverse Walsh kernel is supported on the orthogonal complement of coboundaries, namely the 17-dimensional cycle space. The restriction of a cycle vector to chord edges \(C\) is a linear bijection onto \(\mathbb F_2^{17}\). Therefore the convolution kernel's \(\ell^1\) norm equals
\[
2^{-17}\sum_{y\in\mathbb F_2^{17}}
\left|\sum_{s:W(s)\ne0}(-1)^{\langle s,y\rangle}\right|.
\]
A second exact 17-stage integer Walsh transform of the support indicator has absolute sum \(10,389,668\), both checkers agreeing independently. Thus the norm is \(10,389,668/131,072=2,597,417/32,768\). Convolution by a real symmetric kernel has \(\ell^1\) and \(\ell^\infty\) norms equal to the kernel absolute sum, attained by a point mass or aligned signs, respectively. Finally, averaging *any* projection onto the translation-invariant Fourier range over all group translations cannot increase its endpoint norm. The averaged projection is translation-invariant and therefore uniquely the Fourier support projection. This also proves optimality among all projections onto the range.

## Verification
The package contains `verify_walsh.py` (Python standard library) and `verify_permanent.cpp` (C++17 standard library) plus exact outputs. Run from the package directory:

```text
python3 verify_walsh.py > walsh_result.json
c++ -O2 -std=c++17 verify_permanent.cpp -o verify_permanent
./verify_permanent > permanent_result.json
```

Both JSON results must agree on their shared keys: all 15 spectrum levels, 44,230 reduced zeros, 86,842 reduced nonzeros, minimum nonzero magnitude 8, gcd 8, exact squared sum 35,651,584, projection absolute sum 10,389,668, and projection denominator 131,072. The Python checker also checks all 496 two-edge characters and singleton coefficients. The results file `verification_results.json` records the independently reproduced exact values. The checker source files and that result file are embedded with full hashes and sizes in the accompanying portable package.

## Relationship to prior work
Kenyon's *Lectures on Dimers* (2009), Sections 3.2 and 4.2, develops weighted perfect-matching partition functions, vertex gauge equivalence, and toroidal Kasteleyn techniques. In particular, gauge equivalence is established prior work. Kiwi and Loebl's *Types of Perfect Matchings in Toroidal Square Grids* (initial public version 2014) studies the same toroidal graph class but classifies parity homology types and their cycle-rooted forest representations, not the distribution of signed partition functions over all independent edge-sign gauges. The general Arf-invariant/Pfaffian formula is a stronger **evaluation mechanism** for weighted partition functions but supplies neither this numerical all-signing magnitude histogram nor the absolute Fourier-support transform needed for the endpoint norm without further exhaustive computation.

Östergård and Pettersson's *Enumerating Perfect Matchings in n-Cubes* (2012 online) concerns matching totals and equivalence classes, and the count 272 is not claimed as new. Related published finite studies determine the homotopy type and anti-forcing spectra of the four-cube perfect-matching family, or the Fourier transform for complete-graph perfect matchings on eight vertices; those invariants do not determine the present 32-edge Fourier zero set or projection norm. The complete finite spectrum and sharp endpoint recovery norm stated here were not found in the accessible compared work. That is a bounded priority assessment, not a claim of proven historical uniqueness.

## Limitations
The theorem addresses only the 16-vertex four-cube, not a general dimension or an arbitrary toroidal square grid. The signed all-frequency histogram and projection sum rely on complete integer computations, not on a closed-form symbolic expression across dimensions. The standard gauge reduction and weighted-dimer machinery are prior art. An unindexed source or an inaccessible full account of earlier cube matching enumerations could contain an equivalent finite table; available abstracts do not resolve that possibility. No independent external mathematical audit is claimed.

## References
[1] R. Kenyon, *Lectures on Dimers*, arXiv:0910.3129v1, first posted 2009-10-16; Sections 3.2 and 4.2. https://arxiv.org/abs/0910.3129

[2] M. Kiwi and M. Loebl, *Types of Perfect Matchings in Toroidal Square Grids*, arXiv:1406.3317v1, first posted 2014-06-12; Sections 1--3, Theorems 3 and 9. https://arxiv.org/abs/1406.3317 . Full text inspected at https://kam.mff.cuni.cz/~loebl/clanky/afterEJC07.pdf

[3] P. R. J. Östergård and V. H. Pettersson, *Enumerating Perfect Matchings in n-Cubes*, *Order* 30 (2013), 821--835, first published online 2012-11-21. https://doi.org/10.1007/s11083-012-9279-8
