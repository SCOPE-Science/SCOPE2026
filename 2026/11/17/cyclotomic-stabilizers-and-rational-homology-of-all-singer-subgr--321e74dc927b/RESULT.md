# Cyclotomic stabilizers and rational homology of all Singer-subgroup quotients of finite spherical buildings

## Finding

Let \(q\) be any prime power and \(n\ge4\). The action of a Singer group, including every one of its cyclic subgroups, on the spherical building of proper nonzero subspaces of \(\mathbb F_{q^n}\) has completely determined geometric fixed-point types, first integral homology, and rational homology. The formulas below refer to **ordinary geometric orbit spaces**, not Borel constructions.

For \(t\mid N=(q^n-1)/(q-1)\), let \(Y_t\) be the quotient by the unique order-\(t\) subgroup and put \(L=N/\Phi_n(q)\), with \(\Phi_n\) the cyclotomic polynomial. Then

\[\pi_1(Y_t)\cong H_1(Y_t;\mathbb Z)\cong C_{t/\gcd(t,L)}.\]

Writing \(M_e=(q^e-1)/(q-1)\) for each \(e\mid n\) and \(a_d(t)=\sum_{e\mid d}\mu(d/e)\gcd(t,M_e)\), we also have

\[\widetilde H_i(Y_t;\mathbb Q)=0\quad(i\ne n-2),\qquad \dim_{\mathbb Q}\widetilde H_{n-2}(Y_t;\mathbb Q)=\frac1t\sum_{d\mid n}a_d(t)(-1)^{n-n/d}q^{d\binom{n/d}{2}}.\]

Here \(\mu\) is the number-theoretic Möbius function. The formula includes the complete rational top-homology character for the Singer action: if a projective scalar has field degree \(d\mid n\), its trace equals \((-1)^{n-n/d}q^{d\binom{n/d}{2}}\).

## Assumptions and scope

Identify the \(n\)-dimensional \(\mathbb F_q\)-space \(V\) with the field \(\mathbb F_{q^n}\). Let \(B_{n,q}\) be the **order complex** of the poset of all nonzero proper \(\mathbb F_q\)-linear subspaces of \(V\): vertices are subspaces and simplices are strictly increasing flags. Multiplication by \(\mathbb F_{q^n}^{\times}\) induces a faithful projective Singer group \(G=\mathbb F_{q^n}^{\times}/\mathbb F_q^{\times}\cong C_N\). Every subgroup considered is the unique cyclic subgroup \(H_t\le G\) of order \(t\), where \(t\mid N\). The topology is the usual geometric realization topology. A projective class has the well-defined field degree \(d=[\mathbb F_q(\alpha):\mathbb F_q]\), independent of multiplying its representative by an element of \(\mathbb F_q^{\times}\).

The original building has homotopy type \(\bigvee^{q^{\binom n2}}S^{n-2}\) by the Solomon–Tits theorem. Since \(n\ge4\), it is simply connected. No simply connectedness is presumed for the quotient.

## Proof

**1. Fixed subposets.** The action preserves the dimension of every subspace. A fixed point inside the geometric realization lies in the interior of a unique flag simplex; its positive barycentric-support vertices form a flag setwise preserved by the acting element. Since there is at most one vertex of each dimension in a flag, every support vertex is fixed individually. Thus the geometric fixed set is exactly the order complex of invariant proper nonzero subspaces. A subspace is invariant under multiplication by \(\alpha\) precisely when it is linear over \(\mathbb F_q[\alpha]=\mathbb F_{q^d}\). Hence the fixed set is the building on the \(n/d\)-dimensional space over \(\mathbb F_{q^d}\) for \(d<n\), and is empty for \(d=n\). Its reduced Euler characteristic is \((-1)^{m-2}q^{d\binom m2}\) for \(m=n/d\ge2\), by Solomon–Tits, and equals \(-1\) for \(m=1\), consistent with the same expression under the usual reduced-empty convention.

**2. Fixed-point stabilizers and fundamental groups.** A projective scalar fixes a point exactly when it lies in the image of the multiplicative group of some proper subfield. The image of \(\mathbb F_{q^e}^{\times}\) is the unique order-\(M_e\) subgroup of \(G\). It suffices to take maximal proper divisors \(e=n/p\) for primes \(p\mid n\). Their generated subgroup has order

\[\operatorname{lcm}_{p\mid n}M_{n/p}=\frac{1}{q-1}\operatorname{lcm}_{p\mid n}(q^{n/p}-1)=\frac{q^n-1}{(q-1)\Phi_n(q)}=L.\]

For completeness, the middle equality follows prime by prime from the cyclotomic factorization of \(q^n-1\) together with \(\gcd(q^a-1,q^b-1)=q^{\gcd(a,b)}-1\); alternatively apply the cyclotomic divisibility formula by induction over the prime divisors of \(n\). In the cyclic group \(G\), intersections distribute over subgroup generation: for subgroup orders \(a,b,t\), the equality \(\operatorname{lcm}(\gcd(t,a),\gcd(t,b))=\gcd(t,\operatorname{lcm}(a,b))\) follows from prime valuations. Consequently the elements of \(H_t\) that fix a geometric point generate exactly \(H_t\cap C_L\), of order \(\gcd(t,L)\). Armstrong's orbit-space theorem, applied to the simply connected building and the finite group \(H_t\), gives the displayed cyclic \(\pi_1\). Abelianization gives integral \(H_1\).

**3. Character and rational homology.** For a representative \(g\) of field degree \(d\), the reduced Lefschetz number equals \(\widetilde\chi(|B_{n,q}|^g)\). The original building has reduced homology in only degree \(n-2\); therefore the rational top-homology trace is

\[(-1)^{n-2}\widetilde\chi(|B_{n,q}|^g)=(-1)^{n-n/d}q^{d\binom{n/d}{2}}.\]

The elements of \(H_t\) with degree dividing \(e\) form its intersection with the order-\(M_e\) subgroup, hence number \(\gcd(t,M_e)\). Möbius inversion on the divisor lattice gives exactly \(a_d(t)\) elements of field degree \(d\). Barycentric subdivision yields an admissible simplicial action. Over \(\mathbb Q\), finite-group averaging identifies homology of the quotient with group-invariant homology of the original building. Averaging the above trace gives the asserted top rational Betti formula and vanishing in other reduced degrees. No integral averaging is used.

**4. Illustrative arithmetic boundary.** When \(q=2\) and \(n=6\), \(N=63\), \(\Phi_6(2)=3\), \(L=21\). The full order-\(63\) quotient has fundamental group \(C_3\) and top rational Betti number \(518\); the order-\(21\) quotient has trivial fundamental group and top rational Betti number \(1556\). For \(q=3,n=4\), \(N=40\), \(\Phi_4(3)=10\), \(L=4\), and the order-\(2\) subgroup quotient is simply connected. This last case shows why \(C_{\gcd(t,\Phi_n(q))}\) is **not** a valid replacement for the subgroup formula.

## Verification

The standalone standard-library program `verify_singer.py` reproduces the cyclotomic, subgroup and Lefschetz-averaging formulas for \(n=4,\ldots,16\) and \(q\in\{2,3,4,5,7\}\), for every divisor \(t\mid N\). It also enumerates every subspace for the small binary extension cases \(n=4\) and \(n=6\), checks the fixed-subspace ranks against Gaussian binomial counts and independently enumerates the flag-cell quotient Euler characteristic at \(q=2,n=4\). The checks print `ALL_CHECKS_PASSED` when successful. These are finite consistency tests; the four proof steps above, not the tests, establish the unrestricted theorem.

## Relationship to prior work

Drudge's *On the Orbits of Singer Groups and Their Subgroups* establishes fixed-flat stabilizer and orbit results for individual Grassmannian ranks; it provides the direct classical incidence-geometry motivation but does not calculate the entire spherical-building orbit space's fundamental group, rational top-homology character or subgroup quotient homology. Armstrong gives the general fixed-isotropy quotient theorem; Brown–Higgins give a general groupoid formulation. Solomon–Tits identifies the unquotiented building as a wedge of spheres. A previously recorded classification of the full projective Singer quotient in vector-space dimension four is subsumed at that parameter and is **not** asserted novel here: the new unified assertion covers every dimension at least four, **all subgroup orders**, the fixed-point building types and the complete rational character and quotient ranks.

## Limitations

No classification of higher-degree **integral** homology groups, higher homotopy groups, or complete homotopy types of the quotients is asserted. Except for the first integral homology, the Betti formula is over \(\mathbb Q\) only. Individual subfield fixed-point homotopy types follow classical building theory; mathematical content here is their combination with exact cyclic stabilizer generation and the all-subgroup topology and rational character. Exhaustive database search cannot rule out equivalent work that is unindexed or inaccessible; originality is therefore relative to the inspected primary works and deduplication evidence, and independent audit has not occurred.

## References

1. K. Drudge, *On the Orbits of Singer Groups and Their Subgroups*, Electronic Journal of Combinatorics 9(1), R15, DOI: https://doi.org/10.37236/1632 . The journal's public record lists publication date 2001-03-05; its volume citation is 2002.
2. M. A. Armstrong, *On the Fundamental Group of an Orbit Space*, Proceedings of the Cambridge Philosophical Society 61 (1965), DOI: https://doi.org/10.1017/S0305004100038974 .
3. R. Brown and P. J. Higgins, *The fundamental groupoid of the quotient of a Hausdorff space by a discontinuous action of a discrete group is the orbit groupoid of the induced action*, arXiv:math/0212271, first posted 2002-12-19, https://arxiv.org/abs/math/0212271 .
4. Solomon–Tits theorem on the homotopy type of finite spherical buildings, standard form for the proper-subspace poset.
