# The parity split in quaternary rank-two code distortion

## Finding
Let \(C,E\subseteq\mathbb F_4^n\) be linear codes of dimension two, of the same length and with identical Hamming weight enumerators. Write the five weights of their one-dimensional message classes, in nondecreasing order, as \(0<a_1\le a_2\le a_3\le a_4\le a_5\); each occurs three times among the fifteen nonzero codewords. We use \(\mathcal D(C,E)\), the minimum Hamming distortion of an invertible \(\mathbb F_4\)-linear map between the codes, with distortion the maximum of the output/input nonzero Hamming-weight ratios divided by their minimum.

**Theorem.** For every integer \(n\ge2\), an isospectral fiber of rank-two quaternary codes consists of one monomial linear equivalence class when two of the five \(a_i\)'s coincide, and of exactly two such classes when they are all distinct. The distortion within either class is one. The exact distortion between the two classes in the distinct-weight case is
\[
\mathcal D(C,E)=\left(\min_{1\le i<5}\frac{a_{i+1}}{a_i}\right)^2.
\]
An isospectral pair of linearly inequivalent codes is possible if and only if \(n\ge10\). At \(n=10\), the unique isospectral fiber with two classes has common weight enumerator
\[
W(z)=1+3(z^6+z^7+z^8+z^9+z^{10}),
\]
and its two classes have distortion exactly \(100/81\). For every \(n\ge10\), there is such a pair with distortion exactly \((n/(n-1))^2\).

The equivalence relation here permits coordinate permutations and nonzero coordinate scalings over \(\mathbb F_4\), **not** a global field automorphism. If the Frobenius field automorphism is also admitted, the two classes merge.

## Assumptions and scope
Take \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). All ranks and all linear maps are over \(\mathbb F_4\). A code of dimension two is the row space of a full-rank \(2\times n\) matrix. The five projective directions in \(\mathbb F_4^2\) can be represented by \((1,0),(0,1),(1,1),(1,\alpha),(1,\alpha^2)\). A zero column is allowed. Distortion is measured only on nonzero codewords, which ensures all denominators are positive.

The two codes have the *same* length \(n\) and the *same* ordinary Hamming weight enumerator, with no coordinate ordering or column basis fixed. In the theorem's distinct case, the weights are automatically strictly positive and strictly ordered. An isospectral fiber means the family of codes with fixed length and fixed weight enumerator, taken modulo monomial \(\mathbb F_4\)-linear equivalence.

## Proof
**1. Recovering the column profile from the spectrum.** Choose a rank-two generator matrix. Write \(z\) for its number of zero columns, \(N=n-z\) for its number of nonzero columns, and \(m_P\) for the multiplicity of the projective direction \(P\) among its nonzero columns. Thus \(\sum_Pm_P=N\). A nonzero message row \(u\in\mathbb F_4^2\) vanishes on precisely one projective column direction, its kernel \(P(u)\). Its codeword has weight
\[
a_{P(u)}=N-m_{P(u)}.\]
Each kernel direction corresponds to three scalar multiples of \(u\), so
\[
W_C(t)=1+3\sum_{P\in\mathbb P^1(\mathbb F_4)}t^{N-m_P}.
\]
The sum of the five projective weights is \(4N\), because \(\sum_P(N-m_P)=5N-N=4N\). Hence \(N\), the number \(z=n-N\) of zero columns, and the *unordered* five-tuple of multiplicities \(\{m_P\}\) are uniquely recovered from the common weight enumerator. Conversely, equal \(n,z\) and a permutation of this five-tuple give equal enumerators. Coordinate permutation and scaling identify exactly matrices having the same labeled projective multiplicities in a suitable row basis.

**2. The projective action and the number of classes.** A change of generator basis acts on the five column directions by \(\operatorname{PGL}_2(\mathbb F_4)\). It is faithful and has order \(|\operatorname{GL}_2(\mathbb F_4)|/3=60\), so its permutation image in \(S_5\) is the index-two alternating group \(A_5\). One can also see that all its elements are even because it equals \(\operatorname{PSL}_2(4)\). If all five \(m_P\) are distinct, the stabilizer of their assignments in \(S_5\) is trivial, and the \(S_5\)-orbit splits into precisely two \(A_5\)-orbits, distinguished by parity. If some multiplicities repeat, the stabilizer contains an odd transposition exchanging equal entries; thus every permutation assignment lies in one \(A_5\)-orbit. This proves the asserted one-versus-two classification.

**3. Exact distortion.** Fix increasing, *distinct* weights \(a_1<\cdots<a_5\). Label the five projective nonzero-message classes of \(C\) in this order. Within a given equivalence class, a monomial isometry gives distortion one. For two codes in opposite parity classes, the induced matching of these five ordered weight classes under any invertible \(\mathbb F_4\)-linear isomorphism is an odd permutation \(\pi\); conversely, every odd matching can occur, because the projective basis-change group acts as all even permutations. Its distortion is
\[
D_\pi=\frac{\max_i(a_{\pi(i)}/a_i)}{\min_i(a_{\pi(i)}/a_i)}.
\]
Set \(\delta=\min_{i<5}a_{i+1}/a_i>1\). Every odd \(\pi\) has an inversion \(i<j\) with \(\pi(i)>\pi(j)\). For such a pair, monotonicity of the weights gives
\[
D_\pi\ge\frac{a_{\pi(i)}/a_i}{a_{\pi(j)}/a_j}
=\frac{a_{\pi(i)}}{a_{\pi(j)}}\frac{a_j}{a_i}
\ge\delta^2,
\]
since each factor compares two strictly increasing weights and hence is at least the smallest consecutive ratio \(\delta\). The inversion need not involve adjacent positions; the argument applies to every odd permutation.
An adjacent transposition of \(i,i+1\) attaining the minimum \(\delta\) is odd; it fixes the other three classes and has ratios \(\delta,\delta^{-1},1,1,1\). Its distortion equals \(\delta^2\). Therefore the displayed formula is exact. Any linear isomorphism between two dimension-two subspaces extends to an invertible linear transformation of \(\mathbb F_4^n\) by completing source and target bases, so restricting the minimization to isomorphisms of codes gives the same value as the ambient formulation of code distortion.

**4. The first length and a uniform construction.** Distinct weights are equivalent to distinct nonnegative integers \(m_P\), whose sum \(N\le n\). Their minimum possible sum is \(0+1+2+3+4=10\). Hence no split is possible for \(n<10\). At \(n=10\), the unique unordered multiplicities are \(\{0,1,2,3,4\}\), with no zero generator columns. Choose generators \(G,H\) with respective projective-column multiplicity profiles
\[
(0,1,2,3,4)\quad\text{and}\quad(1,0,2,3,4)
\]
in the ordered directions listed in the assumptions. Both have rank two and share the claimed spectrum, but are in opposite parity classes. Their increasing weights are \(6,7,8,9,10\), giving minimum adjacent ratio \(10/9\), hence distortion \(100/81\).

For any \(n\ge10\), use profiles \((0,1,2,3,n-6)\) and \((1,0,2,3,n-6)\). They give five distinct multiplicities and common increasing weights \(6,n-3,n-2,n-1,n\). The least adjacent ratio is \(n/(n-1)\), since all others are at least as large for \(n\ge10\). Their two classes therefore have distortion \((n/(n-1))^2\). The matrices have no zero columns.

**5. Semilinear boundary.** Frobenius \(x\mapsto x^2\) fixes the projective directions \((1,0),(0,1),(1,1)\) and interchanges \((1,\alpha)\) and \((1,\alpha^2)\). Its induced permutation is odd. Adjoining Frobenius to \(A_5\) generates \(S_5\), so all assignments with a given multiset become semilinearly equivalent. This does not contradict the linear classification above because Frobenius is not \(\mathbb F_4\)-linear.

## Verification
The included standalone `verify.py` implements arithmetic in \(\mathbb F_4\), enumerates all invertible two-by-two matrices, recovers their 60 projective actions, and verifies they are exactly the even permutations of the five directions; it also verifies the odd Frobenius action. It directly expands the two length-ten generator matrices and checks all 15 nonzero codeword weights, computes their exact minimum distortion as the fraction \(100/81\), tests the repeated-multiplicity orbit conclusion on exhaustive short profiles, and tests the distinct-weight distortion formula on 150 additional profiles. Run with `python verify.py`. This finite checking supplements, but does not replace, the proof of the all-length theorem.

## Relationship to prior work
Bennett, Fox, and Morrell (2026) introduce the precise \(\mathbb F_q\)-linear code-distortion invariant and study its general algorithmic complexity and approximations; their exact general algorithm does not supply this quaternary isospectral classification or the closed parity-penalty formula. Bouyukliev, Bouyuklieva, and Kurz (2020) classify linear codes under a broader equivalence that includes field automorphisms; under that convention the parity split in this theorem disappears. Cameron's group-theory notes identify \(\operatorname{PGL}(2,4)\cong A_5\), used in the argument. These are prerequisites and comparisons, not assertions that group theory or weight enumerators are new.

## Limitations
The result concerns quaternary linear dimension-two codes, equal lengths, and identical Hamming weight enumerators. It does not assert an analogous parity dichotomy for other fields, dimensions, nonlinear codes, or distinct weight spectra. The classes depend on forbidding global Frobenius automorphism. Historical priority beyond the inspected published literature is not independently established, and no independent mathematical audit has been performed.

## References
1. H. Bennett, M. Fox, and B. Morrell, *The Code Distortion Problem*, arXiv:2607.26261 (first public 2026-07-28); APPROX/RANDOM 2026, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2026.24. https://arxiv.org/abs/2607.26261
2. I. Bouyukliev, S. Bouyuklieva, and S. Kurz, *Computer classification of linear codes*, 2020, freely accessible manuscript: https://epub.uni-bayreuth.de/id/eprint/4618/1/LinCodeAugmentation_arxiv.pdf
3. P. J. Cameron, *Group Theory Notes 6*, \(\operatorname{PGL}(2,4)\cong A_5\): https://maths.qmul.ac.uk/~pjc/MTHM024/gn6.pdf
