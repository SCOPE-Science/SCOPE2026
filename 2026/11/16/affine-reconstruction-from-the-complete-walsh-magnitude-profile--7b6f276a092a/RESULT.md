# Affine reconstruction from the complete Walsh-magnitude profile of seven-point binary sets

## Finding
Let \(E\subseteq\mathbb F_2^d\) consist of exactly seven distinct points, \(d\ge3\). For each \(a\in\{1,3,5,7\}\), define the normalized multiplicity
\[
p_a(E)=2^{-d}\#\{u\in\mathbb F_2^d: |W_E(u)|=a\},\qquad W_E(u)=\sum_{x\in E}(-1)^{u\cdot x}.
\]
The four-number profile \((p_1,p_3,p_5,p_7)\) **uniquely determines the affine-equivalence class of \(E\)**. Precisely six profiles exist, and they are all realized as soon as \(d\ge6\):

| Affine dimension \(r\) | Affine-relation weights | \((p_1,p_3,p_5,p_7)\) |
| --- | --- | --- |
| \(6\) | none | \((35,21,7,1)/64\) |
| \(5\) | \(4\) | \((19,9,3,1)/32\) |
| \(5\) | \(6\) | \((15,15,1,1)/32\) |
| \(4\) | \(4,4,4\) | \((11,3,1,1)/16\) |
| \(4\) | \(4,4,6\) | \((9,6,0,1)/16\) |
| \(3\) | seven occurrences of \(4\) | \((7,0,0,1)/8\) |

Here the relation-weight column records the Hamming weights of all nonzero vectors of the affine-relation code, with repetitions. For a fixed ambient dimension \(d\), keep exactly the rows with \(r\le d\). Every nonzero unnormalized Walsh coefficient is odd; hence **all seven-point indicator transforms have full Fourier support**, yet their finer absolute-magnitude distributions distinguish all six affine types. In particular, each profile determines the affine dimension from \(p_7=2^{-r}\), and then the relation-code type from \(p_5\).

## Assumptions and scope
All vector spaces, linear dependencies, characters and affine maps are over \(\mathbb F_2\). Points of \(E\) are distinct and unordered; changing their order permutes relation-code coordinates. The transform is unnormalized, so every coefficient is an odd integer in \(\{-7,-5,-3,-1,1,3,5,7\}\). Affine equivalence allows any invertible affine map of the ambient space; for two embedded affine spans of equal dimension, an affine bijection between the spans extends to an ambient invertible affine map. The claim concerns **indicators of seven points**, not weighted signals or general seven-sparse functions.

## Proof
**1. The affine-relation code.** Temporarily label the seven points \(x_1,\ldots,x_7\), and define
\[
R_E=\left\{v\in\mathbb F_2^7:\ \sum_{j=1}^7v_j=0,\ \sum_{j=1}^7v_jx_j=0\right\}.
\]
It is a binary linear code of dimension \(t=6-r\), where \(r=\dim\operatorname{aff}(E)\). Every relation has even Hamming weight, and no nonzero relation can have weight \(2\), because all points are distinct. Consequently the nonzero words of \(R_E\) have weight \(4\) or \(6\). Furthermore, \(R_E\) completely characterizes the configuration up to affine equivalence and coordinate permutation: two lists have the same relation kernel precisely when the linear maps taking each augmented standard basis column to \((1,x_j)\) are related by a linear isomorphism preserving the first-coordinate functional. This isomorphism induces an affine bijection between their affine spans.

**2. At most three independent relations.** The radius-one binary Hamming spheres centered at the words of \(R_E\) are pairwise disjoint, because distinct words have distance at least four. Since every codeword is even, the seven radius-one neighbors of each word are all odd. There are only \(2^6=64\) odd words of length seven; hence \(7\cdot2^t\le64\), implying \(0\le t\le3\). Thus \(3\le r\le6\).

**3. Complete relation-code classification.** If \(t=0\), the relation space is zero. If \(t=1\), its unique nonzero vector has weight four or six, giving two coordinate-permutation classes. If \(t=2\), no two distinct words may have weight six, since their supports omit two different singletons and their XOR would have weight two. The three nonzero word weights are therefore either \((4,4,4)\) or \((4,4,6)\). In the first case, two generating weight-four words intersect in two coordinates; in the second, they intersect in exactly one coordinate. For each pattern, the intersection and difference regions of the two supports have uniquely determined sizes, proving a single coordinate-permutation class.

If \(t=3\), again at most one nonzero codeword could have weight six. Let \(h\in\{0,1\}\) be the number of weight-six words, and let \(z\) be the number of coordinates vanishing identically on \(R_E\). At each of the remaining \(7-z\) coordinates, a nonzero linear functional takes value one on exactly four of the eight words of \(R_E\). Counting total Hamming weights gives
\[
4(7-z)=4(7-h)+6h=28+2h.
\]
Thus \(h=z=0\), and every nonzero word has weight four. Fix a basis of \(R_E\) and regard its seven generator-matrix columns as elements of \(\mathbb F_2^3\). They are all nonzero, since \(z=0\). For every nonzero \(u\in\mathbb F_2^3\), exactly four columns have \(u\)-dot-product one. Hence the sum of their seven signs \(\sum_j(-1)^{u\cdot c_j}=-1\); at zero it is seven. Fourier inversion on \(\mathbb F_2^3\) shows that each nonzero column occurs exactly once. This is the unique binary simplex \([7,3,4]\) code up to coordinate permutation.

All six relation classes are **realizable**. Given any one of these six even-weight codes \(R\subseteq\mathbb F_2^7\) with no weight-two word, form the quotient \(V=\mathbb F_2^7/R\). The parity functional descends to a well-defined nonzero linear functional on \(V\); the seven cosets of the standard unit vectors lie in its affine level-one hyperplane, are pairwise distinct, and have exactly relation kernel \(R\). This is a seven-point affine configuration of dimension \(6-\dim R\). Embed it into any \(\mathbb F_2^d\) with \(d\ge r\).

**4. Walsh magnitudes from the dual code.** Define \(C=R_E^\perp\subset\mathbb F_2^7\). The affine evaluations of a linear character on the seven points give a vector in \(C\), up to a common additive bit, which changes only the sign of its Walsh sum. Each local dual character occurs equally often in the ambient frequency space. Consequently the relative frequency of \(|W_E|=a\) is the same as the relative frequency, for uniform \(c\in C\), of \(|7-2\operatorname{wt}(c)|=a\).

The ordinary binary dual-weight identity gives
\[
\sum_{c\in C}z^{\operatorname{wt}(c)}
=\frac1{|R_E|}\sum_{v\in R_E}(1+z)^{7-\operatorname{wt}(v)}(1-z)^{\operatorname{wt}(v)}.
\]
Substitute the six completely classified weight multisets from Step 3. Grouping complementary weights \(j\) and \(7-j\) yields, respectively, the six displayed rows. As a check, in the no-relation case \(C=\mathbb F_2^7\) and the row is \((70,42,14,2)/128=(35,21,7,1)/64\). The other rows are exact binomial expansions of the same identity, without asymptotics or numerical thresholds.

**5. Rigidity.** The final entry satisfies \(p_7=2^{-r}\), since the only evaluation sign vectors with all seven equal are the two constant vectors in \(C\), and \(|C|=2^{r+1}\). Thus \(p_7\) determines \(r\). Within each of the two repeated dimensions \(r=5\) and \(r=4\), the two \(p_5\) values differ. The four-value profile therefore distinguishes the six relation-code classes, which by Step 1 are exactly the six affine-equivalence classes. This completes the proof in every ambient dimension.

## Verification
The accompanying dependency-free Python 3 script `CHECK.py` enumerates **every** even binary relation subspace of length seven having minimum nonzero weight at least four. It finds exactly \(1,42,175,30,0\) admissible subspaces in dimensions zero through four, verifies that they form precisely six coordinate-permutation orbits, and checks the claimed dual-code Walsh magnitudes for **every** subspace. In a mathematically separate direct test, it evaluates all \(\binom{16}{7}=11440\) seven-point subsets of \(\mathbb F_2^4\) and their complete Walsh transforms, verifying the three available profiles for every subset. The four-dimensional class counts are \(240,6720,4480\), corresponding respectively to affine dimensions \(3\), \(4\) with weights \((4,4,4)\), and \(4\) with weights \((4,4,6)\). It also verifies the dual weight-enumerator coefficient identity using integer binomial sums. Run `python3 CHECK.py`. The all-dimensional theorem follows from Steps 1–5, not from finite testing.

## Relationship to prior work
The binary MacWilliams dual-weight identity (1963) and the \([7,3,4]\) simplex code are established coding-theory tools. Tan's 2012 lecture notes describe the general Fourier analysis of Boolean functions, not an inverse affine-reconstruction classification of exactly seven unweighted points. Two closely related existing studies classify, respectively, all six-point binary-set Walsh magnitude profiles and the nonzero-Fourier-support cardinalities of eight-point binary sets. The former concerns even-valued magnitudes and four affine types; the latter counts only nonzero coefficients and distinguishes affine dimension rather than all classes. Neither theorem states or logically implies the six rows here. The distinctive seven-point feature is that all coefficient supports coincide with the full dual group, yet the **magnitude distribution alone** reconstructs the affine class.

The classical coding-theoretic ingredients are not claimed as new. The asserted classification is the synthesis of the exact seven-point relation-space classification, its six full magnitude profiles, and the Fourier affine-rigidity consequence. An earlier equivalent small binary-code weight-enumerator table is an explicit historical-priority risk; no claim of exhaustive literature coverage is made.

## Limitations
The theorem applies only to indicators of exactly seven distinct points over characteristic two. No conclusions about recovering individually labelled point coordinates, arbitrary seven-sparse coefficients, or robustness to measurement noise follow from it. All Walsh coefficients are nonzero for the elementary parity reason, which is not itself an original assertion. The proof is self-contained apart from classical finite Fourier orthogonality and the dual-weight identity, with an independently implemented exact finite check, but no independent mathematical audit has been performed. Historical priority against all possible coding-theory tables is not established.

## References
1. F. J. MacWilliams, *A Theorem on the Distribution of Weights in a Systematic Code*, Bell System Technical Journal **42** (1963), 79–94, https://doi.org/10.1002/j.1538-7305.1963.tb04003.x. Classical dual-weight identity.
2. Li-Yang Tan, *Analysis of Boolean Functions*, arXiv:1205.0314v1, first posted 2012-05-02, https://arxiv.org/abs/1205.0314. Fourier-analytic context.
3. *Complete Walsh-magnitude spectra and affine rigidity of six-point binary sets* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-walsh-magnitude-spectra-and-affine-rigidity-of-six-poin--5c39c1154219.
4. *The complete Walsh Fourier-support spectrum of eight-point binary sets* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-walsh-fourier-support-spectrum-of-eight-point-binar--bc4834afd25d.
