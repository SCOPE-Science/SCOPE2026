# Sharp first-order convergence speed in unlabelled coloured star forests

## Finding

Uniformly sample **isomorphism classes**, not labelled realizations, of finite coloured directed star forests. For each fixed integer \(q\ge1\), every first-order sentence \(\varphi\) has a limiting probability \(L_\varphi\in\{0,1\}\), and

\[
\Pr_n(\varphi)=L_\varphi+O_{q,\varphi}\bigl(n^{-1/(q+1)}\bigr).
\]

The exponent \(1/(q+1)\) is sharp **uniformly over first-order sentences**: the sentence that some isolated vertex has a specified colour satisfies

\[
\Pr_n(\exists\text{ an isolated vertex of colour }1)
=1-\kappa_q n^{-1/(q+1)}+o\bigl(n^{-1/(q+1)}\bigr),
\qquad \kappa_q=\bigl(q^2\zeta(q+1)\bigr)^{1/(q+1)}.
\]

The qualitative zero–one law is not claimed as new. It is a consequence of Bell's published general monadic-second-order theorem for classes with polynomially many indecomposables. The finding is the sharp quantitative refinement for the specified low-height, uniformly unlabelled class, together with its explicit leading constant.

## Assumptions and scope

Fix \(q\in\mathbb Z_{\ge1}\). The vocabulary is a directed binary relation \(E\) and \(q\) named, exhaustive, pairwise disjoint unary colour predicates. A directed star is either one isolated vertex or a component consisting of one root, with an outgoing edge from the root to each other vertex and no further edges. A star forest is a disjoint union of these components. This is the height-one, one-parent case of a finite directed-acyclic hierarchy. The sample space \(\mathcal S_{q,n}\) consists of *isomorphism classes* of \(n\)-vertex structures, each with equal probability, for integers \(n\ge1\). The empty forest is included only in counting identities, with \(u_{q,0}=1\).

For the component-count statements, choose any single specified complete coloured star type \(\tau\), and write \(M_\tau\) for its multiplicity and \(\ell=|\tau|\ge1\). Integers \(h\ge0\), \(r\ge1\) and \(q\ge1\) are fixed before \(n\to\infty\). Constants in the sentence-level error may depend on \(q\) and on the sentence, but not on \(n\).

## Proof

**1. Exact component enumeration and deletion.** A star with \(m\ge1\) vertices is determined by its root's colour and the multiplicities of the \(q\) leaf colours, summing to \(m-1\). Thus the exact number of isomorphism classes of single stars of size \(m\) is

\[
a_{q,m}=q\binom{m+q-2}{q-1}.
\]

Unique decomposition into a multiset of connected components gives the ordinary generating function

\[
F_q(z):=\sum_{n\ge0}u_{q,n}z^n
=\prod_{m\ge1}(1-z^m)^{-a_{q,m}}.
\]

Deleting \(r\) copies of one selected complete star type is a bijection from forests with at least \(r\) such copies to all size-\(n-r\ell\) forests. Consequently, **exactly** for \(n\ge r\ell\),

\[
\Pr_n(M_\tau\ge r)=\frac{u_{q,n-r\ell}}{u_{q,n}}.\tag{1}
\]

**2. A sharp fixed-shift coefficient ratio.** Put \(a_m=a_{q,m}\). For \(t>0\), independently choose one geometric random variable \(X_{m,j}\) for each single-star type, with

\[
\Pr_t(X_{m,j}=k)=(1-e^{-mt})e^{-mtk},
\quad k\ge0,\quad 1\le j\le a_m,
\qquad S_t=\sum_{m\ge1}\sum_{j=1}^{a_m}mX_{m,j}.
\]

This sum is finite almost surely and has the exact coefficient identity

\[
\Pr_t(S_t=s)=\frac{u_{q,s}e^{-ts}}{F_q(e^{-t})},
\qquad s\ge0.\tag{2}
\]

Choose the unique saddle \(t=t_n>0\) satisfying \(\mathbb E_tS_t=n\). Since \(a_m=q m^{q-1}/(q-1)!+O_q(m^{q-2})\) for \(q\ge2\), with \(a_m=1\) when \(q=1\), standard Riemann-sum estimates for the Bose–Einstein kernel give

\[
\begin{aligned}
\mathbb E_t S_t
&=\sum_{m\ge1}\frac{a_m m}{e^{mt}-1}
=q^2\zeta(q+1)t^{-(q+1)}\bigl(1+O_q(t)\bigr),\\
\sigma_t^2:=\operatorname{Var}_t(S_t)
&=\sum_{m\ge1}\frac{a_m m^2e^{mt}}{(e^{mt}-1)^2}
\sim q^2(q+1)\zeta(q+1)t^{-(q+2)}.
\end{aligned}\tag{3}
\]

In particular,

\[
t_n=\kappa_q n^{-1/(q+1)}+O_q\bigl(n^{-2/(q+1)}\bigr),
\quad \kappa_q=(q^2\zeta(q+1))^{1/(q+1)}.\tag{4}
\]

For completeness, here are Fourier estimates justifying the **precision** of the ratio, beyond a qualitative central limit theorem. The characteristic function of \(S_t\) is

\[
\Phi_t(\theta)=\prod_{m\ge1}
\left(\frac{1-e^{-mt}}{1-e^{-mt+im\theta}}\right)^{a_m},
\qquad -\pi\le\theta\le\pi.
\]

For \(|\theta|\le t\), the terms with \((2t)^{-1}\le m\le t^{-1}\) and \(1-\cos(m\theta)\ge c(m\theta)^2\) yield

\[
|\Phi_t(\theta)|\le \exp\bigl(-c_q\sigma_t^2\theta^2\bigr).
\]

For \(t\le|\theta|\le\pi\), the same band of integers has \(e^{-mt}\) bounded away from both zero and one and obeys the elementary trigonometric bound

\[
\sum_{(2t)^{-1}\le m\le t^{-1}}
(1-\cos(m\theta))\ge c/t.
\]

To see the latter uniformly: when \(|\theta|/t\) stays bounded away from zero and infinity, divide by \(t^{-1}\) and use the positive integral of \(1-\cos(sx)\) on \([1/2,1]\); when \(|\theta|/t\to\infty\), the finite-geometric-sum bound makes the mean cosine negligible (with the usual small-angle denominator bound), uniformly for \(|\theta|\le\pi\). Since \(a_m\ge c_q t^{-(q-1)}\) on that band, this gives

\[
|\Phi_t(\theta)|\le \exp(-c_q t^{-q})
\quad\text{for }t\le|\theta|\le\pi.\tag{5}
\]

The third absolute cumulant is \(O_q(t^{-(q+3)})\), whereas \(\sigma_t^3\asymp t^{-3(q+2)/2}\). Thus the normalized third-cumulant scale tends to zero as \(O_q(t^{q/2})\). Fourier inversion at the mean, using (5), proves the lattice local limit

\[
\Pr_t(S_t=\mathbb E_t S_t)
\sim (2\pi\sigma_t^2)^{-1/2}
\]

when the mean is integral. More importantly, for fixed \(h\ge0\), the difference of the inversion integrands for \(S_t=n\) and \(S_t=n-h\) is bounded by \(h|\theta||\Phi_t(\theta)|\). Integrating (5) gives an absolute difference \(O_{q,h}(\sigma_t^{-2})\), and hence

\[
\frac{\Pr_t(S_t=n-h)}{\Pr_t(S_t=n)}
=1+O_{q,h}(\sigma_t^{-1})
=1+O_{q,h}\bigl(t^{(q+2)/2}\bigr).
\]

Substitute into (2) with \(t=t_n\). Since \((q+2)/2>1\), equations (3)–(4) imply the **sharp fixed-shift formula**

\[
\boxed{\frac{u_{q,n-h}}{u_{q,n}}
=1-h\kappa_q n^{-1/(q+1)}
+o_{q,h}\bigl(n^{-1/(q+1)}\bigr)}.\tag{6}
\]

The argument proves a fixed-shift asymptotic; it does not claim uniformity when \(h\) grows with \(n\).

**3. Uniform first-order speed.** Fix a sentence of quantifier rank \(r\ge1\). Two stars have the same \(r\)-profile if their root colours agree and the numbers of leaves of each colour agree after replacing every count greater than or equal to \(r\) by the common symbol \(\ge r\). There are finitely many such profiles. For every profile choose one canonical star whose leaf multiplicities are precisely \(0,1,\ldots,r\), taking \(r\) whenever the profile says \(\ge r\). Let \(B_r\) be the finite set of these canonical complete star types.

Call a forest \(r\)-rich if it contains at least \(r\) separate copies of every member of \(B_r\). Any two \(r\)-rich forests are \(r\)-round Ehrenfeucht–Fraïssé equivalent: a Spoiler move inside a previously used component is answered inside its already paired component, preserving root, colour and adjacency; the capacity to answer at most \(r\) leaf selections follows from the truncated leaf counts. A move inside a fresh component is answered inside an unused canonical component of its same profile. There is always an unused such copy because at most \(r-1\) different components have previously been paired. This preserves a partial isomorphism for all \(r\) rounds.

It follows that the truth value of the rank-\(r\) sentence is a constant \(L_\varphi\in\{0,1\}\) on \(r\)-rich forests. From the deletion identity (1), the union bound, and (6),

\[
\Pr_n(\text{not }r\text{-rich})
\le\sum_{\tau\in B_r}
\left(1-\frac{u_{q,n-r|\tau|}}{u_{q,n}}\right)
=O_{q,r}\bigl(n^{-1/(q+1)}\bigr).
\]

Therefore \(\Pr_n(\varphi)=L_\varphi+O_{q,\varphi}(n^{-1/(q+1)})\), as claimed. Quantifier-free sentences without constants are eventually constant, so they also satisfy the conclusion.

**4. Sharpness.** Let \(\iota_1\) say that an isolated vertex of named colour \(1\) exists. It is a fixed first-order sentence, and the singleton of this colour is a unique complete component type of size one. Equations (1) and (6) give

\[
\Pr_n(\iota_1)=\frac{u_{q,n-1}}{u_{q,n}}
=1-\kappa_q n^{-1/(q+1)}+o\bigl(n^{-1/(q+1)}\bigr).
\]

Its nonzero leading error proves that no larger universal decay exponent is valid for all first-order sentences.

## Verification

The accompanying self-contained standard-library Python checker independently constructs all coloured single-star types through size eight, compares their explicit multiset generating counts with the recurrence obtained from the Euler product, and verifies the exact selected-component deletion bijection for several colours, sizes and multiplicity thresholds. It also evaluates the proposed scaling numerically at size 400 for one, two and three colours. Execute `python checker.py` from the directory containing this package; its final line should be `ALL_CHECKS_OK`.

These are finite tests only. They are not an exhaustive proof of the coefficient-ratio asymptotics or of the Ehrenfeucht–Fraïssé statement. The infinite conclusions follow from the displayed analytic and logical arguments.

## Relationship to prior work

Koponen (2026) studies finite-model questions and logical convergence for expansions of finite base structures. Its Example 2.2 includes bounded-height finite directed acyclic graphs with bounded parent numbers, motivating the height-one, one-parent family studied here. The inspected introductory material and example do not state a quantitative isomorphism-uniform convergence speed for this family; the complete manuscript was not fully available during this comparison.

Bell (2002), building on Compton's qualitative logical limit laws, proves that a component-closed relational class with polynomially bounded numbers of indecomposable types has a **monadic second-order zero–one law** under uniform sampling of isomorphism classes. Since \(a_{q,m}\) here is a polynomial in \(m\), the **unquantified zero–one law is covered by that published theorem** and is not attributed to the present finding. Burris, Compton, Odlyzko and Richmond (1997) provide a related general first-order zero–one criterion; the full relevant theorem and its asymptotic section were inspected. Bell and Burris (2003) address general ratio-test conditions for limit laws. Standard partition asymptotics underlie the coefficient analysis.

The contribution claimed here is the **explicit sharp universal first-order convergence exponent \(1/(q+1)\)** for these unlabelled coloured star forests and its exact obstruction constant \(\kappa_q\). The older broad qualitative results and classical coefficient techniques are credited. Searches did not locate an earlier theorem stating or directly implying this sharp speed for this family, but an equivalent quantitative result under generalized-partition terminology remains possible.

## Limitations

The result is for fixed \(q\), fixed first-order sentences and uniform **isomorphism-class** sampling; it does not apply unchanged to uniformly labelled structures, variable colours, richer DAG classes, arbitrary sentence families whose ranks grow, or arbitrary quantifier logics. The shift \(h\) is fixed. The qualitative zero–one law is known from more general prior work. Independent priority review and independent mathematical audit have not been performed. An inaccessible relevant quantitative result from the extensive older partition literature could change the originality assessment.

## References

1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories* (2026), arXiv:2610.16163, first public 2026-10-12, https://arxiv.org/abs/2610.16163.
2. J. P. Bell, *Sufficient conditions for zero-one laws*, Transactions of the American Mathematical Society **354** (2002), 613–630, DOI: 10.1090/S0002-9947-01-02884-7.
3. S. Burris, K. Compton, A. Odlyzko and B. Richmond, *Fine Spectra and Limit Laws, II: First-Order 0–1 Laws*, Canadian Journal of Mathematics **49** (1997), 641–652, DOI: 10.4153/CJM-1997-030-6.
4. J. P. Bell and S. Burris, *Asymptotics for logical limit laws: When the growth of the components is in an RT class*, Transactions of the American Mathematical Society **355** (2003), 3777–3794, DOI: 10.1090/S0002-9947-03-03299-9.
5. K. J. Compton, *A logical approach to asymptotic combinatorics. II: Monadic second-order properties*, Journal of Combinatorial Theory, Series A **50** (1989), 110–131.
