# Exact minimal witness-size spectra and a Gaussian law for finite-depth modal tree types

## Finding

**Theorem (complete tree-witness order spectrum and Gaussian concentration).** Fix an integer \(p\geq0\) and let \(q=2^p\). In the Boolean basic modal language with \(p\) named propositional letters, one forward existential modality \(\Diamond\), and finite **unordered outward rooted trees** with the **immediate-child** relation, let \(\mathcal U_h\) be the set of complete pointed modal-depth-\(h\) theories realizable at the root of a finite tree of height at most \(h\). For \(\tau\in\mathcal U_h\), write \(w_h(\tau)\) for the minimum number of vertices in such a tree realizing \(\tau\). These minima have unique attaining trees up to root-, edge- and color-preserving isomorphism.

The polynomial \(P_h(z)=\sum_{\tau\in\mathcal U_h}z^{w_h(\tau)}\) satisfies the exact product recurrence
\[
P_0(z)=qz,\qquad
P_{h+1}(z)=qz\prod_{j=1}^{M_h}(1+z^j)^{[z^j]P_h(z)},\qquad M_h=\deg P_h.
\]
Write \(N_h=P_h(1)\). Then
\[
N_0=q,\quad N_{h+1}=q\,2^{N_h},\qquad
M_0=1,\quad M_{h+1}=1+\frac{N_h(M_h+1)}2.
\]
For every \(h\geq0\), the set of attainable **minimum witness orders** is the full integer interval \(\{1,2,\ldots,M_h\}\), and the extremal coefficients both equal \(q\):
\[
[z]P_h(z)=[z^{M_h}]P_h(z)=q,\qquad P_h(z)=z^{M_h+1}P_h(z^{-1}).
\]

Choose a modal type uniformly from \(\mathcal U_h\) and let \(X_h\) be its minimum tree-witness order. Its mean \(\mu_h\) and variance \(\sigma_h^2\) obey
\[
\mu_h=\frac{M_h+1}{2},\qquad \sigma_0^2=0,\qquad
\sigma_{h+1}^2=\frac{N_h}{4}\bigl(\sigma_h^2+\mu_h^2\bigr).
\]
For every \(h\geq1\), \(\sigma_h>0\), and the following explicit normal approximation and concentration inequalities hold for every real \(x\) and every \(\varepsilon>0\):
\[
\left|\Pr\!\left(\frac{X_h-\mu_h}{\sigma_h}\leq x\right)-\Phi(x)\right|
\leq \frac{0.56\sum_{\tau\in\mathcal U_{h-1}}w_{h-1}(\tau)^3}{\left(\sum_{\tau\in\mathcal U_{h-1}}w_{h-1}(\tau)^2\right)^{3/2}}
\leq\frac{1.12}{\sqrt{N_{h-1}}},
\]
\[
\Pr\bigl(|X_h-\mu_h|\geq\varepsilon M_h\bigr)
\leq 2\exp(-\varepsilon^2N_{h-1}).
\]
In particular, for every fixed propositional vocabulary, \((X_h-\mu_h)/\sigma_h\) converges in distribution to a standard normal random variable as \(h\to\infty\), while \(X_h/M_h\to1/2\) in probability. Here \(\Phi\) is the standard normal distribution function and the constant \(0.56\) is a valid non-identically-distributed Berry--Esseen constant.

## Assumptions and scope

A vertex color is its full truth-value assignment to the \(p\) propositional letters, giving \(q\) labeled colors. Children are unordered, edges point away from the root, all trees are finite and nonempty, and accessibility means exactly one edge, not descendant reachability. A depth-zero modal theory records the root color. At depth \(h+1\), a theory records its root color together with the **set** (not multiset) of depth-\(h\) theories of its children. This is ordinary modal logic without counting; different child multiplicities are invisible.

Depth-\(h\) equivalence means agreement on every formula of modal nesting depth at most \(h\), equivalently existence of a depth-\(h\) forth/back bisimulation. The minimum in \(w_h\) is taken over rooted **trees of height at most \(h\)**, not over arbitrary finite Kripke graphs or directed acyclic graphs. An unrestricted finite pointed model can be unrolled to height \(h\), but state-sharing or loops may reduce its minimum order relative to the tree minimum. We do not make an unrestricted-graph optimality claim.

## Proof

**1. Exact modal signatures and their unique smallest witnesses.** For \(h=0\), a depth-zero theory is one of the \(q\) root colors, and its unique smallest tree is a one-vertex tree. Suppose the claim proved through depth \(h\). A pointed tree of height at most \(h+1\) has signature \((c,S)\), where \(c\) is its root color and \(S\subseteq\mathcal U_h\) is the set of depth-\(h\) signatures of its children. Two such trees agree on modal formulas through depth \(h+1\) iff their colors and these sets agree: the forward implication uses characteristic formulas, and the backward implication uses structural induction. Explicitly, a characteristic formula for \((c,S)\) is
\[
\theta_c\ \wedge\ \bigwedge_{\tau\in S}\Diamond\chi_\tau\ \wedge\ \Box\bigvee_{\tau\in S}\chi_\tau,
\]
where \(\theta_c\) fixes exactly the root color and \(\chi_\tau\) characterizes a lower-depth signature. Empty conjunctions have value true and empty disjunctions false.

Each \(\tau\in S\) requires a **different child**, since one child cannot have two distinct depth-\(h\) signatures. By induction any child having signature \(\tau\) needs at least \(w_h(\tau)\) vertices. Consequently every witness for \((c,S)\) has at least \(1+\sum_{\tau\in S}w_h(\tau)\) vertices. Attach one canonical minimum witness for each \(\tau\in S\) to a new root of color \(c\). The lower bound is attained. Equality forces precisely one child of every specified type and each child to attain its own minimum, so the tree is unique up to isomorphism. In particular, every \((c,S)\) is realizable, completing the induction.

**2. Exact enumerator and support.** A signature at the next depth is a color and an arbitrary subset of the previous types, so the weighted generating polynomial is a product of \((1+z^{w_h(\tau)})\) over previous types with an extra \(qz\) for the root. Grouping equal weights gives the stated product. Setting \(z=1\) yields \(N_{h+1}=q\,2^{N_h}\). Its largest exponent is \(M_{h+1}=1+\sum_{\tau\in\mathcal U_h}w_h(\tau)\).

Complementing the chosen child-type subset sends minimum order \(a\) to \(M_{h+1}+1-a\) and preserves multiplicities (with the root color unchanged). Thus the coefficient sequence is palindromic, and the average weight at level \(h\) is \((M_h+1)/2\). Hence the maximum-order recurrence is \(M_{h+1}=1+N_h(M_h+1)/2\). The empty and full subsets are each unique for each root color, proving the two extreme coefficients.

For gap-freeness induct on \(h\). At level zero there is a type of weight one. If previous weights attain **each** integer from \(1\) through \(M_h\), then sort the positive weights \(a_1\leq\cdots\leq a_{N_h}\), with \(a_1=1\). Every later weight \(a_i\) is at most \(1+\sum_{j<i}a_j\): at least one occurrence of every smaller integer lies among its predecessors (and repeated values only increase their sum). The elementary contiguous-subset-sums induction therefore shows that subsets attain every integer from \(0\) to \(\sum_i a_i\). Adding the new root produces every size \(1\) through \(M_{h+1}\). This also proves the assertion without assuming that any finite experiment exhausts arbitrary depth.

**3. Distribution and moments.** The uniform choice of a pair \((c,S)\) is a uniform choice of root color and, independently, an inclusion decision for each previous type. Thus, with mutually independent Bernoulli\((1/2)\) variables \(B_\tau\),
\[
X_{h+1}\ \stackrel{d}{=}\ 1+\sum_{\tau\in\mathcal U_h}w_h(\tau)B_\tau.
\]
Taking means recovers the palindromic midpoint; taking variances gives \(\sigma_{h+1}^2=\frac14\sum_\tau w_h(\tau)^2\), which equals the stated recursion since the second moment of the uniformly sampled previous weight equals \(\sigma_h^2+\mu_h^2\). Every term has positive weight and \(\mathcal U_h\ne\varnothing\), hence positive variance for positive depth.

**4. Explicit normal approximation.** Center the summands as \(Y_\tau=w_h(\tau)(B_\tau-1/2)\). Their variance sum is \(\sum_\tau w_h(\tau)^2/4\), and the sum of their third absolute centered moments is \(\sum_\tau w_h(\tau)^3/8\). The Berry--Esseen inequality for independent, not necessarily identically distributed, random variables with constant \(0.56\) gives the first claimed bound.

For the second bound, let \(n=N_h\), \(A=\sum_\tau w_h(\tau)\), and \(B=\sum_\tau w_h(\tau)^2\). Since \(w_h(\tau)\leq M_h\), \(\sum w_h(\tau)^3\leq M_h B\), while Cauchy--Schwarz implies \(B\geq A^2/n\). Therefore
\[
\frac{\sum w_h(\tau)^3}{B^{3/2}}
\leq\frac{M_h}{\sqrt{B}}\leq\frac{M_h\sqrt n}{A}
=\frac{2M_h}{(M_h+1)\sqrt n}\leq\frac2{\sqrt n}.
\]
Apply this at level \(h-1\) to get the explicit bound. Because \(N_h\) tends to infinity under \(N_{h+1}=q\,2^{N_h}\), convergence to the standard normal follows.

**5. Concentration.** Hoeffding's inequality for the independent summands between zero and their weights yields
\[
\Pr\bigl(|X_{h+1}-\mu_{h+1}|\geq\varepsilon M_{h+1}\bigr)
\leq 2\exp\left(-\frac{2\varepsilon^2 M_{h+1}^2}{\sum_\tau w_h(\tau)^2}\right).
\]
Since \(\sum w_h(\tau)^2\leq M_h A\), \(A=N_h(M_h+1)/2\), and \(M_{h+1}=1+A\), the exponent coefficient satisfies \(2M_{h+1}^2/\sum w_h(\tau)^2\geq 2A/M_h=N_h(M_h+1)/M_h\geq N_h\). This proves the displayed exponential bound and the convergence in probability. \(\square\)

## Verification

The standalone `verify_modal_tree.py` has no third-party dependencies. Run `python3 verify_modal_tree.py`. It independently enumerates unlabelled unordered colored rooted tree shapes by **vertex count** through six vertices for both one and two colors, extracts their modal signatures and minimum orders, and matches the first six coefficients with the algebraic product recurrence. For small trees it also checks modal type equality against a separate recursive forth/back bisimulation predicate. It then computes complete exact polynomial histograms in tractable cases, checking every coefficient for support, palindromicity and extremes; it cross-checks the mean, variance and the Berry--Esseen upper bound against the exact finite distribution.

Examples: with no propositional atoms (\(q=1\)), the first four nontrivial \((N_h,M_h)\) pairs are \((2,2)\), \((4,4)\), \((16,11)\), and \((65536,97)\). With one propositional letter (\(q=2\)), the pairs through depth three are \((8,3)\), \((512,17)\), and \((2^{513},4609)\). The checker reports `VERIFY_OK` after all its tests. Exact finite enumeration is corroboration, not a substitute for the structural induction and probability inequalities proving the theorem at every depth.

## Relationship to prior work

Wałęga and Cuenca Grau (2026), *Preservation Theorems for Unravelling-Invariant Classes*, Sections 2–4, develop bounded tree unravellings and finite minimal-tree arguments for preservation theorems; their claims concern definability and well-quasi-ordering. Their unravelling locality and tree-minimal-witness setting motivate the **quantitative** question answered here. Neither their statements nor their tree wqo proof provide the present weighted distribution, full order spectrum or Gaussian law. The elementary modal child-type set normal form is standard and is **not** claimed as new.

Bolander and Burigana (2024), *Better Bounded Bisimulation Contractions*, construct world-minimal bounded contractions for pointed models in unrestricted Kripke graphs and analyze succinctness; a graph contraction can share states and need not remain a tree. The present theorem minimizes over finite outward trees and gives a distribution **across all depth-bounded theories**, so their general-model minimality result neither yields nor contradicts its weights. Their paper was examined through the contraction and minimization sections.

A published 2026 exact result on a 47-vertex tree realizing *all sixteen* atom-free depth-three types optimizes a **single shared tree covering every type at some vertex**; it does not give the minimum tree order separately for each type or its all-depth distribution. A separate 2026 result on graded-vs-ordinary bisimulation quotient sizes concerns **fixed-branching colored trees** and **quotient comparisons**, not the present unrestricted-branching uniform-type minimum-order random variable. Both full statements/proofs were compared. The present claimed extension is the joint full weighted enumerator, sharp gap-free support, exact moments, and an explicit normal/concentration law. Searches for these exact implications and aliases found no dominating result, but absence from searched records is not proof of historical uniqueness.

## Limitations

Minimum vertex order is **tree-relative**; arbitrary directed graphs can reuse child states and may be much smaller. Counting, converse, graded, fixpoint, or descendant modalities alter the signatures. The exact polynomial representation grows extremely rapidly with depth, so direct expansion is infeasible for moderately large \(h\); the recurrences and probabilistic estimates remain mathematically exact. The Berry--Esseen bound is an explicit upper bound, not an optimal asymptotic constant. The cited 2026 unravelling paper supplies a motivating problem setting, not an assertion that it conjectured the new quantitative law. Although pertinent full articles and published mathematical results were compared, unindexed older weighted-set enumerations or equivalent tree-compression results could affect novelty priority. No independent mathematical or historical audit has been performed.

## References

1. Przemysław Andrzej Wałęga and Bernardo Cuenca Grau. *Preservation Theorems for Unravelling-Invariant Classes: A Uniform Approach for Modal Logics and Graph Neural Networks*. arXiv:2602.01856, first posted 2026-02-02. https://arxiv.org/html/2602.01856v1.
2. Thomas Bolander and Alessandro Burigana. *Better Bounded Bisimulation Contractions*. arXiv:2405.00480, first posted 2024-05-01. https://arxiv.org/html/2405.00480v1.
3. Thomas Bolander and Alessandro Burigana. *Depth-Bounded Epistemic Planning*. arXiv:2406.01139, 2024. https://arxiv.org/abs/2406.01139.
4. Irina Shevtsova. *On the absolute constants in the Berry--Esseen inequality and its structural and nonuniform improvements*. 2013, https://www.mathnet.ru/eng/ia252 (a valid independent-summand normal-approximation constant \(0.56\)).
5. *A sharp 47-vertex tree for all sixteen depth-three modal types*. Public mathematical research note, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-47-vertex-tree-for-all-sixteen-depth-three-modal-types--dda455b75ffa.
6. *A sharp arity threshold for graded-versus-ordinary bisimulation compression of regular trees*. Public mathematical research note, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-arity-threshold-for-graded-versus-ordinary-bisimulation--818ec1eeacfe.
