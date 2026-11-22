# Exact bounded-rotation reset threshold for even Černý automata

## Finding
For every integer \(m\ge2\), put \(n=2m\) and let \(C_n\) be the deterministic automaton with states \(Q=\{0,1,\ldots,n-1\}\) and input letters
\[
a(i)=i+1\pmod n,\qquad b(i)=\begin{cases}0&i=n-1,\\i&0\le i<n-1.\end{cases}
\]
Among all words \(w\in\{a,b\}^*\) that send every state to the same state and contain **no contiguous occurrence of \(aaa\)**, the shortest length is exactly
\[
\boxed{\tau(2m)=6m^2-8m+3.}
\]
Relative to the unrestricted Černý reset length \((2m-1)^2\), forbidding three consecutive rotations imposes the exact penalty \(2(m-1)^2\). In particular the constrained/unconstrained ratio tends to \(3/2\). The theorem makes no claim for odd state counts.

## Assumptions and scope
Words are read left to right, acting on image subsets. The restriction concerns **consecutive occurrences of the rotation letter \(a\)**, not the number of rotations overall, the other letter, or transitions in the state graph. The initial image is all of \(Q\) and the terminal singleton is not prescribed. Every transition is total. State labels are fixed and no word equivalence or relabeling quotient is used.

## Proof
**Lower bound from trajectories.** Let \(w\) be any reset word and let \(A\) be its total number of \(a\)-letters. For each starting state \(i\), let \(B_i\) count those occurrences of \(b\) when this particular trajectory is at state \(n-1\); these are the \(b\)-letters that advance this trajectory from \(n-1\) to \(0\). Every other \(b\) fixes that trajectory. If all trajectories finish at \(r\), then
\[
r\equiv i+A+B_i\pmod n.
\]
Thus the residues of \(B_i\) for the \(n\) starting states are pairwise distinct, and some trajectory has \(B_i\ge n-1\). Select its first \(n-1\) advancing \(b\)-letters. Between two such letters the trajectory travels from \(0\) to \(n-1\), requiring at least \(n-1=2m-1\) occurrences of \(a\); other \(b\)-letters do not advance this trajectory. There are \(n-2\) intervening segments, hence \(w\) contains at least \((n-2)(n-1)\) rotations.

Each of these intervening segments includes at least \(2m-1\) rotations, and the restriction that no run of rotations exceeds two forces at least \(m-1\) *additional* \(b\)-letters between the two selected advancing \(b\)-letters. These disjoint segments therefore contain at least \((n-2)(m-1)\) additional \(b\)-letters, besides the selected \(n-1\). Consequently
\[
|w|\ge(n-2)(n-1)+(n-1)+(n-2)(m-1)
=(2m-1)^2+2(m-1)^2=6m^2-8m+3.
\]
This argument counts actual letters and requires no assumed normal form for an optimal word.

**Constructive attainment.** Let \(T(S)=b(a^2(S))\) and \(U(S)=b(a(S))\), with function composition in reading order. Start with one \(b\). Define \(n-2=2m-2\) subsequent blocks, each ending in \(b\), as follows. For odd block number \(j=2r-1\), use
\[
P_{2r-1}=(a^2b)^{m-1}ab.
\]
For even block number \(j=2r\), use
\[
P_{2r}=(a^2b)^{r-1}ab(a^2b)^{m-r}.
\]
The explicit reset word is
\[
W_{2m}=bP_1P_2\cdots P_{2m-2}.
\]
Each block has exactly \(2m-1\) rotations and \(m\) occurrences of \(b\). Every rotation run has length one or two, and the blocks end in \(b\), so \(aaa\) never occurs. Its total length is \(1+(2m-2)((2m-1)+m)=6m^2-8m+3\).

It remains to verify that the word really resets for **every** \(m\). Put
\[
E_r=\{0,2,4,\ldots,2m-2r-2\}\quad(1\le r\le m-1),
\]
\[
O_r=\{0\}\cup\{1,3,5,\ldots,2m-2r-1\}\quad(1\le r\le m-1).
\]
After the initial \(b\) the image is \(Q\setminus\{2m-1\}\). Applying \(T\) successively \(m-1\) times leaves exactly the even residues \(\{0,2,\ldots,2m-2\}\): after \(k\) such applications the missing states are \(\{1,3,\ldots,2k-1,2m-1\}\). One subsequent \(U\) produces \(O_1\), establishing the first odd block.

For \(2\le r\le m-1\), starting at \(E_{r-1}\), \(T^{m-1}\) rotates this even set backward two places, giving \(\{2m-2,0,2,\ldots,2m-2r-2\}\). Then \(U\) maps \(2m-2\) to \(0\), and every other even element to the following odd element, producing exactly \(O_r\). Thus every odd block has the stated target image.

Starting at \(O_r\), apply \(T^{r-1}\). The set becomes
\[
\{2r-2\}\cup\{2r-1,2r+1,\ldots,2m-3\}.
\]
The following \(U\) gives \(\{2r-1\}\cup\{2r,2r+2,\ldots,2m-2\}\). The final \(T^{m-r}\) rotates the even portion to \(E_r\), while carrying its one odd element to \(2m-1\), which the final \(b\) sends to the already occupied state \(0\). Hence the image after even block \(2r\) is precisely \(E_r\).

The images therefore alternate \(O_1,E_1,O_2,E_2,\ldots,O_{m-1},E_{m-1}\). Since \(E_{m-1}=\{0\}\), \(W_{2m}\) resets. The upper construction and the trajectory lower bound agree, proving the formula.

## Verification
The accompanying dependency-free `verify.py` constructs the explicit word for every even state count from \(4\) through \(100\), verifies the claimed image after every block, the final singleton, absence of \(aaa\), and exact length. Independently, an exact breadth-first search in the product of image subsets and current rotation-run length confirms the minimum for every even size from \(4\) through \(16\). Run `python3 verify.py`; the observed output is `VERIFY_OK even n=4..100, independent exact BFS n=4..16`. The finite checks corroborate, but do not replace, the all-even-state proof.

## Relationship to prior work
The classical unrestricted \((n-1)^2\) threshold is not new. Kisielewicz, Kowalski and Szykuła (online 2013) describe algorithms for shortest reset words without this input-language restriction. The published mandatory-scattered-subsequence result for Černý automata independently yields a compatible rotation-count lower bound, but not an attainable \(aaa\)-avoiding construction or the constrained sharp threshold. Hoffmann (2021), Section 4, studies *decision complexity* of constrained synchronization for automata with simple idempotents (including the Černý family), not this exact shortest length. Related published exact rank-compression results impose no forbidden command factor. The contribution here is the sharp **all-even-state** resource-restricted length together with a uniform explicit witness and image-set proof, not a new unrestricted result.

## Limitations
No formula for odd state counts, for other maximal rotation-run lengths, or for the number of shortest constrained words is asserted. Searches and close-source inspections cannot completely exclude older equivalent terminology; external independent review remains unperformed. The underlying automaton is exactly the standard two-letter Černý family, not arbitrary synchronizing automata.

## References
1. A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the shortest reset words of synchronizing automata*, first online 17 November 2013, https://doi.org/10.1007/s10878-013-9682-0 .
2. S. Hoffmann, *Constrained Synchronization for Commutative Automata and Automata with Simple Idempotents*, arXiv:2109.02743, initial posting 6 September 2021, https://arxiv.org/abs/2109.02743 .
3. *A mandatory reset subsequence and exact one-step multiplicity for the Černý automata*, published 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-a-mandatory-reset-subsequence-and-exact-one-step-multiplicity-fo--8a725fd1702c/RESULT.md .
4. *Uniform weighted-reset optimality in the Černý automata*, published 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-uniform-weighted-reset-optimality-in-the-ern-automata--6527a70965c4/RESULT.md .
5. *Exact first post-half rank compression in the even Černý automata*, published 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-first-post-half-rank-compression-in-the-even-ern-automata--7debf3d5fc46/RESULT.md .
