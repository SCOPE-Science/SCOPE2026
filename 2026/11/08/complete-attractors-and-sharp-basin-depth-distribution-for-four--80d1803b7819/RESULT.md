# Complete attractors and sharp basin-depth distribution for four-digit duodecimal Kaprekar dynamics

## Finding

Consider the fixed-width four-digit base-\(12\) Kaprekar transformation \(K\): sort the four base-\(12\) digits in descending order, subtract their ascending-order arrangement, and retain leading zeroes. On the \(12^4-12=20724\) non-repdigit digit strings there are **exactly two terminal cycles**, of lengths three and six. Their elements, displayed as ordinary decimal integers, are respectively

\[
\{6908,10890,14212\},\qquad
\{7172,9031,10626,12617,13816,14344\}.
\]

The cycles have precisely \(4712\) and \(16012\) starting strings in their basins. For the three-cycle, the numbers of starts entering that cycle after exactly \(h=0,1,2,3,4,5\) iterations are

\[
(3,1117,1128,1104,520,840).
\]

For the six-cycle, the respective numbers for \(h=0,1,2,3,4,5,6,7\) are

\[
(6,2402,3080,5592,2584,892,808,648).
\]

Consequently the sharp greatest entry time is \(7\). The twelve excluded repdigits map to zero, which is a separate fixed point. Cyclic membership and entry times are defined with respect to the integer Kaprekar map, not a mere digit-multiset dynamical system.

## Assumptions and scope

A digit string is a quadruple of digits in \(\{0,1,\ldots,11\}\). Every quadruple is counted independently, including those whose first digit is zero. Write \(x\in\{0,1,\ldots,20735\}\) for its value, with leading zeros implicitly retained. For a non-repdigit, define its entry time \(h(x)\) as the least \(h\ge0\) for which \(K^h(x)\) is a member of either nonzero periodic cycle. All displayed integer cycle elements are in decimal notation, not base-\(12\) digit strings.

## Proof

**Step 1 (two gap coordinates).** For the sorted digits \(0\le a\le b\le c\le d\le11\), put

\[
u=d-a,\qquad v=c-b.
\]

A non-repdigit has \(1\le u\le11\) and \(0\le v\le u\); there are exactly \(\sum_{u=1}^{11}(u+1)=77\) possible pairs. Directly subtracting the reversed digit arrangements gives

\[
K(x)=(12^3-1)u+(12^2-12)v=1727u+132v=:J(u,v).
\]

In particular \(K\) depends only on the gap pair. Let \(g(y)\) be the pair of outer and inner differences of the sorted base-\(12\) digits of \(y\); after one step the pair evolves by the explicit function

\[
F(u,v)=g(1727u+132v).
\]

This is a total endomorphism of the stated 77-element set. Further, \(J\) is injective on the set: \(1727(u-u')=132(v'-v)\) implies \(u-u'\) is a multiple of \(12\), whereas \(|u-u'|\le10\); hence \(u=u'\) and \(v=v'\). Thus the nonzero integer cycles correspond bijectively to the cycles of \(F\), with each gap cycle giving the distinct integer values \(J(u,v)\).

**Step 2 (finite exhaustive graph certificate).** The accompanying `gap_table.csv` lists **all 77 admissible pairs**, their exact images under \(F\), their eventual cycle lengths and distances to the respective gap cycles. Each image is reproducible by sorting the four base-\(12\) digits of the displayed integer \(1727u+132v\). Following every arrow in this complete finite table produces exactly the gap cycles

\[
\{(4,0),(6,4),(8,3)\}
\quad\text{and}\quad
\{(4,2),(5,3),(6,2),(7,4),(8,0),(8,4)\}.
\]

For the first set, applying \(J\) gives the three decimal values already displayed; for the second, it gives the six displayed values. Because the table lists every possible state, this is an exhaustive finite proof that no further nonzero cycle exists. The standalone `verify.py` reproduces the entire table from the defining formula and checks that the specified cycles and all 77 distances are correct.

**Step 3 (exact sizes of the multiset fibres).** The number \(W(u,v)\) of *ordered* four-digit strings with gap pair \((u,v)\) is

\[
W(u,v)=(12-u)
\begin{cases}
4(3u-1),&v=0,\\
6,&v=u,\\
24(u-v),&0<v<u.
\end{cases}
\]

To prove this, fix the least digit \(a\), with \(0\le a\le11-u\), and write the sorted quadruple as

\[
(a,\ a+s,\ a+s+v,\ a+u),\qquad 0\le s\le u-v.
\]

For \(v=0\), the two boundary values of \(s\) yield multiplicity four each; its \(u-1\) interior values yield multiplicity twelve, for \(4(3u-1)\) permutations. For \(v=u\) there is one arrangement with two pairs of equal digits, giving six permutations. For \(0<v<u\), the two boundary values each yield twelve permutations, and the \(u-v-1\) interior values each yield twenty-four, giving \(24(u-v)\). Multiplying by the \(12-u\) choices of \(a\) proves the formula. In particular, direct summation over the 77 rows gives \(\sum W(u,v)=20724\), all non-repdigits.

**Step 4 (entry times and sharpness).** Let \(t(u,v)\) denote the tabulated distance from \((u,v)\) to its gap cycle. Every original string in the fibre of \((u,v)\) enters the corresponding integer cycle after \(t(u,v)+1\) steps, *except* that when \(t=0\) exactly one string in that fibre is already a member of the integer cycle, so it has entry time zero rather than one. The exception follows because \(F\) traverses each pair of each cycle once and the integer cycle members have exactly those gap pairs, by injectivity of \(J\). Therefore for each periodic state one subtracts one from the \(h=1\) count and adds one to \(h=0\). Applying the exact fibre weights to the 77 certified rows yields the two vectors displayed in the finding, of sums \(4712\) and \(16012\). The largest nonzero count is at \(h=7\), namely \(648\), proving both the upper bound and its attainment. Finally the twelve repdigits all yield zero in one iteration and cannot arise from any non-repdigit (whose sorted outer gap \(u\) is positive, hence \(J(u,v)>0\)).

## Verification

All required finite checks can be repeated using the Python standard library:

```
python3 verify.py
```

The checker independently (i) reconstructs the weighted 77-state gap graph and checks the exact bytes of `gap_table.csv` and (ii) iterates the original digit-sorting map from every one of the \(12^4=20736\) padded strings without relying on the gap graph. It compares cycle membership and complete entry-time histograms to the theorem. The expected output is embedded as `verification_output.txt`. The finite complete certificate supplies the exhaustive step of the proof; its arithmetic derivations and fibre formulas are given above rather than inferred from a sample of trajectories.

## Relationship to prior work

Kay and Downes-Ward (2024) study Kaprekar fixed points and cycles in general even bases and give detailed enumerations for bases \(4,6,8\), noting that higher even bases present unresolved enumeration difficulties. Their digit-gap framework is relevant here, but their paper does not tabulate the complete four-digit base-\(12\) graph, basin populations or entry-time distribution. Hanover (2017) studies base-dependent Kaprekar behavior with its main classification of three-digit cases, rather than this four-digit base-\(12\) census. Standard tables of cycles for familiar bases and OEIS base-\(8\) sequence A165099 do not state the complete base-\(12\) attractor/basin result. The novel asserted contribution is the complete exact base-\(12\), four-digit, two-basin distribution and its finite 77-state certificate, **not** the general notion of gap coordinates or the Kaprekar transformation.

## Limitations

This result is confined to four-digit base-\(12\) strings with leading zeros retained. It does not classify all digit lengths or even bases, and the finite exhaustive theorem is not a general asymptotic formula. The displayed mathematical proof and deterministic checker have undergone the self-review reported separately; no independent mathematical audit is claimed.

## References

- A. Kay and K. Downes-Ward, *Fixed Points and Cycles of the Kaprekar Transformation: 2. Even bases*, arXiv:2408.12257v1 (first posted 22 August 2024), https://arxiv.org/abs/2408.12257 .
- D. Hanover, *The Base Dependent Behavior of Kaprekar's Routine: A Theoretical and Computational Study Revealing New Regularities*, arXiv:1710.06308 (2017), https://arxiv.org/abs/1710.06308 .
- E. W. Weisstein, *Kaprekar Routine*, MathWorld, https://mathworld.wolfram.com/KaprekarRoutine.html .
- OEIS A165099, fixed points and least cycle members of the base-eight Kaprekar transformation, https://oeis.org/A165099 .
