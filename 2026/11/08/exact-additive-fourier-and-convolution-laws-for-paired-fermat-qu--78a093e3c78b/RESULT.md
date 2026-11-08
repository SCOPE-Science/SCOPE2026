# Exact additive Fourier and convolution laws for paired Fermat quotients

## Finding

Let \(p\) be an odd prime and \(h_0,h_1\in\mathbb Z\) have distinct residues modulo \(p\). Write \(\mathbb F_p=\mathbb Z/p\mathbb Z\). For an integer \(u\) prime to \(p\), define its Fermat quotient \(q_p(u)=((u^{p-1}-1)/p)\bmod p\), and take each input \(n\) modulo \(p^2\) for which both \(n+h_0\) and \(n+h_1\) are units. Define the multiplicity function on \(\mathbb F_p^2\) by

\[
\mu(z)=\#\{n\bmod p^2:\ p\nmid(n+h_0)(n+h_1),\ (q_p(n+h_0),q_p(n+h_1))=z\}.
\]

Set \(R=p-2\), let \(\zeta_p=\exp(2\pi i/p)\), and use the unnormalized Fourier transform \(\widehat\mu(u,v)=\sum_{(x,y)\in\mathbb F_p^2}\mu(x,y)\zeta_p^{ux+vy}\). Then its **entire Fourier spectrum**, including the complex phase, is

\[
\widehat\mu(u,v)=\begin{cases}
pR,&(u,v)=(0,0),\\
0,&(u,v)\ne(0,0),\ uv(u+v)=0,\\
p\,\zeta_p^{u q_p(a+h_0)+v q_p(a+h_1)},&uv(u+v)\ne0,
\end{cases}
\]
where, in the third branch, \(a=-(uh_1+vh_0)/(u+v)\in\mathbb F_p\); any integer representative of \(a\) may be used **provided** the same lift choice is used to parametrize the corresponding line. To remove this representative-dependence from the phase, take the unique representative \(a\in\{0,\ldots,p-1\}\) in the displayed formula. There are precisely \(R(p-1)\) nonzero-frequency coefficients of absolute value \(p\); all remaining nonzero-frequency coefficients vanish.

For an integer \(m\ge1\), let \(r_m=\mu^{*m}\) be convolution on the additive group \(\mathbb F_p^2\), so \(r_m(z)\) counts ordered \(m\)-tuples of eligible inputs whose paired Fermat quotients sum to \(z\). For each \(a\in\mathbb F_p\setminus\{-h_0,-h_1\}\), define

\[
 c_a=(q_p(a+h_0),q_p(a+h_1)),\qquad
 v_a=(-(a+h_0)^{-1},-(a+h_1)^{-1}),\qquad
 L_a^{[m]}=m c_a+\mathbb F_p v_a.
\]

For every \(m\ge2\) and \(z\in\mathbb F_p^2\), the **complete pointwise distribution of all sums** is

\[
\boxed{r_m(z)=p^{m-2}(R^m-R)+p^{m-1}\sum_{a\notin\{-h_0,-h_1\}}\mathbf1_{L_a^{[m]}}(z).}
\]

Here \(L_a^{[m]}\) is an affine line with base point \(m c_a\) and fixed direction \(v_a\), even when \(p\mid m\). It is the \(m\)-fold Minkowski sum of the original affine line, **not** multiplication of all its points by \(m\).

The exact even moments (generalized additive energies) consequently are

\[
\boxed{E_m=\sum_{z\in\mathbb F_p^2}r_m(z)^2
=p^{2m-2}\left(R^{2m}+R(p-1)\right)\quad(m\ge1).}
\]

For every \(p\ge5\), the paired-quotient image is a proper subset of \(\mathbb F_p^2\) yet its twofold sumset is **all** of \(\mathbb F_p^2\). In fact the minimum number of ordered representations of any target as a sum of two paired-quotient vectors is **exactly** \(R(R-1)\). Thus its additive basis order is precisely two. For \(p=3\), the image is a single affine line, so no finite repeated sum of it covers the plane. Each of the three scalar functions \(q_p(n+h_0)\), \(q_p(n+h_1)\), and \(q_p(n+h_0)-q_p(n+h_1)\) takes every value of \(\mathbb F_p\) exactly \(R\) times on the eligible inputs modulo \(p^2\).

## Assumptions and scope

The prime \(p\) is odd; the shifts may be any integers with \(h_0\not\equiv h_1\pmod p\). The sample space excludes only the two forbidden residue classes modulo \(p\), and has size \(pR\). Fermat quotients are taken modulo \(p\), not ordinary integer quotients. Coordinates, Fourier frequencies, and sums belong to the additive group \(\mathbb F_p^2\). The result makes no assertion about shorter intervals of inputs, arbitrary higher-precision quotient vectors, or distribution in a varying-prime limit.

## Proof

**1. Lifts become affine lines.** For every unit \(w\) modulo \(p\) and every integer \(t\), the binomial theorem gives

\[
\begin{aligned}
q_p(w+pt)-q_p(w)
&\equiv (p-1)w^{p-2}t\\
&\equiv -t w^{-1}\pmod p.
\end{aligned}
\]

Fix the unique residue representative \(a\in\{0,\ldots,p-1\}\) outside the two forbidden classes. Every input \(n\) in this class modulo \(p^2\) is uniquely \(n=a+pt\), \(t\in\mathbb F_p\). The paired quotient vector is exactly \(c_a+t v_a\). Thus, writing \(L_a=c_a+\mathbb F_p v_a\),

\[
\mu(z)=\sum_{a\notin\{-h_0,-h_1\}}\mathbf1_{L_a}(z).
\]

The slopes of these \(R\) lines are \((a+h_0)/(a+h_1)\), and as \(a\) varies they are precisely the slopes in \(\mathbb F_p\setminus\{0,1\}\): the map is injective because \(h_0\not\equiv h_1\pmod p\), and its image has \(p-2\) elements. In particular every pair of distinct lines has independent directions and meets in one point.

**2. Fourier coefficient and its zeros.** The character sum over \(L_a\) is

\[
\sum_{t\in\mathbb F_p}\zeta_p^{u(c_{a,0}+tv_{a,0})+v(c_{a,1}+tv_{a,1})}
=\begin{cases}p\zeta_p^{u c_{a,0}+v c_{a,1}},&u v_{a,0}+v v_{a,1}=0,\\0,&\text{otherwise.}\end{cases}
\]

For \((u,v)\ne(0,0)\), the orthogonality equation is

\[
 u(a+h_1)+v(a+h_0)=0.
\]

If \(u=0\) or \(v=0\), its only possible solution is a forbidden residue. If \(u+v=0\) with both nonzero, it reduces to \(u(h_1-h_0)=0\), impossible. Otherwise, precisely one allowed \(a=-(u h_1+v h_0)/(u+v)\) solves it, giving the claimed phase and absolute value \(p\). For zero frequency, all \(R\) lines contribute \(p\). The three distinct zero-frequency lines contain \(3(p-1)\) nonzero points; the remaining \((p^2-1)-3(p-1)=R(p-1)\) frequencies have absolute value \(p\).

**3. Convolution.** Expand \(r_m\) by first choosing an ordered word of \(m\) base residues \(a_1,\ldots,a_m\) and then \(m\) lift parameters. There are \(R\) constant words; for a constant word \(a\), the resulting sum is \(m c_a+(t_1+\cdots+t_m)v_a\), which hits each point on \(L_a^{[m]}\) exactly \(p^{m-1}\) times. For each of the other \(R^m-R\) words, at least two directions differ, hence the linear map from \(\mathbb F_p^m\) into \(\mathbb F_p^2\) has rank two. Every target has exactly \(p^{m-2}\) lift tuples. Summing the two contributions gives the pointwise formula, for arbitrary \(m\ge2\) including multiples of \(p\).

**4. Energies.** By finite Fourier orthogonality/Parseval,

\[
 E_m=p^{-2}\sum_{u,v\in\mathbb F_p}|\widehat\mu(u,v)|^{2m}
 =p^{-2}\left((pR)^{2m}+R(p-1)p^{2m}\right),
\]

which simplifies to the claimed expression. This also holds at \(m=1\), where the line intersections give the independent check \(E_1=pR+R(R-1)\).

**5. Exact additive basis order and scalar marginals.** For \(p\ge5\), \(R\ge3\), and the constant part of \(r_2\) equals \(R^2-R>0\). Therefore every target has a two-sum representation, whereas a one-sum representation misses at least \(p^2-pR=2p\) targets. The union of \(R\) shifted affine lines \(L_a^{[2]}\) has at most \(pR<p^2\) points; at a point outside this union the representation count is exactly \(R^2-R\), proving sharpness. When \(p=3\), \(R=1\) and each sumset remains an affine line. Finally, the Fourier transform of any of the three scalar statistics comes from the three corresponding frequency lines \(v=0\), \(u=0\), or \(u+v=0\); all its nonzero Fourier coefficients vanish. Each marginal therefore has the constant fiber size \(R\), since the total sample size is \(pR\).

## Verification

A standalone standard-library checker `verify.py` reconstructs Fermat quotients directly using modular exponentiation; independently constructs the affine-line model; checks all one-, two-, and threefold convolution counts and energy identities; classifies frequency zeros; and numerically checks Fourier phases for the smallest primes. It prints:

```text
VERIFY_OK prime_cases=33 image_entries=2815 m=1,2,3 exact_convolutions=PASS all_nonzero_frequency_classes=PASS complex_Fourier_small_primes=PASS two_sum_full_support_and_sharp_min=PASS
```

Execute `python3 verify.py`. The exact tests use primes \(3,5,7,11,13,17,19\) and multiple distinct shift pairs, including negative representatives. The finite checker is corroboration, **not** an infinite proof; the unrestricted proof is the lift identity, line-direction bijection, character orthogonality, and rank argument above.

## Relationship to prior work

Ostafe and Shparlinski (arXiv:1001.1504, first posted January 10, 2010) develop the Fermat-quotient lift identity and study shorter-range pseudorandomness and joint distributions. The basic lift identity is known and is expressly **not** claimed as new here. Their investigated statements do not specify the complete full-period two-coordinate Fourier spectrum, the pointwise all-order convolution law, or the exact even energies. Shparlinski (arXiv:1104.3909) investigates single-coordinate value sets and exponential sums. Chen and Winterhof (arXiv:1402.1913) study scalar Waring numbers for polynomial quotients with arguments restricted to intervals of length at most \(p\), whereas the present setting is the ordered *joint pair* over a full period \(p^2\). Liu and Zhang (2019) study pseudorandom scalar subsets and related correlations, not this exact full-period paired convolution. A related higher-precision joint-quotient image-count statement has a different invariant and range; cardinality of its image is not an implication of the stated Fourier and convolution law. No assertion is made that exhaustive literature priority has been independently certified.

## Limitations

The theorem requires odd prime modulus, two distinct shifts, and the **complete** eligible period modulo \(p^2\). It does not give a comparable formula for truncated sample intervals, three or more quotient coordinates, or the higher-precision quotient modulo \(p^k\) for \(k>1\). No external mathematical audit has been performed. The originality assessment is literature-based and retains risk of an unlocated equivalent older statement, particularly one derived from line-incidence geometry or higher-precision joint images.

## References

- A. Ostafe and I. E. Shparlinski, *Pseudorandomness and Dynamics of Fermat Quotients*, arXiv:1001.1504 (first public version January 10, 2010); SIAM J. Discrete Math. 25 (2011), 50–71. https://arxiv.org/abs/1001.1504
- I. E. Shparlinski, *Fermat Quotients: Exponential Sums, Value Set and Primitive Roots*, arXiv:1104.3909 (2011). https://arxiv.org/abs/1104.3909
- Z. Chen and A. Winterhof, *Polynomial Quotients: Interpolation, Value Sets and Waring's Problem*, arXiv:1402.1913 (2014). https://arxiv.org/abs/1402.1913
- Liu and Zhang, *Pseudo-random subsets constructed by using Fermat quotients* (2019), DOI:10.5486/PMD.2019.8222.
