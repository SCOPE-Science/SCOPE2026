# Exact power-domination and fragile-sensor census of circular ladders

## Finding

For every integer \(n\ge4\), let \(G_n=C_n\square K_2\) be the labelled circular ladder, whose vertices are \((r,i)\) for \(r\in\{0,1\}\) and \(i\in\mathbb Z/n\mathbb Z\). Starting with a sensor set \(S\), power domination first observes the closed neighborhoods of all sensors, then repeatedly observes the unique unobserved neighbor of any observed vertex having exactly one unobserved neighbor. Call a set *failed* if it does not eventually observe all \(2n\) vertices. Let \(F_n(z)=\sum_{S\text{ failed}}z^{|S|}\), counting the empty failed set.

The complete, labelled failure polynomial is \(F_n(z)=\sum_{k=0}^{\lfloor n/3\rfloor}a_{n,k}z^k\), where \(a_{n,0}=1\) and, for every integer \(1\le k\le\lfloor n/3\rfloor\),
\[
a_{n,k}=\frac{2n}{k}\sum_{j=0}^{\lfloor k/2\rfloor}\binom{k}{2j}\binom{n-3k+2j-1}{k-1}.
\]
Binomial coefficients with negative upper entries or upper entry below the lower entry are zero. For \(n=3\), the triangular prism has no nonempty failed set, so \(F_3(z)=1\). For \(n\ge4\), the full power-domination polynomial is therefore
\[
\mathcal P(G_n;z)=(1+z)^{2n}-F_n(z).
\]
The bivariate failure generating function is the following identity of formal power series:
\[
\sum_{n\ge4}(F_n(z)-1)x^n
=\frac{x(1+3zx^2+4zx^3)}{1-x-zx^3-zx^4}
-\frac{3zx^3}{1+zx^3}-\frac{x}{1-x}.
\]
At \(z=1\), let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\) denote the Lucas sequence. Then the *exact number of failed sensor subsets* is
\[
F_n(1)=L_n+2\mathbf1_{2\mid n}(-1)^{n/2}
+3\mathbf1_{3\mid n}(-1)^{n/3},\qquad n\ge4.
\]
Consequently \(F_n(1)\sim\varphi^n\), where \(\varphi=(1+\sqrt5)/2\). This counts configurations, not merely the maximum number of failed sensors.

For independently surviving sensors at all \(2n\) locations with survival probability \(p\in[0,1]\), the probability of complete observation and expected number of observed vertices are exactly
\[
R_n(p)=1-\sum_{k=0}^{\lfloor n/3\rfloor}a_{n,k}p^k(1-p)^{2n-k},
\]
\[
\mathbb E O_n=2n-\sum_{k=0}^{\lfloor n/3\rfloor}(2n-4k)a_{n,k}p^k(1-p)^{2n-k}.
\]
For a fixed failure probability \(q\in(0,1)\), set \(p=1-q\), \(y=p/q\), and let \(\rho(y)\) be the unique positive root of \(1-\rho-y\rho^3-y\rho^4=0\). Then
\[
1-R_n(1-q)\sim\left(\frac{q^2}{\rho(y)}\right)^n.
\]
The leading asymptotic constant here is exactly one.

There is also a sharp sparse-sensor threshold. If \(p_n=c/\sqrt n\) with fixed \(c\ge0\), then
\[
\lim_{n\to\infty}R_n(p_n)=1-e^{-11c^2},\qquad
\lim_{n\to\infty}\frac{\mathbb E O_n}{2n}=1-e^{-11c^2}.
\]
More generally, if \(p_n\sqrt n\to0\) the success probability tends to zero; if \(p_n\sqrt n\to\infty\) it tends to one. Thus the threshold scale is \(n^{-1/2}\), with an explicit Poisson critical window.

## Assumptions and scope

Graphs are simple, labelled, undirected prisms. All cardinalities count distinct labelled vertex subsets; cycles are not factored by rotations or reflections. The forcing process begins with closed-neighborhood domination, not open-neighborhood observation. The probability model installs an independent potential sensor at every vertex, retaining each with probability \(p\); a failed sensor contributes neither observation nor forcing. The exact formulas hold for all \(n\ge4\), including \(n=4\). The only separate case is \(n=3\). The statements for fixed \(q\) require \(0<q<1\), and the Poisson window uses a fixed nonnegative real \(c\). No claim of a universal result for nonprism graphs is made.

## Proof

**1. Exact stopping condition.** Distances in the prism are
\[
d((r,i),(s,j))=\min\{(i-j)\bmod n,(j-i)\bmod n\}+\mathbf1_{r\ne s}.
\]
For \(n\ge4\), two sensors at distance at most three suffice to power dominate. Indeed, up to rail interchange, cyclic shift, and reflection, the six possibilities are: same-rail column offsets \(1,2,3\) or opposite-rail offsets \(0,1,2\). Following initial closed-neighborhood observation, each case either already observes two consecutive complete rungs or obtains such rungs by at most two unique-neighbor forces (for same-rail offsets \(2\) and \(3\), use the intermediate observed rail vertices to force their rung partners). Two consecutive fully observed rungs force the next rung, one vertex on each rail, and this propagates around the prism. The distance-three pair property is also present as Lemma 2 of Girish and Somasundaram (2024), and is used here as a known ingredient, not a claimed novelty. A general no-full-row obstruction for failed power domination in cylinders is previously developed by Byrne et al. (2022/2023); this is also a prior-known structural theme.

Conversely, suppose all chosen sensors have pairwise distance at least four. Their closed neighborhoods are pairwise disjoint and have no edges between them: an intersection would give sensor distance at most two, and an edge between neighborhoods distance at most three. Because prisms with \(n\ge4\) are cubic and triangle-free, each nonsensor vertex in one such closed neighborhood has exactly two unobserved neighbors. Each sensor has zero. Thus the forcing process stops immediately and observes exactly \(4|S|\) vertices. In particular, every failed sensor set has this form, including the empty set, and
\[
S\text{ fails}\iff d(v,w)\ge4\ \text{for all distinct}\ v,w\in S.
\]
Equivalently the failed sets are the independent sets of the third graph power \(G_n^3\). The prior pair lemma alone supplies neither the complete enumerator nor the random-sensor threshold; the reverse implication above is independently proved.

**2. Enumerating all sizes.** A nonempty failed set has at most one sensor in any column. List its \(k\) occupied columns in cyclic order. Give each a rail color, either zero or one. The forward cyclic gap between consecutive selected columns is at least four when their colors agree and at least three when they disagree. These constraints also exclude every nonconsecutive forbidden pair, since any intervening two gaps have total length at least six. A cyclic two-color sequence has an even number of color changes, say \(2j\). There are exactly \(2\binom{k}{2j}\) such cyclic color words on an indexed circular list. The \(k\) minimum gaps sum to \(4k-2j\); distributing the remaining \(n-4k+2j\) units among the \(k\) gaps yields \(\binom{n-3k+2j-1}{k-1}\) possibilities. Choose the first occupied labelled column in \(n\) ways, and divide by \(k\) for the \(k\) possible starting sensors. This gives the coefficient formula. The \(k=1\) convention is the single gap of length \(n\), yielding \(a_{n,1}=2n\), and the minimum possible gap implies \(k\le\lfloor n/3\rfloor\).

For the rational expression, use the two-color cyclic gap matrix
\[
T(x)=\frac1{1-x}\begin{pmatrix}x^4&x^3\\x^3&x^4\end{pmatrix}.
\]
The cyclic trace construction gives \(-x\partial_x\log\det(I-zT(x))\); explicitly
\[
\det(I-zT(x))=\frac{(1-x-zx^3-zx^4)(1+zx^3)}{1-x}.
\]
Differentiation gives the displayed bivariate rational function, and its coefficients in orders below four vanish. At \(z=1\), the factorization
\[
1-x-x^3-x^4=(1+x^2)(1-x-x^2)
\]
expresses the logarithmic derivative as the Lucas generating series plus two finite-period correction series. Adding the empty failed set proves the stated Lucas formula. Since \(L_n=\varphi^n+(-\varphi)^{-n}\), the stated total-count asymptotic follows.

**3. Reliability and observation.** Independent retention assigns probability \(p^{|S|}(1-p)^{2n-|S|}\) to each sensor subset. On failure with \(k\) retained sensors, exactly \(4k\) vertices are observed by step 1; otherwise all \(2n\) are observed. Summing over the failure polynomial proves both exact probability and expectation formulas.

For fixed \(0<q<1\), the failure probability is \(q^{2n}F_n(y)\) for \(y=(1-q)/q>0\). The characteristic equation \(1-x-yx^3-yx^4=0\) has exactly one positive zero \(\rho(y)\in(0,1)\); its nonnegative, aperiodic coefficient support makes this zero strictly smallest in modulus. The factor \(1+yx^3\) has zeros farther away, since \(y\rho^3(1+\rho)=1-\rho<1\). The logarithmic derivative has a simple pole whose \(x^n\)-coefficient is exactly \(\rho^{-n}\) to leading order. Therefore \(q^{2n}F_n(y)\sim(q^2/\rho)^n\), as claimed; the base is strictly less than one.

**4. Critical sparse-sensor threshold.** For \(n\ge7\), the graph \(G_n^3\) is \(11\)-regular on \(2n\) vertices: each vertex has six same-rail neighbors at cyclic distances one, two, and three, and five opposite-rail neighbors at cyclic distances zero, one, and two. Hence it has exactly \(11n\) edges. Let \(X_n\) count edges of \(G_n^3\) whose two endpoints both retain sensors. By step 1, full observation occurs precisely when \(X_n\ge1\).

For \(p_n=c/\sqrt n\), every fixed factorial moment of \(X_n\) tends to the corresponding moment of a Poisson variable of mean \(11c^2\): disjoint ordered edge tuples give \((11n)^r p_n^{2r}\to(11c^2)^r\), while an overlapping tuple with \(t\) connected components and \(v\ge2t+1\) distinct vertices has only \(O(n^t)\) embeddings in this bounded-degree graph and total contribution \(O(n^{t-v/2})=O(n^{-1/2})\). The factorial-moment criterion proves \(X_n\Rightarrow\mathrm{Poisson}(11c^2)\), whence the success limit follows. For observed fraction, the failed-state contribution is at most \(4\mathbb E|S|/(2n)=4p_n\to0\).

If \(np_n^2\to0\), the union bound \(\Pr(X_n\ge1)\le11np_n^2\) proves failure with high probability. If \(np_n^2\to\infty\), choose \(\lfloor n/2\rfloor\) vertex-disjoint horizontal edges on one rail; the probability none has both endpoints selected is at most \((1-p_n^2)^{\lfloor n/2\rfloor}\to0\). This proves both sides of the sharp threshold.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It builds actual prism adjacency lists and implements domination followed by unique-neighbor forcing, independently checking every one of the \(349440\) sensor subsets across \(4\le n\le9\). It verifies failed-set sizes and full observation against graph distances and the closed binomial formula, detecting \(190\) failed subsets in total. An independent formal-series computation tests all polynomial coefficients for \(4\le n\le160\); exact Lucas totals are compared through \(n=160\). The degree-eleven condition is checked for \(7\le n\le30\), and the triangular-prism boundary is tested. The check returns `VERIFY_OK`. The finite checks are not a proof of the infinite-size and asymptotic assertions; those follow from the arguments above.

## Relationship to prior work

Bjorkman, Brennan, Flagg, and Koch (2023) introduced the random-sensor-failure framework and studied full-observation probabilities and expected coverage for other graph families. Their framework motivates the all-location reliability question here; the present prism formulas and sharp threshold are not stated in the inspected text. Brimkov, Patel, Suriyanarayana, and Teich (2018) developed the power-domination polynomial and counted other graph families, but do not provide the present prism polynomial in their inspected accessible version. Byrne et al. (2022/2023) developed the failed power-domination number for grids, tori, and square cylinders, not the complete two-rail prism sensor-set distribution; its no-full-consecutive-row lemma is acknowledged as background. Girish and Somasundaram (2024) already proved the crucial two-sensor distance-at-most-three characterization for prisms and a scalar extremum for failed placements. These previously known claims are explicitly excluded from novelty. The new theorem is the full labelled size distribution, rational generating function, exact Lucas correction, random-sensor reliability, and Poisson sparse window. Publication priority is provisional: a fully indexed or inaccessible equivalent enumerator cannot be ruled out by search alone.

## Limitations

The theorem applies to complete circular ladders with all locations eligible for independent retention; it does not optimize a fixed sensor-placement budget. The probability model assumes independent, identical sensor survival. The nearest 2024 primary article was accessible only in substantial indexed full-text excerpts because its official full-text endpoint returned a rate-limit error; the inability to inspect every page is a residual priority risk, not scientific evidence of noncoverage. The proof and program have undergone self-review only; no independent mathematical audit or priority certification has been performed.

## References

1. Beth Bjorkman, Zachary Brennan, Mary Flagg, and Johnathan Koch, *Power domination with random sensor failure*, arXiv:2312.12259v1 (2023-12-19), https://arxiv.org/abs/2312.12259.
2. Lakshmi Girish and Kanagasabapathi Somasundaram, *Bound for the k-Fault-Tolerant Power-Domination Number*, *Symmetry* **16** (2024), 781, https://doi.org/10.3390/sym16070781.
3. Boris Brimkov, Rutvik Patel, Varun Suriyanarayana, and Alexander Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (2018-05-28), https://arxiv.org/abs/1805.10984.
4. Isabel T. Byrne, Gretchen L. Matthews, Nikita M. Patel, Anuradha G. Trivedi, and Margaret A. Winslow, *Failed power domination in grids, cylinders, and tori*, preprint dated 2022-10-19; *Involve* **16** (2023), 705–717, https://doi.org/10.2140/involve.2023.16.705.
5. P. Anitha and P. Rajasingh, *Power Domination in Tree Derived Architectures* (2020), on minimum circular-ladder power domination.
