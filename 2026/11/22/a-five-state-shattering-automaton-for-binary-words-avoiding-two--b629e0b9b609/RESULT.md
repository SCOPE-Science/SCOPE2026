# A five-state shattering automaton for binary words avoiding two trigrams

## Finding

Let \(\mathcal H_n\) contain all length-\(n\) binary words with neither `000` nor `101` as a contiguous factor, and query the bit at a chosen coordinate. A support \(S\subseteq[n]\), encoded by its binary indicator \(b_1\ldots b_n\), is VC-shattered **if and only if** that indicator is accepted by the following five-state partial automaton, started in state \(0\), with every listed state accepting and an omitted transition rejecting:

| State | Input `0` (unqueried) | Input `1` (queried) |
|:--|:--|:--|
| 0 | 0 | 1 |
| 1 | 2 | 3 |
| 2 | 0 | 3 |
| 3 | 4 | reject |
| 4 | 2 | reject |

Writing \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\), one has the exact rational series

\[
\boxed{\sum_{n\ge0}\Phi_n(z)t^n=\frac{1+tz+t^2z+t^2z^2-t^3z+2t^3z^2+t^4z^2}{1-t-2t^3z+t^4z-t^5z^2}.}
\]

The exact VC dimension is \(0\) for \(n=0\) and, for every \(n\ge1\),

\[\boxed{\operatorname{VCdim}(\mathcal H_n)=\left\lfloor\frac{2n+6}{5}\right\rfloor.}\]

For instance, \(\Phi_5(z)=1+5z+10z^2+2z^3\) and \(\Phi_{10}(z)=1+10z+45z^2+92z^3+68z^4+4z^5\). The five nonrejecting states are inequivalent as right languages, so this is the minimal partial deterministic automaton (up to state renaming).

## Assumptions and scope

The words are finite and linearly ordered; neither forbidden triple may appear anywhere, including across an endpoint only if all three coordinates lie in the word. Shattering means \(\forall\lambda:S\to\{0,1\}\ \exists w\in\mathcal H_n\) satisfying \(w_i=\lambda(i)\) for all \(i\in S\). Unqueried bits may depend on the labeling. The empty support is counted once, and \(\mathcal H_0\) consists of the empty word.

## Proof

**Exact determinization.** Let \(Q=\{\epsilon,0,1,00,01,10,11\}\) be the seven prefix states storing the last at most two bits. The partial transition \(\delta(q,c)\) appends bit \(c\) and retains at most its last two bits, except that a transition creating `000` or `101` is undefined. For a set \(B\subseteq Q\), put \(\delta_c(B)=\{\delta(q,c):q\in B,\,\delta(q,c)\text{ defined}\}\). A family \(\mathcal F\) of nonempty subsets of \(Q\) represents the possible terminal prefix-states for each assignment to the queried coordinates seen so far, with duplicate sets immaterial. Initially \(\mathcal F=\{\{\epsilon\}\}\).

On indicator symbol `0`, replace every \(B\in\mathcal F\) by \(\delta_0(B)\cup\delta_1(B)\). On indicator symbol `1`, replace every \(B\in\mathcal F\) by both \(\delta_0(B)\) and \(\delta_1(B)\). If any newly produced set is empty, reject. This is exactly the shattering quantifier condition after each prefix: every specified assignment must have at least one admissible completion of the prefix. Because both forbidden patterns are local and there is no terminal constraint, a nonempty reachable prefix always constitutes a valid word at the current length. Thus this family determinization is valid at every length.

Enumerating its reachable nonrejecting families in breadth-first order from the initial family yields exactly sixteen states \(0,1,\ldots,15\). Their two transition columns (with `-` denoting rejection) are, in order:

```
0:(1,2)    1:(3,4)    2:(5,6)    3:(3,4)
4:(5,6)    5:(7,8)    6:(9,-)    7:(10,11)
8:(12,-)   9:(13,-)  10:(3,4)   11:(5,6)
12:(14,-) 13:(15,8) 14:(15,8) 15:(10,11)
```

The five equivalence classes (listed by these sixteen indices) are \(\{0,1,3,7,10,15\}\), \(\{2,4,11\}\), \(\{5,13,14\}\), \(\{6,8\}\), and \(\{9,12\}\). Checking both transitions gives exactly the five-state table in the finding. Partition refinement against the rejecting sink proves distinctness of the five right languages. The finite table can also be derived from the explicit seven-state set map without trusting a computation; the attached standalone checker independently reconstructs it from those definitions.

**Generating function.** For each automaton state \(j\), let \(G_j\) be the generating function of all accepted suffixes, with each indicator `0` weighted \(t\) and each `1` weighted \(tz\), including the empty suffix. The table gives

\[
\begin{aligned}
G_0&=1+tG_0+tzG_1,& G_1&=1+tG_2+tzG_3,\\
G_2&=1+tG_0+tzG_3,& G_3&=1+tG_4,\\
G_4&=1+tG_2.
\end{aligned}
\]

Solving these five linear equations over \(\mathbb Q(t,z)\) yields the displayed rational expression \(G_0=\sum_{n\ge0}\Phi_n(z)t^n\).

**Sharp dimension upper bound.** Assign state potentials \(h=(0,-3,-2,-6,-4)\), indexed \(0,\ldots,4\). Every allowed automaton edge \(i\overset{b}{\longrightarrow}j\), with \(b\in\{0,1\}\), satisfies \(h_j\le h_i+2-5b\), by direct inspection of all eight allowed transitions. Consequently any accepted indicator of length \(n\) and weight \(k\) satisfies \(h_{\rm final}\le 2n-5k\). As all potentials are at least \(-6\), this implies \(5k\le 2n+6\).

**Sharp dimension lower bound.** For each \(r\ge1\), the indicator `11` followed by \(r-1\) copies of `00011` is accepted, has \(2r\) ones, and length \(5r-3\). Similarly, `10011` followed by \(r-1\) copies of `00011` is accepted, has \(2r+1\) ones, and length \(5r\). Both claims follow directly by tracing the five-state table. These are lengths \(\lceil(5k-6)/2\rceil\) for all \(k\ge2\). Appending `0`s preserves acceptance because every nonrejecting state has a defined `0` transition. For \(n=1\), one selected coordinate is shattered. Together with the upper bound, the dimension formula follows for every \(n\ge1\).

## Verification

Run `python3 verify.py` using Python 3.9 or newer. It independently constructs the seven suffix states and all sixteen determinized reachable families, minimizes them by partition refinement, compares the minimized table to the one above, checks the sharp potential bound and the extremal witness patterns, and directly enumerates all hypothesis words and queried-support traces for each length \(0\le n\le11\). Its successful output ends in `FINITE_STATE_CERTIFICATE_PASS`; the accompanying `verification_output.txt` is a record of one replay. The finite enumerations corroborate the proof and are not substitutes for the all-length determinization and potential argument.

## Relationship to prior work

Hunter R. Johnson, *Binary strings of finite VC dimension* (2021), investigates the set system of translates/substrings associated with **one fixed binary sequence**, rather than the coordinatewise projections of all words of a fixed forbidden-factor language. A prior complete calculation for binary words avoiding `000` and `111` gives a different automaton and a different support generating function: its length-five support polynomial is \(1+5z+10z^2+7z^3\), whereas here it is \(1+5z+10z^2+2z^3\). The two languages are not equivalent under uniform coordinatewise complementation or parity relabeling, and neither result logically covers the other. Louidor–Marcus–Pavlov's fixed-background independence-entropy framework requires the unqueried symbols to be fixed before labels vary, whereas VC shattering permits label-dependent completions. These distinctions delimit the claim; they are not proofs of historical uniqueness.

## Limitations

This result concerns the specific pair of forbidden contiguous factors `000` and `101`, linearly indexed finite binary words and existential VC shattering. It does not determine adaptive Littlestone dimension, cyclic words, arbitrary forbidden-factor sets, or all fixed-background independence entropies. Historical priority remains subject to independent review, particularly for symbolic-dynamics results not returned by the searches examined.

## References

- H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first posted 2021-01-16, https://arxiv.org/abs/2101.06490.
- *A regular shattering complex for binary words with no monochromatic triple*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-regular-shattering-complex-for-binary-words-with-no-monochroma--a86c7bc37664/RESULT.md.
- E. Louidor, B. Marcus and R. Pavlov, *Independence entropy of \(\mathbb Z^d\)-shift spaces*, Acta Applicandae Mathematicae 126 (2013), DOI 10.1007/s10440-013-9819-2.
