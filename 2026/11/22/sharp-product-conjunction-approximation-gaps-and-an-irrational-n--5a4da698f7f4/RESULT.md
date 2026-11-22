# Sharp product-conjunction approximation gaps and an irrational nonattainment threshold

## Finding
Let \(n\ge2\), and let \(P_n(x_1,\ldots,x_n)=\prod_{i=1}^n x_i\) be the \(n\)-ary *product t-norm*, viewed as a truth function on \([0,1]^n\). Define
\[
 t_n=n^{-1/(n-1)},\qquad h_n=t_n-t_n^n=(n-1)n^{-n/(n-1)},\qquad e_n=h_n/2.
\]
For the **universal pointed-model uniform-error problem** in the languages defined below:

1. The smallest uniform error in the plain Zadeh fuzzy modal language is exactly \(h_n\), attained by the weak conjunction \(p_1\wedge\cdots\wedge p_n\).
2. The infimum of the uniform errors in the rational-constant non-expansive fuzzy modal language is exactly \(e_n\). It is attained for \(n=2\), by \((p_1\wedge p_2)\ominus\frac18\), but **is not attained by any finite formula for any \(n\ge3\)**.
3. With arbitrary real truth constants allowed, the non-expansive optimum \(e_n\) is attained by \((p_1\wedge\cdots\wedge p_n)\ominus e_n\).

Here \(a\ominus c=\max(0,a-c)\). For every optimal real-constant non-expansive formula \(G\), the restriction \(g(s)\) to the one-world, unit-loop, all-atoms-equal valuation satisfies the **forced diagonal law**
\[
 g(s)=s-e_n\quad\text{for all }t_n\le s\le1.
\]
The gap is a strict arithmetic attainment dichotomy: \(e_2=1/8\) is rational, whereas \(e_n\) is irrational for every \(n\ge3\). Moreover \(e_n\to1/2\) as \(n\to\infty\). Allowing arbitrary modal depth does not improve any of these universal errors.

## Assumptions and scope
The truth set is the standard real unit interval. A pointed fuzzy Kripke model \((W,R,V,w)\) has \(W\ne\varnothing\), an arbitrary relation \(R:W^2\to[0,1]\), a valuation \(V(p_i,v)\in[0,1]\), and a world \(w\in W\). The target at \(w\) is \(P_n(V(p_1,w),\ldots,V(p_n,w))\). For an approximating formula \(G\), its error is
\[
 \operatorname{Err}(G)=\sup_{(W,R,V,w)}\left|V(G,w)-P_n(V(p_1,w),\ldots,V(p_n,w))\right|.
\]
The supremum includes every nonempty finite or infinite world set and all atomic valuations. Only \(p_1,\ldots,p_n\) are permitted as atoms in \(G\). All formulas are finite.

The plain Zadeh language uses constants \(0,1\), atoms, \(\wedge=\min\), \(\vee=\max\), \(\neg a=1-a\), and the modal operators \(\Diamond\varphi(w)=\sup_v\min(R(w,v),V(\varphi,v))\) and its dual \(\Box\varphi=\neg\Diamond\neg\varphi\). The rational non-expansive language extends this language with all rational constants in \([0,1]\) and unary truncated shifts \(a\ominus c=\max(0,a-c)\) and \(a\oplus c=\min(1,a+c)\) for rational \(c\in[0,1]\). The real-constant version allows all real \(c\in[0,1]\) in the same operations. The *target* product conjunction is not a primitive operation of any of these three approximation languages.

The all-model formulation is essential. In particular the singleton reflexive model \(W=\{w\},R(w,w)=1\) is included, where both modalities evaluate as the identity and all rational-term values on rational atomic inputs are rational.

## Proof
**Step 1: sharp product-versus-min envelope.** For \(x\in[0,1]^n\), put \(m=\min_i x_i\), \(p=\prod_i x_i\). One has
\[
 m^n\le p\le m.
\]
The lower bound holds because every factor is at least \(m\); the upper bound because one factor is \(m\) and all others are at most one. Therefore
\[
 0\le m-p\le m-m^n\le h_n.
\]
The scalar function \(u-u^n\) has derivative \(1-nu^{n-1}\), uniquely maximized at \(u=t_n\) with maximum \(h_n\). At the constant vector \((t_n,\ldots,t_n)\), both envelope inequalities are equalities: the discrepancy \(m-p\) is \(h_n\). Thus the plain Zadeh term \(\bigwedge_i p_i\) has exactly error \(h_n\).

**Step 2: universal rational/real non-expansive upper bound.** For any real \(c\in[0,1]\), set \(H_c(x)=\max(0,m-c)\). If \(m<c\), then \(|H_c-p|=p\le m<c\). If \(m\ge c\), then \(p\in[m^n,m]\), so
\[
 |H_c-p|\le\max\{c,\,m-m^n-c\}\le\max\{c,\,h_n-c\}.
\]
Hence, with \(c=e_n=h_n/2\), the real-constant term \(H_{e_n}\) has uniform error at most \(e_n\). The lower bound in Step 3 makes the error exactly \(e_n\). For rational shifts \(q\to e_n\), the clipping map is \(1\)-Lipschitz in its shift parameter; thus
\[
 \operatorname{Err}(H_q)\le e_n+|q-e_n|\longrightarrow e_n.
\]
This proves the rational-language upper bound as an **infimum**, without asserting attainment.

**Step 3: absolute non-expansive lower bound and rigidity.** Restrict any modal formula to the one-world reflexive model. Each formula in either non-expansive language induces a \(1\)-Lipschitz function of the atomic vector in the sup norm: this holds for projections/constants and is preserved by negation, min, max, shifts, and the identity modalities. Consider \(a=(1,\ldots,1)\) and \(b=(t_n,\ldots,t_n)\). Their sup distance is \(1-t_n\), while their product target values differ by \(1-t_n^n\). If a function \(g\) has error at most \(E\), then
\[
 1-t_n^n\le E+(1-t_n)+E,
\]
which forces \(E\ge(t_n-t_n^n)/2=e_n\). When equality holds, every step in this inequality must be tight. In particular
\[
 g(a)=1-e_n,\qquad g(b)=t_n^n+e_n=t_n-e_n.
\]
The one-dimensional diagonal restriction is \(1\)-Lipschitz and has endpoint difference exactly \(1-t_n\). The two endpoint Lipschitz bounds then force \(g(s,\ldots,s)=s-e_n\) for all \(s\in[t_n,1]\). This proves the stated rigidity for every optimal formula, regardless of modal depth.

**Step 4: no rational-constant optimum beyond two inputs.** On the one-world reflexive model, assigning the rational value one to every atom makes every finite rational-language formula evaluate to a rational number: each allowed operation preserves rationals and the modalities are identities. If such a formula attained the error \(e_n\), Step 3 would force its value there to be \(1-e_n\). For \(n\ge3\), \(n^{1/(n-1)}\) is irrational: a rational root of the monic integer polynomial \(X^{n-1}-n\) would be an integer, but no integer \(k\ge2\) has \(k^{n-1}=n\) because \(2^{n-1}>n\). Therefore \(e_n=(n-1)/(2n\,n^{1/(n-1)})\) is irrational. This contradicts rational evaluation and proves nonattainment. At \(n=2\), \(e_2=1/8\) and the explicit rational formula in the finding attains it. The limit \(e_n\to1/2\) follows from \(t_n=\exp(-\log n/(n-1))\to1\) and \(h_n=t_n(1-1/n)\to1\).

**Step 5: sharp plain-Zadeh lower bound.** Again restrict to the one-world unit loop, and then to all-atom-equal inputs \((s,\ldots,s)\). On \(1/2<s<1\), the four functions \(0,1-s,s,1\) are in fixed strict order and are permuted by negation; min/max select one of them. Consequently **every** plain-Zadeh formula agrees, over this entire open interval, with exactly one of these four functions (the modalities remain identities). Its value at \(s=1\) is Boolean. Any putative error strictly below \(h_n<1\) requires value one there. By continuity and the four-function description, its branch on \((1/2,1)\) must then be either \(s\) or \(1\). The branch \(1\) incurs error \(1-2^{-n}>h_n\) by continuity at \(s=1/2\): indeed \(h_n<(n-1)/n\le1-2^{-n}\). The branch \(s\) incurs error \(t_n-t_n^n=h_n\) at \(s=t_n\) when \(n>2\), and in the limit \(s\downarrow1/2\) when \(n=2\). Thus no plain-Zadeh formula improves on the term of Step 1.

Combining the steps completes the proof for every integer \(n\ge2\) and all finite formula depths. \(\square\)

## Verification
The accompanying standalone `checker.py` (Python 3 standard library only) independently evaluates the product target and min-based approximants on rational grids for arities \(2,3,4,5\), checks the analytic two-point lower-bound identity for arities \(2\) through \(100\), and checks \(27,000\) rational-shift approximation inequalities using exact rational arithmetic for truth values and a conservative floating-point tolerance for the transcendental sharp constants. Run `python checker.py`; the expected marker is `VERIFY_OK`. These finite tests corroborate the analytic proof; they do not establish supremum statements over all real vectors or infinite Kripke structures. The irrationality and modal-depth claims are established in Steps 3–5, not by enumeration.

## Relationship to prior work
Gebhart, Schröder and Wild (2026, arXiv:2610.32335v1) introduce the setting for non-expansive fuzzy modal logic and establish uniform interpolation; their accessible abstract and the cited propositions in related published work concern interpolation, not the product-t-norm minimax problem. The earlier non-expansive fuzzy description logic paper (2025, arXiv:2505.09416) sets up the language and complexity comparison. A published published-finding corpus result titled *Exact three-language approximation gap for strong fuzzy disjunction* gives the sharp uniform errors \(1-1/n\) and \((1-1/n)/2\) for the **Łukasiewicz strong disjunction**, together with rational attainment. Its full mathematical statement and proof were inspected. A Boolean duality transforms that result into the analogous strong Łukasiewicz conjunction result, but **not** into a result about the multiplicative product t-norm: the complement dual of product is the *probabilistic sum* \(1-\prod_i(1-x_i)\), not Łukasiewicz truncated addition. The product target has a different optimal constant \(h_n\), a different extremal diagonal point, and rational nonattainment for every \(n\ge3\). This distinction, not a change of connective name, is the novelty claim.

A separate published half-grid theorem gives exact elimination witnesses for rational non-expansive *terms*. Its proof and statements were inspected; they do not imply a best uniform approximation to an outside continuous multiplicative truth function, nor the nonattainment threshold. General optimal Lipschitz approximation methods could potentially imply the metric part of this theorem after specializing to product conjunction. That potential abstract reduction is acknowledged rather than denied.

## Limitations
The result is an exact error and attainment classification for the specified three languages and the particular natural product t-norm target; it is not a universal algorithm for arbitrary fuzzy truth functions. No pointwise assertion about an inaccessible source's full text is made from its abstract alone. The 2026 motivating preprint's full text was not available for inspection in this run, although its abstract, publication record and detailed research context were checked; this remains a priority-comparison limitation. General classical results on best Lipschitz approximation may subsume the purely metric lower bound, but the rational-language nonattainment and modal-language comparison require the stated syntactic analysis. No independent audit has been performed.

## References
1. Stefan Gebhart, Lutz Schröder and Paul Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation*, arXiv:2610.32335v1, first posted 2026-10-23. https://arxiv.org/abs/2610.32335
2. Stefan Gebhart, Lutz Schröder and Paul Wild, *Non-expansive Fuzzy ALC*, arXiv:2505.09416, first posted 2025-05-14. https://arxiv.org/abs/2505.09416
3. *Exact three-language approximation gap for strong fuzzy disjunction*, published-finding corpus, published 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-three-language-approximation-gap-for-strong-fuzzy-disjunct--9cd5fba0d403/RESULT.md
4. *Sharp half-grid witnesses for rational non-expansive fuzzy propositional elimination*, published-finding corpus, published 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-half-grid-witnesses-for-rational-non-expansive-fuzzy-propo--1641f2a5f07b/RESULT.md
5. Mirko Navara, *Triangular Norms and Conorms*, Scholarpedia 2(3):2398 (2007). https://www.scholarpedia.org/article/Conorm
