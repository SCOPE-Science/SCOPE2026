# Exact chord multiplicities and fourth Fourier moment of anisotropic circles over prime-power rings

## Finding
Fix any prime \(p\equiv3\pmod4\) and integer \(k\ge2\). Put \(q=p^k\), \(R=\mathbb Z/q\mathbb Z\), and
\[
C=\{(x,y)\in R^2:x^2+y^2=1\},\qquad m=|C|=p^{k-1}(p+1).
\]
For \(z\in R^2\), define the ordered additive-convolution coefficient
\[
r(z)=|\{(a,b)\in C^2:a+b=z\}|.
\]
The **entire chord-multiplicity histogram** follows from the following mutually disjoint target strata. Here \(Q(x,y)=x^2+y^2\), \(\nu(z)=\min(\nu_p(z_1),\nu_p(z_2),k)\), and \(\nu_p(0)=k\).

* At \(z=0\), there is exactly one target with \(r(z)=m\).
* For primitive \(z\), meaning \(\nu(z)=0\), put \(u=4Q(z)^{-1}-1\in R\). Exactly \(m\) primitive targets have \(u=0\), each with \(r(z)=p^{\lfloor k/2\rfloor}\). For each integer \(t\) satisfying \(0\le 2t<k\), exactly
  \[
  \frac{m(p-1)p^{k-2t-1}}2
  \]
  primitive targets have \(\nu_p(u)=2t\) and square leading unit, each with \(r(z)=2p^t\). Every other primitive target has \(r(z)=0\).
* For each integer \(v\) satisfying \(1\le v<k\), exactly
  \[
  \frac{(p^2-1)p^{2(k-v)-2}}2
  \]
  targets \(z\) with \(\nu(z)=v\) have \(r(z)=2p^v\); an equal number at that valuation have \(r(z)=0\).

These strata specify every target, including zero values, and the multiplicities of coincident values from different strata are added. In particular, with
\[
B_k=1+\frac{p-1}{2}\sum_{t=0}^{\lfloor(k-1)/2\rfloor}p^{k-2t-1},
\]
the exact sumset size is
\[
|C+C|=mB_k+\frac{p^{2k-2}+1}{2}.
\]
The additive energy and **complete unweighted two-frequency fourth Fourier moment** satisfy
\[
\boxed{\ E(C):=\sum_{z\in R^2}r(z)^2=3p^{2k-2}(p+1)\bigl(1+k(p-1)\bigr).\ }
\]
Writing \(\mathcal F_C(a,b)=\sum_{(x,y)\in C}\exp(2\pi i(ax+by)/q)\), one also has
\[
\frac1{q^2}\sum_{a,b\in R}|\mathcal F_C(a,b)|^4=3p^{2k-2}(p+1)\bigl(1+k(p-1)\bigr).
\]

## Assumptions and scope
The prime is odd with \(-1\) nonsquare modulo \(p\), and \(k\ge2\). All congruences, vector sums, and norms are taken in \(R\) unless a smaller quotient is specified. A primitive vector has at least one unit coordinate. Its norm is a unit because \(-1\) is nonsquare modulo \(p\). The Fourier sum is unweighted, with **unnormalized** summation on the circle and **normalized** frequency averaging by \(q^{-2}\). No assertion of a sharp extension-operator norm for arbitrary coefficients is made.

## Proof
**1. Size and smooth lifting.** Over \(\mathbb F_p\), \(x^2+y^2\) is the quadratic field norm, so every nonzero norm value has exactly \(p+1\) preimages. Each solution of \(x^2+y^2=a\), for unit \(a\), is smooth: at least one of the derivatives \(2x,2y\) is nonzero modulo \(p\). Each solution modulo \(p^h\) therefore has exactly \(p\) lifts with prescribed norm modulo \(p^{h+1}\). Inductively, each unit norm fiber over \(R\) has size \(m=p^{k-1}(p+1)\), and each circle point modulo \(p^h\) has exactly \(p^{k-h}\) lifts to \(C\).

**2. Primitive sums.** For an ordered pair \((a,b)\) of circle points with \(a+b=z\), set \(d=a-b\). Since \(2\) is invertible, \(a=(z+d)/2\) and \(b=(z-d)/2\). The two norm equations are equivalent to
\[
Q(z)+Q(d)=4,\qquad z\cdot d=0.
\]
For primitive \(z\), \(Q(z)\) is a unit, and the vectors \(z\), \(Jz=(-z_2,z_1)\) form a basis (determinant \(Q(z)\)). Thus \(z\cdot d=0\) if and only if \(d=hJz\) for a unique \(h\in R\). The norm condition becomes
\[
h^2=\frac4{Q(z)}-1=:u.
\]
Consequently \(r(z)\) is the number of square roots of \(u\) modulo \(p^k\). The map \(z\mapsto u\) on primitive vectors takes each \(u\) with \(1+u\) a unit exactly \(m\) times, by the constant unit-norm fiber count. The leading residue of \(-1\) is a nonsquare, so **every square value** \(u=h^2\) automatically satisfies \(1+u\) a unit. For \(u=0\), the root count is \(p^{\lfloor k/2\rfloor}\). For \(\nu_p(u)=2t<k\) and square leading unit, writing \(h=p^t w\) and using simple-root lifting gives \(2p^t\) roots. The number of such nonzero square values \(u\) is \((p-1)p^{k-2t-1}/2\). All other values have no roots. This proves every primitive stratum.

**3. Nonprimitive sums.** Let \(z=p^v w\) with \(1\le v<k\); the primitive vector \(w\) is defined modulo \(p^{k-v}\), and its norm is a unit. The equations \(Q(a)=Q(z-a)=1\) reduce to
\[
Q(a)=1,\qquad 2a\cdot w=p^vQ(w)\pmod{p^{k-v}}.
\]
Over \(R'=\mathbb Z/p^{k-v}\mathbb Z\), write uniquely \(a=\alpha w+\beta Jw\); the dot-product condition fixes \(\alpha=p^v/2\). The norm equation is
\[
\beta^2=Q(w)^{-1}-\frac{p^{2v}}4\pmod{p^{k-v}}.
\]
Its right side is a unit, with square leading residue exactly when \(Q(w)\) is a square modulo \(p\). It therefore has either two or zero roots in \(R'\). By smooth lifting, each such solution for \(a\) gives exactly \(p^v\) solutions modulo \(p^k\). Hence \(r(z)\) is respectively \(2p^v\) or \(0\). Among the \((p^2-1)p^{2(k-v)-2}\) primitive vectors \(w\) modulo \(p^{k-v}\), precisely half have square norm, because the norm map onto units has constant fibers and half of the units have square reduction. This proves both nonprimitive multiplicities. At \(z=0\), every \(a\in C\) contributes \((a,-a)\), so \(r(0)=m\).

**4. Sumset size.** The total number of square values in \(R\), including zero, is \(B_k\); every such value contributes \(m\) primitive targets. Summing the positive nonprimitive strata gives
\[
\frac{p^2-1}{2}\sum_{h=1}^{k-1}p^{2h-2}=\frac{p^{2k-2}-1}{2}.
\]
Adding the zero target proves the sumset formula.

**5. Energy.** Let \(N_k(u)=|\{h\in R:h^2=u\}|\). The primitive contribution to energy is \(m\sum_{u\in R}N_k(u)^2\): omitted \(u\equiv-1\pmod p\) have no roots. The sum counts ordered \((a,b)\) with \(a^2=b^2\). The invertible linear change \((a,b)\mapsto(a-b,a+b)\) reduces this to counting \(xy=0\) in \(R^2\). For \(x=0\) there are \(p^k\) choices; for each valuation \(0\le j<k\), the \((p-1)p^{k-j-1}\) choices of \(x\) of valuation \(j\) each permit \(p^j\) choices of \(y\). Therefore
\[
\sum_uN_k(u)^2=p^{k-1}\bigl(p+k(p-1)\bigr).
\]
The nonprimitive strata contribute
\[
\sum_{v=1}^{k-1}(2p^v)^2\frac{(p^2-1)p^{2(k-v)-2}}2=2(k-1)(p^2-1)p^{2k-2}.
\]
Including \(r(0)^2=m^2\) and simplifying gives exactly
\[
E(C)=m^2+mp^{k-1}\bigl(p+k(p-1)\bigr)+2(k-1)(p^2-1)p^{2k-2}
=3p^{2k-2}(p+1)\bigl(1+k(p-1)\bigr).
\]
Finally, orthogonality of all \(q^2\) additive characters of \(R^2\) identifies \(q^{-2}\sum|\mathcal F_C|^4\) with the number of quadruples \(a+b=c+d\) in \(C\), namely \(E(C)\).

## Verification
The included standalone standard-library script `verify.py` enumerates the actual circle and ordered pair sums, independently reconstructs their multiplicity histogram, compares it against every target stratum and the complete histogram, checks the energy and support cardinality, and verifies the square-root congruence formula on primitive targets. Run `python3 verify.py`. The explicitly tested moduli are \(3,9,27,81,7,49,11,121\). The script is a finite cross-check, not the all-prime all-exponent proof.

## Relationship to prior work
Iosevich and Koh (arXiv:0804.4505v1, 2008) analyze two-point sums on nondegenerate quadratic surfaces **over fields** in their proof of an \(L^2\to L^4\) bound (especially §4, Theorem 2). Carbery, Stones and Wright (2008) give finite-field averaging estimates. Neither inspected work presents the present local-ring valuation-stratified histogram or exact fourth moment.

The published finite-field norm-one-conic fourth-moment theorem in the published-finding corpus archive (identifier in references) provides a sharper **arbitrary-coefficient** statement over fields and, in particular, covers the \(k=1\) constant-input energy \(3p(p+1)\); that case is explicitly excluded from the claimed novelty. It cannot be substituted for the \(k\ge2\) ring calculation: nonprimitive sum targets and high-valuation tangent fibers do not occur over a field.

Hickman and Wright (arXiv:1801.03176) develop restriction for polynomial-graph surfaces over rings \(\mathbb Z/N\mathbb Z\) but do not state the present norm-one-circle convolution histogram. Previously tabulated modular inverse hyperbolas are the **split** norm-one torus; for \(p\equiv3\pmod4\) the present nonsplit norm form is not linearly equivalent over the residue field (its circle has \(p+1\), not \(p-1\), points modulo \(p\)). The theorem is not a restatement of that split-hyperbola result. These are bounded comparisons, not a proof of exhaustive historical priority.

## Limitations
The theorem applies only to odd primes \(p\equiv3\pmod4\), exponents \(k\ge2\), and the unweighted self-convolution and fourth Fourier moment of one specified conic. It does not solve the sharp \(L^2\to L^4\) extension problem for arbitrary coefficients, and no claim is made for even moduli or split primes. A stronger pre-existing general theorem on local quadratic-norm representation densities might imply the histogram; such a historical priority result has not been ruled out. No independent mathematical validation has been performed.

## References
1. A. Carbery, B. Stones and J. Wright, *Averages in vector spaces over finite fields*, Math. Proc. Cambridge Philos. Soc. **144** (2008), 13–27; first publicly online 2008-01-17, DOI 10.1017/S0305004107000680.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first publicly posted 2008-04-28.
3. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176, first posted 2018-01-09.
4. *Sharp fourth-moment extension on the anisotropic finite-field norm-one conic*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-fourth-moment-extension-on-the-anisotropic-finite-field-no--b7ad248d6495 , specifically `RESULT.md`.
