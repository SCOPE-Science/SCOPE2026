# Exact parity-sparsity law for distinct Fibonacci partitions

## Finding

Let \(F_0=0\), \(F_1=F_2=1\), and \(F_{m+2}=F_{m+1}+F_m\). Define \(R(n)\) as the number of finite subsets of \(\{F_2,F_3,\ldots\}=\{1,2,3,5,\ldots\}\) whose sum is \(n\), with \(R(0)=1\). For every integer \(k\geq0\), let

\[
B_k=\#\{0\leq n<F_{k+2}:R(n)\equiv1\pmod2\}.
\]

Then the exact generating function is

\[
\boxed{\sum_{k\geq0}B_kz^k=\frac{1-2z^4}{1-2z+z^2-2z^4+2z^5}.}
\]

In particular, \(B_0,B_1,\ldots=1,2,3,4,5,8,13,20,29,44,69,108,165,252,\ldots\), and for every \(k\geq5\),

\[
B_k=2B_{k-1}-B_{k-2}+2B_{k-4}-2B_{k-5}.
\]

Let \(\alpha=1.543689012692\ldots\) denote the unique positive real root of \(x^3-2x^2+2x-2=0\), \(\varphi=(1+\sqrt5)/2\), and \(\theta=\log\alpha/\log\varphi=0.9022534195\ldots\). Then

\[
B_k\sim c\alpha^k,\qquad c=0.8943322604\ldots>0,
\]

where \(c=(1-2r^4)/[-rQ'(r)]\), \(r=\alpha^{-1}\), and \(Q(z)=1-2z+z^2-2z^4+2z^5\). Consequently,

\[
\boxed{\#\{0\leq n<X:R(n)\text{ odd}\}=\Theta(X^\theta)\quad(X\longrightarrow\infty),}
\]

so the odd values of the distinct-Fibonacci partition function have natural density zero, with an exact power-law growth exponent.

## Assumptions and scope

All partitions use the distinct positive Fibonacci values beginning with \(F_2=1\) exactly once each; the repeated conventional value \(F_1=1\) is **not** a second available part. The quantity \(B_k\) counts actual integers in the half-open interval from zero to \(F_{k+2}\), not arbitrary binary strings with multiplicity. All identities hold for integers \(k\geq0\); the asymptotic claims concern large real cutoffs \(X\).

## Proof

**1. Recursion in Zeckendorf gaps.** Every positive integer has a unique Zeckendorf representation \(n=\sum_iF_{m_i}\), where its indices satisfy \(m_0>m_1>\cdots>m_t\geq2\), with gaps \(m_{i-1}-m_i\geq2\). The Fibonacci partition recursion of Robbins, as presented with proof by Chow and Slattery [2, Theorem 1.1 and Lemma 2.1], says that if a new largest summand is placed \(g\geq2\) positions above the previous largest summand, the pair of partition counts for the new total and for the total with that largest summand removed transforms via

\[
M(g)=\begin{pmatrix}\lfloor(g+2)/2\rfloor&-\varepsilon(g)\\1&0\end{pmatrix},
\quad\varepsilon(g)=2\lfloor(g+2)/2\rfloor-1-g.
\]

Here \(\varepsilon(g)=1\) for even \(g\), and zero for odd \(g\). Starting from the lowest selected summand \(F_m\), the initial vector is \((R(F_m),R(0))^T=(\lfloor m/2\rfloor,1)^T\), by Carlitz's formula [2]. Successive higher summands are processed in increasing index order; the first coordinate of the resulting vector is \(R(n)\). Reduction modulo two gives the very small update

\[
(a,b)\longmapsto(\tau(g)a+\epsilon(g)b,a)\pmod2,
\]

where \(\tau(g)=1\) for \(g\equiv0,1\pmod4\) and zero otherwise, and \(\epsilon(g)=1\) exactly when \(g\) is even. Thus the parity of \(R(n)\) is decidable using finite states.

**2. An explicit finite-state counting construction.** Read the Zeckendorf digits for indices \(2,3,\ldots,k+1\), from low to high. A word with no adjacent ones corresponds bijectively to one integer \(0\leq n<F_{k+2}\). Include a distinguished no-summand state \(N(p)\), where \(p\in\mathbb Z/4\mathbb Z\) is the current index phase; start at \(N(2)\). After the first digit one at index phase \(p\), enter a selected state \(S(p+1,a,b,d,h)\) with \(a=\lfloor p/2\rfloor\pmod2\), \(b=1\), \(d=1\), and \(h=1\). Here \(p\) always records the *next* index modulo four; \(d\) is the gap from the last selected index to the next index modulo four; and \(h=1\) means the next index is immediately adjacent and cannot be selected. A zero increments both \(p\) and \(d\) modulo four and sets \(h=0\); a one when \(h=0\) applies the above \((a,b)\) update using \(g\equiv d\pmod4\), increments \(p\), and resets \(d=h=1\). A one when \(h=1\) is forbidden. Before the first selection, zero only increments the phase and one initializes the selected state as above. Every state is accepting when it is a no-summand state or when its first parity coordinate \(a\) equals one.

This deterministic automaton has exactly \(84\) reachable states, generated from \(N(2)\). Let \(T\) be its integral transition-count matrix (each of the zero and one edges contributes one), let \(e\) be the initial-state unit column, and let \(u\) be the accepting-state indicator column. The exact counting identity is

\[
B_k=e^T T^k u.
\]

**3. A finite, exact recurrence certificate.** Write \(Q_T=T^5-2T^4+T^3-2T+2I\) and \(w=Q_Tu\). The accompanying standard-library Python checker explicitly enumerates all \(84\) states from the preceding rules and verifies the three integer identities

\[
e^Tw=0,\qquad e^TTw=0,\qquad T^2w=w.
\]

These are finite equality checks of explicitly specified vectors, rather than numerical fits. They imply \(e^TT^jw=0\) for **every** integer \(j\geq0\), because \(T^{j}w\) is \(w\) or \(Tw\) according to the parity of \(j\). Substitution of the definition of \(w\) gives

\[
B_{j+5}-2B_{j+4}+B_{j+3}-2B_{j+1}+2B_j=0
\]

for all \(j\geq0\). The same exact checker evaluates \(e^TT^ju\) for \(0\leq j\leq4\), giving \(1,2,3,4,5\). These initial values and the recurrence prove the displayed rational generating function for all \(k\), since multiplying by \(Q(z)=1-2z+z^2-2z^4+2z^5\) gives numerator \(1-2z^4\).

**4. Asymptotics and sparsity.** Factor

\[
Q(z)=(1-z^2)(1-2z+2z^2-2z^3).
\]

The cubic factor has a simple positive root \(r=\alpha^{-1}\approx0.6477988713\). The other two cubic roots have strictly greater modulus, as do \(\pm1\), so \(r\) is the unique singularity on the circle of convergence. The numerator is nonzero at \(r\), and a simple-pole coefficient calculation yields the positive constant \(c=(1-2r^4)/[-rQ'(r)]\). Thus \(B_k\sim c\alpha^k\). Binet's formula gives \(F_{k+2}=\Theta(\varphi^k)\). For \(F_{k+2}\leq X<F_{k+3}\), monotonicity places the odd-partition count between \(B_k\) and \(B_{k+1}\), proving the global \(\Theta(X^\theta)\) assertion. Since \(\alpha<\varphi\), the density tends to zero.

## Verification

Run `python3 verify.py` from the directory containing the embedded checker. This regenerates exactly \(84\) reachable states; verifies \(w\) and its period-two property by exact integer arithmetic; verifies both required scalar products; checks the recurrence over \(36\) successive prefixes; compares the automaton parity directly against \(17{,}711\) independent Fibonacci-subset dynamic-programming counts; and confirms the parities with an independent binary-polynomial XOR product. The finite-state identities, not these bounded experiments, certify the infinite recurrence.

## Relationship to prior work

The starting partition function and the Zeckendorf recursion are classical and are not new: see Robbins [1] and Chow–Slattery [2]. Sanna's more recent full-text study [3] gives positive-integer moment exponents using Berstel automata, but its results do not determine parity support or the exact count of odd partition values. Coons–Kristensen–Laursen [4] obtain refined summatory asymptotics of the *unreduced* partition function and also do not determine this parity support. Robbins's 1998 parity chapter [5] establishes infinitely many parity changes for Fibonacci-restricted partitions; that qualitative result does not imply this exact rational Fibonacci-window count or the sharp sparsity exponent. The present result supplies the explicit parity-support counting law and its exponent, rather than re-proving any of those baseline results.

## Limitations

The formula counts parity support exactly at Fibonacci cutoffs; it does not provide a universal leading constant for arbitrary real cutoffs, nor any distribution of positive valuations greater than zero. The argument relies on the cited established Fibonacci-partition recursion. Finite exact checking of the displayed transition-vector identities is reproducible and decisive for the consequent recurrence, but does not constitute an external independent mathematical audit. Earlier unindexed derivations of the parity counting law cannot be ruled out categorically.

## References

1. Neville Robbins, *Fibonacci partitions*, Fibonacci Quarterly 34 (1996), 306–313. https://www.mathstat.dal.ca/FQ/Scanned/34-4/robbins.pdf
2. Sam Chow and Tom Slattery, *On Fibonacci partitions*, Journal of Number Theory 225 (2021), 310–326; arXiv:2009.08222. https://arxiv.org/abs/2009.08222
3. Carlo Sanna, *A note on the power sums of the number of Fibonacci partitions*, Discrete Analysis (2025), article 2; arXiv:2309.12724v2. https://arxiv.org/html/2309.12724v2
4. Michael Coons, Simon Kristensen and Mathias L. Laursen, *Asymptotics for partitions over the Fibonacci numbers and related sequences, II*, arXiv:2611.04869v1, first public November 3, 2026. https://arxiv.org/html/2611.04869v1
5. Neville Robbins, *On the parity of certain partition functions*, in *Applications of Fibonacci Numbers*, vol. 7 (1998), pp. 319–325. https://doi.org/10.1007/978-94-011-5020-0_36
6. OEIS A000119 (distinct-Fibonacci partition function). https://oeis.org/A000119
