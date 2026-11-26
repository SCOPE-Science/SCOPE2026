# A universal \(e^{-1}\) derangement law for square-zero Yang–Baxter solutions

## Finding

**Theorem.** Fix a prime \(p\) and integers \(r\geq1\), \(n\geq2r\). Let \(V=\mathbb F_p^n\), and let \(a:V\to V\) be linear with \(a^2=0\) and \(\operatorname{rank}a=r\). On \(V\times V\) define the nondegenerate set-theoretic Yang–Baxter map
\[
R_a(x,y)=(y+a(x),\,x+a(y)).
\]
Write \(G_{n,a}=\operatorname{Aut}(V,R_a)\), where automorphisms are *all bijections* preserving both coordinate operations, not just linear maps. Put \(W=a(V)\), \(Q=V/W\), and \(s=p^{n-2r}\). Then:

1. There is a (choice-dependent) group isomorphism
\[
G_{n,a}\cong W^{Q}\rtimes\bigl(S_s^{\,W}\rtimes\operatorname{GL}_r(\mathbb F_p)\bigr),
\]
where the general linear group permutes the \(p^r\) copies of \(S_s\) by its natural action on \(W\) and acts on \(W^Q\) through the induced permutation of \(Q\) and its linear action on \(W\). Consequently
\[
|G_{n,a}|=p^{r p^{n-r}}(s!)^{p^r}\prod_{j=0}^{r-1}(p^r-p^j).
\]
2. Every \(g\in G_{n,a}\) induces a unique \(\phi_g\in\operatorname{GL}(W)\) satisfying \(a\circ g=\phi_g\circ a\). Choose \(g\) uniformly from \(G_{n,a}\), and write \(F(g)=|\{x\in V:g(x)=x\}|\). For any prescribed \(\phi_g=\phi\), let \(d=\dim_{\mathbb F_p}\ker(I-\phi)\) and \(u=p^d\). The exact probability-generating function is
\[
\mathbb E\bigl[t^{F(g)/u}\mid\phi_g=\phi\bigr]
=\left(\sum_{j=0}^{s}\frac{(t-1)^j}{u^j j!}\right)^{u}.
\]
In particular, every \(F(g)\) is a multiple of \(u\) once \(\phi_g\) is fixed.
3. As \(n\to\infty\) with \(p,r\) fixed (and \(a\) of rank \(r\) varying with \(n\)), conditionally on each \(\phi\),
\[
\mathcal L(F(g)/p^d\mid\phi_g=\phi)
\longrightarrow\operatorname{Poisson}(1)
\]
in total variation. Unconditionally, \(F(g)\) converges in total variation to the mixture \(p^{\dim\ker(I-\Phi)}P\), where \(\Phi\) is uniform in \(\operatorname{GL}_r(\mathbb F_p)\) and \(P\) is an independent \(\operatorname{Poisson}(1)\) variable. **The universal derangement limit is**
\[
\boxed{\lim_{n\to\infty}\Pr_{g\in G_{n,a}}(F(g)=0)=e^{-1},}
\]
independent of \(p\) and \(r\). For every admissible \(p,r,n\), the exact probability differs from \(e^{-1}\) by at most \(1/(s+1)!\); this bound is uniform in \(p,r\).

The full automorphism group has exactly two orbits on \(V\), namely \(\ker(a)\) and its complement. Thus the universal derangement limit does not come from transitivity of the automorphism action.

## Assumptions and scope

Everything is over the *prime* field \(\mathbb F_p\). The rank condition forces \(n\ge2r\), and every square-zero linear map of rank \(r\) exists in these dimensions. The Yang–Baxter solution is involutive for \(p=2\) and generally noninvolutive for odd \(p\). The asymptotic concerns **fixed** \(p\) and **fixed** positive \(r\), with \(n\) increasing; it does not assert uniformity when those parameters grow. The source example is attributed to the published construction in Jedlička–Pilitowska (2023), which itself credits an earlier 2000 lemma for the solution property. The theorem concerns permutations of the underlying set that preserve the solution, not automorphisms required to be additive or linear.

## Proof

**1. The Yang–Baxter structure.** Since \(a^2=0\), the inverse of \(R_a\) is \((u,v)\mapsto(v-a(u),u-a(v))\). Its two one-variable translations are translations of \(V\), hence bijective. Applying \(R_a\) in braid order to any triple \((x,y,z)\), in either order, yields
\[
(z+a(x)+a(y),\,y+a(x)+a(z),\,x+a(y)+a(z)).
\]
Thus the braid relation holds. This also independently verifies the specific 2-reductive construction described in Example 3.2 of Jedlička–Pilitowska.

**2. Recovering the common linear action.** The preservation law for a bijection \(f:V\to V\) is exactly
\[
f(y+a(x))=f(y)+a(f(x))\qquad(x,y\in V).
\]
Both coordinate preservation laws are this same identity after exchanging dummy variables. If \(a(x)=a(x')\), cancellation gives \(a(f(x))=a(f(x'))\); hence there is a well-defined map \(\phi:W\to W\) with \(\phi(a(x))=a(f(x))\). The identity becomes \(f(y+w)=f(y)+\phi(w)\). Applying it twice establishes additivity of \(\phi\). If \(\phi(w)=0\), injectivity of \(f\) gives \(w=0\). Thus \(\phi\) is an automorphism of the finite elementary abelian group \(W\), equivalently \(\phi\in\operatorname{GL}_r(\mathbb F_p)\). Necessarily \(a f=\phi a\), and conversely these two identities suffice for solution preservation.

**3. Every permutation and its count.** Let \(\beta:Q\to W\) be the surjection induced by \(a\), so \(\ker\beta=(\ker a)/W\) has cardinality \(s\). Choose a set section \(h:Q\to V\) of the quotient map. Every \(v\in V\) is written uniquely as \(h(c)+w\) with \(c\in Q,w\in W\). The preceding identities say that all automorphisms, and only those automorphisms, have the form
\[
f(h(c)+w)=h(\tau(c))+b(c)+\phi(w),
\]
where \(\phi\in\operatorname{GL}(W)\), \(\tau\in\operatorname{Sym}(Q)\) satisfies \(\beta\tau=\phi\beta\), and \(b:Q\to W\) is arbitrary. For each \(\phi\), the permutation \(\tau\) bijects the \(p^r\) fibers of \(\beta\), each of cardinality \(s\), in precisely \((s!)^{p^r}\) ways. There are \(|W|^{|Q|}=p^{r p^{n-r}}\) possible maps \(b\). Choosing a vector-space splitting \(Q\simeq W\oplus\ker\beta\) identifies the \((\tau,\phi)\)-group with \(S_s^W\rtimes\operatorname{GL}(W)\). The displayed normal form supplies a splitting of the full extension. This proves the structure and order formulas, including that the map \(f\mapsto\phi\) is uniformly distributed over \(\operatorname{GL}(W)\) when \(f\) is uniform.

**4. Exact fixed-point generating function.** Fix \(\phi\), with \(d=\dim\ker(I-\phi)\), and put \(u=p^d\). A fixed vector must belong to a \(W\)-coset \(c\in Q\) fixed by \(\tau\); then \(\beta(c)\) must be a fixed vector of \(\phi\). There are exactly \(u\) such \(\beta\)-fibers, and conditionally on \(\phi\) the permutations \(\tau\) on those fibers are independent uniform permutations of \(s\) objects. When \(c\) is fixed by \(\tau\), the vector \(h(c)+w\) is fixed precisely if \((I-\phi)w=b(c)\). Since \(b(c)\) is uniform in \(W\), this equation has \(u\) solutions with probability \(1/u\), otherwise none; the tests are independent over fixed cosets. For a uniform \(\sigma\in S_s\), let \(C(\sigma)\) be its number of fixed points. By counting fixed ordered subsets,
\[
\mathbb E[(1+z)^{C(\sigma)}]=\sum_{j=0}^{s}\frac{z^j}{j!}.
\]
Thinning each fixed coset with probability \(1/u\), then multiplying independent contributions from the \(u\) fixed \(\beta\)-fibers, proves the asserted exact generating function.

**5. Limit and orbit assertion.** For any fixed \(u\), the truncated exponential converges uniformly on compact complex sets, so
\[
\left(\sum_{j=0}^{s}\frac{(t-1)^j}{u^j j!}\right)^u\to e^{t-1}.
\]
The left-hand side is a probability-generating polynomial with mean one. Coefficient convergence together with the uniform mean bound proves total-variation convergence to \(\operatorname{Poisson}(1)\) (truncate at a large integer and control the tails by Markov's inequality). Since \(\operatorname{GL}_r(\mathbb F_p)\) is fixed and finite, averaging yields the asserted mixture in total variation. Substituting \(t=0\) gives the limit \(e^{-1}\). In fact, the alternating-series remainder and the inequality \(|x^u-y^u|\le u|x-y|\) for \(0\le x,y\le1\) give the *uniform finite-size bound*
\[
\left|\Pr(F(g)=0)-e^{-1}\right|\le\frac{1}{(s+1)!},\qquad s=p^{n-2r}.
\]
The bound holds for every \(p,r,n\) in the stated scope, even when \(p\) or \(r\) vary. Finally, \(a f=\phi a\) shows that \(\ker a\) is invariant. Transitivity within any \(a\)-fiber follows from arbitrary fiber permutations and \(W\)-translations in the normal form; transitivity across nonzero \(a\)-values follows from transitivity of \(\operatorname{GL}(W)\) on \(W\setminus\{0\}\). Hence there are exactly two orbits.

## Verification

The accompanying `verification.py` directly enumerates **every** bijection of the underlying set for \((p,n,r)=(2,2,1),(2,3,1),(3,2,1)\), checks both solution-coordinate laws for each, and compares the exact group order and the full fixed-point histogram against the coefficient formulas. It produces respectively \(4\), \(64\), and \(54\) automorphisms, with fixed-point histograms
\[
\begin{array}{c|l}
(2,2,1)&\{0:1,2:2,4:1\}\\
(2,3,1)&\{0:25,2:20,4:14,6:4,8:1\}\\
(3,2,1)&\{0:8,1:27,3:12,6:6,9:1\}.
\end{array}
\]
The checker uses only the Python standard library and finite integer/rational arithmetic. These finite tests corroborate the formulas; the proof above, not finite enumeration, establishes the infinite family and its limit.

## Relationship to prior work

Jedlička and Pilitowska, *Skew left braces and 2-reductive solutions of the Yang-Baxter equation* (arXiv:2303.15154, first submitted 2023-03-27), Example 3.2 already constructs this solution from \(a^2=0\) and cites an earlier 2000 source for the Yang–Baxter property. Its Theorems 3.9 and 3.11 classify all 2-reductive solutions and their isomorphisms by orbitwise abelian-group data. **Those foundational results are not claimed as new here.** The explicit normal form above is a specialization used to derive a *newly assessed* fixed-point distribution, conditional law and derangement asymptotic; the latter are not stated in the inspected primary sections. Jedlička, Pilitowska and Zamojska-Dzienio (arXiv:1901.01471) develop involutive level-two constructions and classify their structure, but the inspected material does not give this conditional fixed-point law. Indexed mathematical records on binary transposition cycle sets and exponent-four core quandles concern different operations and do not imply the current statement without a separate identification, which was not found. A possible unindexed specialization of the general isomorphism theorem or a known permutation-wreath limit remains a historical-priority risk.

## Limitations

No independent mathematical audit has been performed. The stated priority assessment is relative to identified and inspected sources, not a proof that no equivalent result exists. The 2023 general isomorphism theorem is strong prior art, and the group-formula portion is a structured specialization; the nontrivial assessed result is the exact conditional fixed-point law and its universal asymptotic. The distributional Poisson-mixture limit is stated only for fixed \(p,r\); the explicitly displayed *zero-fixed-point error bound* is valid even for growing \(p,r\). General finite abelian groups, finite nonprime fields interpreted with their full additive structure, and non-square-zero endomorphisms are outside the proved scope.

## References

1. P. Jedlička and A. Pilitowska, *Skew left braces and 2-reductive solutions of the Yang-Baxter equation*, first submitted 2023-03-27, arXiv:2303.15154, https://arxiv.org/abs/2303.15154 (especially Example 3.2, Theorems 3.9 and 3.11).
2. P. Jedlička, A. Pilitowska and A. Zamojska-Dzienio, *The construction of multipermutation solutions of the Yang-Baxter equation of level 2*, arXiv:1901.01471 (first submitted 2019-01-05), https://arxiv.org/abs/1901.01471.
