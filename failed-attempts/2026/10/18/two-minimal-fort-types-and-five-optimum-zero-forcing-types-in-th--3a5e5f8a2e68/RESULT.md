# Two minimal-fort types and five optimum zero-forcing types in the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane. Exactly \(70\) inclusion-minimal forts exist, forming two orbits of sizes \(14\) and \(56\) under its full automorphism group of order \(336\). The first orbit consists of the fourteen one-sided quadrangles (the complement of a line in either bipartition); the second consists of fifty-six mixed seven-vertex forts, each inducing three disjoint edges and one isolated vertex. Every nonempty fort contains one of these seventy obstructions.

The complete ordinary zero-forcing polynomial is
\[
\mathcal Z_H(z)=700z^{6}+1904z^{7}+2401z^{8}+1862z^{9}+987z^{10}+364z^{11}+91z^{12}+14z^{13}+z^{14}.
\]
In particular, exactly \(8324\) subsets are zero forcing. All inclusion-minimal zero-forcing sets have size \(6\), so \(H\) is well-forced. The \(700\) minimum sets form five automorphism orbits of sizes \(28,168,168,168,168\). Exactly \(196\) such sets force in two simultaneous rounds, and the remaining \(504\) force in three rounds.

## Assumptions and scope

Vertices are seven points \(p_a\), indexed by nonzero vectors \(a\in\mathbb F_2^3\), and seven lines \(\ell_L\), indexed by the seven triples \(L=\{a,b,a\oplus b\}\), with incidence given by \(a\in L\). The seven line triples, in canonical lexicographic order, are \(123,145,167,246,257,347,356\). In computation, points occupy indices \(0,\ldots,6\) (labels \(1,\ldots,7\)), and lines indices \(7,\ldots,13\) in that order.

An ordinary zero-forcing seed \(S\subseteq V(H)\) initially colors exactly \(S\) black. In each synchronous round every black vertex with exactly one white neighbor forces that neighbor black. A set \(S\) is zero forcing if this process colors all vertices. A fort is a nonempty set \(F\subseteq V(H)\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is inclusion-minimal when it contains no *proper, nonempty fort*. A zero-forcing set is inclusion-minimal if no smaller zero-forcing set is contained in it. The orbit and propagation-time claims are specific to this fourteen-vertex graph, not all Steiner triple-system incidence graphs.

## Proof

**Fort equivalence.** A seed \(S\) fails to force all vertices exactly when its complement contains a fort. Indeed, at the terminal closure of the forcing process, the nonempty set \(W\) of uncolored vertices has no vertex outside \(W\) with exactly one neighbor in \(W\), so \(W\) is a fort. Conversely, if \(F\) is a fort disjoint from \(S\), induction on successive forcing rounds shows that no vertex in \(F\) can be the first one colored: at the first such step the forcing vertex outside \(F\) would have exactly one neighbor in \(F\). Thus a seed is zero forcing exactly when it meets every inclusion-minimal fort.

**Exhaustive finite classification.** The standalone program `verify_forcing.py` builds the fourteen labeled vertices from the seven XOR-zero triples. For every one of \(2^{14}=16384\) vertex masks, it computes the exact ordinary forcing closure by simultaneous updates. It separately checks the fort predicate by testing the number of neighbors in each candidate fort from every outside vertex. Inclusion-minimal forts are identified with the exact recurrence
\[
B(F)=\bigvee_{v\in F}\bigl(\mathrm{fort}(F\setminus\{v\})\lor B(F\setminus\{v\})\bigr),
\]
with \(B(\varnothing)=\mathrm{false}\); a fort is inclusion-minimal precisely when \(B(F)\) is false. This recurrence tests whether *any proper subset* is a fort, not merely whether any immediate deletion is one. The resulting seventy minimal forts comprise fourteen of size four and fifty-six of size seven; their orbit representatives and canonical incidence data appear in `heawood_certificate.json`.

The same exhaustive closure computes the displayed zero-forcing polynomial. Monotonicity of zero forcing under enlarging the initial set means that single-vertex deletions do suffice to test inclusion-minimality of a zero-forcing set. This yields precisely seven hundred inclusion-minimal sets, all of size six; their synchronous propagation times have counts \(196\) and \(504\).

**Complete symmetry.** The incidence graph is connected and bipartite, so each automorphism preserves or exchanges its two bipartition classes. Class-preserving automorphisms act on Fano points by all \(168\) members of \(\mathrm{GL}(3,2)\), since the third point of a line through two distinct points is their vector sum; every class-preserving point map therefore preserves addition. The polarity identifying a point with the line orthogonal to it exchanges the two classes. Hence \(|\operatorname{Aut}(H)|=336\). The program enumerates these transformations, checks all adjacency images, and exhausts the two fort orbits and five forcing orbits. The resulting orbit sizes sum to \(70\) and \(700\), respectively, with propagation time constant on each forcing orbit.

**Independent exhaustive method.** `verify_forts.py` constructs the same incidence graph using a different representation: a point vector is adjacent to a line normal exactly when their binary scalar product vanishes. It finds minimal forts by explicitly checking *all* proper submasks and counts zero-forcing sets by hitting those forts. It also performs a separate direct forcing simulation for each of the \(16384\) masks, confirming agreement for every seed. The two methods reproduce the same polynomial and minimality counts; the certificate representatives are converted and checked in the second incidence representation.

## Verification

With Python 3.10 or later, from the directory containing the files, run:

```
python3 verify_forcing.py heawood_certificate.json
python3 verify_forts.py heawood_certificate.json
```

Expected independently checked totals are \(16384\) initial masks, \(8324\) zero-forcing masks, \(70\) minimal forts in two symmetry orbits, and \(700\) minimum and inclusion-minimal zero-forcing masks in five symmetry orbits. The direct program counts \(196\) two-round and \(504\) three-round minimum configurations. Both verifiers require only the Python standard library. The certificate is embedded in the same package; no unseen datasets or previous computational output are dependencies.

## Relationship to prior work

Barioli *et al.* (2010, arXiv:1003.2028) establish the ordinary zero-forcing framework. Deaett and Hall (2017, arXiv:1708.07741) discuss the Heawood graph's rank and zero-forcing bounds and obtain a positive-semidefinite minimum-rank result; their previously discussed ordinary minimum-rank/forcing-number information is not being claimed as new here. Brimkov, Fast, and Hicks (arXiv:1704.02065) use forts and set-cover formulations, while Boyer *et al.* (arXiv:1801.08910) introduce the zero-forcing polynomial and treat several other graph families. Grood *et al.* (arXiv:2312.14298) investigate well-forced graphs, particularly trees. The claimed additional information is this Fano-incidence graph's complete minimal-fort obstruction system, its two full fort orbits, complete ordinary polynomial, five optimum-set orbits, and propagation-time partition. General definitions, the fact that \(Z(H)=6\), and the broader minimum-rank theory are not presented as new.

## Limitations

This is an exact, finite, computer-checkable classification for the labeled Fano incidence graph. It is not an all-orders classification of Steiner triple systems or projective planes, nor a theorem equating ordinary and positive-semidefinite zero forcing. Historical originality is not independently certified; unindexed software, tables, or supplementary classifications could already contain the specific counts. The reported propagation time uses the synchronous parallel convention, and no implication for alternative forcing rules is asserted.

## References

1. F. Barioli *et al.*, *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028 (first posted 2010-03-10), https://arxiv.org/abs/1003.2028.
2. L. Deaett and H. T. Hall, *Orthogonal representations of Steiner triple system incidence graphs*, arXiv:1708.07741 (first posted 2017-08-25), https://arxiv.org/abs/1708.07741.
3. B. Brimkov, C. C. Fast, and I. V. Hicks, *Computational Approaches for Zero Forcing and Related Problems*, arXiv:1704.02065, https://arxiv.org/abs/1704.02065.
4. K. Boyer *et al.*, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (first posted 2018-01-26), https://arxiv.org/abs/1801.08910.
5. C. Grood *et al.*, *Well-forced graphs*, arXiv:2312.14298 (first posted 2023-12-21), https://arxiv.org/abs/2312.14298.
