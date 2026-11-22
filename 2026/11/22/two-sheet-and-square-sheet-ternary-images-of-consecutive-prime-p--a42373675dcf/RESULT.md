# Two-sheet and square-sheet ternary images of consecutive prime-power differences

## Finding

Fix an integer \(s\ge1\), put \(m=3^s\), and define the integer polynomial
\[
G_s(X)=(X+1)^m-X^m.
\]
Write \(\mathbb Z_3\) for the \(3\)-adic integers, \(\mathbb Z_3^2=\{z^2:z\in\mathbb Z_3\}\), and \(c_s=2^{1-m}\in\mathbb Z_3\). Then the **exact** image is the disjoint union
\[
G_s(\mathbb Z_3)=\bigl(1+3^{s+1}\mathbb Z_3\bigr)\ \sqcup\ \bigl(c_s+3^{s+2}\mathbb Z_3^2\bigr).
\]
The first component is attained twice, on two isometric residue branches, while the second component is a scaled square image on the remaining residue branch.

Let \(I_s(n)\) be the number of attained residues modulo \(3^n\), \(n\ge1\). Put \(Q(0)=1\) and, for every \(L\ge1\),
\[
Q(L)=1+\sum_{j=0}^{\lfloor(L-1)/2\rfloor}3^{L-2j-1}.
\]
Then \(I_s(1)=1\), whereas for every \(n\ge2\),
\[
I_s(n)=3^{\max(0,n-s-1)}+Q\bigl(\max(0,n-s-2)\bigr).
\]
In particular, the image has normalized Haar measure
\[
\lim_{n\to\infty}\frac{I_s(n)}{3^n}=\frac{1}{8\cdot3^{s-1}}.
\]

**Complete finite fiber law.** For \(n\ge2\), the two components are distinguished by their residues \(1\) and \(7\) modulo \(9\). Every attained \(y\) in the first component has exactly \(2\cdot3^{\min(s,n-1)}\) preimages \(x\bmod3^n\). For an attained \(y\) in the second component, if \(n\le s+2\) there are exactly \(3^{n-1}\) preimages. If \(n>s+2\), put \(L=n-s-2\), and set
\[
z=\frac{y-c_s}{3^{s+2}}\pmod{3^L}.
\]
If \(z=0\), the fiber has size \(3^{s+1+\lfloor L/2\rfloor}\). If \(0\le2j<L\) and \(\nu_3(z)=2j\), with \(z/3^{2j}\) a square unit, its fiber has size \(2\cdot3^{s+1+j}\). These exhaust the second component. At \(n=1\), the sole output is \(1\) with three inputs.

## Assumptions and scope

The statements concern all integers \(s\ge1\), all finite levels \(n\ge1\), and all residue targets; the variable ranges over all integers modulo \(3^n\) or, in the limiting formulation, over \(\mathbb Z_3\). The inverse power of \(2\) in \(c_s\) is defined because \(2\) is a \(3\)-adic unit. A residue in the second component is interpreted through the quotient only when \(n>s+2\). All valuation statements involving \(z\) require \(z\not\equiv0\pmod{3^L}\). No assertions are made for other primes or exponents not equal to powers of three.

## Proof

**1. Binomial divisibility.** For \(1\le j<m=3^s\), the identity \(j\binom mj=m\binom{m-1}{j-1}\) implies
\[
\nu_3\!\left(\binom mj\right)\ge s-\nu_3(j).
\]
We use this for every coefficient estimate below. In particular, \(j-1-\nu_3(j)\ge1\) for \(j\ge2\), and \(j-2-\nu_3(j)\ge2\) for even \(j\ge4\).

**2. The two regular residue branches.** For \(x=3v\), the top-degree terms cancel and the binomial theorem gives
\[
G_s(3v)=1+3^{s+1}\bigl(v+3R_s(v)\bigr),\qquad R_s\in\mathbb Z_3[v].
\]
Indeed each coefficient of degree \(j\ge2\) in the normalized polynomial has valuation at least \(j-1-\nu_3(j)\ge1\). Thus \(B_s(v)=v+3R_s(v)\) satisfies
\[
\nu_3(B_s(v)-B_s(w))=\nu_3(v-w),\qquad v\ne w,
\]
because the difference of any integral polynomial is divisible by \(v-w\). Consequently its reduction is an injection, hence a permutation, modulo every \(3^k\), and \(B_s\) is a bijective isometry of \(\mathbb Z_3\). Since \(m\) is odd, \(G_s(-1-x)=G_s(x)\). Therefore both \(x\equiv0\pmod3\) and \(x\equiv-1\pmod3\) map onto precisely \(1+3^{s+1}\mathbb Z_3\), separately as scaled isometries. At finite level each output has \(3^{n-1}\) inputs in each branch when \(n\le s+1\), and \(3^s\) in each branch when \(n>s+1\).

**3. The quadratic residue branch.** Every input in the remaining class \(x\equiv1\pmod3\) can be written uniquely as \(x=-\tfrac12+3v\) for \(v\in\mathbb Z_3\). Writing \(c_s=2^{1-m}\), oddness of \(m\) gives the exact polynomial expansion
\[
G_s(-\tfrac12+3v)=c_s\sum_{\substack{0\le j<m\\j\text{ even}}}\binom mj(6v)^j
=c_s+3^{s+2}v^2H_s(v).
\]
The quadratic coefficient is \(u_s=2c_s(m-1)\), and all higher coefficients in \(H_s\) are divisible by \(9\), by the first step and the inequality for even \(j\ge4\). Hence
\[
H_s(v)=u_s+9A_s(v),\qquad A_s\in\mathbb Z_3[v],\quad u_s\equiv1\pmod3.
\]
For every \(v\), \(H_s(v)\in1+3\mathbb Z_3\), which has a unique square root \(h_s(v)\equiv1\pmod3\). This root exists by the simple-root form of Hensel's lemma. Moreover, since \(H_s(v)-H_s(w)\in9(v-w)\mathbb Z_3\), the identity
\[
(h_s(v)-h_s(w))(h_s(v)+h_s(w))=H_s(v)-H_s(w)
\]
shows that \(h_s(v)-h_s(w)\in9(v-w)\mathbb Z_3\), as the second factor is a unit. Thus the map \(\Psi_s(v)=v h_s(v)\) satisfies \(\nu_3(\Psi_s(v)-\Psi_s(w))=\nu_3(v-w)\) for distinct inputs. Every reduction of \(\Psi_s\) is a permutation; it is a bijective isometry of \(\mathbb Z_3\). The critical branch therefore has **exactly** the image \(c_s+3^{s+2}\mathbb Z_3^2\), with the same finite fibers as a square map after accounting for the variable substitution.

**4. Disjointness.** The number \((m-1)/2\) is congruent to \(1\pmod3\). Because \(4^3\equiv1\pmod9\),
\[
c_s=4^{-(m-1)/2}\equiv7\pmod9.
\]
Since \(s\ge1\), every point of the regular component is \(1\pmod9\), while every point of the critical component is \(7\pmod9\). Thus the union is disjoint over \(\mathbb Z_3\) and modulo \(3^n\) for \(n\ge2\); modulo \(3\) both collapse to \(1\).

**5. Counts and fibers.** Squares modulo \(3^L\) consist of zero and the classes of valuation \(2j<L\) with square unit part. For each such \(j\), the number of distinct classes equals \(3^{L-2j-1}\). This proves the formula for \(Q(L)\). At a nonzero square target with valuation \(2j\), the equation \(v^2=z\pmod{3^L}\) has exactly \(2\cdot3^j\) solutions; at zero it has \(3^{\lfloor L/2\rfloor}\). The critical coordinate change \(x=-1/2+3v\) gives \(3^{s+1}\) lifts modulo \(3^n\) of each solution modulo \(3^{n-s-2}\). Combining these with step 2 proves all stated fiber sizes and the image cardinality formula. Finally, squares in \(\mathbb Z_3\) have Haar measure
\[
\frac12\left(1-\frac13\right)\sum_{j\ge0}3^{-2j}=\frac38.
\]
The disjoint image therefore has measure \(3^{-(s+1)}+\frac38\,3^{-(s+2)}=1/(8\cdot3^{s-1})\), as claimed.

## Verification

For the first exponent, the identity \(G_1(X)=3(X+1/2)^2+1/4\) supplies a direct quadratic check of the singular branch. The standalone `check.py` computes \(G_s(x)\bmod3^n\) for every input in each of 34 complete finite rings, independently assembles the predicted regular and square-fiber distributions, and verifies equality of the complete target-to-fiber dictionaries, not just cardinalities. The tested levels are \(1\le s\le2,1\le n\le9\) and \(3\le s\le4,1\le n\le8\). Reproduce using `python3 check.py`. The all-exponent theorem is the symbolic proof above, not an extrapolation from these checks.

## Relationship to prior work

Arias, Borja and Anaya (2023) investigate the number of residues represented by sums and differences of powers with independent variables, including prime-power lifting; their generalized results do not impose the consecutive-input constraint. Under that constraint, the two independent-variable derivatives cannot be varied independently, and the singular square branch is essential. Arias, Borja and Rubio (2019) likewise address independent-variable polynomial forms. Patel and Siksek (2017) address Diophantine perfect-power values of consecutive-power sums, not modular value sets or fiber multiplicities. Published analogous studies of ternary polynomial value images and of dyadic consecutive-power sums treat different polynomials or primes and do not entail this classification. These comparisons do not establish bibliographic uniqueness against unindexed work.

## Limitations

Only the family of odd exponents \(3^s\) at the prime \(3\) is classified. The theorem does not solve the corresponding image problem for general exponents, other primes, or global integer representations. Source searches and mathematical comparisons are not a guarantee of worldwide originality. There has been no independent audit of the proof or calculations.

## References

- F. Arias, J. Borja, S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf (published August 28, 2023; primary MSC 11A07).
- F. Arias, J. Borja, L. Rubio, *Counting Integers Representable as Images of Polynomials Modulo n*, Journal of Integer Sequences **22** (2019), Article 19.6.7. https://arxiv.org/abs/1812.11599 (first posted December 30, 2018).
- V. Patel, S. Siksek, *On powers that are sums of consecutive like powers*, Research in Number Theory **3** (2017), Article 2. https://doi.org/10.1007/s40993-016-0068-0.
