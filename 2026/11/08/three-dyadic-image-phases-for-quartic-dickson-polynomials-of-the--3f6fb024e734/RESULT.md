# Three dyadic image phases for quartic Dickson polynomials of the second kind

## Finding

For an odd \(2\)-adic integer \(a\), put
\[
 f_a(X)=E_4(X,a)=X^4-3aX^2+a^2,\qquad b=-3a,
\]
and set \(c_1=a^2-3a+1\), \(c_2=a^2-12a+16\), and \(\mathcal S_2=\{u^2:u\in\mathbb Z_2\}\). The **complete value image** is
\[
 \boxed{f_a(\mathbb Z_2)=
 (c_1+8\mathbb Z_2)\ \cup\ (c_2+32\mathbb Z_2)\ \cup\ (a^2+16b\mathcal S_2).}
\]
The three displayed sets are pairwise disjoint when \(a\equiv1,5\pmod8\). When \(a\equiv3\pmod8\), the third set is contained in the first; when \(a\equiv7\pmod8\), the second is contained in the first. Consequently, normalized additive Haar measure is
\[
 \boxed{\mu(f_a(\mathbb Z_2))=
 \begin{cases}
  1/6,&a\equiv1,5\pmod8,\\
  5/32,&a\equiv3\pmod8,\\
  13/96,&a\equiv7\pmod8.
 \end{cases}}
\]
This is a parameter-dependent image-density trichotomy within a single nonpermuting Dickson polynomial family.

For \(k\ge3\), let \(R_a(k)\) be the number of values of \(f_a\) modulo \(2^k\), and let \(S(m)\) be the number of square residues modulo \(2^m\), with \(S(0)=1\). Then
\[
 \boxed{R_a(k)=2^{k-3}+
 \begin{cases}
  2^{\max(k-5,0)}+S(\max(k-4,0)),&a\equiv1,5\pmod8,\\
  2^{\max(k-5,0)},&a\equiv3\pmod8,\\
  S(\max(k-4,0)),&a\equiv7\pmod8.
 \end{cases}}
\]
For \(m\ge1\), the elementary closed form is \(S(m)=(2^{m-1}+4)/3\) for even \(m\), and \(S(m)=(2^{m-1}+5)/3\) for odd \(m\). At the two smaller levels, \(R_a(1)=1\) for every odd \(a\), and \(R_a(2)=2\) if \(a\equiv1\pmod4\), otherwise \(R_a(2)=1\).

There is also an **exact formula for every fiber**. For \(k\ge5\), write \(N_{a,k}(z)=\#\{x\bmod2^k:f_a(x)\equiv z\pmod{2^k}\}\), and \(Q_m(r)=\#\{u\bmod2^m:u^2\equiv r\pmod{2^m}\}\). Set \(m=k-4\). For any \(z\bmod2^k\),
\[
 \boxed{\begin{aligned}
 N_{a,k}(z)={}&4\mathbf1_{z\equiv c_1\ (8)}+8\mathbf1_{z\equiv c_2\ (32)}\\
 &+4\mathbf1_{z\equiv a^2\ (16)}Q_m\left(b^{-1}\frac{z-a^2}{16}\bmod2^m\right).
 \end{aligned}}
\]
The last term is interpreted as zero unless the displayed divisibility condition holds. The inverse \(b^{-1}\) exists because \(a\) is odd. Overlapping branches contribute additively, and this formula covers all targets, including those not attained.

## Assumptions and scope

The parameter \(a\) is arbitrary in \(\mathbb Z_2^\times\), or an arbitrary odd integer when working modulo powers of two. The exact image statement concerns \(\mathbb Z_2\); the finite image counts concern all exponents \(k\ge1\), and the stated target-fiber formula concerns all \(k\ge5\). The polynomial is the fourth **second-kind** Dickson polynomial, defined by \(E_0(X,a)=1\), \(E_1(X,a)=X\), and \(E_{n+2}(X,a)=XE_{n+1}(X,a)-aE_n(X,a)\).

## Proof

**1. Unit-square lemma and two regular branches.** The squares of odd \(2\)-adic integers are precisely \(1+8\mathbb Z_2\); for any \(k\ge3\), each such residue modulo \(2^k\) has exactly four square roots modulo \(2^k\). Put \(h_a(Y)=Y^2-3aY+a^2\). For \(Y,Z\) of the same parity,
\[
 h_a(Y)-h_a(Z)=(Y-Z)(Y+Z-3a).
\]
The second factor is odd, so \(h_a\) preserves \(2\)-adic distances on any fixed-parity residue ball and maps each such ball bijectively onto its image ball (finite-level injectivity and cardinality give surjectivity). If \(x\) is odd, \(x^2\) ranges over \(1+8\mathbb Z_2\), and therefore \(f_a(x)\) ranges exactly over \(c_1+8\mathbb Z_2\). If \(x=2t\) with \(t\) odd, then \(x^2\) ranges over \(4+32\mathbb Z_2\), so \(f_a(x)\) ranges exactly over \(c_2+32\mathbb Z_2\).

**2. Singular square branch.** If \(x=4s\), then
\[
 f_a(4s)=a^2+16b s^2\left(1+\frac{16s^2}{b}\right).
\]
Because \(1+16s^2/b\in1+16\mathbb Z_2\), it has a uniquely specified square root \(u(s)\in1+8\mathbb Z_2\). This follows, for example, by applying the elementary isometry \(v\mapsto v+4v^2\) to \((1+8v)^2=1+16(v+4v^2)\). Define \(g(s)=s u(s)\). For distinct \(s,t\),
\[
 u(s)-u(t)=\frac{16(s-t)(s+t)}{b(u(s)+u(t))},
\]
where \(u(s)+u(t)\) has valuation one. Therefore the quotient \((g(s)-g(t))/(s-t)\) is an odd \(2\)-adic integer: it equals \(u(s)\) plus a multiple of eight. Thus \(g\) is a \(2\)-adic isometry. Modulo each \(2^j\) it induces an injection, hence a permutation, so it is surjective on \(\mathbb Z_2\). Consequently \(f_a(4\mathbb Z_2)=a^2+16b\mathcal S_2\), proving the exact image union.

**3. Branch overlap.** Modulo eight, the respective three images lie in the classes \(2-3a\), \(5\), and \(1\). For \(a\equiv1,5\pmod8\), these classes are all different. For \(a\equiv3\pmod8\), the third image lies in the full first ball \(1+8\mathbb Z_2\); for \(a\equiv7\pmod8\), the second image lies in the full first ball \(5+8\mathbb Z_2\). All other pairs are disjoint. This proves the three cases without relying on numerical evidence.

**4. Image size and measure.** The first two branch balls have Haar measures \(1/8\) and \(1/32\). The unit squares have measure \(1/8\); scaling by successive powers of four and adding the measure-zero square zero shows \(\mu(\mathcal S_2)=\sum_{j\ge0}4^{-j}/8=1/6\). Thus the third branch has measure \(1/(16\cdot6)=1/96\). The overlap classification gives all stated measures. The number of residues of the first branch modulo \(2^k\) is \(2^{k-3}\) for \(k\ge3\), of the second is \(2^{\max(k-5,0)}\), and of the third is \(S(\max(k-4,0))\). The formula for \(S\) follows from \(S(m)=2^{m-3}+S(m-2)\) for \(m\ge3\), with \(S(1)=S(2)=2\). The overlap classification proves the image-size formulas; reduction modulo two and four gives the remaining levels.

**5. Every representation fiber.** For \(k\ge5\), a target in the first branch has exactly four odd preimages: \(h_a\) is an isometry on \(1+8\mathbb Z_2\), and each odd square residue has four square roots modulo \(2^k\). A target in the second branch has eight preimages congruent to two modulo four: there are \(2^{k-2}\) such inputs and \(2^{k-5}\) values, with equal fiber sizes by the unit-square property and isometry. Finally, writing \(x=4s\), the value condition is \(g(s)^2\equiv b^{-1}(z-a^2)/16\pmod{2^{k-4}}\). The isometry \(g\) permutes all residues modulo \(2^{k-4}\), and each such residue has exactly four lifts of \(s\) modulo \(2^{k-2}\). Its contribution is therefore \(4Q_{k-4}\), proving the displayed exact fiber formula.

## Verification

The accompanying standard-library Python program `verify_e4.py` exhaustively enumerates each input and each output class modulo \(2^k\), for every \(5\le k\le13\) and every odd parameter \(1\le a\le31\). It independently constructs square-root multiplicities, checks the complete target-fiber formula, and checks the parameter-dependent image-size formulas. Successful execution prints `VERIFY_OK targets=261632 k=5..13 odd_parameters=1..31`. These finite checks corroborate the proof but do not establish the unrestricted theorem by themselves.

## Relationship to prior work

Qu and Ding classified *when* the second-kind Dickson polynomials permute \(\mathbb Z/2^k\mathbb Z\), in particular their 2014 Theorem 3.2. That result treats the yes/no permutation property; it does not give the full image or target-fiber multiplicities of the nonpermuting quartic, nor the three parameter-dependent Haar densities. Fan and Liao analyzed the dynamical decomposition of the classical first-kind Chebyshev polynomials \(T_n\) on \(\mathbb Z_2\); that concerns a different polynomial family and iteration, not the stated noniterated value-image classification. The underlying unit-square characterization is classical and is not claimed as new. No claim of exhaustive historical priority is made.

## Limitations

Only degree four and odd parameters are covered. No general result for the entire Dickson sequence, nonunit parameters, or odd-prime moduli is asserted. Independent specialist assessment of historical priority has not been performed. The fiber formula is given for \(k\ge5\); the image-size formulas include all positive \(k\).

## References

1. Longjiang Qu and Cunsheng Ding, *Dickson Polynomials of the Second Kind that Permute \(\mathbb Z_m\)*, SIAM Journal on Discrete Mathematics 28 (2014), 722–735, especially Theorem 3.2. DOI: `10.1137/130942589`. Author-posted text: `https://cse.hkust.edu.hk/faculty/cding/JOURNALS/siamdm141.pdf`.
2. Shilei Fan and Lingmin Liao, *Dynamics of Chebyshev Polynomials on \(\mathbb Z_2\)*, arXiv:`1511.03529` (first posted 2015-11-11). This covers first-kind Chebyshev dynamics, not this image question.
