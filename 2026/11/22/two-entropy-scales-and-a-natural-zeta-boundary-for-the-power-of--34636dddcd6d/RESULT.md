# Two entropy scales and a natural zeta boundary for the power-of-two even-shift interspersion

## Finding
Let \(Y\subset\{0,1\}^{\mathbb Z}\) be the two-sided **even shift**, in which the number of zeros between successive ones is even. Let \(S=\{2^j:j\geq0\}\), introduce a new marker \(2\), and let \(X\subset\{0,1,2\}^{\mathbb Z}\) be the closure of all bilateral concatenations of code words \(2u\), where \(u\in\mathcal L_{2^j}(Y)\) for some \(j\geq0\). This is the concrete level-one interspersion of the even shift introduced in Huang--Jenkinson--Xu--Zhang (2026).

Write \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\), \(\varphi=(1+\sqrt5)/2\), and
\[
W(z)=\sum_{j\geq0}\bigl(F_{2^j+3}-1\bigr)z^{2^j+1}.
\]
Its Artin--Mazur zeta function, as a formal power series and then as a meromorphic function on \(|z|<\varphi^{-1}\), is exactly
\[
\boxed{\zeta_X(z)=\frac{1+z}{(1-z-z^2)(1-W(z))}.}
\]
In particular, every fixed-point count \(P_n=|\operatorname{Fix}(\sigma^n|_X)|\) is specified by
\[
\sum_{n\geq1}P_nz^n=z\frac{d}{dz}\log\!\left(\frac{1+z}{(1-z-z^2)(1-W(z))}\right).
\]
The radius of convergence of the zeta Taylor series is the unique \(r\in(0,\varphi^{-1})\) satisfying \(W(r)=1\); the dynamical entropy is \(h(X)=-\log r\). The rational interval \(0.442<r<0.443\) is certified by a finite sum and a geometric tail inequality. Numerically \(r=0.44210767533\ldots\), \(\exp h(X)=2.26189242077\ldots\). There is \(\rho<r^{-1}\) for which
\[
P_n=r^{-n}+O(\rho^n),\qquad \#\{\text{primitive orbits of length }n\}\sim\frac{r^{-n}}n.
\]
**The circle \(|z|=\varphi^{-1}\) is a natural boundary for meromorphic continuation of \(\zeta_X\) from its canonical meromorphic domain.** Thus one explicitly named nonsofic system with typical periodic optimization has two distinct analytic entropy scales: a leading simple pole at \(\exp(-h(X))\), and an impenetrable circle at \(\exp(-h(Y))=\varphi^{-1}\).

## Assumptions and scope
The two-sided shift is \(\sigma(x)_i=x_{i+1}\). A factor of the even shift is a finite binary word in which every pair of consecutive ones is separated by an even number of zeros; leading and trailing zero runs are unrestricted. The shift \(X\) is the **closed** code-generated shift, not only the set of infinite concatenations. For each \(n\geq1\) its \(\sigma^n\)-fixed-point set is finite. The phrase *natural boundary* refers to local meromorphic continuation across a nonempty arc of the stated circle, **not** to the radius of the Taylor series at the origin.

## Proof
**1. The even-shift word census and background zeta.** A binary word is either all zeros, or uniquely has the form \(0^a1(0^{2b_1}1)\cdots(0^{2b_t}1)0^c\) for \(a,c,t,b_i\geq0\). Its language-length generating function therefore equals
\[
\sum_{n\geq0}|\mathcal L_n(Y)|z^n=\frac{1}{1-z}+\frac{z}{(1-z)^2}\frac1{1-z/(1-z^2)}
=\frac1{(1-z)(1-z-z^2)}.
\]
Hence \(|\mathcal L_n(Y)|=F_{n+3}-1\), including \(|\mathcal L_0(Y)|=1\). The familiar even-state/odd-state labeled graph has adjacency matrix \(A=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). Its graph trace overcounts the all-zero periodic point once for even periods, and omits it for odd periods. Therefore \(P_n(Y)=\operatorname{tr}(A^n)+(-1)^{n+1}\), and
\[
\zeta_Y(z)=\frac{1+z}{\det(I-zA)}=\frac{1+z}{1-z-z^2}.
\]

**2. Periodic marker decomposition.** The marker-free part of \(X\) is exactly \(Y\): every binary factor avoiding markers comes from a subword of a single allowed even-shift gap, while every finite factor of \(Y\) extends to an allowed gap of arbitrarily large power-of-two length. A periodic point containing a marker has a unique circular decomposition into successive marked words \(2u\) with \(|u|\in S\). There are \(c_s=|\mathcal L_s(Y)|\) choices for each length \(s\in S\), giving the code-length enumerator \(W(z)=\sum_{s\in S}c_sz^{s+1}\).

For any \(n\geq1\), count pairs consisting of an \(n\)-periodic marked configuration and one distinguished marker in its \(n\)-coordinate window. With \(k\) marked blocks, the number of sequences of \(k\) specified blocks of total length \(n\) is \([z^n]W(z)^k\), and the distinction yields the factor \(n/k\). Thus
\[
P_n(X)-P_n(Y)=n[z^n]\sum_{k\geq1}\frac{W(z)^k}{k}
=n[z^n]\bigl(-\log(1-W(z))\bigr).
\]
This argument also covers configurations whose least period divides \(n\), since their markers are counted in the labeled \(n\)-window. Exponentiating proves the zeta identity, without invoking a finite-state presentation for \(X\).

**3. Entropy and the dominant pole.** The coefficients of \(W\) are nonnegative, and \(W\) has radius \(\varphi^{-1}\) by the Fibonacci asymptotic. At that radius each lacunary summand is bounded below eventually by a positive constant, so \(W(t)\uparrow\infty\) as \(t\uparrow\varphi^{-1}\). Thus exactly one \(r\in(0,\varphi^{-1})\) has \(W(r)=1\). The entropy equation is also a specialization of the established entropy formula for \((S,w)\)-gap shifts (Ramirez--Somers, 2025), and is not claimed as independently novel. Alternatively, the exponential word growth follows from a renewal upper bound: marker-free words have generating function \(\sum c_nz^n\), and a marked word is bounded by a binary prefix, a marker, any sequence of complete marked blocks, and a binary suffix. Hence its word-count generating function is coefficientwise bounded by
\[
\sum_{n\geq0}c_nz^n+z\left(\sum_{n\geq0}c_nz^n\right)^2(1-W(z))^{-1}.
\]
This has radius at least \(r\), while periodic-point growth gives entropy at least \(-\log r\), so \(h(X)=-\log r\).

The simple zero at \(r\) follows from \(W'(r)>0\). On \(|z|=r\), equality in \(|W(z)|\le W(r)=1\) at a zero of \(1-W\) forces \(z^2/r^2=z^3/r^3=1\), so \(z=r\). Isolated zeros yield \(R>r\), with \(R<\varphi^{-1}\), on whose closed disk \(1-W\) has no other zero. The logarithmic derivative of the simple-pole factor gives \(P_n=r^{-n}+O(R^{-n})\), and Möbius inversion yields the primitive-orbit asymptotic.

**4. The second, impenetrable circle.** Set \(\psi=(1-\sqrt5)/2=-\varphi^{-1}\) and \(H(t)=\sum_{j\geq0}t^{2^j}\). Binet's formula gives, initially for \(|z|<\varphi^{-1}\),
\[
W(z)=z\left(\frac{\varphi^3}{\sqrt5}H(\varphi z)-\frac{\psi^3}{\sqrt5}H(\psi z)-H(z)\right).
\]
The last two terms are analytic across every point of \(|z|=\varphi^{-1}\). If \(\xi\) is any root of unity of order a power of two, then, as \(t\uparrow1\), the tail of \(H(t\xi)\) is \(\sum_{j\geq J}t^{2^j}\), which diverges at a logarithmic rate: it is unbounded but \(O(\log(1/(1-t)))\). Such a boundary singularity cannot be a meromorphic pole (which diverges at a power-law rate) or a removable singularity. These dyadic roots are dense on the unit circle, so \(W\) cannot extend meromorphically through any arc of \(|z|=\varphi^{-1}\).

If \(\zeta_X\) extended meromorphically through any such arc, the identity
\[
W(z)=1-\frac{\zeta_Y(z)}{\zeta_X(z)}
\]
would make \(W\) meromorphic through that arc as well, a contradiction. This proves the stated meromorphic natural boundary. In particular the zeta function is nonrational.

## Verification
A standalone standard-library program `verify.py` independently enumerates all cyclic ternary words up to period ten, tests their exact marker gaps, and compares them with the formal zeta coefficient recurrence. It also enumerates even-shift words and verifies the Fibonacci language formula through length fourteen. Exact rational arithmetic certifies the bracket \(0.442<r<0.443\), using the inequalities \(F_{n+3}-1\le 2(13/8)^n\) and a dyadic geometric tail bound. The program's reported output is in `verification_output.txt`. These finite checks confirm computations but are not substitutes for the all-period decomposition or analytic-continuation proof.

## Relationship to prior work
Huang, Jenkinson, Xu and Zhang (2026), Section 11 and Remark 11.24, introduce this power-of-two interspersion, prove its Markov boundary is the even shift, and establish typical periodic optimization. They do not assert the formula above for its periodic zeta or its natural boundary. Ramirez and Somers (2025), Theorem 1.1, supply the entropy equation for a general decorated gap shift: the entropy identity itself is **covered prior art**. Dillon (2020/2022), Theorem 8.3, gives zeta functions for finite-graph \(\mathcal S\)-graph shifts with vertex run-length sets; it does not explicitly address this independently constrained even-shift decoration or the positive-background-entropy natural boundary. The publicly available result *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts* (2026) gives a marked-word zeta for Sturmian decorations with **no marker-free periodic points**, and a boundary at radius one. Its counting principle is similar, but its theorem does not imply the additional nontrivial even-shift periodic factor or the boundary at \(\varphi^{-1}\). Hong's (2011) renewal-system zeta results concern finite generators or restricted codes; they are a residual general-formulation comparison risk. The classical theory of lacunary series and basic Perron/renewal counting are not claimed as new.

## Limitations
This theorem concerns exactly the specified power-of-two interspersion of the even shift. No claim is made for arbitrary base subshifts, arbitrary allowed-gap sets, or the zeta of higher iterated interspersions. The numerical root is illustrative; the exact mathematical definition is \(W(r)=1\). The paper does not establish new typical-periodic-optimization conclusions or a new general entropy formula. General coded-shift zeta literature may contain an abstract encompassing formula, so priority for the **explicit second natural-boundary circle** deserves independent bibliographic review. No independent validation has been performed.

## References
1. W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Typical periodic optimization for dynamical systems: symbolic dynamics*, Inventiones mathematicae 245 (2026), first verified public online 2026-03-05, Section 11 and Remark 11.24; https://link.springer.com/article/10.1007/s00222-026-01411-x (arXiv:2603.07224 was posted 2026-03-07).
2. C. Ramirez and A. Somers, *\((S,w)\)-Gap Shifts and Their Entropy*, arXiv:2501.08438, first public 2025-01-14, Theorem 1.1; https://arxiv.org/html/2501.08438v2.
3. T. Dillon, *Dynamics and entropy of \(\mathcal S\)-graph shifts*, arXiv:2010.06031, first public 2020-10-12, Theorem 8.3; https://arxiv.org/abs/2010.06031.
4. S. Hong, *The zeta functions of renewal systems*, Ergodic Theory Dynam. Systems 31 (2011), 833--846; DOI:10.1017/S0143385710000015; https://doi.org/10.1017/S0143385710000015.
5. *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts*, public research note (2026); https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-periodic-zeta-rationality-versus-sturmian-nonsoficity-in-decorat--0881e8e9b148.
