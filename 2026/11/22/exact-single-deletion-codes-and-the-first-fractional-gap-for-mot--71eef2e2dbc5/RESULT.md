# Exact single-deletion codes and the first fractional gap for Motzkin excursions

## Finding

For each integer \(1\le n\le7\), let \(\mathcal M_n\) be the Motzkin excursions of length \(n\) over \(\{U,D,F\}\): the path height starts at zero, rises on `U`, falls on `D`, stays constant on `F`, is never negative and ends at zero. Let \(M_n\) be the largest set of such words correcting one arbitrary deletion; let \(P_n\) be the optimum of the usual deletion-shadow fractional packing program; and let \(N_n\) count distinct maximum codebooks on the labeled coordinate positions and labeled alphabet.

| \(n\) | \(|\mathcal M_n|\) | \(M_n\) | \(P_n\) | \(N_n\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 2 | 2 | 1 |
| 3 | 4 | 2 | 2 | 3 |
| 4 | 9 | 4 | 4 | 8 |
| 5 | 21 | 6 | 6 | 75 |
| 6 | 51 | 14 | 14 | 28 |
| 7 | 127 | 25 | \(382/15\) | 142560 |

Thus the natural fractional packing relaxation has zero objective gap \(P_n-M_n\) through length six and its first strict objective gap at length seven:
\[
P_7-M_7=\frac7{15}>0.
\]
The rounded upper bound at length seven is still tight: \(\lfloor P_7\rfloor=M_7=25\). No integer-rounding failure is asserted. Equality of objectives does not imply that the packing polytope is integral: it has a fractional vertex already at length four.

## Assumptions and scope

An output of a source word \(w\) is any distinct word obtained by deleting exactly one coordinate (including deletions producing a non-Motzkin word). Write \(\Delta(w)\) for that set; distinct source words \(v,w\) are compatible precisely when \(\Delta(v)\cap\Delta(w)=\varnothing\). All excursions in a code have equal length \(n\). The channel does not reveal the deleted coordinate. Since source and one-deletion outputs have different lengths, the results also apply to allowing *zero or one* deletion. The fractional program has one variable \(x_w\ge0\) per source and one inequality \(\sum_{w:y\in\Delta(w)}x_w\le1\) per distinct deletion output \(y\).

## Proof

**Layer decomposition.** Every excursion has equal numbers \(t\) of `U` and `D`. After one deletion, its output has counts \((t-1,t)\), \((t,t-1)\), or \((t,t)\) for (`U`,`D`), depending on whether `U`, `D`, or `F` was removed. Therefore \(t\) is determined by \(\max(\#U,\#D)\) in the received word. Distinct \(t\)-layers have disjoint received-word sets, so their integer optima add, their fractional optima add, and their numbers of optimal codebooks multiply.

**Matching exact lower and upper certificates.** The attached `certificates.json` contains a separate sparse, exact rational primal assignment, exact rational output-price dual assignment and explicit integer codebook for *each* \((n,t)\) with \(1\le n\le7\) and \(0\le t\le\lfloor n/2\rfloor\). Every primal variable is nonnegative and each deletion output has incoming primal mass at most one. Every dual output price is nonnegative and each source word sees dual price at least one. The total primal and dual objectives agree exactly, proving the fractional optimum for each layer by weak duality. Each listed integer codebook has pairwise disjoint deletion shadows. For every layer, its size \(m\) satisfies \(m\le P<m+1\). Hence it is an *integer-optimal* codebook: no larger integer code exists.

**Complete optimizer count.** To count all integer optima, construct the graph on each layer with an edge between two words when their deletion shadows are disjoint. The exact bit-mask Bron–Kerbosch search in `verify.py` uses a pivot and prunes a branch only when the current clique plus all remaining candidate vertices is smaller than the best already found. Every maximum clique is maximal, and no maximum clique can be pruned by this bound. The independently implemented include/exclude dynamic recursion of `verify_independent.py` counts all maximum independent sets of the complementary incompatibility graph, giving the same counts. The layer-wise counts at \(n=7\) are \(1,9,11,1440\) and capacities \(1,5,14,5\) for \(t=0,1,2,3\). Their product is \(142560\), while their sum is \(25\). Their fractional optima are respectively \(1,5,217/15,5\), summing to \(382/15\). The shorter-length totals appear in the table.

**A fractional vertex at length four.** Take \(u=\texttt{FUFD}\), \(v=\texttt{FUDF}\), and \(w=\texttt{UFDF}\). Their deletion shadows intersect pairwise but have no common word: the three pairwise intersections, in the order \((u,v),(u,w),(v,w)\), are \(\{\texttt{FUD},\texttt{FUF}\}\), \(\{\texttt{UFD}\}\), and \(\{\texttt{FDF},\texttt{UDF}\}\). Assign each of \(u,v,w\) weight \(1/2\) and all other words weight zero. Each output receives mass at most one. On the face fixing the other coordinates to zero, the three pairwise capacity equalities are tight and uniquely determine these three weights. The assignment is therefore a vertex of the full polytope. This does not affect its optimum for the objective \(\sum_v x_v\).

All logical implications above are finite and exact; there is no unverified extrapolation to larger \(n\).

## Verification

Save `certificates.json`, `verify.py` and `verify_independent.py` in the same directory. Run `python3 verify.py` for exhaustive maximal-clique counts, exact rational primal/dual constraints and witness validation; it prints `VERIFY_OK`. Independently run `python3 verify_independent.py` for a distinct exhaustive source generator and memoized independent-set recursion; it prints `ALTERNATE_OK`. Both use only the Python standard library and integer arithmetic (the first also uses exact fractions). These programs enumerate every admissible source of each length, every distinct one-deletion output and all maximum compatible selections. The public certificate is not a numerical solver transcript; the verifier checks each constraint and equality on the supplied rational weights.

## Relationship to prior work

Kulkarni and Kiyavash (2012) express arbitrary constrained-source deletion correction as hypergraph matching and use fractional matching/covering upper bounds. Their theory justifies the framework but does not give the Motzkin-instance capacities, optimizer populations or first strict relaxation gap in this table. Oste and Van der Jeugt (2015) develop enumeration and recurrence relations for Motzkin paths but do not analyze deletion-correcting codebooks. Stanovnik, Moškon and Mraz (2024) analyze *non-overlapping* codes, a prefix/suffix constraint, including Motzkin-based constructions; that condition is not equivalent to disjoint deletion shadows, and their optimization problems do not imply this table.

## Limitations

The complete census concerns only lengths one through seven; it gives neither an all-length formula nor asymptotic capacity. The statement of novelty is qualified by the possibility of unindexed equivalent historical enumerations. Exactness of the reported finite counts is supported by the supplied exhaustive recursions and exact rational certificates. The definition of a deletion output is a *set* of distinct words, not a multiset of deletion positions.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, first public 2012-11-13, https://arxiv.org/abs/1211.3128 .
2. R. Oste and J. Van der Jeugt, *Motzkin Paths, Motzkin Polynomials and Recurrence Relations*, Electron. J. Combin. 22(2), P2.8, 2015, https://doi.org/10.37236/4781 .
3. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92, 1299–1326, 2024, https://doi.org/10.1007/s10623-023-01344-z .
