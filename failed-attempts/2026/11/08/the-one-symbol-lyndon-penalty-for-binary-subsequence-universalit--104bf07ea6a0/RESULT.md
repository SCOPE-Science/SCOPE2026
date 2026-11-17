# The one-symbol Lyndon penalty for binary subsequence universality

## Finding

Fix the ordered alphabet \(0<1\). For each integer \(k\ge1\), let \(\ell_{\rm L}(k)\) denote the minimum length of a Lyndon word containing **every** binary word of length \(k\) as a scattered subsequence, and let \(\mathcal E_k\) be the set of all minimizers. Then

\[
\ell_{\rm L}(1)=2,\qquad \mathcal E_1=\{01\},
\]

and for **every** \(k\ge2\),

\[
\boxed{\ell_{\rm L}(k)=2k+1},\qquad
\boxed{\mathcal E_k=\{001(01)^{k-1},\;(01)^k1\}}.
\]

In particular, the Lyndon requirement costs exactly one symbol beyond the unconstrained optimum \(2k\) for every \(k\ge2\), and leaves exactly two extremal words. These are literal binary strings; the exponent on a parenthesized word means repetition.

## Assumptions and scope

A scattered subsequence of \(w=w_1\cdots w_n\) is \(w_{i_1}\cdots w_{i_t}\) with \(1\le i_1<\cdots<i_t\le n\). The word \(w\) is \(k\)-universal over the **fixed ambient alphabet** \(\{0,1\}\) when every member of \(\{0,1\}^k\) is a scattered subsequence. A Lyndon word means a finite nonempty word strictly lexicographically smaller than **all** its nontrivial cyclic rotations under \(0<1\), equivalently strictly smaller than each nonempty proper suffix. All quantifiers above range over every integer \(k\) in the indicated domain; the empty word is excluded. No hypothesis of circular universality is imposed.

## Proof

**Greedy arch lemma.** Scan a word from left to right and close an arch immediately when both letters have been observed since the preceding closure. This yields \(w=A_1\cdots A_rR\), with each \(A_i\) the shortest full-alphabet prefix of the remaining word and with the residual \(R\) missing at least one letter. The index of scattered-subsequence universality is exactly \(r\). For the lower bound, select the prescribed \(i\)-th target letter inside \(A_i\), independently for every \(1\le i\le r\). For the upper bound, let \(c_i\) be the last (new) letter of \(A_i\) and let \(c_{r+1}\) be a letter absent from \(R\). Any embedding of \(c_1\cdots c_{r+1}\) would have to select \(c_i\) at or after the end of \(A_i\), by induction on \(i\), and therefore could not select its final letter in \(R\). Thus \(c_1\cdots c_{r+1}\) is absent. Every arch has length at least two; a length-two arch is exactly \(01\) or \(10\).

**Unconstrained length and the Lyndon obstruction.** Since a \(k\)-universal word needs at least \(k\) copies of each symbol (to contain the all-zero and all-one length-\(k\) words), it has length at least \(2k\). At length \(2k\), the greedy lemma forces exactly \(k\) length-two arches and no residual: \(w\in\{01,10\}^k\). A binary Lyndon word containing both letters starts with \(0\) and ends with \(1\). The latter follows because a word ending with \(0\) has the one-letter proper suffix \(0\), which is lexicographically smaller than the whole word beginning with \(0\). Thus the first arch is \(01\). If a factor \(00\) appeared anywhere, the rotation beginning at that factor would be lexicographically smaller than \(w\), which begins \(01\). Hence no \(00\) appears. A word starting in \(0\), ending in \(1\), having \(k\) of each letter and no \(00\) is necessarily \((01)^k\); for \(k\ge2\) this is periodic and not Lyndon. Thus no such length-\(2k\) word exists when \(k\ge2\).

**Classification at length \(2k+1\).** Fix \(k\ge2\) and a \(k\)-universal Lyndon word \(w\) of length \(2k+1\). It starts in \(0\) and ends in \(1\). If it has no factor \(00\), its \(k\) required zeros must be separated and followed by at least \(k\) ones. There is room for precisely one additional \(1\). Consequently there is exactly one doubled-one gap, and

\[
w=(01)^{j-1}011(01)^{k-j}\quad\text{for some }1\le j\le k.
\]

If \(j<k\), the rotation beginning at the first \(0\) after the unique \(11\) starts with \((01)^{k-1}011\). It is strictly smaller than \(w\), since its alternating prefix continues past the location of \(w\)'s doubled \(1\). Thus \(j=k\), yielding \((01)^k1\).

Otherwise \(w\) contains \(00\). Because \(w\) is Lyndon, it must begin \(00\): otherwise a rotation at the \(00\) would be smaller than its \(01\)-starting form. The greedy arch lemma and length \(2k+1\) force the **entire** decomposition

\[
w=001P_2P_3\cdots P_k,\qquad P_i\in\{01,10\},
\]

with no residual and with \(P_k=01\), because \(w\) ends in \(1\). Suppose some \(P_i=10\). Let \(j\) be the *last* index with \(P_j=10\) and \(P_{j+1}=01\). Such an index exists because \(P_k=01\), and by maximality every \(P_{j+1},\ldots,P_k\) equals \(01\). Put \(t=k-j-1\). Rotating at the terminal \(0\) of \(P_j\) produces a word beginning

\[
001(01)^t00\cdots.
\]

Let \(r\) be the number of initial \(01\) blocks among \(P_2,\ldots,P_k\) before the first \(10\) block. The original \(w\) begins \(001(01)^r10\cdots\). If \(t\le r\), the new rotation has \(00\) where \(w\) has \(01\) or \(10\); if \(t>r\), it has \(01\) where \(w\) has \(10\). Either way the rotation is smaller, a contradiction. Therefore all \(P_i=01\), yielding \(001(01)^{k-1}\).

**Attainment and exactness.** Both displayed words of length \(2k+1\) are \(k\)-universal by their evident greedy arches: \(001\) followed by \(k-1\) copies of \(01\), or \(k\) copies of \(01\) followed by the residual \(1\). The first word has a unique cyclic occurrence of \(00\), at its beginning, so its rotation is strictly minimal; the second has its unique \(11\) at the end, so its initial \(0\) gives a longer strictly alternating prefix than any later cyclic occurrence of \(0\). Rotations beginning in \(1\) are also greater. Both words are Lyndon. The exhaustive two-case argument rules out any other length-\(2k+1\) word. For \(k=1\), the length-two Lyndon word \(01\) is universal and unique. This completes the proof.

## Verification

The accompanying standalone `verify.py` independently implements greedy arch counting, literal cyclic-rotation comparison, and, for small parameters, a separate explicit subsequence test. Its successful execution exhaustively scans all binary words at lengths \(2k\) and \(2k+1\) for \(1\le k\le8\) (262,140 words), cross-checks 2,728 length-\(2k+1\) words against the literal subsequence definition for \(k\le5\), and tests the two prescribed witnesses for \(2\le k\le100\). These checks are finite diagnostics and do not replace the all-\(k\) proof above.

## Relationship to prior work

Barker et al. (2020) establish the combinatorial arch theory for scattered-factor universality. Adamson (2023) provides general counting/ranking algorithms for universal words. The present result combines these objects with the **fixed-order Lyndon minimum-rotation constraint** and gives a sharp closed all-index threshold and an explicit classification of every shortest witness; the generic counting methods do not themselves state that classification. Fleischmann et al. (2022) study *nearly* universal words and Simon congruence, but not this Lyndon extremum. Bannai et al. (2022) compute a longest *Lyndon subsequence of an arbitrary input*, which is a different question. Carpi et al. (2014) use the term “universal Lyndon word” for a different notion involving alphabet orders and rotations; no equivalence is claimed. Published equivalent results may still exist outside the inspected sources.

## Limitations

The classification is for the ordered binary alphabet only; it is not asserted for alphabets of size three or more, arbitrary word lengths above the optimum, or variable alphabet orders. In fact `012021` is a length-six 2-universal ternary Lyndon word, demonstrating that the binary one-letter obstruction does not extend automatically. Finite tests do not certify novelty or the infinite theorem; those rest respectively on incomplete literature coverage and the explicit mathematical proof. No independent scientific audit has been performed.

## References

- Barker, Fleischmann, Harwardt, Manea, Nowotka, *Scattered Factor-Universality of Words* (first public 2020-03-10), https://arxiv.org/abs/2003.04629.
- Adamson, *Ranking and Unranking k-subsequence universal words* (first public 2023-04-10), https://arxiv.org/abs/2304.04583.
- Fleischmann, Haschke, Huch, Mayrock, Nowotka, *m-Nearly k-Universal Words -- Investigating Simon Congruence* (first public 2022-02-16), https://arxiv.org/abs/2202.07981.
- Bannai, I, Kociumaka, Köppl, Puglisi, *Computing Longest (Common) Lyndon Subsequences* (first public 2022-01-18), https://arxiv.org/abs/2201.06773.
- Carpi, Fici, Holub, Oprsal, Sciortino, *Universal Lyndon Words* (first public 2014-06-23; supporting terminology comparison), https://arxiv.org/abs/1406.5895.
