# Complete first-order probability spectra at simultaneous coloured coupon thresholds

## Finding

Fix \(s\ge1\), integers \(r_1,\ldots,r_s\ge0\), and real constants \(c_1,\ldots,c_s\). For each integer \(m\to\infty\), let \(B_m\) be an \(m\)-element sort and let \(A_{i,m}\), for \(1\le i\le s\), be disjoint sorts of sizes \(n_i(m)\), where
\[
\frac{n_i(m)}m=\log m+r_i\log\log m+c_i+o(1).
\]
Choose independently, for every \(i\), a uniformly random total function \(f_i:A_{i,m}\to B_m\). The language consists of equality, these fixed named sorts and the functions, with no order, arithmetic or auxiliary predicates. Set
\[
Z_{i,m}=\#\{b\in B_m:\#f_i^{-1}(b)=r_i\},\qquad
\lambda_i=e^{-c_i}/r_i!.
\]

**Theorem (joint convergence and complete logical spectrum).** The vector \((Z_{1,m},\ldots,Z_{s,m})\) converges in distribution to independent Poisson variables \((Z_1,\ldots,Z_s)\) of means \((\lambda_1,\ldots,\lambda_s)\). Moreover, for **every** first-order sentence \(\varphi\) in the stated fixed language, there exist an integer \(T\ge1\) and a subset \(S\subseteq\{0,1,\ldots,T\}^{s}\) with
\[
\lim_{m\to\infty}\Pr(\mathcal M_m\models\varphi)
=\Pr\bigl((\min(Z_i,T))_{i=1}^{s}\in S\bigr).
\]
**Conversely**, every probability on the right, with arbitrary finite \(T\) and arbitrary \(S\), is the limiting probability of a first-order sentence in the same language. In particular, this completely characterizes the first-order limiting probability spectrum. No assertion is made that distinct descriptions yield distinct real numbers.

For example, at \(s=2\), \(r_1=r_2=0\), \(c_1=c_2=0\), the property that each bin has a preimage of both colours has limiting probability \(e^{-2}\). All finite Boolean combinations of statements about the numbers of bins with exactly \(r_i\) preimages of colour \(i\) have similarly explicit limits.

## Assumptions and scope

All asymptotics hold for fixed \(s\), fixed \(r_i,c_i\), and integer sizes \(n_i(m)\) satisfying the displayed scaling. Every source element chooses its image independently and uniformly from \(B_m\), including across distinct sorts. The sorts and function names are visible to first-order formulas; labels on their individual elements are not. A quantifier has the usual unrestricted first-order meaning (quantification over specified sorts, which is equivalent to unary sort predicates). The result concerns finite structures only, with \(m\to\infty\), and does not allow a number of colours or a sentence varying with \(m\).

## Proof

### 1. Exact factorial moments and the rare Poisson coordinates

For one colour, suppress the index and let \(Y_{j,m}\) be the number of bins with exactly \(j\) preimages. For every fixed integer \(t\ge0\), direct allocation to \(t\) distinct specified bins gives the exact identity
\[
\mathbb E(Y_{j,m})_{t}
=(m)_{t}\frac{(n)_{jt}}{(j!)^{t}m^{jt}}
\left(1-\frac tm\right)^{n-jt},
\]
interpreted as zero if \(jt>n\) or \(t>m\). Here \((x)_t=x(x-1)\cdots(x-t+1)\) is the falling factorial, and \((x)_0=1\). At \(j=r\), writing \(L_m=n/m=\log m+r\log\log m+c+o(1)\), the right side equals
\[
\bigl(m e^{-L_m}L_m^r/r!\bigr)^t(1+o(1))
\longrightarrow (e^{-c}/r!)^t.
\]
The factorial-moment criterion therefore yields \(Y_{r,m}\Rightarrow\operatorname{Poisson}(e^{-c}/r!)\). Different colours use disjoint families of random choices, so their rare counts are independent for each \(m\); the joint convergence follows.

### 2. All other fixed-size fibre types are absent or abundant

For each fixed \(j\ge0\),
\[
\mathbb E Y_{j,m}\sim\frac{e^{-c}}{j!}(\log m)^{j-r}.
\]
For \(j<r\), this tends to zero, so such bins are absent with probability tending to one. For \(j>r\), the expectation tends to infinity and the exact \(t=2\) formula above gives \(\mathbb E(Y_{j,m})_2/(\mathbb E Y_{j,m})^2\to1\), hence \(Y_{j,m}\to\infty\) in probability. These assertions hold simultaneously for any prescribed finite range of \(j\) and all finitely many colours.

For every fixed integer \(M\ge1\) and distinct colours \(i,h\), independence of the maps implies
\[
\mathbb E\#\{b:\#f_i^{-1}(b)<M,\ \#f_h^{-1}(b)<M\}
\le O\left(\frac{(\log m)^{2M}}m\right)\longrightarrow0.
\]
Indeed each one-colour small-fibre probability is \(O((\log m)^M/m)\), with constants depending on its fixed \(r_i,c_i\). Therefore, with probability approaching one, no bin has small fibres in two different colours. In particular, for any fixed \(M>\max_i r_i\), every bin belongs to exactly one of these categories: all its colour fibres have size at least \(M\); or exactly one colour \(i\) has a fibre of size \(j<M\). All classes with \(j<r_i\) are absent, the \(j=r_i\) classes have count \(Z_{i,m}\) up to an event of vanishing probability, and the \(r_i<j<M\) classes contain arbitrarily many bins in probability. The all-large class also contains arbitrarily many bins because the total number of bins with any fibre below \(M\) is \(O_{\Pr}((\log m)^{M})=o_{\Pr}(m)\).

### 3. Finite-round indistinguishability

Fix a quantifier rank \(q\ge1\) and set \(M=1+\max\{q,r_1,\ldots,r_s\}\). Call a finite structure \(q\)-regular if: (a) no bin has a fibre smaller than \(r_i\) in colour \(i\), and no bin has two colour fibres smaller than \(M\); (b) for each \(i\), each fibre-size class \(r_i<j<M\) has at least \(q\) bins, with all other colour fibres large; and (c) there are at least \(q\) all-large bins. Step 2 shows \(\Pr(\mathcal M_m\text{ is }q\text{-regular})\to1\).

We prove the following deterministic Ehrenfeucht–Fraïssé lemma: two \(q\)-regular structures with the same truncated vector \((\min(Z_i,q))_{i=1}^s\) satisfy the same sentences of quantifier rank at most \(q\). For the \(q\)-round game, group the bins by their vector of fibre cardinalities, each cardinality replaced by the symbol \(\ge M\) once it reaches \(M\). For any finite group below \(M\), bins with that group have exactly the stated finite fibre sizes; a fibre marked \(\ge M\) has more than \(q\) distinct elements. Each nonexceptional group has at least \(q\) bins on both sides, while for the exceptional group \((\ge M,\ldots,r_i,\ldots,\ge M)\) the two bin counts either agree below \(q\) or are both at least \(q\).

Duplicator maintains a partial bijection between bins already chosen **or implicitly named as images of chosen source elements**, preserving bin groups, and preserves the equalities, colours, and images of all chosen source elements. On a new bin, choose an unused bin of its group; at most \(q\) such groups' bins can be mentioned within \(q\) moves, while exceptional groups of cardinality below \(q\) can be matched bijectively. On a new source element of colour \(i\), first match its image bin by the same rule, then select an unused source element in its corresponding fibre. That fibre has either the same specified cardinality below \(M\), or size at least \(M>q\), hence supports the extension. Reverse moves are symmetric. Function values and equality are preserved, which is precisely partial isomorphism in this language. The lemma follows from the game theorem. Consequently the truth of \(\varphi\), on \(q\)-regular structures, is determined by the finite vector of rare counts truncated at \(q\). There are finitely many vectors, defining a subset \(S\); coupling the Poisson convergence from Step 1 with the high-probability regularity yields the stated limit.

### 4. Exhaustiveness of the limiting spectrum

For each \(i\) and fixed \(r_i\), the formula \(C_i(b)\) saying that \(b\) has **exactly** \(r_i\) distinct \(i\)-preimages is first-order: list the prescribed distinct preimages and universally exclude all others; for \(r_i=0\), simply assert that no \(i\)-element maps to \(b\). The sentence saying there are exactly \(k\) bins satisfying \(C_i\), or at least \(T\) such bins, is therefore first-order for each fixed \(k,T\). Conjunctions across colours and disjunctions over \(S\subseteq\{0,\ldots,T\}^{s}\) define exactly the event \((\min(Z_{i,m},T))_i\in S\) at every finite \(m\). Step 1 gives the converse limit, completing the classification. The argument is constructive at the level of finite-round bin types and finite Boolean combinations, but claims no complexity bound for computing the representative types.

## Verification

The standalone Python 3 checker `checker.py` uses only the standard library. It enumerates all functions with up to four bins and five source elements, checks 312 exact factorial-moment identities, checks 3,168 two-colour product-moment identities for independent maps, and evaluates three finite-size examples showing convergence toward the predicted means. Execute `python3 checker.py` and expect the marker `CRITICAL_COLOURED_FIBRE_CHECKS_OK`. These tests verify finite formulas and examples only; the infinite joint limit and logical spectrum rest on Steps 1–4.

## Relationship to prior work

The occupancy step is the classical repeated-coupon-collector/Poisson phenomenon, not claimed as novel. Ilienko (2026) analyzes limits for an extended multi-collection coupon collector and distinct completion-time questions. Koponen (2026, especially Remark 2.15) motivates first-order convergence laws for random expansions of finite base structures, but develops finite-model and model-theoretic criteria rather than the coloured-function critical-window classification above. Baron, Drmota and Mutafchiev (1996) study predecessor counts in uniform self-maps with a single domain/codomain of equal size, a different scaling and no first-order spectrum. Adam-Day, Benedikt and Larrauri (2025) establish convergence results for richer logics under different random-structure hypotheses, while Demin and Zhukovskii (2024) give broader notions of first-order limit-law complexity. The asserted new component is the complete, all-quantifier-rank **probability-spectrum equivalence** for independent multicolour maps at each simultaneously critical occupancy level. An unidentified equivalent result in previous logical limit-law literature remains possible.

## Limitations

The result assumes finitely many fixed sorts and **independent uniform** functions. The source sizes must lie in the specified critical windows; it is not a theorem for arbitrary biased sampling, correlated maps, built-in order, counting quantifiers, or increasing quantifier rank. It gives convergence, not a uniform error rate. The inspected published literature does not exclude every possible historical equivalent. Independent verification and historical-priority review have not been performed.

## References

1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first submitted 2026-10-12), https://arxiv.org/html/2610.16163v1 .
2. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, Modern Stochastics: Theory and Applications (published online 2026-08-11), https://doi.org/10.15559/26-VMSTA306 .
3. S. Adam-Day, M. Benedikt, A. Larrauri, *Convergence Laws for Extensions of First-Order Logic with Averaging*, arXiv:2504.14270 (2025), https://arxiv.org/abs/2504.14270 .
4. D. Demin, M. Zhukovskii, *First order complexity of finite random structures*, LICS 2024, https://doi.org/10.1145/3661814.3662127 .
5. G. Baron, M. Drmota, L. Mutafchiev, *Predecessors in Random Mappings*, Combinatorics, Probability and Computing 5 (1996), 317–335, https://doi.org/10.1017/S0963548300002091 .
