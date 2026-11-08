# The sharp prime-field threshold for three consecutive nonsquare cubic residues

## Finding
For a prime \(p\equiv1\pmod6\), let \(C_p\subset\mathbb F_p^\times\) be the elements that are cubic residues but quadratic nonresidues. Define \(N(p)=\#\{a\in\mathbb F_p:a,a+1,a+2\in C_p\}\). Then \(N(p)>0\) for every such prime except exactly the following 28:

\[7,13,19,31,37,43,61,67,73,79,97,103,109,127,157,163,229,277,283,409,421,457,487,577,601,727,733,1399.\]

Consequently the sharp universal threshold is \(p>1399\) (among primes congruent to \(1\) modulo \(6\)). An explicit bound, valid for all these primes, is
\[N(p)\ge\frac{p-325\sqrt{p}-108}{216}.\]

## Assumptions and scope
The field is a **prime** field \(\mathbb F_p\) with \(p\equiv1\pmod6\). A cubic residue means a nonzero cube; a quadratic nonresidue is a nonzero nonsquare. Consecutiveness means addition of \(1\) inside the field. This theorem makes no assertion for proper prime-power fields or for the looser requirement of being nonprimitive without being a cube.

## Proof
Let \(g\) be a primitive root of \(\mathbb F_p^\times\) and fix the order-six character \(\chi\) with \(\chi(g)=e^{2\pi i/6}\), extended by zero at zero. A nonzero element is in \(C_p\) exactly when its discrete logarithm to base \(g\) is congruent to \(3\) modulo \(6\). Therefore, for nonzero \(x\), the indicator of \(C_p\) is \(\frac16\sum_{j=0}^{5}(-1)^j\chi(x)^j\). Here the exponent-zero term is the constant function \(1\) on the nonzero elements.

Restrict \(a\) to \(\mathbb F_p\setminus\{0,-1,-2\}\). Expanding the product of three indicators gives \(216N(p)\) as a sum of \(6^3=216\) complete-character expressions, each weighted by a sign. The term indexed by \((0,0,0)\) is \(p-3\). Group the other terms according to the number \(r\) of nonzero exponents among their three indices.

For \(r=3\), there are \(5^3=125\) terms. Each is a multiplicative-character sum for a polynomial of the form \(x^a(x+1)^b(x+2)^c\), with each exponent between \(1\) and \(5\). Since this polynomial is not a sixth power and has three distinct roots, the standard Weil bound for multiplicative characters gives absolute value at most \(2\sqrt p\). None of the three forbidden arguments contributes to these sums.

For \(r=2\), there are \(3\cdot5^2=75\) terms. The full two-factor Jacobi-type sum has magnitude at most \(\sqrt p\) (equal to \(1\) if the product character is trivial). Removing the one forbidden argument at the unused factor changes its value by at most \(1\), so each term has modulus at most \(\sqrt p+1\).

For \(r=1\), there are \(3\cdot5=15\) terms. The complete single nontrivial character sum vanishes, and excluding the other two forbidden arguments changes it by at most \(2\).

The triangle inequality yields
\[
216N(p)\ge p-3-125(2\sqrt p)-75(\sqrt p+1)-15(2)=p-325\sqrt p-108.
\]
At \(p=106000\) the right side is positive, as certified without floating-point arithmetic by \((106000-108)^2>325^2\cdot106000\). The function \(t-325\sqrt t-108\) increases for \(t\ge106000\), so every eligible prime \(p\ge106000\) has \(N(p)>0\).

It remains to check primes below \(106000\). The accompanying standalone verifier `ns3_verify.py` uses a deterministic Eratosthenes sieve, exact factorization of \(p-1\), and primitive-root testing against every distinct prime divisor of \(p-1\). For each prime \(p\equiv1\pmod6\), it constructs the set \(C_p=\{g^{6j+3}:0\le j<(p-1)/6\}\) with modular integer arithmetic, and examines every possible initial argument \(1\le a\le p-3\). Its exact enumeration of all \(5044\) relevant primes below \(106000\) returns precisely the 28 listed exceptions. Because this covers every remaining prime, the classification is complete. The code also verifies samples via the independent Euler-criterion tests for being a cube and a nonsquare.

## Verification
Run `python3 ns3_verify.py` from a directory containing the extracted standalone script. No third-party Python packages are required. The program checks the full list of exceptions and the positivity threshold. All finite classification arithmetic is exact. The analytic character-sum bound, not the finite computation alone, proves the unbounded statement. The finite enumeration itself is exhaustive for the stated interval; the extra Euler-criterion cross-checks are sampled, as documented.

## Relationship to prior work
Cohen (2026) proves existence theorems for **pairs** of consecutive elements that are nonsquares and \(\ell\)-th powers; it neither supplies a triple theorem nor an exception list for three consecutive non-square cubes. Cohen (2024) classifies triples of nonsquares without imposing the cubic-residue condition. Cohen, Oliveira e Silva and Trudgian (2015) establish existence of three consecutive **primitive** elements in sufficiently large fields; primitive elements cannot belong to \(C_p\), so that theorem does not cover this one. In particular, \(p=1399\) has consecutive triples of nonsquares and consecutive triples of cubes, but none in their intersection, demonstrating the distinction between either weaker condition and this simultaneous one.

## Limitations
Only prime fields with \(p\equiv1\pmod6\) are treated. The numerical exception list is generated by exact finite computation, and no independent human or formal proof audit has been performed. Priority cannot be certified exhaustively against unindexed older literature. The analytic lower bound is deliberately conservative: \(106000\) is a sufficient verification cutoff, not the sharp existence cutoff.

## References
1. S. D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429 (first public 2026-04-23), Sections 1–2 and main theorems.
2. S. D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737 (first public 2024-02-16), Theorem 1.1.
3. S. D. Cohen, T. Oliveira e Silva, T. Trudgian, *On consecutive primitive elements in a finite field*, Bull. London Math. Soc. 47 (2015), 418–426, doi:10.1112/blms/bdv018.
4. Standard Weil multiplicative character-sum bound for a polynomial with \(r\) distinct roots that is not a perfect character-order power: absolute value at most \((r-1)\sqrt p\). See Lidl–Niederreiter, *Finite Fields*, and the background character-sum estimates in Cohen (2026).
