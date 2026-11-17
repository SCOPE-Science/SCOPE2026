# Exact 7-adic value spectrum and frequencies of the classical Lucas numbers

## Finding
Let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\) for integers \(n\geq0\). Write \(\nu_k(y)\) for the number of indices \(0\le n<T_k\) such that \(L_n\equiv y\pmod{7^k}\), where \(T_k\) is the least period modulo \(7^k\). For every integer \(k\geq1\),
\[
T_k=16\cdot7^{k-1}.
\]
For \(k=1\), the respective frequencies at residues \(0,1,2,3,4,5,6\) are \(2,2,1,4,4,1,2\). For \(k\geq2\), put \(m=k-2\), let \(R_m(u)=\#\{z\in\mathbb Z/7^m\mathbb Z:z^2\equiv u\pmod{7^m}\}\), and define \(R_0(0)=1\). The frequency function is exactly
\[
\nu_k(y)=\begin{cases}
2,&y\equiv0,1,6\pmod7,\\
4,&y\equiv3,4\pmod7,\\
7R_m(u),&y\equiv2\pmod7,\ y\equiv2+2205u\pmod{7^k},\\
7R_m(u),&y\equiv5\pmod7,\ y\equiv-2-2205u\pmod{7^k},\\
0,&\text{otherwise.}
\end{cases}
\]
In each critical case, \(u\) is uniquely determined modulo \(7^m\) because \(2205=45\cdot49\) and \(45\) is a unit modulo \(7^m\). Define \(S_0=1\), \(S_1=4\), and \(S_m=3\cdot7^{m-1}+S_{m-2}\) for \(m\ge2\). Then the number \(N_k\) of distinct values modulo \(7^k\) is
\[
N_1=7,\qquad N_k=5\cdot7^{k-1}+2S_{k-2}\quad(k\ge2).
\]
In particular, \((N_1,N_2,N_3,N_4,N_5)=(7,37,253,1759,12307)\). The closure of the Lucas values in \(\mathbb Z_7\) is precisely
\[
\mathcal I=\{x\in\mathbb Z_7:x\bmod7\in\{0,1,3,4,6\}\}\ \cup\ (2+2205\mathbb Z_7^{\,2})\ \cup\ (-2-2205\mathbb Z_7^{\,2}),
\]
where \(\mathbb Z_7^{\,2}=\{z^2:z\in\mathbb Z_7\}\), and its normalized additive Haar measure is \(\mu(\mathcal I)=41/56\).

## Assumptions and scope
The indices are all nonnegative integers, the prime is exactly \(7\), and congruences are of integer values. The three pieces of the displayed 7-adic image are disjoint, since their reductions modulo \(7\) lie in the five regular classes, class \(2\), and class \(5\). The frequency counts refer to the *least* period of the scalar Lucas sequence, not to an arbitrary multiple of that period. Roots counted in \(R_m\) are residue classes; \(m=0\) denotes the singleton quotient ring. No assertion at other primes or for other recurrence initial conditions is made.

## Proof
**1. Exact 7-adic interpolation and its linear term.** In the unramified quadratic extension \(K=\mathbb Q_7(\sqrt5)\), set \(\alpha=(1+\sqrt5)/2\) and \(\beta=(1-\sqrt5)/2\). Their product is \(-1\), and Binet's formula gives \(L_n=\alpha^n+\beta^n\) and \(F_n=(\alpha^n-\beta^n)/\sqrt5\). Direct recurrence calculation gives \(L_{16}=2207\) and \(F_{16}=987\), so
\[
\lambda=\alpha^{16}=(2207+987\sqrt5)/2\in1+7\mathcal O_K,\qquad \beta^{16}=\lambda^{-1}.
\]
Moreover \(\nu_7(\lambda-1)=1\): its \(\sqrt5\)-coefficient has valuation \(1\), whereas its scalar coefficient has valuation \(2\). Thus \(\theta=\log\lambda\) has valuation \(1\), and
\[
\theta/7\equiv\sqrt5/2\pmod{7\mathcal O_K}.
\]
Conjugation sends \(\theta\) to \(-\theta\). For \(r\in\{0,\dots,15\}\), define the analytic function
\[
f_r(t)=\alpha^r\exp(t\theta)+\beta^r\exp(-t\theta),\quad t\in\mathbb Z_7.
\]
It takes values in \(\mathbb Z_7\), by conjugation invariance, and equals \(L_{r+16t}\) when \(t\) is nonnegative integral. Its Taylor coefficients after the constant term are in \(7\mathbb Z_7\). For every \(r\) with \(F_r\not\equiv0\pmod7\), the normalized function \((f_r(t)-L_r)/7\) has the form \(a_rt+7A_r(t)\) with \(a_r\in\mathbb Z_7^\times\) and \(A_r\) a convergent restricted power series over \(\mathbb Z_7\). Indeed,
\[
a_r\equiv(\theta/7)(\alpha^r-\beta^r)\equiv(5/2)F_r\pmod7.
\]
The coefficient of \(t^j\) for \(j\ge2\) is divisible by \(7\) after normalization, because \(j-\nu_7(j!)-1\ge1\). Consequently
\[
\nu_7(f_r(t)-f_r(s))=1+\nu_7(t-s)
\]
for all distinct \(s,t\in\mathbb Z_7\). By contraction/Hensel lifting, \(f_r:\mathbb Z_7\to L_r+7\mathbb Z_7\) is a bijection. In a scalar period modulo \(7^k\), it therefore represents each residue in this ball exactly once.

**2. Exactly two quadratic branches.** The Lucas and Fibonacci sequences modulo \(7\) have period \(16\). Directly, \(F_r\equiv0\pmod7\) for \(0\le r<16\) exactly at \(r=0,8\). The fourteen regular branches reduce to \(L_r\bmod7\) with multiplicities \(2,2,4,4,2\) at residues \(0,1,3,4,6\), respectively. Set
\[
H(t)=\frac{\sinh(t\theta/2)}{\sinh(\theta/2)}.
\]
Since \(\theta^2\in49\mathbb Z_7\), the odd-power expansion is a restricted series over \(\mathbb Z_7\) of the form \(H(t)=t+7B(t)\); more precisely, for powers \(t^{2j+1}\), \(j\ge1\), the coefficient valuation is at least \(2j-\nu_7((2j+1)!)\ge1\), and the linear coefficient is a unit congruent to \(1\pmod7\). Therefore \((H(t)-H(s))/(t-s)\in1+7\mathbb Z_7\), so \(H\) is an isometric bijection of \(\mathbb Z_7\) and induces a permutation modulo every \(7^a\).

An exact algebraic identity gives
\[
\begin{aligned}
f_0(t)&=2+(\lambda^{t/2}-\lambda^{-t/2})^2=2+2205H(t)^2,\\
2205&=\lambda+\lambda^{-1}-2=L_{16}-2=45\cdot7^2.
\end{aligned}
\]
Also \(\alpha^8=-\lambda^{1/2}\), because both sides square to \(\lambda\) and both reduce to \(-1\pmod7\); similarly \(\beta^8=-\lambda^{-1/2}\). Hence
\[
f_8(t)=-2-2205H(t+1/2)^2.
\]
Thus their images are precisely the two translated and reflected square sets in the theorem. Modulo \(7^k\) with \(k\ge2\), any particular square residue \(u\pmod{7^{k-2}}\) has \(R_{k-2}(u)\) root preimages under the bijective reductions of \(H\), with exactly seven lifts modulo \(7^{k-1}\). This proves the claimed factor \(7R_{k-2}(u)\). The regular and critical branches lie in distinct residue classes modulo \(7\), proving the individual-frequency classification.

**3. Least period and counts.** Modulo \(7\), the consecutive pair \((L_n,L_{n+1})\) first returns to \((2,1)\) at \(n=16\), and the scalar Lucas residues have least period \(16\). The sixteen functions \(f_r\) take equal values modulo \(7^k\) when their arguments differ by a multiple of \(7^{k-1}\), so \(16\cdot7^{k-1}\) is a period modulo \(7^k\). Every period is divisible by \(16\) on reduction modulo \(7\). If \(16h\) is a period modulo \(7^k\), the regular-branch isometry at \(r=1\) forces \(7^{k-1}\mid h\). Hence the least period is as stated.

For squares modulo \(7^m\), there are \(3\cdot7^{m-1}\) unit squares, while all other squares are \(49\) times squares modulo \(7^{m-2}\). This gives \(S_0=1\), \(S_1=4\), and \(S_m=3\cdot7^{m-1}+S_{m-2}\). The five full balls contribute \(5\cdot7^{k-1}\) distinct residues, and each quadratic image contributes \(S_{k-2}\) when \(k\ge2\). Finally the Haar measure of squares in \(\mathbb Z_7\) is \((3/7)/(1-1/49)=7/16\). Each quadratic image is a scaled translate of this set by a factor of 7-adic valuation two, so the measure is \(5/7+2(7/16)/49=41/56\).

## Verification
Run `python3 verify_lucas7.py` using only Python's standard library. It enumerates the exact recurrence over one predicted least period at every modulus \(7^k\), \(1\le k\le5\), checks all individual residue frequencies against the square-root classification, checks the least periods by excluding their prime-index divisors, and checks the exact integer identities for \(L_{16}\), \(F_{16}\), and \(2205\). Expected summary: `VERIFY_OK levels=1..5 exact_individual_residues=19607 least_periods=PASS`. This finite check is corroboration, not the proof of the general case, which is the preceding 7-adic argument.

## Relationship to prior work
Bundschuh and Bundschuh (2010) classify the full classical Lucas residue-frequency functions for prime powers with primes \(2\) and \(5\); their results do not cover prime \(7\). Their 2011 article treats the prime \(3\). Lang and Lang (2013) and Avila and Chen (2013) characterize moduli for which the Lucas sequence attains every residue: \(7\) occurs, but \(49\) does not. Their binary completeness result does not specify either the values attained beyond the first power or their individual frequencies. Bragman and Rowland (2025) analyze the *Fibonacci* sequence's limiting prime-power residue density; their example at prime \(7\) also has density \(41/56\), but that agreement is not itself a new Lucas claim and their work does not state this theorem for the Lucas sequence. Carlip and Somer (1999, 2007) give general frequency bounds for second-order recurrences. Their 2007 main theorem concerns a different singular-frequency regime with exponent \(e>1\); here \(e=\nu_7(F_8)=1\), and the earlier 1999 chapter could not be inspected in full. General frequency bounds do not themselves state this exact Lucas spectrum. The explicit frequency formula and the decomposition into two Lucas quadratic images, not the coincident density alone, are the contribution described here.

## Limitations
The argument concerns only the standard classical Lucas sequence at prime \(7\). It neither classifies other primes nor supplies independent historical-priority certification. The full proof is mathematical, while finite execution through \(7^5\) is only a reproducibility check. This report has not undergone independent mathematical audit.

## References
1. P. Bundschuh and R. Bundschuh, *The sequence of Lucas numbers is not stable modulo 2 and 5*, Uniform Distribution Theory 5 (2010), 113–130. https://pcwww.liv.ac.uk/~karpenk/JournalUDT/vol05/no2/6Bundsch10-2.pdf
2. R. Bundschuh and P. Bundschuh, *Distribution of Fibonacci and Lucas Numbers Modulo* \(3^k\), Fibonacci Quarterly 49 (2011), 201–210. https://doi.org/10.1080/00150517.2011.12428042
3. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892, first posted 10 April 2013. https://arxiv.org/abs/1304.2892
4. B. Avila and Y. Chen, *On Moduli For Which the Lucas Numbers Contain a Complete Residue System*, Fibonacci Quarterly 51 (2013), 151–152. https://doi.org/10.1080/00150517.2013.12427958
5. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, Research in Number Theory 11 (2025), article 88. https://doi.org/10.1007/s40993-025-00667-1
6. M. Erickson, *Lucas Numbers Modulo m*, Open Problem Garden, dated 19 March 2012. https://openproblemgarden.org/op/lucas_numbers_modulo_m
7. W. Carlip and L. Somer, *Bounds for frequencies of residues of second-order recurrences modulo* \(p^r\), Mathematica Bohemica 132 (2007), 137–175. https://dml.cz/manakin/handle/10338.dmlcz/134189
8. W. Carlip and L. Somer, *Bounds for frequencies of residues of regular second-order recurrences modulo* \(p^r\), Number Theory in Progress 2 (1999), 691–719. https://doi.org/10.1515/9783110285581.341
