# Rectangular cycle products attain the monitoring lower bound

## Finding

Let \(5\le n\le m\) be arbitrary integers, and let \(G_{n,m}=C_n\square C_m\) be the Cartesian product of simple cycles. The monitoring edge-geodetic number satisfies

\[
\boxed{\operatorname{meg}(G_{n,m})=3m=3\max\{n,m\}.}
\]

In particular, the elementary Cartesian-product lower bound for this invariant is sharp for **every rectangular discrete torus**, not only the equal-circumference case. We also give an explicit optimum monitor set for every pair of lengths. The equal-length statement is previously established by Haslegrave; the added claim concerns every unequal pair.

## Assumptions and scope

All graphs here are finite, simple, undirected and unweighted. Vertices of \(C_k\) are residues \(\{0,\ldots,k-1\}\), with edges between residues differing by \(1\) modulo \(k\). A vertex pair \(u,v\) *monitors* an edge \(e\) when every shortest \(u\)-to-\(v\) path passes through \(e\); a set \(M\) is a monitoring edge-geodetic set (MEG-set) when every graph edge is monitored by some pair in \(M\). The number \(\operatorname{meg}(G)\) is the minimum cardinality of an MEG-set of \(G\).

The theorem covers all \(5\le n\le m\), without an upper bound on either parameter. It does **not** assert the corresponding equality for the strong graph product or for cycles of length three or four.

## Proof

**1. Cycle monitoring by short selected gaps.** Put \(h_k=\lfloor(k-1)/2\rfloor\). If \(X\subseteq V(C_k)\) contains at least three vertices and every cyclic gap between successive elements of \(X\) is at most \(h_k\), then \(X\) is an MEG-set of \(C_k\). Indeed, the arc associated with each such gap has length strictly less than \(k/2\), hence is the **unique** shortest path between its selected endpoints. Every edge belongs to one such arc and is therefore monitored. For any \(k\ge5\), no two vertices can monitor all edges of a cycle, as a pair monitors at most the edges of its unique shortest arc (or none when there are two opposite shortest arcs). Thus \(\operatorname{meg}(C_k)=3\); the three residues \(R_k=\{0,\lfloor k/3\rfloor,\lfloor2k/3\rfloor\}\) realize this minimum. These scalar cycle facts were previously established by Dev et al.

**2. Product fibers and the lower bound.** An edge in a fixed \(C_n\)-fiber of \(G_{n,m}\) can be monitored only by endpoints in that same fiber: if the endpoints differ in both product coordinates, the two orders of taking factorwise geodesics produce edge-disjoint shortest paths; if only the other coordinate changes, a geodesic has no edge in the desired fiber. Conversely, when both endpoints lie in a factor fiber, their product shortest paths coincide with the factor shortest paths. Therefore a set in \(G_{n,m}\) is an MEG-set if and only if its intersection with every \(C_n\)-fiber and every \(C_m\)-fiber is an MEG-set of that cycle. This fiber criterion is already proved in Haslegrave's product theorem. Since there are \(m\) distinct \(C_n\)-fibers and each requires at least three selected vertices,

\[
\operatorname{meg}(G_{n,m})\ge 3m.
\]

**3. Balanced construction.** Set \(R=\{0,\lfloor n/3\rfloor,\lfloor2n/3\rfloor\}\) in \(\mathbb Z/n\mathbb Z\), and for \(0\le j<m\) put \(q(j)=\lfloor nj/m\rfloor\). Select the cells

\[
M_{n,m}=\{(i,j):0\le i<n,\ 0\le j<m,\ i-q(j)\pmod n\in R\}.
\]

Each of the \(m\) columns \(j\) is a translate of \(R\), hence contains exactly three selected cells and is a cycle MEG-set. In particular, \(|M_{n,m}|=3m\).

To inspect a row \(i\), write \(R_i=i-R\pmod n\). This is a three-residue subset of \(C_n\) with all successive cyclic gaps at most \(d=\lceil n/3\rceil\). Since \(m\ge n\), every preimage \(q^{-1}(r)\) is a nonempty interval of columns, with first column \(\lceil rm/n\rceil\) and last column \(\lceil(r+1)m/n\rceil-1\). Treating the residue indices cyclically (and adding \(m\) to columns after wrapping), the gap between the last selected column from residue \(r\) and the first selected column from the next residue \(r+g\) is

\[
\left\lceil\frac{(r+g)m}{n}\right\rceil-
\left\lceil\frac{(r+1)m}{n}\right\rceil+1
\le \left\lceil\frac{(g-1)m}{n}\right\rceil+1
\le B(n,m):=\left\lceil\frac{(\lceil n/3\rceil-1)m}{n}\right\rceil+1.
\]

The inequality on differences of ceilings follows from \(\lceil a+b\rceil-\lceil a\rceil\le\lceil b\rceil\). Since \(\lceil n/3\rceil-1\le n/3\), we have \(B(n,m)\le\lceil m/3\rceil+1\). For every \(m\ge11\), the latter is at most \(\lfloor(m-1)/2\rfloor\): this is checked for \(m=11,12,13,14,15,16\), and increasing \(m\) by six increases the left side by two and the right side by three. For \(5\le n\le m\le10\), direct substitution into the displayed expression for \(B\) gives \(B(n,m)\le\lfloor(m-1)/2\rfloor\) **except** at \((n,m)=(5,6)\) and \((7,8)\). Thus, outside these two pairs, every cyclic gap between successive selected columns of each row is strictly smaller than \(m/2\). Each row is therefore an MEG-set of \(C_m\).

**4. The two small corrections.** In the two exceptional parameter pairs, retain the three-residue set \(R\) but replace the sequence of shifts \((q(0),\ldots,q(m-1))\) respectively by

\[
(3,2,1,2,3,4)\quad\text{for }(n,m)=(5,6),
\]
\[
(2,3,1,2,3,4,5,6)\quad\text{for }(n,m)=(7,8).
\]

Define \(M\) by the same residue test with those shifts. Every column still has three selected vertices forming a translate of \(R\). The selected column positions in rows \(i=0,1,\ldots,n-1\), respectively, are:

- For \((5,6)\): \(\{1,3,5\}\), \(\{0,2,4\}\), \(\{1,2,3,5\}\), \(\{0,1,3,4\}\), \(\{0,2,4,5\}\).
- For \((7,8)\): \(\{1,4,6\}\), \(\{2,5,7\}\), \(\{0,3,6\}\), \(\{1,2,4,7\}\), \(\{0,3,5\}\), \(\{1,2,4,6\}\), \(\{0,3,5,7\}\).

The maximum cyclic gap in these rows is respectively two and three, exactly the allowed values \(h_6\) and \(h_8\). Hence every row is also a cycle MEG-set. The fiber criterion now shows that both corrected sets monitor the entire Cartesian product. Combining these constructions with the lower bound proves the formula for all \(5\le n\le m\).

## Verification

The accompanying standard-library Python program constructs these sets independently, checks all row and column cyclic-gap constraints for 5,551 integer pairs with \(5\le n\le65\) and \(n\le m\le125\), and separately constructs eight small Cartesian-product graphs to test actual edge deletions. In the direct tests, an edge is considered monitored only when removing that edge increases the shortest-path distance between two selected probes. The actual output was:

```text
VERIFY_OK numerical_parameters=5551 direct_edge_deletion_graphs=8 columns_rows_monitored=PASS shortest_path_edge_deletions=PASS opt_lower_bound=3max
```

These are finite corroborating computations. The displayed arbitrary-parameter proof, not extrapolation from testing, establishes the unrestricted theorem. Reproduce with `python3 verify_rectangular_tori.py` (Python standard library only).

## Relationship to prior work

Dev et al., arXiv:2210.03774, introduced the monitoring edge-geodetic problem and proved that a cycle of order at least five has monitoring edge-geodetic number three. Haslegrave, arXiv:2210.08955, proved the exact Cartesian-product fiber criterion, the general lower and upper bounds, and the **square** case \(\operatorname{meg}(C_m\square C_m)=3m\). Those statements are used as existing lemmas, not reintroduced as new results. Their general bounds leave the **unequal** case within the interval from \(3\max\{m,n\}\) to \(3m+3n-9\); neither endpoint follows automatically for unequal factors. The balanced variable-rate construction above resolves that remaining natural two-parameter case.

Later work on algorithms and complexity for monitoring edge-geodetic sets (Foucaud et al., arXiv:2409.19067) addresses algorithmic and complexity results, rather than the rectangular-torus minimum formula. Searches for rectangular toroidal grids, product-cycle monitoring and the equivalent all-shortest-path edge monitoring terminology did not identify a statement covering all unequal cycle lengths. A search result alone does not establish priority.

## Limitations

Only the Cartesian product of two cycles of orders at least five is treated. The analogous optimum for the strong product may be larger and is not proved here. The explicit constructions establish a value and witnesses, not a classification or enumeration of all optimal monitoring sets. Priority remains provisional until an independent literature review; structurally equivalent formulas may exist outside the sources checked. The proof and program are not independent mathematical validation.

## References

1. S. R. Dev, S. Dey, F. Foucaud, K. Narayanan and L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774 (first posted 2022-10-07), especially the cycle theorem.
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955 (first posted 2022-10-17), especially Theorems 1 and 4; *Discrete Applied Mathematics* 340 (2023), 79–84.
3. F. Foucaud, C. Marcille, R. B. Sandeep, S. Sen and S. Taruni, *Algorithms and complexity for monitoring edge-geodetic sets in graphs*, arXiv:2409.19067 (first posted 2024-09-27); related complexity context.
