# Two exhaustive participation-reversal mechanisms for three-candidate Baldwin elimination

## Finding

For a strict three-alternative election under **simultaneous tied-lowest Borda elimination**, let a new voter submit \(A\succ B\succ C\). Write \(s_A,s_B,s_C\) for the initial \((2,1,0)\) Borda scores, and \(m_{UV}\) for the initial number ranking \(U\) above \(V\), minus the number ranking \(V\) above \(U\). Assume both initial and enlarged elections return unique winners.

**Complete if-and-only-if classification, for every finite number of initial voters:** The new voter strictly prefers the initial winner to the enlarged election's winner exactly in either of the following mutually exclusive cases.

- **I — creation of a bottom tie:** \(s_B=s_A+1\), \(s_C\ge s_A+3\), and \(m_{BC}>0\). Initially \(A\) alone is eliminated and \(B\) defeats \(C\). The added ballot creates a bottom Borda tie between \(A\) and \(B\), which are eliminated together, making \(C\) the new winner. Thus \(B\to C\).
- **II — breaking a bottom tie:** \(s_B=s_C<s_A\) and \(m_{BA}\ge2\). Initially \(B\) and \(C\) are simultaneously eliminated and \(A\) wins. After the additional ballot, \(C\) alone is eliminated and \(B\) defeats \(A\). Thus \(A\to B\).

The first possible instance uses 11 initial voters (12 with the extra voter). At this first order, there are precisely six **directed** anonymous instances, consisting of one candidate-relabeling orbit, all of type I. The minimal electorate size itself was established previously by Brandt, Matthäus and Saile (2022); the claimed distinct contribution is the all-order two-mechanism classification and complete first-order orbit census.

## Assumptions and scope

Let the three alternatives be distinct, and let every ballot rank them strictly. For each profile, assign Borda points \((2,1,0)\) to first, second, and last ranks. Eliminate **all** alternatives tied for lowest current score in each round; when exactly two alternatives remain, the scores from the restricted ballots select their strict pairwise-majority winner. If the remaining alternatives tie, no unique winner exists, and that instance is excluded. Thus a tie for last between two candidates while the third leads elects that third candidate immediately. We consider one extra ballot, all finite initial electorate sizes including zero, and only pairs of elections each having a unique winner.

## Proof

By relabeling, take the extra ballot as \(A\succ B\succ C\). Adding it raises the three initial Borda scores by \((2,1,0)\), and increases each pairwise margin in the added ballot's direction by exactly one.

First suppose the identity of the unique last-place candidate is **unchanged**. Then the final two alternatives are unchanged, and adding the ballot cannot change a pairwise winner to one the ballot ranks lower: the pairwise margin changes in the ballot's preferred direction. A strict worsening therefore requires a change in the first-round lowest set.

If both the initial and final lowest sets are **singletons**, the singleton can change only from \(A\) to \(C\). Indeed, two distinct candidates must reverse a strict integer Borda inequality; their score increments must differ by at least two, which only occurs for top \(A\) and bottom \(C\). Before addition the final contest is between \(B\) and \(C\); after addition it is between \(A\) and \(B\). Whatever the respective strict pairwise winners, this cannot be a strict worsening: the initially chosen option is \(B\) or \(C\), whereas the final choice is \(A\) or \(B\).

Next, suppose the old bottom set is a singleton but the new bottom set a **pair**. Since score increments strictly descend \(2>1>0\), the initially unique loser must be \(A\). The only pair ties attainable below the third are \(\{A,B\}\) or \(\{A,C\}\). For \(\{A,B\}\), the equal-score and strict-third conditions are precisely \(s_B=s_A+1\) and \(s_C\ge s_A+3\). This elects \(C\), strictly worse than the old winner exactly when the old \(B\)-versus-\(C\) contest was won by \(B\), i.e. \(m_{BC}>0\). This is case I. For \(\{A,C\}\), the new winner is \(B\), which is never worse than the old winner \(B\) or \(C\). An all-three bottom tie after addition has no unique winner.

Conversely, if the old bottom set is a **pair** and the new set a singleton, the old tied-lowest pair must include \(C\) (the zero-increment candidate); an old tie \(\{A,B\}\) can only yield \(B\) alone last, so the old winner \(C\) is replaced by a more preferred option. An old tie \(\{A,C\}\) can only yield \(C\) alone last, so the old winner \(B\) is replaced by \(A\) or \(B\), never worse. Finally, an old tie \(\{B,C\}\) elects \(A\), and changes to unique elimination of \(C\). The new strict final winner is \(B\) exactly when its old margin over \(A\) is at least two, since the added ballot decreases that margin by one. Together with the initial bottom tie this is precisely case II. Two distinct non-singleton bottom sets cannot both yield unique winners and strict worsening: the only possible pair-to-pair transition is \(\{A,B\}\to\{B,C\}\), and the new winner \(A\) is preferred to the old winner \(C\). This exhausts all cases.

For the **sharp first electorate and orbit census**, list the six strict rankings in order \((ABC,ACB,BAC,BCA,CAB,CBA)\). Every anonymous profile with \(n\) voters corresponds bijectively to a six-tuple of nonnegative integers summing to \(n\). Exhaustively enumerate these six-tuples for \(0\le n\le11\), and test each of the six added rankings against the above winner rule. The accompanying standalone `verify.py` uses only integer arithmetic and checks the classification simultaneously. It finds zero detrimental events for \(n\le10\), and exactly six for \(n=11\), all type I. The six events are exactly the six distinct candidate relabelings of the canonical tuple \((2,0,0,4,5,0)\) with extra ballot \(ABC\): initially the Borda scores are \((9,10,14)\) and \(B\) defeats \(C\) by 6 votes to 5; afterwards they are \((11,11,14)\), so both \(A\) and \(B\) are eliminated, electing \(C\). The assertion of exhaustiveness here is finite and consists of a bijection between all anonymous profiles and all enumerated tuples; it is not extrapolated from partial random experiments. The all-electorate classification was proved above independently of the enumeration.

Both types really occur. Type II occurs with 12 initial voters: the tuple \((0,5,4,0,0,3)\) and extra ballot \(ABC\) yield scores \((14,11,11)\) before and \((16,12,11)\) after, changing winner \(A\) to winner \(B\).

## Verification

Run `python3 verify.py` with Python 3. The checker enumerates every anonymous six-ballot profile with \(0\le n\le17\), and for every one of the six possible added ballots compares the independently computed before/after unique-winner outcome against the two formulae. This makes 605,682 exact comparisons. It also enumerates the first 11-voter event set, tests its size is six, constructs the complete candidate-relabeling orbit, checks orbit equality, checks the canonical 11-voter witness, and checks the first observed second-type configuration. Computation validates finite layers and the sharp 11-voter boundary; the separate case analysis proves the universal statement.

## Relationship to prior work

Narodytska, Walsh and Xia (2011, arXiv:1106.5312v1) study manipulation and complexity of Baldwin and Nanson procedures, using a specified tie-breaking mechanism when several candidates share the lowest score. Such single-candidate tie-breaking is not the simultaneous tied-lowest rule used here. Brandt, Matthäus and Saile (2022, Section 4.9 and their Table 2) explicitly use simultaneous elimination and already exhibit a 12-voter three-alternative Baldwin no-show paradox with minimum electorate size. Their published minimal-witness compilation does not in its inspected statement give the two explicit all-order score-and-margin criteria or the entire first-order orbit census. General impossibility and Condorcet-participation literature is broader in subject but does not directly imply the explicit Baldwin tie-magnitude characterization.

## Limitations

The result concerns exactly three alternatives, strict unweighted rankings, the simultaneous-elimination tie convention, and strict unique winners on both sides of the addition. Other tie-breaking conventions or more alternatives may allow different mechanisms. The 12-total-voter threshold is previously known and is included as a checked boundary rather than claimed as an independent discovery. A full-text historical priority examination of some older voting-paradox frequency papers was unavailable; exact novelty of the all-order classification remains subject to that risk. There is no claim about electoral desirability, turnout behavior, or real-world prevalence.

## References

- N. Narodytska, T. Walsh, L. Xia, *Manipulation of Nanson's and Baldwin's Rules*, arXiv:1106.5312v1 (first posted 2011-06-27), https://arxiv.org/abs/1106.5312.
- F. Brandt, M. Matthäus, C. Saile, *Minimal voting paradoxes*, Journal of Theoretical Politics 34 (2022), DOI:10.1177/09516298221122104, https://doi.org/10.1177/09516298221122104.
- F. Brandt, P. Dong, D. Peters, *Condorcet-Consistent Choice Among Three Candidates*, arXiv:2411.19857v1 (2024), https://arxiv.org/abs/2411.19857.
- J. Lepelley, H. Smaoui, *Comparing Two Ways for Eliminating Candidates in Three-Alternative Elections Using Sequential Scoring Rules* (2019), DOI:10.1007/s10726-019-09618-5 (abstract examined; full text not inspected).
