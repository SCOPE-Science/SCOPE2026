# Exact greedy string attractor of the powers-of-two characteristic word

## Finding

Let \(p=p(0)p(1)\cdots\) be the binary word whose ones occur precisely at indices \(2^j-1\) for integers \(j\ge0\), or equivalently
\[
p(i)=\begin{cases}1,&i+1=2^j\text{ for some }j\ge0,\\0,&\text{otherwise}.\end{cases}
\]
Its beginning is \(1101000100000001\cdots\). For a finite word \(u\), a *string attractor* is a set of letter positions such that every nonempty factor of \(u\) has at least one occurrence containing a selected position. Start with no positions, scan prefixes in increasing order, and select a new position precisely when the previously selected positions fail to attract the new prefix.

**Theorem.** The resulting infinite greedy set is precisely
\[
\boxed{G=\{0\}\cup\{3\cdot 2^k-1:k\in\mathbb Z_{\ge0}\}.}
\]
Thus its initial positions are \(0,2,5,11,23,47,95,\ldots\). For the prefix of length \(N\ge1\), the exact number \(g(N)\) of greedy positions is
\[
\boxed{g(N)=\begin{cases}1,&1\le N\le2,\\2+\lfloor\log_2(N/3)\rfloor,&N\ge3.\end{cases}}
\]
In particular \(g(N)/\log_2N\to1\). The claim concerns the specified greedy online rule; it does not identify the minimum possible attractor or its cardinality.

## Assumptions and scope

All word indices are zero-based. The prefix \(p[0..j]\) has \(j+1\) letters and includes both endpoints. A factor is a nonempty contiguous word, not a subsequence. A factor \(v\) is *attracted* by \(S\) in a prefix if at least one occurrence of \(v\) in that prefix contains a position in \(S\).

Starting with \(S=\varnothing\), the canonical greedy rule selects the least nonnegative index \(j\) for which \(S\) does not attract \(p[0..j]\), and repeats. This agrees with the original greedy-attractor definition of Schaeffer and Shallit. As the input grows, no previously selected position is deleted. The indicator word is \(2\)-automatic because its one-positions are precisely the nonnegative indices with binary representations belonging to the regular language consisting of the single representation \(0\) and nonempty strings of ones.

## Proof

**1. The first two selections.** The one-letter prefix \(p[0]=1\) forces selection of index \(0\). The prefix \(p[0..1]=11\) is still attracted by \(\{0\}\). At index \(2\), the prefix ends in the first zero, so the factor \(0\) has no occurrence crossing the selected index \(0\); the next selection is \(2\). Hence the first two marks are \(0,2\).

**2. No selection between successive proposed marks.** Fix an integer \(k\ge0\), put \(a=2^k\), and suppose the latest greedy position is \(h=3a-1\). We prove that no new mark is needed at any index \(j\) satisfying \(3a\le j<6a-1\). The next one after index \(h\) occurs at \(4a-1\), so the segment \(p[3a..j]\) is either entirely zeros (when \(j<4a-1\)) or has the form
\[
0^{a-1}1\,0^{j-4a+1}
\]
(when \(4a-1\le j<6a-1\)). In the first case this segment occurs earlier, starting at index \(a\), inside the zero run between the ones at \(a-1\) and \(2a-1\). In the second case the entire segment likewise occurs earlier, starting at index \(a\), as
\[
p[3a..j]=p[a..j-2a].
\]
The latter occurrence is well-defined: it contains the one at \(2a-1\) and ends before the next one at \(4a-1\). In both cases the prior occurrence ends at an index strictly smaller than \(j\).

For completeness, let \(S\) be the already selected positions, and assume that \(S\) attracts the prefix ending at index \(j-1\). Any factor newly appearing when position \(j\) is appended must end at \(j\). An occurrence of such a factor either crosses the existing last mark \(h\) (and is then already attracted) or lies wholly in \(p[h+1..j]=p[3a..j]\). The latter segment has an earlier occurrence, so the factor also occurs in the preceding prefix and therefore has an occurrence crossing \(S\) by the induction hypothesis. Thus \(S\) still attracts the prefix ending at \(j\). Induction in \(j\) excludes every position strictly between \(h\) and \(6a-1\).

**3. A forced new selection at the next proposed mark.** At index \(6a-1\), the suffix beginning at \(4a\) is exactly \(0^{2a}\). This is the first occurrence of \(2a\) consecutive zeros in the word: up to that point, each completed zero run between consecutive powers of two has length strictly less than \(2a\), and the current final zero run first reaches length \(2a\) at this endpoint. All previously selected positions are at most \(h=3a-1<4a\), whereas the unique occurrence of \(0^{2a}\) in this prefix occupies \([4a,6a-1]\). Therefore the previously selected positions do not attract this factor and index \(6a-1\) must be added.

Starting from \(h=2=3\cdot1-1\) and applying steps 2–3 inductively with \(a=1,2,4,\ldots\), the selected indices are exactly \(0,2,5,11,23,\ldots\), as asserted. There are \(1+\lfloor\log_2(N/3)\rfloor\) members of the geometric family strictly below \(N\) when \(N\ge3\). Adding index \(0\) gives the displayed cardinality formula and its logarithmic limit. \(\square\)

## Verification

The included standard-library Python file `verify.py` independently checks the attractor definition for all \(128\) initial prefixes by enumerating every distinct factor and each occurrence crossing a selected position. A separate novel-suffix implementation checks all \(800\) initial prefixes. Exact indexwise comparisons of the earlier-occurrence identities and first long-zero runs are performed at \(13\) dyadic scales; the script reports \(24{,}573\) explicit gap checks. Run `python3 verify.py`. These computations are finite diagnostics; the argument in the Proof section establishes the unrestricted infinite statement.

## Relationship to prior work

Schaeffer and Shallit (2020, subsequently revised) introduced the canonical greedy string attractor (their Definition 19) and considered **this same characteristic powers-of-two word** in the context of offline attractors, giving explicit feasible sets and logarithmic bounds (Section 6). Their generic greedy theorem bounds the count asymptotically, but does not specify the greedy positions for this word. The present statement fixes the online canonical rule and gives all selected indices and exact prefix costs; no optimal offline cardinality is asserted.

Whittington (2024) established that the online lazy/greedy rule is equivalent to a self-referencing novel Lempel–Ziv parsing. Thus the theorem also specifies the resulting phrase-end positions for this precise variant, but general equivalence does not imply their arithmetic values for this word. Cassaigne and collaborators' 2024 study addresses other attractor complexities, including logarithmic optimal-profile behavior for the powers-of-two indicator. Béal, Crochemore, and Romana (2025/2026) study a *different*, backward-looking greedy attractor algorithm and tabulate its behavior on this indicator word. Those data do not determine this canonical online sequence. A related result on greedy indices for the **period-doubling word** concerns a different automatic word.

## Limitations

No independence or exhaustive bibliographic uniqueness is claimed. The possibility of an unindexed equivalent characterization, including one phrased in terms of Lempel–Ziv phrase boundaries, remains. The proof treats the indicated one-sided word and the specified online rule only; it does not determine smallest offline attractors, other attractor heuristics, different sparse supports, or finite-word terminal-phrase conventions beyond the prefix positions established here. The finite checker is not an infinite verification.

## References

1. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (first public 2020-12-12), Section 6 and Definition 19 in Section 9. https://arxiv.org/abs/2012.06840
2. P. Whittington, *Online String Attractors*, arXiv:2407.15599 (first public 2024-07-22), Sections 2–4, especially Theorem 3.4. https://arxiv.org/abs/2407.15599
3. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino, and M. Stipulanti, *New string attractor-based complexities for infinite words*, JCTA 208 (2024), 105936; open author preprint available from 2023-12-11. https://orbi.uliege.be/handle/2268/309672
4. M.-P. Béal, M. Crochemore, and G. Romana, *Checking and producing word attractors*, arXiv:2509.08503 (first public 2025-09-10), Sections 4–5 and Table 2. https://arxiv.org/abs/2509.08503
5. S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248. https://ceur-ws.org/Vol-2504/paper8.pdf
