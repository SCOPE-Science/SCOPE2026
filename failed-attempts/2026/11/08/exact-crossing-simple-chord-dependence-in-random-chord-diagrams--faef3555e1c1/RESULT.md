# Exact crossing–simple-chord dependence in random chord diagrams

## Finding

Let \(n\ge 2\), and choose a perfect matching of \(2n\) clockwise-labelled points on a circle uniformly among the \((2n-1)!!\) matchings. Write \(X_n\) for the number of pairs of crossing chords and \(S_n\) for the number of *simple chords*, meaning chords whose endpoints are consecutive modulo \(2n\). Set \(X_0=0\). For \(0\le k\le n\), define

\[
 c_{n,k}=\frac{\displaystyle\frac{2n}{2n-k}\binom{2n-k}{k}}
 {\displaystyle\prod_{j=0}^{k-1}(2n-2j-1)},\qquad c_{n,0}=1.
\]

**Theorem (exact joint deletion law and Gaussian–Poisson separation).** For every complex-valued function \(f\) on \(\{0,\ldots,\binom n2\}\), with the obvious restriction of its domain when evaluating \(X_{n-k}\),

\[
 \mathbb E\!\left[\binom{S_n}{k}f(X_n)\right]
       =c_{n,k}\,\mathbb E[f(X_{n-k})]. \tag{1}
\]

In particular, writing \(Q_m(z)=\mathbb E[z^{X_m}]\) (and \(Q_0(z)=1\)), the **entire finite joint probability-generating polynomial** is

\[
 \boxed{\mathbb E[z^{X_n}u^{S_n}]
       =\sum_{k=0}^{n} c_{n,k}(u-1)^k Q_{n-k}(z).} \tag{2}
\]

The exact Pearson correlation is strictly negative and has the striking simple form

\[
 \boxed{\operatorname{Corr}(X_n,S_n)=-\sqrt{\frac5{n+3}}.} \tag{3}
\]

Finally, with

\[
 \mu_n=\frac{n(n-1)}6,\qquad
 \sigma_n^2=\frac{n(n-1)(n+3)}{45},\qquad
 W_n=\frac{X_n-\mu_n}{\sigma_n},
\]

for every real \(t\) and complex \(u\),

\[
 \boxed{\lim_{n\to\infty}\mathbb E[e^{itW_n}u^{S_n}]
       =e^{-t^2/2}e^{u-1}.} \tag{4}
\]

Consequently \((W_n,S_n)\) converges jointly to an **independent** standard normal and mean-one Poisson pair. Formula (4) is a joint statement, not merely two separate marginal limit theorems.

## Assumptions and scope

The endpoints are distinguished and have their fixed clockwise order. Every perfect matching is equally likely; no independence assumption is made between its chord indicators. A crossing means alternating endpoints, while a simple chord uses consecutive cyclic endpoints, including the wrap-around pair \((2n,1)\). Formulae (1)–(3) hold for all integers \(n\ge2\) exactly. Formula (4) concerns \(n\to\infty\). The zero-chord diagram is defined to have no crossings. Falling-factorial conventions give an empty product equal to one.

For explicit computation of \(Q_m\), the classical Touchard–Riordan polynomial satisfies, for \(m\ge1\),

\[
 (2m-1)!!\,Q_m(z)=\frac{1}{(1-z)^m}
 \sum_{j=-m}^{m}(-1)^j z^{j(j-1)/2}\binom{2m}{m+j}, \tag{5}
\]

with the removable singularity at \(z=1\) understood by polynomial continuation. Equation (2) therefore determines every joint mass; alternatively \(Q_m\) can be computed directly by enumerating perfect matchings.

## Proof

**1. Fixing simple chords deletes them without changing crossings.** Let \(F\) be any specified set of \(k\) mutually vertex-disjoint consecutive-edge pairs on the cycle of \(2n\) endpoints. All its chords are noncrossing and none can cross any other chord. Conditional on their presence, the perfect matching of the remaining \(2(n-k)\) endpoints is uniform. Deleting the endpoints of \(F\) keeps the remaining cyclic order; hence every pair of remaining chords crosses before deletion if and only if it crosses afterward. Thus the conditional crossing statistic is exactly distributed as \(X_{n-k}\), not merely approximated by it. The probability of the prescribed edges is

\[
 \frac{(2n-2k-1)!!}{(2n-1)!!}
 =\prod_{j=0}^{k-1}(2n-2j-1)^{-1},
\]

using \((-1)!!=1\) when \(k=n\).

**2. Counting prescribed disjoint simple chords.** For \(k\ge1\), the number of \(k\)-edge matchings in the cycle on \(2n\) vertices is

\[
 m_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k}
 =\frac{2n}{k}\binom{2n-k-1}{k-1}.
\]

Indeed, identify each chosen cycle edge by its clockwise initial vertex. Those \(k\) initial vertices cannot be adjacent. Mark a start vertex, distribute the \(2n-2k\) *extra* unmarked vertices among the \(k\) cyclic gaps, each of which already contains one required unmarked vertex, and divide by the \(k\) possible marked starts; this gives the displayed count, also valid at \(k=n\). Summing the conditional identity from step 1 over all such \(F\) proves (1), because \(\binom{S_n}{k}\) counts exactly the chosen subcollections of existing simple chords. Expanding \(u^{S_n}=(1+(u-1))^{S_n}\) proves (2).

**3. Covariance and correlation.** Taking \(f=1\) in (1) yields

\[
 \mathbb E[(S_n)_k]=k!c_{n,k}
  =\prod_{j=0}^{k-1}\frac{2n-2j}{2n-j-1}. \tag{6}
\]

In particular, \(\mathbb E[S_n]=\mathbb E[(S_n)_2]=2n/(2n-1)\), and therefore

\[
 \operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2}.
\]

Taking \(k=1\) and \(f(x)=x\) in (1) gives

\[
 \mathbb E[S_nX_n]=\frac{2n}{2n-1}\mathbb E[X_{n-1}].
\]

The classical crossing moments, also independently obtainable by counting pairs of crossing indicators, are

\[
 \mathbb E X_m=\frac{m(m-1)}6,\qquad
 \operatorname{Var}(X_m)=\frac{m(m-1)(m+3)}{45}.
\]

Consequently

\[
 \operatorname{Cov}(X_n,S_n)
 =\frac{2n}{2n-1}\left(\frac{(n-1)(n-2)}6-\frac{n(n-1)}6\right)
 =-\frac{2n(n-1)}{3(2n-1)}.
\]

Dividing by the two positive standard deviations gives (3), including the boundary case \(n=2\), where the correlation is \(-1\).

**4. Joint convergence rather than marginal convergence alone.** For each fixed \(k\), the product in (6) tends to one, so \(c_{n,k}\to1/k!\). The ratio between successive products is

\[
 \frac{\mathbb E[(S_n)_{k+1}]}{\mathbb E[(S_n)_k]}
 =\frac{2n-2k}{2n-k-1}\le1\quad(k\ge1),
\]

and \(\mathbb E[(S_n)_1]=2n/(2n-1)\le4/3\). Thus \(0\le c_{n,k}\le4/(3k!)\), with \(c_{n,k}=0\) for \(k>n\). This gives an absolutely and uniformly summable expansion for every fixed complex \(u\).

For fixed \(k\), (1) with \(f(x)=\exp(it(x-\mu_n)/\sigma_n)\) gives the mixed characteristic/factorial moment. The known crossing central limit theorem for \(X_{n-k}\), together with

\[
 \frac{\mu_{n-k}-\mu_n}{\sigma_n}\to0,
 \qquad \frac{\sigma_{n-k}}{\sigma_n}\to1,
\]

shows that its right-hand expectation tends to \(e^{-t^2/2}\). Hence

\[
 \lim_{n\to\infty}\mathbb E[e^{itW_n}u^{S_n}]
 =\sum_{k=0}^{\infty}\frac{(u-1)^k}{k!}e^{-t^2/2}
 =e^{-t^2/2+u-1},
\]

by dominated convergence for the uniformly bounded factorial series. Joint characteristic-function uniqueness, taking \(u=e^{is}\), proves convergence to the product law. This proves (4).

## Verification

The independent enumeration script `verify.py` enumerates every perfect matching for \(2\le n\le7\), computes crossings and simple chords directly from endpoint patterns, and checks every coefficient of (1) for all \(0\le k\le n\) by exact rational arithmetic. It separately verifies all exact means, variances, covariance, and the squared correlation identity. Run from this directory with `python3 verify.py`; the recorded output was `VERIFY_OK 494 exact assertions; n=2..7 complete matchings`. This finite enumeration is a consistency check, not an infinite proof. The proof above supplies the all-size deletion bijection; the Gaussian crossing limit used in step 4 is a published theorem.

## Relationship to prior work

Flajolet and Noy (2000), Theorem 3, determine the univariate crossing moments and normal limit, with earlier crossing enumeration due to Touchard and Riordan. Acan (2017), Section 3 and Theorem 4.2, establishes Poisson laws for numbers of short chords of fixed lengths, jointly across those lengths. Young (2020) enumerates short chords in linear \(k\)-chord diagrams, a different statistic/model combination. Paguyo (first posted 2021-04-02), Theorems 1.1 and 1.2, gives quantitative **separate** normal and Poisson approximations for crossings and simple chords in the same circular model. The present joint deletion law connects the two statistics and yields their exact covariance, correlation, and independent joint limit; it does not claim the classical marginal results anew.

## Limitations

The theorem is specific to uniformly random chord matchings and simple (cyclically adjacent) chords. Other chord lengths need not be deletion-neutral for crossings. The joint limit is qualitative; no new optimal two-dimensional error rate is asserted. The proof of normality of the marginal crossing count invokes the previously established Flajolet–Noy theorem. Prior work beyond the inspected papers could contain an equivalent mixed-moment calculation; historical priority is not certified.

## References

1. Philippe Flajolet and Marc Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR-3914 (March 2000), Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (initial submission 2021-04-02), Theorems 1.1 and 1.2. https://arxiv.org/abs/2104.01134
3. Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph*, Discrete Mathematics (2017), Section 3 and Theorem 4.2. https://doi.org/10.1016/j.disc.2016.11.004
4. Donovan Young, *Linear k-Chord Diagrams*, Journal of Integer Sequences 23 (2020), Article 20.9.1, Sections 1–2. https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.pdf
