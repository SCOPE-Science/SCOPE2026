# Algebraic thinness and forced fold collisions in finite logistic iterated-function invariant sets

## Finding
For distinct real parameters \(0<\alpha<\beta\le4\), let \(f_t:[0,1]\to[0,1]\) be the logistic map \(f_t(u)=tu(1-u)\). A **finite invariant set** here means a nonempty finite set \(S\subseteq[0,1]\) satisfying the *equality*
\[
S=f_\alpha(S)\cup f_\beta(S).
\]
Then:

1. Every such \(S\ne\{0\}\) contains **two distinct complementary points**: some \(u,v\in S\) satisfy \(u\ne v\) and \(u+v=1\).
2. For every integer \(N\ge2\), there is an explicitly constructible **nonzero polynomial** \(P_N\in\mathbb Z[\alpha,\beta]\) such that any pair admitting an \(S\ne\{0\}\) with \(|S|\le N\) satisfies \(P_N(\alpha,\beta)=0\). For each fixed \(0<\alpha\le4\), the number of \(\beta\in(\alpha,4]\) admitting such a set is at most
\[
B_N^2,\qquad B_N=\sum_{n=1}^N n(2^n-1)=(N-1)2^{N+1}+2-\frac{N(N+1)}2.
\]
3. Consequently, the set of distinct parameter pairs permitting **any** nontrivial finite invariant set is contained in a countable union of proper real algebraic subsets of the parameter plane. It has two-dimensional Lebesgue measure zero and is meagre; for every fixed \(\alpha\), its section in \(\beta\) is countable. Thus, on a residual full-measure set of distinct parameter pairs, the only nonempty finite invariant set is \(\{0\}\).

These obstructions are nonvacuous, not universal nonexistence: every \(2<\beta\le4\) with \(\alpha=\beta/(\beta-1)\) has the invariant pair \(\{1/\beta,1-1/\beta\}\).

## Assumptions and scope
Both generators must have the **same quadratic shape** and positive distinct amplitudes; \(0<\alpha<\beta\le4\) ensures both act on the entire unit interval. Finite invariance means equality of sets, not merely forward inclusion. The theorem does not require ergodicity, irreducibility of the induced finite-state chain, any particular generator-selection probability, or attraction. For a merely forward-invariant finite \(S\ne\{0\}\), the complementary-pair conclusion still holds, but the generic nonexistence conclusion must exempt the universally forward-invariant transient set \(\{0,1\}\).

For \(0\le m<n\), write \(F_t^{[0]}(z)=z\), \(F_t^{[k+1]}(z)=tF_t^{[k]}(z)(1-F_t^{[k]}(z))\), and set
\[
Q_{m,n}(t,z)=\frac{F_t^{[n]}(z)-F_t^{[m]}(z)}{z(1-z)^{\mathbf{1}_{\{m\ge1\}}}}\in\mathbb Z[t,z].
\]
The numerator is divisible by the displayed denominator, so this is a polynomial identity, including at \(z=0,1\). For \(N\ge2\), an explicit algebraic obstruction is
\[
P_N(\alpha,\beta)=
\prod_{0\le m<n\le N}\ \prod_{0\le p<q\le N}
\operatorname{Res}_z\!\bigl(Q_{m,n}(\alpha,z),Q_{p,q}(\beta,z)\bigr).
\]
This polynomial is a *necessary test*, not a sufficient classification: its zero set generally contains spurious parameters.

## Proof
**Fold-collision necessity.** If \(f_\alpha\) is injective on finite \(S\) and \(f_\alpha(S)\subseteq S\), it permutes \(S\). Since \(f_\beta=(\beta/\alpha)f_\alpha\), the restrictions of both generators to \(S\) have precisely the same collision pairs, so \(f_\beta\) is also injective and permutes \(S\). Hence \(S=(\beta/\alpha)S\), impossible for a finite set with positive maximum and \(\beta>\alpha\). Thus there are distinct \(u,v\in S\) with \(f_\alpha(u)=f_\alpha(v)\). Factoring
\[
 f_\alpha(u)-f_\alpha(v)=\alpha(u-v)(1-u-v)
\]
forces \(u+v=1\). This argument requires only forward invariance.

**An interior point is unavoidable under equality.** Any \(S\subseteq\{0,1\}\) satisfies \(f_\alpha(S)\cup f_\beta(S)\subseteq\{0\}\). Therefore, if \(S\) is invariant in the equality sense and \(S\ne\{0\}\), it contains \(z\in(0,1)\).

**Finite-orbit polynomial constraints.** If \(|S|\le N\), the \(N+1\) points \(z,f_\alpha(z),\ldots,f_\alpha^{\circ N}(z)\) belong to \(S\), so some \(0\le m<n\le N\) satisfy \(F_\alpha^{[m]}(z)=F_\alpha^{[n]}(z)\). Likewise, a pair \(0\le p<q\le N\) exists for \(\beta\). Because \(z\in(0,1)\), both denominator factors in the definition of \(Q\) are nonzero at \(z\). Therefore \(Q_{m,n}(\alpha,z)=Q_{p,q}(\beta,z)=0\), making their resultant vanish and proving \(P_N(\alpha,\beta)=0\).

**Every resultant factor is nonzero.** For \(t>0\), \(F_t^{[k]}\) has degree \(2^k\) in \(z\); hence \(Q_{m,n}(t,z)\) is not identically zero. At the fixed parameter \(t=2\), the endpoint derivatives satisfy \((F_2^{[k]})'(0)=2^k\), \((F_2^{[k]})'(1)=-2^k\) for \(k\ge1\), and \(F_2^{[k]}(1)=0\). Consequently, for every \(m<n\), \(Q_{m,n}(2,0)\ne0\) and \(Q_{m,n}(2,1)\ne0\); its finitely many complex roots avoid \(0,1\). For any such root \(z\), the polynomial \(Q_{p,q}(\beta,z)\) is nonzero in \(\beta\), because its highest \(\beta\)-degree is \(2^q-1\) with coefficient nonzero when \(z\notin\{0,1\}\). Excluding finitely many parameter values \(\beta\) then removes every common root. Thus each resultant is a nonzero polynomial in \((\alpha,\beta)\), and their finite product \(P_N\) is nonzero.

**Uniform vertical-section bound.** For fixed \(\alpha>0\), each \(Q_{m,n}(\alpha,z)\) has at most \(2^n-1\) distinct roots \(z\in(0,1)\). Summed over \(0\le m<n\le N\), this gives at most \(B_N\) candidate interior points. For each candidate \(z\) and every \(0\le p<q\le N\), the polynomial \(Q_{p,q}(\beta,z)\) has degree \(2^q-1\) in \(\beta\), so there are at most \(B_N\) possible partner parameters. The union has at most \(B_N^2\) values, including any overcount from shared roots or extraneous candidates.

**Genericity and sharpness of scope.** The zero set of a nonzero bivariate polynomial has Lebesgue measure zero and is nowhere dense. Taking the countable union over \(N\ge2\) proves both genericity statements; the finite-section bound proves countability for each fixed \(\alpha\). Finally, for \(\alpha=\beta/(\beta-1)\), direct substitution shows \(f_\alpha(1/\beta)=f_\alpha(1-1/\beta)=1/\beta\) and \(f_\beta(1/\beta)=f_\beta(1-1/\beta)=1-1/\beta\), yielding the claimed invariant pair.

## Verification
The companion script `verify.py` runs exact symbolic checks through iteration order three, proves by symbolic resultant computations that all nine factors defining \(P_2\) are nonzero, checks the degree and endpoint identities, and verifies exact rational finite-invariant examples. It also verifies the closed form of \(B_N\) for small values. Run `python verify.py` with Python 3 and SymPy installed. These finite computations are diagnostic cross-checks; the arbitrary-\(N\) conclusion rests on the proof above, not on exhaustive enumeration.

Two boundary checks illustrate logical scope. The two-point example \((\alpha,\beta)=(3/2,3)\), \(S=\{1/3,2/3\}\), is a genuine nontrivial equality-invariant set. At \((\alpha,\beta)=(2,4)\), the three-point equality-invariant set \(\{0,1/2,1\}\) has the complementary pair \(\{0,1\}\) but **no distinct interior complementary pair**; this precludes strengthening the fold-collision conclusion to interior complements without further hypotheses.

## Relationship to prior work
Kato, Onozaki, Saiki and Sugita study this exact two-logistic-map IFS and give explicit two-, three- and five-point toss-and-catch constructions. They describe special parameter curves. Their April 2026 preprint's main text and supplementary discussion do not assert a size-uniform polynomial elimination obstruction, a bound on possible second-generator parameters for a fixed first generator, or the resulting full-measure residual exclusion over *all* finite invariant sets. The complementary-pair mechanism abstracts the preimage collisions visible in their examples. The result here does not re-label their explicit constructions as new.

Abbasi, Gharaei and Homburg previously analyzed synchronization and intermittency of logistic IFSs and an exceptional two-point invariant set. Their available abstract does not establish the all-cardinality parameter-locus theorem, but full-text comparison with that article remains incomplete. D'Aniello and Steele study IFS attractors for contracting maps, a substantially different class. Existing results on individual logistic-map preperiodic points are compatible with the argument; common preperiodicity for *two* generators is what yields the parameter restriction.

## Limitations
The polynomial equations are necessary rather than sufficient: their zero sets may include parameters having no nontrivial finite invariant set. The bound \(B_N^2\) is deliberately coarse and not asserted optimal. The theorem does not classify which points in an exceptional algebraic locus support an invariant set, prove their attracting character, or describe invariant Cantor sets, infinite attractors, stationary laws, or noise. It does not apply without modification to logistic-tent pairs, which are not scalar multiples of the same quadratic.

Historical priority is provisional pending examination of the inaccessible complete 2018 source and comparison with the complete later 2026 revision. The mathematical arguments are self-contained but independent verification has not been performed.

## References
- H. Kato, T. Onozaki, Y. Saiki and Y. Sugita, *Finite Invariant Sets with Bridging Points in Logistic IFS*, arXiv:2604.13124v1 (13 April 2026), https://arxiv.org/html/2604.13124v1 ; revised arXiv:2604.13124v2 (13 June 2026), https://arxiv.org/html/2604.13124 . Later journal DOI: 10.1063/5.0335032.
- N. Abbasi, M. Gharaei and A. J. Homburg, *Iterated function systems of logistic maps: synchronization and intermittency*, Nonlinearity **31** (2018), 3880–3913, DOI: 10.1088/1361-6544/aac637.
- E. D'Aniello and T. H. Steele, *Attractors for iterated function systems*, Journal of Fractal Geometry **3** (2016), 95–117, DOI: 10.4171/JFG/31.
