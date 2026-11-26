# Parity-split ground-state magnetization and Curie response on Ising antiprisms

## Finding

Let \(A_n\) be the skeleton of the \(n\)-gonal antiprism, \(n\ge3\), with \(2n\) labeled sites, \(4n\) edges and spins \(\sigma_v\in\{-1,+1\}\). For uniform antiferromagnetic coupling \(J>0\), define
\[
H_h(\sigma)=J\sum_{\{u,v\}\in E(A_n)}\sigma_u\sigma_v-h\sum_{v\in V(A_n)}\sigma_v.
\]
Write \(\Omega_n(m)\) for the number of **zero-field** ground configurations with total spin \(M=\sum_v\sigma_v=m\). The complete ground-state magnetization polynomial is
\[
\boxed{\sum_m\Omega_n(m)y^m=\begin{cases}
4,&n\text{ even},\\[2pt]
\tfrac{n(n-1)}2(y^{-2}+y^2)+n(n+1),&n\text{ odd}.
\end{cases}}
\]
The minimum zero-field Hamiltonian equals \(-2Jn\) for even \(n\) and \(-2J(n-1)\) for odd \(n\). Consequently, the total ground degeneracy is \(4\) for even \(n\), and \(2n^2\) for odd \(n\).

For the finite-volume Gibbs measure at temperature \(T>0\), with \(k_B>0\), let \(\chi_n(T)=\left.\partial_h\langle M\rangle_{T,h}\right|_{h=0}\). Then the exactly determined zero-temperature Curie coefficient satisfies
\[
\boxed{\lim_{T\downarrow0}k_BT\,\chi_n(T)=\begin{cases}
0,&n\text{ even},\\[2pt]
2(n-1)/n,&n\text{ odd}.
\end{cases}}
\]
In particular, the odd-size coefficient approaches \(2\), while the even-size coefficient remains zero. The order of limits is \(T\downarrow0\) at fixed \(n\), followed, if desired, by \(n\to\infty\).

## Assumptions and scope

The antiprism has two vertex rings \(a_i,b_i\), indexed cyclically by \(i\in\mathbb Z/n\mathbb Z\). Its four edge families are \(a_i a_{i+1}\), \(b_i b_{i+1}\), \(a_i b_i\), and \(a_i b_{i-1}\). Each edge appears once. This graph is isomorphic to the square \(C_{2n}^2\) of a \(2n\)-cycle, so its Hamiltonian is also a uniform nearest/next-nearest-neighbor Ising ring. The spins are classical, all couplings are the same positive \(J\), and the field is uniform. Ground-state claims concern \(h=0\), while \(h\) is used to define the linear susceptibility.

A frustrated edge means an edge with equal endpoint spins, which contributes \(+J\) rather than \(-J\). There are \(2n\) triangular side faces: \((a_i,a_{i+1},b_i)\) and \((b_{i-1},b_i,a_i)\). On any triangle of three Ising spins the number of frustrated edges is either one or three.

## Proof

Let \(r_a\) and \(r_b\) count frustrated edges on the two cyclic rims, and let \(d\) count frustrated cross edges. Each rim edge occurs in exactly one side triangle, while each cross edge occurs in exactly two side triangles. Summing frustrated-edge incidences over the \(2n\) triangles gives
\[
2d+r_a+r_b\ge2n.
\]
The total number of frustrated edges is \(F=d+r_a+r_b\); thus
\[
F\ge n+\frac{r_a+r_b}{2}.
\]
A cyclic spin sequence has an even number of spin changes. Therefore \(r_a\equiv r_b\equiv n\pmod2\). For even \(n\), \(F\ge n\); for odd \(n\), \(F\ge n+1\). Since \(|E|=4n\), the zero-field energy is \(J(2F-4n)\).

**Even case.** Each rim can alternate its spins, giving \(r_a=r_b=0\). The four possible choices of initial ring spins make every side triangle contain precisely one frustrated cross edge; hence \(F=n\). Conversely, equality \(F=n\) in the bound forces \(r_a=r_b=0\) and precisely one frustrated edge on each triangle. Thus exactly four ground states exist, and each has \(M=0\).

**Odd case.** Equality \(F=n+1\) requires \(r_a=r_b=1\) and exactly one frustrated edge per triangle. Choose independently the positions \(a,b\) of the unique frustrated rim bonds. By cyclic rotation and a global spin flip we may put \(a=0\), set \(a_0=a_1=+1\), and obtain \(a_i=(-1)^{i-1}\) for \(1\le i\le n-1\). The exceptional top triangle forces \(b_0=-1\). For a prescribed bottom defect bond at \(b\), the bottom spins are then uniquely
\[
b_i=\begin{cases}-(-1)^i,&0\le i\le b,\\(-1)^i,&b<i\le n-1.\end{cases}
\]
For the bottom exceptional triangle, \(a_{b+1}=-b_b\), with cyclic interpretation of \(a_n=a_0\), as is checked directly from these formulas. All other side triangles have opposite rim spins and hence precisely one frustrated cross edge. Thus every pair of defect positions determines exactly two ground configurations, related by global reversal. There are \(n^2\) such pairs, so the degeneracy is \(2n^2\). Conversely the lower-bound equality forces one defect per rim, so no ground state has been missed.

For the above normalization, \(\sum_i a_i=+1\), and the bottom-ring magnetization is \(-1\) when \(b\) is even and \(+1\) when \(b\) is odd. Among \(b=0,\ldots,n-1\), exactly \((n+1)/2\) values are even and \((n-1)/2\) are odd. For each of the \(n\) choices of top defect, the latter give one configuration with \(M=+2\) and its global reversal with \(M=-2\), while the former give two configurations with \(M=0\). Hence
\[
\Omega_n(+2)=\Omega_n(-2)=\frac{n(n-1)}2,\qquad
\Omega_n(0)=n(n+1).
\]
This proves the claimed complete magnetization polynomial.

At finite \(n\), the partition function has finitely many energies, so as \(T\downarrow0\) its Gibbs probabilities converge to equal probabilities on the ground-state manifold. The fluctuation-response identity at zero field is \(k_BT\chi_n(T)=\langle M^2\rangle_{T,0}-\langle M\rangle_{T,0}^2\). Global spin reversal gives the second term zero. For odd \(n\), the ground-state variance is \(4n(n-1)/(2n^2)=2(n-1)/n\); for even \(n\), it is zero. This proves the Curie-coefficient formula.

## Verification

The standalone Python 3 script `verify.py` uses only standard-library modules. It implements two independent representations: (i) a direct, labeled four-edge-family antiprism graph enumerated over all spins for \(3\le n\le9\); and (ii) an exact minimum-energy dynamic program on the isomorphic squared cycle \(C_{2n}^2\), with magnetization tracking, for every \(3\le n\le80\). The two routines independently reproduce the predicted minimum frustrated-edge counts and magnetization polynomials. All 319 assertions passed in a clean execution.

Run `python3 verify.py` from the directory containing this file. This finite computation is not used as an infinite proof; the preceding face-counting and defect arguments establish the formulas for all \(n\ge3\).

## Relationship to prior work

Antiprism graphs are identified with squared cycles in the graph reference cited below. The Ising interpretation is consequently a nearest/next-nearest-neighbor classical triangular ladder. Dublenych's 2011 preprint (public webpage dated 2012-02-08) and the later 2013 journal version study ground-state structure and anisotropy on an infinite triangular lattice via an effective chain with interactions up to distance two; the examined material does not state this finite-antiprism parity-resolved degeneracy or Curie coefficient. The published work on antiferromagnetic Ising models in stack triangulations derives different bounds through planar triangulation and perfect-matchings, not these exact finite antiprism counts. Garuchava's 2025 preprint (revised 2026) addresses a generalized periodic triangular ladder with additional three-spin interactions and ground-state phases; it explicitly notes finite-size realizability constraints, and its examined results do not furnish the exact formulas above. Standard transfer-matrix methods could in principle reproduce them, but a general method alone is not the stated parity-resolved evaluation.

## Limitations

This is a finite-size zero-field theorem for classical spins with equal positive edge couplings; it does not give the all-field ground-state diagram, finite-temperature susceptibility curve, dynamic relaxation, or a thermodynamic phase transition. The Curie-limit order of limits is important. Historical priority remains provisional: an older finite-range Ising transfer-matrix table could contain an equivalent formula even without antiprism terminology. The theorem has not undergone independent scientific validation.

## References

- Antiprism Graph, MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html (graph identification).
- Yu. I. Dublenych, *Ground states of the Ising model on the anisotropic triangular lattice: Stripes and zigzags*, ICMP preprint 11-11U, public listing dated 2012-02-08, https://icmp.lviv.ua/en/preprints/2011/11-11u ; journal version, *J. Phys.: Condens. Matter* 25 (2013), 406003, https://doi.org/10.1088/0953-8984/25/40/406003 .
- *Antiferromagnetic Ising model in triangulations with applications to counting perfect matchings*, *Discrete Applied Mathematics* 172 (2014), 45–61, https://doi.org/10.1016/j.dam.2014.02.016 .
- Shota Garuchava, *Ground states of the Ising model at fixed magnetization on a triangular ladder with three-spin interactions*, arXiv:2511.05948v2 (2026 revision of a 2025 preprint), https://arxiv.org/html/2511.05948v2 .
