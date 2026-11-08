# Sharp reciprocity repair and equilibrium rarity in one-neighbor public-goods networks

## Finding
For every finite loopless one-neighbor directed public-goods network, a specialized Nash equilibrium exists exactly when **all directed cycles have even length**. Its number is \(2^{c}\), where \(c\) is the number of cycles; otherwise it is zero. The minimum number of reciprocal arcs needed to restore existence equals the number \(o\) of odd cycles. Furthermore, among reverse arcs of existing arcs, a single arc repairs an odd-cycle component if and only if its original arc starts on the odd cycle or at a vertex directly pointing into that cycle. Consequently, the number of minimum-size repair sets is
\[
\prod_{C\text{ odd}}\left(|C|+a_C\right),
\]
where \(a_C\) counts vertices outside the cycle with their unique outgoing edge into the cycle (and the empty product is one).

For the uniform loopless random mapping on \(n\ge2\) labeled vertices, the probability-generating transform of the specialized equilibrium count \(K\) is
\[
Q_n(u):=\mathbb E\!\left[u^{c}\mathbf 1_{\{K>0\}}\right]
=\frac{n!}{(n-1)^n}[z^n](1-T(z)^2)^{-u/2},\quad T(z)=ze^{T(z)},\qquad u>0.
\]
In particular, as \(n\to\infty\),
\[
\Pr(K>0)\sim\frac{e\sqrt{2\pi}\,2^{-3/4}}{\Gamma(1/4)}n^{-1/4},\qquad
\mathbb E K\longrightarrow\frac e2.
\]
The asymptotic prefactor in the probability is approximately \(1.1174570615\). Although existence becomes rare, the expected number of equilibria remains bounded away from zero.

## Assumptions and scope
Fix \(n\ge2\). Each player \(i\) has exactly one distinct original out-neighbor \(f(i)\ne i\), and the directed edge \(i\to f(i)\) means that \(i\) benefits from \(f(i)\)'s effort. The effort domain is \([0,\infty)\), and payoffs are \(U_i(e)=b(e_i+\sum_{j\in N_i^+}e_j)-ce_i\), with \(c>0\), continuously differentiable strictly concave \(b\), and a unique \(a>0\) satisfying \(b'(a)=c\); assume the best response is \(\max\{a-\sum_{j\in N_i^+}e_j,0\}\), as follows under the usual decreasing-marginal-benefit conditions. A specialized profile restricts each \(e_i\) to \(\{0,a\}\). New reciprocal arcs may only be arcs \(f(i)\to i\) added without removing existing arcs; adding an already present arc is not counted. In the random model the \(n\) choices \(f(i)\) are independent and each uniformly distributed over the other \(n-1\) vertices. The analytic claims concern specialized pure Nash equilibria, not all equilibria.

A functional digraph has a unique directed cycle in every weak component. Write \(c\) for total cycle count, \(o\) for odd-cycle count, and \(a_C=|\{x\notin C:f(x)\in C\}|\) for the number of cycle-depth-one vertices. The term \(u^c\mathbf1_{\{K>0\}}\) is a cycle-count transform, not the probability-generating function of \(K\) itself; for \(u=1\) it gives existence probability and for \(u=2\) it gives \(\mathbb E K\).

## Proof
**Best-response reduction.** If \(s_i=e_i/a\in\{0,1\}\), the strict-concavity best-response rule says that \(s_i=1\) exactly when all of \(i\)'s out-neighbors have \(s=0\), and \(s_i=0\) exactly when at least one out-neighbor has \(s=1\). Before augmentation, this is \(s_i=1-s_{f(i)}\). Following any directed cycle makes alternation consistent exactly for even cycle length, with two initial choices. All noncycle values are then uniquely obtained in reverse tree order, proving the number \(K\).

**Sharp reciprocity repair.** Let \(C\) be an original odd directed cycle. Without a new arc whose **tail lies in \(C\)**, every cycle player's outgoing neighborhood remains the singleton \(\{f(i)\}\); the inconsistent alternation around \(C\) persists. The reverse of \(x\to f(x)\) has new tail \(f(x)\). Thus one new reverse arc can affect \(C\) only if \(f(x)\in C\), i.e., if \(x\) is on \(C\) or immediately outside it with \(f(x)\in C\). Distinct original odd-cycle components require distinct such arcs, establishing at least \(o\) additions.

Conversely, if \(x\in C\), write \(v=f(x)\) and add \(v\to x\). Set \(s_x=1\), propagate alternating values backwards along the original cycle toward \(v\), and set \(s_v=0\). Since \(C\) has odd length, the values on all other cycle vertices satisfy their original one-neighbor equations, while \(v\)'s new neighbor \(x\) is a specialist; hence \(v\) may be zero even though its original successor is zero. If instead \(x\notin C\) and \(f(x)=v\in C\), add \(v\to x\), assign \(s_x=1,s_v=0\), and propagate backwards along the odd cycle from \(v\), assigning the remaining cycle vertices in alternating order. Now the final original cycle equation fails only at \(v\), where the additional specialist neighbor \(x\) exactly repairs it. Every incoming tree, including the remaining descendants of \(x\), can be completed deterministically in reverse distance order, assigning each child the opposite state from its unique successor. These assignments are valid specialized Nash equilibria. Hence any of the \(|C|+a_C\) eligible original arcs suffices for that component; selections in different components are independent. The lower bound \(o\) is achieved, and all minimum repair sets choose exactly one such arc per odd component, giving the stated product.

**Random enumeration.** The exponential generating function of rooted labeled in-trees is the unique formal power series \(T=ze^T\), with \(T(0)=0\). A weak component consists of a directed cycle of \(k\) vertices, each decorated by an in-tree. Keeping only even cycle lengths and weighting every component by \(u\), the exponential formula gives
\[
\exp\left(u\sum_{j\ge1}\frac{T(z)^{2j}}{2j}\right)=(1-T(z)^2)^{-u/2}.
\]
The total number of loopless maps is \((n-1)^n\). Taking labeled coefficients therefore gives \(Q_n(u)\). For an entirely finite expression, Lagrange inversion yields
\[
Q_n(u)=\frac{n!}{(n-1)^n}\frac{u}{n}
\sum_{j=0}^{\lfloor(n-2)/2\rfloor}
\frac{(1+u/2)_j}{j!}
\frac{n^{n-2j-2}}{(n-2j-2)!},
\]
where \((q)_j=q(q+1)\cdots(q+j-1)\), with \((q)_0=1\).

**Asymptotics.** The dominant square-root singularity of the tree function at \(z=e^{-1}\) is \(T(z)=1-\sqrt{2(1-ez)}+O(1-ez)\). It follows that
\[
(1-T(z)^2)^{-u/2}\sim 2^{-3u/4}(1-ez)^{-u/4}.
\]
Standard singularity transfer, for each fixed \(u>0\), gives the coefficient asymptotic \(2^{-3u/4}e^n n^{u/4-1}/\Gamma(u/4)\). Stirling's formula and \((n-1)^n\sim n^n/e\) yield
\[
Q_n(u)\sim\frac{e\sqrt{2\pi}\,2^{-3u/4}}{\Gamma(u/4)}n^{u/4-1/2}.
\]
At \(u=1\) this is the existence probability; at \(u=2\), because \(K=2^c\) on the existence event, the limit equals \(e/2\). This proves the claims for all \(n\ge2\) and the stated asymptotic regime.

## Verification
The accompanying `verify.py` independently enumerates every self-loop-free mapping on two through six labeled vertices, enumerates all binary effort vectors to test the specialized best-response equations, and checks the cycle law and exact coefficient identities using rational arithmetic. It also independently tests every possible single reverse-arc addition in every mapping with one odd-cycle component for sizes two through six, and compares the observed existence of a repaired specialized equilibrium with the specified cycle-or-direct-child criterion. Both test suites pass. At six vertices there are \(15{,}625\) mappings; the single-addition tests involve \(33{,}840\) candidate arcs. Explicit multiple-component tests check the minimum repair count and product of repair choices. These finite computations are corroboration, not a substitute for the general proofs above. Run `python3 verify.py` with Python standard library only.

## Relationship to prior work
Huang, Sun, Xu and Zhao (2025, arXiv:2512.23193v1) prove the general equivalence between graph kernels and specialized equilibria, and show that reciprocating directed relationships preserves existing specialized equilibria. Their general statements neither determine the **minimum number and complete location set of reciprocity repairs** for functional networks nor the exact random-loopless-mapping law or sharp decay rate claimed here. Their graph-kernel equivalence is an input, not claimed as new; the one-out-neighbor reduction and repair characterization are established independently here. Kempe, Yu and Vorobeychik (2020) examine network modification to induce selected equilibrium forms in broader games, but do not supply the particular complete minimum reciprocal-edge classification here. Classical functional-digraph enumeration, Lagrange inversion and singularity transfer are established mathematical tools; the new application is not a new general enumeration theorem. Deligkas and collaborators (2025) study a related but different indivisible-good and capacity-constrained sharing game.

## Limitations
No assertion is made about nonspecialized pure or mixed equilibria. The random law requires independent uniform outgoing choices without self-loops; other random graph models need not show the same exponent. The repair count addresses only **reverse arcs of existing edges**, not arbitrary new directed arcs or simultaneous edge deletion. The necessary-and-sufficient criterion for an individual repair is component-local; when several odd components exist, one repair in just one component does not restore a global equilibrium. Possible unindexed equivalent results in kernel theory, random mapping theory, or network games are a residual originality risk. Independent scientific audit has not been performed.

## References
1. J. Huang, Y. Sun, F. Xu, W. Zhao, *Public Goods Provision in Directed Networks: A Kernel Approach*, arXiv:2512.23193v1, December 29, 2025, https://arxiv.org/abs/2512.23193.
2. D. Kempe, S. Yu, Y. Vorobeychik, *Inducing Equilibria in Networked Public Goods Games through Network Structure Modification*, arXiv:2002.10627, February 25, 2020, https://arxiv.org/abs/2002.10627.
3. A. Deligkas, G. Gutin, M. Jones, P. R. Neary, A. Yeo, *Public Goods Games in Directed Networks with Constraints on Sharing*, arXiv:2511.11475v1, November 14, 2025, https://arxiv.org/abs/2511.11475.
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, chapters II and VI (standard labeled structures, tree functions and singularity analysis).
