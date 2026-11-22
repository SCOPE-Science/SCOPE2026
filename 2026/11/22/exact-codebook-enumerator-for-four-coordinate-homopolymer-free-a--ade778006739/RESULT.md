# Exact codebook enumerator for four-coordinate homopolymer-free adjacent-swap codes

## Finding
For any integer \(q\ge 2\), let \(\Sigma\) be a labeled alphabet of size \(q\). Let \(X_q\) be the four-coordinate words \(w=w_1w_2w_3w_4\in\Sigma^4\) with \(w_i\ne w_{i+1}\) for \(i=1,2,3\). A channel use either leaves the source unchanged or exchanges exactly one adjacent pair of coordinates; the received word need not be homopolymer-free. A code is a set of sources with pairwise disjoint full output sets, including unchanged outputs. Write \(Z_q(t)=\sum_C t^{|C|}\) with the sum over every such **labeled, unordered codebook**, including the empty codebook. Then
\[
\boxed{Z_q(t)=(1+2t)^{\binom q2}
 (1+6t+4t^2)^{q\binom{q-1}2}
 (1+24t+180t^2+472t^3+366t^4+48t^5)^{\binom q4}.}
\]
Consequently the maximum zero-error code size, number of maximum labeled codebooks, and the natural output-incidence fractional packing optimum are, respectively,
\[
\boxed{M_q=\frac{q(q-1)(q+1)(5q-6)}{24},\qquad
N_q=2^{\binom q2}4^{q\binom{q-1}2}48^{\binom q4},\qquad
P_q=\frac{q^2(q-1)^2}{4}.}
\]
The fractional integrality gap is exactly \(P_q-M_q=\binom q4\). It vanishes for \(q\le3\), first occurs at \(q=4\), when \((M_4,P_4,N_4)=(35,36,51{,}539{,}607{,}552)\), and has limiting ratio \(P_q/M_q\to6/5\) as \(q\to\infty\) with blocklength four fixed. The full enumerator, rather than the isolated size-five result on distinct-symbol permutations, is the contribution.

## Assumptions and scope
Write \(B(w)=\{w,\tau_1w,\tau_2w,\tau_3w\}\), where \(\tau_i\) exchanges positions \(i,i+1\) once. There is **at most one swap**, not simultaneous swaps at both disjoint sites, not two successive swaps, and no requirement that outputs satisfy the source constraint. Two different codewords are confusable exactly when their output sets intersect. A codebook is counted once as a subset of \(X_q\), not as an ordered list and not modulo alphabet permutations. In the fractional relaxation, there is a variable \(x_w\ge0\) per source and one constraint \(\sum_{w:\,u\in B(w)}x_w\le1\) per possible received word \(u\); maximize \(\sum_w x_w\). Its dual assigns \(y_u\ge0\) to outputs, minimizes \(\sum_u y_u\), and requires \(\sum_{u\in B(w)}y_u\ge1\) for every source. Standard conventions set \(\binom ab=0\) for \(a<b\). The size of the source language is \(q(q-1)^3\).

## Proof
**1. Canonical multiset decomposition.** Swaps preserve the four-letter multiset. Thus different source multiplicity classes have disjoint output universes, and every codebook is an independent choice of a codebook in each component. Because adjacent equal letters are forbidden, the only possible multiplicity types are \((2,2)\), \((2,1,1)\), and \((1,1,1,1)\). They have, respectively, \(\binom q2\), \(q\binom{q-1}2\), and \(\binom q4\) labeled components. Within each type, renaming symbols identifies all components with those of the canonical source multisets `aabb`, `aabc`, and `abcd`. These have exactly 2, 6, and 24 admissible source words, respectively.

**2. Exact local codebook enumeration.** Define the finite conflict graph of a canonical component: vertices are its admissible source words, and an edge joins two vertices whose at-most-one-swap output sets intersect. Its independence polynomial is \(I_G(t)=\sum_{S\ \mathrm{independent}}t^{|S|}\). For any vertex \(v\), the exact recurrence is
\[
I_G(t)=I_{G-v}(t)+tI_{G-N[v]}(t),\qquad I_{\varnothing}(t)=1,
\]
where \(N[v]\) denotes the closed neighborhood. The following coefficients result from applying this recurrence to **all** canonically generated conflict edges; a separate exhaustive subset scan recomputes them without using the recurrence. The enumerator at each degree records the number of independent subsets of precisely that size.

| Canonical multiset | Vertices | Number of independent sets of sizes \(0,1,2,3,4,5\) | Maximum | Number of maxima |
| --- | ---: | --- | ---: | ---: |
| `aabb` | 2 | \((1,2,0,0,0,0)\) | 1 | 2 |
| `aabc` | 6 | \((1,6,4,0,0,0)\) | 2 | 4 |
| `abcd` | 24 | \((1,24,180,472,366,48)\) | 5 | 48 |

For `aabb` the two alternating centers conflict, giving \(1+2t\). For `aabc`, the centers `abca` and `acba` are each adjacent to every other center, while the remaining four centers form two disjoint conflicting pairs, `{abac, baca}` and `{acab, caba}`. This gives \(2t+(1+2t)^2=1+6t+4t^2\) by hand. For `abcd`, the conflict graph is the square of the 24-vertex adjacent-transposition Cayley graph of \(S_4\): each vertex has eight conflict neighbors, so the size-two coefficient is \(\binom{24}{2}-24\cdot8/2=180\). The higher coefficients in the displayed table follow by the complete finite recurrence and independent subset scan.

To make this a finite reproducible proof rather than an unchecked coefficient assertion, `local_certificate.json` contains the entire ordered center/output incidence list and 0-based adjacency lists for all three graphs, and `verify.py` reconstructs them anew from the definition. The program evaluates the displayed recurrence using integer arithmetic and separately iterates all \(\binom{24}{r}\) subsets for \(r=1,\ldots,6\) (and analogous smaller component ranges), checking independence directly. In particular, it proves the absence of a six-vertex independent set rather than extrapolating from a partial search. The maximum codes `abab`, `{abac, acab}`, and `{abcd, adcb, bcda, cdab, dbac}` explicitly attain their local maxima. In the last case these five words are distinct permutations. Substitution of each labeled component's symbols transports these witnesses bijectively.

**3. Global polynomial and equality cases.** Codebooks in distinct multiset components are independent choices. Therefore multiplying the three local independence polynomials with the exact component counts gives the boxed \(Z_q(t)\). Its degree equals \(\binom q2+2q\binom{q-1}2+5\binom q4\), which simplifies to the boxed \(M_q\). To attain that degree, every component must itself attain its local maximum. Their leading coefficients are \(2,4,48\), respectively. Multiplying them yields exactly the boxed \(N_q\), with no quotient by relabeling. The coefficient of \(t\) is \(2\binom q2+6q\binom{q-1}2+24\binom q4=q(q-1)^3\), independently checking all admissible one-word codebooks.

**4. Fractional packing certificates.** Fractional output packing also decomposes by multiset. For `aabb`, both possible source balls contain `abba`, so a dual weight of one at `abba` gives \(P_{aabb}\le1\); an integral one-word code gives equality. For `aabc`, dual weights of one at `abca` and `caab` meet every source ball and total two; the explicit two-word code gives equality. For `abcd`, each of 24 source balls has exactly four outputs and each of the 24 possible received permutations belongs to exactly four source balls. Assigning \(x_w=1/4\) for every source gives a feasible primal objective six, while assigning \(y_u=1/4\) for every received permutation gives a feasible dual of six. Thus its fractional optimum is six, versus integer optimum five. Adding components gives \(P_q=\binom q2+2q\binom{q-1}2+6\binom q4=q^2(q-1)^2/4\). Its difference from \(M_q\) is \(\binom q4\), yielding the stated threshold and limiting ratio. \(\square\)

## Verification
From the directory containing this file, execute `python3 verify.py`. It generates each canonical source multiset and every full output set directly from the definition, builds all three conflict graphs, verifies every independent-set coefficient both by a memoized deletion–contraction recurrence and by an independent exhaustive subset scan, checks each displayed optimal code, and checks integral and rational fractional certificates. It also checks the full alphabet constructions for \(q=2,3,4,5,6,7,8\). The expected terminal line is `VERIFY_OK`; no third-party libraries are used. `local_certificate.json` records the explicit finite incidence data and can be independently rebuilt from the channel. The exact all-\(q\) theorem rests on the finite component decomposition and recurrence, not an unsupported extrapolation from the finite alphabet tests.

## Relationship to prior work
Barg and Mazumdar [1] introduced rank-modulation error correction using Kendall's \(\tau\) metric on permutations. Buzaglo and Etzion [2] study single-error correcting permutation codes and establish nonexistence of perfect single-error correction in \(S_4\); the limitation of the distinct-symbol component to five sources and the general single-swap channel are not claimed as new in isolation. The adjacent-swap rank-metric results do not give the complete labeled **independence polynomial** on each multiplicity class or the resulting arbitrary-alphabet constrained word enumerator.

Langberg, Schwartz and Yaakobi [3] study the distinct *limited-permutation* channel allowing simultaneous disjoint adjacent swaps, for which the all-distinct four-coordinate component has maximum four and the alphabet itself is unrestricted. A published exact four-coordinate result for that model [4] gives an all-alphabet capacity but does not imply this at-most-one-swap, homopolymer-free model or its codebook enumerator. Search comparisons additionally considered coding under homopolymer constraints, equivalent permutation metrics, and finite graph-table formulations. None of the inspected primary texts establishes the boxed three-part enumerator. An earlier unindexed equivalent independent-set calculation or its implicit derivation remains possible.

## Limitations
The theorem fixes blocklength four. It does not characterize longer codes, error sequences involving two swaps, simultaneous disjoint swaps, or deletion and substitution channels. The accepted alphabet varies, but the finite component counts are not a blocklength-asymptotic rate. The enumerator counts **labeled** codebook subsets; it does not count classes modulo letter permutation or reversal. Publicly inspected literature and indexed search cannot prove global novelty; especially the size-five distinct-permutation component is substantially covered by earlier single-swap coding. Reproducibility relies on the provided finite exhaustive data and checker rather than a short hand enumeration of all 24-vertex independent sets; independent mathematical review is not claimed.

## References
1. A. Barg and A. Mazumdar, *Codes in Permutations and Error Correction for Rank Modulation*, arXiv:0908.4094, first posted 27 August 2009, https://arxiv.org/abs/0908.4094 .
2. S. Buzaglo and T. Etzion, *Bounds on the Size of Permutation Codes with the Kendall \(\tau\)-Metric*, arXiv:1408.4963, https://arxiv.org/abs/1408.4963 ; see also *Perfect Permutation Codes with the Kendall's \(\tau\)-Metric*, arXiv:1310.5515, https://arxiv.org/abs/1310.5515 .
3. M. Langberg, M. Schwartz and E. Yaakobi, *Coding for the \(\ell_\infty\)-Limited Permutation Channel*, 2015 conference full text, https://yaakobi.net.technion.ac.il/files/2015/11/53_Perm_Channel_ISIT15.pdf .
4. *Exact four-coordinate \(q\)-ary limited-permutation code capacity*, published 18 October 2026, full scientific result: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-four-coordinate-q-ary-limited-permutation-code-capacity--5320b24cd567 .
