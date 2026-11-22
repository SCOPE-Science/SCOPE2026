# A uniform reversal cutoff for cyclic repeated-letter morphisms

## Finding
Let \(q\ge3\) be an integer and let \(\Sigma_q=\mathbb Z/q\mathbb Z\). Define the length-three morphism \(\sigma_q(a)=aa(a+1)\), with addition in \(\Sigma_q\), and its right-infinite fixed point \(s_q=\sigma_q^{\omega}(0)\). For \(n\ge1\), let \(\mathcal L_q(n)\) be the set of its distinct contiguous length-\(n\) factors. Put
\[
R_q(n)=|\{w\in\mathcal L_q(n):w^{\mathrm R}\in\mathcal L_q(n)\}|,
\qquad
P_q(n)=|\{w\in\mathcal L_q(n):w=w^{\mathrm R}\}|.
\]
Here reversal is the usual order reversal and is **not** a letter complementation. The exact formulas for every \(q\ge3\) are
\[
R_q(n)=\begin{cases}q,&n=1,\\q^2,&n=2,\\4q,&n=3,\\3q,&4\le n\le7,\\q,&n=8,\\0,&n\ge9,\end{cases}
\qquad
P_q(n)=\begin{cases}q,&n=1,2,\\2q,&n=3,\\q,&4\le n\le8,\\0,&n\ge9.\end{cases}
\]
In particular the entire factor language becomes disjoint from its reversal at length nine, and this is sharp because the palindromes \(aa(a+1)aa(a+1)aa\) of length eight occur for every \(a\in\Sigma_q\).

## Assumptions and scope
All indices are zero based. A factor is contiguous; this result does not count scattered subsequences or reversals of a different substitution. The theorem holds for every integer \(q\ge3\) and every positive factor length, with no numerical cutoff on \(q\). The binary case \(q=2\) has different short-length multiplicities and is not part of the claim. If \(w\) is a finite word, \(w^{\mathrm R}\) denotes its reversal. This study counts the factors whose reversal appears, not the number of reversal-equivalence classes (which would additionally require ordinary factor complexity).

## Proof
**1. Pair completeness.** Each letter occurs in \(s_q\): starting at zero, the rule \(a\mapsto aa(a+1)\) inductively introduces all residue classes. Thus \(aa\) occurs for each \(a\). If \(ab\) occurs, applying \(\sigma_q\) shows that \((a+1)b\) occurs at the boundary of \(\sigma_q(a)\sigma_q(b)\). Iterating this implication from \(bb\) proves that all \(q^2\) ordered pairs of letters occur in \(s_q\).

**2. Finite exact factor window.** Put \(B_a=\sigma_q^2(a)\). Then
\[
B_a=aa(a+1)\,aa(a+1)\,(a+1)(a+1)(a+2),
\]
a nine-symbol word. Since \(s_q=\sigma_q^2(s_q)\), every factor of length at most nine is contained in \(B_aB_b\) for two consecutive letters \(ab\) of \(s_q\). Pair completeness supplies the converse: **every** such two-block window occurs. Thus for \(1\le n\le9\), the union of length-\(n\) windows of the \(q^2\) words \(B_aB_b\) is exactly \(\mathcal L_q(n)\), not merely a finite-prefix approximation.

**3. Uniform symbolic reversal comparison.** For \(3\le n\le9\), compare all ordered pairs of windows (starts \(i,j\) from \(0\) through \(18-n\)) in \(B_aB_b\) and \(B_cB_d\), requiring one to be the reversal of the other. Each coordinate equality is a constraint of the form \(X+u\equiv Y+v\pmod q\), where \(X,Y\in\{a,b,c,d\}\) and \(u,v\in\{0,1,2\}\). Regard these as edges \(Y-X=u-v\) of a four-vertex difference graph. Choosing integer potentials along a spanning forest, the constraints are solvable modulo \(q\) precisely when \(q\) divides every cycle discrepancy, equivalently when it divides their nonnegative greatest common divisor \(g\); \(g=0\) means universally soluble. This is a finite, exact algebraic criterion for **all** alphabet sizes, not experimental extrapolation.

The accompanying `verify_symbolic.py` enumerates these \(\sum_{n=3}^{9}(19-n)^2\) window comparisons by this integer graph criterion. Every nonzero \(g\) is exactly \(1\) or \(2\), hence has no solution for \(q\ge3\). In every case with \(g=0\), the variables used in the first window belong to one connected component; after subtracting its first letter, its complete pattern is fixed. The resulting **exhaustive normalized factor signatures** (entries are integer offsets from the initial symbol, interpreted modulo \(q\)) are:

| Length | Normalized reversible signatures |
|---|---|
| 3 | `(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,-1,-1)` |
| 4 | `(0,0,1,0)`, `(0,1,0,0)`, `(0,-1,-1,0)` |
| 5 | `(0,0,1,0,0)`, `(0,1,0,0,1)`, `(0,-1,-1,0,-1)` |
| 6 | `(0,0,1,0,0,1)`, `(0,1,0,0,1,0)`, `(0,-1,-1,0,-1,-1)` |
| 7 | `(0,0,1,0,0,1,0)`, `(0,1,0,0,1,0,0)`, `(0,-1,-1,0,-1,-1,0)` |
| 8 | `(0,0,1,0,0,1,0,0)` |
| 9 | None |

For \(q\ge3\), distinct signatures on any one line remain distinct modulo \(q\), and each has exactly \(q\) global letter translations. This proves \(R_q(n)\) at lengths three through nine. Length one has \(q\) reversible letters and length two has all \(q^2\) ordered pairs and their reversals. When a word of length at least nine has its reversal in the language, their length-nine prefixes/suffixes would yield a reversible length-nine factor, a contradiction. This proves \(R_q(n)=0\) for all \(n\ge9\).

**4. Palindromes.** Inspecting the same complete signatures, there are two palindromic signatures at length three and exactly one at each length four through eight, yielding the stated \(P_q(n)\). Every length-one letter and each doubled letter is a palindrome, proving the remaining cases. The length-eight signature is self-reversing, so the cutoff is attained sharply. These deductions use the exact window certificate from Step 3, not unbounded enumeration.

## Verification
Run `python3 verify_symbolic.py` and `python3 verify_direct.py` in the same directory. The first program checks all integer-cycle comparison cases for lengths three through nine without fixing \(q\), and asserts both the nonzero discrepancy set \(\{1,2\}\) and every normalized signature in the displayed table. The second independently computes the fixed point using its base-three digit-two formula and compares actual factor and reversal sets for all lengths one through nine at \(q=3,4,5\), also checking pair completeness. The exact captured outputs are in `symbolic_output.txt` and `direct_output.txt`. Finite-prefix tests corroborate the result but do not establish the infinite claim; the pair-completeness lemma, exact two-block reduction, and modular graph certificate do.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit and Stipulanti (2026, arXiv:2610.03837v1) investigate abelian complexity of automatic words arising from cyclic repeated-letter morphisms, explicitly proposing related morphism families for study. Their construction has three repetitions and a modulus-three alphabet, rather than the two-repetition family in this theorem, and it does not classify reversals. Rowland and Yassawi (online September 5, 2019, Example 5.7) already introduced the \(q=3\) member \(0\mapsto001,1\mapsto112,2\mapsto220\) for cellular-automaton dynamics; its construction is not claimed as new. Frid, Laborde and Peltomäki (2020) prove a general regularity theorem for prefix palindromic length of automatic words with finitely many palindromes; it does not supply these explicit languages or the reversal cutoff. Related published computations of reversal barriers for the distinctly defined substitution \(0\mapsto01,1\mapsto21,2\mapsto0\) likewise do not imply the claimed alphabet-uniform count for \(a\mapsto aa(a+1)\). No first-appearance claim is made for any general principle already established by those sources.

## Limitations
The classification is for the specific cyclic substitution family and alphabet sizes at least three. It is not a classification of reversal barriers for all primitive substitutions; it supplies neither all ordinary factor counts nor a closed prefix-palindromic-length function. Historical literature may contain an unindexed equivalent, and no independent external mathematical audit has been performed. The normalized-signature table is supported by a small auditable symbolic certificate whose exact graph-solving argument is specified in the proof.

## References
1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1, first submitted 2026-10-02. https://arxiv.org/html/2610.03837v1
2. E. Rowland, R. Yassawi, *Automaticity and Invariant Measures of Linear Cellular Automata*, Canadian Journal of Mathematics 72 (2020), 1691–1726, online 2019-09-05, Example 5.7. https://doi.org/10.4153/S0008414X19000488
3. A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (2020). https://arxiv.org/abs/2009.02934
4. *Exact reflection spectrum and a sharp reversal barrier for a ternary morphic word* (2026), a distinct substitution and separately scoped reversal result. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-reflection-spectrum-and-a-sharp-reversal-barrier-for-a-ter--2fe09ee974cf
