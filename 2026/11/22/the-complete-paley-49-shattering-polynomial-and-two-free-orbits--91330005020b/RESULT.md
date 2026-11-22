# The complete Paley-49 shattering polynomial and two free orbits of extremal supports

## Finding
Let \(P_{49}\) be the open-neighborhood Paley graph on \(\mathbb F_{49}\), and let \(\mathcal N=\{N(c):c\in\mathbb F_{49}\}\) be its 49 Boolean vertex-membership concepts. Its complete shattered-support polynomial is
\[
\Phi_{49}(z)=1+49z+1176z^2+18424z^3+199920z^4+4704z^5.
\]
Thus \(\operatorname{VCdim}(\mathcal N)=5\). Every three-point support is shattered; exactly \(11{,}956\) of the \(211{,}876\) four-point supports fail, and just \(4{,}704\) of the \(1{,}906{,}884\) five-point supports are shattered. The five-point shattered supports split into **two orbits of size 2,352** under the explicitly specified affine semilinear group of order 2,352; their representative sets, in the field encoding below, are
\[
\{0,1,9,10,28\},\qquad\{0,1,9,28,34\}.
\]
Of the 199,920 shattered four-point supports, exactly **188,160 are inclusion-maximal**; each of the other 11,760 belongs to exactly two shattered five-point supports. Hence this shattering complex has maximal faces of distinct dimensions and is not pure.

## Assumptions and scope
Represent \(\mathbb F_{49}=\mathbb F_7[i]/(i^2+1)\) with the field element \(a+bi\) encoded as integer \(a+7b\), where \(0\le a,b<7\). The polynomial \(i^2+1\) is irreducible over \(\mathbb F_7\), because \(-1=6\) is a nonsquare. Let \(Q=\{u^2:u\in\mathbb F_{49}^{\times}\}\) (24 nonzero squares), so \(N(c)=c+Q\). Zero difference is *not* adjacent. Hypothesis centers \(c\) **may** belong to a queried support, and then the associated self-query has value zero. A finite support \(S\subseteq\mathbb F_{49}\) is shattered when every map \(S\to\{0,1\}\) is the restriction of one of the 49 neighborhood indicators. All counts concern unordered, distinct-vertex supports.

The named symmetry group is
\[
G=\{x\longmapsto a x^{7^{\varepsilon}}+b:\ a\in Q,\ b\in\mathbb F_{49},\ \varepsilon\in\{0,1\}\},\qquad |G|=24\cdot49\cdot2=2352.
\]
We do not assert that this is the full abstract automorphism group. Here \(x^7\) is Frobenius conjugation \(a+bi\mapsto a-bi\), since \(i^7=-i\).

## Proof
**Finite-field and trace reduction.** In the chosen coordinate model, subtraction is coordinatewise modulo seven and multiplication is
\[
(a+bi)(c+di)=(ac-bd)+(ad+bc)i.
\]
The included C++17 verifier directly generates all 24 nonzero squares by squaring 48 nonzero field elements, builds the 49-by-49 zero-diagonal adjacency matrix, and verifies degree 24. For an ordered support \(S=(s_0,\ldots,s_{k-1})\), every center \(c\) yields a binary trace integer \(\sum_{j=0}^{k-1}2^j\mathbf 1_Q(s_j-c)\). Since \(-1\) is square in this field, the C++ program's equivalent \(c-s_j\) condition gives the same indicators. All \(2^k\) masks must occur for shattering. This exact Boolean criterion, applied over all centers, is a complete finite decision procedure without random sampling.

**Exhaustive support count with a proof of reduction.** Translating both support and center by any field element preserves all neighborhood traces. Consequently, if \(a_k\) is the number of shattered \(k\)-supports containing zero, then double counting pairs (a shattered support, one of its \(k\) vertices) gives the exact identity \(k f_k=49a_k\), for every \(k>0\). The C++ verifier explicitly visits every one of the \(\binom{48}{k-1}\) possible zero-containing \(k\)-supports, for each \(1\le k\le5\), and obtains
\[
(a_1,a_2,a_3,a_4,a_5)=(1,48,1128,16320,480).
\]
The claimed coefficients follow from \(f_k=49a_k/k\); there is one empty support. Since only 49 concepts exist, no six-point support can be shattered: it would require at least 64 distinct traces. Hereditariness excludes all larger supports. In particular, the count \(a_3=\binom{48}{2}\) establishes that every three-point support is shattered. The executable assertions check the entire anchored enumeration and expected counts, not merely a sampled collection.

**Independent field-norm and symmetry verification.** The Python verifier constructs adjacency differently: the norm \(\mathrm N(a+bi)=a^2+b^2\in\mathbb F_7\) satisfies \(\mathrm N(u)=u^8\); for nonzero \(u\), \(u\) is square in the cyclic group \(\mathbb F_{49}^{\times}\) if and only if its norm belongs to \(\{1,2,4\}\), the nonzero squares of \(\mathbb F_7\). It exhaustively rechecks the 480 anchored shattered five-supports and 16,320 anchored shattered four-supports. Multiplication by a square, conjugation, and translation preserve adjacency, so they preserve shattering. For each remaining anchored five-support, Python computes the complete orbit of anchored images under all square multipliers, both conjugations and translations that move one image vertex to zero. The resulting two disjoint sets have 240 zero-containing supports each and exhaust the 480. Counting zero-incidences as before shows each full orbit has \(49\cdot240/5=2352\) distinct supports. Every group element is unique (the affine maps with and without conjugation differ on the generator \(i\)), so both orbits are free. The two representatives above are the lexicographically least anchored members.

**Nonpurity and four-face extension census.** For *each* anchored shattered four-support, the independent Python verifier tests all 45 possible additional vertices. Exactly 15,360 such supports admit no shattered five-support extension, and 960 admit exactly two. Since any shattered superset of cardinality at least five contains a shattered five-support, the 15,360 zero-extension four-supports are inclusion-maximal. Translational double-counting gives \(49\cdot15360/4=188160\) four-facets. The other 11,760 shattered four-supports each have two extensions, consistent with \(11760\cdot2=4704\cdot5\). All 4,704 five-supports are maximal because six-point shattering is impossible. These different facet sizes prove nonpurity, without needing any classification of smaller-dimensional facets. \(\square\)

## Verification
The two standalone standard-library programs are `verify_paley49.cpp` and `verify_paley49.py`. Replay with `g++ -O2 -std=c++17 verify_paley49.cpp -o verify_paley49 && ./verify_paley49` and `python3 verify_paley49.py`, respectively. They assert the anchored coefficients, all 480 and 16,320 relevant anchored supports, the two extremal orbits, and the exact four-face extension histogram. The C++ code reconstructs squares by field multiplication; the Python code uses the independent norm criterion and independently computes all extremal trace masks. This establishes all claims through finite exhaustive verification on 49 explicitly given vertices. No infinite-field or all-prime-power assertion is made.

## Relationship to prior work
McDonald, Sahay and Wyman [1], first posted in 2022, study the same general quadratic-residue translate VC-dimension problem and prove asymptotic character-sum bounds. Their Section 4 numerical experiments explicitly restrict to **prime fields**, so they do not supply this quadratic-extension 49-vertex exhaustive polynomial or its two orbit counts. Their treatment also discusses a fuzzy/excluded-center convention at zero, which must not be conflated with this ordinary zero-diagonal open-neighborhood concept class. The Paley-25 shattering classification [2] supplies a complete but **different-field-order** polynomial, and its four-point orbit results do not imply the 49-vertex coefficients or free five-point orbits. The exact explicit field-49 trace counts and four-facet extension distribution are the contribution asserted here; the translation invariance and general quadratic-residue framework are credited to prior literature.

## Limitations
This is an exact finite classification for the single Paley graph on \(\mathbb F_{49}\), not a universal theorem for all Paley graphs, all graphs with the same strongly regular parameters, or a proof of asymptotic random-like behavior. The group used in the orbit statement is the explicitly defined affine semilinear subgroup. We do not claim a complete orbit classification of four-point facets or determine integral topology. Execution of finite exhaustive verifiers is part of the proof, not a substitute for independent validation; historical priority outside the inspected primary sources remains a risk. Alternative conventions that include zero as a square, use closed neighborhoods, or prohibit centers in the query set lead to different concept systems.

## References
[1] B. McDonald, A. Sahay and E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, arXiv:2210.03789, first public 2022-10-07, particularly Definitions 1.1–1.2, Proposition 1.7 and Section 4. https://arxiv.org/abs/2210.03789

[2] *The exact Paley-25 shattering polynomial and its exceptional triples*, publicly available research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-paley-25-shattering-polynomial-and-its-exceptional-tri--d709a1a3fcdd
