# The exact 2-adic image of the central Delannoy numbers has measure one seventh

## Finding

Define the central Delannoy sequence by \(D_n=\sum_{j=0}^n2^j\binom{n}{j}^2\) for integers \(n\ge0\). Its entire \(2\)-adic value closure is the following **disjoint** union:

\[
\overline{\{D_n:n\ge0\}}=
(3+16\mathbb Z_2)\cup(13+16\mathbb Z_2)
\cup\{1,-1\}
\cup\bigcup_{a\ge2}\big[(1+2^{3a}\mathbb Z_2^\times)
\cup(-1+2^{3a}\mathbb Z_2^\times)\big].
\]

Its normalized Haar measure is exactly \(\frac18+\sum_{a\ge2}2^{-3a}=\boxed{\frac17}\). Moreover, for every integer \(k\ge4\), the number of distinct residues represented modulo \(2^k\) is
\[
N_k=2^{k-3}+2+\sum_{a=2}^{\lfloor(k-1)/3\rfloor}2^{k-3a}.
\]
At \(k=1,2,3\) the counts are respectively \(1,2,4\). Every represented residue class modulo any binary power occurs at infinitely many nonnegative indices; none of the excluded residue classes is taken.

## Assumptions and scope

All rings, valuations, and measures are \(2\)-adic; \(\mathbb Z_2^\times\) denotes the odd units. For \(x\in\mathbb Z_2\), define the convergent interpolation
\[
F(x)=\sum_{j\ge0}2^j\binom xj^2.
\]
Each summand belongs to \(\mathbb Z_2\), and its valuation is at least \(j\); hence convergence is uniform. In particular, \(F(n)=D_n\) for nonnegative integers \(n\). Because those integers are dense, the closure of integer values is \(F(\mathbb Z_2)\), a compact image.

## Proof

**Step 1: two unrestricted residue balls.** Write \(x=4u+b\) with \(u\in\mathbb Z_2\). The exact finite coefficient certificates checked in `verify.py` are
\[
\sum_{j=0}^6 2^j\binom{4u+1}j^2\equiv3+16u\pmod{32\mathbb Z_2[u]},\qquad
\sum_{j=0}^6 2^j\binom{4u+2}j^2\equiv13+16u\pmod{32\mathbb Z_2[u]}.
\]
To bound the omitted tails in the integral-coefficient restricted power-series ring, let \(s_2(j)\) denote the binary digit sum. Every coefficient of the \(j\)-th summand for \(b=1,2\) has valuation at least
\[
L_j=-j+2\lfloor j/2\rfloor+2\lfloor j/4\rfloor+2s_2(j).
\]
For \(j=7,8,9,10\), direct substitution gives \(L_j\ge5\); for \(j\ge11\), the floor inequalities give \(L_j\ge j/2-1/2\ge5\), and the bound tends to infinity. Thus
\[
F(4u+1)=3+16(u+2V_1(u)),\qquad F(4u+2)=13+16(u+2V_2(u))
\]
with \(V_1,V_2\in\mathbb Z_2\langle u\rangle\). Each map \(u\mapsto u+2V_b(u)\) is an isometry: subtracting its values factors out \(u-v\) times an odd unit. On each finite residue ring it is consequently injective and therefore bijective, and compactness gives a bijection of \(\mathbb Z_2\). Their images are precisely \(3+16\mathbb Z_2\) and \(13+16\mathbb Z_2\).

**Step 2: exact cubic behavior near zero.** For \(b=0\), the truncated polynomial satisfies
\[
\sum_{j=0}^8 2^j\binom{4u}j^2\equiv1+64u^3\pmod{128\mathbb Z_2[u]}.
\]
For every \(j\ge9\), every coefficient of the \(j\)-th summand has valuation at least
\[
4-j+2\lfloor(j-1)/2\rfloor+2\lfloor(j-1)/4\rfloor+2s_2(j)\ge7.
\]
The coefficient of \(u\) in \(F(4u)\) vanishes identically. Its coefficient of \(u^2\) is \(16\sum_{j\ge1}2^j/j^2\), which also vanishes **exactly**, not merely modulo \(128\). Indeed the convergent 2-adic dilogarithm \(\operatorname{Li}_2(z)=\sum_{j\ge1}z^j/j^2\) satisfies, for \(z\in2\mathbb Z_2\),
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac z{z-1}\right)
=-\frac12\log^2(1-z).
\]
This follows by differentiating and checking the value at zero. At \(z=2\), the two arguments coincide and \(\log(-1)=0\), so \(\operatorname{Li}_2(2)=0\). Consequently the exact factorization is
\[
F(4u)=1+64u^3U(u),\qquad U\in1+2\mathbb Z_2\langle u\rangle.
\]
Writing \(u=2^tw\) for \(t\ge0\) and \(w\in\mathbb Z_2^\times\), the normalized map \(w\mapsto w^3U(2^tw)\) is an isometry of the odd units: the quotient of differences is odd because \((w^3-z^3)/(w-z)=w^2+wz+z^2\) is odd and the perturbation from \(U-1\) contributes an even quotient. Injectivity on finite odd residue rings and their equal cardinalities give surjectivity. Hence the image on \(4\mathbb Z_2\) is precisely \(\{1\}\cup\bigcup_{a\ge2}(1+2^{3a}\mathbb Z_2^\times)\).

**Step 3: reflection.** For each nonnegative integer \(n\), the rational binomial generating-function identity
\[
\sum_{j\ge0}\binom{n+j}n^2z^j
=\frac{\sum_{j=0}^n\binom nj^2z^j}{(1-z)^{2n+1}}
\]
holds at \(z=2\) in \(\mathbb Q_2\). Since \(\binom{-1-n}j=(-1)^j\binom{n+j}n\) and \(1-2=-1\), this gives \(F(-1-n)=-F(n)\). Continuity and density extend it to \(F(-1-x)=-F(x)\) for all \(x\in\mathbb Z_2\). Therefore \(F(3+4\mathbb Z_2)=-F(4\mathbb Z_2)\), producing the second cubic tower centered at \(-1\).

**Step 4: enumeration.** The four index classes are exhausted. The four image sectors lie at distinct residues \(1,3,13,15\pmod{16}\), so the union is disjoint. For \(k\ge4\), two full disks contribute \(2^{k-3}\) residue classes, the two centers contribute two, and for each \(a\) with \(3a<k\), the two odd-unit shells contribute a total of \(2^{k-3a}\). The claimed formula and Haar measure follow. All attained cylinders contain infinitely many nonnegative indices by continuity, density, and the local isometries.

## Verification

`verify.py`, using only Python's standard library, recomputes exact rational polynomial coefficients for the three finite certificates, tests the analytic tail inequalities, and independently generates Delannoy terms by the exact integral three-term recurrence \(nD_n=3(2n-1)D_{n-1}-(n-1)D_{n-2}\). It compares the observed and predicted image sets for every modulus through \(2^{11}\). Successful finite checks are supporting calculations; the infinite statement follows from the displayed tail bounds, 2-adic dilogarithm identity, and isometries.

## Relationship to prior work

Guo and Zeng (2010, arXiv:1008.2894) study sums and congruences involving the central Delannoy sequence. Lengyel (2021) gives 2-adic congruences and conjectures valuation patterns near \(\pm1\). A later published result establishes the exact cubic valuation \(\nu_2(D_n-1)=3\nu_2(n)\) on indices divisible by four. Such valuation information predicts the possible shells but does not assert or imply that **all** odd units in every shell occur, nor supply the two unrestricted image disks. The present result uses stronger local isometries to determine the complete image and its measure.

## Limitations

This theorem concerns the **set** of values and its 2-adic Haar measure, not the frequency of individual Delannoy values over index intervals. The earlier full-text literature comparison is not exhaustive; an implicit or unpublished equivalent could affect historical priority.

## References

1. V. J. W. Guo and J. Zeng, *New congruences for sums involving Apéry numbers or central Delannoy numbers*, arXiv:1008.2894 (first submitted 2010-08-17), https://arxiv.org/abs/1008.2894.
2. T. Lengyel, *On some p-adic properties and supercongruences of Delannoy and Schröder numbers*, INTEGERS 21 (2021), A86, https://math.colgate.edu/~integers/v86/v86.pdf.
3. *Resolution of the sharp binary valuation conjecture for central Delannoy numbers* (2026), published mathematical finding, https://github.com/published-finding corpus/2026.
