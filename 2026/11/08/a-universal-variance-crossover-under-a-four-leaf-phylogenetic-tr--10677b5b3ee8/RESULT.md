# A universal variance crossover under a four-leaf phylogenetic tree rotation

## Finding

The independent-extinction model for rooted phylogenetic diversity admits an explicit, sharp family of topology-dependent variance reversals. For every integer \(n\geq 4\), define the rooted, nonplane, full-binary caterpillar \(C_n\) recursively by \(C_1=\bullet\) and \(C_n=(\bullet,C_{n-1})\). Define \(B_4=((\bullet,\bullet),(\bullet,\bullet))\), and \(B_n=(\bullet,B_{n-1})\) for \(n\geq5\). Each edge has length one, including every terminal edge, and there is no stem above the root. Every leaf survives independently with probability \(1-q\), where \(0<q<1\). Let \(X_T(q)\) be the rooted phylogenetic diversity (the number of edges joining the root to at least one surviving leaf), and put \(V_T(q)=\operatorname{Var} X_T(q)\).

For all \(n\geq4\), the two trees have the same number of leaves, and

\[
\mathbb E X_{C_n}(q)-\mathbb E X_{B_n}(q)=q^2(1-q)>0,
\]

but their variance difference is

\[
V_{C_n}(q)-V_{B_n}(q)=q^2(1-q)\,H_n(q),\quad
H_n(q)=q^3+3q^2+8q-5+2\sum_{j=4}^{n-1}q^j.
\]

The sum is empty for \(n=4\). For every \(n\geq4\), \(H_n\) has exactly one root \(q_n\) in \((0,1)\): \(V_{C_n}<V_{B_n}\) for \(0<q<q_n\), while \(V_{C_n}>V_{B_n}\) for \(q_n<q<1\). The thresholds strictly decrease with \(n\), with \(q_5=1/2\) and

\[
q_n\downarrow q_\infty\approx0.491144250260296,
\qquad q_\infty^4-2q_\infty^3-5q_\infty^2+13q_\infty-5=0.
\]

Here \(q_\infty\) is the unique zero of this polynomial in \((0,1/2)\). Four is the smallest leaf count at which two different unlabelled rooted full-binary tree shapes with unit edges can exhibit any topology-ranking reversal: for one, two or three leaves, there is only one such shape.

Thus a tree topology can have strictly higher *expected* future phylogenetic diversity at all extinction risks but lower *variance* at low risk and higher variance at high risk. This is a statement about the precise independent-extinction model, not about optimal real-world conservation policies.

## Assumptions and scope

A rooted full-binary tree has exactly two children at every internal vertex. Child order and tip labels do not define distinct tree shapes. The root is included in PD even when no taxa survive, in which case PD is zero. All \(2n-2\) edges have length one. The probability \(q\) is the common *extinction* probability, not survival probability. Extinctions are independent across taxa. The topology pair differs only in the arrangement of the four leaves at the deepest end of a caterpillar backbone; no molecular-clock or ultrametric assumption is made.

## Proof

**1. Exact edge-covariance identity.** For each edge \(e\), let \(D_e\) be its descendant-leaf set and \(d_e=|D_e|\). Let \(I_e\) equal one if some leaf in \(D_e\) survives and zero otherwise, so \(X_T=\sum_e I_e\). Then

\[
\mathbb E I_e=1-q^{d_e},\qquad \operatorname{Var}I_e=q^{d_e}(1-q^{d_e}).
\]

If \(D_e\cap D_f=\varnothing\), independence gives zero covariance. If \(D_f\subsetneq D_e\), then \(I_f=1\) forces \(I_e=1\), giving

\[
\operatorname{Cov}(I_e,I_f)=q^{d_e}(1-q^{d_f}).
\]

The reverse inclusion is symmetric. Consequently

\[
V_T(q)=\sum_e q^{d_e}(1-q^{d_e})
+2\sum_{D_f\subsetneq D_e}q^{d_e}(1-q^{d_f}).\tag{1}
\]

Equation (1) follows directly from the indicators; its general form is prior work (Faller, Pardi and Steel, 2007, Lemma 1.1).

**2. Four-leaf calculation.** For the four-leaf caterpillar \(C_4\), the nontrivial edge clade sizes are \(2,3\), in addition to four singleton edges. For \(B_4\), they are \(2,2\), in addition to the same four singleton edges. Applying (1) gives

\[
\begin{aligned}
V_{C_4}(q)&=q(1-q)(q^4+3q^3+10q^2+5q+4),\\
V_{B_4}(q)&=2q(1-q)(q^2+5q+2),\\
V_{C_4}(q)-V_{B_4}(q)&=q^2(1-q)(q^3+3q^2+8q-5).
\end{aligned}\tag{2}
\]

The expectation identity follows from summing \(1-q^{d_e}\), because the four pendant contributions cancel and \((1-q^3)-(1-q^2)=q^2(1-q)\).

**3. Grafting onto a longer backbone.** For \(n>4\), the two trees consist of the same caterpillar backbone above the bottom four leaves. Their newly shared ancestral edges have descendant-clade sizes \(4,5,\ldots,n-1\), and the rest of the nonbottom leaf edges are also shared. Every new edge has the same marginal variance in both trees. A new ancestral edge with \(j\) descendant leaves covaries with all edges below the bottom four-leaf subtree by \(q^j\) times the mean contribution of these bottom edges. Consequently the *difference* in the sum of its covariance terms is exactly \(2q^j\,[q^2(1-q)]\). Other added covariances are either identical or zero by disjointness. Summing over \(j=4,\ldots,n-1\) and using (2) proves the displayed variance formula for every \(n\ge4\). The expected-PD difference remains \(q^2(1-q)\) because all shared-edge means cancel.

**4. One strictly moving crossover.** For \(0<q<1\),

\[
H_n'(q)=3q^2+6q+8+2\sum_{j=4}^{n-1}j q^{j-1}>0.
\]

Also \(H_n(0)=-5\) and \(H_n(1)=2n-1>0\), giving precisely one interior root. The positive prefactor \(q^2(1-q)\) proves both strict variance rankings. Furthermore, \(H_{n+1}(q)=H_n(q)+2q^n>H_n(q)\) inside \((0,1)\), so \(q_{n+1}<q_n\). The infinite geometric sum converges uniformly on \([0,q_4]\), since \(q_4<1\). Its strictly increasing limit

\[
H_\infty(q)=q^3+3q^2+8q-5+\frac{2q^4}{1-q}
\]

has a unique zero there, proving convergence. Multiplication by \(1-q\) gives \(q^4-2q^3-5q^2+13q-5=0\). Substitution gives \(H_5(1/2)=0\). The root \(q_\infty\) lies below \(1/2\) because \(H_\infty(1/2)>0\), and its displayed decimal is a numerical approximation rather than a defining condition.

**5. Sharp leaf count.** Full-binary rooted nonplane shapes with \(1,2,3\) leaves are unique by the recursive root split. With \(4\) leaves the caterpillar and balanced fork are nonisomorphic, and steps 1–4 prove a strict reversal. The minimum four-leaf assertion therefore follows without assuming any unproved finite-exhaustion claim.

## Verification

Run `python3 check_pd_swap.py` with Python 3.9 or later from the directory containing this file. It uses only the Python standard library. The checker independently derives polynomial expectations and variances from all edge-clade covariances for \(n=4,\ldots,12\), and compares these with the displayed formulas. For \(n=4,\ldots,9\), it separately enumerates all \(2^n\) possible surviving subsets, constructs their exact polynomial probabilities, computes the first and second moments, and compares both methods coefficient by coefficient. It also counts unlabelled nonplane full-binary shapes for \(n=1,2,3,4\) and performs exact rational sign/derivative tests at selected larger orders. The reported run produced `PASS: 61 symbolic/independent finite checks` and two additional PASS lines. The all-\(n\) assertion is justified analytically in the proof, not inferred from finite computation.

## Relationship to prior work

Faller, Pardi and Steel (2007 preprint; 2008 journal article) define the generalized field-of-bullets model and prove the general PD variance covariance formula as their Lemma 1.1. The present formula is a specialization of that identity *plus* a topology-pair comparison, proof of exactly one switch for every \(n\), strict movement of the switch, and a limiting algebraic threshold. The known general variance identity is not claimed as new. Faith (2008) motivates distinguishing expected diversity from uncertain or risk-sensitive outcomes, but does not derive this topology-switching family. Nipperess and Matsen (2013) provide formulas for rarefaction under a fixed sample budget, which is a different sampling law. The rank reversals of Fischer, Francis and Wicke (2022) concern a species-level Fair Proportion score after taxa are removed, not comparisons of variance of total future PD as a function of independent extinction probability.

## Limitations

The result is a stylized mathematical counterexample in rooted unit-edge binary trees, with independent homogeneous extinction and no stem. It is not an optimization theorem for *all* tree topologies or branch lengths and makes no claim about ultrametric trees, correlated extinctions, unrooted PD, or intervention priorities. The source's general variance identity makes the polynomial calculations possible; the historical originality of the specific crossover classification cannot be independently guaranteed without an exhaustive literature review.

## References

1. B. Faller, F. Pardi and M. Steel, *Distribution of phylogenetic diversity under random extinction*, first publicly available 2 August 2007, arXiv:0708.0425, https://arxiv.org/abs/0708.0425 ; Journal of Theoretical Biology 251 (2008), 286–296, https://doi.org/10.1016/j.jtbi.2007.11.034.
2. D. P. Faith, *Threatened Species and the Potential Loss of Phylogenetic Diversity: Conservation Scenarios Based on Estimated Extinction Probabilities and Phylogenetic Risk Analysis*, Conservation Biology 22 (2008), 1461–1470, https://doi.org/10.1111/j.1523-1739.2008.01068.x.
3. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, Methods in Ecology and Evolution 4 (2013), 566–572, https://doi.org/10.1111/2041-210X.12042.
4. M. Fischer, A. Francis and K. Wicke, *Phylogenetic Diversity Rankings in the Face of Extinctions: The Robustness of the Fair Proportion Index*, Systematic Biology 72 (2023), 606–619; preprint 1 July 2021, https://arxiv.org/abs/2107.00748.
