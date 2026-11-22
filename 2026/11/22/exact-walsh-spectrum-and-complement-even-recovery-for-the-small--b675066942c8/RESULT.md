# Exact Walsh spectrum and complement-even recovery for the small Witt design

## Finding
Let \(W_{12}=(V,\mathcal H)\) be the Steiner system \(S(5,6,12)\), so \(|V|=12\) and each five-element subset belongs to exactly one of its 132 six-element blocks (hexads). Identify hexads with their binary incidence vectors in \(G=\mathbb F_2^{12}\). Let \(h:G\to\{0,1\}\) be their indicator, and \(T_h f(x)=\sum_{y\in G}h(y)f(x+y)\), with no probability normalization. The Walsh multiplier at the character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) is \(\Lambda(S)=\sum_{B\in\mathcal H}(-1)^{|B\cap S|}\).

The complete signed spectrum, with each multiplier's multiplicity, is

| Multiplier | Multiplicity |
|---:|---:|
| \(-12\) | 924 |
| \(0\) | 2048 |
| \(4\) | 990 |
| \(52\) | 132 |
| \(132\) | 2 |

The zero characters are **exactly** the odd-cardinality subsets \(S\). Thus \(\operatorname{rank}T_h=2048\), \(\operatorname{nullity}T_h=2048\), its positive/negative/zero inertia is \((1124,924,2048)\), and its range is precisely the complement-translation-invariant subspace \(\{f:f(x)=f(x+\mathbf1)\}\). On that range, the least singular value is \(4\), the largest is \(132\), the exact Euclidean condition number is \(33\), and \(\|T_h^\dagger\|_{2\to2}=1/4\). The orthogonal range projection is \(Qf(x)=(f(x)+f(x+\mathbf1))/2\), a norm-one projection on every \(\ell^p(G)\), \(1\le p\le\infty\). The product of nonzero singular values has exact 2-adic valuation \(4096\).

## Assumptions and scope
The only combinatorial assumption is the defining property of the small Witt design \(S(5,6,12)\); no generator matrix or choice of point labels enters the theorem. The group is the Boolean group under coordinatewise XOR, Walsh transforms are **unnormalized**, and operator norms are taken with counting-measure \(\ell^2(G)\). A spectral zero means a lost Fourier mode, not a missing hexad. The statement is about all 4096 characters of this particular 12-point design, not arbitrary block designs.

## Proof
For any \(0\le j\le5\), each fixed \(j\)-subset is contained in exactly
\[\lambda_j=\frac{\binom{12-j}{5-j}}{\binom{6-j}{5-j}},\qquad(\lambda_0,\ldots,\lambda_5)=(132,66,30,12,4,1).\]
This follows by double-counting pairs \((F,B)\) with \(F\) a five-set extending the fixed \(j\)-set and \(B\) its unique block.

We first prove complement-closure without assuming it. Fix a block \(C\), and let \(A_i\) count blocks intersecting \(C\) in exactly \(i\) points. Distinct blocks cannot meet in five or six points, so \(A_5=0\), \(A_6=1\). The incidence identities
\[\sum_i\binom{i}{j}A_i=\binom6j\lambda_j\quad(0\le j\le5)\]
give, descending from \(j=4\) to \(j=0\), the vector \((A_0,A_1,A_2,A_3,A_4,A_5,A_6)=(1,0,45,40,45,0,1)\). The unique block disjoint from \(C\) is its six-point complement, so \(C^c\in\mathcal H\).

The sign identity \((-1)^r=(1-2)^r=\sum_j\binom rj(-2)^j\), followed by the design incidence counts, gives for every \(S\subseteq V\) of size \(k\le6\)
\[\Lambda(S)=\sum_{j=0}^{\min(k,5)}\binom{k}{j}(-2)^j\lambda_j+64\mathbf1_{\{k=6,\ S\in\mathcal H\}}.\]
Indeed the additional \(j=6\) term exists only at \(k=6\), when its incidence count is one for a block and zero otherwise. Because hexads occur in complement pairs, \(\Lambda(S)=0\) for odd \(k\). Also \(\Lambda(S^c)=\Lambda(S)\) since every hexad has size six. Consequently it suffices to evaluate even \(k=0,2,4,6\): the values are \(132,-12,4\), and \(52\) on a hexad versus \(-12\) on a non-hexad six-set.

There are \(\binom{12}{0}+\binom{12}{12}=2\) characters of value \(132\), \(\binom{12}{2}+\binom{12}{10}+\binom{12}{6}-132=924\) of value \(-12\), \(\binom{12}{4}+\binom{12}{8}=990\) of value \(4\), and exactly 132 of value \(52\). Odd subsets number 2048 and contribute zeros, completing the spectrum. Walsh orthogonality diagonalizes convolution. The nonzero multiplier magnitudes are \(4,12,52,132\); this proves the rank, inertia, conditioning and pseudoinverse norm. A character is invariant under translating its argument by \(\mathbf1\) precisely when its weight is even; hence the stated range and averaging projection. Every nonzero magnitude is congruent to \(4\) modulo \(8\), so each contributes exactly two factors of two. Therefore the 2-adic valuation of the nonzero singular-value product is \(2\cdot2048=4096\).

## Verification
Run \(\texttt{python3 verify_witt.py}\) using the standard library. The checker generates the extended ternary Golay code from a fully printed six-row generator, selects its distinct weight-six supports, independently verifies all 792 five-set incidences and complement-closure, evaluates all 4096 Walsh characters by direct signed summation and by a separate fast Walsh--Hadamard transform, and compares against the closed formulas and exact histogram. It also checks Parseval and spectral bounds. The finite calculation certifies this explicit 12-point model; the abstract design proof above establishes that the result is independent of representation.

## Relationship to prior work
The 132 hexads, 5-design property and complement pairing are classical and are not claimed as new; see Havlicek--Lenz (2001), whose complete freely available paper proves an explicit construction. The additional spectral statement is the **entire signed Boolean Walsh spectrum and exact complement-even convolution recovery law**, including sharp spectral constants. The spectrum follows from the classical incidence parameters but is not identified as such in the inspected construction paper. Searches of related mathematical literature and published result records did not locate equivalent coverage; this is a bounded historical comparison, not a priority certificate.

## Limitations
The result is a finite-design theorem, not a general theorem for arbitrary Steiner systems. All numerical assertions can be reproduced exactly; the computation does not constitute a proof for any larger class of designs. An earlier unindexed equivalent character-sum calculation might exist.

## References
1. H. Havlicek and H. Lenz, *Another simple proof for the existence of the small Witt design*, Elemente der Mathematik **56** (2001), 89--94; https://ems.press/journals/em/articles/585 ; https://www.geometrie.tuwien.ac.at/havlicek/pub/anothersimple.pdf .
2. C. Godsil, *Witt Designs*, chapter 11 of lecture notes on finite geometry; https://www.math.uwaterloo.ca/~cgodsil/pdfs/bigGeom.pdf .
