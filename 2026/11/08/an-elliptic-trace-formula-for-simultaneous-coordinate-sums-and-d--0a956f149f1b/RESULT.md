# An elliptic-trace formula for simultaneous coordinate sums and differences on odd modular hyperbolas

## Finding
For an odd integer \(m\ge3\), let \(U_m=(\mathbb Z/m\mathbb Z)^\times\) and define the two **coordinate images** of the modular hyperbola \(xy\equiv1\pmod m\) by
\[
S_m=\{x+x^{-1}:x\in U_m\},\qquad D_m=\{x-x^{-1}:x\in U_m\}.
\]
Here each set consists of residue classes modulo \(m\); the symbol \(x^{-1}\) denotes multiplicative inverse. The intersection measures which scalar residue can be both a coordinate sum and a coordinate difference, possibly at different hyperbola points.

For an odd prime \(p\), use the Legendre symbol \(\chi_p(t)=(\frac{t}{p})\), with \(\chi_p(0)=0\), and put
\[
\varepsilon_p=\chi_p(2),\qquad \delta_p=\mathbf 1_{p\equiv1\pmod4},\qquad
 a_p=-\sum_{t\in\mathbb F_p}\chi_p(t^3-t).
\]
The integer \(a_p\) is the Frobenius trace of the elliptic curve \(E:y^2=x^3-x\), so \(\#E(\mathbb F_p)=p+1-a_p\). Define
\[
G_p=\frac{p-5-2\delta_p-2(1+\delta_p)\varepsilon_p-a_p}{4},\qquad
Q_{p,k}=1+\frac{p-1}{2}\sum_{j=1}^{\lfloor(k-1)/2\rfloor}p^{k-2j-1}.
\]
Empty sums are zero. Then \(G_p\) is a nonnegative integer, and **for every** \(k\ge1\),
\[
\boxed{|S_{p^k}\cap D_{p^k}|=p^{k-1}G_p+(1+\delta_p)(1+\varepsilon_p)Q_{p,k}.}
\]
For arbitrary odd \(m\ge3\), the Chinese remainder theorem gives the complete multiplicative count
\[
\boxed{|S_m\cap D_m|=\prod_{p^k\parallel m}|S_{p^k}\cap D_{p^k}|.}
\]
In particular,
\[
\boxed{S_m\cap D_m=\varnothing\quad\Longleftrightarrow\quad3\mid m.}
\]
These are one linked classification of a single natural intersection invariant, not separate research claims.

## Assumptions and scope
All moduli are odd positive integers \(m\ge3\). For local factors, \(p\ge3\) is a prime and \(k\ge1\) is an integer. The Legendre character convention includes the value zero; integer coefficients and exponents in the local formula are exact. No asymptotics, conjectural prime distribution, or unevaluated infinite limits are needed. The formula is effective using the finite character sum defining \(a_p\).

## Proof
**1. Discriminant equivalence.** Since \(2\) is a unit modulo odd \(p^k\), the polynomial \(X^2-sX+1\) has a root modulo \(p^k\) exactly when its discriminant \(s^2-4\) has a square root modulo \(p^k\). Every such root is a unit because the constant term is \(1\). The same argument for \(X^2-sX-1\) shows
\[
 s\in S_{p^k}\cap D_{p^k}\iff
s^2-4\text{ and }s^2+4\text{ are both squares modulo }p^k,
\]
where zero is a square.

**2. Ordinary residues modulo the prime.** Write \(L(s)=s^2-4\) and \(R(s)=s^2+4\). Their roots never coincide in odd characteristic. There are exactly two roots of \(L\), and exactly \(2\delta_p\) roots of \(R\). On the complement of these \(2+2\delta_p\) exceptional residues, both values are nonzero, so exactly the residues having \(\chi_p(L)=\chi_p(R)=1\) qualify. Their number is
\[
G_p=\frac14\sum_{\substack{s\bmod p\\L(s)R(s)\ne0}}(1+\chi_p(L(s)))(1+\chi_p(R(s))).
\]
For each nonzero \(c\in\mathbb F_p\), the standard difference-of-squares count proves \(\sum_s\chi_p(s^2-c)=-1\): the equation \(v^2=s^2-c\) is equivalent to \((s-v)(s+v)=c\) and has \(p-1\) solutions. At each root of \(L\), \(\chi_p(R)=\chi_p(8)=\varepsilon_p\); at each root of \(R\), available only when \(\delta_p=1\), \(\chi_p(L)=\chi_p(-8)=\varepsilon_p\). Finally,
\[
\begin{aligned}
\sum_s\chi_p(L(s)R(s))
 &=\sum_s\chi_p(s^4-16)\\
 &=\sum_{u\in\mathbb F_p}(1+\chi_p(u))\chi_p(u^2-16)\\
 &=-1+\sum_{v\in\mathbb F_p}\chi_p(v^3-v)\\
 &=-1-a_p.
\end{aligned}
\]
The substitution in the third line is \(u=4v\); its character factor is unchanged since \(4^3\) is a square. Expanding the preceding indicator sum, omitting the roots of \(L\) and \(R\), yields precisely
\[
4G_p=p-5-2\delta_p-2(1+\delta_p)\varepsilon_p-a_p.
\]
This proves both integrality and nonnegativity of \(G_p\) independently of the displayed quotient.

**3. Lifts to higher prime powers.** Every ordinary residue \(s\bmod p\) counted by \(G_p\) has all \(p^{k-1}\) lifts counted: over odd prime powers, units are squares if and only if their reductions modulo \(p\) are squares. For an exceptional residue \(s_0\bmod p\) with \(L(s_0)=0\), the other discriminant reduces to \(8\), so no lifts qualify when \(\varepsilon_p=-1\). If \(\varepsilon_p=1\), the other discriminant is a square for every lift. Because \(L'(s_0)=2s_0\) is a unit, Hensel's lemma gives a bijection from the \(p^{k-1}\) lifts of \(s_0\) to the multiples of \(p\) modulo \(p^k\), by the map \(s\mapsto L(s)\). Exactly \(Q_{p,k}\) multiples of \(p\) are squares: zero contributes one; a nonzero square divisible by \(p\) has valuation \(2j\) with \(1\le j\le\lfloor(k-1)/2\rfloor\) and there are \((p-1)p^{k-2j-1}/2\) possible residues for that valuation. Roots of \(R\) are treated identically, using \(R'(s_0)=2s_0\) and \(\chi_p(-8)=\varepsilon_p\) when \(\delta_p=1\). Thus the \(2+2\delta_p\) exceptional root classes each contribute \((1+\varepsilon_p)Q_{p,k}/2\), giving the announced local formula.

**4. Chinese remainder theorem.** Simultaneous squarehood of the two discriminants holds modulo \(m\) precisely when it holds modulo every prime-power factor. Residues and the two image sets factor as products under the Chinese remainder theorem; therefore their intersection counts multiply.

**5. Sharp emptiness criterion.** For \(p=3\), \(\varepsilon_p=-1\), \(\delta_p=0\), and \(a_p=0\) (the defining character sum cancels under \(t\mapsto-t\)); the formula gives zero for every \(k\). For every prime \(p\ge5\) at least one qualifying residue exists modulo \(p\): when \(p\equiv1\pmod4\), take \(s=0\), making both discriminants \(\pm4\) squares; when \(p\equiv7\pmod8\), take \(s=2\), making them \(0,8\) squares; when \(p\equiv3\pmod8\), necessarily \(p\ge11\), we have \(\delta_p=0\), \(\varepsilon_p=-1\), and \(a_p=0\), hence \(G_p=(p-3)/4>0\). Every such qualifying prime residue lifts to some qualifying residue modulo all \(p^k\) by Step 3, and the CRT proves the criterion.

## Verification
The accompanying `verify_joint_image.py` uses only Python's standard library. It independently constructs \(S_m\) and \(D_m\) by enumerating units and modular inverses, independently factors the modulus, computes the cubic character sum for each prime, and compares the exact cardinalities. On replay it reports `VERIFY_OK odd_moduli_3..1299=649 prime_powers=77 zero_iff_3_divides=PASS exact_count=PASS elliptic_trace_and_singular_lifts=PASS`. Among the small examples are \(|S_7\cap D_7|=2\), \(|S_{49}\cap D_{49}|=2\), \(|S_{343}\cap D_{343}|=8\), \(|S_{121}\cap D_{121}|=22\), and \(|S_{27}\cap D_{27}|=0\). All finite checks are corroborating evidence, not substitutes for the unrestricted proof.

## Relationship to prior work
Eichhorn, Khan, Stein, and Yankov (2009) and Bower, Evans, Luo, and Miller (arXiv:1212.2930v1, 2012) study the same modular-hyperbola coordinate sum and difference sets and determine their individual cardinalities, along with dominance ratios. In particular, Theorem 3.6 of the 2012 manuscript gives separate formulas for \(|S_{p^k}|\) and \(|D_{p^k}|\). Separate cardinalities do not imply the size of an intersection: that requires a joint quadratic-character correlation, here identified with the elliptic trace of \(y^2=x^3-x\), and separate handling of ramified prime-power lifts. The present result is a simultaneous-image classification, not a new proof of the individual size formulas. See the source-comparison limitations below.

## Limitations
This theorem covers odd moduli only; even moduli are not classified. The 2009 Eichhorn–Khan–Stein–Yankov primary full text could not be obtained despite public-source attempts; its content is therefore a material historical-priority risk, not certified to omit the intersection result. The 2012 full manuscript explicitly describes the 2009 contribution as separate cardinalities, and its own Theorem 3.6 and subsequent ratios likewise concern separate sets. No absolute priority or independent audit is claimed. The elliptic trace \(a_p\) is a finite sum rather than a single elementary expression independent of the prime. There is no asserted extension to arbitrary scaled hyperbolas \(xy\equiv a\) or to finite fields of non-prime order.

## References
- Dennis Eichhorn, Mizan R. Khan, Alan H. Stein, Christian L. Yankov, *Sums and Differences of the Coordinates of Points on Modular Hyperbolas*, in *Combinatorial Number Theory* (2009), DOI: 10.1515/9783110208504.17.
- Amanda Bower, Ron Evans, Victor Luo, Steven J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930v1 (first public version, 2012-12-12), especially Theorem 3.6 and Section 3.3; https://arxiv.org/pdf/1212.2930.
- Igor E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879v1 (first public version, 2011-03-15); background survey, https://arxiv.org/abs/1103.2879.
