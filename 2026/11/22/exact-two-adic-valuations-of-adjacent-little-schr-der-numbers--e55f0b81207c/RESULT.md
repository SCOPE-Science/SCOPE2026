# Exact two-adic valuations of adjacent little Schröder numbers

## Finding

Let \(s_n\) count the little Schröder numbers (polygon dissections), normalized by \(s_0=s_1=1\); thus \(s_2=3,s_3=11,s_4=45\). Write \(d_n=s_{n+1}-s_n\). For every integer \(n\ge1\),
\[
\nu_2(d_n)=\begin{cases}1,&n\text{ odd},\\\nu_2(n(n+2)),&n\text{ even}.\end{cases}
\]
In particular valuation two never occurs. For every \(k\ge3\),
\[
2^k\mid d_n\quad\Longleftrightarrow\quad n\equiv0\text{ or }-2\pmod{2^{k-1}}.
\]
The natural density of indices with \(\nu_2(d_n)=1\) is \(1/2\), with valuation \(2\) is zero, and with each fixed valuation \(j\ge3\) is \(2^{1-j}\).

## Assumptions and scope

The numbers are the **little**, not large, Schröder sequence. Thus \(s_n=S_n/2\) for positive indices if \(S_n\) is the large sequence of Cao–Pan. The theorem concerns positive indices \(n\ge1\); the zero difference at \(n=0\) is deliberately excluded. The valuation is taken only of nonzero integers. The local congruence holds for all \(k\ge3\). Densities are natural densities over all positive indices, not finite-block equalities.

A previously recorded binomial identity for the derived sequence [2] is the starting point. For nonnegative integers \(m\), put
\[
f(m)=\frac{s_{m+2}-s_{m+1}}2=\sum_{j=0}^{m}\frac{2^j}{j+1}\binom mj\binom{m+2}j.
\]
The right-hand side is \({}_2F_1(-m,-m-2;2;2)\), explicitly listed in [2]; its generating function is \(((z-1)\sqrt{z^2-6z+1}-z^2-4z+1)/(8z^3)\), also listed there. The identity follows from that generating function and the classical little-Schröder generating function \((1+z-\sqrt{1-6z+z^2})/(4z)\). This previously known identity is **not** the novel claim.

## Proof

**1. Uniform two-adic extension.** For \(x\in\mathbb Z_2\), the generalized binomial coefficients \(\binom{x}{j}\) belong to \(\mathbb Z_2\). Consequently
\[
F(x)=\sum_{j\ge0}\frac{2^j}{j+1}\binom{x}{j}\binom{x+2}{j}
\]
converges uniformly on \(\mathbb Z_2\), since \(j-\nu_2(j+1)\to\infty\). On nonnegative integers it equals \(f(m)\), because the sum terminates. Its two relevant zeros are explicit:
\[
F(-1)=1-1=0,\qquad
F(-3)=\frac12\sum_{j\ge0}(j+2)2^j=0,
\]
using \(\sum2^j=-1\) and \(\sum j2^j=2\) in \(\mathbb Q_2\).

**2. Isometry on odd residue balls.** Claim that for every odd \(x\in\mathbb Z_2\) and every nonzero \(h\in4\mathbb Z_2\),
\[
\nu_2(F(x+h)-F(x))=\nu_2(h).
\]
Set \(a=\nu_2(h)\ge2\) and \(T_j(x)=\frac{2^j}{j+1}\binom{x}{j}\binom{x+2}{j}\). By Vandermonde's identity and \(i\binom hi=h\binom{h-1}{i-1}\),
\[
\nu_2\left(\binom{x+h}{j}-\binom xj\right)\ge a-\lfloor\log_2j\rfloor\quad(j\ge1),
\]
and likewise with \(x+2\). Hence the difference of the \(j\)-th product has the same lower bound. Multiplying by \(2^j/(j+1)\) shows \(T_j(x+h)-T_j(x)\in2^{a+1}\mathbb Z_2\) for all \(j\ge4\), since \(j-\nu_2(j+1)-\lfloor\log_2j\rfloor\ge1\). The same bound holds for \(j=2\). The \(j=0\) term is constant, while \(T_1(x)=x(x+2)\) changes by \(h(2x+2+h)\in2^{a+1}\mathbb Z_2\).

The decisive term is
\[
T_3(x)=\frac{x^2(x^2-4)(x^2-1)}{18}.
\]
Set \(Q(x)=x^2(x^2-4)\). If \(x\) is odd and \(h\in4\mathbb Z_2\), then \(Q(x+h)\) is odd, \((Q(x+h)-Q(x))/h\in4\mathbb Z_2\), and \((x^2-1)/18\in4\mathbb Z_2\). Therefore the exact divided difference satisfies
\[
\frac{T_3(x+h)-T_3(x)}h
=\frac{Q(x+h)-Q(x)}h\frac{x^2-1}{18}
+Q(x+h)\frac{2x+h}{18}
\equiv\frac{x+h/2}{9}\equiv1\pmod2.
\]
All the other differences are divisible by \(2^{a+1}\). Thus \((F(x+h)-F(x))/h\) is odd and the claimed exact isometry holds, for **every** two-adic odd \(x\) and all nonzero \(h\) divisible by four.

**3. Evaluation at integers.** If \(m\ge1\) is odd, then exactly one of \(m+1,m+3\) is divisible by four. For \(m\equiv3\pmod4\), compare \(F(m)\) to \(F(-1)=0\) with displacement \(h=m+1\); for \(m\equiv1\pmod4\), compare to \(F(-3)=0\) with displacement \(h=m+3\). The isometry proves
\[
\nu_2(F(m))=\begin{cases}\nu_2(m+1),&m\equiv3\pmod4,\\\nu_2(m+3),&m\equiv1\pmod4.\end{cases}
\]
If \(m\) is even, the \(j=0\) term of \(F(m)\) is one, \(T_1(m)=m(m+2)\) is even, and every \(T_j(m)\), \(j\ge2\), is even; hence \(F(m)\) is odd. Inserting \(m=n-1\) into \(d_n=2F(n-1)\) yields precisely the stated valuation formula. As the difference is strictly increasing by the classical positive Schröder recurrence, no zero valuation ambiguity arises.

**4. Divisibility and densities.** If \(n\) is odd, \(\nu_2(d_n)=1\). If \(n=2t\) is even, then \(\nu_2(d_n)=2+\nu_2(t(t+1))\). As exactly one of \(t,t+1\) is even, \(2^r\mid t(t+1)\) exactly when \(t\equiv0,-1\pmod{2^r}\). Replacing \(r\) by \(k-2\) yields the claimed zero loci. Among all positive \(t\), \(\nu_2(t(t+1))=r\) has density \(2^{-r}\) for \(r\ge1\), giving overall density \(2^{-(r+1)}=2^{1-(r+2)}\). This proves the complete distribution.

## Verification

The accompanying standalone `check.py` performs exact integer and rational arithmetic, reconstructs the little Schröder sequence from its recurrence, checks the finite hypergeometric identity, the stated valuation rule, local zero loci for multiple powers of two, and discrete isometry instances. Its actual output was `CHECK_OK 17261 exact assertions; n<= 1100`. These finite checks do not substitute for steps 1–4, which establish the infinite theorem.

## Relationship to prior work

Sun [1] studied Delannoy/Schröder congruence sums, prominently at odd primes, and supplies a verified earlier primary number-theory setting. The OEIS entry [2] already gives the derived difference sequence, its generating function, and its hypergeometric expression; none is presented as a new discovery. Cao and Pan [3, Theorems 1–2] prove dyadic Stern-type index-shift congruences for the large Schröder numbers. Those theorems are closely related and constrain index shifts, but do not state the exact **consecutive-increment valuations**, both high-divisibility residue branches, or their complete valuation density law. Their refined index-shift congruence gives compatible local information, but its applicability to the exact zero branches needs the additional root and divided-difference analysis above.

## Limitations

The theorem concerns only prime two, consecutive differences, and positive indices. It does not provide the complete nonzero residue distribution of differences at a fixed modulus, nor assert historical priority beyond the inspected sources. The hypergeometric starting formula is previously published, and no independent mathematical audit has been performed. More general implicit results in earlier work on \(2\)-adic Schröder sequences may exist.

## References

[1] Zhi-Wei Sun, *On Delannoy numbers and Schröder numbers*, arXiv:1009.2486v1 (first submitted 2010-09-13), https://arxiv.org/abs/1009.2486.

[2] OEIS A239204, *Expansion of a square-root algebraic generating function* (created 2014-03-17; hypergeometric/difference identities added 2014-09-23), https://oeis.org/A239204.

[3] Hui-Qin Cao and Hao Pan, *A Stern-type congruence for the Schröder numbers*, arXiv:1512.06310v1 (2015-12-20), https://arxiv.org/pdf/1512.06310.
