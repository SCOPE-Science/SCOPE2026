# The sharp three-descendant stability gap for binary two-step length-two palindromic duplication

## Finding

For every integer \(n\ge4\), among binary length-\(n\) sources, the greatest number of distinct descendants after **exactly two sequential length-two palindromic duplications** is the previously known
\[
M_n=\frac{n^2+5n-8}{2}.
\]
The **strict second-highest** number is
\[
\boxed{M_n-3=\frac{n^2+5n-14}{2}}.
\]
It is attained by exactly four sources: precisely one pair of neighboring bits is equal, and that pair is the first or last adjacency; all other neighboring pairs are unequal. The two alternating words are the maximum-level sources. Every other nonalternating source has at most \(M_n-4\) descendants.

In a parity-alternating coordinate change conjugating palindromic duplication to reverse-complement duplication, the left-endpoint second-level words have exactly \(n-1,3n-7,\binom{n-1}{2}\) descendants with three, four, five zero symbols. The corresponding right-endpoint words have \(n,3n-8,\binom{n-1}{2}\) descendants. The two different weight spectra have the same total, namely \(M_n-3\).

## Assumptions and scope

The alphabet is \(\{0,1\}\); positions are indexed from zero. For a binary word \(x\) of length at least two, let \(T_i(x)\), \(0\le i\le |x|-2\), replace the two-symbol factor \(ab=x_i x_{i+1}\) by \(abba\). Define
\[
D_2(x)=\{T_j(T_i(x)):0\le i\le n-2,\ 0\le j\le n\}.
\]
This is an exact-two sequential sphere, not an at-most-two ball or a count of error histories. There is no restriction on overlap or reuse of inserted symbols. The classification is asserted only for \(n\ge4\); smaller lengths have different boundary behavior.

## Proof

**1. A universal canonical history bound.** For each first start \(i\), a second start \(j\ge i+4\) duplicates a length-two block disjoint from the first original block. Commuting the two operations replaces the history \((i,j)\) by \((j-2,i)\), which has the same final word. Hence every descendant is represented by a canonical history in
\[
\mathcal H_n=\{(i,j):0\le i\le n-2,\ 0\le j\le\min(n,i+3)\}.
\]
Counting these gives
\[
|\mathcal H_n|=\frac{n^2+5n-8}{2}=M_n.
\]
The known alternating-word calculation attains this bound [1, Section 5.1], so it is sharp. This paragraph is background; neither the bound nor the alternating maximizers is claimed as new.

**2. A local loss principle.** If \(v\) is a contiguous length-\(m\) factor of \(x\), shift the canonical history starts of \(v\) by the start position of the factor. The shifted starts remain canonical for \(x\), and the corresponding output is an unchanged exterior prefix, followed by the local output, followed by an unchanged exterior suffix. Therefore if \(v\) identifies \(r\) of its \(M_m\) canonical history outputs, then \(x\) identifies at least \(r\) among its own \(M_n\), so
\[
|D_2(x)|\le M_n-\bigl(M_m-|D_2(v)|\bigr).
\]
Direct evaluation of the at most twelve canonical histories for the following short factors gives \(|D_2(000)|=1\), \(|D_2(0110)|=10\), and therefore respective deficits \(7\) and \(4\) against \(M_3=8\) and \(M_4=14\). Complementation preserves these sizes. Consequently any triple of equal bits forces a deficit of at least seven; any factor of the form \(abba\) for distinct bits \(a,b\) forces a deficit of at least four.

**3. Why only isolated endpoint defects can reach the second level.** Call an index \(i\) a defect when \(x_i=x_{i+1}\). In a source without three equal consecutive bits, every interior defect is flanked by the opposite bit, and therefore occurs inside a factor \(baab\) with \(a\ne b\). This forces deficit at least four. If there are no interior defects but both endpoint adjacencies are defective, use five independent identifications among canonical histories. The first defect \(x_0=x_1\) forces the triple \((0,0),(0,1),(0,2)\) to produce one descendant, and forces \((0,3),(1,0)\) to produce another common descendant. The last defect \(x_{n-2}=x_{n-1}\) forces the triple \((n-2,n-2),(n-2,n-1),(n-2,n)\) to produce one descendant. These three sets of canonical history labels are disjoint for \(n\ge4\). Their identifications cost at least \(2+1+2=5\) output types, even if any resulting classes merge further. Thus every nonalternating source other than a solitary endpoint-defect word has at most \(M_n-4\) descendants.

**4. Exact witness enumeration, not finite extrapolation.** Let \(A_\ell(x)_t=x_t\oplus(t\bmod2)\) be bitwise exclusive-or with alternating parity. For every length-two palindromic duplication, direct inspection of the four-bit replacement shows
\[
A_{\ell+2}(T_i(x))=R_i(A_\ell(x)),
\]
where \(R_i\) replaces a block \(ab\) by \(ab\overline b\,\overline a\) (reverse-complement duplication). This bijection preserves every two-step sphere cardinality. A left-endpoint-defect source becomes, up to whole-word complement, \(z=0\,1^{n-1}\). Its reverse-complement descendants have the following *exhaustive, pairwise disjoint by zero count* forms (all displayed integer ranges are inclusive):

- Exactly three zeros: \(01010\,1^{n-1}\), and \(0\,1^a00\,1^{n+1-a}\) for \(2\le a\le n-1\). Count: \(n-1\).
- Exactly four zeros: \(010\,1^b00\,1^{n-1-b}\) for \(2\le b\le n-1\); \(0\,1^a0100\,1^{n-a-1}\) for \(2\le a\le n-1\); and \(0\,1^a0010\,1^{n-a-1}\) for \(2\le a\le n-2\). Count: \(3n-7\).
- Exactly five zeros: \(0\,1^a00\,1^b00\,1^c\) where \(a\ge2\), \(b,c\ge0\), and \(a+b+c=n-1\). Count: \(\binom{n-1}{2}\).

To check exhaustiveness, a duplicated block \(00,01,10,11\) inserts respectively \(11,01,10,00\), hence adds respectively \(0,1,1,2\) zeros. Start with one zero; only totals three, four and five can occur. The first operation either duplicates the unique initial mixed pair \(01\), or one of the pairs \(11\) to its right. For the second operation, the only mixed adjacencies are the initial boundary and the boundaries of any newly inserted zero-pair. Sorting these choices according to whether the insertion lies before, across or after a zero-pair produces exactly the three rows above. Their ranges express the availability of the relevant adjacent factor. The displayed words have distinct run positions within each row; direct substitution of the indicated duplication starts reaches every word.

For a right-endpoint-defect source the conjugate input is, up to complement, \(1^{n-1}0\). Its exact-three, exact-four and exact-five-zero descendants instead have the following forms:

- Three zeros: \(1^a00\,1^{n+1-a}0\) for \(2\le a\le n-1\); plus \(1^{n-1}00011\) and \(1^{n-1}01010\). Count: \(n\).
- Four zeros: \(1^a0010\,1^{n-a-1}0\) for \(2\le a\le n-2\); \(1^a00\,1^{n-a-1}010\) for \(2\le a\le n-1\); and \(1^a0100\,1^{n-a-1}0\) for \(2\le a\le n-1\). The first and second listed families meet in exactly one word, when \(a=n-2\), so the total is \(3n-8\).
- Five zeros: \(1^a00\,1^b00\,1^c0\) with \(a\ge2\), \(b,c\ge0\), and \(a+b+c=n-1\). Count: \(\binom{n-1}{2}\).

The same first- and second-operation split \(11\) versus \(10\), followed by copying \(00,01,10,11\), proves both exhaustion and reachability; the adjacent one-bit tail is retained in the templates. In each case the total equals
\[
(n-1)+(3n-7)+\binom{n-1}{2}=n+(3n-8)+\binom{n-1}{2}=\frac{n^2+5n-14}{2}=M_n-3.
\]
The two possible defective positions and two choices of initial bit yield exactly four distinct sources for \(n\ge4\). Together with Step 3, this establishes the sharp second-level theorem and its entire equality set. \(\square\)

## Verification

`verify_bruteforce.py` enumerates all binary sources of lengths \(4\) through \(12\), all first and second duplication positions, distinct outputs and both top layers. It separately checks the short local loss certificates. `verify_normal_form.py` constructs every right and left reverse-complement descendant directly, and independently generates the claimed run-template families for each \(4\le n\le60\); it compares the resulting sets and their zero-count profiles exactly. Both scripts use only the Python standard library and can be run from this package directory. Their finite verification supports the symbolic proof but does not replace its unbounded quantifiers.

## Relationship to prior work

Zabokritskiy [1, Sections 4 and 5.1] proved the even-length PAL/RC conjugacy and the sharp two-duplication maximum, and Section 5.2 gives an edge-tree structural history normal form. Those facts, including the two alternating maximizers, are prior work. A published maximum-level classification [2] likewise does not determine the strict runner-up. The new statement is precisely the sharp next-largest value, all four extremizers and separate left/right output-weight refinements; it is not implied by the previously known maximum formula or equality criterion. The known finite maximum-code-size tables [3] answer a different optimization problem.

## Limitations

The claim does not cover alphabet sizes greater than two, duplication lengths other than two, more than two operations or the exceptional lengths two and three. It establishes sphere-cardinality stability, not optimal correcting-code redundancy. The proof is mathematical and has been checked against independent exact calculations; no independent external audit has been performed. An equivalent unindexed theorem remains an originality risk.

## References

[1] A. L. Zabokritskiy (Yohananov), *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first posted 2026-09-01, https://arxiv.org/abs/2609.00779 ; consulted the available full text, including Sections 4–5.2.

[2] *All maximizers of two length-two palindromic duplication spheres*, public research record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-all-maximizers-of-two-length-two-palindromic-duplication-spheres--4e43b4f9127d .

[3] *Exact binary two-PAL2 code sizes through length eight*, public research record dated 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-mathrm-pal-2-code-sizes-through-length-eight--ba7c5d4a4968 .
