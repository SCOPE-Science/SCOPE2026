# Sharp completeness threshold for four consecutive cubic-power coset words

## Finding

For each prime \(p\equiv1\pmod 3\), fix a primitive root \(g\) of \(\mathbb F_p^\times\). Define the *cubic-coset color* \(c_g(u)\in\{0,1,2\}\) of \(u\ne0\) by \(u\in g^{c_g(u)}(\mathbb F_p^\times)^3\). A word \(\mathbf a=(a_0,a_1,a_2,a_3)\in\{0,1,2\}^4\) occurs if there exists \(x\in\mathbb F_p\) such that all \(x,x+1,x+2,x+3\) are nonzero and \(c_g(x+j)=a_j\) for all \(j=0,1,2,3\).

**Theorem.** Every one of the \(81\) possible four-letter words occurs for every prime \(p\equiv1\pmod3\) with \(p\ge571\), independent of the primitive root chosen. The complete list of primes \(p\equiv1\pmod3\) for which some word fails is

\[
\{7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 139, 151, 157, 163, 181, 193, 199, 211, 223, 229, 271, 277, 283, 307, 313, 331, 337, 367, 373, 379, 397, 457, 487, 499, 547\}.
\]

This universal threshold is sharp: at \(p=547\), taking \(g=2\), exactly \((0,2,2,0)\) is missing, whereas at the next eligible prime \(p=571\) all \(81\) words occur. The last prime failing the all-cubic word \((0,0,0,0)\) is \(379\); thus the final obstruction is a mixed-color word, not the all-cubic word. Changing the primitive root either preserves or simultaneously swaps colors \(1\) and \(2\), leaving completeness and the exceptional-prime list unchanged.

## Assumptions and scope

The field is the prime field \(\mathbb F_p\), not an arbitrary extension field. All four tested arguments must be nonzero, so \(x\notin\{0,-1,-2,-3\}\). The assertion is **completeness of the word set**, not an exact formula for each word's multiplicity. The analytic estimate covers every prime \(p\ge19000\), and the standalone finite certificate exhausts the required primes below that cutoff. The original source of 23 July 2020, Hu and Chen, carries primary mathematics classification \(11\) (specifically \(11A15\)).

## Proof

Write \(\omega=e^{2\pi i/3}\), and let \(\chi\) be the multiplicative character of order three normalized by \(\chi(g)=\omega\), extended by \(\chi(0)=0\). For \(a\in\{0,1,2\}\) set

\[
B_a(u)=1+\omega^{-a}\chi(u)+\omega^{-2a}\chi(u)^2.
\]

If \(u\ne0\), orthogonality of the cubic roots of unity gives \(B_a(u)=3\) if \(c_g(u)=a\), and \(B_a(u)=0\) otherwise. At zero, \(B_a(0)=1\). Thus, denoting by \(N_{\mathbf a}\) the exact number of valid starts for word \(\mathbf a\),

\[
81N_{\mathbf a}=\sum_{x\notin\{0,-1,-2,-3\}}\prod_{j=0}^3 B_{a_j}(x+j).
\]

Expand the product over **all** \(x\in\mathbb F_p\). There are \(3^4=81\) monomials. The constant monomial contributes \(p\); each of the \(8\) monomials whose support contains exactly one position has full sum zero by nontrivial character orthogonality. For any other monomial the summand has form \(\chi(f(x))\), where \(f(X)=\prod_{j\in J}(X+j)^{e_j}\), \(e_j\in\{1,2\}\), \(|J|=k\in\{2,3,4\}\). The roots \(-j\) are distinct modulo every eligible prime. The polynomial is not a cube; the standard Weil bound for multiplicative character sums gives

\[
\left|\sum_{x\bmod p}\chi(f(x))\right|\le(k-1)\sqrt p.
\]

All coefficients in the expansion have modulus one, and exactly \(\binom4k2^k\) monomials have support size \(k\). Hence the full-field product sum differs from \(p\) in absolute value by at most

\[
\sum_{k=2}^4\binom4k 2^k(k-1)\sqrt p=(24+64+48)\sqrt p=136\sqrt p.
\]

The four excluded starts are distinct (since \(p\ge7\)). At each excluded start, one factor \(B_a(0)=1\) and the remaining three factors are each either zero or three, so the excluded contribution is between \(0\) and \(4\cdot3^3=108\). Consequently the **uniform** estimate

\[
\boxed{81N_{\mathbf a}\ge p-136\sqrt p-108}
\]

holds for every word. The right side is positive at \(p=19000\) and strictly increasing for \(p\ge19000\), proving that every word occurs for every eligible prime in this entire infinite range.

For \(7\le p<19000\), the file `verify.py` sieves **all** primes \(p\equiv1\pmod3\), constructs the smallest primitive root \(g\), labels each nonzero element by its discrete-log exponent modulo three, and visits every permitted start \(x=1,\ldots,p-4\) (a complete enumeration modulo \(p\) avoiding the four zero arguments). It records an \(81\)-bit spectrum. The computation finds \(1072\) eligible primes in this range, exactly \(39\) with incomplete spectra, and the full exception set printed above. For every prime, the script independently rederives the same color labeling by Euler's criterion \(u^{(p-1)/3}\in\{1,\chi(g),\chi(g)^2\}\); at seven selected primes it also directly constructs cubic-power sets and their two cosets. The two exhaustive methods agree, including the sole absent word at \(547\). Combining the exhaustive finite range with the uniform infinite bound proves the theorem.

## Verification

Run `python3 verify.py` with standard Python (no packages, network, or external files). Expected concluding lines include `cubic_coset_primes_under_19000 1072`, `complete 1033 incomplete 39`, `boundary 547 generator 2 missing [(0, 2, 2, 0)]`, `boundary 571 generator 3 missing []`, and `All finite checks PASS`. The finite computation is exhaustive for all primes below \(19000\), not a random sample. Its scope does **not** substitute for the Weil argument for arbitrarily large primes. The source code additionally checks that \(19000-136\sqrt{19000}-108>0\).

## Relationship to prior work

Lehmer, Lehmer, Mills and Selfridge (1962) classify primes without **three consecutive cubic residues**, which concerns one all-zero word of *length three*, not all \(81\) words of *length four*. Hu and Chen (2020) derive character-sum formulas for cubic residue conditions involving \(a+a^{-1}\) and \(a-a^{-1}\); Yuan and Zhang (2022 online) similarly study inverse-related cubic-residue conditions. The published theorem "Sharp universal completeness threshold for three consecutive cubic-residue coset colors" covers the complete **length-three, 27-word** spectrum with threshold \(307\); it does not imply this four-coordinate, 81-word result. The published "Sharp universal threshold for all 256 consecutive quartic-coset quadruples" has four positions but studies **fourth-power cosets**, not cubic-power cosets. The use of character indicators and the Weil estimate is classical; what is asserted here is the exact new 81-word exception set and cutoff, subject to the literature-coverage limitations below.

## Limitations

No assertion is made about extension fields, exact per-word multiplicities, or optimality of the analytic \(19000\) cutoff. The sharp \(571\) result requires the finite exhaustive certificate; the simple Weil estimate alone is insufficient for it. The prior-work search cannot exclude unpublished, unindexed, or inaccessible equivalent classifications. A potentially related paper, *Cubic residues and their new distributive properties* (DOI: 10.1007/s13226-024-00540-4), could not be fully inspected; available abstract-level information suggests a different class of transformations, but cannot establish noncoverage. Independent mathematical audit has not yet occurred.

## References

1. Hu Jiayuan and Chen Zhuoyu, *On distribution properties of cubic residues*, AIMS Mathematics **5** (2020), 6051–6060, published 2020-07-23, DOI: 10.3934/math.2020388. https://www.aimspress.com/aimspress-data/math/2020/6/PDF/math-05-06-388.pdf
2. D. H. Lehmer, E. Lehmer, W. H. Mills and J. L. Selfridge, *Machine Proof of a Theorem on Cubic Residues*, Mathematics of Computation **16** (1962), 407–415, DOI: 10.1090/S0025-5718-1962-0162379-2. https://www.cs.umd.edu/~gasarch/TOPICS/res/llms.pdf
3. Xiaodan Yuan and Wenpeng Zhang, *On cubic residues and related problems*, published online 2022-08-02, Indian J. Pure Appl. Math. **54** (2023), 806–815, DOI: 10.1007/s13226-022-00299-6. https://insa.nic.in/writereaddata/UpLoadedFiles/IJPAM/Vol54_2023_3_ART17.pdf
4. *Sharp universal completeness threshold for three consecutive cubic-residue coset colors*, published research result, https://github.com/published-finding corpus/2026
5. *Sharp universal threshold for all 256 consecutive quartic-coset quadruples*, published research result, https://github.com/published-finding corpus/2026
