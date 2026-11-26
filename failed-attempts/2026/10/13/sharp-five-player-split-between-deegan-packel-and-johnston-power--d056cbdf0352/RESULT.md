# Sharp five-player split between Deegan–Packel and Johnston power rankings
## Finding
Let \(v\) be a proper simple voting game with player set \(N\), and let \(\mathcal M(v)\) denote its minimal winning coalitions.

The normalized **Deegan–Packel index** is
\[
DP_i(v)=\frac{1}{|\mathcal M(v)|}
\sum_{\substack{S\in\mathcal M(v)\\i\in S}}\frac{1}{|S|}.
\]
It gives every minimal winning coalition equal weight and divides that coalition's unit contribution equally among its members.

For a winning coalition \(S\), let
\[
C(S)=\{i\in S:v(S\setminus\{i\})=0\}
\]
be its critical-player set. The raw Johnston score is
\[
j_i(v)=\sum_{\substack{S\text{ winning}\\i\in C(S)}}\frac{1}{|C(S)|},
\]
and the normalized **Johnston index** is
\[
J_i(v)=\frac{j_i(v)}{\sum_{k\in N}j_k(v)}.
\]

Compare the two vectors only by the weak ordering they induce on players.

Every proper simple game with at most \(4\) players gives exactly the same weak player ranking under \(DP\) and \(J\).

For \(5\) players there are exactly
\[
2645
\]
labeled proper simple games, and exactly
\[
940
\]
of them give different weak rankings. Thus the exact first-layer incidence is
\[
\frac{940}{2645}=\frac{188}{529}.
\]

Those \(940\) games form exactly \(18\) isomorphism classes under player relabeling.

The divergent layer has a sharp internal dichotomy.

First, exactly
\[
480
\]
labeled games in \(9\) isomorphism classes are **pure Johnston tie refinements**: every strict Deegan–Packel comparison is preserved, while Johnston breaks one or more Deegan–Packel ties. Of these, \(420\) games in \(7\) classes break exactly two tied unordered player comparisons, and \(60\) games in \(2\) classes break exactly four.

Second, exactly
\[
460
\]
labeled games in \(9\) isomorphism classes contain **genuine strict reversals** and no tie refinement. Among them, \(300\) games in \(4\) classes reverse one unordered player comparison, \(120\) games in \(3\) classes reverse two, and \(40\) games in \(2\) classes reverse three.

There is no first-layer game in which Deegan–Packel refines a Johnston tie, and there is no mixed divergence having both a strict reversal and a Johnston refinement of a Deegan–Packel tie.

All \(940\) divergent games are dummy-free. Among the \(2645\) proper five-player games, \(2330\) are dummy-free, so the divergence incidence within that subdomain is
\[
\frac{940}{2330}=\frac{94}{233}.
\]

A compact strict-reversal witness has minimal winning coalitions
\[
\{AB,ACD,ACE\}.
\]
Its Deegan–Packel vector is
\[
\left(\frac7{18},\frac16,\frac29,\frac19,\frac19\right),
\]
which ranks
\[
A>C>B>D=E.
\]
Its Johnston vector is
\[
\left(\frac{20}{33},\frac5{22},\frac7{66},\frac1{33},\frac1{33}\right),
\]
which ranks
\[
A>B>C>D=E.
\]
Thus players \(B\) and \(C\) are strictly reversed.

A compact tie-refinement witness has minimal winning coalitions
\[
\{ABC,ABD,ACD,BCE\}.
\]
Its Deegan–Packel vector is
\[
\left(\frac14,\frac14,\frac14,\frac16,\frac1{12}\right),
\]
which ranks
\[
A=B=C>D>E.
\]
Its Johnston vector is
\[
\left(\frac8{27},\frac{13}{54},\frac{13}{54},\frac4{27},\frac2{27}\right),
\]
which ranks
\[
A>B=C>D>E.
\]

Hence five players are the sharp first size at which Deegan–Packel and Johnston cease to be ordinally interchangeable in proper simple voting games, and the entire first divergent layer splits evenly by isomorphism-class count between tie refinement and genuine reversal.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) cooperative game with the grand coalition winning. It is proper when no coalition and its complement are both winning.

Every simple game is represented uniquely by the antichain of its minimal winning coalitions.

The comparison is ordinal. Numerical values may differ even when the induced weak player rankings coincide.

The Johnston index is normalized after the raw critical-coalition score is computed. Since normalization multiplies all player scores by the same positive constant, it does not change the weak ranking.

The classification exhausts all proper simple games on one through five labeled players. It makes no claim for six or more players or for the non-proper domain.

## Proof
The verifier enumerates every nonempty antichain of nonempty coalitions for \(n\le5\), interprets it as a minimal-winning family, and filters by properness.

The exact numbers of labeled proper simple games are
\[
1,\ 3,\ 11,\ 80,\ 2645
\]
for one through five players. The corresponding numbers of isomorphism classes are
\[
1,\ 2,\ 5,\ 14,\ 86.
\]

For each game, Deegan–Packel is computed independently in two exact rational forms. One applies the defining formula directly. The other constructs the equal-split unit vector of each minimal winning coalition and averages these vectors.

Johnston is also computed independently in two exact rational forms. One loops over every winning coalition, forms its critical-player set, and divides that coalition's unit contribution equally among its critical players. The second loops player by player and reconstructs the same critical-coalition contributions. The raw vectors agree exactly before normalization.

The verifier confirms that the two indices induce identical weak rankings for every proper game with at most four players.

At five players, it records for every unordered pair \(\{i,j\}\) whether the Deegan–Packel and Johnston comparisons are equal, tie-refining, reverse-tie-refining, or strictly reversed. Summing these exact pairwise relation signatures gives
\[
940
\]
divergent labeled games.

The only nonzero divergent signatures are:
- \(300\) games with exactly one strict reversal;
- \(120\) games with exactly two strict reversals;
- \(40\) games with exactly three strict reversals;
- \(420\) games with exactly two Johnston refinements of Deegan–Packel ties;
- \(60\) games with exactly four such refinements.

No other divergent signature occurs. Therefore
\[
300+120+40=460
\]
games have strict reversals and
\[
420+60=480
\]
have pure Johnston tie refinements.

Canonicalizing every five-player game under all \(5!=120\) player relabelings yields exactly \(18\) divergent isomorphism classes. The same signature census on canonical representatives gives \(9\) reversal classes and \(9\) tie-refinement classes.

The verifier independently checks dummy status and finds that every divergent game is dummy-free.

Direct substitution into the two index formulas yields the displayed strict-reversal and tie-refinement witness vectors.

## Verification
The embedded `verify_dp_johnston_proper_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every proper simple game on one through five players;
- exact labeled counts \(1,3,11,80,2645\);
- exact isomorphism-class counts \(1,2,5,14,86\);
- two independent Deegan–Packel implementations;
- two independent Johnston implementations;
- ordinal agreement for every proper game through four players;
- exactly \(940\) divergent labeled five-player games;
- exact incidence \(188/529\);
- exactly \(18\) divergent isomorphism classes;
- the \(480\)-game, \(9\)-class pure tie-refinement layer;
- the \(460\)-game, \(9\)-class strict-reversal layer;
- absence of opposite tie refinements and mixed signatures;
- dummy-freeness of every divergence;
- the exact vectors and weak rankings of the two displayed witnesses.

Run:

`python3 verify_dp_johnston_proper_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Lorenzo-Freire, Alonso-Meijide, Casas-Méndez, and Fiestras-Janeiro directly study the Deegan–Packel and Johnston indices together. Their 2007 article gives new axiomatic characterizations of Deegan–Packel and two characterizations of Johnston and states that a political numerical example illustrates differences between the indices.

Freixas and Marciniak give an open full-text treatment of power indices for simple games, including exact formulas for Johnston and Deegan–Packel. Their analysis shows that the indices have materially different structural behavior: Johnston satisfies their egalitarian property, while Deegan–Packel admits counterexamples.

Those results establish that a comparison between the indices is natural and that the concepts are not equivalent in general. They do not, in the material inspected, determine the smallest proper simple game where the induced player rankings differ, nor the complete first divergent layer.

Targeted searches using both index names, rank-reversal and ordinal-equivalence language, five-player restrictions, and exact small-game census language did not locate the sharp \(4\)-versus-\(5\)-player boundary, the \(940\)-game count, the \(18\)-class quotient, or the tie-refinement/reversal split.

## Limitations
The theorem compares weak player rankings, not numerical distance between the two power vectors.

The classification stops at five players and is restricted to proper simple games.

The full text of the closest 2007 direct-comparison article was not available through the open copies located during this run; its abstract and bibliographic metadata were inspected. That leaves a residual bibliographic risk that a detailed table in the inaccessible article could overlap part of the finite census, although its accessible abstract describes axiomatic characterizations and a single political numerical illustration rather than a complete small-game classification.

The metadata date uses \(2011\)-\(09\)-\(21\), the earliest exact day-resolved public date verified for an inspected full-text source. Older relevant publications were identified bibliographically but no exact public day was inferred from year-only or month-only records.

An unindexed historical table, thesis appendix, software test corpus, or teaching enumeration could contain the same finite census.

## References
1. S. Lorenzo-Freire, J. M. Alonso-Meijide, B. Casas-Méndez, and M. G. Fiestras-Janeiro, “Characterizations of the Deegan-Packel and Johnston power indices,” *European Journal of Operational Research* 177 (2007), 431–444. DOI: 10.1016/j.ejor.2005.08.025.
2. J. Freixas and D. Marciniak, “Egalitarian property for power indices,” *Social Choice and Welfare* (2011), published online 21 September 2011. DOI: 10.1007/s00355-011-0593-7.
3. J. Deegan Jr. and E. W. Packel, “A new index of power for simple \(n\)-person games,” *International Journal of Game Theory* 7 (1978), 113–123.
4. R. J. Johnston, “On the measurement of power: some reactions to Laver,” *Environment and Planning A* 10 (1978), 907–914.
