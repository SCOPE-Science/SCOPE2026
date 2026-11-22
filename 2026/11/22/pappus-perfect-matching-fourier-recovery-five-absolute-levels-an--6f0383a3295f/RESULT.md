# Pappus perfect-matching Fourier recovery: five absolute levels and an exact inverse norm

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, understood as the bipartite Levi graph of the nine-point, nine-line Pappus configuration, with its \(27\) edges as distinct coordinates. Let \(G=\mathbb F_2^{E(P)}\). For every perfect matching \(M\) of \(P\), let \(\mathbf1_M\in G\) denote its edge-incidence vector. Define the **unnormalized counting convolution** on complex (or real) functions \(h:G\to\mathbb C\) by
\[
(T h)(x)=\sum_{M\in\mathcal M(P)}h(x\oplus\mathbf1_M).
\]
For each Fourier frequency \(S\subseteq E(P)\), its Walsh multiplier is
\[
W(S)=\sum_{M\in\mathcal M(P)}(-1)^{|M\cap S|}.
\]

**Theorem.** There are \(42\) perfect matchings. Every frequency satisfies \(W(S)\equiv2\pmod4\), so \(T\) is invertible on all \(2^{27}\) complex or real coordinates. Its **complete absolute multiplier spectrum** is:

| \(|W(S)|\) | Reduced multiplicity among \(2^{10}\) sign classes | Full multiplicity among \(2^{27}\) frequencies |
|---:|---:|---:|
| \(2\) | 504 | 66,060,288 |
| \(6\) | 342 | 44,826,624 |
| \(10\) | 81 | 10,616,832 |
| \(14\) | 96 | 12,582,912 |
| \(42\) | 1 | 131,072 |

In particular the sharp Hilbert-space inverse norm and condition number are
\[
\|T^{-1}\|_{\ell^2\to\ell^2}=\frac12,\qquad \kappa_2(T)=21.
\]
The unique inverse counting-convolution kernel is supported at **exactly all \(2^{10}=1024\) vectors** of an affine coset of the binary cycle space of \(P\), and its sharp endpoint operator norms are
\[
\boxed{\|T^{-1}\|_{\ell^1\to\ell^1}=\|T^{-1}\|_{\ell^\infty\to\ell^\infty}=\frac{1637}{210}.}
\]
These are exact norms for the full \(2^{27}\)-dimensional operator, not a restricted inverse or a projection norm.

## Assumptions and scope

The vertex set of the incidence model consists of nine points \(A,B,C,a,b,c,X,Y,Z\) and the nine line triples \(ABC,abc,AbX,aBX,AcY,aCY,BcZ,bCZ,XYZ\). A point is adjacent to a line precisely when it occurs in that triple. No embedding or planar-face choice is used. Its standard, independently used LCF representation is \([5,7,-7,7,-7,-5]^3\), with vertices taken modulo \(18\). These determine the same classical abstract Pappus graph [1, 4].

All values are exact integers or rationals; there are no sampling or floating-point steps. The Fourier convention is the unnormalized transform \(\widehat f(S)=\sum_{x\in G}f(x)(-1)^{S\cdot x}\); convolution itself is not divided by \(|G|\). For an operator norm, the domain and codomain are equipped with the ordinary counting-measure \(\ell^p(G)\) norms. There is no assertion about all incidence graphs, larger Levi graphs, all graph orders, or other kinds of convolution kernels.

## Proof

**1. Complete matching family and an arithmetic noncancellation certificate.** The nine-line incidence specification gives a \(9\times9\) zero-one matrix. A perfect matching is precisely a bijection from nine lines to nine points selecting a nonzero entry in each row. Enumerating the three permitted choices per row with unused columns gives exactly \(42\) matchings; the exhaustive recursion and a separate graph-theoretic matching enumeration from the LCF model are in `verify_pappus_walsh.py`. The Pappus graph is edge-transitive [1, 4], so every one of its \(27\) edges belongs to the same number \(m\) of perfect matchings. Counting pairs \((e,M)\) with \(e\in M\) gives \(27m=9\cdot42\), hence \(m=14\). The verifier also directly counts \(14\) matchings through every edge in *both* encodings.

For any negative-edge set \(S\), expand \(W(S)=\sum_M\prod_{e\in S}(1-2\mathbf1_{\{e\in M\}})\) in integers. Modulo four, all terms involving at least two selected edges disappear, leaving
\[
W(S)\equiv42-2\sum_{e\in S}|\{M:e\in M\}|=42-28|S|\equiv2\pmod4.
\]
Thus no Walsh multiplier is zero, with no untested frequencies hidden by the later reduction.

**2. Exhaustive ten-sign classification.** Choose any spanning tree of \(P\). It has \(17\) edges, leaving \(10=27-18+1\) chords. Multiplying an edge sign by the product of signs assigned to its endpoints preserves the **absolute** signed matching sum: every perfect matching uses each vertex exactly once, so every term acquires the same factor \(\prod_v g(v)\). Since the tree is connected, vertex sign switches can make every tree-edge sign positive. Each assignment of the ten residual chord signs represents exactly \(2^{17}\) of the \(2^{27}\) original frequency assignments. Therefore there are exactly \(1024\) absolute-sign classes, not merely a sample.

For a chord mask \(u\in\mathbb F_2^{10}\), let \(a(u)\) count perfect matchings with that chord-incidence mask. The exact Walsh-Hadamard transform
\[
w(t)=\sum_{u\in\mathbb F_2^{10}}a(u)(-1)^{t\cdot u}
\]
produces the complete five-level absolute histogram in the theorem. The standalone verifier reconstructs \(a\) from each of the two graph descriptions, transforms all \(1024\) coordinates, and independently evaluates all \(1024\) signed permanents using a row-by-row subset recurrence in the incidence representation. Each of the five reduced multiplicities is then multiplied by \(2^{17}\). The smallest and largest absolute multipliers are exactly \(2\) and \(42\), giving the Hilbert norm and condition number by Fourier diagonalization.

**3. Exact full inverse and its endpoint norm.** The edge-incidence vectors of perfect matchings lie in one affine coset \(\mathbf1_{M_0}+C\) of the graph's binary cycle space \(C\), because any two perfect matchings have even-degree symmetric difference. Connectivity gives \(\dim C=10\). Conversely, the ten chord bits uniquely determine an even-degree edge subset, so they coordinatize \(C\) and its affine translate. The verifier confirms that the differences of the \(42\) matching masks span all ten dimensions.

Since \(w(t)\) never vanishes, invert the signed convolution on this affine coset. With \(L=\operatorname{lcm}(2,6,10,14,42)=210\), put \(b(t)=L/w(t)\in\mathbb Z\), and form the *integer* Walsh transform
\[
q(u)=\sum_{t\in\mathbb F_2^{10}}b(t)(-1)^{t\cdot u}.
\]
The inverse kernel at the unique edge vector of the matching coset with chord mask \(u\) is exactly \(q(u)/(1024\cdot210)\), and it is zero outside that coset. This follows because the Fourier transform of the proposed inverse is \(1/W(S)\) for every one of the full \(2^{27}\) characters; the verifier checks this identity exactly, as well as independent selected XOR convolution coefficients.

Here is the **complete signed integer numerator distribution** of \(q\); every entry is obtained by exact integral Walsh inversion:

| Numerator \(q(u)\) | Count |
|---:|---:|
| −13,312 | 6 |
| −4,096 | 18 |
| −1,536 | 135 |
| −1,024 | 342 |
| −512 | 243 |
| 1,024 | 18 |
| 2,048 | 216 |
| 8,192 | 45 |
| 11,264 | 1 |

The counts total \(1024\), none of the entries vanishes, and \(\sum_u|q(u)|=1,676,288=1024\cdot1637\). Thus \(\|g\|_{\ell^1(G)}=1637/210\). For a convolution kernel on a finite group, its \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal the kernel's \(\ell^1\) norm: the upper bound is Young's inequality; a delta input attains the \(\ell^1\) bound and a phase/sign-aligned input attains the \(\ell^\infty\) bound. As the inverse is unique, this is the full sharp deconvolution constant.

## Verification

Run `python3 verify_pappus_walsh.py` using Python 3.9 or newer. It needs only the Python standard library, builds the incidence and LCF graph representations independently, enumerates their perfect matchings with exhaustive vertex branching, checks their \(27\) edge marginals, constructs the entire \(1024\)-class Walsh spectrum twice, evaluates the signed permanent for every incidence class by an unrelated subset recurrence, checks rank-ten spanning, computes the exact rational inverse, and checks the inverse convolution in Fourier space and by selected direct XOR sums. The terminal assertion marker is `PAPPUS_WALSH_EXACT_PASS`. The code contains no stored output table that is used as input; all expected numerical values are independently asserted against regenerated data.

## Relationship to prior work

The Pappus Levi graph, its LCF representation, symmetry, and pseudotwo-factor-isomorphic behavior are classical and are *not* new claims [1–4]. Abreu and collaborators' original work [2, Proposition 3.3] shows that complementary two-factors have Hamiltonian or three-hexagon configurations, and their later classification [3] identifies the Pappus graph as an exceptional irreducible Levi graph. Neither establishes the signed sum for all \(2^{27}\) edge-sign choices, its five absolute levels or the endpoint inverse constant. The already published Pappus perfect-matching flip-graph classifications [5, 6] enumerate \(42\) states and describe relations under alternating cycle switches; the **number \(42\) is prior context**, and flip adjacency alone does not determine the explicit Walsh spectrum of edge-incidence vectors or the inverse convolution kernel.

Signed permanent/one-factor identities provide broad general algorithms, but an unevaluated permanent expression is not the same as the complete Pappus-specific signed distribution and exact inverse norm. Public mathematical-record and literature searches for Pappus, signed permanent, Walsh spectrum, gauge signs, Fourier inverse, and the fraction \(1637/210\) did not identify a statement already covering this result. This is a bounded novelty comparison, not proof of global historical uniqueness.

## Limitations

The finding applies only to the fixed Pappus graph and unnormalized binary edge-incidence convolution, not to arbitrary weighted matchings, graph families, or perturbation stability. Its finite computation is exhaustive for the indicated finite object but gives no general all-order theorem. Previously published material establishes the ordinary perfect-matching count, and further unindexed accounts of random signed permanents or toroidal dimer models could contain equivalent invariants. No independent external scholarly audit has yet been performed.

## References

[1] E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html (classical LCF representation and symmetry).

[2] M. Abreu, A. A. Diwan, B. Jackson, D. Labbate and J. Sheehan, *Pseudo 2-Factor Isomorphic Regular Bipartite Graphs*, J. Combin. Theory Ser. B 98 (2008), 432–442, https://doi.org/10.1016/j.jctb.2007.08.006 (full author text examined).

[3] M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1, first public 2010-02-09, https://arxiv.org/abs/1002.1891 (full publicly reproduced text examined).

[4] M. Abreu, D. Labbate and J. Sheehan, *Pseudo and Strongly Pseudo 2-Factor Isomorphic Regular Graphs*, arXiv:1002.1033v1, first public 2010-02-04, https://arxiv.org/abs/1002.1033.

[5] *The Pappus perfect-matching hexagon-flip graph is two alternating hexagon triangles*, publicly archived result, 2026-10-25, record `157dc0be9f8c` (matching count and alternating-cycle reconfiguration, full result examined).

[6] *Hexagon parity and octagon mobility in Pappus perfect matchings*, publicly archived result, 2026-11-02, record `b52665049fe7` (matching count and flip-graph connectivity, full result examined).
