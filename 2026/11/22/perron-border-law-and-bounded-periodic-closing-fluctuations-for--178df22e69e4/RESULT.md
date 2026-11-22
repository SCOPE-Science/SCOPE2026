# Perron border law and bounded periodic-closing fluctuations for mixing Markov shifts

## Finding
Let \(B\) be a primitive zero-one adjacency matrix with Perron root \(\lambda>1\), and let a word \(W_n\) be uniform among all admissible words of length \(n\) in its one-sided edge-constrained symbol shift. Write \(\eta(W_n)\) for the least period of a periodic point in the cylinder determined by \(W_n\), and \(D_n=n-\eta(W_n)\).

**Theorem.** The integer random variables \(D_n\) converge in total variation, exponentially fast, to a variable \(D_B\) with exponentially decreasing positive tail and bounded negative part. All polynomial moments converge exponentially fast. Thus the canonical one-symbol generator has
\[
\mathbb E[\eta(W_n)]=n-\mathbb E[D_B]+o(1),\qquad
\operatorname{Var}(\eta(W_n))\longrightarrow \operatorname{Var}(D_B)<\infty,
\]
and, writing \(N_n\) for the number of admissible \(n\)-words,
\[
\lim_{n\to\infty}\frac{\mathbb E[\eta(W_n)]}{1+\log N_n}=\frac1{\log\lambda},\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(\eta(W_n))}{(1+\log N_n)^2}=0.
\]
For each fixed positive integer \(k\), the probability that \(W_n\) has a proper border of length \(k\) tends to
\[
\frac{\langle\ell,r\rangle}{(\sum_i\ell_i)(\sum_i r_i)}\lambda^{1-k},
\]
where \(\ell,r>0\) are left and right Perron eigenvectors of \(B\). The *expected total number of nonempty proper borders*, counting each length separately, therefore tends to
\[
\frac{\langle\ell,r\rangle}{(\sum_i\ell_i)(\sum_i r_i)}\frac{\lambda}{\lambda-1}.
\]

This law includes a persistent directed closing penalty. For the primitive three-symbol shift
\[
B=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix},
\]
let \(q_n\) be the fraction of length-\(n\) cylinders whose shortest periodic point has period \(n+1\). Then \(q_n\) converges exponentially, and its limit satisfies
\[
\boxed{\frac1{12}\le\lim_{n\to\infty}q_n\le\frac13.}
\]
This is an actual overhead, not just a nonsharp universal closing bound. In this example the expected number of proper borders tends to exactly \(2/3\).

## Assumptions and scope
Here \(B\) is finite, primitive, and has entries in \(\{0,1\}\), with \(\lambda>1\). A word \(w=w_0\ldots w_{n-1}\) is admissible when \(B_{w_i,w_{i+1}}=1\) for every \(0\le i<n-1\). The shift consists of all infinite admissible symbol sequences, with its ordinary left shift. The cylinder \([w]\) prescribes the first \(n\) symbols. Period means the *least positive* shift period, not the period of an arbitrary word extension. All probability statements use the uniform counting measure on the finite admissible length-\(n\) language, not Parry measure on the infinite shift. The claim concerns the canonical cylinder generator, **not** the supremum over all admissible open generating covers.

A border of length \(k\) is equality of the prefix and suffix of that length, where \(1\le k<n\). Let \(L(w)\) be the largest such length, or zero. Let \(d_B(j,i)\) be the smallest positive number of directed edges along an admissible path from \(j\) to \(i\). Primitivity makes it finite for every pair, including \(i=j\).

## Proof
**1. Exact closing rule.** If \(L(w)>0\), then \(w\) has least combinatorial period \(p=n-L(w)<n\). Its first \(p\) symbols repeat to produce exactly \(w\). This repetition is admissible, because the only new closing edge, from \(w_{p-1}\) to \(w_0=w_p\), occurs already inside \(w\). A periodic point of shorter period would give a longer border. If \(L(w)=0\), no periodic sequence of period below \(n\) contains \(w\). To close the fixed path from \(w_0\) to \(w_{n-1}\), the shortest possible additional path has \(d_B(w_{n-1},w_0)\) edges, so the first possible period is \(n-1+d_B(w_{n-1},w_0)\). Hence, exactly,
\[
\eta(w)=\begin{cases}n-L(w),&L(w)>0,\\n-1+d_B(w_{n-1},w_0),&L(w)=0.\end{cases}
\]
The finite directed diameter gives a uniform lower bound on \(D_n\).

**2. Exponential rarity of large borders.** Put \(N_j={\bf1}^{\!T}B^{j-1}{\bf1}\). The Perron–Frobenius theorem supplies positive constants \(c,C\), uniform in integer \(j\ge1\), with \(c\lambda^j\le N_j\le C\lambda^j\). A word with a border of length \(k\) has combinatorial period \(n-k\), and is determined uniquely by its first \(n-k\) symbols. Therefore, uniformly over \(1\le k<n\),
\[
\Pr(\text{border of length }k)\le (C/c)\lambda^{-k},\quad
\Pr(L(W_n)\ge k)\le\frac{C/c}{1-\lambda^{-1}}\lambda^{-k}.
\]
Consequently \(D_n\) has uniformly bounded moments of every fixed order; its negative part is bounded by the directed diameter.

**3. Exact fixed-border limit.** For fixed \(k\) and \(n\ge2k\), enumerate a common prefix/suffix \(u\) of length \(k\). The number of admissible length-\(n\) words having this border is
\[
\sum_{u\in\mathcal L_k}(B^{n-2k+1})_{u_{k-1},u_0}.
\]
Normalize by \(N_n\), use \(\lambda^{-m}B^m\to r\ell^{\!T}/\langle\ell,r\rangle\), and observe
\[
\sum_{u\in\mathcal L_k}\ell_{u_0}r_{u_{k-1}}=\ell^{\!T}B^{k-1}r=\lambda^{k-1}\langle\ell,r\rangle.
\]
This proves the border probability formula. The bound in Step 2 permits dominated convergence when summing over all border lengths, proving the expected-border formula.

**4. Complete limiting closing law.** For any finite admissible word \(u\) of length \(m\), define consistent probabilities for an infinite *forward* boundary string by
\[
\nu_+([u])=\frac{r_{u_{m-1}}}{\lambda^{m-1}\sum_i r_i},
\]
and an infinite *backward* boundary string, represented chronologically by its terminal \(m\) letters, by
\[
\nu_-([u])=\frac{\ell_{u_0}}{\lambda^{m-1}\sum_i\ell_i}.
\]
Take these two boundary strings independently. Their matching prefix/terminal blocks have an almost surely finite largest common length \(L_\infty\), by Step 3 and geometric summability. Define \(D_B=L_\infty\) when \(L_\infty>0\), and otherwise \(D_B=1-d_B(j,i)\), where \(i\) and \(j\) are the first forward and last backward symbols. Perron–Frobenius convergence makes the finite \(m\)-prefix and \(m\)-suffix of \(W_n\) converge exponentially to the independent boundary strings. Truncate border tests at \(m=\lfloor n/3\rfloor\). Their disagreement with the untruncated law has probability at most \(O_B(\lambda^{-m})\), while boundary-block mixing has error \(O_B(\theta^{n-2m})\) for some \(0<\theta<1\). Thus the distributions converge in total variation at \(O_B(\rho^n)\) for some \(0<\rho<1\). Geometric tail bounds and the finite negative bound yield exponential convergence of every fixed polynomial moment (after absorbing polynomial factors into a slightly larger \(\rho\)). The displayed mean and variance laws follow. Finally \(\log N_n=n\log\lambda+O_B(1)\), proving the canonical normalized limits.

**5. Directed closing penalty.** For the displayed three-symbol matrix, \(\lambda=2\), all Perron eigenvector entries are one, and all admissible length-\(n\) words are uniformly represented by a starting symbol and \(n-1\) independent stay/advance increments. The total increment modulo three asymptotically becomes uniform. The shortest directed return from final to first symbol has length two exactly when the total increment is congruent to one modulo three. Consequently the event of \(\eta=n+1\) is precisely this endpoint condition together with no nonempty border, and it has a limit by Step 4. Its limiting upper bound is \(1/3\). The sum of limiting probabilities of borders of lengths \(k\ge2\) is \(\sum_{k\ge2}1/(3\cdot2^{k-1})=1/3\). The length-two border event with equal initial and terminal symbols has limiting probability \(1/12\), but is disjoint from the endpoint condition requiring total increment one modulo three. By the union bound over the other border events, the fraction with that endpoint condition *and no border* is at least \(1/3-(1/3-1/12)=1/12\). The expected-border formula gives \((1/3)\cdot2/(2-1)=2/3\).

## Verification
Run `python3 check.py` from this package. It verifies the exact closing rule both by a direct period-by-period periodic-word enumeration (small lengths) and the border/directed-distance formula; it also reports finite-size moments and exact border frequencies for the golden-mean and three-symbol lazy directed cycle shifts. It performs finite tests only. The analytical Perron limits, total-variation convergence, and infinite-length penalty bound follow from the preceding proof rather than numerical extrapolation.

## Relationship to prior work
Pannipitiya (2026), Sections 2.4 and 4.2, defines periodic cylinder penetration, proves a general linear maximum bound for primitive shifts, and computes normalized mean/variance for the full shift. The present claim derives the uniform-primitive-shift limits, the exact weighted border constants, the limiting directed closure distribution, and an example with a positive limiting proportion requiring a period longer than the prescribed cylinder. Holub and Shallit (2015/2016) establish convergence and quantitative border laws for independent uniformly random unrestricted words; the present directed Markov-language law needs Perron-weighted ends and a closing path. No claim is made to the independent-uniform full-shift result.

## Limitations
The result requires a primitive finite zero-one presentation with Perron root strictly above one. It neither proves a statement for arbitrary nonmixing or countable-state shifts, nor evaluates the supremal all-generators invariants. The limiting distribution is defined constructively through independent boundary Markov chains; it is not claimed to have a universal closed elementary mass formula. This is a mathematical same-source extension, with residual priority risk from older unindexed symbolic-dynamics work and related Markov-border studies.

## References
1. D. N. Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1, first submitted 2026-11-10, especially §§2.4, 4.2. https://arxiv.org/abs/2611.13416
2. Š. Holub and J. Shallit, *Periods and borders of random words*, arXiv:1509.05240v1 (2015), STACS 2016. https://arxiv.org/html/1509.05240v1
3. D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press (1995), standard background on primitive shifts and Perron–Frobenius growth.
