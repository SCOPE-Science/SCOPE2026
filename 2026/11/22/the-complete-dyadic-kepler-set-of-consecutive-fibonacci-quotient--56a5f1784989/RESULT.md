# The complete dyadic Kepler set of consecutive Fibonacci quotients

## Finding
Put \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\), and \(q_n=F_{n+1}/F_n\) for integers \(n\ge1\). Define the Kepler set as the closure of these rational quotients in \(\mathbb Q_2\), not the unrestricted set of quotients of arbitrary Fibonacci terms.

**Theorem.** The exact closure is the disjoint union
\[
\mathcal K_2=\bigcup_{a\in\{0,1,2,7\}}(a+8\mathbb Z_2)\ \cup\ (3/2+2\mathbb Z_2)\ \cup\ \{x\in\mathbb Q_2:\nu_2(x)\le-3\}.
\]
Consequently \(\mathcal K_2\cap\mathbb Z_2\) has normalized Haar measure \(1/2\), while the finite nonzero valuation spectrum consists of all integers except \(-2\) and \(2\). The zero element belongs to the Kepler set as a limit.

For each integer \(k\ge3\), the least Fibonacci period modulo \(2^k\) is \(\pi_k=3\cdot2^{k-1}\). Among \(1\le n\le\pi_k\), exactly \(2^k\) indices satisfy \(3\nmid n\), and their \(F_{n+1}F_n^{-1}\pmod{2^k}\) values attain each of the \(2^{k-1}\) residues congruent to \(0,1,2,7\pmod8\) exactly twice. The other \(2^{k-1}\) indices satisfy \(3\mid n\); their reciprocal values \(F_nF_{n+1}^{-1}\pmod{2^k}\) attain each of the \(2^{k-2}\) residues congruent to \(0,6\pmod8\) exactly twice. All inverses here have odd denominators.

## Assumptions and scope
Here \(\nu_2\) is the standard valuation on \(\mathbb Q_2\), \(\nu_2(2)=1\), and \(\nu_2(0)=+\infty\). The symbol \(a+8\mathbb Z_2\) denotes a closed 2-adic residue ball. All residue inverses in the finite statement exist because \(F_n\) is odd exactly when \(3\nmid n\). The second inverse uses \(F_{n+1}\), odd when \(3\mid n\). The full Kepler set concerns rational consecutive quotients, not every ratio \(F_m/F_n\).

## Proof
**1. Exact dyadic Fibonacci valuations and entry indices.** The Fibonacci recurrence modulo two has period three; hence \(2\mid F_n\) precisely when \(3\mid n\). The identity
\[
F_{n+6}=8F_{n+1}+5F_n
\]
with \(F_3=2\) implies \(\nu_2(F_n)=1\) when \(n\equiv3\pmod6\), since successive shifts by six preserve \(F_n\pmod4\). The further identity
\[
F_{n+12}=144F_{n+1}+89F_n
\]
and \(F_6=8\) imply \(\nu_2(F_n)=3\) for \(n\equiv6\pmod{12}\), since the first coefficient is divisible by sixteen and \(89F_n\equiv9F_n\equiv8\pmod{16}\). For the companion Lucas numbers \(L_n=F_{n-1}+F_{n+1}\), the same six-step recurrence and \(L_6=18\) give \(L_m\equiv2\pmod4\) whenever \(6\mid m\). Doubling by \(F_{2m}=F_mL_m\) therefore increases the 2-adic valuation by exactly one on such indices. Writing any \(n\equiv0\pmod6\) as \(n=6u2^t\), \(u\) odd, proves
\[
\nu_2(F_n)=\begin{cases}0,&3\nmid n,\\1,&n\equiv3\pmod6,\\\nu_2(n)+2,&n\equiv0\pmod6.\end{cases}
\]
In particular, for \(k\ge3\),
\[
2^k\mid F_n\quad\Longleftrightarrow\quad z_k\mid n,\qquad z_k=3\cdot2^{k-2}.
\]

**2. An exact projective separation identity.** Cassini's determinant gives, for all positive integers \(m,n\),
\[
F_{n+1}F_m-F_{m+1}F_n=(-1)^nF_{m-n}
\]
using the standard extension \(F_{-j}=(-1)^{j+1}F_j\). When both \(n,m\) are not multiples of three, both denominators of their respective quotients \(F_{n+1}/F_n\) and \(F_{m+1}/F_m\) are 2-adic units. Their difference consequently has 2-adic valuation \(\nu_2(F_{m-n})\), except when \(m=n\) when it vanishes. If instead \(3\mid n,m\), both \(F_{n+1}\) and \(F_{m+1}\) are units and the difference of the reciprocal quotients \(F_n/F_{n+1}\) and \(F_m/F_{m+1}\) again has valuation \(\nu_2(F_{m-n})\). Therefore for either type of quotient and every \(k\ge3\), equality modulo \(2^k\) holds **if and only if** \(m\equiv n\pmod{z_k}\).

**3. Every lift occurs, and no others.** At \(k=3\), \(z_3=6\). The integer quotients at \(n=1,2,4,5\) have respective residues \(1,2,7,0\pmod8\); reciprocal quotients at \(n=3,6\) have residues \(6,0\pmod8\). For all \(k\ge3\), \(z_{k+1}=2z_k\). Every admissible index \(n\) at depth \(k\) has the two lifts \(n\) and \(n+z_k\), which retain its index category modulo three. By the separation identity,
\[
\nu_2(q_{n+z_k}-q_n)=\nu_2(F_{z_k})=k
\]
for integer quotients, with the analogous equality for reciprocals. Thus the two index lifts give **both** lifts of the same value residue modulo \(2^{k+1}\). Induction shows that the integer quotient residues at every \(k\ge3\) are precisely those congruent to \(0,1,2,7\pmod8\), each attained exactly once when \(n\) ranges through \(1,\ldots,z_k\) in the appropriate category. Their number is \(2z_k/3=2^{k-1}\). Reciprocal residues are exactly those congruent to \(0,6\pmod8\), each once in \(1,\ldots,z_k\), numbering \(z_k/3=2^{k-2}\). The known Fibonacci period \(\pi_k=2z_k\) (also obtainable by testing the pair state and the lifting identity) doubles every count, yielding exactly twice per residue for \(1\le n\le\pi_k\). This is an exact finite theorem, not merely a computational observation.

**4. Passage to \(\mathbb Q_2\).** For \(3\nmid n\) the quotients \(q_n\) lie in \(\mathbb Z_2\), and step 3 proves their closure is the four integer balls stated. For \(3\mid n\), \(F_{n+1}\) is odd and \(s_n=1/q_n=F_n/F_{n+1}\) lies in \(2\mathbb Z_2\). By step 3 its closure is \((6+8\mathbb Z_2)\cup8\mathbb Z_2\). Inversion is continuous on \(\mathbb Q_2^\times\), so the closure of the inverse set in \(\mathbb Q_2\) is
\[
(3/2+2\mathbb Z_2)\ \cup\ \{x:\nu_2(x)\le-3\},
\]
because inverting \(2(3+4\mathbb Z_2)\) gives \((1/2)(3+4\mathbb Z_2)=3/2+2\mathbb Z_2\), and inverting nonzero elements of \(8\mathbb Z_2\) gives precisely all elements of valuation at most \(-3\). No additional finite limits occur: any convergent sequence of terms from the union of the two index categories has a subsequence entirely in one category, and the two closed sets above already contain all such limits. The four disjoint integer balls each have Haar measure \(1/8\).

## Verification
The accompanying `CHECK.py` uses only integer arithmetic and Python's standard library. It verifies Fibonacci and Lucas valuation identities; tests the exact modular separation equivalence and both residue images and their full multiplicity histograms for all \(3\le k\le12\); and tests the rational determinant identity on finite index ranges. These finite checks are independent corroboration of the all-depth induction, not a substitute for it.

## Relationship to prior work
Lang and Lang (2013) study residue completeness of scalar Fibonacci-type cycles and record the least dyadic Fibonacci periods in Appendix A, not the consecutive-ratio image. Kumar (2024) explicitly confines his theorem on second-order \(p\)-adic Kepler sets to odd primes \(p\ge3\); therefore the dyadic case is not covered by those main results. Garcia and Luca (2016) study the **unrestricted quotient set** \(\{F_m/F_n\}\), which can be dense even when this consecutive-ratio set excludes whole dyadic balls. The present statement concerns the full exact dyadic Kepler set, including nonintegral poles, not only the separate scalar periods or individual valuations.

## Limitations
This result does not classify other primes or more general recurrences. It makes no claim to historical priority beyond the directly compared literature; an implicit older two-adic projective orbit classification remains possible. Independence has not been established through external mathematical review. The count of possible integral residues is \(2^{k-1}\), with \(2^k\) admissible indices in one complete Pisano period; these are different quantities.

## References
1. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892, first public 2013-04-10. https://arxiv.org/abs/1304.2892
2. R. Kumar, *Kepler Sets of Second-Order Linear Recurrence Sequences Over Q_p*, arXiv:2406.05890, first public 2024-06-09. https://arxiv.org/abs/2406.05890
3. S. R. Garcia and F. Luca, *Quotients of Fibonacci Numbers*, Amer. Math. Monthly 123 (2016), 1039–1044. https://doi.org/10.4169/amer.math.monthly.123.10.1039
