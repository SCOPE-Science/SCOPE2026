# GCD-delayed triple-trace dependence and primitive temporal recurrences for Rule 90

## Finding
Let \(K\) be any finite field of size \(q\), let \(X=K^{\mathbb Z}\) with its uniform product (Haar) measure, and let \(F:X\to X\) be the synchronous additive cellular automaton
\[
(Fx)_j=x_{j-1}+x_{j+1}.
\]
Fix integers \(0<h<k\) and a number \(t\ge1\) of consecutive observations. Read the three stationary sensors at \(0,h,k\) at times \(0,1,\ldots,t-1\). Write \(g=\gcd(h,k)\), and define the polynomial sequence in \(K[u]\) by
\[
B_0(u)=0,\quad B_1(u)=1,\quad B_{n+1}(u)=uB_n(u)-B_{n-1}(u),\qquad n\ge1.
\]
Then \(B_g\) divides each of \(B_h,B_k,B_{k-h}\). The three full time streams \(v_j(s)=(F^s x)_j\), \(j\in\{0,h,k\}\), satisfy the **primitive temporal relation**
\[
\boxed{\frac{B_k(\mathsf S)}{B_g(\mathsf S)}v_h-
\frac{B_h(\mathsf S)}{B_g(\mathsf S)}v_k-
\frac{B_{k-h}(\mathsf S)}{B_g(\mathsf S)}v_0=0,}
\tag{1}
\]
where \((\mathsf S v)(s)=v(s+1)\), and every polynomial quotient in (1) belongs to \(K[u]\). Every polynomial-coefficient linear relation among the three complete streams is a polynomial multiple of (1).

For finite observations, the **only** restrictions on the resulting \(3t\) values are the \(\max\{0,t-k+g\}\) shifts of (1) for starting times \(0\le s<t-k+g\). These restrictions are independent. Consequently, the exact dimension of the attainable pattern space, and hence the logarithm of its size, are
\[
\boxed{\rho_{h,k}(t)=3t-\max\{0,t-k+\gcd(h,k)\},\qquad
|\mathcal T_{h,k}(t)|=q^{\rho_{h,k}(t)}.}
\tag{2}
\]
Under uniform independent initial symbols, the output is uniform on this linear space; its Shannon entropy is \(\rho_{h,k}(t)\log q\). In particular, the three streams are jointly independent through exactly \(k-g\) observations, with their **first nontrivial dependence at observation horizon** \(t=k-g+1\). Every pair of distinct stationary sensors, in contrast, has completely independent uniform temporal streams at every finite horizon.

For example, observations at positions \((0,6,12)\) first become dependent at \(t=7\), whereas observations at \((0,5,12)\) remain fully independent until \(t=11\) and become dependent at \(t=12\), despite having identical endpoints and the same number of sensors. The formula is valid in every field characteristic, not just binary Rule 90.

## Assumptions and scope
The spatial lattice is bilateral and infinite; it is not a finite ring. Each initial coordinate is independently uniform in the finite field \(K\). Observations use exactly the three fixed, distinct sites \(0<h<k\), and include times \(0\) through \(t-1\), without missing frames. Algebraic assertions about possible observations hold for **all** initial configurations, without probability assumptions; uniformity requires the stated Haar input law. The operator \(\mathsf S\) in (1) shifts the temporal index forward and is not a spatial shift. A polynomial temporal relation is interpreted as a formal identity applying at every nonnegative integer starting time. No claim is made about finite rings or noisy sensors.

## Proof
**Step 1: Observation functionals and field extension.** Set \(z\) to be the formal bilateral spatial shift and put \(u=z+z^{-1}\). The reading at site \(j\) at time \(s\) is the linear functional corresponding to the Laurent polynomial \(z^j u^s\) in \(K[z,z^{-1}]\). Finite families of such readings have the same rank as their Laurent-polynomial coefficient vectors: the finite set of input coordinates they use can be assigned arbitrarily.

The field extension \(K(z)/K(u)\) has degree two. Indeed, \(z\) is a root of \(Z^2-uZ+1\), while the nonidentity involution \(z\mapsto z^{-1}\) of \(K(z)\) fixes \(u\). Therefore the quadratic is irreducible over \(K(u)\) and \(1,z\) form a basis. Further, \(z^d\notin K(u)\) for any \(d\ge1\), since applying the involution would give \(z^d=z^{-d}\), impossible in the rational function field. This proves temporal independence for every two distinct sites.

**Step 2: Strong divisibility.** The polynomials \(B_n\) are monic of degree \(n-1\) for \(n\ge1\), including in characteristic two. Their recurrence gives
\[
B_{m+n}=B_{m+1}B_n-B_mB_{n-1},\qquad
B_{m+1}B_{m-1}-B_m^2=-1.
\]
The second identity implies \(\gcd(B_m,B_{m+1})=1\). The first implies \(\gcd(B_m,B_{m+n})=\gcd(B_m,B_n)\), with monic normalization, and the Euclidean algorithm on indices yields
\[
\boxed{\gcd_{K[u]}(B_m,B_n)=B_{\gcd(m,n)}}\qquad(m,n\ge1).
\tag{3}
\]
In particular, \(B_g\) divides \(B_h\), \(B_k\), and \(B_{k-h}\).

**Step 3: The unique primitive syzygy.** From \(z^2=uz-1\), induction gives
\[
z^n=B_n(u)z-B_{n-1}(u)\qquad(n\ge1).
\]
The recurrence determinant identity implies
\[
B_k(u)z^h-B_h(u)z^k-B_{k-h}(u)=0.
\tag{4}
\]
Suppose \(P_0,P_h,P_k\in K[u]\) satisfy \(P_0+P_h z^h+P_k z^k=0\). Expansion in the \(K(u)\)-basis \(1,z\) shows \(P_hB_h+P_kB_k=0\). By (3), writing \(G=B_g\), all polynomial solutions have \(P_h=R B_k/G\), \(P_k=-R B_h/G\) for one \(R\in K[u]\). The constant coefficient then forces \(P_0=-R B_{k-h}/G\), using (4). This proves that (4), divided by \(G\), generates the **entire polynomial relation module**. Since multiplication by \(u\) corresponds to advancing one time step, this is exactly (1).

**Step 4: Finite-horizon ranks and complete constraints.** A linear dependence among the \(3t\) observation functionals corresponds to \(P_0,P_h,P_k\) with each degree strictly less than \(t\). In the primitive syzygy the polynomial degrees are respectively \(k-h-g\), \(k-g\), and \(h-g\); the maximum is exactly \(k-g\) and occurs at the middle sensor. Hence its polynomial multiples obey all three degree bounds precisely when \(\deg R<t-(k-g)\). The vector space of such multiples has dimension \(\max\{0,t-k+g\}\). Taking the complement in the \(3t\)-dimensional space of all formal observations proves (2), and the evident temporal shifts of (1) form a basis of every finite relation space.

**Step 5: Measure and threshold.** Only finitely many input coordinates affect a fixed finite set of readings, so under independent uniform input coordinates every attainable vector in the linear image has the same number of preimages. This gives the uniform law and the entropy formula. The degree bound gives strict independence when \(t\le k-g\) and one first relation at \(t=k-g+1\). The two-site assertion follows separately from Step 1. All steps hold over an arbitrary finite field.

## Verification
Run `python3 verify_three_probe.py` using Python 3, with no external packages. The checker independently constructs Laurent-polynomial observation rows and computes exact finite-field Gaussian ranks; it passed 13,464 field/range/horizon instances across the prime fields with 2, 3, 5 and 7 elements. Separately, it verified 2,244 Laurent-polynomial relation identities and 6,724 polynomial strong-divisibility instances. It also enumerated all input assignments and compared exact output distributions in four small cases. These are finite consistency tests; the proof above establishes the infinite and all-parameter quantifiers.

For reproducibility, the checker prints a line beginning `VERIFY_OK` followed by these counts. No simulation output, statistical fitting, or large-time extrapolation is used in the proof.

## Relationship to prior work
Castronuovo, Dennunzio, Kari and Margara (arXiv:2611.16746v1, first public 12 November 2026) compute asymptotic topological entropy of group cellular automata using fixed-width space-time traces and Laurent-polynomial algebra. Their theorems do not give the exact three-separated-site, finite-horizon observation language or its primitive generator. The 2023/2024 work of Akın, Dikranjan, Giordano Bruno and Toller handles polynomial trajectories and contiguous observation windows, not this nonconvex three-column rank law.

Salo's *Cutting Corners* and Salo–Schabanel's *Solitaire of independence* establish extensions and bases for convex regions of totally extremally permutive space-time subshifts, with broader independence-set operations. The three separated temporal columns here are nonconvex for nonadjacent sensors; those theorems do not state the closed gcd-dependent law or the unique temporal filter in (1). Cervelle, Formenti and Guillon analyze single-site ultimate traces and undecidability, a different question.

There are two important quantitative relatives. The published finite-ring Rule-90 observability result *Exact rank deficits and optimal static sensors for cyclic Rule 90* characterizes eventual recovery of ring states and gcd-dependent invisible dimensions, but has cyclic rather than bilateral geometry and does not supply (1)–(2). The published symbolic-return result *The Fine–Wilf threshold for hidden triple dependence in symbolic self-returns* has an exactly matching gcd-shaped **count** for intersections of full-shift recurrence events. Its objects are symbolic equality events rather than linear cellular-automaton observation streams; the present result additionally determines all characteristic-dependent linear constraints via the generator (1). The shared arithmetic form is acknowledged, not asserted to be independently unprecedented. Historical equivalence via other unindexed formulations remains a priority risk.

## Limitations
The theorem concerns a single elementary additive rule, exactly three stationary sites, full consecutive temporal observations, and uniform product input. It does not classify more than three sites, missing time samples, sensor noise, finite cyclic spatial lattices, or nonlinear rules. The polynomial modules may be computed in other settings but no general result for them is claimed. Structural links to classical Fine–Wilf and TEP independence theory warrant independent historical-priority review; no independent scientific audit is represented by this document.

## References
1. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1 (submitted 2026-11-12), https://arxiv.org/abs/2611.16746.
2. H. Akın, D. Dikranjan, A. Giordano Bruno and D. Toller, *The algebraic entropy of one-dimensional finitary linear cellular automata*, arXiv:2306.10838 (first public 2023-06-19), https://arxiv.org/abs/2306.10838.
3. V. Salo, *Cutting Corners*, arXiv:2002.08730, https://arxiv.org/abs/2002.08730.
4. V. Salo and J. Schabanel, *Solitaire of independence*, Natural Computing 24 (2025), 431–467, https://doi.org/10.1007/s11047-025-10010-3.
5. J. Cervelle, E. Formenti and P. Guillon, *Ultimate Traces of Cellular Automata*, arXiv:1001.0251, https://arxiv.org/abs/1001.0251.
6. *Exact rank deficits and optimal static sensors for cyclic Rule 90*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-rank-deficits-and-optimal-static-sensors-for-cyclic-rule-9--162c468ed707.
7. *The Fine–Wilf threshold for hidden triple dependence in symbolic self-returns*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-fine-wilf-threshold-for-hidden-triple-dependence-in-symbolic--99486a928fd1.
