# A zero-entropy phase transition for the first two binary Abelian-cube periods

## Finding

Let \(\Sigma=\{0,1\}\). For each integer \(n\ge0\), let \(L_n\subseteq\Sigma^n\) consist of the **indexed linear words** without any factor \(XYZ\) such that \(|X|=|Y|=|Z|=p\in\{1,2\}\) and \(X,Y,Z\) have the same Parikh vector (the same number of ones). Denote \(a_n=|L_n|\). Then

\[
(a_0,a_1,\ldots,a_7)=(1,2,4,6,10,16,18,12),
\qquad a_n=10+2\mathbf{1}_{3\mid n}\quad(n\ge8).
\]

The complete generating function is
\[
\sum_{n\ge0}a_nz^n=
1+2z+4z^2+6z^3+10z^4+16z^5+18z^6+12z^7
+\frac{10z^8}{1-z}+\frac{2z^9}{1-z^3}.
\]

The two-sided shift of all bi-infinite words with the same avoidance requirement consists of **exactly six points**: the three shifts of \((001)^{\mathbb Z}\) and the three shifts of \((011)^{\mathbb Z}\). Hence its topological entropy is \(0\). For each \(n\ge8\), the finite words split into six all-cycle paths, two initial-entrance paths, two final-exit paths, and two entrance-to-exit paths when \(3\mid n\); these groups are disjoint and exhaustive.

## Assumptions and scope

An Abelian cube of period \(p\) is a factor \(XYZ\) of length \(3p\) with \(p\ge1\), where the three blocks are anagrams. Only periods \(1\) and \(2\) are forbidden here; cubes of period \(3\) or larger are **allowed**. Words are linear and labeled, not necklaces. The empty word is included once. Entropy refers to the associated two-sided subshift, equivalently the exponential growth rate of its finite admissible factors; the exact finite-word counts also have exponential rate zero.

## Proof

**1. The exact forbidden-window reduction.** A period-one Abelian cube is `000` or `111`. A period-two Abelian cube consists of three consecutive two-letter blocks, each with equally many ones. If the common count is zero or two, it already contains `000` or `111`. Otherwise each block is `01` or `10`. Therefore a word avoids both forbidden periods if and only if it avoids `000`, `111`, and every six-letter concatenation from \(\{01,10\}^3\). This gives a complete finite-type presentation of memory five.

**2. Complete overlap graph.** There are precisely sixteen binary five-letter words avoiding `000` and `111`. For each such word, append a bit only if the resulting six-letter word passes the preceding test, then shift left by one. The complete directed adjacency table is:

| State | Successor states |
|---|---|
| `00100` | `01001` |
| `00101` | `01010`, `01011` |
| `00110` | `01100`, `01101` |
| `01001` | `10010`, `10011` |
| `01010` | `10100` |
| `01011` | none |
| `01100` | none |
| `01101` | `11011` |
| `10010` | `00100` |
| `10011` | none |
| `10100` | none |
| `10101` | `01011` |
| `10110` | `01100`, `01101` |
| `11001` | `10010`, `10011` |
| `11010` | `10100`, `10101` |
| `11011` | `10110` |

Each row follows directly by checking its two possible appended bits against the two forbidden-window conditions. The only directed cycles are the two disjoint three-cycles
\[
00100\to01001\to10010\to00100,
\qquad
01101\to11011\to10110\to01101.
\]
There are exactly two distinct entry edges into these cycles from outside, \(11001\to10010\) and \(00110\to01101\), and exactly two exit edges to terminal states, \(01001\to10011\) and \(10110\to01100\). The remaining transient-only paths have at most two edges and therefore generate no word of length at least eight (which requires at least three edges from a five-letter state).

**3. All-length path census.** Every word of length \(n\ge5\) corresponds bijectively to a path of length \(n-5\) starting at any of these sixteen states. For \(n\ge8\), the only such paths are: (i) six cycle-only paths (one for each of the six cycle phases); (ii) two paths taking an entry edge and then remaining on a cycle; (iii) two paths leaving a cycle on their last edge; and (iv) possibly two paths taking both an initial entry edge and a final exit edge. In case (iv), each entry-to-exit path has four edges plus a multiple of the three-edge cycle length, so this path is possible exactly when \(n-5\equiv1\pmod3\), namely when \(3\mid n\). All paths are disjoint by their starting and ending states. This proves the stated formula for every \(n\ge8\).

For \(0\le n\le4\), direct exclusion of `000` and `111` gives the values \(1,2,4,6,10\). There are sixteen allowed five-letter words, eighteen edges, and twelve paths of length two, yielding \(a_5=16,a_6=18,a_7=12\). Summing the resulting sequence yields the rational series above.

**4. Two-sided rigidity.** A bi-infinite path in this finite graph must remain on a directed recurrent component in both time directions. The table has only the two three-cycles, with no directed connection between them; all other vertices lie on finite transient paths. Thus there are precisely six bi-infinite admissible sequences and their entropy is zero. The two periodic binary patterns correspond to \((001)^\mathbb Z\) and \((011)^\mathbb Z\).

## Verification

Two standalone Python 3 standard-library programs accompany the result. `graph_checker.py` constructs the states and all edges directly from the Abelian-cube definition, asserts the complete displayed adjacency table, and checks the transfer recurrence for lengths five through five hundred. `bruteforce_checker.py` independently enumerates all binary words of lengths zero through nineteen using direct factors, and checks the exact formula. Both programs completed successfully. The all-length proof is the finite adjacency-table decomposition above; these computations check its implementation and the small boundary cases, not an extrapolation to infinitely many lengths.

## Relationship to prior work

Huova and Karhumäki (2011) introduced closely related \(k\)-Abelian repetition avoidance questions. Rao and Rosenfeld (2014 preprint; later revised) state that every binary word longer than nine contains some Abelian cube and establish that avoiding all cubes of period at least two is impossible in an infinite binary word. Their statements concern different forbidden-period sets and do not give the present exact language for *only* periods one and two. Rao's work on \(2\)-Abelian-cube avoidability and Mercaş–Saarela's work on \(5\)-Abelian-cube avoidability concern stronger equivalence requirements, not a restriction to short ordinary Abelian block lengths. The known nine-letter ceiling for **unrestricted** Abelian-cube avoidance is not claimed as new here.

## Limitations

The theorem treats only the binary alphabet and the first two block periods. It does not count words avoiding Abelian cubes of all periods, and it does not address \(k\)-Abelian equivalence. An earlier unindexed characterization of the same forbidden-factor shift or a general theorem implicitly giving this exact state graph remains a possible historical priority issue. Independent verification by a separate mathematician has not been performed.

## References

1. M. Huova and J. Karhumäki, *Observations and Problems on k-abelian avoidability* (first public arXiv version 2011-04-21), https://arxiv.org/abs/1104.4273.
2. M. Rao and M. Rosenfeld, *Avoidability of long k-abelian repetitions* (public 2014 preprint), https://jm2014.sciencesconf.org/44432/Rao_Rosenfeld_JM2014.pdf; revised https://arxiv.org/abs/1507.02581.
3. M. Rao, *On some generalizations of abelian power avoidability* (2014 preprint), https://perso.ens-lyon.fr/michael.rao/publi/kab.pdf.
4. R. Mercaş and A. Saarela, *5-Abelian cubes are avoidable on binary alphabets* (2014), https://www.numdam.org/item/10.1051/ita/2014020.pdf.
