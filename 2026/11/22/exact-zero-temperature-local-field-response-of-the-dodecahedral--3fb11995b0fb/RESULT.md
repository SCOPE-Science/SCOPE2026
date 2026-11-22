# Exact zero-temperature local-field response of the dodecahedral Ising antiferromagnet

## Finding

Let \(D\) be the ordinary twenty-vertex dodecahedral graph, and give its thirty edges identical antiferromagnetic Ising coupling \(J>0\). At zero external field, put the uniform probability measure on its classical ground configurations, and define \(C_{uv}=\mathbb E_0(\sigma_u\sigma_v)\), where \(\sigma_u\in\{-1,+1\}\). The complete covariance matrix is determined solely by graph distance \(d_D(u,v)\):

| \(d_D(u,v)\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| \(C_{uv}\) | \(1\) | \(-3/5\) | \(1/5\) | \(-3/25\) | \(1/5\) | \(-31/125\) |

Its complete real eigenvalue multiset is

\[
\operatorname{spec}(C)=\left\{
\left(\frac{4}{125}\right)^{[1]},\ \left(\frac{24}{125}\right)^{[5]},\ \left(\frac{36}{125}\right)^{[4]},\ \left(\frac{204}{125}\right)^{[4]},\
\left(\frac{236-100\sqrt5}{125}\right)^{[3]},\
\left(\frac{236+100\sqrt5}{125}\right)^{[3]}
\right\},
\]
where bracketed superscripts denote multiplicities rather than powers. In particular, \(C\) is positive definite, its unique least-responsive normalized field direction is the uniform vector, and the maximal-to-minimal local-field Curie response ratio is exactly

\[
\frac{\lambda_{\max}(C)}{\lambda_{\min}(C)}=59+25\sqrt5.
\]

## Assumptions and scope

The classical Hamiltonian with local probe fields is
\[
H_{J,\mathbf h}(\boldsymbol\sigma)=J\sum_{uv\in E(D)}\sigma_u\sigma_v-\sum_{u\in V(D)}h_u\sigma_u,
\qquad J>0,
\]
with \(\boldsymbol\sigma\in\{-1,+1\}^{20}\). Take the local linear-response derivative at \(\mathbf h=0\) at each finite inverse temperature \(\beta\) before taking the zero-temperature limit. Thus
\[
\chi_{uv}(\beta)=\left.\frac{\partial\langle\sigma_u\rangle_{\beta,\mathbf h}}{\partial h_v}\right|_{\mathbf h=0}
=\beta\,\operatorname{Cov}_{\beta,\mathbf0}(\sigma_u,\sigma_v),\quad
\lim_{\beta\to\infty}\beta^{-1}\chi_{uv}(\beta)=C_{uv}.
\]
The result does not concern finite applied probe fields, a broken-symmetry choice of one ground state, a quantum transverse-field Hamiltonian, or an infinite-volume phase transition.

For explicit reproducibility, label the vertices \(0,\ldots,19\). The ordered edge list is embedded in both accompanying checkers, and the twelve oriented pentagonal faces appear in the face-dual checker. These data specify the ordinary dodecahedral graph up to vertex relabelling.

## Proof

**1. A finite frustration bound and dual description.** Each of the twelve pentagonal faces has an odd number of ferromagnetically aligned (frustrated) bonds in any spin configuration. Every edge borders two faces, so the number of frustrated edges is at least six; therefore \(H_{J,\mathbf0}\ge-18J\). Equality forces exactly one frustrated edge on each face. In the planar dual icosahedral graph, the corresponding six dual edges form a perfect matching. Conversely, each such dual perfect matching prescribes ferromagnetic alignment on its six primal edges and antiferromagnetic alignment on the remaining 24. Around every pentagonal face the product of prescribed bond signs is \(+1\), and facial cycles generate the entire cycle space of the planar connected graph. Consequently, the signs integrate to exactly two consistent spin assignments, related by simultaneous spin reversal.

The dual perfect matchings are enumerated by the finite recurrence: on an unmatched nonempty face set choose its least-labelled vertex, pair it with each still-unmatched dual neighbour, and recurse on the remaining set. The attached standard-library checker reports exactly 125 matchings, establishing exactly 250 ground spin configurations and the attainment of energy \(-18J\). This ground-state count and energy are consistent with the established dodecahedral Ising calculations [1], and are not claimed as new.

**2. Exact two-point correlations.** For each of the 125 perfect matchings, fix one spin \(+1\) at vertex zero and recover the other spins by graph traversal, applying the edge prescription from step 1. Both global choices produce the same pair products. Explicit summation of \(\sigma_u\sigma_v\) for every ordered pair of vertices gives the following integer numerators, each over 250 ground assignments:

| Graph distance | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Correlation numerator | 250 | -150 | 50 | -30 | 50 | -62 |

The enumeration is exhaustive rather than statistical: all twelve faces and all dual matchings are constructed by an exact recursion, and every matching is integrated into both allowed spin configurations. The checker also verifies that all pairs at each graph distance have the same numerator, a fact consistent with distance transitivity of the dodecahedral graph. Global reversal symmetry implies \(\mathbb E_0\sigma_u=0\), so these are covariances.

**3. Exact response spectrum.** Write \(N=250C\). Computing its integer characteristic polynomial from the explicit 20-by-20 distance matrix gives
\[
\det(xI-N)=(x-8)(x-48)^5(x-72)^4(x-408)^4
(x^2-944x+22784)^3.
\]
The two roots of the quadratic are \(472\pm200\sqrt5\). Dividing all roots by 250 yields exactly the spectrum stated in the Finding. Since \(8<472-200\sqrt5\), the eigenvalue \(8/250=4/125\) is strictly smallest. The row sums of \(N\) equal eight, so the all-ones vector spans this simple eigenspace. The largest is \((472+200\sqrt5)/250\), with multiplicity three, giving ratio \((472+200\sqrt5)/8=59+25\sqrt5\).

**4. Physical response.** At finite inverse temperature, fluctuation-response differentiation of the finite partition function gives \(\chi(\beta)=\beta\operatorname{Cov}_{\beta,0}\). The energy gap above the finite ground set is strictly positive, hence the Gibbs measure tends to the uniform measure on the 250 ground configurations. Therefore the eigenvalues of \(C\) are exactly the limiting normalized local-field response eigenvalues. All 20 are strictly positive. In particular the total-magnetization variance is \(\mathbf1^TC\mathbf1=16/25\), consistent with [1]; its value by itself is not a new claim.

## Verification

Two independently constructed standard-library Python programs accompany this result.

- `verify_dual.py` constructs the twelve pentagonal faces, enumerates all 125 perfect matchings of the dual icosahedron, integrates each matching to its two ground configurations, and verifies all 400 covariance numerators by distance, plus the magnetization distribution.
- `verify_exhaustive.py` independently scans all \(2^{20}=1{,}048{,}576\) spin assignments, establishes the six-frustrated-edge minimum, recovers exactly 250 minimizers, and calculates the full 20-by-20 characteristic polynomial using exact integer matrix multiplication and Newton's identities (no floating-point eigenvalue determination).

Run them with a standard Python 3 interpreter. Both programs passed when run from the actual package files before serialization, and after extraction the same decoded bytes can be rerun independently. The finite graph and exhaustive index bounds, not a sampling assumption, make these calculations complete.

## Relationship to prior work

Strečka, Karlová and Madaras [1] already determined the dodecahedral Ising ground-state multiplicity, magnetization sectors and uniform-field magnetocaloric response; their zero-field ground-state degeneracy 250 is not presented here as novel. Konstantinidis [2] discusses the nearest-neighbour correlation and magnetic response in anisotropic classical dodecahedral magnets; the nearest-neighbour entry \(-3/5\) also is not claimed as new. Lopez-Bezanilla and collaborators [3] use the same 250-state manifold for a quantum-annealing benchmark, analysing resonant dimers rather than the exact all-distance classical covariance eigenspectrum. A published calculation for the 60-vertex fullerene [4] addresses a related local-response problem on a different graph. The contribution here is the explicit distance-three through antipodal correlations, the entire 20-mode local-field Hessian spectrum, and the rigorous sharp nonuniform-to-uniform response anisotropy. The listed work does not provide these exact quantities; this is an assessed literature comparison, not a proof that no earlier equivalent exists.

## Limitations

The result is confined to the ordinary 20-site dodecahedron, nearest-neighbour equal positive antiferromagnetic couplings, zero external field and a classical Ising ensemble. The limit differentiates at zero field before taking temperature to zero. The proof gives no quantum dynamical spectral properties, no stability to disorder or additional couplings, and no general result for arbitrary fullerenes. Exhaustive finite enumeration is a valid proof for this one finite network but does not imply a thermodynamic-limit law. An equivalent unindexed old calculation of the full covariance remains possible.

## References

[1] J. Strečka, K. Karlová, T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra* (first public arXiv version 2015-02-16), https://arxiv.org/abs/1502.04449.

[2] N. P. Konstantinidis, *Origin of the classical magnetization discontinuities of the dodecahedron* (2025), https://doi.org/10.1016/j.jmmm.2025.173061.

[3] A. Lopez-Bezanilla et al., *Quantum dynamics in frustrated Ising fullerenes* (2026), https://doi.org/10.1140/epjqt/s40507-026-00536-5.

[4] *Exact zero-temperature local-response spectrum of the C60 Ising antiferromagnet*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-zero-temperature-local-response-spectrum-of-the-c60-ising--68509e3863d8.
