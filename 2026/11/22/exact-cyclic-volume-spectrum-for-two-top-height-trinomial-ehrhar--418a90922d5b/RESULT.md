# Exact cyclic volume spectrum for two-top-height trinomial Ehrhart simplices

## Finding

Let \(k\ge2\) and \(a\ge1\) be integers. Suppose a lattice polytope \(P\) has Ehrhart numerator
\[
h_P^*(t)=1+a t^k+2t^{2k}
\]
and its associated finite lattice-simplex group \(\Lambda_P\) is cyclic. Then its normalized volume belongs **exactly** to
\[
\operatorname{Vol}_{\mathbb Z}(P)=a+3\in\{4,5,6,8,10\}.
\]
Conversely, **each of the five values is attained for every integer \(k\ge2\)** by a cyclic-group lattice simplex. Thus the attainable middle coefficients are precisely \(a\in\{1,2,3,5,7\}\), and the sharp cyclic normalized-volume bound is \(10\). This is a statement about cyclic *full simplex groups*, not the narrower cyclic intermediate subgroup appearing in some previous decompositions.

## Assumptions and scope

The normalized volume of a \(d\)-dimensional lattice polytope is \(d!\) times its Euclidean volume. The lattice simplex group \(G=\Lambda_P\) consists of the barycentric residue classes in \((\mathbb R/\mathbb Z)^{d+1}\) satisfying the simplex integrality condition. The integer height \(\operatorname{ht}(g)\) is the sum of representatives of coordinates in \([0,1)\); the coefficient of \(t^j\) in the Ehrhart numerator counts group elements of height \(j\). Since \(k\ge2\), the vanishing coefficient at \(t\) forces \(P\) to be an empty lattice simplex, so this group description applies. The cyclicity hypothesis means \(G\cong\mathbb Z/m\mathbb Z\), with \(m=a+3\); the dimension is unrestricted. Zero coordinates of \(G\) may be omitted without changing heights.

## Proof

**1. The two high elements generate the group.** Write \(B=\{x,y\}\subset G\) for the two distinct elements of height \(2k\). Every other nonzero element has height \(k\). Put \(J=\langle x,y\rangle\), \(h=|J|\), \(m=|G|\). For any finite subgroup \(H\le G\), the average of one fractional coordinate over \(H\) equals \((q-1)/(2q)\), where \(q\) is the order of its coordinate image. As every image order for \(J\) divides the corresponding image order for \(G\), \(\mathbb E_J\operatorname{ht}\le\mathbb E_G\operatorname{ht}\). Direct counting, since both high elements lie in \(J\), gives \(\mathbb E_J\operatorname{ht}=k(1+1/h)\) and \(\mathbb E_G\operatorname{ht}=k(1+1/m)\). Hence \(h\ge m\), and \(J=G\).

**2. A uniform finite order bound.** For a nonzero element \(z\) let \(s(z)\) be its number of nonzero fractional coordinates. The identity \(s(z)=\operatorname{ht}(z)+\operatorname{ht}(-z)\) gives \(s(x),s(y)\ge3k\). Every unit multiple \(uz\) in \(\langle z\rangle\) has the same support as \(z\). For an element \(z\in B\) of order \(N>2\), each unordered unit pair \(\{uz,-uz\}\) must contain a high element, because two low elements would have total height \(2k<s(z)\). There are \(\varphi(N)/2\) such pairs and only two high elements in all of \(G\), so \(\varphi(N)\le4\). Orders \(N=2\) satisfy the same restriction trivially. Thus each high element has order in \(\{2,3,4,5,6,8,10,12\}\), and cyclicity together with \(G=\langle x,y\rangle\) yields
\[
m=\operatorname{lcm}(\operatorname{ord}x,\operatorname{ord}y)\le60.
\]
This **proves** the finite cutoff; it is not inferred from experiments.

**3. Necessary exact character restrictions.** Identify \(G\) with \(\mathbb Z/m\mathbb Z\) and write the high elements as distinct indices \(a_0,b_0\in\{1,\dots,m-1\}\). Every fractional coordinate is a character \(j\mapsto (jr\bmod m)/m\), for some \(0\le r<m\); let \(n_r\ge0\) be its multiplicity. When \(a_0=j+(a_0-j)\) and both summands are low-height, height subadditivity is equality \(k+k=2k\). Hence there is **no coordinate carry** in such a sum. The only possibly carrying \(j\) are \(b_0\) and \(a_0-b_0\), since \(j=0,a_0\) cannot carry. The analogous condition holds with \(a_0,b_0\) exchanged. For a character \(r\ne0\), write \(g=\gcd(r,m)\) and \(c_h=(hr\bmod m)\). Direct enumeration of cyclic residues shows that the total number of \(j\in\mathbb Z/m\mathbb Z\) whose character residues carry in \(j+(h-j)\) is exactly \(m-g-c_h\). Consequently this number is at most two and must equal the number of carries in the two allowed exceptional indices, with coincident indices counted only once. These explicit equalities define the allowable character set \(R(m,a_0,b_0)\) computed in `cyclic_screen.cpp`.

Every unordered pair \(1\le a_0<b_0<m\) is included in the finite enumeration for all \(4\le m\le60\). There is no sampling of parameters, no representative-pair assumption, and no need to infer completeness from a symmetry partition. The cutoff of sixty is proved in Step 2.

**4. Exact finite inconsistency certificate.** For each candidate pair, the checker first constructs all allowable character residues and discards sets that cannot generate a faithful cyclic representation, namely those with \(\gcd(m,\{r:r\in R\})>1\). Any actual representation would assign nonnegative integer multiplicities \(n_r\) to the allowable characters and satisfy, for every \(1\le j<m\),
\[
\sum_{r\in R}(jr\bmod m)n_r
  =mk\bigl(1+\mathbf1_{j=a_0}+\mathbf1_{j=b_0}\bigr).
\]
Dividing by \(k\), this gives a **necessary rational linear system** with unknowns \(\lambda_r=n_r/k\). The checker forms its integer coefficient matrix \(A\) and right-hand column \(v\), then reduces modulo \(p=1{,}000{,}000{,}007\). It certifies a pair impossible only if \(A\) has full column rank \(s=|R|\) modulo \(p\) **and** the augmented matrix \([A\mid v]\) is inconsistent modulo \(p\). This implies the rational system is inconsistent: a nonzero \(s\)-minor modulo \(p\) would give a unique rational solution with denominator invertible modulo \(p\), contradicting modular inconsistency. Neither positivity nor any numerical tolerance is needed for an exclusion.

The self-contained code inspects **34,219** unordered high-element pairs with \(4\le m\le60\). Of these, **2,366** have faithful allowable character sets and **2,352** have certified modular inconsistency. The remaining **14 pairs** occur only at \(m\in\{4,5,6,8,10\}\); `cyclic_screen.cpp` prints each surviving pair and its character set. Therefore every other cyclic volume is excluded. Running the same program over \(m\le1024\) is an additional check, not a substitute for the analytic cutoff.

**5. Exact witnesses in all degrees.** For each of the five values of \(m\), use the following generator's **coordinate residues** modulo \(m\):

| \(m\) | generator coordinate residues \(r\) |\(a=m-3\)|
|---:|---|---:|
|4|\((1,2,2,3)\)|1|
|5|\((2,4,4)\)|2|
|6|\((2,5,5)\)|3|
|8|\((4,5,7)\)|5|
|10|\((5,6,9)\)|7|

Each residue tuple sums to a multiple of \(m\), is faithful (residue gcd with \(m\) equals one), and has heights \(0\) once, \(1\) exactly \(m-3\) times and \(2\) exactly twice. The group-to-lattice-simplex correspondence realizes every such finite subgroup as a lattice simplex. Repeating **each** coordinate exactly \(k\) times preserves the cyclic group and multiplies all heights by \(k\), producing \(h^*(t)=1+(m-3)t^k+2t^{2k}\) for each \(k\ge2\). This completes the claimed exact spectrum.

## Verification

From this directory, compile and run `g++ -std=c++17 -O2 cyclic_screen.cpp -o cyclic_screen && ./cyclic_screen 60`. The final stderr line must be `SUMMARY 60 34219 2366 2352 14`; the fourteen stdout exceptions must have only the five stated volumes. Execute `python3 witness_check.py`, which verifies every cyclic generator height exactly without third-party libraries. The matrix elimination uses exact modular integer operations, and the analytic steps certify that all group orders needing examination lie at most sixty. An independent second-prime replay can be obtained by substituting prime \(1000000009\) for \(1000000007\). The independent mathematical audit of this result has not been performed.

## Relationship to prior work

Tsuchiya's 2026 article supplies the initial finite-group perspective, the general upper bound \((8b^2)^b\) for a final coefficient \(b\ge2\), and examples of normalized volume \(4(b+1)\). A separate published 2026 result establishes the sharp **unrestricted** bound \(12\) when \(b=2\), attained by noncyclic examples. The present theorem is **not** a second proof of that bound: it classifies the entire possible normalized-volume spectrum under the natural full-group cyclicity restriction and shows its strictly smaller maximum \(10\). The previously known cyclic *intermediate subgroup* bound under an additional support-size condition is not the statement here. The cited full-text results do not imply the five-value classification.

## Limitations

The theorem concerns exactly two elements at maximum height and full-group cyclicity. It does **not** classify noncyclic groups, the lattice simplices up to lattice equivalence, all possible dimensions, or more general trinomial coefficients. The exclusion relies on a transparent exhaustive **finite** modular arithmetic certificate, whose correctness still depends on the included enumeration and linear algebra being executed as specified. The cited literature and mathematical-record searches cannot guarantee priority against inaccessible or unpublished work. Independent review has not occurred.

## References

1. A. Tsuchiya, *Scott-type inequalities for trinomial \(h^*\)-polynomials*, arXiv:2610.35287 (first public version October 26, 2026), especially Proposition 4.3, Example 4.5, and Question 4.6. https://arxiv.org/abs/2610.35287
2. V. Batyrev and B. Hofscheier, *Lattice polytopes, finite abelian subgroups in \(\mathrm{SL}(n,\mathbb C)\) and coding theory*, arXiv:1309.5312 (2013), Theorem 2.3 and Proposition 2.6. https://arxiv.org/abs/1309.5312
3. *Sharp dimension-free volume bound for trinomial \(h^*\)-polytopes with final coefficient two* (2026), a published mathematical record establishing the unrestricted sharp bound \(12\). https://github.com/published-finding corpus/2026
