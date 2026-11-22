# Exact dyadic valuation census and sharp extremal layers for quaternary Fuss–Catalan numbers

## Finding
For each integer \(n\ge0\), let
\[
F_n=\frac{1}{3n+1}\binom{4n}{n},\qquad V_n=\nu_2(F_n),
\]
where \(F_n\) counts plane rooted full four-ary trees with \(n\) internal vertices. For each integer \(L\ge0\), define the integer polynomial
\[
P_L(t)=\sum_{0\le n<2^L}t^{V_n}.
\]
The complete finite-block valuation distribution has the rational bivariate generating function
\[
\boxed{\sum_{L\ge0}P_L(t)z^L=\frac{1+(1-t)z-z^2}{(1-(1+t)z)(1-(1-t+t^2)z^2)}.}
\]
In particular, for all \(L\ge0\),
\[
\#\{0\le n<2^L:V_n=0\}=\left\lfloor\frac{L+1}{2}\right\rfloor+1,
\qquad
\max_{0\le n<2^L}V_n=2\left\lfloor\frac L2\right\rfloor.
\]
The maximum occurs once when \(L\) is even and exactly \(L+1\) times when \(L\) is odd. For even \(L\), its unique index is \(n=(2^{L+1}-2)/3\). If \(n\) is uniformly sampled from \(\{0,\dots,2^L-1\}\), then the valuation \(V_n\) has the exact moments
\[
\mathbb E V_n=\frac L2-\frac13+\frac{(-1)^L}{3\cdot2^L},
\]
\[
\operatorname{Var}(V_n)=\frac L4+\frac29+\frac{7(-1)^L}{18\cdot2^L}-\frac1{2^{L+1}}-\frac1{9\cdot4^L}.
\]
Moreover, \((V_n-L/2)/(\sqrt L/2)\) converges in distribution to a standard Gaussian as \(L\to\infty\).

## Assumptions and scope
All claims concern integer indices \(n\ge0\), binary index blocks of exact length \(2^L\) starting at zero, and the usual valuation \(\nu_2\) of a positive integer. The indeterminates \(t,z\) are formal: the displayed generating function is an equality in \(\mathbb Z[t][[z]]\). No assertion is made for other arities or other primes. The first source is an original publication of the general Fuss–Catalan object; the valuation distribution here is a separate claim.

## Proof
Legendre's binary digit-sum identity, with \(s_2(m)\) the sum of the base-two digits of \(m\), gives
\[
V_n=s_2(n)+s_2(3n)-s_2(4n)-\nu_2(3n+1)
=s_2(3n)-\nu_2(3n+1).
\]
Adding one to \(3n\) erases its initial run of binary ones; therefore \(V_n\) is the count of binary ones strictly *after* the first zero, read from least significant digit toward the most significant digit, in the expansion of \(3n\). This is valid also at \(n=0\).

Read the \(L\) digits of \(n\) from least to most significant. Multiplication by three is performed with an incoming carry \(c\in\{0,1,2\}\). On reading \(d\in\{0,1\}\), the output bit is \(e\equiv3d+c\pmod2\) and the new carry is \(c'=\lfloor(3d+c)/2\rfloor\). Maintain a flag \(b\in\{0,1\}\) saying whether an output zero has already occurred. Multiply the weight by \(t\) exactly when \(b=1\) and \(e=1\), then update \(b'=b\lor(e=0)\).

Order the six states as \((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)\). Their transition matrix, counting both possible input digits with their weights, and the terminal carry weights, are
\[
T=\begin{pmatrix}
0&1&1&0&0&0\\
0&1&0&t&0&0\\
1&0&0&0&0&1\\
0&t&0&0&0&1\\
0&0&0&1&1&0\\
0&0&0&1&0&t
\end{pmatrix},\qquad
f=\begin{pmatrix}1\\1\\1\\t\\t\\t\end{pmatrix}.
\]
The terminal vector reflects the remaining binary carry, whose value is at most two; the \((2,0)\) entry is harmless because that state is unreachable from the initial state. Thus \(P_L(t)=e_1^{\mathsf T}T^Lf\) for every \(L\ge0\). Exact elimination over \(\mathbb Z[t,z]\) gives
\[
e_1^{\mathsf T}(I-zT)^{-1}f
=\frac{1+(1-t)z-z^2}{(1-(1+t)z)(1-(1-t+t^2)z^2)},
\]
proving the main generating function. There is also a finite algebraic certificate independent of formal matrix inversion: with \(Q(X)=X^3-(1+t)X^2-(1-t+t^2)X+(1+t^3)\), direct multiplication yields \(Q(T)f=t(t-1)^2(t+1)e_5\), where \(e_5\) is the fifth standard basis column. No path from the initial state reaches the fifth state \((2,0)\), hence \(e_1^{\mathsf T}T^jQ(T)f=0\) for every \(j\ge0\). This proves the third-order recurrence below for all indices, not merely on tested initial values. An equivalent directly checkable recurrence is
\[
P_L=(1+t)P_{L-1}+(1-t+t^2)P_{L-2}-(1+t^3)P_{L-3}\quad(L\ge3)
\]
with \(P_0=1\), \(P_1=2\), and \(P_2=2+t+t^2\). These formulas are identities, not guesses based on finite tests.

Putting \(t=0\) yields \((1+z-z^2)/((1-z)(1-z^2))\); coefficient extraction proves the precise odd-value count. For completeness, put \(A_j(t)=\sum_{b=0}^{\lfloor j/2\rfloor}(1+t)^{j-2b}(1-t+t^2)^b\) for \(j\ge0\), and \(A_j=0\) for \(j<0\). The rational identity says \(P_L=A_L+(1-t)A_{L-1}-A_{L-2}\). The leading coefficient of \(A_j\) is \(\lfloor j/2\rfloor+1\); its next-to-leading coefficient is \(\sum_{b=0}^{\lfloor j/2\rfloor}(j-3b)\). These two coefficients, with the cancellation of the top term at odd depths, give degree \(2\lfloor L/2\rfloor\), with leading coefficient \(1\) for even \(L\) and \(L+1\) for odd \(L\). For even \(L\), the index \((2^{L+1}-2)/3\) has \(3n=2^{L+1}-2\), a binary word of exactly \(L\) ones followed by one zero, so it attains that maximum; uniqueness follows from the leading coefficient.

Differentiating the rational function once and twice in \(t\), setting \(t=1\), and using \(P_L(1)=2^L\) gives the mean and the factorial second moment, hence the stated variance. For the normal limit, the denominator has a unique dominant pole \(z=(1+t)^{-1}\) in a complex neighborhood of \(t=1\); its other two poles have modulus close to one, whereas the dominant pole has modulus close to \(1/2\). Uniform singularity extraction therefore gives \(P_L(e^s)/2^L=H(s)((1+e^s)/2)^L(1+O(\rho^L))\) for \(s\) near zero with an analytic \(H(0)=1\) and some \(\rho<1\). The centered and \(L^{1/2}\)-scaled moment generating functions tend to \(e^{u^2/2}\), proving the Gaussian statement.

## Verification
The included standalone Python checker independently compares exact binomial coefficients with the digit-sum valuation formula for all indices below \(2^8\). It also compares every valuation histogram below \(2^{14}\), both from direct digit arithmetic and from the six-state carry transducer, against the polynomial recurrence. It verifies the odd counts, maximum values and their multiplicities, mean and variance identities, and the total count in every block. It passed 623 exact assertions in the package-development execution. Its finite scope does not replace the matrix identity or the symbolic arguments above.

To replay, extract `checker.py` and run `python3 checker.py` with Python 3 and only the standard library; success prints `CHECK_OK`.

## Relationship to prior work
Aval's 2007 manuscript gives the classical general Fuss–Catalan numbers and their tree interpretation, not a full \(2\)-adic valuation census. Kauers–Krattenthaler–Müller (first preprint 2011; journal 2012), especially Sections 6 and 13, provides algorithms for Fuß–Catalan coefficients modulo powers of two and a higher-power-series representation, but does not evaluate the displayed all-block histogram. Krattenthaler–Müller (first preprint 2015), Section 7, generalizes prime-power coefficient congruences but likewise does not give this \(L\)-uniform moment and extremal distribution. Two 2026 studies of *ternary* Fuss–Catalan numbers have distinct exact binary valuation generating functions; changing arity changes the underlying arithmetic and does not entail this quaternary formula. The original valuation identity follows from classical Legendre arithmetic and is not, by itself, claimed as a new theorem.

## Limitations
No independent mathematical audit has been performed. The literature comparison is bounded: an earlier or more general published digit-transducer classification may imply the rational series even if the exact formula is not indexed or readily located. The Gaussian limit is for uniform finite binary-index blocks, not uniformly sampled unrestricted positive integers. The maximum multiplicity assertions are not claims about arbitrary translated intervals.

## References
- J.-C. Aval, *Multivariate Fuss–Catalan numbers*, arXiv:0711.0906v1 (first public 2007-11-06), https://arxiv.org/abs/0711.0906 .
- M. Kauers, C. Krattenthaler, and T. W. Müller, *A method for determining the mod-\(2^k\) behaviour of recursive sequences, with applications to subgroup counting*, arXiv:1107.2015 (first public 2011-07-11); Electron. J. Combin. 18(2), P37 (2012), https://arxiv.org/abs/1107.2015 .
- C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, arXiv:1508.02580 (first public 2015-08-11), https://arxiv.org/abs/1508.02580 .
- *Exact dyadic two-adic valuation census of ternary Fuss–Catalan numbers*, indexed published research, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-two-adic-valuation-census-of-ternary-fuss-catalan-n--7f423ce9ed57 .
