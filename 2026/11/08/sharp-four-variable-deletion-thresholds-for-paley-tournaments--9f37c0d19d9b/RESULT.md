# Sharp four-variable deletion thresholds for Paley tournaments

## Finding
Let \(q\equiv3\pmod4\) be a prime power, let \(T_q\) be the quadratic-residue tournament over \(\mathbb F_q\), and let \(U\) be the countable random tournament. For \(t\in\{0,1,2,3,4\}\), define \(P(q,t)\) to mean that **every** vertex-deleted induced subtournament \(T_q-S\) with \(|S|\le t\) is equivalent to \(U\) in counting-free four-variable first-order logic at *unrestricted quantifier depth*. Then
\[
 P(q,t)\quad\Longleftrightarrow\quad q\ge Q_t,
 \qquad(Q_0,Q_1,Q_2,Q_3,Q_4)=(19,27,43,47,59).
\]
In particular, for orders \(19\) and \(23\), every single vertex deletion can destroy this equivalence; order \(27\) (a non-prime prime power) and order \(31\) tolerate every single deletion but not every pair; order \(43\) tolerates every pair, order \(47\) every triple, and order \(59\) every quadruple.

## Assumptions and scope
The vertex set of \(T_q\) is \(\mathbb F_q\). An arc \(a\to b\) is present precisely when \(b-a\) is a nonzero square. Since \(q\equiv3\pmod4\), exactly one of \(b-a\) and \(a-b\) is a nonzero square, so this defines a tournament. The language contains equality and only the directed-edge relation. There are no functions, constants, counting quantifiers, or extra definable named vertices. A first-order sentence may reuse four variable *names* arbitrarily many times.

For any tournament \(T\), three distinct anchors \(a_1,a_2,a_3\), and signs \(s_i\in\{1,-1\}\), a *witness* is a vertex \(x\) distinct from all three anchors with \(\chi(x-a_i)=s_i\) for each \(i\), where \(\chi\) denotes the quadratic character on \(\mathbb F_q\) when \(T=T_q\). Define \(m(q)\) to be the minimum number of witnesses over all anchor triples and all eight sign patterns. The condition \(m(q)\ge1\) is the three-extension property.

## Proof
**1. The logical reduction.** A countable random tournament realizes every orientation pattern relative to any finite tuple of distinct vertices. A finite tournament with the three-extension property is equivalent to it for counting-free \(\mathrm{FO}^{4}\) sentences: in the four-pebble Ehrenfeucht--Fraisse game, at most three pebbles remain stationary when the fourth moves, and the three-extension property provides a fresh vertex with any required directions to the stationary vertices. For one or two anchors, extend to three by choosing extra distinct vertices; three-extension itself ensures enough vertices. Duplicator preserves equality and all directed arcs at every round, for arbitrarily many rounds. Conversely, failure of a three-anchor orientation pattern is witnessed by a first-order sentence with four variable names and three existentially chosen distinct anchors followed by one universal variable, whereas the random tournament satisfies every such sentence. Thus
\[
  T_q-S\equiv_{\mathrm{FO}^{4}}U\quad\Longleftrightarrow\quad
  T_q-S\text{ has the three-extension property}.
\]

**2. The exact deletion reduction.** If \(m(q)\ge t+1\), removing any at most \(t\) vertices leaves a witness for every pattern based on surviving anchors; hence every deletion preserves equivalence. If \(m(q)\le t\), choose a triple and pattern with precisely \(m(q)\) witnesses and delete all those witnesses. The anchors survive but the pattern is lost, so that deletion fails equivalence. Therefore
\[
  P(q,t)\quad\Longleftrightarrow\quad m(q)\ge t+1.
\]

**3. Infinite-family lower bound.** Fix three distinct field elements \(a_1,a_2,a_3\) and signs \(s_1,s_2,s_3\). The exact witness count \(N\) satisfies
\[
  8N=\sum_{x\notin\{a_1,a_2,a_3\}}
    \prod_{i=1}^{3}(1+s_i\chi(x-a_i)).
\]
Expand first over *all* \(x\in\mathbb F_q\). The constant contribution is \(q\); each linear character sum is zero; each distinct-pair character sum is \(-1\); and the cubic term is a character sum of a squarefree cubic, whose absolute value is at most \(2\sqrt q\) by the Hasse bound (equivalently the degree-three Weil character-sum bound). The three pair contributions total at least \(-3\). At each excluded anchor the product is between zero and four, since one factor equals one and the other two lie in \(\{0,2\}\); therefore excluding all three decreases the full sum by at most twelve. Consequently
\[
   8N\ \ge\ q-15-2\sqrt q.
\]
The right-hand side is strictly increasing for \(q>1\). For each \(t\in\{0,1,2,3,4\}\), it exceeds \(8t\) from the indicated field order onward:
\[
  \begin{array}{c|ccccc}
 t&0&1&2&3&4\\\hline
 \text{bound valid from }q&27&43&47&59&67
 \end{array}
\]
(here the inequality can be verified at each displayed starting value). Since \(N\) is an integer, it follows that \(m(q)\ge t+1\) for the corresponding ranges.

**4. All remaining admissible orders.** A finite exhaustive calculation gives the following *exact* minima, with the field of order \(27\) constructed explicitly as \(\mathbb F_3[X]/(X^3+2X+1)\):
\[
\begin{array}{c|rrrrrrrrrr}
q&3&7&11&19&23&27&31&43&47&59\\\hline
m(q)&0&0&0&1&1&2&2&3&4&5
\end{array}
\]
The attached `verify_multiplicity.py` checks every unordered anchor triple and all eight orientation patterns. The independently implemented `verify_affine.py` normalizes triples using affine maps, treats order \(27\) through a separately implemented field multiplication, and confirms the same minima. The normalization is valid because translation plus multiplication by any nonzero field element either preserves all arc orientations (square multiplier) or reverses them all (nonsquare multiplier); both transformations permute sign patterns and preserve the minimum. These calculations cover exactly the admissible orders below the general bound thresholds; there are no omitted admissible orders. Combining them with Step 3 gives the stated five sharp thresholds.

## Verification
Two executable, standard-library-only Python programs and their verbatim output files are embedded alongside this result. Running `python verify_multiplicity.py` and `python verify_affine.py` must reproduce `verification_output.txt` and `verification_affine_output.txt` respectively. The first enumerates all \(\binom q3\) unordered anchor triples at each displayed field order, with \(32{,}509\) triples at order \(59\). The second independently reduces the check to normalized triples and provides a separate order-\(27\) field model. The programs certify the finite minima; they do not replace the general character-sum argument.

## Relationship to prior work
Bonato, Gordinowicz and Prałat (2010) study existential closure of tournaments and Paley examples, including the smallest three-existentially closed tournaments. Duffy, MacGillivray and Sopena (arXiv:1812.05510, 2018) introduce the *exact equivalent multiplicity property* \(P_{i,j}\): our requirement \(m(q)\ge t+1\) is precisely their \(P_{3,t+1}\). Their Proposition 5.1 verifies a useful multiplicity instance at order \(67\), but does not supply the five exact field-order cutoffs or all small-field minima. Javier, Llano and Zuazua (2026) give detailed orientation-pattern counts in prime-order Paley tournaments, but neither a prime-power deletion-resilience classification nor the five sharp thresholds. Earlier Paley-graph deletion statements refer to **undirected** Paley graphs of residue-field orders congruent to one modulo four, so do not imply the oriented case here.

## Limitations
The asserted theorem covers only prime-power Paley tournaments with \(q\equiv3\pmod4\), counting-free \(\mathrm{FO}^{4}\) in the pure directed-edge language, and deletion budgets zero through four. It says nothing about deletion budgets at least five, larger variable widths, counting logics, or arbitrary tournaments. The computational certificates are finite; the large-field statement depends on the classical Hasse character-sum bound. Historical priority is provisional: in particular, a not-yet-identified exact multiplicity census or sharper general theorem might cover portions of this classification. No independent mathematical audit has been performed.

## References
- A. Bonato, P. Gordinowicz, P. Prałat, *Bounds and constructions for n-e.c. tournaments*, Contributions to Discrete Mathematics 5(2), 2010, first published 2010-09-28. DOI: 10.55016/ojs/cdm.v5i2.62061. https://cdm.ucalgary.ca/article/view/62061
- C. Duffy, G. MacGillivray, É. Sopena, *Oriented Colourings of Graphs with Maximum Degree Three and Four*, arXiv:1812.05510 (first posted 2018-12-13), especially Property \(P_{i,j}\) and Proposition 5.1. https://arxiv.org/pdf/1812.05510
- N. Y. Javier, B. Llano, R. Zuazua, *2- and 3-existentially closed tournaments*, Contributions to Discrete Mathematics, 2026-02-27. DOI: 10.55016/0sre1423. https://cdm.ucalgary.ca/article/download/78881/58831/277078
- R. L. Graham, J. H. Spencer, *A Constructive Solution to a Tournament Problem*, Canadian Mathematical Bulletin, 1971. DOI: 10.4153/CMB-1971-007-1.
