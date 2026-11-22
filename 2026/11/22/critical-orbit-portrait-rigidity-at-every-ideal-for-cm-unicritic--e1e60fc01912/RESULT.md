# Critical-orbit portrait rigidity at every ideal for CM unicritical polynomials

## Finding
For an integer \(d\ge 2\), let \(f_{d,c}(z)=z^d+c\), with \(c\) a postcritically finite (PCF) parameter belonging to some CM number field. Put \(K=\mathbb Q(c)\), and, for every nonzero proper integral ideal \(\mathfrak a\subset\mathcal O_K\), let \((m_{\mathfrak a},n_{\mathfrak a})\) be the exact preperiod and eventual period of the orbit of \(0\) under the reduction of \(f_{d,c}\) on \(\mathcal O_K/\mathfrak a\).

**Complete classification.** Reduction preserves the characteristic-zero critical-orbit type at every such ideal, with precisely the following exceptions (and no others):

| Degree and parameter | Exceptional ideal | Exact reduced type |
|---|---|---|
| \(d=2,\ c=-2\) | \((2)\subset\mathbb Z\) | \((0,1)\) |
| \(d=2,\ c=-2\) | \((4)\subset\mathbb Z\) | \((1,1)\) |
| \(d=2,\ c=i\) or \(c=-i\) | \((1+i)\subset\mathbb Z[i]\) | \((0,2)\) |
| \(d=2,\ c=i\) or \(c=-i\) | \((1+i)^2\subset\mathbb Z[i]\) | \((1,2)\) |
| \(d=2,\ c=i\) or \(c=-i\) | \((2c-1)\subset\mathbb Z[i]\) | \((2,1)\) |

In particular, **every** CM-PCF unicritical polynomial of degree at least three retains its exact critical preperiod and period under reduction modulo **every** nonzero proper ideal of \(\mathcal O_{\mathbb Q(c)}\), including ideals supported at wildly ramified primes and all prime powers. The quadratic exceptional set is exhaustive even for composite ideals. For \(c=\pm i\), the exceptional ideal \((2c-1)\) has absolute norm \(5\), and the two signs select the two conjugate primes above \(5\).

## Assumptions and scope
For an orbit \(a_0=0\), \(a_{r+1}=f_{d,c}(a_r)\) in a finite ring, its type \((m,n)\) means \(a_{m+n}=a_m\), the integers \(m\ge0\), \(n\ge1\) are minimal, and the \(m+n\) points \(a_0,\ldots,a_{m+n-1}\) are pairwise distinct. The same definition applies to the PCF characteristic-zero orbit. There is no claim about other starting points, generic positive-characteristic PCF parameters, behavior over arbitrary base extensions, or conjugacy-invariant marked portraits. The prime-power exponents are measured in the intrinsic ideal factorization of \(K=\mathbb Q(c)\), not in a larger ramified field.

The permitted characteristic-zero parameters are exactly those in Sano's classification [1]: for \(d=2\), \(c\in\{0,-1,-2,i,-i\}\); for \(d\ge3\), either \(c=0\), or \(c^{d-1}=-1\), or, when \(d\equiv0,1\pmod6\), \(c^{d-1}\) is a primitive cube root of unity. This external classification is an input; the new assertion is the **all-ideal specialization spectrum**, not a reproof of the CM classification.

## Proof
**1. Local portrait criterion.** Let the characteristic-zero critical orbit have type \((m,n)\), with orbit entries \(a_0,\ldots,a_{m+n-1}\). For any prime ideal \(\mathfrak p\subset\mathcal O_K\) and positive integer \(e\), the reduced orbit is the image of this finite list. Every equality between reduced orbit entries occurs precisely when \(a_r-a_s\in\mathfrak p^e\). Since the characteristic-zero relation \(a_{m+n}=a_m\) remains valid modulo any ideal, it suffices to compare the pairwise differences of the initial \(m+n\) entries to determine the exact reduced type; no unexamined longer orbit can occur.

**2. All degrees \(d\ge3\).** Put \(h=d-1\). If \(c=0\), then \(0\) is fixed. If \(c^h=-1\), then \(0\mapsto c\mapsto0\), and \(c\) is an algebraic unit. Hence \(0\) and \(c\) remain distinct modulo every nonzero proper ideal, giving \((0,2)\) everywhere.

For the remaining parameters, choose a primitive cube root \(\omega\) such that \(c^h=\omega\). Set \(u=1+\omega=-\omega^2\), a sixth root of unity. The initial orbit is \(0\mapsto c\mapsto uc\). Since \(u^6=1\) and \(c^d=\omega c\), the next image equals \(uc\) if \(d\equiv0\pmod6\) and equals \(0\) if \(d\equiv1\pmod6\). The pairwise differences among \(0,c,uc\) are, up to sign, \(c\), \(uc\), and \(\omega c\), all algebraic units. Thus the initial three points remain distinct modulo **every** nonzero proper ideal, and the exact types \((2,1)\) and \((0,3)\), respectively, are preserved without any restriction on the residue characteristic or ramification. This proves the entire infinite-degree portion.

**3. Quadratic rational parameters.** For \(c=0\), the orbit is fixed. For \(c=-1\), it is \(0,-1,0\); the sole nonzero difference is a unit, so \((0,2)\) survives every ideal of \(\mathbb Z\).

For \(c=-2\), the orbit is \(0,-2,2,2\). The three pairwise differences among \(0,-2,2\) have absolute values \(2,2,4\), so only the prime \(2\) can cause collisions. Modulo \(2\), the orbit is constant; modulo \(4\), the first and second nonzero entries coincide but remain distinct from \(0\); modulo \(2^e\) for \(e\ge3\), all three initial entries are distinct. Their exact types are \((0,1),(1,1),(2,1)\), respectively. Every odd prime-power reduction has the original \((2,1)\) type.

**4. Gaussian parameters.** For \(c=\pm i\), the orbit in \(\mathbb Z[i]\) is
\[
0\longmapsto c\longmapsto c-1\longmapsto-c\longmapsto c-1.
\]
The nonunit differences among its four distinct entries are exactly, up to signs, \(c-1\), \(2c\), and \(2c-1\); all other pairwise differences are units. In \(\mathbb Z[i]\), \(c-1\) has valuation \(1\) at \(\mathfrak p_2=(1+i)\), \(2c\) has valuation \(2\) at \(\mathfrak p_2\), and \(2c-1\) has valuation \(1\) at the unique prime \(\mathfrak p_5=(2c-1)\) of norm \(5\). None has other prime factors. Thus at \(\mathfrak p_2\), the first and third entries merge and the second and fourth merge, giving type \((0,2)\); at \(\mathfrak p_2^2\) only the second and fourth merge, giving \((1,2)\); at \(\mathfrak p_2^e\), \(e\ge3\), all four remain distinct, giving \((2,2)\). At \(\mathfrak p_5\), the third and fourth merge, giving \((2,1)\); at \(\mathfrak p_5^e\), \(e\ge2\), there is no collision, giving \((2,2)\). Every other prime-power modulus has type \((2,2)\).

**5. Arbitrary composite ideals.** Factor \(\mathfrak a=\prod_j\mathfrak p_j^{e_j}\). The Chinese remainder theorem identifies the orbit modulo \(\mathfrak a\) with the product of the local orbits. If its local exact types are \((m_j,n_j)\), its exact type is
\[
\left(\max_j m_j,\ \operatorname{lcm}_j n_j\right).
\]
Indeed, all components are periodic from the maximum preperiod onward, and no earlier iterate can start a cycle in a component having larger exact preperiod; the eventual period is exactly the least common multiple of the component periods.

For \(c=-2\), an odd-prime factor restores \((2,1)\), so the only exceptional **whole ideals** are exactly \((2)\) and \((4)\). For \(c=\pm i\), any factor with the ordinary type \((2,2)\) restores that type globally. If both of the distinct exceptional primes \(\mathfrak p_2\) and \(\mathfrak p_5\) occur in a modulus, the maximum of the preperiods is \(2\) and the least common multiple of the periods is \(2\), again restoring \((2,2)\). Equivalently and more directly, each proper ideal that identifies two distinct entries must divide the principal ideal generated by one of the three nonunit differences; their complete ideal-divisor lists are exactly \(\{\mathfrak p_2,\mathfrak p_2^2,\mathfrak p_5\}\). This also rules out all mixed ideals without an appeal to special-case enumeration. Therefore only the three single-prime exceptional ideals listed in the finding are possible. This completes the all-ideal proof.

## Verification
The companion self-contained Python 3 program `check_portraits.py` constructs initial critical orbits independently and identifies their exact types by divisibility of Gaussian-integer differences, rather than relying on the stated table. It passed **1,078** integer/Gaussian prime-power cases (rational primes through \(101\), exponents through \(7\)), **484** composite Gaussian-ideal cases, and **9,438** finite-prime-field instances from the higher-degree cyclotomic branches (degrees \(3\) through \(120\), primes up to \(97\)). Run with `python3 check_portraits.py`. These are finite consistency tests; the proof for all degrees and all ideals is the unit, valuation, and Chinese-remainder argument above.

## Relationship to prior work
Sano [1, Theorem 1.1, Proposition 3.4, Corollary 5.4] gives the complete **characteristic-zero** CM-PCF parameter list and orbit types; it does not classify their exact reductions over prime-power or composite-ideal quotient rings. Pink [2] studies finiteness and liftability of quadratic morphisms over fields of characteristic other than two; its field-valued liftability is not an ideal-power portrait table for a **fixed parameter**. Anderson–Manes–Tobin [3] study persistent bad reduction of polynomial maps as maps, a different invariant from the collision of an integral marked critical orbit under reduction. Existing published individual dynamical finite-ring studies treat other maps and full basins, not this simultaneous all-degree, all-ideal CM classification. The claim is only the stated arithmetic specialization refinement and does not claim the underlying complex classification as new.

## Limitations
The result concerns the critical **point** orbit in the canonical polynomial coordinates; after extending the base field the thresholds at ramified primes can change because ideal powers change, hence \(K=\mathbb Q(c)\) is essential. A polynomial can have good reduction as a map while its critical points collide after reduction; the two notions must not be confused. The result does not cover non-CM PCF parameters or the functional graph of all points in each finite ring. Unindexed literature or implicit specialized computations in broader arithmetic dynamics may contain overlapping all-ideal statements; external independent mathematical checking has not been performed.

## References
[1] K. Sano, *Postcritically Finite Unicritical Polynomials over CM Fields*, arXiv:2611.16354v1, first publicly posted 2026-11-12, https://arxiv.org/html/2611.16354v1 .

[2] R. Pink, *Finiteness and liftability of postcritically finite quadratic morphisms in arbitrary characteristic*, arXiv:1305.2841, 2013, https://arxiv.org/abs/1305.2841 .

[3] J. Anderson, M. Manes, B. Tobin, *Some Applications of Dynamical Belyi Polynomials*, arXiv:2109.03339, 2021; *La Matematica* 3 (2024), 891–906, https://arxiv.org/abs/2109.03339 .
