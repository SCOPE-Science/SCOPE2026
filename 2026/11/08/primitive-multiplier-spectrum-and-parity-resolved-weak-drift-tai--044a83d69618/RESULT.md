# Primitive multiplier spectrum and parity-resolved weak-drift tails of the Dyck shift

## Finding
Let \(M\ge2\) be an integer. On the two-sided \(M\)-type Dyck shift \((\Sigma_D,\sigma)\), let \(H_n\) be the number of opening symbols minus closing symbols in a period-\(n\) word. For integers \(1\le d\le n\) with \(n-d\) even, let \(P_n^{(M)}(d)\) count *points of least shift period exactly* \(n\) with \(H_n=d\) (not the number of cyclic orbits). Then
\[
P_n^{(M)}(d)=\sum_{k\mid\gcd(n,d)}\mu(k)\binom{n/k}{(n-d)/(2k)}M^{(n+d)/(2k)},
\]
where a summand with a nonintegral lower binomial argument is defined to be zero, and \(\mu\) is the number-theoretic Möbius function. The number of primitive cyclic orbits in this class is \(P_n^{(M)}(d)/n\). For forbidden \(d\), the count is zero.

The smallest strictly positive height is \(d_n=1\) for odd \(n\), \(d_n=2\) for even \(n\). These *weakest non-neutral classes* have the exact formulas
\[
P_{2m+1}^{(M)}(1)=\binom{2m+1}{m}M^{m+1}\quad(m\ge0),
\]
\[
P_{2m}^{(M)}(2)=\binom{2m}{m-1}M^{m+1}
-\mathbf1_{\{m\ \mathrm{odd}\}}\binom{m}{(m-1)/2}M^{(m+1)/2}\quad(m\ge1).
\]
For the uniform probability distribution on the positive-height least-period-\(n\) *points*, let \(D_n=H_n\). Set \(\rho_M=2\sqrt M/(M+1)<1\). Then, along odd and even \(n\), respectively,
\[
\Pr(D_n=d_n)\sim
\begin{cases}
\sqrt{2M/(\pi n)}\,\rho_M^n,&n\ \mathrm{odd},\\
M\sqrt{2/(\pi n)}\,\rho_M^n,&n\ \mathrm{even}.
\end{cases}
\]
At the same time, \(\bigl(D_n-n(M-1)/(M+1)\bigr)/(2\sqrt{nM}/(M+1))\) converges in distribution to \(\mathcal N(0,1)\). The negative-height spectrum is its image under exchanging opening and closing symbol types. These formulas resolve a parity effect and an exact first weak-multiplier shell, which is not supplied by a large-deviation exponent alone.

## Assumptions and scope
Fix an integer \(M\ge2\). The alphabet is \(D=\{\alpha_1,\dots,\alpha_M,\beta_1,\dots,\beta_M\}\). A two-sided word belongs to \(\Sigma_D\) exactly when every finite contiguous block has nonzero reduction under \(\alpha_i\beta_j=\delta_{ij}\), with mismatched pairs reducing to zero. Each length-\(n\) period class is counted as points with a marked origin; an orbit of least period \(n\) contains \(n\) such points. The balance \(H_n\) is the signed count of symbols within one marked period, invariant under a cyclic change of origin. The result refers to the *symbolic shift*, not to exact periodic-point counts in a piecewise-affine geometric realization, where boundary conventions need separate treatment.

## Proof
**1. Positive-height marked-period census.** For a periodic Dyck word with \(H_n=d>0\), its bi-infinite opening/closing pattern has positive forward drift. Every closing symbol has a uniquely matched opening symbol to its left, since positive drift ensures an unmatched opener is present in its infinite past. Specifying the \(j=(n-d)/2\) closing positions and freely choosing one of \(M\) colors for each of the \(n-j=(n+d)/2\) opening positions determines the entire bi-infinite colored word. Conversely these choices produce a legal periodic Dyck word: each closing symbol receives the color of the most recently unmatched opening symbol, so all cancellations match. This construction commutes with cyclic shift, and hence is a bijection of marked period-\(n\) points with \(\binom nj M^{n-j}\) choices. Write this count as \(F_n^{(M)}(d)\). The special case \(d=0\) is not used in this bijection.

**2. Least-period inversion.** A point counted by \(F_n^{(M)}(d)\) whose least period is \(\ell=n/k\) is the \(k\)-fold repetition of an \(\ell\)-periodic point with strictly positive height \(d/k\). Thus \(k\mid\gcd(n,d)\) and
\[
F_n^{(M)}(d)=\sum_{k\mid\gcd(n,d)}P_{n/k}^{(M)}(d/k).
\]
Möbius inversion on divisors of the pair \((n,d)\) gives the displayed formula for \(P_n^{(M)}(d)\). Summing \(n\)-periodic points into shift cycles divides by \(n\). When \(d=1\) the gcd is one, proving the odd formula. For \(n=2m\), \(d=2\), only \(k=1,2\) can occur, and \(k=2\) contributes \(F_m^{(M)}(1)\), which is zero for even \(m\); the stated correction follows.

**3. The distribution and rarest positive shell.** Let \(B_n=\sum_{d>0}F_n^{(M)}(d)\). Put \(J\sim\operatorname{Bin}(n,1/(M+1))\). The first census shows exactly
\[
B_n=(M+1)^n\Pr(J<n/2).
\]
Since \(M\ge2\), the binomial parameter is strictly less than \(1/2\). By the elementary Chernoff bound at \(1/2\),
\[
1-\Pr(J<n/2)=O_M(\rho_M^n),\qquad \rho_M=\frac{2\sqrt M}{M+1}<1.
\]
More directly, \(\Pr(J\ge n/2)\le \rho_M^n\) follows by exponential Markov with tilt \(e^t=M\), choosing \(t=\log M\). Let \(Q_n=\sum_{d>0}P_n^{(M)}(d)\). Every positive-height point fixed by \(\sigma^n\) but of smaller least period is obtained by repeating a positive-height word of period \(\ell\mid n\), \(\ell\le n/2\). Since the number of such words is at most \((M+1)^\ell\), the union bound gives
\[
0\le B_n-Q_n\le n(M+1)^{n/2}.
\]
Therefore
\[
Q_n=(M+1)^n\bigl(1+O_M(\rho_M^n+n(M+1)^{-n/2})\bigr).
\]
Stirling's approximation gives \(\binom n{\lfloor n/2\rfloor}=2^n\sqrt{2/(\pi n)}(1+O(n^{-1}))\). Hence, for odd \(n\), \(P_n^{(M)}(1)\sim\sqrt{2M/(\pi n)}(2\sqrt M)^n\); for even \(n\), the dominant term \(P_n^{(M)}(2)\sim M\sqrt{2/(\pi n)}(2\sqrt M)^n\), since the possible period-half correction grows only as \(O_M((2\sqrt M)^{n/2})\). Dividing by \(Q_n\) proves the parity-sensitive probabilities.

**4. Gaussian law.** Under the full \((M+1)\)-symbol product model, \(H_n=n-2J\) has mean \(n(M-1)/(M+1)\) and variance \(4nM/(M+1)^2\). The total variation distance between this law and the positive-height primitive-point law is at most \(O_M(\rho_M^n+n(M+1)^{-n/2})\), by conditioning on \(J<n/2\) and deleting nonprimitive repetitions. The classical binomial central limit theorem therefore transfers. Interchanging \(\alpha_i\leftrightarrow\beta_i\) proves the negative-height analogue.

## Verification
The independent exact-arithmetic script `verify.py` enumerates every word over the \(M+1\)-letter presentation for \(M=2\), \(1\le n\le10\), and \(M=3\), \(1\le n\le8\). It compares the least cyclic periods and heights against the Möbius formula, including both parity-sensitive weakest-height formulas. It passed 91 pairs of \((n,d)\). The symbolic bijection, inversion, asymptotics, and central limit theorem are proved for all allowed parameters without relying on that finite test. The checker tests the full-shift presentation underlying the proven positive-drift coding, not every one of the \(2M\) literal symbol words.

## Relationship to prior work
Takahasi (2024, arXiv:2409.01261) proves asymptotic distributions for positive- and negative-multiplier Dyck periodic points and their heterochaos-baker counterparts. The earlier Krieger/Hamachi–Inoue counting framework provides the coding and total periodic-point enumerations; the fixed-height period-\(n\) binomial count follows directly from it and is not by itself claimed as a new coding principle. Takahasi (2025, arXiv:2503.14164) gives level-2 and level-1 large deviation principles, including the rate function for the opening/closing frequency; that yields the exponential rarity scale but does **not** by itself give the exact least-period divisor spectrum, even-period correction, or sharp \(n^{-1/2}\) rare-shell prefactors. Alsharari–Noorani–Akhadkulov (2014) establish a prime-orbit theorem for the unrefined Dyck shift. The present combined exact primitive-height and near-neutral refinements concern a different, more selective statistic.

## Limitations
This is a statement about exact symbolic periodic points and their signed-height multiplier classes, not a claim that every such point is realized away from the boundaries of a particular geometric baker-map coding. The exact binomial fixed-height count and Möbius inversion are elementary once the known positive-drift coding is supplied. Novelty is claimed only for their unified least-period, parity-corrected, sharp weak-multiplier classification relative to the material inspected, not for the classical binomial CLT or existing level-1 LDP. Earlier specialized multiplier-refined enumeration outside the accessible sources remains possible. The full 2005 Hamachi–Inoue article was not accessed, so its detailed enumerative scope is a residual risk.

## References
1. Hiroki Takahasi, “Distributions of periodic points for the Dyck shift and the heterochaos baker maps,” first public 2024-09-02, arXiv:2409.01261, https://arxiv.org/abs/2409.01261.
2. Hiroki Takahasi, “Large deviation principles for periodic points of the Dyck shift,” 2025, arXiv:2503.14164, https://arxiv.org/html/2503.14164.
3. Fahad Alsharari, Mohd Salmi Md. Noorani, Habibulla Akhadkulov, “Counting Closed Orbits for the Dyck Shift,” Abstract and Applied Analysis (2014), doi:10.1155/2014/304798.
4. T. Hamachi and K. Inoue, “Embedding of shifts of finite type into the Dyck shift,” Monatshefte für Mathematik 145 (2005), 107–129, doi:10.1007/s00605-004-0297-5.
5. Y. Saiki, H. Takahasi, K. Yamamoto, J. A. Yorke, “The dynamics of the heterochaos baker maps,” arXiv:2401.00836.
