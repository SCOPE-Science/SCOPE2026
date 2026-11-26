# Exact two-facility covering profile and rigidity on rectangular taxicab tori

## Finding
Let \(T=\prod_{j=1}^d\mathbb R/\ell_j\mathbb Z\) be a product of metric circles, with the intrinsic sum (taxicab) metric \(\rho\). Define the covering radius of two prescribed sites by
\[
\mathcal R(a,b)=\max_{x\in T}\min\{\rho(x,a),\rho(x,b)\}.
\]
For every integer \(d\ge1\), every choice of side lengths \(\ell_j>0\), and every pair \(a,b\in T\), put \(D=\tfrac12\sum_{j=1}^d\ell_j\). The exact complete prescribed-pair profile is
\[
\boxed{\mathcal R(a,b)=D-\tfrac12\rho(a,b).}
\]
Consequently, the *unrestricted* two-center minimum equals \(D/2=\tfrac14\sum_j\ell_j\). Equality holds precisely when the two centers are coordinatewise antipodal, that is, \(b_j=a_j+\ell_j/2\) modulo \(\ell_j\) for all \(j\). The excess radius of an arbitrary pair over optimum is exactly
\[
\mathcal R(a,b)-D/2=\frac12\sum_{j=1}^d\left(\frac{\ell_j}{2}-\rho_j(a_j,b_j)\right).
\]
This last identity is a sharp *global*, not asymptotic, linear stability relation.

## Assumptions and scope
Each factor is a circle of **strictly positive** circumference \(\ell_j\). For points on a factor set \(\rho_j(s,t)=\min_{k\in\mathbb Z}|s-t+k\ell_j|\), and set \(\rho=\sum_j\rho_j\). The maximum defining \(\mathcal R\) is over the whole compact continuous torus; the center pair is unrestricted and may coincide. Here the metric is \(\ell_1\), **not** the Euclidean flat-torus geodesic metric or the max metric. The diameter of \((T,\rho)\) is \(D\).

## Proof
1. **Antipodal identity.** Define \(\tau:T\to T\) by \(\tau(x)_j=x_j+\ell_j/2\) modulo \(\ell_j\). For every circle and every \(u,v\), exactly one of the two complementary distances to \(v\) sums to the semicircumference:
\[
\rho_j(\tau(u)_j,v_j)=\ell_j/2-\rho_j(u_j,v_j).
\]
Summing gives \(\rho(\tau u,v)=D-\rho(u,v)\), for all points, including antipodal/tie cases.

2. **Universal upper bound for arbitrary sites.** Fix any \(a,b,x\in T\). The metric triangle inequality at \(\tau x\), followed by the antipodal identity, gives
\[
\rho(a,b)\le \rho(a,\tau x)+\rho(\tau x,b)
=2D-\rho(x,a)-\rho(x,b).
\]
Consequently
\[
\min\{\rho(x,a),\rho(x,b)\}\le\frac{\rho(x,a)+\rho(x,b)}2
\le D-\frac{\rho(a,b)}2.
\]
This bound is valid at every \(x\), hence also for the maximum.

3. **Simultaneous sharp witness.** Translate coordinates so \(a_j=0\), reflect individual factors if needed, and represent \(b_j=s_j\) with \(0\le s_j\le\ell_j/2\). Choose \(x_j=(\ell_j+s_j)/2\) modulo \(\ell_j\), namely the midpoint of the complementary, longer arc from \(b_j\) back to \(a_j\). Then
\[
\rho_j(x_j,a_j)=\rho_j(x_j,b_j)=(\ell_j-s_j)/2.
\]
Summation yields \(\rho(x,a)=\rho(x,b)=\sum_j(\ell_j-s_j)/2=D-\rho(a,b)/2\). This witnesses equality, so the prescribed-pair identity follows with no approximation or genericity assumption.

4. **Optimization and rigidity.** For every pair \(\rho(a,b)=\sum_j s_j\le D\), with equality if and only if \(s_j=\ell_j/2\) for every \(j\). Thus minimizing the exact profile is equivalent to maximizing the separation, and produces \(D/2\) exactly at coordinatewise half-period pairs. Subtracting this optimum proves the displayed exact excess identity. The coefficient \(1/2\) is sharp since the identity holds with equality for every pair.

## Verification
The companion standard-library program `verification/checker.py` tests the exact antipodal identity, the constructed simultaneous equal-distance witness, the profile formula, the global pointwise inequality, the diametral rigidity condition, and the excess identity using exact rational arithmetic on deterministic finite cases in dimensions one through five. It makes no claims that finite tests prove the universally quantified result; Steps 1–4 above do that.

To reproduce from the file bundle, run `python3 verification/checker.py` with Python 3.10 or later. The script has no third-party dependencies.

## Relationship to prior work
Cieliebak and Cieliebak (2026) study covering numbers of metric spaces and product behavior in the sum metric, providing direct motivation for an exact two-site profile on products of metric circles. Bogdanov, Grigoryan and Zhukovskii (2022) analyze covers of flat tori by axis-parallel cubes, which represent max-metric balls rather than the taxicab balls here. The unit square taxicab torus's previously known two-site optimum \(1/2\) is a special case of the present result, but it does not supply the entire *prescribed-pair* profile or arbitrary-dimensional/aspect-ratio rigidity. A published covering study of well-rounded flat tori concerns Euclidean geodesic disks, whose shapes and metric differ from the sum metric.

## Limitations
The theorem is restricted to rectangular product tori and their intrinsic sum metric. It asserts nothing about the geodesic Euclidean metric, arbitrary skew flat tori, three or more centers, or classification of the maximizing farthest points. The claim is mathematically proved here, but independent review and exhaustive historical priority verification have not been performed.

## References
1. Cieliebak, K. and Cieliebak, M., *Covering Numbers of Metric Spaces* (2026), arXiv:2611.15599v1, https://arxiv.org/abs/2611.15599.
2. Bogdanov, I. I., Grigoryan, O. R. and Zhukovskii, M. E., *On Coverings of Tori with Cubes*, Doklady Mathematics 105 (2022), DOI:10.1134/S1064562422020077, https://link.springer.com/article/10.1134/S1064562422020077.
