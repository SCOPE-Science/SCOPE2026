# Magnetic-field collapse and critical enhancement of single-spin stability on antiferromagnetic wheels

## Finding

For the classical antiferromagnetic Ising Hamiltonian on a wheel, the exact count of configurations stable against any single spin flip changes from Perrin-exponential to parity-dependent polynomial and then to a unique state as the positive uniform field is increased. At the first critical field, its exponential growth rate jumps *up* to the golden-ratio rate before disappearing just above the critical field.

Put \(a=h/J\), let \(P_0=3,P_1=0,P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\). Let \(L_0=2,L_1=1,L_n=L_{n-1}+L_{n-2}\) be the Lucas numbers, and let \(\varepsilon_n=1\) for even \(n\), and \(0\) otherwise. Define, with binomial coefficients outside their usual range taken as zero,
\[
C_n(k)=\sum_{r=1}^n\frac nr\binom r{k-r}\binom r{n-k-r},\qquad
Q_n=\sum_{k=0}^{\lfloor(n+1)/2\rfloor}C_n(k).
\]
The number \(B_n(a)\) of weak one-spin-flip minima for every integer \(n\ge5\) is exactly
\[
\begin{array}{c|c|c}
\text{field range} & n\text{ even} & n\text{ odd}\\ \hline
0<a<1 & 2P_n-2 &2P_n\\
a=1&Q_n+L_n-2&Q_n+L_n\\
1<a<2&3&n+1\\
2\le a<3&3+n(n-4)/4&n+1\\
a=3&3+n^2/4&1+n+n(n^2-1)/24\\
3<a<n&1&1\\
a=n&2&2\\
a>n&1&1
\end{array}
\]
Here the symbol \(n\) in a field-range endpoint means the numerical field ratio \(h/J=n\).

With \(\rho\) the unique real root of \(\rho^3=\rho+1\) greater than one and \(\phi=(1+\sqrt5)/2\), for each *fixed* field ratio \(a>0\),
\[
\lim_{n\to\infty}\frac1n\log B_n(a)
=\begin{cases}
\log\rho,&0<a<1,\\
\log\phi,&a=1,\\
0,&a>1.
\end{cases}
\]
The two positive entropy values are distinct: \(\log\rho\approx0.28120\) and \(\log\phi\approx0.48121\).

## Assumptions and scope

Let \(W_n=K_1\vee C_n\) have one center vertex \(v_0\) and a labeled rim \(v_1,\ldots,v_n\), with cyclic rim indices. At each vertex choose \(\sigma_v\in\{-1,+1\}\), and use uniform antiferromagnetic edge coupling \(J>0\) and uniform field \(h>0\):
\[
\mathcal H(\sigma)=J\sum_{\{u,v\}\in E(W_n)}\sigma_u\sigma_v-h\sum_{v\in V(W_n)}\sigma_v.
\]
A configuration is *weakly one-spin stable* if flipping any individual spin does not strictly decrease the energy, i.e. every flip energy change is nonnegative. At fields where a flip energy change is zero, this definition includes marginal configurations. It does not assert that marginal configurations are absorbing for a zero-temperature rule that accepts energy-neutral flips. At nonresonant values displayed in the open field intervals, every counted configuration is strictly stable.

## Proof

Write \(s=\sigma_{v_0}\), \(x_i=\sigma_{v_i}\), and \(M=\sum_{i=1}^n x_i\). Direct subtraction of the Hamiltonian before and after a flip gives
\[
\Delta_{v_0}\mathcal H=2Js(a-M),\qquad
\Delta_{v_i}\mathcal H=2Jx_i(a-s-x_{i-1}-x_{i+1}).
\]
Hence a positive hub needs \(M\le a\), a negative hub needs \(M\ge a\); a positive rim spin needs \(a\ge s+x_{i-1}+x_{i+1}\), and a negative rim spin needs \(a\le s+x_{i-1}+x_{i+1}\). These conditions are necessary and sufficient, with no approximation.

**Weak fields \(0<a<1\).** For \(s=+1\), every positive rim spin must have two negative neighbors, and every negative rim spin must have at least one positive neighbor. Thus the positive rim sites form a maximal independent set of \(C_n\): the cyclic word contains neither adjacent positive spins nor three consecutive negative spins. Its rim magnetization is nonpositive, so the hub condition is automatic. The number of such cyclic words is the Perrin number \(P_n\). For completeness this follows by tracing the three-state finite automaton with adjacency matrix
\[
A=\begin{pmatrix}0&1&0\\1&0&1\\1&0&0\end{pmatrix},
\qquad \det(\lambda I-A)=\lambda^3-\lambda-1.
\]
A cyclic word with isolated positives and negative runs of length one or two corresponds bijectively to a closed walk of length \(n\) in this automaton; thus \(P_n=\operatorname{tr}(A^n)\) for \(n\ge3\). For \(s=-1\), the spin-reversed rim words are allowed locally, but the hub requires \(M\ge a\), thereby discarding exactly the two alternating words when \(n\) is even. The first row of the table follows.

**Intermediate fields \(1<a<3\).** For \(s=-1\), every negative rim spin is unstable, while an entirely positive rim is stable and satisfies the negative hub condition because \(a<3<n\). Hence this hub orientation contributes exactly one configuration. For \(s=+1\), negative rim spins must be isolated and positive runs have length at most two, so the rim magnetization is a nonnegative integer with the parity of \(n\). If \(1<a<2\), its permitted values are \(0\) for even \(n\) and \(1\) for odd \(n\); for \(2\le a<3\), value \(2\) is additionally permitted in the even case. There are exactly two alternating words with magnetization \(0\), exactly \(n\) words with magnetization \(1\) when \(n\) is odd, and exactly \(n(n-4)/4\) words with magnetization \(2\) when \(n\) is even: in the last case there are \((n-2)/2\) isolated negative sites and exactly two of the positive runs have length two. The corresponding count of cyclic labeled words is \(n/k\binom{k}{2}=n(n-4)/4\), where \(k=(n-2)/2\). This gives both intermediate rows, including equality at \(a=2\).

**The field \(a=1\).** For \(s=-1\), the negative rim sites are an arbitrary independent set of \(C_n\), subject to \(M\ge1\). All independent sets number \(L_n\); exactly the two alternating maximum independent sets for even \(n\) have \(M=0\), and are excluded. For \(s=+1\), local stability is precisely the absence of three consecutive spins of either sign; the hub condition is \(M\le1\). To count such a cyclic word with \(k\) positive sites, choose \(r\) positive runs and \(r\) negative runs, all of length one or two. Choose \(k-r\) of the positive runs and \(n-k-r\) of the negative runs to have length two. Among the \(n\) labeled choices of a starting positive-run site, each cyclic word is counted \(r\) times. The resulting count is \(C_n(k)\), and summing the allowed \(k\) yields \(Q_n\).

**The field \(a=3\).** With positive hub, negative rim spins must be isolated, positive rim spins have no local restriction, and the hub requires \(M\le3\). On a cycle of \(n\) sites, the number of independent sets of size \(k\) is \(n/(n-k)\binom{n-k}{k}\) for \(0\le k\le\lfloor n/2\rfloor\), including the empty case. Only \(M=0,2\) (even \(n\)) or \(M=1,3\) (odd \(n\)) are eligible. Their counts, respectively, are \(2,n^2/4\) and \(n,n(n^2-1)/24\). The negative-hub case contributes one entirely positive rim. This establishes the \(a=3\) row.

**Fields above three.** Both hub orientations require an entirely positive rim, since no negative rim spin can satisfy its stability inequality. The positive hub is stable exactly for \(a\ge n\), and the negative hub exactly for \(a\le n\). This proves the remaining rows, including the tie at \(a=n\).

**Entropy.** The Perrin recurrence has one positive dominant root \(\rho>1\) of \(z^3-z-1=0\), with the two other roots of modulus strictly less than one, hence \(P_n=\rho^n+o(\rho^n)\). At \(a=1\), the negative-hub contribution is \(L_n-2\varepsilon_n\sim\phi^n\), giving a lower exponential bound. The positive-hub contribution is bounded by all cyclic two-symbol words with no triple repeat. Such words are traced by the four-state pair automaton, whose characteristic polynomial is \((z^2-z-1)(z^2+z+1)\), and so their count is \(O(\phi^n)\). Therefore the critical entropy is exactly \(\log\phi\). For every fixed \(a>1\), the table gives at most a polynomial number of stable configurations in \(n\), and at least one; its entropy is zero. This proves the stated entropy law.

## Verification

The standalone `checker.py` enumerates every labeled spin assignment for wheel rims \(5\le n\le14\), calculates the exact local flip inequalities, independently constructs the Perrin/Lucas and cyclic-run formulas, and compares the totals at representative open-field values and at all nontrivial boundary values \(a=1,2,3,n\). The checker passed 195 exact checks: 90 direct spin-enumeration comparisons across field regimes and 105 independent run-composition coefficient comparisons. The proof above, not the finite enumeration, establishes the theorem for all \(n\ge5\). Run with `python checker.py` from the extracted package directory; it uses only the Python standard library.

## Relationship to prior work

One-spin-flip-stable states and their complexity are classical objects of spin-glass statistical mechanics; see Waclaw and Burda (2008) and De Smedt, Godrèche and Luck (2002). The equality \(P_n=\#\{\text{maximal independent sets of }C_n\}\) is **previously known** and is explicitly credited to Bisdorff and Marichal (2007/2008), with their earlier historical attribution. The new claim is not that Perrin enumeration, nor a generic transfer matrix, but the all-field wheel-specific coupling of rim constraints to the hub, its exact parity-dependent field counts, and the critical enhancement/collapse of the one-spin-stability entropy. Baek, Ha and Jeong (2011) study zero-temperature dynamics on random networks, with a different graph and no corresponding field-resolved wheel count. A relevant later random-regular-graph disassortative-partition study treats different graph families and general thresholds, not this exact finite wheel ensemble. No reviewed primary source directly asserts the combined wheel field-response statement; this is a best-knowledge literature comparison, not a guarantee of historical priority.

## Limitations

This is a mathematical classification of weak local energy minima, not a claim about attraction basins, the probability of reaching a minimum from random initialization, or positive-temperature metastable lifetimes. At \(a=1,2,3,n\), some counted states admit neutral flips and need not be absorbing under a tie-accepting Glauber rule. The entropy result holds for fixed \(a\) as \(n\) grows; it does not assert uniformity when \(h/J\) scales with \(n\). Equivalent results in unindexed literature remain possible.

## References

1. B. Waclaw and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224v1 (first public 2008-01-08), https://arxiv.org/abs/0801.1224 .
2. G. De Smedt, C. Godrèche and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465v1 (first public 2002-02-26), https://arxiv.org/abs/cond-mat/0202465 .
3. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647 (first public 2007-01-23), https://arxiv.org/abs/math/0701647 ; Journal of Integer Sequences 11 (2008), Article 08.5.7.
4. Y. Baek, M. Ha and H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927 (first public 2011-12-27), https://arxiv.org/abs/1112.5927 .
