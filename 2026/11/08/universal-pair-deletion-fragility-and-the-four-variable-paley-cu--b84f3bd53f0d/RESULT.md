# Universal pair-deletion fragility and the four-variable Paley cutoff

## Finding

For an odd prime power \(q\equiv1\pmod4\), let \(P_q\) be the Paley graph on \(\mathbb F_q\), with two distinct field elements adjacent exactly when their difference is a nonzero square. Let \(\mathcal R\) denote the countable random graph, in the pure undirected adjacency language with equality and without counting quantifiers.

**Theorem.** For every prime power \(q\ge29\) with \(q\equiv1\pmod4\), and **every** two-element vertex set \(S\subseteq V(P_q)\),
\[
P_q-S\equiv_{\mathrm{FO}^{4}}\mathcal R\quad\Longleftrightarrow\quad q\ge49.
\]
Here \(\mathrm{FO}^{4}\) permits at most four reusable variable names but unbounded quantifier depth. More sharply, for each \(q\in\{29,37,41\}\), deletion of **any one** vertex preserves this theory, while deletion of **any two** vertices destroys it. For every allowable \(q\ge49\), any deletion of at most two vertices preserves the theory. This is a complete, sharp pair-deletion phase transition within the Paley graphs that have order at least \(29\).

## Assumptions and scope

Graphs are simple, undirected, and use only binary adjacency and equality. All vertex deletions are induced deletions. For distinct vertices \(a,b,c\), an *extension pattern* is a choice of required adjacency or nonadjacency to each of them; a witness is a fourth vertex distinct from the three realizing all three choices. A graph is *3-existentially closed* (3-e.c.) if every pattern on every distinct triple has a witness. We write \(N(a,b,c;\varepsilon)\) for its number of witnesses in \(P_q\) with prescribed quadratic-character signs \(\varepsilon\in\{-1,1\}^{3}\).

## Proof

**1. Logical equivalence.** A graph is 3-e.c. if and only if it satisfies the finite conjunction of eight sentences of the form \(\forall x\forall y\forall z\,[(x\ne y\land y\ne z\land z\ne x)\Rightarrow\exists w\,\Phi_\varepsilon(x,y,z,w)]\), where \(\Phi_\varepsilon\) requires \(w\) to be distinct from all three vertices and imposes the prescribed adjacency/nonadjacency relations. These are \(\mathrm{FO}^{4}\) sentences. Conversely, if a graph is 3-e.c., Duplicator wins every finite-round four-pebble game against \(\mathcal R\): after the moving pebble is lifted, at most three matched pebbles remain; choose a fresh vertex realizing the same pattern, which exists in both graphs. Thus, for the present finite graphs, 3-e.c. is equivalent to \(\mathrm{FO}^{4}\)-equivalence with \(\mathcal R\).

**2. A uniform three-witness bound.** Let \(\chi\) denote the quadratic character of \(\mathbb F_q\), with \(\chi(0)=0\). Write \(a_1=a,a_2=b,a_3=c\), all distinct. The exact character expansion, with the three base vertices excluded, is
\[
\begin{aligned}
8N(a,b,c;\varepsilon)={}&q-\sum_{i<j}\varepsilon_i\varepsilon_j
+\varepsilon_1\varepsilon_2\varepsilon_3\,T(a,b,c)\\
&-\sum_{u\in\{a,b,c\}}\prod_{i=1}^{3}\bigl(1+\varepsilon_i\chi(u-a_i)\bigr),\\
T(a,b,c)={}&\sum_{x\in\mathbb F_q}\chi\bigl((x-a)(x-b)(x-c)\bigr).
\end{aligned}
\]
Indeed, for \(x\notin\{a,b,c\}\), the product divided by eight is exactly the indicator of its pattern. Linear character sums vanish. Each quadratic character sum at two distinct roots equals \(-1\). The separable cubic defines a nonsingular elliptic curve; the Hasse bound yields \(\lvert T(a,b,c)\rvert\le2\sqrt q\). Each of the three excluded-root product terms is between zero and four, and \(\sum_{i<j}\varepsilon_i\varepsilon_j\le3\). Consequently,
\[
8N(a,b,c;\varepsilon)\ge q-15-2\sqrt q.
\]
For every \(q\ge49\), the right side is at least \(20>16\), so the integer \(N(a,b,c;\varepsilon)\) is at least three. Removing at most two vertices therefore leaves at least one witness for every triple and pattern in the remaining graph. By Step 1 its \(\mathrm{FO}^{4}\) theory is that of \(\mathcal R\).

**3. Three sharp exceptional orders.** The finite prime fields of orders \(29,37,41\) are checked exhaustively by `verify_small_orders.py`: for all \(\binom q3\) distinct unordered triples and all eight patterns, the minimum witness count is exactly two. Hence deletion of an arbitrary single vertex preserves 3-e.c. In the following compact certificates, each row gives a pair \(S\), a triple \((a,b,c)\) disjoint from \(S\), and a three-bit pattern, with `1` meaning adjacency to the corresponding entry. The *entire* witness set is exactly \(S\):

| \(q\) | \(S\) | \((a,b,c)\) | pattern |
| --- | --- | --- | --- |
| 29 | \(\{0,1\}\) | \((3,11,24)\) | `001` |
| 29 | \(\{0,2\}\) | \((1,6,7)\) | `111` |
| 37 | \(\{0,1\}\) | \((6,14,19)\) | `000` |
| 37 | \(\{0,2\}\) | \((1,11,27)\) | `111` |
| 41 | \(\{0,1\}\) | \((5,21,37)\) | `111` |
| 41 | \(\{0,3\}\) | \((15,22,29)\) | `000` |

Each equality of witness sets is checked by `verify_orbit_certificates.py` using integer quadratic residues, independently of the exhaustive counting program. For each of these three primes, \(1\) is a square, while \(2\) (at \(29,37\)) and \(3\) (at \(41\)) are nonsquares. Affine maps \(x\mapsto ux+v\), where \(u\) is any nonzero square, are automorphisms of \(P_q\). They act transitively on unordered adjacent vertex pairs and separately on unordered nonadjacent vertex pairs. The six certificates therefore show that **every** two-vertex deletion at these orders eliminates an extension pattern whose three base vertices remain. Such a graph is not 3-e.c., and by Step 1 cannot have the four-variable theory of \(\mathcal R\). Since there are no allowable prime-power orders strictly between \(41\) and \(49\), the phase transition is complete.

## Verification

The standalone files `verify_small_orders.py` and `verify_orbit_certificates.py` use Python's standard library only. Run `python verify_small_orders.py` and `python verify_orbit_certificates.py` from this directory. Their complete expected outputs appear in `finite_census.txt` and `orbit_certificates.txt`. The first checks \(29{,}232\), \(62{,}160\), and \(85{,}280\) triple-pattern cases at orders \(29,37,41\) respectively, and finds minimal multiplicity two in all three cases and complete pair coverage. The second directly verifies the six residue certificates. The programs certify these *finite* computations only. The uniform infinite-field result relies on the displayed character-sum calculation and the standard elliptic-curve Hasse bound.

## Relationship to prior work

Classical work established existential closure of sufficiently large Paley graphs and, in particular, 3-e.c. for Paley orders at least \(29\). Blass, Exoo, and Harary connected such extensions to first-order adjacency axioms. Ananchuen and Caccetta studied the more general witness-multiplicity property \(P(m,n,k)\), which can potentially imply large-order parts of the present result. Bonato, Holzmann, and Kharaghani discussed Paley 3-e.c. graphs and constructed non-Paley examples via Hadamard matrices. The 2025 study *Existentially closed critical Cayley graphs* explicitly notes that every one-vertex deletion of \(P_{29}\) remains 3-e.c., but does not give the universal two-deletion phase classification in its inspected text. The specific conjunction of (i) vulnerability of **every** pair at three small orders, (ii) safety of **every** pair at all orders at least \(49\), and (iii) its sharp \(\mathrm{FO}^{4}\)-theory interpretation is the contribution assessed here; the prior 3-e.c. threshold is **not** claimed as new.

## Limitations

Only prime powers congruent to one modulo four and at least \(29\) are classified. The result concerns **induced vertex deletion**, not edge deletion, and only the pure adjacency signature with counting-free \(\mathrm{FO}^{4}\). It does not claim an exact larger-deletion resilience number for every order, or equivalence in full first-order logic. The relevant 1993 paper by Ananchuen and Caccetta was obtainable in abstract and bibliographic form but not in full text during this comparison, so stronger coverage from its witness-multiplicity theorems remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. W. Ananchuen and L. Caccetta, *On the adjacency properties of Paley graphs*, Networks 23 (1993), 227–236. DOI: 10.1002/net.3230230404. Abstract and publication metadata inspected; full text not accessed.
2. A. Bonato, W. H. Holzmann, and H. Kharaghani, *Hadamard Matrices and Strongly Regular Graphs with the 3-e.c. Adjacency Property*, Electronic Journal of Combinatorics 8 (2001), R1. DOI: 10.37236/1545. Published 2000-11-06; accessible PDF text inspected.
3. *Existentially closed critical Cayley graphs*, Ars Combinatoria 164 (2025), 19–32. DOI: 10.61091/ars164-02. Full HTML sections 1, 2, and 4 inspected.
4. A. Blass, G. Exoo, and F. Harary, *Paley graphs satisfy all first-order adjacency axioms*, Journal of Graph Theory 5 (1981), 435–439. DOI: 10.1002/jgt.3190050414.
5. H. Hasse's bound for elliptic curves over finite fields: for an elliptic curve over \(\mathbb F_q\), the difference between its number of rational points and \(q+1\) has absolute value at most \(2\sqrt q\).
