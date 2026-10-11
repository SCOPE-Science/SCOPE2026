# A Landau–Ramanujan secondary term for square-free arithmetic numbers
## Finding
An integer \(n\) is called arithmetic when \(\sigma(n)/\tau(n)\) is an integer. Let \(E_{\mathrm{sf}}(x)\) count square-free non-arithmetic integers \(n\le x\), and let \(A_{\mathrm{sf}}(x)\) count square-free arithmetic integers \(n\le x\). Define the Landau–Ramanujan constant by
\[
K_{\mathrm{LR}}=\frac{1}{\sqrt 2}\prod_{p\equiv3\, (\mathrm{mod}\,4)}(1-p^{-2})^{-1/2}.
\]
Then
\[
E_{\mathrm{sf}}(x)\sim \frac{2K_{\mathrm{LR}}}{\pi^2}\frac{x}{\sqrt{\log x}},
\]
and hence
\[
A_{\mathrm{sf}}(x)=\frac{6}{\pi^2}x-\frac{2K_{\mathrm{LR}}}{\pi^2}\frac{x}{\sqrt{\log x}}+o\!\left(\frac{x}{\sqrt{\log x}}\right).
\]
In particular, the non-arithmetic proportion inside the square-free integers is asymptotic to \(K_{\mathrm{LR}}/(3\sqrt{\log x})\).

## Assumptions and scope
All integers are positive. The functions \(\sigma\) and \(\tau\) are the ordinary sum-of-divisors and divisor-count functions. The result concerns only the square-free stratum; it does not replace the substantially broader distribution theorem for all non-arithmetic integers.

The square-free criterion used below is classical and is restated explicitly in Oller-Marcén: every odd square-free integer is arithmetic, while an even square-free integer is arithmetic exactly when at least one of its prime divisors is congruent to \(3\pmod 4\).

## Proof
By the square-free criterion, a square-free integer is non-arithmetic exactly when it has the form \(n=2m\), where \(m\) is square-free and every prime divisor of \(m\) is congruent to \(1\pmod 4\). The case \(m=1\) includes \(n=2\).

Let \(f(m)\) be the indicator of square-free integers all of whose prime factors are congruent to \(1\pmod 4\), with \(f(1)=1\). Its Dirichlet series is
\[
F(s)=\sum_{m\ge1}\frac{f(m)}{m^s}=\prod_{p\equiv1\, (\mathrm{mod}\,4)}(1+p^{-s}).
\]
Put
\[
P_1(s)=\prod_{p\equiv1\, (\mathrm{mod}\,4)}(1-p^{-2s}),
\qquad
P_3(s)=\prod_{p\equiv3\, (\mathrm{mod}\,4)}(1-p^{-2s}).
\]
If \(\chi_4\) is the nonprincipal character modulo \(4\), then the Euler products for \(\zeta(s)\) and \(L(s,\chi_4)\) give
\[
F(s)=\zeta(s)^{1/2}G(s),
\]
where, in a neighborhood of \(s=1\),
\[
G(s)=P_1(s)\left(L(s,\chi_4)(1-2^{-s})P_3(s)\right)^{1/2}.
\]
The products \(P_1(s)\) and \(P_3(s)\) converge absolutely for \(\Re(s)>1/2\), and \(L(1,\chi_4)=\pi/4\). The standard Landau–Selberg–Delange theorem with exponent \(1/2\) therefore yields, for \(B(y)=\sum_{m\le y}f(m)\),
\[
B(y)\sim \frac{G(1)}{\Gamma(1/2)}\frac{y}{\sqrt{\log y}}
=\frac{P_1(1)\sqrt{P_3(1)}}{2\sqrt2}\frac{y}{\sqrt{\log y}}.
\]
Now
\[
P_1(1)P_3(1)=\prod_{p>2}(1-p^{-2})=\frac{8}{\pi^2},
\]
while the definition of \(K_{\mathrm{LR}}\) gives \(P_3(1)^{-1/2}=\sqrt2K_{\mathrm{LR}}\). Hence
\[
\frac{P_1(1)\sqrt{P_3(1)}}{2\sqrt2}=\frac{4K_{\mathrm{LR}}}{\pi^2}.
\]
Because \(E_{\mathrm{sf}}(x)=B(x/2)\) exactly,
\[
E_{\mathrm{sf}}(x)\sim \frac{2K_{\mathrm{LR}}}{\pi^2}\frac{x}{\sqrt{\log x}}.
\]
Finally, the standard square-free count is
\[
\sum_{n\le x}\mu(n)^2=\frac{6}{\pi^2}x+O(\sqrt x).
\]
Subtracting \(E_{\mathrm{sf}}(x)\), and noting that \(\sqrt x=o(x/\sqrt{\log x})\), proves the stated expansion for \(A_{\mathrm{sf}}(x)\). Dividing the first asymptotic by the square-free count gives the stated relative proportion.

## Verification
The packaged `verify.py` checks the exact square-free criterion against the direct divisibility condition \(\tau(n)\mid\sigma(n)\) for every square-free \(n\le10^6\). It finds exactly \(42186\) square-free non-arithmetic integers in that range. It also evaluates a truncated Euler product for \(K_{\mathrm{LR}}\), obtaining a coefficient close to \(0.15486409\) for \(2K_{\mathrm{LR}}/\pi^2\), and compares the normalized finite counts at three cutoffs. These computations corroborate the structural reduction and constant but are not used as proof of the asymptotic.

## Relationship to prior work
Oller-Marcén restates Ore's complete square-free criterion and gives primary classification \(11A25\); the same paper discusses arithmetic numbers more generally but does not state this square-free counting asymptotic. Bateman, Erdős, Pomerance, and Straus prove a much broader order-of-magnitude theorem for the number of all non-arithmetic integers. Their theorem does not imply an asymptotic for the square-free subfamily, whose scale here is \(x/\sqrt{\log x}\) and whose leading constant is explicit.

The analytic step is a direct application of the classical Landau–Selberg–Delange method to the multiplicative indicator supported on square-free products of primes congruent to \(1\pmod4\). Granville and Koukoulopoulos provide a modern statement of that method for partial sums of multiplicative functions. Targeted searches for the square-free arithmetic-number asymptotic, its equivalent exception count, and the Landau–Ramanujan constant connection did not locate a source stating the displayed formula.

## Limitations
The originality comparison cannot rule out an obscure non-indexed note that combines the classical square-free criterion with this standard analytic argument. The proof imports the classical Landau–Selberg–Delange theorem rather than reproving it. No claim is made about a sharper error term or about the full set of non-arithmetic integers.

## References
1. Antonio M. Oller-Marcén, *On arithmetic numbers*, arXiv:1206.1823v1, submitted 2012-06-08; later Mathematische Nachrichten 288 (2015), 665–669, DOI 10.1002/mana.201400085.
2. Paul T. Bateman, Paul Erdős, Carl Pomerance, and E. G. Straus, *The arithmetic mean of the divisors of an integer*, Lecture Notes in Mathematics 899 (1981), 197–220, DOI 10.1007/BFb0096462.
3. Andrew Granville and Dimitris Koukoulopoulos, *Beyond the LSD method for the partial sums of multiplicative functions*, arXiv:1710.01389v1; Ramanujan Journal 49 (2019), 287–319, DOI 10.1007/s11139-018-0119-3.
