# Complete five-voter Kemeny–Copeland conflict layer
## Finding
Consider elections with exactly three candidates, complete strict ballots, and an odd number of voters.

For a profile \(P\), the **Kemeny winner correspondence** \(K(P)\) consists of the candidates that top at least one linear order maximizing total pairwise agreement with the voters.

The **Copeland correspondence** \(C(P)\) selects candidates with maximum number of pairwise victories, with a half-point for a pairwise tie. For odd electorates, pairwise ties cannot occur.

Published work and an explicit five-voter tilted cycle already establish the qualitative first odd-electorate separation: one and three voters do not separate the rules, while five voters can.

The complete five-voter layer is:
\[
\#\{P:K(P)\ne C(P)\}=180
\]
among the
\[
6^5=7776
\]
labeled strict profiles. Thus the exact impartial-culture incidence is
\[
\frac{180}{7776}=\frac5{216}.
\]

Passing to anonymous profiles, there are
\[
\binom{5+6-1}{6-1}=252
\]
multisets of five ballots, and exactly
\[
6
\]
are divergent. Hence the exact impartial-anonymous-culture incidence is
\[
\frac6{252}=\frac1{42}.
\]

Every divergence has the same set relation:
\[
K(P)\subsetneq C(P),
\]
with
\[
|K(P)|=2,\qquad |C(P)|=3.
\]

Moreover, the six anonymous divergent profiles form a single orbit under relabeling of the three candidates.

One representative is
\[
2\,ABC+2\,BCA+1\,CAB.
\]
Its pairwise majority margins are
\[
m_{A,B}=1,\qquad m_{A,C}=-1,\qquad m_{B,C}=3.
\]
Equivalently, the cyclic majority margins have absolute values
\[
(3,1,1).
\]
For this profile,
\[
K(P)=\{A,B\},
\qquad
C(P)=\{A,B,C\}.
\]

Every anonymous divergent profile has ballot multiplicities \(2,2,1\) on the three rankings around a majority cycle. Therefore each has
\[
\frac{5!}{2!\,2!}=30
\]
labeled realizations, and the six candidate relabelings give
\[
6\cdot30=180.
\]

Thus the first odd-electorate Kemeny–Copeland conflict is not merely a single tilted-cycle example: the entire preference-profile layer is one candidate-symmetry type, with exact labeled and anonymous incidences.

## Assumptions and scope
There are exactly three candidates. Every voter submits a complete strict ranking. The electorate size is restricted to odd integers so that all pairwise comparisons are tie-free.

Kemeny is set-valued: every candidate topping at least one maximum-agreement ranking is selected. Copeland is also set-valued.

The five-voter minimality of a tilted three-candidate majority cycle is treated as prior. The new claim is the complete preference-profile census and orbit classification at that known first odd separation.

No statement is made about even electorates or about odd electorates with seven or more voters.

## Proof
With three candidates and no pairwise ties, a profile either has a Condorcet winner or a strict majority cycle.

If there is a Condorcet winner, both Kemeny and Copeland select it.

In a strict majority cycle, Copeland gives every candidate one victory and one defeat, so
\[
C(P)=\{A,B,C\}.
\]

For three candidates, published results identify Kemeny with maximin. In a majority cycle, each candidate's maximin score is determined by the support it receives against its unique defeater. Hence Kemeny selects the candidates whose defeat margin is smallest.

There is also a direct parity bound on the first odd layers. Fix a cycle orientation and sum its three signed margins. A transitive ballot agrees with either two cycle arcs and disagrees with one, contributing \(+1\), or agrees with one and disagrees with two, contributing \(-1\). Therefore the sum of the three positive cyclic margins is at most the number of voters, and all three margins have the electorate's parity.

For three voters, the only positive odd triple with sum at most \(3\) is
\[
(1,1,1),
\]
so Kemeny and Copeland both return all three candidates in every cycle.

For five voters, the only possible positive odd margin multisets are
\[
(1,1,1)
\quad\text{and}\quad
(3,1,1).
\]
The symmetric case still gives equality. In the tilted case \((3,1,1)\), Kemeny drops the candidate suffering the margin-\(3\) defeat while Copeland keeps all three.

What remains is to classify all preference profiles realizing the tilted case.

The verifier performs this classification twice.

First, it exhausts all
\[
6^5=7776
\]
labeled five-voter profiles. Exactly \(180\) are divergent.

Second, it independently enumerates all
\[
252
\]
anonymous ballot-multiplicity vectors. Exactly \(6\) are divergent. Canonicalization under all candidate relabelings shows that the six vectors form one orbit. Every member has multiplicity pattern \(2,2,1\), so each anonymous profile represents exactly \(30\) labeled profiles. This independently recovers
\[
6\cdot30=180.
\]

## Verification
The embedded `verify_kemeny_copeland_odd_first_layer.py` uses only the Python standard library and exact integer arithmetic.

It checks all labeled profiles for odd electorate sizes \(1\), \(3\), and \(5\).

Kemeny is computed independently in two ways:
1. maximizing total pairwise agreement over all six candidate rankings;
2. minimizing total Kendall inversion distance.

For every ranking \(\pi\) and profile with \(n\) voters, it verifies
\[
S_P(\pi)+D_P(\pi)=3n.
\]

It also independently checks the three-candidate Kemeny–maximin equivalence throughout the finite domains used here.

The second census enumerates all \(252\) anonymous five-voter profiles directly from ballot multiplicities and weights each profile by its multinomial number of labeled realizations.

The verifier confirms:
- equality of Kemeny and Copeland for every one-voter and three-voter profile;
- exactly \(180\) divergent labeled five-voter profiles;
- exact labeled incidence \(5/216\);
- exactly \(6\) divergent anonymous profiles;
- exact anonymous incidence \(1/42\);
- \(K(P)\subsetneq C(P)\) with size pair \((2,3)\) in every divergence;
- one candidate-relabeling orbit of anonymous divergent profiles;
- multiplicity pattern \(2,2,1\) and labeled weight \(30\) for every anonymous divergent profile;
- the displayed representative, its margins, and its winner sets.

Run:

`python3 verify_kemeny_copeland_odd_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Courtin, Mbih, and Moyouwou define both Copeland and Kemeny in the same Condorcet-procedure framework. For three candidates they prove that Kemeny is equivalent to the maximin rule they call Condorcet's function, while Copeland behaves differently on majority cycles.

Brandt, Dong, and Peters give a modern correspondence-level refinement diagram for three candidates. Their diagram places Kemeny in the maximin cluster below Copeland, so Kemeny refines Copeland on every three-candidate profile. They also note that, in the absence of majority ties, Copeland returns all three candidates on a majority cycle.

A public educational test-case library already isolates the smallest odd tilted cycle: five voters, cyclic margins \((3,1,1)\), and Kemeny/maximin winner set of size two versus Copeland's three-way tie. It proves that three voters force the symmetric \((1,1,1)\) cycle and that \((3,1,1)\) is the only tilted five-voter margin shape.

The contribution here is strictly stronger at the preference-profile level: the complete sharp-layer census is \(180\) labeled profiles and \(6\) anonymous profiles, and those six anonymous profiles form one candidate-relabeling orbit.

Targeted searches using the rule names, the five-voter parameter, the exact counts \(180\) and \(6\), the fractions \(5/216\) and \(1/42\), and orbit/isomorphism language did not locate an equivalent published census.

## Limitations
The result concerns only the first odd-electorate separation and does not give a formula for larger electorates.

The five-voter minimality and the \((3,1,1)\) margin shape are prior and are not claimed as new.

The exact release day of the September 2012 working paper was not stated on its cover. The metadata uses \(2012\)-\(10\)-\(06\), the earliest day-resolved public indexing date verified for that working paper, rather than inventing a September day.

An unindexed software test corpus, thesis appendix, teaching note, or unpublished enumeration could contain the same \(180/6\) census.

## References
1. S. Courtin, B. Mbih, and I. Moyouwou, “Are Condorcet procedures so bad according to the reinforcement axiom?”, THEMA Working Paper 2012-37, September 2012; later *Social Choice and Welfare* 42 (2014), 927–940.
2. F. Brandt, C. Dong, and D. Peters, “Condorcet-Consistent Choice Among Three Candidates,” arXiv:2411.19857, first submitted 29 November 2024; later *Games and Economic Behavior* 153 (2025), 113–130.
3. “The minimal tilted cycle — five voters, and already the methods disagree,” STAR Voting Education & Test-Case Library, accessed for comparison with the published three-candidate theory.
