# Sharp Grundy-growth classification for two-state word-subtraction games

## Finding
Let \(\Sigma\) be any nonempty finite alphabet. A complete two-state DFA has states \(\{0,1\}\), starts at the rejecting state \(0\), and has \(\{1\}\) as its accepting set. Its accepted language \(S\subseteq\Sigma^+\) is the rule set of the normal-play suffix-subtraction game: from \(w\), remove any nonempty suffix in \(S\). Write \(G(w)\) for the Sprague–Grundy value and \(M(n)=\max_{w\in\Sigma^n}G(w)\). Classify each input letter according to its action on \(\{0,1\}\): \(Z=(0,0)\), \(I=(0,1)\), \(T=(1,0)\), or \(O=(1,1)\), listing images of states \(0\) and \(1\). Then for every \(n\ge1\), the **complete sharp length-\(n\) maximum law** is
\[
M(n)=\begin{cases}
n,&\text{if some letter has type }O,\\
\lceil n/2\rceil,&\text{if no }O\text{ occurs but both }Z,T\text{ occur},\\
1,&\text{if only }I,T\text{ occur and both occur},\\
n\bmod2,&\text{if every letter has type }T,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus the Grundy function is bounded over all words **if and only if** there is no type-\(O\) letter and types \(Z\) and \(T\) do not both occur; in every bounded case \(G(w)\le1\). In the mixed \(Z,T\) case the individual values also have an exact structure: partition \(w=u_0z_1u_1\cdots z_mu_m\) at all type-\(Z\) letters, so that each \(u_i\) uses only \(I,T\). Put \(\eta_i=1\) when \(u_i\) has any type-\(T\) letter and \(\eta_i=0\) otherwise, and put \(\rho_m\) equal to the parity of its number of type-\(T\) letters. Then
\[
G(w)=\rho_m\sum_{i=0}^{m}\eta_i.
\]
The empty word has Grundy value zero. A two-state DFA whose accepting set is empty also gives the identically zero game.

## Assumptions and scope
All transition maps are deterministic and total. The initial state is rejecting and the other state is accepting; neither minimality nor reachability is assumed. Every language \(S\subseteq\Sigma^+\) recognized by at most two states has such a presentation unless \(S\) is empty (which is already covered). Letter types may repeat, and the alphabet need not be binary. Moves strictly shorten words, so the Grundy recurrence is well-defined: \(G(\varepsilon)=0\) and \(G(w)=\operatorname{mex}\{G(u):w=us,\ s\in S\}\). The result concerns exactly this suffix-removal convention, not infix removal, misère play, or an unbounded number of DFA states.

## Proof
A two-element set has exactly four self-maps, so every input letter is of type \(Z,I,T\), or \(O\). There are no other cases.

If an \(O\)-letter \(o\) exists, all nonempty powers \(o^k\) belong to \(S\). Induction gives \(G(o^n)=n\): the \(n\) permitted suffix lengths lead to all \(o^j\) with \(0\le j<n\). Any length-\(n\) word has at most \(n\) distinct suffix-removal options, hence \(G(w)\le n\). This proves the first line sharply.

Assume no \(O\). If there is no \(T\), all letters fix state \(0\), so \(S=\varnothing\) and \(G\equiv0\). If there is a \(T\) but no \(Z\), the transition monoid consists of identity and swap. Consequently \(S\) consists exactly of words having an odd number of \(T\)-letters. By induction on length, \(G(w)\) equals the parity of that number: removing an accepted suffix toggles parity, so every option from an even-parity word has Grundy value one; every option from an odd-parity word has value zero, and the latter includes the option \(\varepsilon\). If \(I\) occurs, \(I^{n-1}T\) realizes one for every \(n\ge1\); if only \(T\) occurs, every word has parity \(n\bmod2\).

It remains to assume that \(Z,T\) both occur and \(O\) does not. Split a word at its type-\(Z\) letters as in the finding. Induct on word length to prove the displayed individual-value formula. A suffix beginning at or before the last \(Z\) is accepted precisely when the final segment has odd \(T\)-parity. A suffix lying entirely after the last \(Z\) is accepted precisely when its \(T\)-parity is odd. If the final segment has even parity, all accepted suffixes leave a prefix with odd \(T\)-parity in that same segment, hence positive Grundy value by induction; mex is zero. If the final segment has odd parity, every prefix ending at or before the last \(Z\) is an option (delete the suffix containing that \(Z\)), while every option from a suffix contained in the final segment has Grundy value zero. Let \(c\) be the number of earlier \(Z\)-separated segments containing a \(T\). The options ending before or at the last \(Z\) realize exactly the values \(0,1,\ldots,c\): zero comes from the empty prefix, and the first \(T\) in each previously nonempty-\(T\) segment realizes the next positive integer by induction. No such prefix has value exceeding \(c\). Thus the mex is \(c+1\), as claimed. When there is no \(Z\) in the word, the same parity argument as in the preceding paragraph gives value one or zero, agreeing with the formula. This completes the induction.

If \(G(w)=k>0\) in this last case, the word contains at least \(k\) distinct segments with a \(T\), requiring at least \(k\) type-\(T\) letters and \(k-1\) intervening type-\(Z\) letters. Hence \(|w|\ge2k-1\), so \(k\le\lceil |w|/2\rceil\). This is sharp: for odd \(n=2k-1\) the word \(T(ZT)^{k-1}\), and for even \(n=2k\) the word \(ZT(ZT)^{k-1}\), both have Grundy number \(k\). Here type symbols denote any fixed letters realizing the corresponding maps.

## Verification
The included standalone `checker_types.py` enumerates all \(4^3=64\) ternary assignments of transition types and every input through length eight, directly computing the mex over all accepted suffixes and checking the closed formulas. The independent `checker_table.cpp` enumerates all \(4^2=16\) binary assignments through length sixteen using integer-coded words and checks both the pointwise formulas (when no \(O\) occurs) and the sharp maximum law. Their respective successful runs covered 629,760 and 2,097,120 nonempty words, counting repeats across transition assignments. These finite checks are regression evidence only: the all-length theorem follows from the preceding induction and sharp witnesses.

Run `python3 checker_types.py`; independently compile with `g++ -O2 -std=c++17 checker_table.cpp -o checker_table` and run `./checker_table`.

## Relationship to prior work
Inoue and Inazu, *Word Subtraction Games* (arXiv:2611.09157v1, first public November 6, 2026), establish regularity of each fixed-Grundy-value fiber when the subtraction language is regular (Section 3) and explicitly ask when the whole Grundy function is bounded (Section 7). Neither this fiberwise result nor the general construction supplies the exact two-state criterion, all-length maxima or mixed reset/swap run formula shown here. Takata, Inoue and Seki (arXiv:2609.00871, September 2026) study Grundy computation for a related right-linear-grammar derivation-game model, including general decision-complexity results; that does not state this suffix-removal two-state classification. Hetyei (arXiv:0912.0573, 2009) treats winning strategies for a class of word truncation games; no claim is made here about all his possible unpublished or inaccessible extensions. The general Sprague–Grundy mex rule and DFA transition-map enumeration are standard inputs, not novel claims.

## Limitations
This theorem covers only DFA rule languages representable with at most two states, with normal-play right-suffix deletion. It does not solve boundedness for general regular subtraction sets, nor provide a pointwise formula when a type-\(O\) letter occurs. Same-source literature inspection identifies no explicit duplicate theorem, but unpublished or unindexed equivalents cannot be excluded. Finite checker agreement is not a substitute for the symbolic induction, and no independent review has been performed.

## References
1. Y. Inoue and H. Inazu, *Word Subtraction Games*, arXiv:2611.09157v1 (November 6, 2026), https://arxiv.org/abs/2611.09157.
2. Y. Takata, Y. Inoue and H. Seki, *Construction of a DFA for Computing Grundy Numbers in the Successful Derivation Games on Right-Linear Grammars*, arXiv:2609.00871 (September 1, 2026), https://arxiv.org/abs/2609.00871.
3. G. Hetyei, *Enumeration by kernel positions for strongly Bernoulli type truncation games on words*, arXiv:0912.0573 (December 3, 2009), https://arxiv.org/abs/0912.0573.
