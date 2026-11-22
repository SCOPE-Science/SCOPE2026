# Branch-contact classification at infinity for symmetric Fermat quotient plane models

## Finding

Let \(n\ge 11\) be any integer with \(\gcd(n,6)=1\), over \(\mathbb C\). Let \(P_n(E_1,E_2,E_3)\) be the \(n\)-th Newton power sum of the three roots of \(T^3-E_1T^2+E_2T-E_3\), and set \(N_n(u,v)=P_n(1,u,v)\). Let \(\overline C_n\subset\mathbb P^2_{[U:V:W]}\) be the ordinary projective closure of \(N_n(u,v)=0\), with \(u=U/W\) and \(v=V/W\).

The degree of \(\overline C_n\) is \(d=(n-1)/2\). Its affine part is smooth, and its only singular point is \(P=[0:1:0]\). The other point at infinity, \(Q=[1:1:0]\), is smooth. The normalization of \(\overline C_n\) is the symmetric Fermat quotient \(D_n=\{X^n+Y^n+Z^n=0\}/S_3\).

In the affine chart \(V=1\) at \(P\), put \(a=U/V\), \(b=W/V\). The complete branch-contact description is as follows.

* If \(n=6\ell+5\) (\(\ell\ge1\)), there are \(\ell\) smooth branches with equations \(b=\lambda_i a^3+O(a^4)\), with mutually distinct nonzero \(\lambda_i\), and one smooth branch with \(b=a/(\ell+1)+O(a^2)\). The first \(\ell\) branches meet each other with intersection multiplicity exactly \(3\), while each meets the distinguished branch transversely (multiplicity \(1\)). The tangent cone is proportional to \(b^\ell((\ell+1)b-a)\). Here
\[
\delta_P=\frac{\ell(3\ell-1)}2,\qquad \mu_P=\ell(3\ell-2),\qquad r_P=\ell+1.
\]
* If \(n=6\ell+1\) (\(\ell\ge2\)), there are \(\ell-1\) smooth branches with equations \(b=\lambda_i a^3+O(a^4)\), with mutually distinct nonzero \(\lambda_i\), and one smooth distinguished branch with \(b=-\ell a^2+O(a^3)\). The first \(\ell-1\) branches meet pairwise with multiplicity \(3\) and each meets the distinguished branch with multiplicity \(2\). The tangent cone is proportional to \(b^\ell\). Here
\[
\delta_P=\frac{(\ell-1)(3\ell-2)}2,\qquad \mu_P=3(\ell-1)^2,\qquad r_P=\ell.
\]
Here \(r_P\) denotes the number of analytic branches, \(\delta_P\) their local delta invariant, and \(\mu_P\) the characteristic-zero Milnor number. In particular, the \(n=11\) model has an ordinary node at infinity, and the \(n=13\) model has an ordinary tacnode there. For every allowed \(n\), these data account for all of the arithmetic-genus defect of \(\overline C_n\).

## Assumptions and scope

All assertions concern the reduced complex plane curve defined by the *ordinary*, not weighted, homogenization of \(N_n(u,v)\). The symmetric group acts on the smooth Fermat curve by permutations of its three homogeneous coordinates. The parameters \(\ell\) and \(n\) are integers in the ranges stated; arbitrary composite \(n\) coprime to six are included. The results do not assert that the corresponding singularity germs for different \(n\) are analytically isomorphic: the classification is by branch counts, tangents and pairwise intersection multiplicities.

## Proof

**1. Polynomial model and the two points at infinity.** Newton's identities give
\[
P_0=3,\quad P_1=E_1,\quad P_2=E_1^2-2E_2,\quad P_3=E_1^3-3E_1E_2+3E_3,
\]
\[
P_j=E_1P_{j-1}-E_2P_{j-2}+E_3P_{j-3}\quad(j\ge4).
\]
The projective invariant-field calculation \(\mathbb C(\mathbb P^2)^{S_3}=\mathbb C(e_2/e_1^2,e_3/e_1^3)\), with \(e_1=X+Y+Z\), \(e_2=XY+YZ+ZX\), \(e_3=XYZ\), identifies the quotient's function field with \(\mathbb C(u,v)\) subject to \(N_n=0\), as in [1, Proposition 2.3]. On the chart \(e_1\ne0\), normalize \(e_1=1\). Since taking \(S_3\)-invariants of a characteristic-zero quotient by the invariant Fermat equation is exact, its affine coordinate ring is \(\mathbb C[u,v]/(N_n)\). This is the quotient of a smooth affine curve by a finite group and therefore a smooth curve. The projective closure is integral and its normalization is \(D_n\).

Write \(n=2d+1\). In the power-sum expansion a monomial \(E_1^\alpha E_2^\beta E_3^\gamma\) has \(\alpha+2\beta+3\gamma=n\). Upon setting \(E_1=1\), the maximum ordinary degree \(\beta+\gamma\) is \(d\), reached only at \((\alpha,\beta,\gamma)=(1,d,0)\) and \((0,d-1,1)\). Their coefficients, by the Newton power-sum formula, are \(n(-1)^d\) and \(n(-1)^{d-1}\). Thus the highest homogeneous part of \(N_n\) is
\[
n(-1)^{d-1}u^{d-1}(v-u).
\]
The only points of its projective closure on \(W=0\) are \(P=[0:1:0]\) and \(Q=[1:1:0]\). The factor \(v-u\) is simple at \(Q\), so \(Q\) is smooth.

**2. Points of the normalization above infinity.** On the Fermat curve \(F_n\), the preimage of the infinity divisor lies on \(e_1=0\). There are three special points in one \(S_3\)-orbit with \(e_3=0\), namely permutations of \([1:-1:0]\), and two points in one orbit with \(e_2=0\), namely \([1:\omega:\omega^2]\) and \([1:\omega^2:\omega]\), where \(\omega^3=1\ne\omega\). All remaining points have \(e_2e_3\ne0\), and their stabilizers in \(S_3\) are trivial.

The intersection of the line \(e_1=0\) with \(F_n\) is transverse at the three special points and at all points with \(e_2e_3\ne0\). Indeed, tangency would require \(X^{n-1}=Y^{n-1}=Z^{n-1}\); since all three coordinates are then nonzero roots of unity up to common scale and sum to zero, they must be proportional to \((1,\omega,\omega^2)\) or its conjugate. At these two triple-cycle points, direct local expansion of \(P_n(e_1,e_2,e_3)\) shows intersection order \(1\) if \(n\equiv5\pmod6\), and order \(2\) if \(n\equiv1\pmod6\). The \(n\) intersections counted with multiplicity are hence \(3+2h+6s\), where \(h=1\) or \(2\); thus the number \(s\) of generic \(S_3\)-orbits is respectively \(s=\ell\) or \(s=\ell-1\).

The rational map to the ordinary plane closure is given wherever defined by \([e_1e_2:e_3:e_1^3]\). At the generic and triple-cycle points \(e_3\ne0\), so all map to \(P\). At a special point \(e_1=e_3=0\), expand the invariant Fermat equation with \(e_2\ne0\): its initial terms are a nonzero multiple of \(e_2^{d-1}(e_3-e_1e_2)\). Hence \(e_3/(e_1e_2)\to1\), and the extended map sends the special orbit to \(Q\). Since the map is an isomorphism over the smooth affine curve, these are all normalization preimages of points at infinity.

**3. Generic branches and their mutual contacts.** In the chart \(V=1\) near \(P\), the coordinates pull back to
\[
a=\frac{e_1e_2}{e_3},\qquad b=\frac{e_1^3}{e_3},\qquad \frac{b}{a^3}=\frac{e_3^2}{e_2^3}.
\]
At any generic point of \(e_1=0\), transversality makes \(e_1\) a local uniformizer; both \(e_2,e_3\) are units, so \(a\) is a uniformizer and \(b=\lambda a^3+O(a^4)\), with \(\lambda=e_3^2/e_2^3\ne0\). This \(\lambda\) separates the generic \(S_3\)-orbits: the unordered triple of coordinates on \(e_1=0\) is determined up to scale by \(e_2,e_3\), and the invariant ratio \(e_3^2/e_2^3\) determines its projective \(S_3\)-orbit when both are nonzero. Thus all \(s\) values \(\lambda_i\) are distinct, and two generic branches have intersection multiplicity exactly \(3\).

**4. The distinguished triple-cycle branch.** Near \(e_2=e_1=0\), choose an analytic cube-root trivialization of \(e_3\ne0\). The stabilizer is a cyclic group of order three acting faithfully on the Fermat-curve tangent, so the quotient parameter is the cube of a local parameter upstairs. The power-sum expansion gives, with nonzero coefficients:
\[
\begin{aligned}
n=6\ell+5:&\quad P_n=n e_3^{2\ell+1}\bigl((\ell+1)e_1^2-e_2\bigr)+\text{higher terms near }(e_1,e_2)=(0,0),\\
n=6\ell+1:&\quad P_n=n e_3^{2\ell-1}\bigl(e_1e_3+\ell e_2^2\bigr)+\text{higher terms near }(e_1,e_2)=(0,0).
\end{aligned}
\]
Here the higher terms do not affect the leading orders after solving the local Fermat equation. In the first case \(e_1\) is a local parameter upstairs, \(e_2=(\ell+1)e_1^2/e_3^{0}+O(e_1^3)\) after setting \(e_3=1\), and \(a,b\) both have order three upstairs. Downstairs this branch is smooth with \(b=a/(\ell+1)+O(a^2)\). In the second case \(e_2\) is a local parameter upstairs and \(e_1=-\ell e_2^2/e_3+O(e_2^3)\); then \(a\) has order three, \(b\) order six, and \(b=-\ell a^2+O(a^3)\) downstairs. It is smooth in both cases. Its intersections with each generic branch therefore have multiplicity one and two, respectively.

**5. Completeness and invariants.** Every branch over \(P\) is smooth; hence its delta invariant is the sum of pairwise intersection multiplicities. With \(s=\ell\) and distinguished contact \(c=1\), or \(s=\ell-1\) and \(c=2\), this is \(\delta_P=3\binom{s}{2}+cs\). The formulas in the Finding follow; the Milnor formula \(\mu_P=2\delta_P-r_P+1\) applies to reduced plane curves over \(\mathbb C\). The tangent cone is the product of the branch tangent lines. Finally, with \(d=(n-1)/2\) and the known genus \(g(D_n)=(n-1)(n-5)/12\) [1], direct simplification yields
\[
\frac{(d-1)(d-2)}2-g(D_n)=\delta_P,
\]
confirming that no additional singularities or hidden genus defects remain. This last identity is a consistency check, not a substitute for the local proof.

## Verification

The included `check_local.py` implements Newton's recurrence with exact symbolic arithmetic and independently checks the leading homogeneous factor, squarefreeness of the generic-branch polynomial, and equality between local delta and arithmetic-genus defect at degrees \(n=5,7,11,13,17,19,23,25,29,31\). The first two small degrees serve as sanity checks only and are not claimed within the theorem. The actual run passed each test. The general proof above is symbolic and does not extrapolate from finite checks. Analytic expansions in the proof use characteristic zero and the faithful local stabilizer action.

## Relationship to prior work

[1] proves the genus and automorphism classification of the symmetric Fermat quotient and explicitly identifies its affine equation \(N_n(u,v)=0\). The present result concerns the *ordinary projective plane compactification* of that given affine equation: its complete infinity singularity, normalization branch count, pairwise contacts, delta and Milnor number, none of which is asserted in [1, §§2–4]. The established genus formula is used only as a check. Earlier work on individual Fermat quotients and classical symmetric polynomials supplies background but not an identified all-degree branch-contact theorem for this specific ordinary projective closure. Broad novelty cannot be certified from database searches alone.

## Limitations

All claims are geometric over \(\mathbb C\). The theorem does not classify integral reduction at small primes, arithmetic fields of the individual branches, complete analytic moduli beyond intersection/contact data, or canonical embeddings. Classical or unindexed earlier accounts of Newton power-sum plane curves could overlap; a separate independent literature audit is appropriate before priority claims. The earlier Tzermias model for the degree-eleven quotient is a different affine equation and projective completion.

## References

[1] S. Tafazolian, *Fermat quotients with CM Jacobians and trivial automorphism group*, arXiv:2611.08176v1 (first submitted November 5, 2026), especially Proposition 2.3 and Lemma 2.1. https://arxiv.org/html/2611.08176v1

[2] P. Tzermias, *Parametrization of low-degree points on a Fermat curve*, Acta Arith. 108 (2003), 25–35. https://doi.org/10.4064/aa108-1-3 (inspected in Sections 1–5; provides a distinct degree-eleven quotient plane model, not relied upon for the branch calculation).
