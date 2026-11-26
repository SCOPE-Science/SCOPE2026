# Square-zero matrices over length-two chain rings: rank strata and asymptotic flattening

## Finding

For every finite commutative chain ring of length two, the exact number of square-zero matrices in each **residue-rank stratum** is independent of the ring's mixed or equal characteristic. More unexpectedly, their residue ranks become asymptotically uniformly distributed over every admissible value, rather than concentrated near one rank.

Write \(k=R/\mathfrak m\cong\mathbb F_q\), with \(\mathfrak m=(\pi)\), \(\pi^2=0\), and let \(d\ge3\). The residue rank of \(A\in M_d(R)\) means \(a=\operatorname{rank}_k(\bar A)\); it is not the rank of an \(R\)-module homomorphism. Define

\[
P_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\qquad P_0(q)=1,\qquad P_\infty(q)=\prod_{i=1}^{\infty}(1-q^{-i})>0.
\]

For each integer \(0\le a\le\lfloor d/2\rfloor\),

\[
\boxed{\#\{A\in M_d(R):A^2=0,\ \operatorname{rank}_k(\bar A)=a\}
=\frac{|\mathrm{GL}_d(k)|}{P_a(q)P_{d-2a}(q)}.}
\]

No other residue ranks occur. In particular, this formula is identical for \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\) and the length-two Witt ring \(W_2(\mathbb F_q)\). Writing \(S_d(q)\) for the total count (with the same formula for \(d=0,1,2\)), its normalized generating function is

\[
\boxed{\sum_{d\ge0}\frac{S_d(q)}{|\mathrm{GL}_d(k)|}t^d
=\prod_{j=0}^{\infty}\frac1{(1-tq^{-j})(1-t^2q^{-j})}.}
\]

For fixed \(q\), if \(\mu_{d,q}\) is the distribution of \(\operatorname{rank}_k(\bar A)\) conditioned on \(A^2=0\), and \(U_d\) is uniform on \(\{0,1,\ldots,\lfloor d/2\rfloor\}\), then

\[
\boxed{\|\mu_{d,q}-U_d\|_{\mathrm{TV}}=O_q(d^{-1}),\qquad
S_d(q)=q^{d^2}\left(\frac{d}{2P_\infty(q)}+O_q(1)\right).}
\]

For example, when \(q=2\), the residue-rank counts are \((512,672)\) for \(d=3\), and \((65536,107520,53760)\) for \(d=4\). The latter total is \(226816\).

## Assumptions and scope

The ring is finite, commutative, local, and principal, with exactly two composition factors in its ideal chain. Hence \(|R|=q^2\), \(|\mathfrak m|=q\), and multiplication by a chosen \(\pi\in\mathfrak m\setminus\{0\}\) identifies \(k\) with \(\mathfrak m\) as additive \(k\)-vector spaces. The prime-power \(q\) may be even. No coefficient-field embedding into \(R\) is assumed. Matrix dimension \(d\) is arbitrary, and the novel higher-dimensional scope begins at \(d\ge3\); the expressions happen also to specialize correctly to smaller dimensions. The total-variation limit fixes \(q\) and lets \(d\) grow.

## Proof

**1. Classification of reductions.** If \(A^2=0\), then \(N=\bar A\in M_d(k)\) satisfies \(N^2=0\). Thus its Jordan type is \((2^a,1^b)\), where \(a=\operatorname{rank}_k N\), \(b=d-2a\), and \(0\le a\le\lfloor d/2\rfloor\). Conversely, each such residue type has a square-zero lift: conjugate a standard block diagonal matrix of \(a\) size-two nilpotent blocks and \(b\) zero blocks by a lift of a residue change-of-basis matrix. Surjectivity of \(\mathrm{GL}_d(R)\to\mathrm{GL}_d(k)\) follows because a determinant with nonzero residue is a unit.

**2. Every reduction has the same-size square-zero lift fiber within its type.** Fix a square-zero lift \(J\) of \(N\). Since \(\mathfrak m^2=0\), all its other lifts are uniquely \(J+\pi X\), with \(X\in M_d(k)\), after choosing representatives. Their squares vanish exactly when

\[
NX+XN=0.
\]

This is valid even in characteristic two. In a Jordan basis, a diagonal sign matrix \(D\) with opposite signs on the two vectors in every length-two block satisfies \(DND^{-1}=-N\). Thus \(X\mapsto XD\) is a vector-space bijection between solutions of \(NX+XN=0\) and elements commuting with \(N\). For Jordan type \((2^a,1^b)\), the commutant dimension is

\[
\sum_{s,t\in\{1,2\}}m_s m_t\min(s,t)
=2a^2+2ab+b^2=(d-a)^2+a^2.
\]

The displayed dimension follows directly by regarding \(k^d\) as a \(k[t]\)-module with \(a\) summands \(k[t]/(t^2)\) and \(b\) summands \(k[t]/(t)\): the \(k\)-dimension of the homomorphism space between length-\(s\) and length-\(t\) blocks is \(\min(s,t)\). Hence each square-zero reduction of residue rank \(a\) has exactly \(q^{(d-a)^2+a^2}\) square-zero lifts, independently of the ring structure.

**3. Count the reductions without an orbit table.** Choose the \(a\)-dimensional image \(I\) of \(N\) in \(\binom{d}{a}_q\) ways. Choose a \((d-a)\)-dimensional kernel containing \(I\) in \(\binom{d-a}{a}_q\) ways. Finally choose an isomorphism \(k^d/\ker N\to I\) in \(|\mathrm{GL}_a(k)|\) ways. Thus the number of square-zero reductions of rank \(a\) is

\[
\binom{d}{a}_q\binom{d-a}{a}_q|\mathrm{GL}_a(k)|
=q^{2a(d-a)}\frac{P_d(q)}{P_a(q)P_{d-2a}(q)}.
\]

The second equality follows by expanding both Gaussian binomial coefficients and using \(\lvert\mathrm{GL}_a(k)\rvert=q^{a^2}P_a(q)\). Multiplying by the lift fiber and using \(|\mathrm{GL}_j(k)|=q^{j^2}P_j(q)\) gives precisely

\[
\frac{|\mathrm{GL}_d(k)|}{P_a(q)P_{d-2a}(q)}.
\]

**4. Generating function.** Sum over all \(a,b\ge0\) with \(d=2a+b\). The Euler \(q\)-binomial identity

\[
\sum_{r\ge0}\frac{z^r}{P_r(q)}=\prod_{j\ge0}(1-zq^{-j})^{-1}
\]

holds as a formal power series in \(z\) at each fixed \(q\ge2\) (the factors converge coefficientwise). Apply it to \(z=t\) and \(z=t^2\).

**5. Uniform-rank limit.** Set \(h=\lfloor d/2\rfloor\), \(M=h+1\), and \(w_a=1/[P_a(q)P_{d-2a}(q)]\). Put \(w_\infty=P_\infty(q)^{-2}\). Since \(P_j(q)\searrow P_\infty(q)\),

\[
0\le w_\infty-w_a
\le \frac{w_\infty}{q-1}\bigl(q^{-a}+q^{-(d-2a)}\bigr).
\]

Indeed, divide by \(w_\infty\) and bound \(1-\prod(1-u_i)\) by \(\sum u_i\) for the two infinite tails. Summing over \(a=0,\ldots,h\) gives \(\sum_a|w_a-w_\infty|=O_q(1)\), because both resulting geometric sums are bounded independently of \(d\). Hence the normalized distribution proportional to \(w_a\) differs from uniform on its \(M\) support points in total variation by \(O_q(1/M)=O_q(1/d)\). Also

\[
S_d(q)=|\mathrm{GL}_d(k)|\sum_{a=0}^h w_a
=q^{d^2}P_d(q)\bigl(MP_\infty(q)^{-2}+O_q(1)\bigr)
=q^{d^2}\bigl(d/[2P_\infty(q)]+O_q(1)\bigr).
\]

No enumeration bound substitutes for this proof of the infinite-dimensional asymptotic statement.

## Verification

Run `python3 checker.py` using the Python standard library. The checker independently enumerates all matrices in \(M_3(\mathbb Z/4\mathbb Z)\) and \(M_3(\mathbb F_2[\varepsilon]/(\varepsilon^2))\), as well as \(2\times2\) cases over two residue field sizes. It classifies their reductions by finite-field rank and independently verifies the rank-specific formula. A second independent route enumerates all square-zero residue matrices over \(\mathbb F_2\) through dimension four and over \(\mathbb F_3\) through dimension three; for each reduction it row-reduces the \(d^2\)-variable anticommutator equation and checks the predicted dimension. These are finite checks, not the proof for all \(d\) or \(q\).

## Relationship to prior work

Danchev, García and Gómez Lozano [1], especially Lemma 2.4 and Theorem 2.6, prove square-zero **lifting** and potent-plus-square-zero **existence** over rings with square-zero radical, but do not supply the cardinality of each square-zero fiber, rank-stratified counts, or a limiting law. Cheong, Liang and Strand [2], Theorems 1.1 and 1.3 and Remark 1.2, count solutions to matrix polynomial equations over prime-power rings in the case of square-free/irreducible residue polynomial; their introduction expressly excludes the nonsquare-free polynomial \(P(t)=t^2\) treated here. Stasinski [3] studies representation theory and centralizers for two distinct length-two ring types, not square-zero matrix counts. Cheraghpour and Ghosseiri [4] give broader **unrefined nilpotent** counts, which do not determine the index-two rank distribution. Moreau and Yu [5] study geometric jet schemes of nilpotent orbit closures in characteristic zero; their results do not give this finite-field point count or a residue-rank law. These statements compare mathematical scope, not merely titles.

The smallest \(2\times2\) chain-ring square-zero case and classical finite-field Jordan reduction counts are prerequisites, not newly claimed. The new scope is a dimension-uniform rank-stratified law for \(d\ge3\), together with its ring-type invariance and its asymptotic uniformity.

## Limitations

The ring must be commutative, principal, local and of exactly length two. For higher nilpotency length, cross-terms beyond first order need not vanish; the proof does not extend unchanged. Only residue rank is classified; conjugacy over the ring, invariant factors over \(R\), and nilpotency indices greater than two are not enumerated. The rank-uniform limit fixes the residue-field order \(q\). An equivalent reformulation could exist in general quiver-representation, Hall-algebra, or jet-scheme point-count literature; the accessible sources inspected here do not resolve that bibliographic uncertainty. No claim of independent audit or exhaustive literature coverage is made.

## References

1. P. Danchev, E. García, M. Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460 (first submitted 2021-02-20), especially Lemma 2.4 and Theorem 2.6.
2. G. Cheong, Y. Liang, M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, arXiv:2209.03626 (first submitted 2022-09-08), especially Theorems 1.1, 1.3, Remark 1.2 and the nonsquare-free limitation in the Introduction.
3. A. Stasinski, *Representations of \(\mathrm{SL}_n\) over finite local rings of length two*, arXiv:1907.09878 (first submitted 2019-07-23), especially Sections 1 and 3.
4. M. Cheraghpour and A. Ghosseiri, *On the idempotents, nilpotents, units and zero-divisors of finite rings*, Linear and Multilinear Algebra, DOI:10.1080/03081087.2017.1418826.
5. A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427 (first submitted 2014-11-24).
