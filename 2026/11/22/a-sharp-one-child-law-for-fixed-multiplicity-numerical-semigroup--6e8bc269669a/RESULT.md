# A sharp one-child law for fixed-multiplicity numerical-semigroup trees

## Finding
Fix an integer \(m\ge3\). For each integer \(g\ge m-1\), let \(\mathcal S_m(g)\) be the finite set of numerical semigroups of multiplicity \(m\) and genus \(g\). For \(S\in\mathcal S_m(g)\), let \(\mu(S)\) be the number of its minimal generators strictly larger than its Frobenius number: equivalently, the number of its children in the ordinary numerical-semigroup tree. Put
\[
N_m(g)=|\mathcal S_m(g)|,\qquad
B_m(g)=|\{S\in\mathcal S_m(g):\mu(S)\ne1\}|,\qquad
T_m(g)=|\{S\in\mathcal S_m(g):\mu(S)\ge2\}|.
\]
Then, as \(g\to\infty\) **with \(m\) fixed**,
\[
\boxed{N_m(g)=\Theta_m(g^{m-2}),\quad B_m(g)=\Theta_m(g^{m-3}),\quad T_m(g)=\Theta_m(g^{m-3}).}
\]
Thus a uniformly chosen multiplicity-\(m\), genus-\(g\) numerical semigroup has exactly one child with probability
\[
\boxed{\mathbb P(\mu(S)=1)=1-\Theta_m(1/g).}
\]
In particular the number of leaves is \(O_m(g^{m-3})\), and for every fixed \(m\) there is a finite \(G_m\) such that internal semigroups outnumber leaves whenever \(g\ge G_m\). The error order \(1/g\) is sharp because semigroups with at least two children already occupy a positive order-\(1/g\) fraction. For \(m=2\), every genus \(g\ge2\) semigroup has exactly one child, so the exceptional-rate assertion is deliberately restricted to \(m\ge3\).

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\) containing zero. Its multiplicity \(m\) is its smallest positive element, its genus \(g\) is its number of positive gaps, its Frobenius number \(F\) is the largest gap, and a minimal generator is a positive element not expressible as a sum of two positive semigroup elements. The constants hidden in \(\Theta_m\) and \(O_m\) may depend on the fixed multiplicity; no assertion uniform in increasing \(m\) is made. The parent of a semigroup is obtained by adjoining its Frobenius number, and each child is obtained by deleting an effective (right) minimal generator, i.e. one greater than \(F\).

Write \(d=m-1\) and let \(x=(x_1,\ldots,x_d)\) be the Kunz coordinates, so that the Apéry representatives are \(w_0=0\) and \(w_i=mx_i+i\) for \(1\le i\le d\). Their exact conditions are
\[
x_i\ge1,\quad\sum_{i=1}^{d}x_i=g,\qquad
x_i+x_j+\left\lfloor\frac{i+j}{m}\right\rfloor\ge x_{(i+j)\bmod m}
\]
for \(1\le i\le j\le d\) with \(i+j\ne m\). In these inequalities the remainder belongs to \(\{1,\ldots,d\}\). These are the standard Kunz conditions, and their integral solutions correspond bijectively to \(\mathcal S_m(g)\).

## Proof
**1. Primitive Apéry representatives and a finite exceptional-hyperplane covering.** The Frobenius number satisfies \(F=\max_{1\le i\le d}w_i-m\). Each \(w_r\) is a minimal generator if and only if there is no pair \(i,j\in\{1,\ldots,d\}\) with \(w_i+w_j=w_r\). Indeed, any decomposition of \(w_r\) into positive semigroup elements can be reduced modulo \(m\); minimality of the Apéry representatives forces equality with the two representatives and no extra multiples of \(m\). Such an equality is precisely equality in a nontrivial Kunz inequality. Thus **strict Kunz inequalities make all \(w_i\) primitive**.

For \(g\ge m+1\), the elementary bound \(F\ge g\) implies \(m<F\), so only Apéry representatives can be effective generators. If \(\mu(S)=0\), a largest representative \(w_r=F+m\) cannot be primitive: if it were, it would be an effective generator. Therefore \(x\) lies on at least one affine hyperplane
\[
x_i+x_j+\left\lfloor\frac{i+j}{m}\right\rfloor=x_{(i+j)\bmod m},
\]
with \(i+j\ne m\). If instead \(\mu(S)\ge2\), two distinct effective representatives \(w_i,w_j\) both lie in the half-open interval \((F,F+m]\); hence \(|w_i-w_j|<m\). Since \(w_i-w_j=m(x_i-x_j)+(i-j)\), necessarily \(x_i-x_j\in\{-1,0,1\}\). Consequently every exceptional vector with \(\mu(S)\ne1\) belongs to a finite union (depending only on \(m\)) of these Kunz-equality hyperplanes and coordinate-near-tie hyperplanes.

Each such hyperplane is linearly independent of the genus equation \(\sum x_i=g\), including when indices repeat in a Kunz equality. With \(d\) positive coordinates bounded by \(g\), one can freely choose \(d-2\) coordinates and solve the two independent linear equations for the remaining two; there is at most one solution per choice. Thus each hyperplane contributes \(O_m(g^{d-2})\) integral points, and
\[
B_m(g)=O_m(g^{d-2}),\qquad T_m(g)\le B_m(g).
\]

**2. Full-dimensional count.** The total number of positive integer vectors with sum \(g\) is \(\binom{g-1}{d-1}=O_m(g^{d-1})\). On the other hand, in a small open relative neighborhood of the balanced point \((g/d,\ldots,g/d)\), all entries are positive and the largest entry is strictly less than twice the smallest. Every nontrivial Kunz inequality is then strict. Choosing \(d-1\) coordinates independently in intervals of length proportional to \(g\), while determining the final coordinate by the sum, gives \(\Omega_m(g^{d-1})\) integer vectors in this neighborhood. Hence \(N_m(g)=\Theta_m(g^{d-1})\).

**3. A positive-dimensional two-child family for every multiplicity.** For \(m=3\) (so \(d=2\)), take \(x=(h,h)\) when \(g=2h\), and \(x=(h+1,h)\) when \(g=2h+1\). For all sufficiently large \(h\), both vectors obey all Kunz inequalities strictly; their two Apéry representatives differ by respectively \(1\) and \(2\), and both are effective. Thus \(T_3(g)\ge1=\Omega(g^0)\) for every sufficiently large \(g\).

Now suppose \(m\ge4\), so \(d\ge3\). Choose a fixed small rational \(\delta\in(0,1/20]\) and let
\[
p_1=p_2=\frac{1+\delta}{d},\qquad
p_i=\frac{1-2\delta/(d-2)}{d}\quad(3\le i\le d).
\]
These numbers sum to one, are positive, and satisfy \(p_1=p_2>p_i\) for \(i\ge3\), while \(2\min p_i>\max p_i\). Consider the \(d-2\)-dimensional affine lattice slice \(x_1=x_2\), \(\sum x_i=g\). An open relative neighborhood of \(gp\) in this slice has all positive entries, every Kunz inequality strict, and \(x_1=x_2>x_i\) for all \(i\ge3\). It contains \(\Omega_m(g^{d-2})\) integer vectors for all sufficiently large integer \(g\): choose \(x_1=x_2\) and \(x_3,\ldots,x_{d-1}\) independently in fixed-width proportional-to-\(g\) intervals and determine \(x_d\) using the sum. For each such vector, \(w_2=mx_2+2\) is the largest Apéry element, \(w_1=mx_1+1=w_2-1\), and both are primitive and greater than \(F=w_2-m\). Thus \(\mu(S)\ge2\), proving \(T_m(g)=\Omega_m(g^{d-2})\).

Combining the bounds gives \(T_m(g)=\Theta_m(g^{d-2})\), and since \(T_m(g)\le B_m(g)\le O_m(g^{d-2})\), also \(B_m(g)=\Theta_m(g^{d-2})\). Dividing by \(N_m(g)=\Theta_m(g^{d-1})\) gives the sharp \(1/g\) probability order. The leaf bound follows from the first hyperplane covering. Since it is \(o(N_m(g))\), internal semigroups strictly outnumber leaves for all sufficiently large \(g\) at each fixed \(m\). \(\square\)

## Verification
The standalone Python 3 standard-library program `verify_one_child.py` independently checks two definitions of child count on all valid Kunz coordinate vectors for multiplicities \(2\le m\le6\) and genera \(m-1\le g\le16\): one counts primitive Apéry representatives using equalities, while the other enumerates semigroup membership and directly tests all positive additive decompositions. It checks 1,275 semigroups and obtains `INDEPENDENT_CHILDREN_OK 1275` and `VERIFY_OK`. It also reports complete child-degree histograms for \(3\le m\le7\) and \(g\in\{12,18,24,32\}\). These are finite corroborations only: the all-genus assertion follows from the preceding proof, not from extrapolation.

## Relationship to prior work
Casas, Madrid, and Rosales (2026) introduce the general internal/leaf classification program, give algorithms for fixed multiplicity and genus, and formulate the internal-versus-leaf conjecture. García-Sánchez, Marín-Aragón, and Robles-Pérez (2018) analyze child counts at multiplicity three and prove fixed-multiplicity total-count monotonicity for multiplicities up to five. Alhajjar, Russell, and Steward (2019) already prove asymptotic density one of **maximal embedding dimension** for fixed multiplicity and genus; that claim is not new here. Maximal embedding dimension does not, however, imply exactly one child: in the strict interior of the Kunz polytope two near-maximal Apéry representatives can both be effective, and Step 3 proves a matching-order family of such points for every multiplicity. The present theorem concerns the **sharp exceptional branching frequency**, not a new maximal-embedding-dimension density claim. Related prior work classifies fixed-multiplicity infinite chains (Rosas-Ribeiro and Bras-Amorós, 2023), while published special-case degree enumerations at multiplicity four provide further consistency checks; those cases alone do not cover the simultaneous all-multiplicity asymptotic statement.

## Limitations
The constants implicit in the order bounds are not computed; an exact leading coefficient, a uniform result as multiplicity grows with genus, and a fixed-genus all-multiplicity inequality are not claimed. Already established Kunz-polytope results explain the general lattice-point-counting mechanism, so the specific mathematical contribution is the all-multiplicity **one-child law with sharp matching exceptional exponent**, including the explicit two-effective-generator lower bound. Priority beyond the inspected literature is not independently certified. No external independent audit has been performed.

## References
1. M. Casas, J. A. Madrid, J. C. Rosales, *Internal numerical semigroups* (first public arXiv version August 20, 2026), https://arxiv.org/abs/2608.19984 . Primary MSC 20M14.
2. P. A. García-Sánchez, D. Marín-Aragón, A. M. Robles-Pérez, *The tree of numerical semigroups with low multiplicity* (2018), https://arxiv.org/abs/1803.06879 .
3. E. Alhajjar, T. Russell, M. Steward, *Numerical semigroups and Kunz polytopes*, Semigroup Forum 99 (2019), 153–168, https://doi.org/10.1007/s00233-019-10028-x .
4. M. DiPasquale, B. Gillespie, C. Peterson, *Quasi-polynomial growth of numerical and affine semigroups with constrained gaps* (2022), https://arxiv.org/abs/2208.09760 .
5. M. Rosas-Ribeiro, M. Bras-Amorós, *Infinite chains in the tree of numerical semigroups* (2023), https://arxiv.org/abs/2308.09500 .
6. T. Gomes, C. O'Neill, E. Torres Davila, *Numerical semigroups, polyhedra, and posets III: minimal presentations and face dimension* (2020), https://arxiv.org/abs/2009.05921 .
