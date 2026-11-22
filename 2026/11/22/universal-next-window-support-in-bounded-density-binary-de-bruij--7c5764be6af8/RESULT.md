# Universal next-window support in bounded-density binary de Bruijn cycles

## Finding
Fix integers \(n\ge 1\) and \(1\le k\le n\). Write \(\mathcal B_{n,k}=\{x\in\{0,1\}^n:\operatorname{wt}(x)\le k\}\), and let \(\mathcal U_{n,k}\) be the family of oriented circular words whose cyclic length-\(n\) factors consist of **every** member of \(\mathcal B_{n,k}\) exactly once. The existence of such universal cycles is classical. For any such cycle, count length-\(n+1\) factors cyclically, and take the **union** of their supports over all cycles in \(\mathcal U_{n,k}\).

A binary word \(w\) of length \(n+1\) is **locally admissible** if its first and final length-\(n\) factors both have weight at most \(k\). Among locally admissible words, precisely the following are absent from *every* cycle:

* For every \(n,k\): \(0^{n+1}\) and \(1\,0^{n-1}1\).
* Additionally, if \(k\ge2\) and \(k\mid n\): \(0v0\) and \(1v1\), where \(d=n/k\) and
  \[
  v=0^{d-1}(1\,0^{d-1})^{k-1}.
  \]

No other locally admissible word is universally absent. In particular, there are exactly two forbidden locally admissible next-windows when \(k\nmid n\) or \(k=1\), and exactly four otherwise. If \(S_{n,k}\) denotes the union support, its cardinality is
\[
\boxed{\ |S_{n,k}|=\sum_{j=0}^{k}\binom{n+1}{j}+\binom{n-1}{k-1}-2-2\mathbf1_{\{k\ge2,\ k\mid n\}}\ }.
\]
The words \(0v0\) and \(1v1\) are distinct from the first two exceptions when \(k\ge2\), so no duplicate subtraction occurs. The endpoint \(n=k\) specializes to the four classically forced omissions for ordinary binary de Bruijn cycles.

## Assumptions and scope
Words are binary, the alphabet symbols are distinguished, and Hamming weight counts ones. A universal cycle has length \(\sum_{j=0}^{k}\binom nj\) and is understood up to circular rotation, **not** complementation or reversal. The cyclic next-windows are overlapping factors of length \(n+1\) in its periodic extension, and can exceed the cycle circumference. The claimed support is a union over all such cycles, not a claim that one particular cycle contains every permitted next-window. A length-\(n+1\) word that fails local admissibility is impossible for the immediate trivial reason that an illegal length-\(n\) factor would appear. The substantive classification concerns locally admissible words only, including the cases \(n=k\), \(k=1\), and \(n=1\).

## Proof
**1. The overlap graph and transition types.** Let \(G\) be the directed edge-labeled overlap graph whose edges are the binary words of length \(n\) and weight at most \(k\), from their length-\(n-1\) prefixes to their corresponding suffixes. All vertices are the words of length \(n-1\) and weight at most \(k\). Append zeros to reach the zero vertex from any vertex, and append a target word's bits from the zero vertex to reach that vertex. Therefore \(G\) is strongly connected. At a vertex \(v\) with \(\operatorname{wt}(v)<k\), the two incoming edges are \(0v,1v\) and the two outgoing edges are \(v0,v1\). If \(\operatorname{wt}(v)=k\), only \(0v\) and \(v0\) occur. Consequently \(G\) is balanced and Eulerian, and universal cycles correspond to its edge-distinct Euler circuits.

At a two-in/two-out vertex \(v\), an Euler circuit pairs arriving edges with departing edges either in the **rotation pairing**
\[
0v\longmapsto v0,\qquad 1v\longmapsto v1,
\]
or in the **cross pairing**
\[
0v\longmapsto v1,\qquad 1v\longmapsto v0.
\]
At a one-in/one-out vertex the pairing is forced. A locally admissible next-window is just a pair of consecutive distinct directed edge labels in an Euler circuit. (If two consecutive labels happened to be the same, the unique edge would need to be used twice; this is excluded automatically by the classification below.)

**2. The necklace connection graph.** For each length-\(n\) binary rotation class (necklace) with weight at most \(k\), form a vertex of an undirected *multigraph* \(H\). For every length-\(n-1\) word \(v\) with \(\operatorname{wt}(v)<k\), add an edge labeled \(v\) from necklace \([0v]\) of weight \(\operatorname{wt}(v)\) to necklace \([1v]\) of weight \(\operatorname{wt}(v)+1\). These two necklace vertices are distinct because their weights differ; parallel edges are retained. Each positive-weight necklace has an edge downward to a strictly lower-weight necklace: rotate it so a selected one is first and replace that one with zero. Hence \(H\) is connected by repeated downward steps to the all-zero necklace.

Under rotation pairings at every vertex of \(G\), the edge set splits into one directed cycle per necklace. Changing the pairing at vertex \(v\) swaps two successors belonging to the different necklace cycles \([0v]\) and \([1v]\). Thus, starting with all rotation pairings and changing precisely the edges of **any** spanning tree of \(H\), we merge previously disjoint directed cycles one tree edge at a time, obtaining one Euler circuit. As a consequence, a cross pairing at every specified \(v\) is realizable: choose a spanning tree containing its edge. A rotation pairing at \(v\) is realizable exactly when the corresponding edge is **not a bridge** of \(H\): if it is not a bridge, choose a spanning tree avoiding it; if it is a bridge, any set of switches joining all initial necklace cycles must use it, since the switches define connections along the edges of \(H\). Therefore the universally absent locally admissible next-windows are exactly \(0v0\) and \(1v1\) for edges \(v\) that are bridges of \(H\).

**3. The complete bridge classification.** For a necklace \(Y\) of weight \(m>0\), consider its incident edges going to weight \(m-1\). Each is obtained by selecting a one in a representative of \(Y\) and changing that one to zero. Distinct downward edges are indexed by the orbits of one positions under the rotational stabilizer of \(Y\). Hence their number \(\delta(Y)\) equals the number of ones in the primitive period of \(Y\). In particular, \(\delta(Y)=1\) if and only if \(m\mid n\) and \(Y\) is the necklace of the evenly spaced word \((1\,0^{d-1})^m\) with \(d=n/m\).

Fix an edge \(e\) from a necklace \(X\) of weight \(m-1\) upward to \(Y\) of weight \(m\). If \(\delta(Y)\ge2\), there is another downward edge \(e'\) from \(Y\) to a necklace \(X'\) of weight \(m-1\). The induced subgraph on necklaces of weights at most \(m-1\) is connected by downward moves, so a route from \(X'\) to \(X\) together with \(e'\) avoids \(e\). This remains true if \(e'\) is a distinct parallel edge. Therefore \(e\) cannot be a bridge.

Suppose instead \(\delta(Y)=1\). If \(m=1\), then \(X=[0^n]\) has degree one in \(H\); hence \(e\) is a bridge. If \(m=k\), then \(Y\) has no upward edges and its only downward edge is \(e\); again \(e\) is a bridge. For the remaining case \(2\le m<k\), the equally spaced ones in \(Y\) have separation \(d=n/m\ge2\). Insert an extra one immediately after one existing one, producing a necklace \(Z\) of weight \(m+1\). Delete one of the original ones, retaining the added one, to produce a necklace \(Y'\) of weight \(m\) with unequal cyclic gaps, so \(Y'\ne Y\). Deleting the extra one from \(Y'\) produces precisely the original necklace \(X\) (the result of deleting one of the uniformly spaced original ones). Consequently the three edges \(Y-Z-Y'-X\) form a detour avoiding \(e\). (Their existence follows from the one-bit insertions/deletions defining \(H\).) Thus this case also is not a bridge.

The only bridges are therefore the unique edge out of the all-zero necklace (label \(v=0^{n-1}\)) and, if \(k\ge2\) divides \(n\), the unique downward edge of the top-weight evenly spaced necklace, labeled
\[
v=0^{d-1}(1\,0^{d-1})^{k-1},\qquad d=n/k.
\]
When \(k=1\), these descriptions refer to the *same* edge and are not counted twice.

**4. Translate back and count.** Step 2 shows that each bridge forbids exactly the two rotation-pair next-windows \(0v0\) and \(1v1\), and that all cross-pair next-windows and all rotation pairs at nonbridges occur in some universal cycle. Step 3 gives the two-or-four list in the Finding, including \(n=1\), where \(H\) has two necklace vertices and one bridge.

Finally, locally admissible length-\(n+1\) words either have weight at most \(k\), giving \(\sum_{j=0}^k\binom{n+1}{j}\), or have weight \(k+1\), in which case both endpoint bits must be one and the interior must have weight \(k-1\), giving \(\binom{n-1}{k-1}\). Subtracting two windows per bridge yields the stated exact support formula. This completes the proof for every allowed pair \((n,k)\).

## Verification
Run `python3 verify.py` in the same directory. Two mathematically distinct finite checks are implemented: (i) construction of the undirected necklace multigraph followed by a Tarjan bridge test for all \(n\le13\) and \(k\le\min(n,6)\); (ii) direct directed-overlap Euler feasibility by contracting *each* candidate consecutive edge pair and testing strong connectivity, for every \(n\le9\) and every \(1\le k\le n\). They independently agree with both the forbidden list and the support-size formula. Expected final line: `VERIFY_OK`. These are finite corroborations; the preceding bridge argument, not extrapolation from finite data, proves the all-length theorem.

## Relationship to prior work
Sawada, Stevens and Williams (2011) construct maximum-density binary de Bruijn cycles for every order and weight bound; the existence theorem is theirs, not a new contribution. Sawada, Williams and Wong (2013) provide weight-range universal cycles through gluing, establishing further constructive background. Sawada, Williams and Wong (2016) study greedy and necklace constructions for broad languages. Known universal-cycle enumerations at weight at most two (2026) classify the cycles for that small bound, and the ordinary unrestricted de Bruijn case has known four next-window exclusions. The present assertion concerns **the union of all admissible next-window supports** across every maximum-density cycle, including its sharp divisibility transition at every \(k\), not the count of cycles, the existence of a particular cycle, or the unrestricted endpoint alone.

## Limitations
The family is restricted to binary factors of bounded Hamming weight; the result does not assert the number of cycles realizing a given window or the intersection of next-window supports across cycles. The complete union-support classification does not determine a full joint transition distribution. Mathematical priority is assessed against the inspected literature and searches; an earlier equivalent formulation in unindexed treatments of necklace-joining remains possible. Independent external mathematical audit has not been performed.

## References
1. J. Sawada, B. Stevens, A. Williams, *De Bruijn Sequences for the Binary Strings with Maximum Density*, WALCOM 2011, Lecture Notes in Computer Science 6552, pp. 182–190. Springer proceedings eBook published February 10, 2011. Full text: https://www.socs.uoguelph.ca/~sawada/papers/max_density.pdf ; book metadata: https://link.springer.com/book/10.1007/978-3-642-19094-0
2. J. Sawada, A. Williams, D. Wong, *Universal Cycles for Weight-Range Binary Strings*, IWOCA 2013. Full text: https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf
3. J. Sawada, A. Williams, D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, Electronic Journal of Combinatorics 23(1), #P1.24 (2016), published February 5, 2016. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p24/pdf/
4. Earlier published universal-cycle studies of weight-at-most-two binary windows and next-order factor support in unrestricted binary de Bruijn cycles; these special cases are not claimed as new.
