# Exact negative cherry–Sackin covariance under Yule–Harding growth

## Finding

Let \(T_n\) be a standard Yule–Harding–Kingman rooted binary tree with \(n\) leaves: start from one two-leaf cherry and, at each subsequent step, choose one current leaf uniformly and replace it with two leaf children. Leaf labels, assigned uniformly afterward if desired, do not change the statistics below. Let \(K_n\) denote the number of cherries, and let \(S_n\) denote the sum of all leaf depths measured in edges from the binary root (depth zero). Set \(H_n=\sum_{j=1}^{n}1/j\).

**Theorem.** For every integer \(n\ge3\),
\[
\operatorname{Cov}(K_n,S_n)=-\frac{(n-3)(n+2)}{9(n-1)}.
\]
Thus the covariance is zero at \(n=3\), strictly negative for every \(n\ge4\), and \(\operatorname{Cov}(K_n,S_n)=-n/9+O(1)\). For \(n=2\), both statistics are deterministic and the covariance is zero.

An auxiliary exact mixed geometric moment, essential to the proof, is
\[
\mathbb E[Q_n]=\frac{4n}{3}(H_n-1)+\frac{2n}{9},\qquad n\ge3,
\]
where \(Q_n\) is the sum of the depths of the \(2K_n\) leaves that belong to cherries. The harmonic terms in this auxiliary moment cancel those from expected Sackin depth in the final covariance recurrence.

## Assumptions and scope

Trees are rooted, full binary, and unordered at internal vertices. A cherry means an internal node whose two children are both leaves, not a Colless-type balance index. Depth is the number of root-to-leaf edges, with binary root depth zero. Each transition from \(n\) to \(n+1\) leaves selects one of the \(n\) existing leaves with equal probability, independently of the past. The conclusion concerns topology, not continuous coalescent branch lengths or the uniform (PDA) tree distribution. Expectations are with respect to the entire finite Yule growth law; no large-size approximation is needed for the exact identities.

## Proof

Write \(K,S,Q\) for the current statistics at size \(n\). If the selected leaf has depth \(d\) and belongs to a cherry, put \(I=1\); otherwise put \(I=0\). Splitting that leaf changes the statistics by
\[
\Delta K=1-I,\qquad \Delta S=d+2,\qquad \Delta Q=2(d+1)-2Id.
\]
Indeed a split at a cherry leaf replaces the previous cherry with a new cherry two levels lower than its old parent; if the leaf was not a cherry member, the newly created cherry is additional. Exactly \(2K\) leaves are cherry members. Thus, conditional on the complete current tree \(T_n\),
\[
\mathbb E[I\mid T_n]=\frac{2K}{n},\quad
\mathbb E[d\mid T_n]=\frac{S}{n},\quad
\mathbb E[Id\mid T_n]=\frac{Q}{n}.
\]
Consequently
\[
\begin{aligned}
\mathbb E[K_{n+1}\mid T_n]&=\left(1-\frac2n\right)K+1,\\
\mathbb E[S_{n+1}\mid T_n]&=\left(1+\frac1n\right)S+2,\\
\mathbb E[Q_{n+1}\mid T_n]&=\left(1-\frac2n\right)Q+\frac2n S+2,\\
\mathbb E[K_{n+1}S_{n+1}\mid T_n]&=\left(1-\frac1n\right)KS
+\left(1+\frac1n\right)S
+\left(2-\frac4n\right)K-\frac Qn+2.
\end{aligned}
\]
All of these are identities for each individual finite tree, not approximations. At \(n=3\), the unique unlabeled shape has one cherry, leaf depths \(1,2,2\), hence \((K_3,S_3,Q_3)=(1,5,4)\) deterministically. Direct induction in the first two expectation recurrences, beginning there, yields
\[
\mathbb E K_n=\frac n3,\qquad \mathbb E S_n=2n(H_n-1),\qquad n\ge3.
\]
Substitute the second formula into the recurrence for \(\mathbb E Q_n\). The unique solution with \(\mathbb E Q_3=4\) is
\[
q_n:=\mathbb E Q_n=\frac{4n}{3}(H_n-1)+\frac{2n}{9}.
\]
(The induction step uses \(H_{n+1}=H_n+1/(n+1)\).)

Now set \(v_n=\operatorname{Cov}(K_n,S_n)\). Subtracting the product of the first two unconditional moment recurrences from the fourth recurrence, and using \(\mathbb EK_n=n/3\), gives
\[
v_{n+1}=\left(1-\frac1n\right)v_n
+\frac1n\left(\frac23\mathbb ES_n-\mathbb E Q_n\right)
=\frac{n-1}{n}v_n-\frac29,
\qquad n\ge3.
\]
Because \(v_3=0\), multiplication by \(n\) yields
\[
nv_{n+1}=(n-1)v_n-\frac{2n}{9},
\]
and telescoping from size three gives
\[
(n-1)v_n=-\frac29\sum_{j=3}^{n-1}j
=-\frac{n(n-1)-6}{9}.
\]
This equals the asserted expression \(-\frac{(n-3)(n+2)}{9(n-1)}\). The strict sign and asymptotic statement are immediate. The two-leaf exceptional case is deterministic. \(\square\)

## Verification

A standalone exact-arithmetic checker, `verify_yule.py`, is included. It independently enumerates all unordered rooted binary tree shapes reachable by uniform-leaf splitting, retaining **integer counts of ordered leaf-splitting histories** rather than assuming equal probabilities of tree shapes. Through \(n=12\), the checker computes \(\mathbb E K_n\), \(\mathbb E S_n\), \(\mathbb E Q_n\), and their mixed covariance and compares all against the theorem with exact rational arithmetic. A separate exact-state moment recurrence check extends through \(n=300\). Both procedures passed (1232 exact comparisons). Run `python3 verify_yule.py` with Python 3 standard library; no package installation is necessary. The enumeration is finite corroboration, while the conditional recurrences and induction above prove all sizes.

## Relationship to prior work

Ford (2005, sections 4 and 5) develops Sackin/Colless balance statistics and cherry counts for random phylogenetic trees; his covariance discussion concerns Sackin **versus Colless**, not the number of cherries versus Sackin's depth sum. Cardona, Mir, and Rosselló (2012, sections 4 and 8) derive Sackin variance and its covariance with the total cophenetic index, but not with cherry number. Wu and Choi (2015, sections 3 and 6) derive the joint distribution of cherry and pitchfork counts under Yule–Harding–Kingman and PDA models; neither statistic is Sackin's depth sum. The leaf-splitting process and marginal moment formulas are classical. The item asserted here is their precise **mixed** dependence, with auxiliary cherry-member depth expectation.

## Limitations

The statement concerns only the Yule–Harding–Kingman model and discrete, unit-edge topological depth. It does not assert the same formula for the uniform-PDA or Ford general-parameter tree laws, actual branch lengths, or convergence of joint distributions. Earlier literature may contain an implicit equivalent mixed-moment identity; searches and primary-text comparison cannot establish absolute novelty. A full McKenzie–Steel 2000 paper was not inspected, although its abstract describes only the cherry marginal law. Independent mathematical evaluation remains outstanding.

## References

1. Daniel J. Ford, *Probabilities on cladograms: introduction to the alpha model*, first public 2005-11-09, arXiv:math/0511246v1, https://arxiv.org/html/math/0511246v1 (sections 4 and 5).
2. Gabriel Cardona, Arnau Mir, Francesc Rosselló, *Exact formulas for the variance of several balance indices under the Yule model*, first public 2012-02-29, arXiv:1202.6573v1, https://arxiv.org/html/1202.6573v2 (sections 4 and 8; version 2 used only for material inspection).
3. Taoyang Wu and Kwok Pui Choi, *On joint subtree distributions under two evolutionary models*, first public 2015-08-13, arXiv:1508.03139v1, https://arxiv.org/abs/1508.03139 (sections 3 and 6).
