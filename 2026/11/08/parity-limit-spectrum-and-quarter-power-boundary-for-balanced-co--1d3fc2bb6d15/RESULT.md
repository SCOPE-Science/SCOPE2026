# Parity-limit spectrum and quarter-power boundary for balanced counting-modal formulas

## Finding
Let \(T_n\) be the full rooted directed \(n\)-ary tree of depth exactly two, with independent fair truth values for a single unary proposition \(p\). Write \(\#\chi\) for the number of immediate successors satisfying \(\chi\), and at a depth-one node define
\[
\theta_a:=\bigl(\#p-\#\neg p=a\bigr),\qquad a\in\mathbb Z.
\]
At the root let \(C_a:=\#\theta_a\). Every Boolean combination \(\Phi\) of finitely many fixed-threshold atoms
\[
C_a-C_b\ge h\quad\text{and}\quad C_a\ge t,
\qquad a,b,h,t\in\mathbb Z,
\]
has rational limiting truth probabilities \(L_0(\Phi)\) and \(L_1(\Phi)\) along even and odd branching degrees, respectively. They can be computed exactly by counting permutations of the active offsets; the unrestricted limit exists precisely when these two rationals agree. Moreover, the exact spectrum of pairs is
\[
\bigl\{(L_0(\Phi),L_1(\Phi)):\Phi\text{ in the indicated fragment}\bigr\}
=(\mathbb Q\cap[0,1])^2.
\]
This uses only one unary proposition and modal depth two.

For any distinct fixed integers \(a,b\) of the same parity and any fixed integer \(h\), along branching degrees \(n\equiv a\pmod2\), the following universal lattice correction holds:
\[
\Pr\bigl(C_a-C_b\ge h\bigr)
=\frac12+\frac{\frac12-h}{2(2\pi)^{1/4}}n^{-1/4}
+o(n^{-1/4}). \tag{1}
\]
In particular the single depth-two formula
\[
\Psi:=\bigl[(C_0-C_2\ge0)\land(C_0\ge1)\bigr]
\lor\bigl[(C_1-C_3\ge0)\land(C_1\ge1)\bigr]
\]
converges without restricting to a parity class, but has the **sharp nonzero leading correction**
\[
\Pr(T_n,\mathrm{root}\models\Psi)
=\frac12+\frac{1}{4(2\pi)^{1/4}}n^{-1/4}+o(n^{-1/4}). \tag{2}
\]
The conclusions concern uniform independent labels on the fixed full tree, not sampling unlabelled trees or sampling an arbitrary tree with a branching bound.

## Assumptions and scope
The frame has one root, exactly \(n\) children of the root, and exactly \(n\) leaves below each of these children. Its only edges are parent-to-child edges. All its vertices are independently labelled \(p\) or \(\neg p\) with probability \(1/2\), but only leaf labels affect the displayed formulas. The language permits integer linear comparisons of successor counts, Boolean connectives, and their nesting to depth two. The offsets and all thresholds in any one formula are fixed integers, independent of \(n\); the set of offsets is finite. An equality is shorthand for two opposing inequalities. A vacuous active set is handled by deterministic evaluation.

## Proof
**Exact category law.** For a root child \(v\), let \(B_v\) be the number of its \(p\)-labelled leaves. Independently for the \(n\) children, \(B_v\sim\operatorname{Bin}(n,1/2)\). Put \(S_v=2B_v-n\). For a fixed integer \(a\),
\[
\pi_{n,a}:=\Pr(S_v=a)=
\begin{cases}
2^{-n}\binom{n}{(n+a)/2},&|a|\le n,\ n\equiv a\pmod2,\\
0,&\text{otherwise}.
\end{cases} \tag{3}
\]
For distinct offsets, \((C_a)\) is a subvector of a multinomial count with \(n\) trials, category probabilities \((\pi_{n,a})\), and a residual category. Let \(c=\sqrt{2/\pi}\). For each fixed finite offset set, Stirling's formula and the ratio of adjacent central binomial coefficients give, uniformly over its compatible offsets,
\[
\pi_{n,a}=c n^{-1/2}+O(n^{-3/2}),\quad
n\pi_{n,a}=c\sqrt n+O(n^{-1/2}). \tag{4}
\]
In particular, every compatible category count is positive with probability \(1-\exp[-c\sqrt n+O(1)]\); incompatible counts vanish identically.

**Joint square-root-count fluctuations.** Fix a parity \(\varepsilon\in\{0,1\}\) and let \(A_\varepsilon\) be the offsets of that parity in the formula. The centered vector
\[
\left(\frac{C_a-c\sqrt n}{n^{1/4}}\right)_{a\in A_\varepsilon}
\quad\Longrightarrow\quad (Z_a)_{a\in A_\varepsilon},
\qquad Z_a\text{ independent }N(0,c), \tag{5}
\]
as \(n\to\infty\) with \(n\equiv\varepsilon\pmod2\). Indeed, for fixed real coefficients \((t_a)\), the characteristic function of the multinomial sum is
\[
\left(1+\sum_{a\in A_\varepsilon}\pi_{n,a}
 (e^{it_a/n^{1/4}}-1)\right)^n.
\]
After subtracting the center \(c\sqrt n\), its logarithm tends to \(-c\sum_a t_a^2/2\): the linear errors in (4) are \(O(n^{-3/4})\), and the cross-category quadratic terms from the logarithm are \(O(n^{-1/2})\). This proves (5) by characteristic-function convergence. The limit is absolutely continuous, so all active counts are distinct with probability tending to one, and every strict ordering of the active offsets has limiting probability \(1/|A_\varepsilon|!\).

**Exact parity-limit algorithm.** Given a Boolean combination of the specified atoms, fix \(\varepsilon\) and enumerate all permutations of \(A_\varepsilon\). In the evaluation associated with one permutation: (i) replace each active \(C_a\) by a positive, mutually distinct score with the specified ordering; (ii) replace each inactive \(C_a\) by zero; (iii) evaluate an atom \(C_a-C_b\ge h\) for distinct active offsets by the strict sign of the rank comparison, for two inactive offsets by \(0\ge h\), for active versus inactive by true, and for inactive versus active by false; (iv) evaluate \(C_a-C_a\ge h\) by \(0\ge h\), and \(C_a\ge t\) by true for active offsets or by \(0\ge t\) for inactive offsets. The fixed threshold does not change a comparison between distinct active counts because their fluctuations in (5) grow at scale \(n^{1/4}\), while exact ties have vanishing probability. Let \(N_\varepsilon(\Phi)\) be the number of permutations for which this Boolean evaluation is true. Then
\[
L_\varepsilon(\Phi)=\frac{N_\varepsilon(\Phi)}{|A_\varepsilon|!}. \tag{6}
\]
For \(|A_\varepsilon|=0\), the denominator is \(0!=1\) and the deterministic evaluation applies. This proves rationality and that full-sequence convergence is equivalent to \(L_0=L_1\).

**Attainability of every rational pair.** Given \(u_0,u_1\in\mathbb Q\cap[0,1]\), choose \(k\ge2\) such that the denominators of both rationals divide \(k!\). Select \(k\) distinct even offsets \(0,2,\dots,2k-2\) and \(k\) distinct odd offsets \(1,3,\dots,2k-1\). For each parity, choose exactly \(u_\varepsilon k!\) of the \(k!\) strict score orders, and express their disjunction by comparisons \(C_a-C_b\ge1\). Conjoin the even branch with \(C_0\ge1\) and the odd branch with \(C_1\ge1\), and disjoin both branches. Wrong-parity gates are identically false, while the correct-parity gate is true with probability tending to one. Equation (5) gives the respective limits \(u_0,u_1\). Thus (6) has exactly the claimed rational-pair range, not just a dense subset.

**Local lattice correction.** For fixed distinct compatible \(a,b\), let \(D_n=C_a-C_b\). Each of the \(n\) root children contributes \(+1\), \(-1\), or \(0\), with probabilities \(\pi_{n,a}\), \(\pi_{n,b}\), and \(1-\pi_{n,a}-\pi_{n,b}\). Writing \(p=\pi_{n,a}\), \(q=\pi_{n,b}\), Fourier inversion yields for each fixed integer \(j\)
\[
\Pr(D_n=j)=\frac{1}{2\pi}\int_{-\pi}^{\pi}
(1-p-q+pe^{it}+qe^{-it})^n e^{-ijt}\,dt. \tag{7}
\]
Here \(p,q=c n^{-1/2}+O(n^{-3/2})\). At \(t=u n^{-1/4}\), the logarithm of the factor raised to the \(n\)th power tends to \(-cu^2\), uniformly for bounded \(u\). On the complementary range the modulus is dominated by \(\exp[-C\sqrt n(1-\cos t)]\) for a fixed \(C>0\), using
\[
1-|1-p-q+pe^{it}+qe^{-it}|^2
=2(1-p-q)(p+q)(1-\cos t)+2pq(1-\cos2t).
\]
Dominated Fourier scaling therefore gives, for every fixed \(j\),
\[
\Pr(D_n=j)=\frac{1}{2\sqrt{\pi c}}n^{-1/4}+o(n^{-1/4})
=\frac{1}{2(2\pi)^{1/4}}n^{-1/4}+o(n^{-1/4}). \tag{8}
\]
Swapping the labels of categories \(a,b\) changes the law of any one trial by total variation distance \(|p-q|=O(n^{-3/2})\), so a coupling of all \(n\) trials changes the distribution by at most \(n|p-q|=O(n^{-1/2})\). Under the swapped law \(D_n\) is distributed as \(-D_n\). Hence \(\Pr(D_n>0)-\Pr(D_n<0)=O(n^{-1/2})\). Combining this with (8), and adding or subtracting finitely many masses \(\Pr(D_n=j)\) to move from threshold zero to threshold \(h\), gives (1).

**A convergent sharp example.** In \(\Psi\), the even branch is identically false when \(n\) is odd and the odd branch is identically false when \(n\) is even. On the matching parity, the positive-count gate fails with probability at most \(\exp[-c\sqrt n+O(1)]\). Thus (1) with \(h=0\) applies on both parities with the same constant, proving (2). Since that constant is strictly positive, the exponent \(1/4\) cannot be replaced by any larger power in a bound valid for every convergent formula in this fragment.

## Verification
The standalone `checker.py` uses only Python's standard library. Run `python checker.py`. It independently enumerates all leaf valuations for \(n\le4\) and compares their exact probabilities with the multinomial category formulas for several distinct offset pairs and comparison thresholds. It also checks the parity-gated formula and numerically solves the one-dimensional count-difference distribution for \(n=100,400,1600\), reporting its scaled tie mass and weak-comparison excess. The observed finite values approach the analytical constants. These finite tests cannot establish (5), the universal permutation formula (6), or the infinite asymptotics (8); the characteristic-function and Fourier arguments above do so.

## Relationship to prior work
Ghosh and Schwarzentruber, *On Counting Graphs for Modal Logic with Counting* (arXiv:2610.26187, first publicly posted 2026-10-19), examine model-counting complexity and convergence for counting-modal logic. Their Section 6.1 exhibits a parity-oscillating tree formula, while Section 6.2 studies a recursive replacement limit via Gaussian inequalities with fixed lower-level probabilities. The present result instead treats a joint family of lower-level categories whose probabilities vanish like \(n^{-1/2}\); their root counts diverge like \(\sqrt n\) and fluctuate on the \(n^{1/4}\) scale. It gives an exact parity-limit spectrum and an explicit lattice correction for the *ordinary* probabilities on full depth-two trees. Classical central binomial asymptotics, multinomial characteristic functions, and Fourier inversion are used as standard tools rather than claimed as new.

## Limitations
Only one fair unary predicate, exact full branching and depth two, and formulas assembled from finitely many fixed-offset balance categories with fixed integer linear thresholds are covered. Other counting-modal formulas, variable branching degrees inside the tree, biased labels, and offsets growing with \(n\) are outside the theorem. The sharp correction is proved for two-category comparisons, not for every Boolean formula in the fragment. No claim about the complexity of deciding convergence for unrestricted counting-modal logic is made. Independent mathematical validation and exhaustive historical-priority certification have not been performed.

## References
1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1, 2026-10-19, https://arxiv.org/html/2610.26187 and https://arxiv.org/abs/2610.26187.
2. Classical Stirling central-binomial asymptotics and characteristic-function inversion for lattice sums; standard results are used in self-contained specializations above.
