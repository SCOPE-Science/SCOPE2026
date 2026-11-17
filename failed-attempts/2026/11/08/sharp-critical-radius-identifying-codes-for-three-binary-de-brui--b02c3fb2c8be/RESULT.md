# Sharp critical-radius identifying codes for three binary de Bruijn networks

## Finding

Let \(\vec B(2,n)\) be the directed binary de Bruijn graph: its vertices are binary words of length \(n\), and there is an arc from \(a_1\cdots a_n\) to \(a_2\cdots a_n b\) for each \(b\in\{0,1\}\). A radius-\(t\) identifying code is a vertex subset \(S\) such that the closed directed **in-balls** \(B^-_t(v)\cap S\) are nonempty and pairwise distinct as \(v\) ranges over all vertices. Write \(\gamma_t(n)\) for its minimum size.

At the critical identifiable dimension \(n=2t-1\), the first three cases beyond the exceptional \(t=2\) instance achieve the universal half-vertex lower bound:

\[
\boxed{\gamma_3(5)=16,\qquad \gamma_4(7)=64,\qquad \gamma_5(9)=256.}
\]

These are exact optima for **indexed** vertices and closed incoming balls, not undirected or outgoing neighborhoods. Witnesses are recorded in `WITNESSES.json` as complete fixed-length binary inclusion bitmaps; `verify.py` verifies all vertex identifiers and all distinctness conditions.

## Assumptions and scope

For each \((n,t)\in\{(5,3),(7,4),(9,5)\}\), define the vertex labeled \(i\), with \(0\le i<2^n\), to be its ordinary \(n\)-digit binary expansion, most significant symbol first. There are loops at the all-equal vertices; balls are **closed** and use paths of length zero through \(t\). Distinct vertices are not identified under rotation. A witness inclusion bitmap \(H\) represents precisely \(S_H=\{i: \lfloor H/2^i\rfloor\bmod2=1\}\).

## Proof

**Universal lower bound.** For every binary \((n-1)\)-word \(u\), the two vertices \(u0\) and \(u1\) have the same incoming neighbors at every strictly positive path length. Indeed, a length-\(k\) predecessor for \(1\le k\le t<n\) is exactly a word whose final \(n-k\) symbols equal the first \(n-k\) symbols of its target. Those prefixes are identical for \(u0\) and \(u1\). Therefore the symmetric difference of their closed incoming balls is contained in \(\{u0,u1\}\). An identifying code must select at least one of these two vertices. There are \(2^{n-1}\) disjoint pairs, proving \(\gamma_t(n)\ge 2^{n-1}\).

**Matching constructions.** The three integer bitmaps in `WITNESSES.json` specify code sets \(S_5,S_7,S_9\) of sizes respectively \(16,64,256\). All three satisfy the stronger condition of containing **exactly one** of \(u0,u1\) for every \(u\) of length \(n-1\). The following is a complete finite proof of their identifying property, not a statistical experiment. For each target \(v\), set \(R_0(v)=\{v\}\) and recursively

\[
R_{j+1}(v)=\{a w_1\cdots w_{n-1}:a\in\{0,1\},\;w\in R_j(v)\}.
\]

Then \(B^-_t(v)=\bigcup_{j=0}^{t}R_j(v)\), directly from the graph's definition. Running `python verify.py` with the accompanying JSON file computes each of the \(32\), \(128\), or \(512\) complete sets \(B^-_t(v)\cap S_n\), asserts none is empty, and asserts all are distinct. It also independently constructs every in-ball using the suffix/prefix overlap characterization instead of the recurrence, and asserts the two calculations agree. Every finite quantifier in these three explicit cases is exhausted. The program reports `VERIFY_OK cases=3 all_vertices_and_pairs_separated`.

Consequently \(\gamma_3(5)\le16\), \(\gamma_4(7)\le64\), and \(\gamma_5(9)\le256\). Combined with the lower bound, these are equalities.

## Verification

Run with standard Python 3, from a directory containing `verify.py` and `WITNESSES.json`:

```bash
python verify.py
```

The expected `CASE` lines report \((n,t,|V|,|S|,\min_v|B^-_t(v)\cap S|)\) as \((5,3,32,16,3)\), \((7,4,128,64,4)\), and \((9,5,512,256,12)\). The program's assertions check witness size, the one-per-prefix-pair property, nonempty identification for every target, and injectivity among all identification sets. Two distinct independent derivations of the in-balls are compared for all \(672\) targets across the three graphs. These are finite exhaustive certificates for the stated cases; no extrapolation to other \(n\) or \(t\) is implied.

## Relationship to prior work

Boutin, Horan Goliber, and Pelto, *Identifying Codes on Directed De Bruijn Graphs* (public arXiv version first posted 2014-12-18, arXiv:1412.5842), give the general \(2^{n-1}\) lower bound (Theorem 3.5), prove it attainable when \(n\ge 2t\), and construct a nonminimal upper bound at the critical length \(n=2t-1\) (Theorem 3.9). Immediately after that construction they identify determining the critical-length optimum as an open problem. Their Figure 2 documents the exceptional earlier case \(\gamma_2(3)=7\). The present result closes exactly the next three binary critical-length instances, using explicit equal-half witnesses; it does not claim the general critical-length problem is solved.

The original paper is about vertex-set monitoring of network topologies, with the code acting as sensor locations. The present numerical optima directly give sharp node-monitoring costs for the three shortest as-yet-unsettled critical-radius binary overlap networks in that formulation.

## Limitations

Only alphabet size two and the three designated critical lengths are classified. No assertion is made about all \(t\ge6\), nonbinary alphabets, undirected identification, fault-tolerant identifying codes, or the number or structure of all optimal codes. The finite witness proof is rigorous for these specified sizes; its conclusion is not an asymptotic claim. Possible older or subsequently indexed equivalent critical-length constructions remain a historical-priority risk. No independent mathematical audit is claimed.

## References

1. D. Boutin, V. Horan Goliber, and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, earliest public posting 2014-12-18; journal version in *Discrete Applied Mathematics* 262 (2019), DOI:10.1016/j.dam.2019.02.005. https://arxiv.org/abs/1412.5842 . Especially Theorems 3.5, 3.6, 3.9 and the discussion immediately after Theorem 3.9.
2. MSC2020, classification 68R10, graph theory in computer science, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=68R10 .
