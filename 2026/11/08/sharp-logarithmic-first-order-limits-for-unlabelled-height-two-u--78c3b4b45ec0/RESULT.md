# Sharp logarithmic first-order limits for unlabelled height-two unary forests

## Finding

Let \(\mathcal U_n\) be the set of isomorphism classes of structures \((V,f)\) with \(|V|=n\), one total unary operation, and \(f^3=f^2\). The probability measure is uniform on **isomorphism classes**, not on labelled functions. Let \(U_n=|\mathcal U_n|\), with \(U_0=1\), and put \(A=\pi^2/6\). Each connected component is a rooted tree of height at most two, with edges directed toward its unique fixed point.

**Theorem.** For every fixed first-order sentence \(\varphi\) in the language of one unary function, there is \(L_\varphi\in\{0,1\}\) for which
\[
\Pr_{\mathcal U_n}(\varphi)=L_\varphi+O_\varphi(1/\log n).
\]
This is a sharp universal rate. If \(\psi\) asserts the existence of a fixed point with no other preimage (equivalently, a singleton component), then
\[
\Pr_{\mathcal U_n}(\neg\psi)\sim \frac{\pi^2}{6\log n}.
\]

There is also a joint component-count limit. Fix pairwise nonisomorphic rooted components \(T_1,\ldots,T_r\) of heights at most two, set \(s_i=|T_i|\), and let \(M_i\) be the multiplicity of \(T_i\) in a uniformly sampled member of \(\mathcal U_n\). Then
\[
\left(\frac{A M_1}{\log n},\ldots,\frac{A M_r}{\log n}\right)
\ \xrightarrow{\ d\ }\ (E_1,\ldots,E_r),
\]
where the \(E_i\) are independent exponential random variables with **rates** \(s_i\). In particular, for any fixed positive integer \(b\) and any fixed component \(T\) of size \(s\),
\[
\Pr(M_T<b)\sim\frac{b s\pi^2}{6\log n}.
\]
The familiar unlabelled first-order zero-one law and the coefficient enumeration are **not** asserted to be new; the quantitative logarithmic scale, its leading constant, and the joint rescaled component law are the subject of the finding.

## Assumptions and scope

The language has exactly one unary function and equality, with no named colours, labels, order, or extra predicates. The identity \(f^3=f^2\) holds at every element. For all \(n\ge1\), sampling is uniform among the finitely many unlabelled isomorphism types. The height of a singleton component is zero. All convergence statements hold as \(n\to\infty\) through every positive integer. The number \(r\), the components \(T_i\), and each first-order sentence are fixed independently of \(n\). The zero-one rate constant may depend on the sentence, and the stated sharp constant concerns the particular singleton-component sentence.

Write \(p(m)\) for the ordinary integer partition function, with \(p(0)=1\). A connected tree of size \(m\) and height at most two consists of its root and an unordered collection of branches, with exactly one branch type of each positive size. Thus it has \(p(m-1)\) possible isomorphism types. The known forest enumeration is
\[
F(z)=\sum_{n\ge0}U_nz^n
=\prod_{m\ge1}(1-z^m)^{-p(m-1)}.
\]
Adjoining an additional root gives an ordinary rooted tree of height at most three, so \(U_n\) is the shift of the classical sequence OEIS A001383. This identity is background, not the new assertion.

## Proof

**1. Exact deletion identity.** Fix distinct component isomorphism types \(T_1,\ldots,T_r\) with sizes \(s_i\) and nonnegative integers \(b_i\). Adding \(b_i\) copies of each \(T_i\) is a bijection from \(\mathcal U_{n-h}\) to the isomorphism types in \(\mathcal U_n\) having at least \(b_i\) copies of every \(T_i\), where \(h=\sum_i b_i s_i\). Therefore, with \(U_j=0\) for \(j<0\),
\[
\Pr(M_i\ge b_i\text{ for all }i)=\frac{U_{n-h}}{U_n}.\tag{1}
\]
This bijection holds for unlabelled structures without combinatorial multiplicity factors.

**2. A coefficient-ratio lemma with an explicit saddle.** Write \(z=e^{-t}\),
\[
C(t)=e^{-t}\prod_{j\ge1}(1-e^{-jt})^{-1},\qquad
H(t)=\log F(e^{-t})=\sum_{k\ge1}\frac{C(kt)}{k}.
\]
The standard partition-product asymptotic (Euler's modular transformation, or the Hardy--Ramanujan asymptotic with a saddle summation) gives, as \(t\downarrow0\),
\[
C(t)=\sqrt{\frac{t}{2\pi}}\exp(A/t)\bigl(1+O(t)\bigr),
\quad -H'(t)=\frac{A C(t)}{t^2}\bigl(1+O(t)\bigr),
\quad H''(t)=\frac{A^2 C(t)}{t^4}\bigl(1+O(t)\bigr).\tag{2}
\]
For the derivatives, all terms with \(k\ge2\) are exponentially smaller than the \(k=1\) term, uniformly to every fixed derivative order. Set \(t_n>0\) to be the unique solution to \(-H'(t_n)=n\) (monotonicity follows from the positive variance of the Boltzmann size). Equation (2) yields
\[
n=\frac{A}{\sqrt{2\pi}}t_n^{-3/2}e^{A/t_n}(1+o(1)),
\qquad t_n\sim\frac{A}{\log n},
\qquad \sigma_n^2:=H''(t_n)\sim\frac{A n}{t_n^2}.\tag{3}
\]
The following uniform local estimate is sufficient:
\[
\frac{U_{n-h}}{U_n}=e^{-h t_n}\bigl(1+o(t_n)\bigr)
\quad\text{uniformly for integers }0\le h\le K\log n,\tag{4}
\]
for every fixed \(K>0\). Here are details of its analytic justification.

At \(t=t_n\), let \(N\) be the Boltzmann size with distribution \(\Pr_t(N=j)=U_j e^{-tj}/F(e^{-t})\). It has mean \(n\) and variance \(\sigma_n^2\). Its characteristic function satisfies
\[
\left|\mathbb E_t e^{i\theta N}\right|
\le\exp\left(-\sum_{m\ge1}p(m-1)e^{-tm}(1-\cos(m\theta))\right).\tag{5}
\]
By the classical Hardy--Ramanujan estimate \(p(m)\sim e^{\pi\sqrt{2m/3}}/(4\sqrt3m)\), a block of \(\Theta(t^{-3/2})\) consecutive integers centered at \(A/t^2\) carries a fixed positive fraction of \(C(t)\), and every weight in this block is bounded below by a constant times \(C(t)t^{3/2}\). For a block of \(L\ge2\) consecutive integers and \(|\theta|\le\pi\), the finite geometric-sum formula gives
\[
1-\left|L^{-1}\sum_{j=0}^{L-1}e^{ij\theta}\right|
\ge c\min\{1,L^2\theta^2\}
\]
with an absolute \(c>0\). Applied to that central block, (5) implies, for small \(t\),
\[
\left|\mathbb E_t e^{i\theta N}\right|
\le\exp\bigl(-c_1 C(t)\min\{1,t^{-3}\theta^2\}\bigr).\tag{6}
\]
Choose the central Fourier arc \(|\theta|\le (\log n)^3/\sigma_n\). On its complement, (3) and (6) bound the integral by \(\exp[-c_2(\log n)^5]\). On the central arc, the cumulant expansion gives
\[
\log\mathbb E_{t_n}e^{i\theta N}
=in\theta-\sigma_n^2\theta^2/2
+O\bigl(C(t_n)t_n^{-6}|\theta|^3\bigr).
\]
The remainder is uniformly \(O((\log n)^{10}/\sqrt n)\) on this arc. Fourier inversion therefore gives, uniformly for \(|h|\le K\log n\),
\[
\Pr_{t_n}(N=n-h)
=\frac{1}{\sqrt{2\pi}\sigma_n}
\left(1+O\left(\frac{(\log n)^{12}}{\sqrt n}\right)\right).\tag{7}
\]
Here \(h^2/\sigma_n^2=O(1/n)\) is negligible. Dividing the \(h\)-shifted version of (7) by its \(h=0\) version, and undoing the Boltzmann weight, proves (4), since \((\log n)^{12}/\sqrt n=o(t_n)\). The coefficient estimates are uniform for the stated range; no inference from finite numerical experiments is used.

**3. Logarithmic multiplicity law.** For any fixed nonnegative reals \(x_i\), choose \(b_i=\lceil x_i/t_n\rceil\), so the shift \(h=\sum_i b_i s_i\) is \(O(\log n)\). Inserting (4) into (1) yields
\[
\Pr(t_n M_i\ge x_i\text{ for all }i)
\longrightarrow\exp\bigl(-\sum_i s_i x_i\bigr).
\]
This is the joint survival function of independent exponentials of rates \(s_i\). Equation (3) allows replacement of \(t_n\) by \(A/\log n\). For a fixed integer \(b\ge1\), (1) and (4) also give
\[
\Pr(M_T<b)=1-\frac{U_{n-bs}}{U_n}
=1-e^{-bs t_n}(1+o(t_n))
=bs t_n+o(t_n)\sim\frac{bs A}{\log n}.\tag{8}
\]
The singleton case has \(s=b=1\), proving the stated leading constant.

**4. First-order saturation.** Fix a quantifier rank \(q\ge1\). A rooted tree of height at most two is described, up to the information needed for \(q\) rounds of the Ehrenfeucht--Fraïssé game, by counting the children of each of the finitely many branch types, with all counts truncated at \(q\); a branch type is itself the number of its leaves, truncated at \(q\). Thus there are finitely many such capped component profiles. Each profile admits a finite exact representative \(T\). If a forest contains at least \(q\) copies of every representative, then all its component profiles are represented at least \(q\) times. Any two such forests are equivalent for \(q\) first-order quantifier rounds: the duplicator always matches a selected component, child-branch, and leaf to a like capped type, and fewer than \(q\) previous choices cannot exhaust a category with at least \(q\) representatives. The map preserves all iterates of \(f\) because each selected vertex's closure has at most three vertices. This is the standard bounded-height component Ehrenfeucht--Fraïssé strategy, stated here for the unary language.

By (8), for each representative \(T\) of size \(s\), the probability of fewer than \(q\) copies is \(O_q(s/\log n)\). There are finitely many representatives for fixed \(q\), so the probability of failure of simultaneous saturation is \(O_q(1/\log n)\). Every rank-\(q\) sentence has one constant truth value on the saturated forests. Therefore its probability differs from that value by \(O_q(1/\log n)\). The singleton sentence from step 3 makes this universal order sharp.

## Verification

The standalone `checker.py` independently computes the integer partition numbers by two recurrences, derives the unlabelled forest counts both from the product and from a logarithmic-derivative recurrence, and directly enumerates isomorphism classes of small unary functions. The product and recurrence agree through size 48; direct orbits agree through size 5. The sequence agrees with OEIS A001383 after a one-vertex shift. The checker also tests the Euler partition-product asymptotic numerically, and its run reports `ALL_CHECKS_OK`. These finite checks corroborate the exact combinatorial identities only; the analytic coefficient-ratio bound and first-order conclusion are established in the proof above.

For reproducibility, run `python3 checker.py` using Python 3 with its standard library. No external data files or downloaded software are required.

## Relationship to prior work

Koponen's 2026 treatment of finite-model properties and finite base structures includes bounded-height directed acyclic graphs with bounded numbers of parents (Example 2.2); the present one-parent height-two unary class is a concrete model in that setting. Compton's method, as presented and strengthened by Bell, Burris and Yeats, already proves a qualitative first-order (indeed monadic second-order) zero-one law for many component-closed unlabelled forests of bounded height. That qualitative result is not new here. Riordan's 1960 height enumerations and OEIS A001383 already give the ordinary generating product and exact counts for the equivalent height-three rooted-tree census. Those enumerative identities are also not new here.

The assertion isolated for comparison is the precise \(\pi^2/(6\log n)\) first-order obstruction together with the joint independent exponential law for fixed component multiplicities at the same logarithmic scale. Generic weighted-partition asymptotics and conditioning methods provide nearby techniques, but the specific probability and logical rate are not stated by the inspected sources.

## Limitations

The probability space is uniform on isomorphism classes and is not the labelled uniform random-function model. The formula is specific to the one-function identity \(f^3=f^2\); arbitrary functional digraphs or larger fixed heights are not covered. The first-order error bound is sentence-dependent and need not be attained by every sentence. The exponential-law conclusion is for a fixed finite list of component types; it does not assert joint convergence over infinitely many types or a total-variation limit. Historical-priority uncertainty remains for older weighted-partition literature under different terminology, despite explicit comparison with the classical exact enumeration and logical zero-one results.

## References

1. V. Koponen, *A characterization of the finite model property for omega-categorical theories*, arXiv:2610.16163, first submitted 12 October 2026, especially Example 2.2 and the discussion of finite base structures. https://arxiv.org/abs/2610.16163
2. J. Bell, S. Burris, K. Yeats, *Monadic Second-Order Classes of Forests with a Monadic Second-Order 0-1 Law*, arXiv:1004.1128, 2010, especially Theorem 1.1, Corollary 1.2 and Sections 3--4. https://arxiv.org/abs/1004.1128
3. J. Riordan, *The Enumeration of Trees by Height and Diameter*, IBM Journal of Research and Development 4 (1960), 473--478, especially Section 2 and equation (1a). DOI: 10.1147/rd.45.0473. Open annotated copy: https://oeis.org/A007401/a007401_8.pdf
4. OEIS A001383, *Number of n-node rooted trees of height at most 3*, including the exact Euler-product formula. https://oeis.org/A001383
5. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, Proceedings of the London Mathematical Society (1918), for the classical integer-partition asymptotic.
6. L. Mutafchiev, *Limit Theorems for the Number of Parts in a Random Weighted Partition*, Electronic Journal of Combinatorics 18 (2011), P206, DOI: 10.37236/693; a nearby but distinct total-part-count setting.
