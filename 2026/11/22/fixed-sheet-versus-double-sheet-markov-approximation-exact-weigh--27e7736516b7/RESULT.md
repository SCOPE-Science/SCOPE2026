# Fixed-sheet versus double-sheet Markov approximation: exact weighted and equal-weight laws

## Finding
Let \(X\) be a finite connected topological graph with a connected two-sheeted covering \(q_2:Y_2\to X\). Adjoin one disjoint identity sheet \(Y_0=X\), and let \(q:Y_0\sqcup Y_2\to X\) be the resulting three-sheeted covering. On real spaces of continuous functions with supremum norm, define the fiber-average Markov operator
\[
(Af)(x)=\frac13 f(x\in Y_0)+\frac13\sum_{y\in q_2^{-1}(x)}f(y).
\]
Here \(f(x\in Y_0)\) denotes the value at the point of the identity component over \(x\). Let \(\mathcal E_m\) consist of sums \(\sum_{j=1}^m\alpha_j C_{h_j}\), where \(\alpha_j\ge0\), \(\sum\alpha_j=1\), \(h_j:X\to Y_0\sqcup Y_2\) is continuous and \(C_{h_j}f=f\circ h_j\). Let \(\mathcal E_m^{\mathrm{eq}}\) consist of their equally weighted counterparts \(m^{-1}\sum_{j=1}^m C_{h_j}\); repetitions are permitted.

**Theorem.** Both distances are attained. For every integer \(m\ge2\),
\[
\operatorname{dist}(A,\mathcal E_m)=\frac{4}{3(m-1)},
\qquad
\operatorname{dist}(A,\mathcal E_m^{\mathrm{eq}})=
\begin{cases}
\frac{8}{3m},&m\equiv2\pmod3,\\[2pt]
\frac2m,&m\equiv0,1\pmod3.
\end{cases}
\]
For \(m=1\), both distances equal \(4/3\). The equal-weight distance therefore coincides at every budget with the known formula for any *connected* three-sheeted covering, even though this covering has a global section. But the unrestricted distance falls to the smaller scale \(4/(3m)\), rather than the connected-covering scale \(2/m\). More precisely, for \(m\ge2\), the equal-weight/unrestricted ratio is
\[
\begin{cases}
\frac{2(m-1)}m,&m\equiv2\pmod3,\\[2pt]
\frac{3(m-1)}{2m},&m\equiv0,1\pmod3,
\end{cases}
\]
with sharp residue-class limiting factors \(2\) and \(3/2\). No finite sum of extreme Markov operators equals \(A\).

## Assumptions and scope
A finite topological graph is a finite one-dimensional CW complex; connected covering means a genuine two-sheeted topological covering whose total space \(Y_2\) is connected. In particular, \(Y_2\to X\) has no section. The disjoint union \(Y=Y_0\sqcup Y_2\) is compact. The point-mass kernel for \(A\) gives equal mass \(1/3\) to the three points of every fiber. All operators act from \(C(Y;\mathbb R)\) to \(C(X;\mathbb R)\). Approximation uses the operator norm and *globally constant* mixing coefficients. No approximating map is required to respect the covering. The statement concerns only this canonical minimal reducible monodromy profile (one fixed sheet and one transposed pair), not general disconnected coverings or component-dependent target masses.

## Proof
**1. Exact norm as missing mass.** Let \(\mu_x\) put mass \(1/3\) on the three points of \(q^{-1}(x)\). For an approximant \(R=\sum_j\alpha_jC_{h_j}\), write \(\nu_x=\sum_j\alpha_j\delta_{h_j(x)}\). Riesz representation and total variation give
\[
\|A-R\|=\sup_{x\in X}\|\mu_x-\nu_x\|_{\mathrm{TV}}
=2\sup_{x\in X}\sum_{i=0}^2\left(\frac13-\nu_x(\{y_i(x)\})\right)_+,
\]
where \(y_0(x)\in Y_0\) is the identity sheet, \(y_1(x),y_2(x)\in Y_2\) are the other fiber points, and \(v_+=\max\{v,0\}\). The last formula remains valid with mass outside the fiber. Every continuous map \(X\to Y\) takes values in one of the two connected components.

**2. Unrestricted lower bound.** Suppose \(1\le r\le m-1\) of the \(m\) maps take values in \(Y_0\), with total coefficient \(w\), and the other \(n=m-r\) maps take values in \(Y_2\), with total coefficient \(u=1-w>0\). Write \(\mu_{0,x}=\delta_{y_0(x)}\), \(\mu_{2,x}=(\delta_{y_1(x)}+\delta_{y_2(x)})/2\), and let \(\nu_{2,x}\) be the normalized convex combination of the \(n\) maps in \(Y_2\). The two components are disjoint, hence
\[
\|\mu_x-\nu_x\|_{\mathrm{TV}}
\ge\left|\frac13-w\right|+
\left\|\frac23\mu_{2,x}-u\nu_{2,x}\right\|_{\mathrm{TV}}
\ge\frac23\|\mu_{2,x}-\nu_{2,x}\|_{\mathrm{TV}}.
\]
The second inequality is precisely the triangle inequality and \(|u-2/3|=|w-1/3|\). The sharp connected-degree-two theorem of Duru--İlter--Bilgin [1, Theorem 1.1] gives minimum norm error \(2/n\) for \(n\) arbitrary-weight maps, so \(\|A-R\|\ge4/(3n)\ge4/[3(m-1)]\). If \(u=0\) or all maps lie in \(Y_0\), missing the other two target atoms forces error at least \(4/3\). If all maps lie in \(Y_2\) and \(m\ge3\), the identity sheet is missed, forcing error at least \(2/3\), no smaller than the asserted bound. For \(m=2\) with all maps in \(Y_2\), choose a positive-weight map that fails to lie over some \(x\): the other map can hit at most one fiber atom, leaving both the identity sheet and a second target atom empty, so the error is at least \(4/3\). The argument also covers zero coefficients by deleting zero terms or using the same missing-mass inequalities.

**3. Unrestricted attainment and the one-map endpoint.** Choose one identity-section map with coefficient \(1/3\). Give the remaining \(m-1\) maps in \(Y_2\) the optimal connected-degree-two coefficients rescaled to total \(2/3\). Theorem 1.1 of [1] produces an actual minimum \(2/(m-1)\) on the two-sheet component; multiplying by \(2/3\) gives exact error \(4/[3(m-1)]\). For \(m=1\), the identity section has error \(4/3\). Every map into \(Y_2\) must miss the fiber somewhere, yielding error \(2\); a map into \(Y_0\) misses the two other target atoms and has error at least \(4/3\). This establishes the first assertion for all \(m\).

**4. Equal-weight universal lower bound.** For \(m\ge2\), if all maps lie in \(Y_0\), the error is at least \(4/3\), which exceeds or equals the desired bound. Otherwise choose a map into the connected double cover. It cannot be a section, so at some \(x\) its target is outside the three-point fiber. At that point at most \(m-1\) equal atoms occupy the three fiber points. If their integer occupancy counts are \(c_0,c_1,c_2\), then
\[
\frac12\|\mu_x-\nu_x\|_{\mathrm{TV}}
=\sum_{i=0}^2\left(\frac13-\frac{c_i}m\right)_+,
\qquad c_0+c_1+c_2\le m-1.
\]
Convexity of the positive-part function allows counts to be balanced without increasing this sum. If \(m=3k+1\), the best three counts are \((k,k,k)\), with deficit \(1/m\). If \(m=3k+2\), they are \((k+1,k,k)\), with deficit \(4/(3m)\). If \(m=3k\), they are \((k,k,k-1)\), with deficit \(1/m\). This proves the required operator-norm lower bounds \(2/m\) and \(8/(3m)\).

**5. Equal-weight attainment for every covering.** Work with atoms each of global weight \(1/m\). In all cases the identity-sheet atoms follow its section continuously. For \(m=3k\) (\(k\ge1\)), put \(k\) atoms on the identity sheet and arrange the remaining \(2k\) as \((k,k)\) over the two double-cover positions. In any single-atom exchange their stationary double-cover counts are \((k-1,k)\), so the missing target mass is exactly \(1/m\). For \(m=3k+1\) (\(k\ge1\)), put \(k\) atoms on the identity sheet and arrange \(2k+1\) double-cover atoms as \((k+1,k)\). Every full-to-low move leaves stationary counts \((k,k)\), so all three fiber positions are short by \(1/(3m)\), giving total deficit \(1/m\). For \(m=3k+2\) (\(k\ge0\)), use \(k+1\) identity-sheet atoms and \(2k+1\) double-cover atoms arranged as \((k+1,k)\); during a move the double-cover stationary counts are \((k,k)\), yielding deficit \(4/(3m)\). The defect when all atoms are at fiber points is no larger than during these moves.

For each double-cover allocation, all sheet-label permutations are reachable by elementary single-atom exchanges with the stated balanced stationary occupancies. For even numbers of atoms, exchange an atom in each direction in succession; for odd numbers, use the temporarily lower-occupied site as a buffer to exchange labels. This is the degree-two specialization of [1, Lemma 5.2]. Because \(Y_2\) is a connected finite graph, the edgewise path-gluing construction in [1, Lemma 4.2] realizes every required sheet permutation by continuous maps \(h_j:X\to Y_2\) while at most one atom travels off the fiber at any instant. The moving atom cannot increase missing fiber mass, so the above stationary deficits bound the norm uniformly. The resulting equal-weight averages attain both lower bounds. The \(m=1\) case follows from Step 3. \(\square\)

## Verification
The standalone `verify.py` uses exact rational arithmetic to test the minimum of the three-site off-fiber integer deficit over all assignments of zero through \(m\) maps to the identity component for each \(1\le m\le500\). It separately checks the prescribed equal-weight constructions, the arithmetic specialization of [1, Theorem 1.1] to two sheets, and reachable sheet-flip paths via explicit labelled-atom state searches for \(2\le m\le18\). Observed output: `THREE_SHEET_RATIONAL_CHECK_OK 2513`. These finite tests do **not** prove the topological path-gluing statement or the theorem for all \(m\); those facts are established in the proof using [1, Lemmas 4.2 and 5.2].

## Relationship to prior work
Duru--İlter--Bilgin [1] prove the sharp arbitrary- and equal-weight formulas for a **connected** degree-\(d\) covering. Their connected-degree-three formula yields the same equal-weight numbers displayed above, but does not imply the unrestricted split-cover law: the present three-sheeted cover has a global section and a different unrestricted rate. The earlier two-map disconnected-covering result [2] already covers \(m=2\). The three-map weighted split-cover result [5] covers \(m=3\): its degree-two component with total mass \(2/3\) gives error \(2/3\), attained with the identity coefficient and both double-cover coefficients equal to \(1/3\), so it also covers the equal-weight specialization. The extension beyond these budget-specific results starts at **\(m\ge4\)** and includes the exact asymptotic contrast between coefficient constraints. Brown [3] treats qualitative approximation on measure spaces, not this fixed-budget \(C\)-space norm problem. Kim [4, Theorems 3 and 4] gives sequential approximation for \(\mu\)-continuous Markov operators and \(L^2\)-norm approximation for Hilbert–Schmidt operators, respectively, not these fixed-term graph-cover distances.

## Limitations
The exact formulas require one identity component and one connected two-sheet component, uniform target fiber masses, a connected finite-graph base, globally constant convex coefficients and real continuous-function spaces. They do not classify arbitrary disconnected covers or nonuniform target masses. The constructive steps use the published single-atom transport lemmas [1] and do not claim novelty for those underlying lemmas. Priority relative to inaccessible older Markov-approximation literature remains conditional; absence from searches is not a proof of global novelty. No independent audit has been performed.

## References
[1] H. Duru, S. İlter, A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1, first posted 2026-10-26. https://arxiv.org/abs/2610.35575 ; https://arxiv.org/html/2610.35575v1.

[2] *Exact two-map approximation of componentwise-weighted disconnected covering averages*, 2026-11-08. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-two-map-approximation-of-componentwise-weighted-disconnect--25459b8578e0.

[3] J. R. Brown, *Approximation theorems for Markov operators*, Pacific J. Math. **16** (1966), 13--23. https://msp.org/pjm/1966/16-1/pjm-v16-n1-p03-s.pdf.

[4] C.-W. Kim, *Approximation theorems for Markov operators*, Z. Wahrscheinlichkeitstheorie verw. Gebiete **21** (1972), 207--214. https://doi.org/10.1007/BF00538394.

[5] *Three-map phase transition for weighted disconnected graph covers*, 2026-11-17. https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-three-map-phase-transition-for-weighted-disconnected-graph-cover--db5f5672882f.
