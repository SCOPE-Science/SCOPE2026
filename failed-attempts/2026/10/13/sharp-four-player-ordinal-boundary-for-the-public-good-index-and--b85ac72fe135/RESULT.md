# Sharp four-player ordinal boundary for the Public Good index and the nucleolus
## Finding
Let \(v\) be a simple voting game with player set \(N\), and let \(\mathcal M(v)\) be its family of minimal winning coalitions.

The normalized **Public Good index** of player \(i\) is
\[
PG_i(v)=\frac{\lvert\{S\in\mathcal M(v):i\in S\}\rvert}{\sum_{j\in N}\lvert\{S\in\mathcal M(v):j\in S\}\rvert}.
\]
It measures how often a player participates in minimal winning coalitions.

For an imputation \(x\), write the excess of coalition \(S\) as
\[
e(S,x)=v(S)-\sum_{i\in S}x_i.
\]
The **nucleolus** \(\nu(v)\) is the unique imputation whose vector of coalition excesses, sorted from largest to smallest, is lexicographically minimal.

Compare the two allocations only by the weak ordering they induce on players.

Every proper simple game with at most \(3\) players gives the same weak player ranking under \(PG\) and \(\nu\).

For \(4\) players there are exactly
\[
80
\]
labeled proper simple games, and exactly
\[
18
\]
of them give different weak rankings.

Those \(18\) games form exactly two isomorphism classes under player relabeling, with orbit sizes
\[
12\quad\text{and}\quad 6.
\]

Using players \(A,B,C,D\), canonical minimal-winning families are
\[
\mathcal W_1=\{AB,AC\}
\]
and
\[
\mathcal W_2=\{AB,ACD,BCD\}.
\]

For \(\mathcal W_1\),
\[
PG=\left(\frac12,\frac14,\frac14,0\right),
\qquad
\nu=(1,0,0,0).
\]
Thus Public Good ranks
\[
A>B=C>D,
\]
while the nucleolus ranks
\[
A>B=C=D.
\]

For \(\mathcal W_2\),
\[
PG=\left(\frac14,\frac14,\frac14,\frac14\right),
\qquad
\nu=\left(\frac13,\frac13,\frac16,\frac16\right).
\]
Thus Public Good ties all four players, while the nucleolus ranks
\[
A=B>C=D.
\]

Both first-layer divergent classes are weighted voting games. They admit the representations
\[
[3;2,1,1,0]
\]
and
\[
[4;2,2,1,1],
\]
respectively.

The first class has a dummy player. The second does not. Among the \(50\) labeled proper four-player games with no dummy player, exactly
\[
6
\]
diverge, so the nondummy incidence is
\[
\frac{3}{25}.
\]

Properness is essential to the stated boundary. If properness is removed, exactly \(3\) labeled three-player simple games already diverge, all relabelings of
\[
\mathcal M=\{A,BC\}.
\]
There
\[
PG=\left(\frac13,\frac13,\frac13\right)
\]
while
\[
\nu=\left(\frac12,\frac14,\frac14\right).
\]

Hence four players are the sharp first size at which the Public Good index and the nucleolus can rank players differently inside the proper-simple-game domain.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) cooperative game with the grand coalition winning. It is **proper** when no coalition and its complement are both winning.

Every simple game is represented uniquely by its antichain of minimal winning coalitions.

The comparison is ordinal. Two numerical allocations count as equivalent here when they induce the same weak ranking of players.

The theorem exhausts every proper simple game on one through four players. It does not classify five-player games or quantify numerical distances between \(PG\) and \(\nu\).

## Proof
The verifier enumerates every nonempty antichain of nonempty subsets of \(N\), interprets it as the minimal-winning family of a simple game, and filters by properness.

The exact labeled counts of proper simple games are
\[
1,\ 3,\ 11,\ 80
\]
for one through four players. Their numbers of isomorphism classes under player relabeling are
\[
1,\ 2,\ 5,\ 14.
\]

For each canonical class, the Public Good index is computed independently in two equivalent ways: first by the defining normalized coalition-participation counts, and second by explicitly forming the player-minimal-coalition incidence multiset and normalizing its frequencies.

The nucleolus is computed by an exact rational implementation of the standard successive least-core construction. At each stage, the linear program minimizes the current maximal excess subject to all previously fixed excess levels. All vertices of the small rational polytope are enumerated exactly, coalitions whose excess is constant throughout the optimum face are fixed, and the process stops when the allocation is uniquely determined.

No proper game on one, two, or three players gives different weak rankings.

At four players exactly \(18\) labeled games diverge. Canonicalization under all \(4!\) player permutations gives exactly the two families \(\mathcal W_1\) and \(\mathcal W_2\), with orbit sizes \(12\) and \(6\).

For \(\mathcal W_1\), player \(A\) is the unique veto player. Therefore the core is the singleton
\[
(1,0,0,0),
\]
which is necessarily the nucleolus.

For \(\mathcal W_2\), write an imputation as \(x=(a,b,c,d)\). The excesses of its three minimal winning coalitions are
\[
e(AB,x)=1-a-b,
\qquad
e(ACD,x)=b,
\qquad
e(BCD,x)=a.
\]
Their maximum is at least \(1/3\). Equality forces
\[
a=b=\frac13
\]
and
\[
c+d=\frac13.
\]
Thus the least core is the segment obtained by splitting the residual \(1/3\) between \(C\) and \(D\). The game is symmetric in \(C,D\), and the lexicographic refinement therefore gives
\[
c=d=\frac16.
\]
Hence
\[
\nu=\left(\frac13,\frac13,\frac16,\frac16\right).
\]
The exact successive-LP replay independently returns the same vector.

The verifier also searches integer weighted representations and obtains the two displayed quota-weight descriptions.

Finally, filtering the four-player proper games by absence of dummy players leaves \(50\) labeled games, of which exactly \(6\) diverge, all in the orbit of \(\mathcal W_2\). Removing the properness filter at three players gives exactly \(3\) divergent labeled games, one isomorphism class represented by \(\{A,BC\}\).

## Verification
The embedded `verify_pg_nucleolus_proper_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every proper simple game on one through four players;
- exact labeled counts \(1,3,11,80\);
- exact isomorphism-class counts \(1,2,5,14\);
- two independent calculations of the Public Good index;
- an exact successive least-core computation of the nucleolus on every canonical class;
- agreement of weak rankings for every proper game through three players;
- exactly \(18\) divergent labeled four-player proper games;
- exactly two divergent isomorphism classes with orbit sizes \(12\) and \(6\);
- the two displayed canonical minimal-winning families;
- the displayed Public Good vectors and nucleoli;
- weighted representations \([3;2,1,1,0]\) and \([4;2,2,1,1]\);
- \(50\) proper four-player games without dummies and exactly \(6\) nondummy divergences;
- exactly \(3\) non-proper three-player divergences, all in one isomorphism class.

Run:

`python3 verify_pg_nucleolus_proper_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The Public Good index, also called the Holler or Holler–Packel index, is a classical voting-power measure based on participation in minimal winning coalitions. Alonso-Meijide, Álvarez-Mozos, and Fiestras-Janeiro give an open treatment in which Public Good is explicitly defined from minimal-winning-coalition participation and contrasted with other power indices.

Elkind and Pasechnik study the nucleolus in weighted voting games. Their open paper emphasizes the conceptual contrast between power indices, which allocate according to influence, and the nucleolus, which is a stability-oriented payoff allocation obtained by lexicographically controlling coalition deficits.

Those sources make the comparison natural, but they do not imply an ordinal equivalence threshold between Public Good and the nucleolus. Targeted searches using Public Good/Holler aliases, nucleolus terminology, the four-player parameter, the exact count \(18\), and the two weighted representatives did not locate the sharp boundary or the complete first divergent layer proved here.

## Limitations
The theorem is finite and stops at four players.

It compares weak rankings, not numerical distance between allocations.

The originality search cannot exclude an unindexed teaching computation, software test corpus, thesis appendix, or historical table containing the same finite census.

The oldest day-resolved public source used for cohort dating is the nucleolus paper submitted on \(3\) August \(2008\); earlier classical Public Good publications were identified bibliographically but no invented day was assigned to year-only evidence.

## References
1. E. Elkind and D. V. Pasechnik, “Computing the nucleolus of weighted voting games,” arXiv:0808.0298, first submitted 3 August 2008; later in *Proceedings of SODA 2009*, 327–335.
2. J. M. Alonso-Meijide, M. Álvarez-Mozos, and M. G. Fiestras-Janeiro, “Power Indices and Minimal Winning Coalitions in Simple Games with Externalities,” UB Economics Working Paper E15/328, 2015, open repository record hdl:2445/66937.
3. M. J. Holler, “Forming coalitions and measuring voting power,” *Political Studies* 30 (1982), 262–271.
4. M. J. Holler and E. W. Packel, “Power, luck and the right index,” *Zeitschrift für Nationalökonomie* 43 (1983), 21–29.
