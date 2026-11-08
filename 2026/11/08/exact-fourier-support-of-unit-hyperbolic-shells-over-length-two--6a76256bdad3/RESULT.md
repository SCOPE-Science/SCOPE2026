# Exact Fourier support of unit hyperbolic shells over length-two chain rings

## Finding

Let \(R\) be any finite commutative chain ring of length exactly two, with maximal ideal \(\mathfrak m=(\pi)\), \(\mathfrak m^2=0\), and residue field \(\mathbb F_q\), where \(q\ge2\) is any prime power. Fix \(n\ge2\) and a generating additive character \(\psi:R\to\mathbb C^\times\). Put
\[
H=\{(x,y)\in R^n\oplus R^n:\ x\cdot y=1\},\qquad
F(a,b)=\sum_{(x,y)\in H}\psi(a\cdot x+b\cdot y).
\]
The following characterization of all the Fourier zeros is exact:
\[
\boxed{F(a,b)\ne0\quad\Longleftrightarrow\quad
\bigl((a,b)\in\mathfrak m^{2n}\bigr)\quad\text{or}\quad
\left(\overline{a\cdot b}\in S_q\right),}
\]
where \(S_q=\mathbb F_q^\times\) when \(q\) is even, and \(S_q=(\mathbb F_q^\times)^2\) when \(q\) is odd. In the second case the residue dot product is nonzero, so the two alternatives are disjoint. The criterion is independent of the choice of generating character and holds for equal- and mixed-characteristic chain rings.

For additive convolution by \(\mathbf1_H\) on the complex functions on \(R^{2n}\), set \(s_q=q-1\) when \(q\) is even and \(s_q=(q-1)/2\) when \(q\) is odd. Its **exact rank** is
\[
\boxed{\operatorname{rank}_{\mathbb C}T_H
=q^{2n}\left(1+s_q(q^n-1)q^{n-1}\right).}
\]
Its nullity is \(q^{4n}-\operatorname{rank}_{\mathbb C}T_H\). In particular, along odd residue-field sizes the surviving Fourier fraction approaches one half, while along powers of two it approaches one. (For fixed \(q\), the fraction tends to \(s_q/q\) as \(n\to\infty\).)

An exact multiplier description supplements this support classification. Write \(c=a\cdot b\). For a frequency outside \(\mathfrak m^{2n}\),
\[
F(a,b)=q^{2n-2}\sum_{t\in R^\times}\psi(-t-c/t).
\]
If \(q\) is odd and \(\bar c\) is a nonzero square, choose either square root \(s\in R^\times\) with \(s^2=c\); then
\[
F(a,b)=q^{2n-1}\bigl(\psi(2s)+\psi(-2s)\bigr).
\]
If \(q\) is even and \(\bar c\ne0\), choose any unit \(u\) with \(\bar u^2=\bar c\); then
\[
F(a,b)=q^{2n-1}\psi(-u-c/u).
\]
Let \(\chi:\mathbb F_q\to\mathbb C^\times\) be the nontrivial additive character induced by \(\chi(\bar z)=\psi(\pi z)\). For a nonzero frequency in \(\mathfrak m^{2n}\), write \(a=\pi A\), \(b=\pi B\) and \(C=\overline{A\cdot B}\); then
\[
F(a,b)=q^{3n-2}\sum_{t\in\mathbb F_q^\times}\chi(-t-C/t)\ne0.
\]
Finally, \(F(0,0)=|H|=q^{4n-2}-q^{3n-2}\).

## Assumptions and scope

A chain ring here is finite, commutative, local, principal, and of ideal length two. Thus \(|R|=q^2\), \(|\mathfrak m|=q\), and \(\mathfrak m\) is the nonzero socle. The character \(\psi\) is generating: no nonzero ideal of \(R\) lies in its kernel. This makes its restriction to \(\mathfrak m\) nontrivial. The unnormalized Fourier transform uses the **plus** sign in the phase. Changing to the minus convention only reindexes frequencies and does not change the support or convolution rank. The dimension bound \(n\ge2\) is part of the theorem; the elementary one-pair hyperbola is not presented as a novel case. The Fourier rank is over \(\mathbb C\), not over \(R\) or \(\mathbb F_q\).

## Proof

**Character reduction.** Since a generating additive character has orthogonality on \(R\),
\[
F(a,b)=q^{-2}\sum_{t\in R}\psi(-t)
\sum_{x,y\in R^n}\psi(t\,x\cdot y+a\cdot x+b\cdot y).
\]
For \(t\in R^\times\), summing over \(y\) forces \(x=-t^{-1}b\); the inner sum is \(q^{2n}\psi(-c/t)\). Hence all unit terms total \(q^{2n-2}K_R(c)\), with \(K_R(c)=\sum_{t\in R^\times}\psi(-t-c/t)\). For \(0\ne t\in\mathfrak m\), the inner sum is zero unless \(a,b\in\mathfrak m^n\). Indeed, summation over the socle fibres of \(x,y\) forces both residue frequency vectors to vanish. When \(a=\pi A\), \(b=\pi B\), and \(t=\pi u\), the inner sum is \(q^{3n}\chi(-C/u)\). The \(t=0\) term survives only when \(a=b=0\), when it is \(q^{4n}\). In addition, \(K_R(0)=0\): it is the difference of the zero sums over \(R\) and \(\mathfrak m\). The displayed multiplier formulas (including the value at the origin) follow.

**Exact unit sum.** Partition \(R^\times\) into fibres of reduction to \(\mathbb F_q^\times\). For \(v\in\mathfrak m\), one has \(v^2=0\), so
\[
-(t+v)-c/(t+v)=-t-c/t+v(-1+c/t^2).
\]
The sum over \(v\) is zero unless \(\bar t^2=\bar c\), in which case it equals \(q\). Thus \(K_R(c)=0\) unless \(\bar c\) is a nonzero square in the residue field. In odd characteristic of the residue field, Hensel lifting is valid because \(2\) is a unit: a square unit \(c\) has exactly two roots \(s,-s\) in \(R\), one over each residue root. The two stationary phases are \(\psi(-2s)\) and \(\psi(2s)\), so their sum cannot vanish: a sum of two roots of unity of odd prime-power order cannot be zero. In residue characteristic two the squaring map on \(\mathbb F_q^\times\) is bijective. There is exactly one stationary residue, contributing one nonzero term \(q\psi(-u-c/u)\), independent of the chosen lift because the phase is constant on the fibre. This establishes the primitive-frequency criterion in every characteristic, including mixed characteristic four.

**Exact socle sum.** If \((a,b)\in\mathfrak m^{2n}\setminus\{0\}\), the only contribution is the finite-field Kloosterman sum \(\sum_{t\ne0}\chi(-t-C/t)\). This is a sum of exactly \(q-1\) roots of unity of order dividing the residue characteristic \(p\). Such a sum cannot vanish: writing it as an integer polynomial in a primitive \(p\)-th root, zero would force every residue-class coefficient to be equal (the cyclotomic polynomial has degree \(p-1\)), making its total term count a multiple of \(p\), while \(q-1\equiv-1\pmod p\). The origin coefficient is the positive size of the shell. Thus every socle frequency survives.

**Counting.** There are \(q^{2n}\) socle frequency pairs. A primitive frequency survives precisely when \(\bar a\ne0\) and \(\overline{a\cdot b}\in S_q\). For each nonzero \(\bar a\) (\(q^n-1\) choices), each permitted nonzero dot product has \(q^{n-1}\) choices of \(\bar b\). Every residue pair has \(q^{2n}\) ring lifts. This proves the rank formula. The ambient additive space has \(q^{4n}\) characters; Fourier diagonalization of convolution establishes the nullity. The asymptotics follow by dividing the rank expression by \(q^{4n}\).

## Verification

Run `python3 checks/verify.py` (Python 3 standard library; no optional dependencies). The checker performs exact cyclotomic coefficient-count tests over \(\mathbb Z/p^2\mathbb Z\) and \(\mathbb F_p[t]/(t^2)\), exhaustively at \((p,n)=(2,2),(3,2)\), plus additional boundary and higher-prime instances. Over \(\mathbb F_4[t]/(t^2)\), it verifies all frequencies at \(n=1\) and 400 deterministic frequencies at \(n=2\). Among the exact all-frequency evaluations, the resulting convolution ranks are 112 at \(q=2,n=2\) and 2025 at \(q=3,n=2\), both for cyclic and split rings. The checker compares cyclotomic zero conditions *exactly*, not with floating-point tolerances. These finite checks are corroborating experiments; the preceding argument proves the universal statement.

## Relationship to prior work

Iosevich and Koh [1,2] calculate finite-field quadratic-sphere Fourier transforms, including even-dimensional settings. Those results concern fields and do not supply the length-two chain-ring frequency stratification. Nica [3, Theorem 8.2] establishes vanishing of appropriate local-ring Kloosterman sums at nonunits and (in odd characteristic) nonsquare units. This accounts for a necessary part of the present condition but does **not** by itself classify nonvanishing at square units, supply the characteristic-two case, describe socle-frequency survival, or count convolution rank for the hyperbolic shell. Classical stationary phase and Salié evaluations for prime-power moduli are also antecedents. The present classification integrates both conductor strata over every length-two commutative chain ring and exhibits the odd/even Fourier-support density dichotomy. An equivalent specialization of broader existing Fourier analysis remains a genuine originality risk.

## Limitations

The theorem assumes exactly length-two chain rings and unit level \(1\), with \(n\ge2\); it does not address longer chain rings, arbitrary level sets, noncommutative rings, or the eigenvalue multiplicity distribution beyond the exact zero set. The square condition in odd characteristic is on the residue dot product, not the entire ring matrix or the Fourier frequency norm. An earlier general local-ring quadratic Fourier transform may imply the conclusion; the literature review is bounded. The numerical checks are finite and not a proof of the infinite family. No independent mathematical audit has been performed.

## References

1. A. Iosevich and D. Koh, *Extension Theorems for Spheres in the Finite Field Setting*, arXiv:0712.1627v1, first posted 2007-12-11, https://arxiv.org/abs/0712.1627.
2. A. Iosevich and D. Koh, *Extension Theorems for the Fourier Transform Associated with Nondegenerate Quadratic Surfaces in Vector Spaces over Finite Fields*, arXiv:0804.4505v1, first posted 2008-04-28, https://arxiv.org/abs/0804.4505.
3. B. Nica, *Kloosterman sums over finite Frobenius rings*, arXiv:1910.00165v1, first posted 2019-10-01, https://arxiv.org/abs/1910.00165.
4. R. Dąbrowski and B. Fisher, *A stationary phase formula for exponential sums over \(\mathbb Z/p^m\mathbb Z\) and applications to \(\operatorname{GL}(3)\)-Kloosterman sums*, Acta Arithmetica 80 (1997), https://eudml.org/doc/207231.
