# Frobenius splitting of Bring's 120 tritangents and their contact points

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\ge 11\), and let \(C/k\) be the canonical Bring curve in \(\mathbb P^4_k\), defined by
\[
\sum_{i=1}^5X_i=\sum_{i=1}^5X_i^2=\sum_{i=1}^5X_i^3=0.
\]
Put \(F(t)=t^3+2t^2+3t+4\), let \(d\in\{1,2,3\}\) be the order of the permutation induced by \(q\)-Frobenius on its three roots, and put \(e=1\) if \(-15\) is a square in \(k\), and \(e=2\) otherwise. Write \(\ell=\operatorname{lcm}(d,e)\).

**Theorem.** For the reduced finite schemes \(\mathcal T\) of all geometric tritangent planes, \(\mathcal W\) of the 60 stalls, and \(\mathcal O\) of non-stall tritangent contact points, their degrees are \(120,60,120\) and every Frobenius cycle on them has length \(d,d,\ell\), respectively. Thus, for every \(n\ge 1\),
\[
\begin{aligned}
\#\mathcal T(\mathbb F_{q^n})&=120\mathbf1_{d\mid n},& Z(\mathcal T,U)&=(1-U^d)^{-120/d},\\
\#\mathcal W(\mathbb F_{q^n})&=60\mathbf1_{d\mid n},& Z(\mathcal W,U)&=(1-U^d)^{-60/d},\\
\#\mathcal O(\mathbb F_{q^n})&=120\mathbf1_{\ell\mid n},& Z(\mathcal O,U)&=(1-U^\ell)^{-120/\ell}.
\end{aligned}
\]
Of the 120 tritangents, 60 contact three stalls and the other 60 contact one stall and two points of \(\mathcal O\). Consequently, the number of tritangent planes with all three contacts rational over \(k\) is \(0\) when \(d>1\), is \(60\) when \(d=1,e=2\), and is \(120\) when \(d=e=1\). The rationality of a plane alone does not ensure the rationality of all its contacts.

## Assumptions and scope
The characteristic bound ensures \(2,3,5,7\) are invertible and every root/configuration used below is geometrically separable and projectively distinct. Tritangent planes are considered **inside the canonical \(\mathbb P^3\)** cut out by \(\sum X_i=0\); coefficient vectors for two equations define the same plane exactly when they differ by a scalar and an additive multiple of \((1,1,1,1,1)\). A stall is a point of osculating contact order at least four. The reduced finite schemes are the geometric support schemes, not infinitesimal degeneracy loci. The finite-scheme zeta function has convention \(Z(S,U)=\exp(\sum_{n\ge1}\#S(\mathbb F_{q^n})U^n/n)\).

## Proof
**1. Smoothness.** The three Jacobian rows are proportional to \((1)_i\), \((X_i)_i\), and \((X_i^2)_i\). If they have rank less than three, all five coordinates attain at most two values \(a,b\). If \(a\) occurs \(r\) times, \(1\le r\le4\), the first two power-sum equations imply \(b=-ra/(5-r)\) and \(5ra^2/(5-r)=0\), a contradiction for \(p\ge11\). A single coordinate value likewise vanishes. Thus \(C\) is smooth, a genus-four canonical degree-six complete intersection.

**2. Explicit geometric configurations.** Write \(\alpha,\beta,\gamma\) for the distinct roots of \(F\). Their discriminant is \(-200\). Define \(f(t)=(t-1)(t+4)\), \(h(t)=t^2+t+1\), and let \(\xi,\eta\) be the two roots of \(A(t)=t^2-t+4\), of discriminant \(-15\). The classical tritangent descriptions [1,2] take the following explicit form, with coordinate positions independently permuted:

- The 60 stalls are the permutations of \((1,1,\alpha,\beta,\gamma)\).
- The 60 first-type planes are \(\gamma X_j-\beta X_k=0\), for an ordered pair of distinct roots \((\beta,\gamma)\) and a choice of distinct positions \((j,k)\) in a fixed order. Equivalently, choose an unordered pair of positions and assign an ordered pair of different roots; there are \(10\cdot6=60\) planes.
- The 60 second-type planes are \(f(\alpha)X_i+f(\beta)X_j+f(\gamma)X_k=0\), on a chosen three-element coordinate support, with the three roots assigned in any order; there are \(10\cdot6=60\).
- The 120 other contact points are the permutations of \((\xi,\eta,h(\alpha),h(\beta),h(\gamma))\).

For a tangent hyperplane at a point with coordinates \((z_i)\), its coefficient vector is the evaluation of a polynomial of degree at most two at all \(z_i\). Hence the first-type planes are tangent at the three stalls obtained by putting \(\beta,\gamma\) at positions \(j,k\) and distributing \((1,1,\alpha)\) over the other positions: the polynomial \((t-1)(t-\alpha)\) has the required coefficient ratio because \(\beta(\beta-1)(\beta-\alpha)+\gamma(\gamma-1)(\gamma-\alpha)=0\). The second-type plane is tangent at its unique stall, because \(f(1)=0\). It is tangent at the two points obtained by placing \(h(\alpha),h(\beta),h(\gamma)\) in the support positions and \(\xi,\eta\) in either order in the complement: the identity \(h(t)^2-h(t)+4\equiv-f(t)\pmod{F(t)}\), together with \(A(\xi)=A(\eta)=0\), expresses the plane coefficient vector as a polynomial of degree two evaluated at the contact point. The resultant identity
\[
\operatorname{Res}_t(F(t),Y-h(t))=Y^3+Y^2-3Y-7
\]
and its product with \(A(Y)\) give \(Y^5-5Y-28\); its first three Newton sums vanish, so all non-stall points lie on \(C\). The first three Newton sums of \((1,1,\alpha,\beta,\gamma)\) vanish likewise. Bezout's degree-six intersection bound confirms each plane's three indicated tangencies exhaust its intersection divisor.

**3. Distinctness over all allowed characteristics.** The polynomial \(Y^5-5Y-28\) has discriminant \(2^{13}3\cdot5^7\), hence five distinct roots for \(p\ge11\). Its coefficients at degrees one and zero are both nonzero. If scaling a permutation of these five roots yielded another projectively equal permutation, preservation of the monic polynomial of the scaled root multiset gives \(c^4=c^5=1\), so \(c=1\); therefore the 120 contact points are projectively distinct. The stall points are distinct since the repeated coordinate value \(1\) fixes the projective normalization.

For the first-type planes, all six oriented root ratios are distinct: a collision would require two roots to be opposite or three roots to form a geometric progression. The former would force \(F(-2)=-2=0\); the latter forces a root \(-3/2\) and then \(F(-3/2)=5/8=0\). Neither occurs for \(p\ge11\). For the second-type planes, the three \(f\)-values are distinct because \(f(\alpha)-f(\beta)=(\alpha-\beta)(1-\gamma)\), and they have sum \(-20\ne0\). Planes with identical three-coordinate supports cannot differ by projective scaling or addition of the all-ones vector; different supports cannot coincide because either they share an absent coordinate or two distinct \(f\)-values would have to be equal. A first-type and a second-type plane cannot coincide because their support sizes differ and their two nonzero first-type coefficients are unequal. Thus all 120 planes remain distinct as planes of the canonical \(\mathbb P^3\). The contact description exhibits all 120 odd-theta tritangents; there can be no others by the standard genus-four theta count, which also follows from the classical integral classification [1,2] and its good-characteristic specialization established here.

**4. Frobenius cycles.** The formulas above define the configurations over the splitting field \(k_F\) of \(F\), with the non-stall contacts also requiring the splitting field \(k_A\) of \(A\). The Galois action is literal permutation of \(\alpha,\beta,\gamma\) and independent possible interchange of \(\xi,\eta\). Because the displayed objects are geometrically distinct, a nonidentity permutation of the three roots fixes no label in the 60 stalls or in either ordered-root plane family; the stabilizer of every such object under the root permutation group is trivial. Their Frobenius orbit lengths therefore all equal \(d\). Similarly, each of the 120 non-stall points contains all five distinctly labeled entries; its stabilizer under root permutations and the quadratic swap is trivial, so its orbit length is exactly \(\ell=\operatorname{lcm}(d,e)\). Counting cycles gives the claimed zeta functions. The two types of plane are separately Galois-stable. For \(d=1\), all 60 first-type planes have three rational stall contacts; each second-type plane has two more rational contacts exactly when \(e=1\).

## Verification
Run `python3 verify_bring.py` with Python 3 and SymPy installed. It checks the cubic and quintic discriminants, the resultant and tangent polynomial identities, all six Frobenius cycle types on the full 120/60/120 labeled sets, the distinct 120 plane vectors in five split prime fields, the three stall contacts of every first-type plane in those fields, and all 120 non-stall contacts and their second-type incidence at split test primes with \(e=1\). The script is an exact reproducibility check; the symbolic and uniform geometric arguments above prove the infinite-field statement. Its recorded output is `verification_output.txt`.

## Relationship to prior work
Edge [1] calculated the 120 complex tritangents and their contact coordinates in 1981. Braden and Disney-Hogg [2], §5.2, re-exhibit the two 60-element families, the 60 stalls, the explicit two other contacts on each second-type tritangent, and describe the 120 odd theta orbits under \(S_5\). These geometric formulas, the 60+60 partition, and the count of contact points are **not** proposed as new. The arithmetic theorem here concerns the positive-characteristic good-reduction range and gives the exact finite étale Frobenius zeta functions of all three natural configurations, with a second quadratic obstruction for complete rational tritangent contacts. The existing complex orbit decomposition alone does not specify the arithmetic Frobenius permutation of the cubic roots or quadratic contacts. Related published calculations of modular-two theta representations likewise do not establish this statement in the inspected sources.

## Limitations
The theorem does not cover characteristics \(2,3,5,7\), or arbitrary twists/forms of Bring's curve. It concerns only the specified integral equation and the reduced geometric support schemes; it does not determine the Weil polynomial or point counts of the curve itself. The geometric equations are classical; the priority of the arithmetic synthesis may be affected by unindexed finite-field analyses or previously implicit consequences of the formulas. No independent audit is asserted.

## References
1. W. L. Edge, *Tritangent Planes of Bring's Curve*, Journal of the London Mathematical Society (2) **23** (1981), 215–222, https://webhomes.maths.ed.ac.uk/cheltsov/edge2022/pdf/1981a.pdf (especially §§1,5).
2. H. W. Braden and L. Disney-Hogg, *Bring's curve: Old and New*, arXiv:2208.13692 (first public version 2022-08-29), European Journal of Mathematics **10** (2024), https://arxiv.org/pdf/2208.13692 (especially §§2,5.2).
