# Complete antidictionary and sharp prefix cutoff for the triangular-marker word

## Finding

Let \(\mathbf{t}=\prod_{j\ge1}(1\,0^j)=101001000100001\cdots\), where the product denotes concatenation over increasing integers \(j\). For a right-infinite binary word, a **minimal absent factor** is a nonempty finite binary word absent as a contiguous factor but with every proper factor present. The complete minimal-absent-factor language of \(\mathbf{t}\) is

\[
\mathcal M(\mathbf t)=\{11\}\;\sqcup\;\{0^a1\,0^a1:a\ge1\}\;\sqcup\;\{1\,0^a1\,0^{a+2}:a\ge1\}.
\]

The unions are disjoint. Thus all minimal absent factors have at most two ones, and their length generating function is

\[
\sum_{v\in\mathcal M(\mathbf t)}z^{|v|}
=z^2+\frac{z^4}{1-z^2}+\frac{z^6}{1-z^2}
=\frac{z^2+z^6}{1-z^2}.
\]

Exactly one minimal absent factor has length \(2\), exactly one has length \(4\), exactly two have every even length at least \(6\), and none have odd length. The language is deterministic context-free but not regular.

For each integer \(N\ge1\), the *shortest prefix* of \(\mathbf t\) that contains every infinite-word factor of length at most \(N\) has length exactly

\[
L(N)=\frac{N(N+3)}2.
\]

Equivalently, the minimal absent factors of a finite prefix through length \(N\) agree exactly with those of \(\mathbf t\) if and only if that prefix has length at least \(L(N)\). This gives a sharp finite certificate for the entire infinite antidictionary up to any prescribed length.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), positions and prefix lengths are counted in ordinary units, and \(0^a\) denotes \(a\) consecutive zeros, including the empty block for \(a=0\). There are no implicit cyclic factors or scattered subsequences. The word starts with \(1\), with one, two, three, and so on zeros between consecutive ones. All claims quantify over every positive integer \(N\), and the language families quantify over every positive integer \(a\). For finite prefixes, minimal absence is relative to the same fixed binary alphabet; the empty word is always present.

## Proof

**The unique-gap principle.** Index the ones from \(1\). The gap of zeros after the \(a\)-th one has exactly \(a\) zeros. Hence \(1\,0^a1\), for any \(a\ge1\), occurs exactly once, beginning at the \(a\)-th one. A factor with at least two ones therefore occurs at most once: its first consecutive pair of ones determines its position. For a factor containing exactly two ones in the form \(0^\ell1\,0^a1\,0^r\) with \(a\ge1\), occurrence is equivalent to the two inequalities

\[
0\le\ell\le a-1,\qquad 0\le r\le a+1.
\]

The first bound is the preceding run of zeros (zero before the first one when \(a=1\)); the second is the following run of zeros.

**No minimal absence with fewer than two ones.** Every \(0^m\) occurs because zero runs grow without bound. Likewise every \(0^\ell1\,0^r\) occurs by choosing a one sufficiently far along that both neighboring zero runs accommodate the requested margins. An absent two-one word with zero zeros between its ones contains the absent proper factor `11`, unless it is exactly `11`, which is minimal absent.

**No minimal absence with at least three ones.** Suppose a minimal absent word \(v\) contains at least three ones. Both the prefix of length \(|v|-1\) and suffix of length \(|v|-1\) occur. If their common length-\(|v|-2\) overlap contains at least two ones, the unique-gap principle forces these two occurrences to align at the same place; this would realize \(v\), contradiction. Therefore \(v\) must start and end with a one and contain exactly three ones, of the form \(1\,0^a1\,0^b1\) with \(a,b\ge1\). Its prefix \(1\,0^a1\,0^b\) can occur only if \(b\le a+1\). Its suffix \(0^a1\,0^b1\) can occur only if \(a\le b-1\). Both conditions force \(b=a+1\), in which case the whole triple occurs. Contradiction.

**The two families.** An absent two-one word \(0^\ell1\,0^a1\,0^r\) has \(a\ge1\) and violates at least one unique-gap inequality. If \(\ell\ge a\), minimality forces \(\ell=a\) and \(r=0\): otherwise deleting the first or last symbol retains a two-one absence. This yields \(0^a1\,0^a1\), whose immediate prefix and suffix do occur. If \(r\ge a+2\), minimality likewise forces \(r=a+2\) and \(\ell=0\), yielding \(1\,0^a1\,0^{a+2}\), again with both immediate proper factors occurring. All larger violations are nonminimal. Along with `11`, these give exactly the stated language.

**Enumeration and language class.** The two parametric families have lengths \(2a+2\) and \(2a+4\), respectively. Summing geometric series gives the displayed rational generating function. Intersecting \(\mathcal M(\mathbf t)\) with the regular language \(0^+10^+1\) gives \(\{0^a1\,0^a1:a\ge1\}\), which is not regular by Myhill–Nerode: prefixes with distinct first zero-run lengths are distinguished by a matching final run. Thus \(\mathcal M(\mathbf t)\) is not regular. It is deterministic context-free: the first symbol selects one of the two parametric families (or the isolated word `11`), and a deterministic one-counter pushdown compares the two zero-run lengths, allowing exact equality in the first family and an offset of two in the second.

**Sharp finite-prefix cutoff.** Let \(T_N=N(N+1)/2\). The first occurrence of \(0^N\) starts at zero-based position \(T_N\): it is in the first zero run of length \(N\). Therefore any prefix containing all length-\(N\) factors has length at least \(T_N+N=L(N)\). Conversely, all factors with at most one one occur by the end of the length-\(N\) zero run, since the one just preceding it has at least \(N-1\) preceding zeros. For a length-\(N\) factor containing at least two ones, its first consecutive ones have a gap \(a\le N-2\); its unique occurrence starts no later than the \(a\)-th one, and ends no later than \(N-1\) positions after that one. Hence its occurrence ends strictly before the endpoint \(L(N)\). So all factors of length \(N\), and therefore all shorter factors, occur in the length-\(L(N)\) prefix. Finally, two factorial languages over the same fixed alphabet have identical minimal absent words through length \(N\) exactly when their factor sets agree through length \(N\): any missing factor of least length produces a false minimal absent word. This proves the equivalence and sharpness.

## Verification

The standalone Python 3 script `verify_triangle.py` constructs explicit finite prefixes and performs independently generated factor-set and minimal-absence comparisons against the formulas at every length \(1\le n\le26\). It also checks that the cutoff prefix contains every length-\(n\) factor, and that shortening it by one symbol loses a factor, at every such length. It checks the complete minimal-absence list for all lengths up to the cutoff at each test radius. Run `python3 verify_triangle.py` from the same directory. Successful execution prints `CHECK_OK`. All checks use only the Python standard library. These finite checks supplement and do not replace the proof for arbitrary lengths.

## Relationship to prior work

Akagi, Okabe, Mieno, Nakashima and Inenaga (arXiv:2202.13591, first publicly posted 2022-02-28) give compressed algorithms and a five-class analysis of minimal absent words of **finite** run-length encoded strings. Their statements do not furnish the infinite triangular-marker antidictionary, the two explicit parametric families, its formal-language classification, or the sharp convergence threshold.

Gheorghiciuc (arXiv:math/0512256, first posted 2005-12-13) gives a general exact **factor complexity** formula for words with strictly increasing marker gaps. In particular, the familiar factor-complexity identity \(p_{\mathbf t}(n)=\lfloor(n+1)^2/4\rfloor+1\) follows from that work and is not claimed here as new. Factor counts alone do not determine which specific finite words are minimally absent. General finite-word minimal forbidden-word and automaton methods (Crochemore–Mignosi–Restivo, 1998) also do not explicitly settle the infinite language or finite-prefix threshold here.

## Limitations

The claim is specialized to the specified triangular-marker word; it does not assert a corresponding formula for arbitrary growing gap sequences. It does not furnish a new factor-complexity theorem. The checked published record and research index may omit an equivalent earlier antidictionary derivation. The finite verifier tests lengths only through \(26\); all-length validity rests on the arguments above, not on enumeration. No independent scientific audit has been performed.

## References

1. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima and S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (first version 2022-02-28); CPM 2022, DOI: 10.4230/LIPIcs.CPM.2022.27. https://arxiv.org/abs/2202.13591
2. I. Gheorghiciuc, *The subword complexity of a class of infinite binary words*, arXiv:math/0512256 (first version 2005-12-13). https://arxiv.org/abs/math/0512256
3. M. Crochemore, F. Mignosi and A. Restivo, *Automata and forbidden words*, Information Processing Letters 67 (1998), 111–117. https://doi.org/10.1016/S0020-0190(98)00097-2
