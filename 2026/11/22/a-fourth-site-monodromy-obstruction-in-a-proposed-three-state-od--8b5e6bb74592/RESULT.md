# A fourth-site monodromy obstruction in a proposed three-state odometer

## Finding

Let \(\Sigma=\{0,1,2\}\). For the second candidate ternary odometer given by the conditional permutations in Table 3 of Kamilya, Kari and Paturi (2026), the induced maps on the first \(n\) coordinates have cycle types
\[
\begin{array}{c|c}
 n & \text{cycle lengths, with multiplicities}\\\hline
 1 & 3\\
 2 & 9\\
 3 & 27\\
 4 & 27,27,27.
\end{array}
\]
In particular, this candidate is **not topologically transitive or minimal** on \(\Sigma^{\mathbb N_0}\), despite its first three finite-prefix maps being single cycles. The fourth coordinate is the first finite-prefix obstruction; its three invariant clopen components arise from identity monodromy over the complete \(27\)-cycle of the first three coordinates.

## Assumptions and scope

The ambient space is the full one-sided configuration space \(X=\Sigma^{\mathbb N_0}\) with the product topology. Fix the boundary value to the left of cell zero as \(0\). Updates are **synchronous**, and for all \(i\ge0\),
\[
(Hx)_i=P_{x_{i-1}}(x_i),\qquad x_{-1}=0,
\]
where the three permutations of \(\Sigma\) are
\[
P_0=(0\ 1\ 2),\qquad P_1=(0\ 1),\qquad P_2=(0\ 2).
\]
Here cycle notation describes their actions: \(P_0(0)=1\), \(P_0(1)=2\), \(P_0(2)=0\); \(P_1\) interchanges \(0,1\); \(P_2\) interchanges \(0,2\). Thus this is exactly the published proposed rule \(g,h,h,\ldots\), or equivalently its uniform rule \(h\) with constant left boundary \(0\). Let \(H_n\) be the induced map on the first \(n\) coordinates, indexed \(0,\ldots,n-1\).

## Proof

**Step 1: triangular permutation extension.** Each \(P_a\) is a permutation, hence \(H_n\) is bijective: recover the old coordinates successively from left to right. The first \(n\) outputs depend only on the first \(n\) inputs. Suppose \(H_n\) has a single orbit \(u(0),\ldots,u(L-1)\) of length \(L\). Write \(w=u_0(n-1)\cdots u_{L-1}(n-1)\) for the final-coordinate symbols of that orbit, in temporal order. In the extension \(H_{n+1}\), after \(L\) steps the first \(n\) coordinates return, while the new coordinate is transformed by
\[
M(w)=P_{w_{L-1}}\circ\cdots\circ P_{w_1}\circ P_{w_0}.
\]
If this monodromy is a three-cycle, \(H_{n+1}\) has a single orbit of length \(3L\). If it is the identity, \(H_{n+1}\) has precisely three disjoint orbits of length \(L\). This follows by lifting the single \(L\)-cycle and inspecting the return permutation on its three-element fiber.

**Step 2: the first two lifts.** The unique \(H_1\)-orbit starts at \(0\) and has temporal word \(w_1=012\). Direct multiplication gives
\[
M(w_1)=(0\mapsto2,\ 1\mapsto0,\ 2\mapsto1),
\]
a three-cycle. Hence \(H_2\) is a single nine-cycle. Starting from \(00\), the second-coordinate word over its nine steps is
\[
w_2=010201122.
\]
Multiplying the nine conditional permutations again gives \(M(w_2)=(0\mapsto2,\ 1\mapsto0,\ 2\mapsto1)\). Consequently \(H_3\) is a single \(27\)-cycle.

**Step 3: the first failure.** Starting with \(000\), the complete \(H_3\)-orbit is the following exact cyclic list (each successive triple is obtained by applying the displayed local rule):

```
000 111 200 021 101 212 012 122 220
002 110 201 022 100 211 010 121 221
001 112 202 020 102 210 011 120 222
```

These are all \(27\) distinct triples; the last returns to the first. Reading the third coordinate yields
\[
w_3=010112220\,201201011\,122020102.
\]
The three consecutive nine-letter blocks have monodromies, respectively, given by the image triples
\[
(2,0,1),\quad (0,1,2),\quad (1,2,0).
\]
Their composition in temporal order is the identity. Thus \(M(w_3)=\mathrm{id}_\Sigma\), and the skew-extension lemma proves that \(H_4\) has exactly **three \(27\)-cycles**, rather than one \(81\)-cycle. Equivalently, \(H_4^{27}=\mathrm{id}\) on all \(81\) four-symbol words.

**Step 4: consequences for the infinite map.** The canonical projection \(\pi_4:X\to\Sigma^4\) satisfies \(\pi_4\circ H=H_4\circ\pi_4\). The inverse images of the three distinct \(H_4\)-orbits partition \(X\) into three nonempty, pairwise disjoint, proper **clopen invariant** sets. A topologically transitive map cannot have such a partition (take open sets in distinct components). Thus \(H\) is not transitive and therefore not minimal. Since \(H_1,H_2,H_3\) are single cycles, \(n=4\) is the first finite-prefix transitivity obstruction. As each prefix update is a bijection and the system is triangular, \(H\) is also an equicontinuous homeomorphism; no claim about its complete infinite-orbit decomposition is needed.

## Verification

The standalone `check.py` independently implements the nine entries of the published table in conditional form and as a lookup table; it checks their equality for every word of lengths \(1\) through \(4\), enumerates all finite-prefix cycles through length \(4\), reproduces the three trace words and permutation products, verifies the exact \(27\)-step return for every four-symbol state, and verifies that the three orbits through \(0000,0001,0002\) are disjoint and cover all \(81\) states. Run `python3 check.py`. The infinite nontransitivity conclusion is proved by the finite clopen-factor argument, not inferred merely from experiments.

## Relationship to prior work

Kamilya, Kari and Paturi (arXiv:2605.22762v1, Sections 3 and 6) rigorously prove minimality of their **first** ternary odometer whose conditional rule for predecessor \(0\) is the identity. In their concluding Table 3, they propose a different second candidate that instead applies the three-cycle when the predecessor is \(0\), and say it appears to behave similarly but is unproved. The present exact monodromy calculation concerns only that second candidate and shows that its first three prefixes are misleading: at the fourth coordinate, the orbit unexpectedly splits into three components. It does not challenge the proved first construction or resolve the separate question of transitive nonsensitive non-uniform automata on \(\mathbb Z\).

## Limitations

This is an exact four-coordinate dynamical obstruction, not a classification of all finite-prefix orbit structures or all invariant measures of the infinite system. It does not imply that every candidate uniform-boundary modification of an odometer fails. Historical priority is limited to the primary and public-result comparisons described in the accompanying review; no independent mathematical audit has been performed.

## References

1. Supreeti Kamilya, Jarkko Kari and Katariina Paturi, *Minimality, transitivity and sensitivity of non-uniform cellular automata*, arXiv:2605.22762v1 (first posted 21 May 2026), in particular Section 3, Theorem 1, and Section 6, Table 3. https://arxiv.org/abs/2605.22762 ; lawful public full text: https://www.researchgate.net/publication/405132270_Minimality_transitivity_and_sensitivity_of_non-uniform_cellular_automata
2. Supreeti Kamilya and Jarkko Kari, *Nilpotency and periodic points in non-uniform cellular automata*, Acta Informatica 58 (2021), 319–333. Background on temporal periodic points and non-uniform rules; no claim about the distinct Table 3 rule is used here.
