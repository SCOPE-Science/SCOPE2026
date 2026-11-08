# Exact residue fibers of square-pyramidal numbers over all moduli

## Finding
For every integer \(n\ge0\), put \(S(n)=\sum_{j=1}^{n}j^2=n(n+1)(2n+1)/6\). For a positive modulus \(m\), let \(P(m)\) be the least positive period of \(S(n)\bmod m\), and define the fiber multiplicity
\[
 R_m(y)=\#\{0\le n<P(m):S(n)\equiv y\pmod m\}\quad (y\in\mathbb Z/m\mathbb Z).
\]
The exact least period and the number of values are
\[
 \boxed{P(m)=m\gcd(m,6)},\qquad
 \boxed{\#\{S(n)\bmod m:n\ge0\}=m\prod_{\substack{p\mid m\\p\ge5}}\frac{2p+\left(\frac{-3}{p}\right)}{3p}.}
\]
Here each \(p\) in the product is a distinct prime and \(\left(\frac{\cdot}{p}\right)\) is the Legendre symbol. This formula is an integer; for \(m=1\), both quantities are one.

The following explicit local histogram determines the *entire* multiplicity distribution, not just the number of values. For \(p=2\) or \(p=3\) and all \(k\ge1\), every target \(y\bmod p^k\) has exactly \(p\) representations in the least period \(p^{k+1}\).

For primes \(p\ge5\), put
\[
 \eta=\left(\frac{-3}{p}\right),\quad
 d=1+\left(\frac3p\right)\in\{0,2\},\quad
 u=\frac{p-\eta-3d}{6},\quad v=p-3u-2d,
\]
and, for \(1\le j\le\lfloor(k-1)/2\rfloor\), define
\[
 a_j=\frac{p-1}{2}p^{k-2j-1},\qquad A=\sum_{j=1}^{\lfloor(k-1)/2\rfloor}a_j.
\]
For \(r\ge1\), let \(H_{p,k}(r)=\#\{y\bmod p^k:R_{p^k}(y)=r\}\). The nonzero entries are exactly the following, with any coincident entries added (none coincide for \(p\ge5\)):
\[
\begin{aligned}
H_{p,k}(1)&=v p^{k-1}+d(p^{k-1}-1-A),\\
H_{p,k}(3)&=u p^{k-1},\\
H_{p,k}(1+2p^j)&=d a_j\quad(1\le j\le\lfloor(k-1)/2\rfloor),\\
H_{p,k}(1+p^{\lfloor k/2\rfloor})&=d.
\end{aligned}
\]
For all other positive integers \(r\), the histogram count \(H_{p,k}(r)\) is zero. The number of residues with \(R_{p^k}(y)=0\) is \(p^k-\#\operatorname{im}(S)\). In particular the size of the value set is \(p^{k-1}(2p+\eta)/3\). The top exceptional multiplicity \(1+p^{\lfloor k/2\rfloor}\) occurs at exactly two targets if \(3\) is a quadratic residue modulo \(p\), and never otherwise.

For coprime moduli \(a,b\), the Chinese remainder theorem gives \(R_{ab}(y)=R_a(y\bmod a)R_b(y\bmod b)\); thus the local rules are a complete classification for every \(m\). For example, modulo \(30\) there are exactly \(18\) represented residues; twelve have multiplicity \(6\) and six have multiplicity \(18\), in the least period \(180\).

## Assumptions and scope
Every modulus is a positive integer and every period is taken over all nonnegative indices, with the standard zero value \(S(0)=0\). The local odd-prime histogram concerns counts of residue targets (not counts of indices) indexed by fiber size. The result includes prime powers and composites; no unproved distributional assumption is made.

## Proof
**Periods at the small primes.** Direct subtraction of the cubic polynomial, for arbitrary integers \(n,h\), yields
\[
S(n+2h)-S(n)=h\frac{8h^2+12hn+6h+6n^2+6n+1}{3},
\]
\[
S(n+3h)-S(n)=h\frac{18h^2+18hn+9h+6n^2+6n+1}{2}.
\]
The displayed quotients are, respectively, odd integers and integers congruent to \(2\pmod3\). Consequently, for \(p\in\{2,3\}\), each map \(z\mapsto S(a+pz)\) for a fixed \(a\bmod p\) is an isometry on \(\mathbb Z_p\): it preserves the \(p\)-adic valuation of the difference of two inputs. A compatible isometry of this form maps onto all residues modulo \(p^k\): its reduction modulo \(p\) is a translation times a unit, and each solution lifts uniquely digit by digit. Thus each of the \(p\) index classes modulo \(p\) hits every residue once in a complete block of length \(p^{k+1}\). For minimality, \(S(n)\bmod2\), for \(n=0,1,2,3\), is \((0,1,1,0)\), of least period four, and \(S(n)\bmod3\), for \(n=0,\ldots,8\), is \((0,1,2,2,0,1,1,2,0)\), of least period nine. Any higher-level period must therefore be divisible by \(p\); applying the isometry to a shift divisible by \(p\) forces divisibility by \(p^{k+1}\). Hence the exact least periods are \(p^{k+1}\), and every fiber has size \(p\).

**Reduction at odd primes at least five.** The identity
\[
 24S(n)=(2n+1)^3-(2n+1)
\]
identifies the fibers modulo \(p^k\) with those of \(f(t)=t^3-t\), since both the change of variable and output scaling are bijections when \(p\ge5\). The least period is \(p^k\): if \(S(n+h)\equiv S(n)\pmod{p^k}\) for all \(n\), the second finite difference in \(n\) of the polynomial \(S(n+h)-S(n)\) is exactly \(2h\), forcing \(p^k\mid h\).

**Field fiber counts.** For \(p\ge5\), \(f(x)=f(y)\) if and only if \((x-y)(x^2+xy+y^2-1)=0\). The nonsingular conic \(x^2+xy+y^2=1\) has exactly \(p-\eta\) ordered solutions over \(\mathbb F_p\). Indeed, for fixed \(x\) its discriminant is \(4-3x^2\), so the number of \(y\) is \(1+\left(\frac{4-3x^2}{p}\right)\), and the standard quadratic-character sum gives \(\sum_x\left(\frac{4-3x^2}{p}\right)=-\eta\). Equivalently, this follows without invoking a character-sum theorem: counting solutions of \(z^2+3x^2=4\) gives \(p-1\) when \(-3\) is a square (factor into two distinct lines, then count solutions of a nonzero product), and \(p+1\) when \(-3\) is a nonsquare (the nonzero norm fiber of \(\mathbb F_{p^2}/\mathbb F_p\)). Exactly \(d=1+\left(\frac3p\right)\) of these conic solutions lie on the diagonal. The off-diagonal collision count is therefore \(p-\eta-d\). When \(d=2\), the two critical points of \(f\), satisfying \(3x^2=1\), give two distinct values with exactly two roots (one double and one simple); otherwise there are no two-root fibers. If \(u\) is the number of three-root fibers, then \(6u+2d=p-\eta-d\). Thus \(u=(p-\eta-3d)/6\), and the number of one-root fibers is \(v=p-3u-2d\). All these roots are simple except the doubled roots in the two critical fibers.

**Lifting noncritical fibers.** Every simple root modulo \(p\) lifts uniquely to a root of \(f(t)=y\bmod p^k\) for *each* lift of its target \(y\). Hence each one-root field value has \(p^{k-1}\) lifts of multiplicity one; each three-root field value has \(p^{k-1}\) lifts of multiplicity three. Each two-root field value also has one simple root modulo \(p\), hence every one of its target lifts is represented.

**Critical fibers.** Suppose \(d=2\). In \(\mathbb Z_p\), let \(c\) be either root of \(3c^2=1\). The critical value is \(f(c)\), while the simple root of the same field value is \(-2c\). For \(z\in p\mathbb Z_p\),
\[
f(c+z)=f(c)+z^2(3c+z).
\]
The unit \(1+z/(3c)\) has a unique square root congruent to one modulo \(p\). The change \(w=z\sqrt{1+z/(3c)}\) is a bijective isometry of \(p\mathbb Z_p\), so the critical-branch equation becomes
\[
 w^2\equiv\frac{y-f(c)}{3c}\pmod{p^k},\qquad w\equiv0\pmod p.
\]
Among the \(p^{k-1}\) possible target lifts of the fixed critical residue, exactly one has zero right-hand side modulo \(p^k\), contributing \(p^{\lfloor k/2\rfloor}\) critical roots. For each \(j\) with \(1\le j\le\lfloor(k-1)/2\rfloor\), exactly \(a_j=(p-1)p^{k-2j-1}/2\) targets have right-hand side of valuation \(2j\) and square unit, each contributing \(2p^j\) critical roots. The other \(p^{k-1}-1-A\) target lifts have no critical root. Add the one simple lift in every target, and multiply by \(d=2\) critical value classes. This proves every histogram entry. In particular all field values possess a simple preimage, so every such value has all \(p^{k-1}\) lifts; the image size is \(p^{k-1}(u+v+d)=p^{k-1}(2p+\eta)/3\).

**Composite moduli.** For prime powers \(p^k\Vert m\), the least periods \(p^{k+1}\) for \(p=2,3\) and \(p^k\) otherwise are pairwise coprime. Their least common multiple is \(m\gcd(m,6)\). The corresponding index classes and target residue classes both combine independently by CRT, yielding the product fiber formula and product image cardinality. Since each local period is least, the global one is least as well. The case \(m=1\) is immediate.

## Verification
Run the accompanying standard-library-only checker using `python3 verify.py`. It directly recomputes local fiber histograms for sixty-six prime powers (prime \(p\le43\), modulus at most \(60000\)); it enumerates \(377179\) local domain inputs. It also checks periods, minimum periods, and image cardinalities for every composite or prime modulus from \(1\) through \(300\), using \(113400\) exact integer evaluations per full least-period block. All tests use integer arithmetic. Finite checks are not a substitute for the unrestricted argument above.

## Relationship to prior work
Classical Dickson-polynomial value-set formulas over finite fields determine the *number* of field values of \(t^3-t\); this number is not claimed as a new standalone field-theoretic result. The archived work of Küçüksakallı (2015) discusses Chebyshev/Dickson value sets over finite fields and separately treats bivariate maps. The present statement distinguishes every prime-power residue-fiber size, incorporates the integer-valued small-characteristic branches, proves exact least periods, and combines the data across all moduli. Bremser and Gómez-Calderon (1991) studied Dickson-polynomial value sets and preimages over Galois rings, and may contain overlapping degree-three prime-power material. That full text was unavailable for comparison; historical-priority uncertainty remains for the prime-power portion.

## Limitations
This result does not determine fibers for arbitrary higher-degree power-sum polynomials or provide asymptotic analytic distribution bounds beyond the exact finite residue classifications. The 1991 Galois-ring paper's full theorem statements were unavailable, so a stronger historical novelty assertion is not justified. No independently audited mathematical certification is claimed.

## References
1. Ö. Küçüksakallı, *Value sets of bivariate Chebyshev maps over finite fields*, first made public 2 July 2015, arXiv:1507.00487, Section 1 and introduction, https://arxiv.org/html/1507.00487v2.
2. Ö. Küçüksakallı, *Value sets of Lattès maps over finite fields*, preliminary manuscript dated 20 April 2014, https://blog.metu.edu.tr/komer/files/2018/12/kucuksakalli-lattes.pdf.
3. P. S. Bremser and J. Gómez-Calderon, *Value sets of Dickson polynomials over Galois rings*, J. Number Theory 38 (1991), 240–250, DOI:10.1016/0022-314X(91)90087-R (abstract inspected; full text inaccessible).
4. S. Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226 (2023), https://arxiv.org/abs/2310.20226 (general bounds, not specific fiber histograms).
