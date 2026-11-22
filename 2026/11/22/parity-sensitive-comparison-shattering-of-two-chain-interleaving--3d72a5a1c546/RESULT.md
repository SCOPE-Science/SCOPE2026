# Parity-sensitive comparison shattering of two-chain interleavings

## Finding

Fix integers \(a,b\ge1\). Let \(A_1\prec\cdots\prec A_a\) and \(B_1\prec\cdots\prec B_b\) be two chains, whose labels are ordered globally with every \(A\)-label before every \(B\)-label. Let \(\mathcal E_{a,b}\) be the **even** linear extensions of their disjoint union: words with \(a\) letters \(A\), \(b\) letters \(B\), preserving order within each chain and containing an even number of pairs in which a \(B\) precedes an \(A\). Query \(q_{i,j}\) asks whether \(A_i\) precedes \(B_j\).

For a word \(w\), write \(\partial(w)\) for its set of query pairs \((i,j)\) such that \(A_i\) and \(B_j\) appear **consecutively**, in either order, in \(w\). A set \(S\subseteq[a]\times[b]\) of query pairs is shattered by \(\mathcal E_{a,b}\) **if and only if**:

1. \(S=\{(i_t,j_t):1\le t\le k\}\) for strictly increasing lists \(i_1<\cdots<i_k\) and \(j_1<\cdots<j_k\); and
2. there is **no odd interleaving** \(w\) for which \(\partial(w)\subseteq S\).

The empty support satisfies the criterion. In particular, for every \(a,b\ge1\),

\[
\boxed{\operatorname{VCdim}(\mathcal E_{a,b})=
\begin{cases}
\min(a,b)-1,&a=b\text{ is odd},\\
\min(a,b),&\text{otherwise}.
\end{cases}}
\]

Thus the parity restriction leaves the unrestricted two-chain VC dimension unchanged except at the **equal odd-chain** boundary, where it drops by one. For illustration, the full shattered-support polynomials in the smallest balanced cases are \(1+8z+7z^2\) at \((a,b)=(3,3)\), \(1+16z+36z^2+14z^3+z^4\) at \((4,4)\), and \(1+24z+96z^2+91z^3+19z^4\) at \((5,5)\).

## Assumptions and scope

The concept class comprises only shuffles preserving the two **fixed internal chain orders**; it is not the full alternating group. Evenness is defined relative to the globally ordered labels \(A_1,\ldots,A_a,B_1,\ldots,B_b\). Every comparison \(q_{i,j}\) is a distinct Boolean instance, with answer one when \(A_i\) appears before \(B_j\). Shattering means that **all** \(2^{|S|}\) binary answer patterns occur among even shuffles. The dimension formula holds for all positive integer \(a,b\); polynomial coefficients above concern only the named finite examples.

## Proof

**1. Which supports are shattered by unrestricted shuffles?** Encode a shuffle by its nondecreasing gap vector \(0\le g_1\le\cdots\le g_a\le b\), where \(g_i\) counts \(B\)-letters preceding \(A_i\). Then \(q_{i,j}(w)=1\) exactly when \(g_i<j\). Two queried pairs in the same row or column cannot receive arbitrary answers. Nor can two pairs \((i,j),(i',j')\) with \(i<i'\), \(j>j'\), because the chain orders imply a fixed comparison between their truth values. Thus a shattered support must consist of strictly increasing pairs. Conversely, given such a support and arbitrary labels, choose the \(g_{i_t}\) to be \(j_t-1\) for label one and \(j_t\) for label zero. Since the \(j_t\) increase strictly, these choices are nondecreasing and extend to a valid gap vector. Hence **every** binary label pattern occurs among unrestricted shuffles exactly for these supports.

**2. The singleton-fiber parity lemma.** Fix the answer pattern on \(S\). The shuffles realizing it are the linear extensions of the poset obtained by adjoining the oriented queried comparisons to the two chains. Whenever this finite poset has at least two linear extensions, it has both even and odd ones: linear extensions are connected by swaps of adjacent incomparable elements (move the next desired element left successively to transform one extension into another), and each swap changes permutation sign. Thus a nonempty answer fiber lacks an even shuffle **exactly when it consists of one odd shuffle**.

A shuffle \(w\) is the unique realization of its answers on \(S\) exactly when \(\partial(w)\subseteq S\). For the forward implication, swapping any consecutive unlike letters whose comparison is not in \(S\) leaves all queried answers unchanged. For the reverse implication, if all consecutive unlike-letter comparisons are queried, no adjacent opposite-color swap preserves the answers; connectivity of the linear-extension graph rules out any other realization. Combining this fact with Step 1 proves the all-support criterion.

**3. The maximum support size.** Every increasing set of pairs has at most \(m=\min(a,b)\) members. Suppose \(a<b\) and choose \(S=\{(i,i):1\le i\le a\}\). A shuffle for which every consecutive unlike-letter pair lies in this diagonal must start with \(A\) when \(a\) is odd, or with \(B\) when \(a\) is even. Each interior same-letter run then has length two: after the first change of letter, the next allowed change must be at the next equal-index diagonal pair. The terminal run contains all excess \(B\)-letters. These rules determine **exactly one** possible word. If it starts with \(A\), all \(B\)-runs preceding later \(A\)-letters have even length; if it starts with \(B\), its initial one-letter \(B\)-run precedes an even number of \(A\)-letters and every other such \(B\)-run has length two. Thus in either case the unique word has even inversion parity. The support \(S\) is therefore shattered.

If \(a>b\), reverse every shuffle word and simultaneously interchange the names \(A,B\). The two operations together preserve the number of inversions modulo two and carry the just-proved diagonal construction to \(\{(a-b+j,j):1\le j\le b\}\). Hence that support of size \(b\) is shattered.

When \(a=b=m\), the only increasing support of size \(m\) is the full diagonal. Exactly two shuffles have all unlike-letter adjacencies on this diagonal: the alternating two-letter-run words starting with \(A\) and with \(B\). The first has even inversion parity. The second has inversion parity \(m\pmod 2\): its first \(B\) precedes all \(m\) occurrences of \(A\), while every later \(B\)-run that precedes an \(A\) has even length. Thus the full diagonal is shattered exactly when \(m\) is even. For odd \(m\), the subdiagonal \(S'=\{(i,i):1\le i\le m-1\}\) is shattered: any word containing both colors has a cross-color adjacency immediately after the first of its two final occurrences \(A_m,B_m\), so \(\partial(w)\) contains a pair whose \(A\)-index or \(B\)-index is \(m\). No \(\partial(w)\) can therefore be contained in \(S'\), and the criterion proves shattering. This includes \(m=1\), when \(S'\) is empty. The dimension formula follows.

## Verification

Two independently written standalone programs enumerate shuffles and supports, calculate every observed even-parity trace, and independently test the forbidden odd singleton criterion. They cross-check all \(66\) ordered positive profiles with \(a+b\le12\), including the full coefficient vectors, and verify the all-parameter formula in those profiles. Run `python3 verify_parity_shuffles.py` and `g++ -std=c++17 -O2 -Wall -Wextra verify_parity_shuffles.cpp -o verifier && ./verifier`. The delivered `python_report.txt` and `cpp_report.txt` record successful runs. These finite enumerations support but do **not** replace the all-parameter proof above.

## Relationship to prior work

Chase and Freitag's 2019 *Bounds in Query Learning* develops query-learning combinatorics. Diallo, Zopf and Fürnkranz's 2020 *Permutation Learning via Lehmer Codes* treats permutations and inversion counts in ranking prediction; neither derives this parity-sensitive two-chain Boolean trace law. Previous results describe all pair-comparison shattering for **unrestricted** linear extensions, or even permutations with **no fixed internal chain order**. Neither restriction commutes with taking all Boolean traces: fixing both chain orders can discard the only even realization of a label vector. In particular, the unrestricted two-chain static dimension is always \(\min(a,b)\), whereas the present restricted class loses one dimension precisely on balanced odd profiles. The general even-permutation forest criterion does not determine this smaller concept class.

## Limitations

No all-parameter closed formula for the entire shattered-support polynomial and no Littlestone dimension is claimed. The criterion may require enumerating candidate odd shuffles; it is an exact characterization, not an asserted polynomial-time algorithm. Symmetry in the labels is broken by the fixed parity convention, so the class cannot be identified with unrestricted two-chain shuffles. The literature comparison cannot exclude unindexed equivalent work, and no independent scientific audit has been performed.

## References

1. H. Chase and J. Freitag, *Bounds in Query Learning*, arXiv:1904.10122v1, first public 2019-04-23, https://arxiv.org/abs/1904.10122.
2. A. Diallo, M. Zopf, J. Fürnkranz, *Permutation Learning via Lehmer Codes*, ECAI 2020, DOI 10.3233/FAIA200206, published online 2020-09-18, https://doi.org/10.3233/FAIA200206.
3. *Parity-refined comparison shattering of even permutations*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-refined-comparison-shattering-of-even-permutations--824e5263ec2a.
4. *The first entropy obstruction for two-chain comparison shattering*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-first-entropy-obstruction-for-two-chain-comparison-shatterin--31054849abf0.
5. *Comparison shattering for linear extensions of finite posets*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-comparison-shattering-for-linear-extensions-of-finite-posets--aed8bda32d56.
