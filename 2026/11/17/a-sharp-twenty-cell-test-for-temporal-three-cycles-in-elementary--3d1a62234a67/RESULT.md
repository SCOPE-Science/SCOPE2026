# A sharp twenty-cell test for temporal three-cycles in elementary cellular automata

## Finding

For each Wolfram elementary binary cellular automaton rule \(r\in\{0,\ldots,255\}\), let \(F_{r,n}\) be its synchronous global map on indexed cyclic binary words of length \(n\ge 1\). A *primitive temporal three-cycle* is a configuration \(x\) with \(F_{r,n}^{3}(x)=x\) but \(F_{r,n}(x)\ne x\); its temporal orbit contains exactly three states.

**Sharp uniform finite-ring criterion.** Every one of the 256 rules either admits no primitive temporal three-cycle on any cyclic ring or admits one with \(n\le20\). The bound 20 is optimal and is attained as the *least* such length by Rule 105 alone. The exact distribution of least ring lengths is:

| Least ring length | Number of rules |
|---:|---:|
| no such length | 106 |
| 3 | 112 |
| 5 | 3 |
| 6 | 18 |
| 7 | 4 |
| 9 | 8 |
| 12 | 4 |
| 20 | 1 |

A complete 256-rule, machine-readable table is provided in `minimum_lengths.csv`. In particular, precisely 150 rules admit a temporal three-cycle on some finite ring, and 106 never do.

**Arithmetic sharp case.** For Rule 105, the primitive temporal three-cycle exists on a cyclic ring of length \(n\) *if and only if* \(20\mid n\). For every \(n\) divisible by 20 there are exactly 60 labelled configurations of least temporal period three, forming exactly 20 temporal three-cycles. When \(4\mid n\) but \(5\nmid n\), Rule 105 has four fixed configurations and no temporal-three configurations. For all other lengths it has no fixed or three-periodic configurations.

One explicit 20-cell three-periodic configuration for Rule 105 is `00010101111110101000`. Its first iterate is `11001011000011010011`, its second is `01000111011011100010`, and its third recovers the original word.

## Assumptions and scope

Cells are indexed modulo \(n\), with repeated neighbors allowed at \(n=1,2\). The Wolfram rule \(r\) has local update \(f_r(a,b,c)=\lfloor r/2^{4a+2b+c}\rfloor\bmod 2\). All configurations are labelled by cell position, with no quotient under cyclic rotation, reflection or color exchange. Temporal periods refer to exact equality of indexed states, not equality up to spatial shift. The period-three condition excludes temporal fixed points. The theorem is about the complete set of 256 radius-one binary rules, not arbitrary larger-neighborhood automata.

## Proof

**1. Exact finite graph model.** For each \(r\), form a directed graph with 64 vertices, the six-bit words \(u\). For every seven-bit word \(w=(w_0,\ldots,w_6)\), draw an edge from \((w_0,\ldots,w_5)\) to \((w_1,\ldots,w_6)\) precisely if the radius-three local third iterate, applied to \(w\), outputs its central bit \(w_3\). Mark this edge if \(f_r(w_2,w_3,w_4)\ne w_3\). Such edges are uniquely indexed by their seven-bit word.

Every cyclic word of length \(n\) determines a length-\(n\) closed walk, since its cyclic seven-bit neighborhoods overlap. The walk belongs to this graph if and only if \(F_{r,n}^3(x)=x\). A marked edge occurs if and only if \(F_{r,n}(x)\ne x\). Conversely, every closed walk of length \(n\) gives a cyclic word of length \(n\) with exactly these properties, including for \(n<7\), where neighborhoods repeat bits. As 3 is prime, a nonfixed configuration returning after three updates has exact period three.

A marked edge \(u\to v\) belongs to some directed closed walk if and only if there is a directed path from \(v\) to \(u\). A shortest such path may be chosen simple, of at most 63 edges. Hence any rule exhibiting a primitive temporal three-cycle has an example on a ring of length at most 64. More precisely, the least witness length is the minimum over marked edges of one plus the shortest-path distance from head to tail. This distance is computable exactly by finite breadth-first search.

**2. Complete 256-rule certificate.** `verify_windows.py` constructs all allowed seven-bit edges by applying the local rule three times to each seven-bit pattern. For every marked edge, it uses breadth-first search on the full 64-vertex directed graph and finds the shortest return path. The program checks each recovered witness directly under the global automaton, rejecting incorrect returns or fixed configurations. `verify_spacetime.py` independently constructs a different 64-vertex graph whose vertices are pairs of three-bit temporal columns. Its edge constraints require that three successive time rows update cyclically; a marked middle column records change at the first temporal step. This graph has the same closed-walk characterization but does not use the seven-bit third-iterate calculation. Its independently computed 256-rule least lengths agree *entry by entry* with the first graph. Both report the exact eight-row distribution above and unique maximum 20 at Rule 105. These two short, complete finite certificates prove the uniform theorem; no inference from a bounded sample of ring lengths is used.

**3. Exact Rule 105 resonance.** Over \(\mathbb F_2\), Rule 105 is the affine map \(F(x)=Lx+\mathbf1\), where \(L=S^{-1}+1+S\) and \(S\) is cyclic spatial shift. Since \(L\mathbf1=\mathbf1\), one has \(F^3(x)=L^3x+\mathbf1\). Identify cyclic words with \(R_n=\mathbb F_2[s]/(s^n-1)\) and let \(J=1+s+\cdots+s^{n-1}\). Then fixed points satisfy \((s+1)^2x=sJ\), while configurations returning after three steps satisfy
\[
(s+1)^2\Phi_5(s)x=s^3J,\qquad \Phi_5(s)=1+s+s^2+s^3+s^4.
\]
Indeed \(L+1=s^{-1}(s+1)^2\) and \(L^2+L+1=s^{-2}\Phi_5(s)\).

For any polynomial \(P\), a congruence \(Px\equiv J\pmod {s^n-1}\) is solvable exactly when \(\gcd(P,s^n-1)\) divides \(J\), and then it has \(2^{\deg\gcd(P,s^n-1)}\) solutions. Write \(n=2^a m\) with \(m\) odd. In characteristic two, \(s^n-1=(s^m-1)^{2^a}\); the factor \(s+1\) has multiplicity \(2^a\), and \(\Phi_5\), irreducible of degree four, divides \(s^m-1\) exactly when \(5\mid m\). The polynomial \(J\) has multiplicity \(2^a-1\) at \(s+1\) and multiplicity \(2^a\) at \(\Phi_5\) when present. Therefore both fixed-point and third-return equations are solvable exactly when \(a\ge2\), i.e. \(4\mid n\). When solvable, the fixed-point equation has \(2^2=4\) solutions and the third-return equation has \(2^{2+4\mathbf1_{5\mid n}}\) solutions. Subtracting the four fixed states gives exactly 60 least-three-period states when \(20\mid n\), and zero otherwise. Division by three gives exactly 20 primitive temporal orbits.

## Verification

Run `python3 verify_windows.py`, `python3 verify_spacetime.py`, and `python3 verify_rule105.py` from this directory. Their exact captured outputs are `windows_output.json`, `spacetime_output.json`, and `rule105_output.json`. The two full-classification programs return identical `minimum_ring_length` arrays of 256 entries; the first includes an explicit 20-bit Rule 105 witness. The polynomial program independently checks Rule 105's counts at lengths 1 through 240, while the algebraic proof establishes the statement for *all* lengths. `minimum_lengths.csv` is the complete classification table. The certificates use only Python's standard library.

## Relationship to prior work

Wolfram (1983) introduced the systematic elementary-rule framework. Banks and Djirar (1992) developed finite overlap graphs for fixed points and spatial shift cycles; their graph method is a predecessor to the present finite construction, not a 256-rule minimal temporal-three witness classification. Schüle and Stoop (arXiv:1107.2080, originally 2011) classify elementary automata by topological sensitivity, equicontinuity and chaos, rather than this finite-ring minimum. Koller and Hudcová (arXiv:2508.09768, 2025) develop general transfer matrices for short trajectories and cycle lengths, including length three; their inspected paper gives entropy calculations for representative rule classes, not the uniform sharp length-20 criterion or the exact Rule 105 congruence. Epperlein (2015) develops general temporal-period-point methods; only its abstract and bibliographic descriptions were accessible, so any overlap with its unpublished-in-this-inspection detailed results remains a historical-priority risk. Existing exact temporal-three results for individual rules (including Rule 62) do not logically imply a sharp all-rule bound. General algorithmic formalisms are credited, not claimed new.

## Limitations

The result classifies existence and *smallest ring size* of primitive temporal three-cycles, not their exact counts for all rules at all lengths, nor higher temporal periods. The 256-rule table is a finite exhaustive certificate, accompanied by two distinct implementations, not an external formal-verification proof. Rule 105's all-length orbit count is supported separately by a polynomial proof. No claim of absolute historical novelty or independent mathematical review is made. The full article by Epperlein (2015) could not be inspected in this investigation; a matching exact table or bound there would supersede the originality assessment.

## References

1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* **55** (1983), 601; https://doi.org/10.1103/RevModPhys.55.601 (published 1983-07-01).
2. S. P. Banks and S. Djirar, “Fixed Points and Shift Cycles in Cellular Automata,” ACSE Research Report 459 (1992); https://eprints.whiterose.ac.uk/id/eprint/79286/.
3. M. Schüle and R. Stoop, “A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata,” arXiv:1107.2080; https://arxiv.org/html/1107.2080v8.
4. J. Epperlein, “Classification of Elementary Cellular Automata Up to Topological Conjugacy,” *AUTOMATA 2015*, LNCS **9099**, 99–112; https://doi.org/10.1007/978-3-662-47221-7_8.
5. C. Koller and B. Hudcová, “Counting Short Trajectories in Elementary Cellular Automata using the Transfer Matrix Method,” arXiv:2508.09768 (2025); https://arxiv.org/abs/2508.09768.
