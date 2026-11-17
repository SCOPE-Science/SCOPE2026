# Rule 73: exact temporal-two zeta and an exponential oscillation–equilibrium gap

## Finding

Let \(F_n\) be synchronous elementary binary cellular automaton Rule 73 on the **indexed** cyclic ring \(\mathbb Z/n\mathbb Z\). For every integer \(n\ge1\), let \(s_n=|\{x:F_n(x)=x\}|\), \(t_n=|\{x:F_n^2(x)=x\}|\), and \(c_n=(t_n-s_n)/2\), the number of unordered primitive temporal two-cycles. Then the two *spatial* dynamical zeta functions are exactly

\[
\boxed{\exp\!\left(\sum_{n\ge1}\frac{s_nz^n}{n}\right)=\frac{1}{1-z^3-z^4}}
\]

and

\[
\boxed{\exp\!\left(\sum_{n\ge1}\frac{t_nz^n}{n}\right)
=\frac{1}{(1-z)^2(1+z^2)^2(1-2z^2-z^3+z^4)}.}
\]

In particular, every \(c_n\) is determined exactly by these rational functions. If \(\alpha\) is the largest positive root of \(u^4-2u^2-u+1=0\) and \(\beta\) the unique positive root of \(u^4-u-1=0\), then

\[
1.490<\alpha<1.491,\qquad1.220<\beta<1.221,
\quad c_n\sim\tfrac12\alpha^n,
\quad s_n\sim\beta^n.
\]

Thus primitive two-cycle populations grow exponentially faster than equilibrium populations, and the fraction of \(F_n^2\)-fixed configurations that are fixed by one update tends to zero exponentially. For \(n=5\), for example, there are zero equilibria but six primitive two-cycles.

## Assumptions and scope

Rule 73 has local output one precisely on the input triples `000`, `011`, and `110`; the other five triples produce zero. Sites update simultaneously, with each site reading its immediately preceding, current, and immediately following bit. Indices are reduced modulo \(n\), even at \(n=1,2\), where the same physical bit can appear more than once in a neighborhood. An indexed word and its rotation are counted as distinct unless they are literally equal. Temporal cycles are unordered pairs \(\{x,F_n(x)\}\); spatial rotations are **not** identified. The displayed generating functions enumerate periodic points for the spatial shift on the subshifts \(\operatorname{Fix}(F)\) and \(\operatorname{Fix}(F^2)\), not periods of the entire time-evolution map.

## Proof

**One-update fixed-point transfer.** For an input triple \(abc\), draw \(ab\to bc\) in the binary order-two de Bruijn graph exactly if \(f(a,b,c)=b\). Its four vertices `00`, `01`, `10`, `11` have directed edges `00→01`, `01→11`, `10→00`, `10→01`, `11→10`. Let \(B\) be this four-by-four adjacency matrix, indexed in the stated vertex order. Every closed walk of length \(n\) corresponds to precisely one indexed \(n\)-periodic binary word fixed by \(F_n\), including the cases \(n<3\) because overlapping bits are identified. Hence \(s_n=\operatorname{tr}(B^n)\). Direct characteristic/determinant calculation gives

\[
\det(I-zB)=1-z^3-z^4.
\]

**Two-update transfer.** For any five-bit word \(w=w_0w_1w_2w_3w_4\), set

\[
g(w)=f\bigl(f(w_0,w_1,w_2), f(w_1,w_2,w_3), f(w_2,w_3,w_4)\bigr).
\]

Then \(F_n^2(x)=x\) means exactly that every five-bit cyclic window satisfies \(g(w)=w_2\). Evaluating all \(32\) possibilities leaves precisely the following \(20\) admissible five-bit words:

`00000 00010 00011 00100 00101 00110 01000 01011 01100 01101 10001 10011 10100 10101 10110 11000 11001 11010 11011 11111`.

Let \(A\) be the adjacency matrix on all sixteen four-bit words, with edge \(w_0w_1w_2w_3\to w_1w_2w_3w_4\) exactly for these windows. The same cyclic-walk bijection, valid for every \(n\ge1\), proves \(t_n=\operatorname{tr}(A^n)\).

The graph has two singleton loop components at `0000` and `1111`, two acyclic singletons `0111`, `1110`, and one strongly connected twelve-vertex component

`0001 0010 0011 0100 0101 0110 1000 1001 1010 1011 1100 1101`.

That twelve-vertex component has directed edges `0001:0010,0011; 0010:0100,0101; 0011:0110; 0100:1000; 0101:1011; 0110:1100,1101; 1000:0001; 1001:0011; 1010:0100,0101; 1011:0110; 1100:1000,1001; 1101:1010,1011`. Exhausting elementary directed cycles and all collections of vertex-disjoint cycles in these explicitly stated graphs gives the **exact** signed cycle-cover determinants

\[
\det(I-zA)=(1-z)^2(1+z^2)^2(1-2z^2-z^3+z^4),
\quad \det(I-zB)=1-z^3-z^4.
\]

The elementary-cycle determinant expansion gives weight \((-1)^kz^{\ell}\) to a selection of \(k\) vertex-disjoint directed elementary cycles with total length \(\ell\). The standard-library verifier recomputes the cycles and their complete disjoint-subset expansion, instead of trusting an unsupported symbolic factorization. There are ten elementary cycles in the sixteen-vertex graph and two in the four-vertex graph. The finite graph calculation plus the closed-walk correspondence proves the determinant identities for **all** ring lengths; no finite-length extrapolation is used.

**Zeta and asymptotics.** For any finite matrix \(M\), the formal identity

\[
-\log\det(I-zM)=\sum_{n\ge1}\operatorname{tr}(M^n)\frac{z^n}{n}
\]

establishes both boxed formulas. The twelve-state component of \(A\) is strongly connected (every listed vertex reaches and can be reached from `0001`) and aperiodic: it has a three-cycle and a four-cycle meeting at `0110`. Its characteristic polynomial is

\[
u^4(u^2+1)^2(u^4-2u^2-u+1).
\]

By Perron–Frobenius, its spectral radius is a simple positive eigenvalue strictly exceeding the moduli of all other eigenvalues in the component. The quartic has a positive root between \(1.490\) and \(1.491\) (direct rational sign tests); it is the unique root greater than \(1.3\), since the quartic is negative at \(1.3\) and strictly increasing thereafter (its derivative is \(4u^3-4u-1>0\) there); so it is that Perron root \(\alpha\). The two isolated loops contribute only bounded traces, and the two acyclic vertices contribute zero. Therefore \(t_n=\alpha^n+o(\alpha^n)\).

The four-state graph of \(B\) is also strongly connected and aperiodic (its three- and four-cycles intersect). Its characteristic polynomial is \(u^4-u-1\), whose unique positive root \(\beta\) lies strictly between \(1.220\) and \(1.221\), by exact rational sign tests. Consequently \(s_n=\beta^n+o(\beta^n)\). Since \(\alpha>\beta\), subtraction yields \(c_n=(t_n-s_n)/2\sim\alpha^n/2\) and \(s_n/t_n\to0\) exponentially.

## Verification

The included `verify.py` constructs both graphs directly from the Rule-73 truth table, exhausts their elementary cycles and **all** disjoint-cycle collections with integer arithmetic, verifies both determinant polynomials, checks reachability and intersecting coprime cycles in the primitive components, and directly enumerates all bit configurations at lengths \(1\) through \(17\). Its final line is `CERTIFICATE_OK`. The independent `check_direct.py` derives the trace sequences from the two displayed determinant polynomials and checks them against direct synchronous updates for all \(524286\) configurations on rings of lengths \(1\) through \(18\), reporting `BRUTE_OK`. Both scripts use only the Python standard library; the included output files record actual successful executions. All-length validity comes from the finite directed-graph construction and the exact determinant identities, not from these finite direct-enumeration checks.

For orientation, the primitive temporal two-cycle orbit counts at lengths \(3,4,5,6,7,8,9,10\) are respectively \(1,3,6,1,8,11,19,21\).

## Relationship to prior work

Wolfram's *A New Kind of Science* (2002) describes Rule 73's persistent walls, localized structures, and frequent period-three density oscillations, but does not give the stated exact temporal-two orbit counts or zeta. Kang's Rule-73 investigation (2013) chiefly treats spaced neighborhoods such as LDCA-1-2 and its particle collisions; its state update is not this nearest-neighbor cyclic automaton. Stricker (2023) analyzes finite-ring *maximal cycle lengths* and reports data for Rule 73, but the inspected paper does not derive counts of all primitive temporal two-cycles at every ring length. The published all-length Rule-73 **one-step image** result counts distinct outputs \(|\operatorname{im}F_n|\), not \(\operatorname{Fix}(F_n)\) or \(\operatorname{Fix}(F_n^2)\), and does not imply this formula. The previously published exact temporal-two spatial zeta for **Rule 18** is a closely related technique but concerns a different local map with different determinant and growth rate. The present formulas are not claimed to classify higher temporal periods, and the novelty comparison is not a proof of historical priority.

## Limitations

The theorem counts exactly period-one and period-two *temporal* configurations on cyclic finite rings and their spatial entropies; it does **not** classify all attractors, transient times, or the maximal temporal period of Rule 73. The growth constants measure populations of constrained periodic configurations, not the density of these configurations among all \(2^n\) words. Finite tests support the exact transfer computation but do not independently establish it for unbounded lengths. The literature search cannot exclude inaccessible or unindexed equivalent earlier formulas. No independent scientific audit has been performed.

## References

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, first publication 2002-05-14; page 699 and Rule-73 notes pp. 885 and 954. https://www.wolfram-media.com/products/nks/ ; https://www.wolframscience.com/nks/p699--the-threshold-of-universality-in-cellular-automata/ ; https://www.wolframscience.com/nks/notes-3-2--rule-73/ ; https://www.wolframscience.com/nks/notes-6-5--density-oscillations-in-rule-73/ .
2. L. Kang, *Investigation of Rule 73 as Case Study of Class 4 Long-Distance Cellular Automata*, 2013, arXiv:1310.3311; accessible related author text https://mazziotti.uchicago.edu/journal/kang_l.pdf .
3. H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, *Complex Systems* 32(3) (2023), 229–251, DOI 10.25088/ComplexSystems.32.3.229; https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf .
4. *Exact cyclic one-step image series of elementary cellular automaton Rule 73*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-one-step-image-series-of-elementary-cellular-automa--4412da3b7a44 .
5. *Exact temporal-two orbit census and spatial zeta for elementary cellular automaton 18*, published 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-temporal-two-orbit-census-and-spatial-zeta-for-elementary--752b17859ec3 .
