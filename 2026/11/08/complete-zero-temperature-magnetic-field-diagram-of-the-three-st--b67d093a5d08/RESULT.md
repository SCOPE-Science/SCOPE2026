# Complete zero-temperature magnetic-field diagram of the three-state Potts antiferromagnet on the dodecahedron

## Finding
Let \(D\) denote the 20-vertex regular dodecahedral graph, with 30 edges. For the three-state antiferromagnetic Potts Hamiltonian
\[
H_{J,h}(\sigma)=J\sum_{uv\in E(D)}\mathbf 1_{\sigma_u=\sigma_v}-h\sum_{v\in V(D)}\mathbf 1_{\sigma_v=0},\qquad \sigma_v\in\{0,1,2\},\quad J>0,\quad h\in\mathbb R,
\]
the exact ground-state energy is
\[
\frac{E_0(h)}{J}=\begin{cases}
6,&h/J\le-1,\\
-6h/J,&-1\le h/J\le0,\\
-8h/J,&0\le h/J\le\frac32,\\
6-12h/J,&\frac32\le h/J\le3,\\
30-20h/J,&h/J\ge3.
\end{cases}
\]
There are four exact coexistence fields, \(h/J\in\{-1,0,3/2,3\}\). The favored-color occupancy \(k=|\{v:\sigma_v=0\}|\) and the complete ground-state degeneracy are:

| Field \(h/J\) | Ground occupancies \(k\) | Total degeneracy |
|---|---|---:|
| \(( -\infty,-1)\) | \(0\) | 250 |
| \(-1\) | \(0,1,2,3,4,5,6\) | 98770 |
| \((-1,0)\) | \(6\) | 2720 |
| \(0\) | \(6,7,8\) | 7200 |
| \((0,3/2)\) | \(8\) | 320 |
| \(3/2\) | \(8,10,12\) | 32320 |
| \((3/2,3)\) | \(12\) | 1280 |
| \(3\) | \(12,13,14,15,16,17,18,19,20\) | 212905 |
| \((3,\infty)\) | \(20\) | 1 |

The zero-field proper-three-coloring occupancy polynomial is \(2720w^6+4160w^7+320w^8\). It is included as a consistency check; the main contribution is the complete all-field energy and coexistence census, including configurations with violated antiferromagnetic bonds.

## Assumptions and scope
The model is classical, at exactly zero temperature, with three *labeled* spin colors and one singled-out color. There are no next-nearest-neighbor interactions; all 30 edges have identical positive penalty \(J\) for equal adjacent colors. The external field is a real number of either sign, coupled only to color 0. Degeneracies count distinct labeled configurations, without quotienting by graph or spin symmetry. All inequalities at field thresholds include equality; the energy pieces agree there.

For an explicit graph realization, write \(V(D)=\{u_i,v_i: i\in\mathbb Z/10\mathbb Z\}\), with edge families \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), where indices are reduced modulo 10. This is \(GP(10,2)\), the dodecahedral graph. The ten edges \(v_iv_{i+2}\) form two disjoint pentagons.

## Proof
For a configuration \(\sigma\), let \(k(\sigma)\) count sites in color 0 and let \(p(\sigma)\) count equal-color edges. Then \(H_{J,h}(\sigma)=Jp(\sigma)-hk(\sigma)\). For each integer \(0\le k\le20\), define \(p_k=\min_{\sigma:k(\sigma)=k}p(\sigma)\), and let \(N_k\) be the number of configurations attaining this minimum. A complete, finite min-plus count yields:

| \(k\) | \(p_k\) | \(N_k\) | \(k\) | \(p_k\) | \(N_k\) |
|---:|---:|---:|---:|---:|---:|
|0|6|250|11|5|115200|
|1|5|3000|12|6|1280|
|2|4|13800|13|9|40960|
|3|3|30400|14|12|79360|
|4|2|32760|15|15|61184|
|5|1|15840|16|18|24160|
|6|0|2720|17|21|5280|
|7|0|4160|18|24|640|
|8|0|320|19|27|40|
|9|2|57600|20|30|1|
|10|3|30720||||

Here is an exhaustive recurrence establishing this finite table. Fix any coloring \(a_i=\sigma(v_i)\) of all ten inner vertices. Its inner-edge penalty is \(p_{\rm in}=\sum_i\mathbf 1_{a_i=a_{i+2}}\) and its favored-color count is \(k_{\rm in}=\sum_i\mathbf 1_{a_i=0}\). Enumerate all \(3^{10}\) possible \(a\). For each choice of initial outer color \(b_0\in\{0,1,2\}\), maintain a min-plus state \(F_i(c,r)\): the least accumulated penalty through outer vertex \(u_i\), with \(\sigma(u_i)=c\), using exactly \(r\) zero-colored outer vertices. Alongside its cost, carry the exact integer number of minimizers, adding counts in equal-cost ties.

Initialize \(F_0(b_0,\mathbf1_{b_0=0})=\mathbf1_{b_0=a_0}\), with count one; other states are inaccessible. For \(1\le i\le9\), make the exhaustive transition
\[
F_i(c,r)=\mathbf1_{c=a_i}+\min_{d\in\{0,1,2\}}
\bigl(F_{i-1}(d,r-\mathbf1_{c=0})+\mathbf1_{d=c}\bigr),
\]
again summing counts over all minimizing predecessors. For each final outer color \(b_9\), add \(\mathbf1_{b_9=b_0}\) to close the outer decagon, add \(p_{\rm in}\) to the cost and \(k_{\rm in}\) to the occupancy, and merge by global minimum at that occupancy. This enumerates every spin assignment exactly once: every assignment has exactly one inner coloring, initial outer color, and chain of successive outer colors. Thus the resulting \((p_k,N_k)\) table is exhaustive, not a sample or asymptotic approximation.

As an independent decomposition, first enumerate all \(3^{10}\) outer decagon colorings, then optimize and count each of the two inner five-cycles separately by enumerating their \(3^5\) colorings; combine their independent costs and zero counts by exact convolution. The independent algorithm reproduces every entry of the table.

Finally, \(E_0(h)=\min_{0\le k\le20}(Jp_k-hk)\). Taking the lower envelope of the 21 affine functions yields precisely the five pieces above, with active occupancy sets \(\{0\}\), \(\{6\}\), \(\{8\}\), \(\{12\}\), and \(\{20\}\) on successive open field intervals. At the four boundary fields, the entire sets of tied occupancies shown in the first table are obtained by exact equality of their affine energies. Summing the respective \(N_k\) gives the stated degeneracies.

## Verification
The included standalone scripts `verify_inner_ring.cpp` and `verify_outer_pentagons.py` implement the two different exhaustive decompositions, and both assert all 21 sector costs and counts. The second also checks the ground occupancies and coexistence multiplicities with exact rational arithmetic. Reproduction commands from the extracted file directory:

```sh
g++ -std=c++17 -O2 verify_inner_ring.cpp -o verify_inner_ring
./verify_inner_ring
python3 verify_outer_pentagons.py
```

Their success markers are `INNER_RING_DP_OK` and `INDEPENDENT_PENTAGON_OK`. The complete \((k,p_k,N_k)\) data are also supplied in `SECTOR_TABLE.csv`. All arithmetic in the two enumerators is integral, apart from exact fractions used for the field comparisons; no numerical fit or floating-point tolerance enters the result.

## Relationship to prior work
Chang's 2000 chromatic-polynomial calculation treats a family of generalized dodecahedra, explicitly identifying the ordinary dodecahedron as its five-cell member; it therefore covers zero-field proper-coloring enumeration, not the all-field competition among improper configurations. Shrock and Xu (2010) give general field-dependent Potts partition functions and weighted proper colorings, while Ellis-Monaghan and Moffatt (2010/2011) establish a general field-inclusive graph-polynomial framework. Their general identities can encode this finite model but do not furnish the evaluated dodecahedral field thresholds or degenerate ground-state sectors. Strečka, Karľová and Madaras (2015) study the same Platonic geometry for the two-state Ising antiferromagnet, not the present three-state Potts response. The present result is an exact graph-specific evaluation, not a new general Potts representation or a claim of novelty for the ordinary chromatic polynomial.

## Limitations
The result applies only to this 20-vertex graph, three labeled colors, equal positive nearest-neighbor coupling and a one-color field. It does not establish finite-temperature observables, lattice thermodynamic limits, robustness to inhomogeneous couplings, or a general fullerenes theorem. Its critical degeneracies refer to exact algebraic coexistence fields; perturbations may lift them. Historical priority for an unindexed equivalent Potts enumeration remains a residual risk. Independent external mathematical audit has not been performed.

## References
1. S.-C. Chang, *Chromatic Polynomials for Lattice Strips with Cyclic Boundary Conditions* (public preprint 2000-10-20), arXiv:cond-mat/0010321, https://arxiv.org/abs/cond-mat/0010321, especially the \(O_m\) family and \(O_5\).
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings* (public preprint 2010-09-07), arXiv:1009.1182, https://arxiv.org/abs/1009.1182.
3. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts Connection in the Presence of an External Magnetic Field* (public preprint 2010-05-29), arXiv:1005.5470, https://arxiv.org/abs/1005.5470.
4. J. Strečka, K. Karľová and T. Madaras, *Giant Magnetocaloric Effect, Magnetization Plateaux and Jumps of the Regular Ising Polyhedra* (public preprint 2015-02-16), arXiv:1502.04449, https://arxiv.org/abs/1502.04449.
