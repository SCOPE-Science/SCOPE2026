# Golden-mean periodic cylinders: a Mahler law and a sharp parity split

## Finding

In the golden-mean one-sided subshift, forbid the block `11`. Sample uniformly from all admissible length-\(n\) words, and let \(\eta_n\) be the least period of an infinite periodic admissible sequence beginning with the sampled word. The full-period atom \(P_n=\Pr\{\eta_n=n\}\) has a sharp parity-dependent correction to its limiting probability. For \(n\ge2\), it equals the unbordered-word proportion; the scalar generating law below is the weight-one specialization of [6] and is included as the starting point for the refinement:

\[
P_n=\frac{2t_n}{F_{n+2}},\qquad
T(z)=\sum_{n\ge2}t_nz^n,\qquad
(1-z-z^2)T(z)+T(z^2)=z^2.
\]

Here \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and each \(t_n\) is a nonnegative integer. Define

\[
\varphi=\frac{1+\sqrt5}{2},\quad q=\varphi^{-1},\quad
A=\frac{q^2-T(q^2)}{1+q^2},\quad p_*=2\sqrt5\,q^2 A,
\]
\[
K_0=\frac{p_*q}{1-q^3},\qquad
K_1=\frac{p_*}{\sqrt q\,(1-q^3)}.
\]

Then \(A,p_*,K_0,K_1>0\), and, as \(n\to\infty\) through integers,

\[
\boxed{P_n=p_*+K_{n\bmod2}\,\varphi^{-n/2}+O(\varphi^{-3n/4})}.
\]

Numerically \(p_*\approx0.1556298471279007\), \(K_0\approx0.1259071911584468\), and \(K_1\approx0.2591385329674485\). The two corrections have the same exponential rate but different, strictly positive coefficients: \(K_1/K_0=\varphi^{3/2}>1\). The pole argument also explains why the unit circle is a natural boundary for meromorphic continuation of \(T\).

## Assumptions and scope

The space is \(X=\{x\in\{0,1\}^{\mathbb N_0}:x_jx_{j+1}\ne11\ \forall j\}\), with left shift. All counts concern **distinct indexed length-\(n\) words**, not rotation orbits or individual periodic points. A word \(w\) is *unbordered* if no nonempty proper prefix equals a suffix of the same length. For \(w\) in the admissible language, \(\eta_n(w)\) is the minimum least shift period among **one-sided infinite admissible periodic sequences** starting with \(w\). The sampling distribution is uniform over its \(F_{n+2}\) admissible words, not an arbitrary Bernoulli input. Limits are for every integer \(n\to\infty\); the correction constants depend on parity.

## Proof

**1. Periodic penetration equals the ordinary least word period.** Let \(p\) be the least (ordinary) combinatorial period of an admissible word \(w=w_0\cdots w_{n-1}\), where \(w_i=w_{i+p}\) whenever both indices are in range. If \(p<n\), the first \(p\) letters repeated indefinitely contain no adjacent `11`: every transition inside the repeating block, including its wrap-around transition, already occurs inside \(w\) (the latter is the transition from \(w_{p-1}\) to \(w_p=w_0\)). Therefore the periodic continuation is admissible. If \(p=n\), the word is unbordered, and in the binary alphabet its first and last letters must differ. Its \(n\)-periodic continuation is again admissible. Any periodic point with a prefix \(w\) induces a combinatorial period on \(w\), and its least period cannot be smaller than the least word period. Thus \(\eta_n(w)=p\), and \(\eta_n(w)=n\) exactly when \(w\) is unbordered.

**2. Unique shortest-border decomposition.** In an unbordered binary word of length at least two, the endpoints differ. Reversal preserves the no-`11` constraint and swaps the two endpoint orientations. Define \(t_n\) to be the number of unbordered, admissible length-\(n\) words beginning in `0` and ending in `1`. The total number of unbordered admissible words is \(2t_n\). There are \(F_{n-1}\) admissible length-\(n\) words with those prescribed endpoints (count the \(n-2\) interior symbols, using the forced `0` before the terminal `1`).

A bordered word with endpoints `0`, `1` has a **unique shortest nonempty border** \(u\), which must itself be unbordered, begin in `0`, end in `1`, and have length \(2\le k\le\lfloor n/2\rfloor\). Indeed, a border of length \(k>n/2\) induces a period \(n-k<k\) on the whole word, hence also on its length-\(k\) prefix; that would give a proper border of \(u\). The original word is uniquely \(u v u\), with \(|v|=n-2k\). The join after the first \(u\), ending in `1`, requires \(v\) to begin with `0` when it is nonempty; the join into the second \(u\), beginning with `0`, imposes no additional restriction. Hence the admissible fillings of length \(m\) number \(F_{m+1}\), including the empty filling \(m=0\). Conversely, any \(u v u\) so formed has shortest border \(u\), since a shorter border would also be a border of \(u\). Therefore

\[
\boxed{t_n=F_{n-1}-\sum_{k=2}^{\lfloor n/2\rfloor}t_k F_{n-2k+1}}\quad(n\ge2).
\]

Multiplying by \(z^n\), summing, and using \(\sum_{m\ge0}F_{m+1}z^m=(1-z-z^2)^{-1}\) yields \((1-z-z^2)T(z)+T(z^2)=z^2\), including \(t_2=1\). This exact identity needs no limiting or independence assumption.

**3. The first pole and its positive residue coefficient.** Put \(D(z)=1-z-z^2=(1-z/q)(1+qz)\). Since \(0\le t_n\le F_{n-1}\), the series \(T(z)\) converges at least in \(|z|<q\), and \(T(z^2)\) is analytic in \(|z|<\sqrt q\). The functional equation continues \(T\) meromorphically into \(|z|<\sqrt q\), with at most a pole at \(z=q\). It is a genuine pole: at \(y=q^2\),

\[
0\le T(y)\le\sum_{n\ge2}F_{n-1}y^n=\frac{y^2}{1-y-y^2}<y,
\]

because \(2y+y^2<1\) for \(y=q^2\). The positive coefficient of \((1-z/q)^{-1}\) at the simple pole \(z=q\) is precisely

\[
A=\frac{q^2-T(q^2)}{1+q^2}>0.
\]

**4. Square-root poles and the two parity coefficients.** The same equation \(T(z)=[z^2-T(z^2)]/D(z)\), iterated, gives a meromorphic continuation throughout \(|z|<1\). Let \(s=\sqrt q\). The poles at \(\pm s\) are genuine, and their principal parts, written as multiples of \((1-z/(\pm s))^{-1}\), are

\[
b_+=\frac{A}{2(s-q^2)},\qquad
b_-=-\frac{A}{2(s+q^2)}.
\]

Indeed \(T(z^2)\) contributes \(A/(1-z^2/q)\) and each root contributes half that coefficient, with a minus sign from the functional equation. Since \(D(s)=q^2-s\) and \(D(-s)=q^2+s\), the expressions follow. The next poles have modulus \(q^{1/4}\). Subtract the three principal parts at \(q,\pm s\) and the four principal parts on modulus \(q^{1/4}\); the remainder is analytic in a disk of radius strictly greater than \(q^{1/4}\). Cauchy's coefficient bound now gives

\[
t_n=Aq^{-n}+[b_++(-1)^n b_-]s^{-n}+O(q^{-n/4}).
\]

Direct algebra simplifies

\[
\frac{b_++b_-}{A}=\frac{q}{1-q^3},\qquad
\frac{b_+-b_-}{A}=\frac{1}{\sqrt q\,(1-q^3)}.
\]

Finally \(F_{n+2}=\varphi^{n+2}/\sqrt5+O(\varphi^{-n-2})\). Divide \(2t_n\) by this expression to obtain the claimed constant, the two parity coefficients, and the error \(O(\varphi^{-3n/4})\). The Fibonacci denominator error decays faster than this remainder. Both correction coefficients are positive and distinct.

**5. Natural boundary.** The simple pole at \(q\) propagates under every choice of square-root preimages: at each radius \(q^{1/2^j}\), the \(2^j\) preimages are genuine poles because \(D(z)\ne0\) there for \(j\ge1\). Their arguments are all dyadic rational multiples of a full turn, dense on the unit circle, and their radii approach one from below. Every neighborhood of every point on \(|z|=1\) therefore contains interior poles. Meromorphic continuation across any arc would require a meromorphic function whose isolated poles accumulate at an interior point, which is impossible. Thus \(|z|=1\) is a natural boundary to meromorphic continuation.

## Verification

The Python 3 program `checks/verify.py` requires only the standard library. It enumerates every admissible word at lengths \(2\) through \(15\), tests the ordinary-period/unbordered equivalence and the exact counts, checks the \(219\) integer coefficient identities of degrees \(2\) through \(220\), and evaluates finite-length approximations to both parity coefficients. It prints \(t_2,\ldots,t_{16}=1,1,1,2,2,4,5,9,12,21,31,52,79,131,205\). Truncating \(T(q^2)\) at degree \(220\) leaves a positive tail bounded by \(q^{222}/(1-q)<1.1\times10^{-46}\). The finite checks do not prove the asymptotic or the continuation statement.

## Relationship to prior work

Pannipitiya's November 2026 analysis defines periodic-orbit penetration times and gives a uniform \(n+K-1\) upper bound for mixing finite-type shifts in Proposition 2.27. The present theorem computes a particular **nontrivial limiting atom and its sharp residue-class correction**, not a bound on the largest penetration time or a normalized average.

Holub and Shallit (2016), Section 4.1, give exact recurrences and unbordered probabilities for uniformly sampled **unrestricted** \(q\)-ary words (including the independent binary case). Their Theorem 7 is not the recurrence for the adjacent-`11`-avoiding language, and their limit \(0.2677868402\ldots\) differs from the constrained value here. Régnier (1992), Sections 1–3, develops shortest-border generating functions for unrestricted \(q\)-ary words; the constrained transition weights, Fibonacci normalization, and two square-root pole coefficients do not occur in its statement.

A general finite-type result [4] proves exponential tail bounds for the shortest-period deficit and an exact expectation of the number of qualifying periods, not an exact atom asymptotic. The individual morphic Fibonacci word [5] is also different from the full language of `11`-avoiding words.

The closest counting result is [6]. Its bivariate enumerator \(U(z,t)\), at weight \(t=1\), is \(2z+2T(z)\); its equation, unweighted recurrence and limiting constant are exactly the baseline used here, including a bound \(P_n-p_*=O(\varphi^{-n/2})\). The refinement here extracts the two actual nonzero leading coefficients from the poles at \(\pm\sqrt q\), and separates them from the next pole shell with a smaller error. The limiting constant and recurrence are not presented as distinct contributions, and the natural boundary is an accompanying consequence of the meromorphic pole cascade.

## Limitations

This result concerns the single binary one-step shift forbidding `11`, uniform finite-word sampling, and the full-length penetration atom \(\Pr\{\eta_n=n\}\). It does **not** give the entire distribution of \(\eta_n\), nor a universal formula for arbitrary finite-type shifts or nonuniform Gibbs sampling. Numerical constants are derived from a convergent series, not asserted to be rational or algebraic. The comparison does not establish exhaustive publication priority.

## References

1. D. N. Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1 (first publicly posted 10 November 2026), especially Proposition 2.27, https://arxiv.org/abs/2611.13416.
2. Š. Holub and J. Shallit, *Periods and Borders of Random Words*, STACS 2016, LIPIcs 47, art. 44, DOI:10.4230/LIPIcs.STACS.2016.44, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.44.
3. M. Régnier, *Enumeration of bordered words, le langage de la vache-qui-rit*, RAIRO 26(4) (1992), 303–317, https://www.numdam.org/item/ITA_1992__26_4_303_0/.
4. *Entropy-sharp periodic-cylinder closure and parity-oscillating short-period counts* (2026), https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-entropy-sharp-periodic-cylinder-closure-and-parity-oscillating-s--22e18f2d92a1.
5. H. Mousavi, L. Schaeffer, and J. Shallit, *Decision Algorithms for Fibonacci-Automatic Words, I: Basic Results*, RAIRO 50 (2016), 39–66, DOI:10.1051/ita/2016010 (the morphic Fibonacci-word setting).
6. *A weight-refined border-free spectrum for Fibonacci-admissible binary words* (2026), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-weight-refined-border-free-spectrum-for-fibonacci-admissible-b--491b08dec094, equations (1)–(4).
