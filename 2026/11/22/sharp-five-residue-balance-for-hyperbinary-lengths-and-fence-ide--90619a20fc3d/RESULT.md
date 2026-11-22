# Sharp five-residue balance for hyperbinary lengths and fence ideals

## Finding

For every integer \(m\geq 0\), let \(\mathcal H(m)\) comprise all finite digit sequences \((e_0,e_1,\ldots)\) satisfying \(e_j\in\{0,1,2\}\), \(\sum_{j\geq0}e_j2^j=m\), and with only finitely many nonzero digits. The *length* is \(\ell(e)=\sum_{j\geq0}e_j\). For \(r\in\{0,1,2,3,4\}\), put

\[
C_r(m)=\#\{e\in\mathcal H(m):\ell(e)\equiv r\pmod5\}.
\]

**Theorem (sharp five-residue balance).** For every \(m\geq0\),

\[
\max_{0\leq r<5}C_r(m)-\min_{0\leq r<5}C_r(m)\leq2.
\]

The constant \(2\) is sharp: at \(m=10\), the five residue-class counts are \((1,0,1,2,1)\). Consequently, for every finite fence poset \(P\) (a poset whose unoriented Hasse diagram is a path, including one-element and empty cases), the numbers \(\#\{I\in J(P):|I|\equiv r\pmod5\}\) of order ideals of the five sizes modulo five have maximum-minus-minimum at most two. The same constant is sharp for fences.

## Assumptions and scope

Only finite integer-valued hyperbinary expansions and finite fence posets are involved. There is no restriction on \(m\), on the length of the fence, or on its alternating or repeated edge orientations. The result bounds *additive discrepancy* between residue-class cardinalities, not a relative error or each class size individually. It does not assert exact equidistribution or an analogous bound at every other modulus.

Write \(H_m(z)=\sum_{e\in\mathcal H(m)}z^{\ell(e)}\), with \(H_0(z)=1\) and \(H_{-1}(z)=0\). Let \(\zeta\) be a primitive fifth root of unity and \(R=\mathbb Z[t]/(t^4+t^3+t^2+t+1)\). In the basis \((1,t,t^2,t^3)\), represent an element by a four-integer tuple. Multiplication by \(t\) is the exact integer map

\[
Z(a,b,c,d)=(-d,a-d,b-d,c-d).
\]

No floating-point approximation to \(\zeta\) is used in the proof.

## Proof

**1. Polynomial recurrence.** A hyperbinary expansion of an odd integer \(2k+1\) necessarily has \(e_0=1\); remove that part and divide the others by two. An expansion of \(2k\) has \(e_0=0\) or \(e_0=2\). These mutually exclusive cases yield

\[
H_{2k+1}(z)=zH_k(z)\quad(k\geq0),\qquad
H_{2k}(z)=H_k(z)+z^2H_{k-1}(z)\quad(k\geq1).
\]

In particular \(H_1(z)=z\).

**2. Finite exact cyclotomic state system.** Put \(F(m)=H_m(\zeta)\in R\) and \(V_m=(F(m),F(m-1))\) for \(m\geq1\). Addition is coordinatewise. By the preceding recurrence,

\[
V_1=(\zeta,1),\quad
V_{2k}=T_0(V_k),\quad
V_{2k+1}=T_1(V_k),
\]

where for \((a,b)\in R^2\),

\[
T_0(a,b)=(a+\zeta^2b,\zeta b),\qquad
T_1(a,b)=(\zeta a,a+\zeta^2b).
\]

The supplied `states.json` contains **120 distinct eight-integer state records**, each representing a pair in \(R^2\). The accompanying exact-integer verifier checks the following finite mathematical certificate: the records are distinct; \((\zeta,1)\) occurs; *both* successors \(T_0(s),T_1(s)\) of *every one* of the 120 records occur; and the coordinate range criterion in Step 3 holds for every record. It also verifies all 120 records are reachable from the seed. Thus the finite set is inductively invariant, and every \(V_m\) belongs to it: for \(m>1\), apply the appropriate transformation to \(V_{\lfloor m/2\rfloor}\). This inductive coverage is for **every** positive integer, not an experiment over a bounded list of integers.

The exact certificate has 240 checked transitions. Among its 120 records, the spread in Step 3 is zero for 10 states, one for 100 states, and two for 10 states. The first coordinates take 31 distinct values. The file `verify.py` implements all transitions with integer tuples; `states.json` is the independent explicit table to be checked, not an unreported computation.

**3. Recover residue counts from the root evaluation.** Since \(1+\zeta+\zeta^2+\zeta^3+\zeta^4=0\),

\[
F(m)=\sum_{r=0}^{4}C_r(m)\zeta^r
=\sum_{j=0}^{3}\bigl(C_j(m)-C_4(m)\bigr)\zeta^j.
\]

The representation of \(R\) is unique because the fifth cyclotomic polynomial has degree four. Therefore, if \(F(m)\) has tuple \((a_0,a_1,a_2,a_3)\), then \(a_j=C_j(m)-C_4(m)\). Consequently,

\[
\max_r C_r(m)-\min_r C_r(m)
=\max(0,a_0,a_1,a_2,a_3)-\min(0,a_0,a_1,a_2,a_3).
\]

The 120-record certificate verifies that the right-hand side is always at most two. This proves the theorem for \(m\geq1\). For \(m=0\), there is a single empty expansion of length zero, so the bound is immediate.

**4. Sharpness.** Directly from the recurrence,

\[
H_{10}(z)=z^2+2z^3+z^4+z^5,
\]

so \((C_0(10),C_1(10),C_2(10),C_3(10),C_4(10))=(1,0,1,2,1)\). Thus one cannot replace the constant two by one.

**5. Transfer to every fence.** McConville, Propp and Sagan's rank-preserving correspondence, as expressed by Alekseyev, gives for the fence \(\mathcal F(m)\) associated with \(m\) the identity

\[
H_m(z)=z^{s_2(m)}\sum_{I\in J(\mathcal F(m))}z^{|\mathcal F(m)|-|I|},
\]

where \(s_2(m)\) is the number of ones in the binary expansion. Every finite nonempty fence arises as \(\mathcal F(m)\): encode its successive oriented edges in a binary word beginning with \(1\), and append \(01\) to make this word the principal prefix; see the proof of Alekseyev's Corollary 20. Multiplication by a monomial and reversal of exponents merely permute residue classes modulo five; hence the bound transfers unchanged. The empty fence has one ideal. Finally, \(m=10\) supplies a fence realizing discrepancy two through the same correspondence. This finishes the proof.

## Verification

From the directory containing the two supplied independent files, run `python3 verify.py`. This loads `states.json` and checks all 120 distinct states, the seed, complete closure under both transformations, reachability, the exact range histogram and the 31 distinct first coordinates. As a secondary check, it independently computes the full coefficient polynomials using the parity recurrence for each integer from zero through 12000 and confirms the claimed discrepancy and sharpness at ten. The exhaustive finite-state closure, not the second finite-index experiment, is the part that certifies the unrestricted theorem. All arithmetic in the verifier is exact integer arithmetic, with no external package or network dependency.

## Relationship to prior work

Alekseyev (arXiv:2611.01243v1, first posted 2026-10-31) proved that the *three* length classes modulo three differ by at most one and transferred this bound to all fence order ideals (Theorem 19 and Corollary 20). McConville, Propp and Sagan (arXiv:2508.20026v1) established the underlying hyperbinary/fence-poset correspondence and length generating functions. Kogiso, Miyamoto, Ren, Wakui and Yanagawa (arXiv:2403.08446v2, Section 7) examined evaluations of related rational \(q\)-polynomials at third and fourth roots of unity; their fifth-root example concerns divisibility obstructions, rather than the present additive five-residue discrepancy. None of the inspected pertinent statements provides the sharp five-class bound or the 120-state certificate. In particular, an assertion for three classes does not imply a bound for five classes by grouping or refinement. The exact index automaton and uniform bound are the new claims here, not the known recurrences or known fence correspondence.

## Limitations

The finite-state proof certifies the stated discrepancy but does not classify which integers give equality, nor does it establish analogous results for every prime modulus. A thorough historical-priority judgment may require examining additional older Stern-polynomial and root-of-unity literature; online and semantic searches are not a uniqueness proof. The included certificate is reproducible and has received the described self-review; independent external mathematical validation has not been performed.

## References

1. M. A. Alekseyev, *Halving Partitions and Hyperbinary Expansions*, arXiv:2611.01243v1 (first posted 2026-10-31), https://arxiv.org/html/2611.01243v1, especially Theorem 19, Corollary 20 and Equation (49).
2. T. McConville, J. Propp and B. E. Sagan, *Hyperbinary partitions and q-deformed rationals*, arXiv:2508.20026v1 (first posted 2025-08-27), https://arxiv.org/html/2508.20026v1, especially Theorems 3.16 and 3.17.
3. T. Kogiso, Y. Miyamoto, X. Ren, K. Wakui and H. Yanagawa, *Arithmetic on q-deformed rational numbers*, arXiv:2403.08446v2, https://arxiv.org/html/2403.08446v2, especially Section 7, Proposition 7.5 and Example 7.8.
