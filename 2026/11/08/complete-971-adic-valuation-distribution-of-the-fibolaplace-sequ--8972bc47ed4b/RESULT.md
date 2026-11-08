# Complete \(971\)-adic valuation distribution of the FiboLaplace sequence

## Finding
Let \(e_1=e_2=1\) and \(e_n=(n-1)e_{n-1}-e_{n-2}+1-(-1)^n\) for \(n\ge3\). With \(p=971\), for every integer \(n\ge1\),
\[
\nu_p(e_n)=\begin{cases}
1,&n\equiv388\text{ or }1554\pmod{1942},\\
\nu_p(n),&n\equiv0\pmod{1942},\\
0,&\text{otherwise}.
\end{cases}
\]
The natural distribution of the nonnegative valuations exists: density \(1-3/(2p)\) for valuation zero, density \(1/p+(p-1)/(2p^2)\) for valuation one, and density \((p-1)/(2p^{k+1})\) for each integer \(k\ge2\). The mean valuation in the sense of natural averages is \(1/p+1/[2(p-1)]\).

## Assumptions and scope
All indices are positive integers, \(p=971\) is prime, and \(\nu_p(a)\) is the exponent of \(p\) in a nonzero integer \(a\). The recurrence and initial conditions define the sequence; equivalently it arises by Laplace-transform integration of Fibonacci polynomials. The statement concerns this prime only and gives neither a general all-primes law nor any independent audit.

## Proof
**Step 1: exact finite residue census.** Reduce the defining recurrence modulo \(p\). Its coefficients and forcing have period \(2p\), since \(p\) is odd. Direct modular recurrence yields \(e_1\equiv e_{2p+1}\equiv1\), \(e_2\equiv e_{2p+2}\equiv1\pmod p\), hence induction yields period \(2p\) for all positive indices. An exhaustive integer-modular computation of all \(2p=1942\) residues, reproducible using the standalone verifier, finds precisely \(n\equiv388,1554,0\pmod{1942}\) as zeros. This is a finite exhaustive modular lemma, not a numerical inference about arbitrarily large indices. The verifier also independently checks the standard direct product representation on one complete period.

**Step 2: polynomial truncation modulo \(p^2\).** Set \(P(m,0)=1\) and \(P(m,j)=\prod_{\ell=1}^{j}(m^2-\ell^2)\). The exact identity of Givens and Moll is
\[
e_{2m}=mA(m),\qquad A(m)=\sum_{j=0}^{m-1}P(m,j)\quad(m\ge1).
\]
Define the fixed polynomial \(S(t)=\sum_{j=0}^{p-1}\prod_{\ell=1}^{j}(t^2-\ell^2)\). For every integer \(m\ge1\), \(A(m)\equiv S(m)\pmod{p^2}\): if \(j\ge p\), the product is divisible by \(p^2\). Indeed, if \(m\equiv0\pmod p\), the factor with \(\ell=p\) is divisible by \(p^2\); otherwise the two distinct factors \(\ell=r\) and \(\ell=p-r\), where \(r\equiv m\pmod p\) and \(1\le r<p\), each contribute a factor of \(p\). For \(m<p\), all extraneous terms vanish identically because the factor \(\ell=m\) is zero. Accordingly, for every integer \(a\) and \(t\), the polynomial Taylor congruence gives
\[
A(a+pt)\equiv S(a)+ptS'(a)\pmod{p^2}.
\]

**Step 3: the two terminal branches.** The verifier supplies the following exactly reproducible modular certificates:
\[
S(194)\equiv S(777)\equiv459283=971\cdot473\pmod{971^2},
\]
and \(S(194+971)\equiv S(777+971)\equiv459283\pmod{971^2}\). Subtraction and the Taylor congruence force \(S'(194)\equiv S'(777)\equiv0\pmod{971}\). Hence for all \(m\equiv194,777\pmod{971}\), the value \(A(m)\) has valuation exactly one; these \(m\) are units modulo \(p\), so \(\nu_p(e_{2m})=1\). The corresponding full-index residues are \(388\) and \(1554\) modulo \(1942\).

**Step 4: the distinguished branch.** For \(m\equiv0\pmod p\), the same truncation shows
\[
A(m)\equiv S(0)=\sum_{j=0}^{p-1}(-1)^j(j!)^2\equiv383\pmod{971}.
\]
Thus \(A(m)\) is a unit and \(\nu_p(e_{2m})=\nu_p(m)=\nu_p(2m)\). Combining with the complete residue census proves every case, including all odd indices.

**Step 5: densities and mean.** The two terminal classes each have natural density \(1/(2p)\). Multiples of \(2p\) have density \(1/(2p)\), and conditional on that class, the valuation of \(2pt\) is \(1+\nu_p(t)\). The geometric valuation distribution of ordinary positive integers gives the three density formulas above. To justify the mean, the counts of multiples of \(2p^k\) contribute a summable series, with uniformly controlled tails; the limiting arithmetic mean of valuations equals \(1/p+\sum_{k\ge1}1/(2p^k)=1/p+1/[2(p-1)]\).

## Verification
Run `python3 verify.py` in this file's directory. It produces `CYCLE_ROOTS [388, 1554, 1942]`, verifies direct product formulas on one period, checks the exact modular terminal values and distinguished unit, and independently computes the recurrence modulo \(971^3\) for \(1\le n\le1,885,682\), printing `VERIFY_OK`. The finite one-period modular census is exhaustive for the periodicity lemma, and the polynomial congruence provides the infinite lift. The longer finite check is corroboration, not an infinite proof.

## Relationship to prior work
Flórez, Higuita-Diaz, and Ramírez (arXiv:2610.37356v1, posted October 27, 2026) studied valuation trees and specifically displayed a terminal internal branch at \(p=971\), residue \(388\). Their discussion does not give the complete \(971\)-adic valuation formula, identify both terminal classes \(388,1554\), or derive their densities. Givens and Moll (2020) established the exact product representations and explicit valuations for other primes; those identities are used as prior results. OEIS A003470 records the sequence and recurrence. An equivalent older, unindexed complete distribution cannot be ruled out.

## Limitations
Novelty is an implication comparison with accessible literature, not a certification of absolute priority. The proof includes an exhaustive finite modular computation as a fully reproducible lemma; it does not claim a closed-form conceptual classification of the modular root set without that computation. This theorem is only for the single prime \(971\). No independent mathematical audit has been performed.

## References
- R. Flórez, R. Higuita-Diaz, J. L. Ramírez, *On \(p\)-Adic Valuation Trees Arising from Laplace Transform of Fibonacci Polynomials*, arXiv:2610.37356v1 (first posted 2026-10-27).
- Givens and Moll, *Integrals of Fibonacci Polynomials and Their Valuations* (2020), source for exact product representations and recurrence.
- OEIS A003470, the FiboLaplace integer sequence.
