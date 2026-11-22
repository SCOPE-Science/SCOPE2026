# Complete quartic cyclotomic coefficient-weight spectrum over \(\mathbb F_8\)

## Finding

Let \(\mathbb F_8=\mathbb F_2[u]/(u^3+u+1)\), and let \(\Phi_n(X)\) be the \(n\)-th cyclotomic polynomial reduced over this field. For each positive \(n\) with \(\operatorname{ord}_n(8)=4\), write \(N_j(n)\) for the number of **distinct monic irreducible quartic factors** of \(\Phi_n\) with exactly \(j\) nonzero coefficients. The entire spectrum is:

| \(n\) | \(N_3(n)\) | \(N_4(n)\) | \(N_5(n)\) |
|---:|---:|---:|---:|
| 5 | 0 | 0 | 1 |
| 13 | 0 | 0 | 3 |
| 15 | 2 | 0 | 0 |
| 35 | 0 | 0 | 6 |
| 39 | 0 | 0 | 6 |
| 45 | 0 | 0 | 6 |
| 65 | 0 | 0 | 12 |
| 91 | 0 | 0 | 18 |
| 105 | 12 | 0 | 0 |
| 117 | 0 | 6 | 12 |
| 195 | 0 | 6 | 18 |
| 273 | 0 | 0 | 36 |
| 315 | 0 | 0 | 36 |
| 455 | 0 | 0 | 72 |
| 585 | 6 | 24 | 42 |
| 819 | 0 | 36 | 72 |
| 1365 | 0 | 36 | 108 |
| 4095 | 36 | 144 | 252 |

These are all eighteen possible quartic cyclotomic layers. The unique all-trinomial layers are \(n=15\) and \(n=105\). The only mixed layers containing trinomials are \(n=585\) and \(n=4095\); both have

\[
N_3(n):N_4(n):N_5(n)=1:4:7,
\]

so their exact trinomial fraction is \(1/12\). In particular, in this first field where genuinely mixed quartic layers contain trinomials, the proportion can be substantially smaller than the general \(1/2\) upper bound of Zhu and Wu (Theorem 8.4). Exactly \(56\) of the \(1008\) monic irreducible quartics over \(\mathbb F_8\) are trinomials.

## Assumptions and scope

The coefficient weight of \(\sum_j c_j X^j\) means the number of indices with \(c_j\ne0\). A *cyclotomic layer of degree four* means \(\operatorname{ord}_n(8)=4\), equivalently all irreducible factors of \(\Phi_n\) have degree four. The multiplicative order is defined for positive \(n\) coprime to \(8\). All counts are exact, finite, and over the stated field; no limiting inference or extension to arbitrary \(q\) is claimed.

Since \(8^4-1=4095=3^2\cdot5\cdot7\cdot13\), every such \(n\) divides \(4095\). The orders of \(8\) modulo the prime-power factors are \(2\) modulo \(3\) and \(9\), \(4\) modulo \(5\) and \(13\), and \(1\) modulo \(7\). Thus \(\operatorname{ord}_n(8)=4\) exactly for the eighteen divisors of \(4095\) divisible by \(5\) or \(13\), and no others. An irreducible quartic in characteristic two with nonzero constant term has at least three nonzero coefficients: a binomial of degree four is a fourth power.

## Proof

**1. Structural enumeration of all trinomials.** A quartic with nonzero constant and exactly three terms can be irreducible only with its middle term of degree one or three: \(X^4+A X^2+B\) is a square. Reciprocal monic normalization pairs the first and third choices bijectively, preserving root order and weight. For \(A,B\ne0\), the cube map is a permutation of \(\mathbb F_8^*\); write uniquely \(A=c^3\), \(B=c^4 t\). Scaling \(X=cY\) reduces the polynomial to \(Y^4+Y+t\). The polynomial is irreducible precisely when \(\operatorname{Tr}_{\mathbb F_8}/{\mathbb F_2}(t)=1\), by the trace-zero image of \(Y\mapsto Y^4+Y\) and the corresponding degree-two-extension trace obstruction (equivalently, Zhu–Wu Proposition 8.5). In the chosen field, this gives \(t\in\{1,u+1,(u+1)^2,(u+1)^4\}\).

For \(t=1\), the normalized polynomial \(Y^4+Y+1\) has root order \(15\); multiplying a root by \(c\in\mathbb F_8^*\), whose order divides \(7\), leaves order \(15\) if \(c=1\), and gives \(105\) otherwise. Together with reciprocity the trinomial counts are \(2\) and \(12\).

The three nonunit trace-one parameters are Frobenius conjugate. Choose \(t=u+1\) and \(c_0=t^{-2}\), for which \(c_0^4t=1\) and \(c_0^3=t\). The corresponding polynomial is \(F(X)=X^4+(u+1)X+1\). Direct arithmetic modulo \(F\) gives

\[
X^{585}\equiv1\pmod F,\qquad
X^{585/p}\not\equiv1\pmod F\quad(p=3,5,13),
\]

so each root of \(F\) has multiplicative order exactly \(585\). These tests are reproducible by `verify.py`; over the \(u^3+u+1\) basis the respective nonunit remainder vectors in increasing polynomial degree are \([4,5,7]\), \([7,1,4,6]\), and \([4,7,6,4]\). The other six scalings \(c/c_0\) have order \(7\), coprime to \(585\), and give root order \(4095\). The three Frobenius-conjugate parameters and reciprocal pairing therefore give exactly \(6\) trinomials at order \(585\) and \(36\) at order \(4095\). There are none at other quartic orders.

**2. Certified exhaustive distribution of four- and five-term factors.** Every monic irreducible quartic \(f\) has a nonzero constant and divides \(X^{4095}-1\). The polynomial is irreducible if and only if \(\gcd(f,X^{64}-X)=1\), since every proper factorization of a degree-four polynomial has an irreducible factor of degree one or two, and all such factors divide \(X^{64}-X\). Enumerate exactly the \(7\cdot 8^3=3584\) monic quartics with nonzero constant, retain those satisfying the gcd test, determine each root order by starting at \(4095\) and repeatedly dividing by \(3,5,7,13\) whenever \(X^{m/p}\equiv1\pmod f\), and increment the tuple indexed by root order and coefficient weight. This yields exactly the eighteen rows above.

An independent exhaustive method uses \(K=\mathbb F_8[z]/(z^4+(u+1)z+1)\), a field by the preceding irreducibility criterion, and \(\gamma=uz\). Modular exponentiation verifies that \(\gamma\) has order \(4095\) (powers \(4095/p\) are nonidentity for \(p\in\{3,5,7,13\}\)). Enumerating all \(4095\) exponents modulo \(4095\) into Frobenius orbits under multiplication by \(8\), each size-four orbit contributes the minimal polynomial \(\prod_{i=0}^3 (X-\gamma^{8^i k})\), of root order \(4095/\gcd(4095,k)\). Reading its five coefficients produces the same table. The two methods use different ambient representations and irreducibility/weight computations; both cover the complete finite search spaces.

**3. Exhaustiveness checks.** Summing every row gives \((8^4-8^2)/4=1008\), the standard number of monic irreducible quartics. The sum of the trinomial column is \(56=8(8-1)\), agreeing with the independent aggregate formula in Zhu–Wu Proposition 8.5. For each order the row sum also equals \(\varphi(n)/4\).

## Verification

Run `python3 verify.py` in any Python 3 environment; no third-party package is used. The script reconstructs arithmetic in \(\mathbb F_8\) from the irreducible binary polynomial \(u^3+u+1\), checks the quartic irreducibility predicate via polynomial gcd and modular exponentiation, then independently generates a primitive element of \(\mathbb F_{8^4}\) and reconstructs all quartic Frobenius-minimal polynomials. Both routes are required to match the embedded table. Executing the attached checker produced `PASS: two independent full quartic enumerations; 1008 factors in 18 orders`. This is a complete finite certificate, not statistical sampling or a numerical extrapolation.

## Relationship to prior work

Zhu and Wu, *Cyclotomic polynomials with trinomial irreducible factors over finite fields* (first publicly submitted 31 October 2026), characterize **all-trinomial** layers, show that mixed quartic layers have at most half of their factors trinomial (Theorem 8.4), and count the total number of quartic trinomials (Proposition 8.5). Those results constrain but do not specify the **separate full three-weight histograms for all eighteen \(\mathbb F_8\) quartic orders**, nor the joint \(1:4:7\) ratios in the two mixed trinomial-bearing layers. Cheng's corrected characteristic-two global \(3\)-sparsity classification concerns whether **every** factor of \(X^n-1\) is sparse, rather than these partial proportions. Graner's general finite-field factorization formula covers the underlying irreducible factors for every \(q,n\), from which the current finite table is in principle calculable; it does not provide this coefficient-weight census or a direct sparsity-spectrum theorem. These are mathematical distinctions between statements, not claims of independent priority certification.

## Limitations

Only the exact field \(\mathbb F_8\) and degree-four cyclotomic layers are classified; this does not supply a general formula for \(N_j(n;q)\) for all prime powers. The finite enumeration is complete for the stated field but depends on the provided executable arithmetic certificate, whose operations and search ranges are fully specified above. General finite-field factorization results could make the counts derivable by specialization, so prior implicit calculations remain an originality risk. No independent external mathematical audit is claimed.

## References

- Li Zhu and Hongfeng Wu, *Cyclotomic polynomials with trinomial irreducible factors over finite fields*, arXiv:2611.00647, first public submission 2026-10-31; version 2 dated 2026-11-03, https://arxiv.org/html/2611.00647v2 (Theorem 8.4 and Proposition 8.5).
- Kaimin Cheng, *The \(3\)-sparsity of \(X^n-1\) over finite fields, II*, corrected version arXiv:2507.10779v2, https://arxiv.org/html/2507.10779v2.
- Anna-Maurin Graner, *Closed formulas for the factorization of \(X^n-1\), the \(n\)-th cyclotomic polynomial, \(X^n-a\) and \(f(X^n)\) over a finite field for arbitrary positive integers \(n\)*, arXiv:2306.11183v2, https://arxiv.org/html/2306.11183v2 (cyclotomic factorization theorem).
