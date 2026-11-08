# The seven cyclic rotated odometers: an exact ergodic–periodic dichotomy

## Finding
For the standard von Neumann–Kakutani map \(a\) on \([0,1)\), define the cyclic translation \(R_k(x)=(x+k/7)\bmod1\), and \(F_k=a\circ R_k\), for every integer \(0\le k\le6\). Then the complete pointwise and measure-theoretic dichotomy is
\[
\operatorname{Per}(F_k)=\varnothing\quad\Longleftrightarrow\quad k\in\{0,1,4\}.
\]
For \(k\in\{2,3,5,6\}\) a nonempty interval of initial conditions is periodic. Thus (by Bruin–Lukina's general theorem) normalized Lebesgue measure is ergodic precisely for \(k\in\{0,1,4\}\). This is a classification of seven naturally defined maps, not of all seven-interval permutations.

## Assumptions and scope
The odometer \(a:[0,1)\to[0,1)\) is the half-open interval exchange
\[
a(x)=x-1+\frac{3}{2^n}\quad\text{if}\quad
1-2^{1-n}\le x<1-2^{-n},\quad n=1,2,\ldots .
\]
All endpoints use precisely these half-open conventions. For a permutation \(\pi\) of \(\{0,\ldots,6\}\), the map \(R_\pi\) takes the \(j\)th length-\(1/7\) interval by translation to the \(\pi(j)\)th. Put \(F_\pi=a\circ R_\pi\), and \(\pi_k(j)=j+k\pmod7\). The symbol “periodic” refers to equality of an exact forward iterate, not numerical near recurrence.

## Proof
**An exact 56-cell induction rule.** Partition \([0,1)\) into \(J_j=[j/56,(j+1)/56)\), \(0\le j<56\); let \(L=[0,1/8)\), the union of \(J_0,\ldots,J_6\). For the permutation \(\pi\), set \(m=8\pi(\lfloor j/8\rfloor)+(j\bmod8)\). On \(J_j\), the map \(F_\pi\) has the following exact alternatives:
\[
\begin{array}{c|c}
\text{condition}&\text{image or action}\\ \hline
m<28 & J_{m+28}\text{ by translation}\\
28\le m<42&J_{m-14}\text{ by translation}\\
42\le m<49&J_{m-35}\text{ by translation}\\
49\le m<56&x\longmapsto\frac18a(8(R_\pi(x)-7/8))\in L.
\end{array}
\]
The rigid branches follow from the first three dyadic intervals of \(a\); the final branch follows by scaling its tail on \([7/8,1)\). The formulas are identities for whole half-open intervals, including endpoints.

Starting separately from each \(J_i\subset L\), follow its deterministic rigid-cell path until the first tail branch. If the paths do not overlap and cover all 56 cells, their consecutive heights form a Kakutani–Rokhlin tower partition, and the first-return map on \(L\), after scaling by eight, is another rotated odometer \(F_{\pi'}\). Here \(\pi'(i)=m-49\) at the endpoint of the path starting from \(i\). The following complete return certificates consist of the current permutation word \(\pi(0)\ldots\pi(6)\), the seven first-return heights, the number of distinct tower cells, and the next permutation word:

| Starting translation | Current word | Heights | Tower cells | Next word |
|---|---|---|---:|---|
| \(k=0\) | `0123456` | `8,8,8,8,8,8,8` | 56 | `0123456` |
| \(k=1\) | `1234560` | `4,4,4,20,20,2,2` | 56 | `4562301` |
| \(k=1\), induced | `4562301` | `2,2,2,2,2,2,44` | 56 | `1234560` |
| \(k=2\) | `2345601` | `38,3,3,3,3,3,3` | 56 | `6012345` |
| \(k=2\), induced | `6012345` | `8,1,1,1,1,1,1` | 14 | `6012345` |
| \(k=3\) | `3456012` | `8,8,8,8,18,3,3` | 56 | `3456201` |
| \(k=3\), induced | `3456201` | `4,4,4,4,18,3,3` | 40 | `3456201` |
| \(k=4\) | `4560123` | `2,2,2,2,2,2,44` | 56 | `1234560` |
| \(k=5\) | `5601234` | `8,8,3,3,2,2,2` | 28 | `5634012` |
| \(k=6\) | `6012345` | `8,1,1,1,1,1,1` | 14 | `6012345` |

Only the 56-cell-full rows are iterated as return maps; the next permutation in an incomplete row is a formal tail-exit word, not a global induced map. The supplied standalone integer checker reconstructs every entry and verifies that every full row indeed consists of 56 distinct cells.

**The aperiodic three maps.** For \(k=0\), the complete induced permutation is again `0123456`, with every return height eight. For \(k=1\), the two full permutations `1234560` and `4562301` alternate forever; for \(k=4\), the first complete step goes to `1234560`. Every return height in these recurring states is at least two. Every point of \([0,1)\) therefore visits the nested intervals \([0,8^{-r})\) at arbitrary depths \(r\), while the least possible first-return time to the depth-\(r\) interval grows at least exponentially in \(r\). A finite periodic orbit would have to contain zero, as its finite point set intersects all these nested intervals, but then its positive return time to zero would contradict the diverging lower bound. Thus these three maps have no periodic point, including the half-open endpoints.

**Periodic intervals for the four others.** For \(k=5\), the rigid-cell graph contains a length-seven closed cycle, e.g. `16,28,40,52,22,34,46`; for \(k=6\), it contains a length-21 closed cycle, e.g. `8,28,48,26,46,24,44,22,42,20,40,18,38,16,36,14,34,54,11,31,51`. For \(k=3\), the first full return to \(L\), scaled by eight, has permutation `3456201`, whose rigid graph has the two-cell cycle `32,44`. For \(k=2\), the corresponding induced permutation is `6012345`, whose rigid graph has the above 21-cell cycle. Every rigid edge is an exact translation onto its target macrocell; traversing a closed cycle carries a whole half-open interval onto itself by a translation, hence by the zero translation. Consequently each such cycle is a nonempty interval of periodic points, in the original map in the last two cases by lifting the finite return towers.

By Bruin and Lukina, Theorem 1.4 of *Rotated odometers*, normalized Lebesgue measure is ergodic if and only if the rotated odometer has no periodic points. Combining the two directions gives the claimed seven-way measure classification.

## Verification
Run `python3 verify.py` with the Python standard library. It rebuilds the 56-edge map using integer cell arithmetic, verifies all displayed return heights and distinct-cell counts, checks the finite rigid cycles or their absence as required, and verifies exact rational branch images at cell midpoints as an independent spot check on the affine formulas. Expected terminal line: `SEVEN_ROTATIONS_EXACT_GRAPH_OK`. The mathematical proof uses the whole-cell formulas and exact finite graph induction, not the midpoint checks as a substitute for an infinite statement.

## Relationship to prior work
Bruin and Lukina introduced this family and proved the general ergodicity-versus-periodicity equivalence; this general theorem is used rather than reproved. Their paper treats seven-interval permutations in particular examples and sets up general finite induction, but the seven specific *cyclic translations* are not explicitly classified in the inspected sections. Their separate analysis of dyadic-denominator permutations is not a classification of denominator seven. Prior exact cyclic classifications for denominator five are likewise on different objects. Thus the contribution here is the seven-case, endpoint-inclusive arithmetic dichotomy, not the underlying odometer or general ergodicity criterion.

## Limitations
The seven maps are only the cyclic shifts of seven equal intervals, not all \(7!\) permutations. Although the periodic cases are shown to contain intervals of periodic points, their full periodic sets, exact individual period spectra, nonperiodic components and ergodic decompositions are not classified here. General return-induction techniques were known; this result is an exact application yielding new explicit parameter classification, not an independently new induction algorithm. Equivalent unindexed classifications remain possible. Independent assessment has not been performed.

## References
1. H. Bruin and O. Lukina, *Rotated odometers*, arXiv:2101.00868 (first publicly submitted 2021-01-04); *Journal of the London Mathematical Society* 107 (2023), 1983–2024, DOI: 10.1112/jlms.12731. In particular Sections 1, 5–7 and Theorem 1.4.
2. H. Bruin and O. Lukina, *Rotated odometers and actions on rooted trees*, arXiv:2104.05420 (2021), concerning rotations involving dyadic subinterval lengths.
