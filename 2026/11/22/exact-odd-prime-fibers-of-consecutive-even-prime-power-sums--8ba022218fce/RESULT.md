# Exact odd-prime fibers of consecutive even prime-power sums

## Finding

For every **odd prime** \(p\) and integer \(s\ge1\), put \(d=2p^s\) and
\[
 f(x)=x^d+(x+1)^d,\qquad c=2^{1-d},\qquad A=2^{3-d}(d-1)\in\mathbb Z_p^\times.
\]
Here \(c\) and \(A\) are interpreted in the \(p\)-adic integers. Let \(B\) consist of one representative of each unordered pair \(\{a,-1-a\}\) of noncritical residues modulo \(p\). There are exactly \((p-1)/2\) such pairs. Then the **entire image** of \(f\) is the disjoint union
\[
 \boxed{ f(\mathbb Z_p)=\bigsqcup_{a\in B}\bigl(f(a)+p^{s+1}\mathbb Z_p\bigr)\ \sqcup\ \bigl(c+A p^{s+2}(\mathbb Z_p)^2\bigr). }
\]
The first components are full \(p\)-adic balls and the final component is a translated, scaled square image. The components are disjoint already modulo \(p\).

Write \(N_k(y)=\#\{x\bmod p^k:f(x)\equiv y\pmod{p^k}\}\) for \(k\ge1\), and let \(R_{p^n}(z)\) count square roots of \(z\) modulo \(p^n\), with the convention \(R_{1}(0)=1\). **Every target fiber is explicit:**

* For \(1\le k\le s+1\), each of the \((p-1)/2\) **individual regular targets** \(y\equiv f(a)\pmod{p^k}\), \(a\in B\), has \(N_k(y)=2p^{k-1}\); the sole critical class \(y\equiv c\pmod{p^k}\) has \(N_k(y)=p^{k-1}\); every other target has no preimages.
* For \(k\ge s+2\), a target in a regular ball has \(N_k(y)=2p^s\). For a target \(y\equiv c\pmod{p^{s+2}}\), put \(n=k-s-2\) and \(z\equiv A^{-1}(y-c)/p^{s+2}\pmod{p^n}\). Then \(N_k(y)=p^{s+1}R_{p^n}(z)\). All other fibers are empty.

Consequently, if \(Q_p(0)=1\) and for \(n\ge1\)
\[
 Q_p(n)=1+\frac{p-1}{2}\sum_{j=0}^{\lfloor(n-1)/2\rfloor}p^{n-2j-1},
\]
the exact number of attained residues at **every** finite level is
\[
 \boxed{\#f(\mathbb Z/p^k\mathbb Z)=\frac{p-1}{2}p^{\max(k-s-1,0)}+Q_p\bigl(\max(k-s-2,0)\bigr).}
\]
The limiting proportion of attained residue classes, equal to the Haar measure of the image, is
\[
 \boxed{\mu\bigl(f(\mathbb Z_p)\bigr)=\frac{p^{1-s}}{2(p+1)}.}
\]
For example, at \(p=3\), \(s=1\), the image occupies exactly \(1/8\) of \(\mathbb Z_3\).

## Assumptions and scope

Only odd primes and integer exponents \(s\ge1\) are covered. Inputs are **consecutive**, not two independent summation variables. Residues and fiber counts are taken in \(\mathbb Z/p^k\mathbb Z\); negative rational centers are interpreted with denominators invertible modulo every power of the odd prime. The symbol \((\mathbb Z_p)^2\) denotes the set of squares, including zero, not the Cartesian square.

## Proof

**Uniform residue-class isometries.** Use the identity
\[
 \binom dj=\frac d j\binom{d-1}{j-1}
\]
for \(j\ge1\), so that \(\nu_p\binom dj\ge s-\nu_p(j)\). Since \(j-\nu_p(j)\ge2\) for every \(j\ge2\), the expansion for any integer representative \(a\) of a class modulo \(p\) takes the form
\[
 f(a+pu)=f(a)+p^{s+1}\{2(2a+1)u+pE_a(u)\},\qquad E_a(u)\in\mathbb Z_p[u].
\]
Here we used \(d-1\equiv1\pmod{p-1}\), hence \(a^{d-1}+(a+1)^{d-1}\equiv2a+1\pmod p\). For \(a\not\equiv-1/2\pmod p\), the expression in braces is a bijective isometry of \(\mathbb Z_p\): its linear coefficient is a unit and the remainder is \(p\) times a 1-Lipschitz polynomial. Indeed, for each prescribed output the resulting fixed-point equation is contracting. Its image is therefore precisely \(f(a)+p^{s+1}\mathbb Z_p\), and its fibers modulo \(p^k\), once \(k\ge s+2\), have \(p^s\) points in this input class. The reflection identity \(f(-1-x)=f(x)\) pairs exactly the two classes \(a\) and \(-1-a\), with identical output ball.

**Disjointness.** For \(x\in\mathbb F_p\), Fermat's theorem gives
\[
 f(x)\equiv x^2+(x+1)^2=2(x+1/2)^2+1/2\pmod p.
\]
Since equality of two squares over a field forces equality up to sign, this identifies *exactly* the reflected input pair and one critical class \(x=-1/2\). Different regular output balls, and the critical output, are therefore disjoint modulo \(p\).

**The singular branch.** For \(x=-1/2+pu\), the even binomial expansion is
\[
 f(x)=c+2^{1-d}\sum_{j\ge2,\,j\,\mathrm{even}}\binom dj(2pu)^j.
\]
The quadratic coefficient is \(A p^{s+2}\); all higher even coefficients are divisible by \(p^{s+3}\). Thus, for some integral-coefficient polynomial \(E(u)\),
\[
 f(-1/2+pu)=c+A p^{s+2}u^2(1+pE(u)).
\]
The odd-prime binomial square root \(\sqrt{1+pE(u)}\) exists uniquely in \(1+p\mathbb Z_p\), is 1-Lipschitz in \(u\), and the map \(H(u)=u\sqrt{1+pE(u)}\) is a bijective isometry of \(\mathbb Z_p\), because \(H(u)=u+pJ(u)\) for a 1-Lipschitz \(J\). Consequently the critical branch is **exactly** \(c+A p^{s+2}(\mathbb Z_p)^2\). At level \(k\ge s+2\), the input parameter \(u\) runs through \(p^{k-1}\) residues but the output depends only on its residue modulo \(p^{k-s-2}\). Each root class therefore lifts \(p^{s+1}\) times, yielding the stated fiber formula. At smaller levels the whole input class collapses to one output residue.

**Image sizes and density.** The regular balls contribute \((p-1)p^{\max(k-s-1,0)}/2\) image residues modulo \(p^k\). The singular branch contributes \(Q_p(\max(k-s-2,0))\). To count squares modulo \(p^n\), separate zero from nonzero squares of valuation \(2j\), whose number is \((p-1)p^{n-2j-1}/2\); this proves the displayed finite sum. The measure of \((\mathbb Z_p)^2\) is \(p/[2(p+1)]\), by the geometric sum over even valuations. Multiplying by the scale \(p^{-(s+2)}\), adding the regular measure \((p-1)/(2p^{s+1})\), and simplifying gives \(p^{1-s}/[2(p+1)]\). Thus all finite and limiting claims follow.

## Verification

Execute `python3 CHECK.py` using Python 3's standard library only. It enumerates all input residue classes and compares **every** target's fiber with the formula, including target zero-fibers, for 30 distinct combinations: \((p,s)=(3,1),(3,2)\) through level 6; \((5,1),(5,2)\) through level 5; and \((7,1),(11,1)\) through level 4. All tests passed. These exhaustive finite checks corroborate but do not substitute for the uniform proof.

## Relationship to prior work

Arias, Borja and Anaya (2023, first public source 2023-08-28) count values of **unrestricted** sums of two \(d\)-th powers, with independent summation variables, modulo prime powers. Their Propositions 26 and 28 include relevant even powers, but their full two-dimensional sumsets and image counts do not classify the one-dimensional restricted line \(y=x+1\) or the target-by-target fibers proved here. Ding and Zieve (2023) study related consecutive-power and polynomial-value questions over **finite fields** rather than the complete odd-prime-power lifting of this family. Published comparisons about dyadic even-power sums and modular Waring lengths likewise do not imply this consecutive-input odd-prime result. The proof employs standard Hensel isometries and square-class counting; neither technique itself is claimed as novel.

## Limitations

The theorem covers neither the prime two nor exponents outside \(2p^s\). The formula describes modular/p-adic local solvability, not the number of integral solutions in a prescribed finite interval. General analytic normal-form machinery might imply parts of the local classification, and priority relative to unindexed or implicitly stronger literature has not been independently established. Finite verification tests only explicitly listed moduli; independent mathematical audit has not been performed.

## References

- F. Arias, J. Borja and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences 26 (2023), Article 23.8.1, first public 2023-08-28. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
- Z. Ding and M. E. Zieve, *On sums of powers of consecutive squares over finite fields, and sums of distinct values of polynomials*, arXiv:2309.14979v1, 2023-09-26. https://arxiv.org/html/2309.14979v1
- Standard facts used: finite-field square pairs; Hensel's lemma, convergence of \(p\)-adic binomial square roots, and prime-power quadratic residue counts.
