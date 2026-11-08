# The first eight-cycle threshold beyond the four-cycle phase of symmetric negative-doubling holes

## Finding

For every real parameter \(2/5\le a\le7/17\), consider the negative-doubling interval map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1,\end{cases}
\]
with open hole \(H_a=(a,1-a)\) and compact survivor
\[
S_a=\{x\in[0,1]: T^j(x)\notin H_a\text{ for all integers }j\ge0\}.
\]
The map is only evaluated on the survivor, which avoids \(1/2\). Every survivor is eventually periodic. For all \(2/5\le a<7/17\), the complete list of primitive periodic orbits is the two-cycle \(\{0,1\}\), two fixed points \(\{1/3\}\) and \(\{2/3\}\), and the four-cycle \(\{1/5,3/5,4/5,2/5\}\). At the *sharp* threshold \(a=7/17\), precisely one further primitive orbit appears, the eight-cycle
\[
\frac1{17}(7,3,11,12,10,14,6,5),
\]
where the displayed tuple is in temporal order. No other periodic orbits exist at or below this threshold within the stated parameter interval.

Thus, for every integer \(n\ge1\) and \(2/5\le a\le7/17\),
\[
\#\operatorname{Fix}(T^n|_{S_a})=
2\mathbf1_{2\mid n}+2+4\mathbf1_{4\mid n}
+8\mathbf1_{a=7/17}\mathbf1_{8\mid n},
\]
and the Artin–Mazur zeta function is exactly
\[
\zeta_a(z)=\frac{1}{(1-z^2)(1-z)^2(1-z^4)}
(1-z^8)^{-\mathbf1_{a=7/17}}.
\]
In particular \(h_{\mathrm{top}}(T|_{S_a})=0\) and \(\dim_{\mathrm H}S_a=0\) throughout this window, although the full periodic-orbit spectrum jumps at its right endpoint.

## Assumptions and scope

The dynamical system is the *interval* negative-doubling map, not the circle quotient. In particular \(T(0)=1\), \(T(1)=0\), so \(\{0,1\}\) is a genuine two-cycle. Both endpoints of the open hole survive whenever their forward iterates avoid the hole. The stated result concerns exact real parameters in the closed interval \([2/5,7/17]\) and all positive iterate orders, with no numerical discretization or bounded-period assumption.

## Proof

**1. Reduction to the right endpoint.** The retained sets \(K_a=[0,a]\cup[1-a,1]\) are nested as \(a\) increases. Hence \(S_a\subseteq S_{7/17}\) for every \(a\le7/17\). It is enough to classify all eventual dynamics at \(a_*=7/17\), then test which of its periodic orbits survive smaller holes.

**2. A forward-invariant finite boundary set.** At \(a_*\), both hole endpoints belong to the same primitive eight-cycle:
\[
7\mapsto3\mapsto11\mapsto12\mapsto10\mapsto14\mapsto6\mapsto5\mapsto7,
\]
where all entries are divided by \(17\). The further boundary points \(0\) and \(1\) form the two-cycle \(0\mapsto1\mapsto0\). Consequently the retained set \(K_{a_*}\) has the following eight closed Markov intervals, whose endpoints are forward invariant:
\[
I_0=[0,3]/17,\ I_1=[3,5]/17,\ I_2=[5,6]/17,\ I_3=[6,7]/17,
\]
\[
I_4=[10,11]/17,\ I_5=[11,12]/17,\ I_6=[12,14]/17,\ I_7=[14,17]/17.
\]
Here \([u,v]/17\) means \([u/17,v/17]\). On each interval the map is affine decreasing with slope \(-2\). Directly applying its two branch formulas and discarding target intervals in the open hole produces the exact *full-cell* transition table:

| Source | Allowed successors |
| --- | --- |
| \(I_0\) | \(I_5,I_6,I_7\) |
| \(I_1\) | \(I_4\) |
| \(I_2\) | \(I_2,I_3\) |
| \(I_3\) | \(I_1\) |
| \(I_4\) | \(I_6\) |
| \(I_5\) | \(I_4,I_5\) |
| \(I_6\) | \(I_3\) |
| \(I_7\) | \(I_0,I_1,I_2\) |

For example, \(T(I_0)=[11,17]/17\) and \(T(I_7)=[0,6]/17\), explaining the first and last rows. All entries follow from the other six endpoint-image calculations, which the standalone checker reproduces using exact rational arithmetic.

**3. Eventual periodicity.** Any survivor whose orbit ever meets a partition endpoint is eventually on the listed eight-cycle or two-cycle. For every other survivor, each iterate belongs to the interior of a unique cell, and its infinite cell itinerary follows the directed graph in the table. The graph's strongly connected components are exactly
\[
\{0,7\},\quad\{1,3,4,6\},\quad\{2\},\quad\{5\}.
\]
Each component is a single directed cycle (of lengths \(2,4,1,1\), respectively). The finite acyclic condensation graph ensures that every infinite path eventually stays in one of these components. Its cell itinerary is therefore eventually periodic. For a fixed cycle itinerary of length \(p\), the corresponding iterate is affine of slope \((-2)^p\); repeated inverse branches contract by \(2^{-p}\). Thus there is exactly one point following that cycle forever, and that point is periodic. Every survivor is hence eventually periodic, not merely asymptotic to a periodic orbit.

**4. Complete periodic-orbit list.** The unique points on the four interior graph cycles are, respectively, \(0\leftrightarrow1\), the four-cycle \(1/5\mapsto3/5\mapsto4/5\mapsto2/5\mapsto1/5\), and the fixed points \(1/3\) and \(2/3\). The only additional periodic points on partition boundaries are the eight distinct points listed in Step 2. The graph decomposition excludes every other primitive period, including arbitrarily large periods.

**5. Sharp parameter cutoff.** Each point of the two-cycle, fixed points and four-cycle lies outside \((a,1-a)\) for every \(a\ge2/5\). The eight-cycle includes \(7/17\) and \(10/17\), so it survives exactly when \(a\ge7/17\). By monotonicity, no further periodic orbit can survive for \(2/5\le a<7/17\). This proves both the sharp birth of the unique eight-cycle and the nonexistence of any intermediate higher-period orbits.

**6. Zeta, cardinality, entropy.** A primitive orbit of length \(p\) contributes \(p\) points to \(\operatorname{Fix}(T^n)\) precisely when \(p\mid n\), and contributes \((1-z^p)^{-1}\) to the Artin–Mazur zeta. This gives the formulas. Since every point eventually enters the displayed finite periodic set, the full survivor is a subset of the countable union of its finite preimage sets, hence countable and of Hausdorff dimension zero. Every invariant probability measure is supported on periodic points by Poincaré recurrence, and so has zero measure entropy; the variational principle for the compact continuous restriction \(T|_{S_a}\) gives topological entropy zero.

## Verification

The self-contained standard-library Python program `verify_period_window.py` reconstructs the eight Markov intervals and all 14 graph edges from the exact branch formulas, computes strongly connected components by an independent reachability algorithm, and verifies all five listed primitive orbits. It also independently enumerates exact rational periodic points of every order through \(16\) at four parameters, including both endpoints and two interior samples; it obtains `VERIFY_OK checks=89`. Exhaustive finite-period enumeration is a *diagnostic only*. The proof for arbitrary iterate order and every real parameter is the graph argument in Steps 2–5.

To reproduce, run `python3 verify_period_window.py` with a standard Python 3 installation; no network, packages or external files are required.

## Relationship to prior work

Ding, Steiner and Sun [1] establish a broad alternating-order and kneading description of negative-doubling open systems and prove survivor and entropy plateau results, but do not state this sharp symmetric-hole \(7/17\) period-eight cutoff or its exact all-order periodic census. The earlier published *three-phase* calculation [2] establishes the symmetric-hole census only through \(a=2/5\); its period-four endpoint and zeta factors agree with the left endpoint here. The present result extends the domain by an entire sharp natural phase and uses a different finite Markov partition at the first new eight-cycle boundary.

Glendinning and Hege [3] analyze the general boundary of chaos for piecewise-monotone maps and associated survivor sets, including finite-periodic-orbit transition mechanisms; their statements do not identify this rational symmetric-hole endpoint or the exact periodic census. Olivares-Vinales [4] treats Artin–Mazur zeta functions for interval maps broadly and shows rationality phenomena, without the explicit negative-doubling window and retained boundary cycles considered here. A general kneading formalism can in principle be specialized to rational parameters; the novelty claim is the exact sharp classification and its proof, not invention of kneading theory or Markov presentations.

## Limitations

No positive entropy or appearance of any particular orbit for parameters larger than \(7/17\) is claimed. The result does not classify arbitrary asymmetric holes, nonlinear Lorenz maps or the count of transient preimages. The standalone exact-rational checker samples finitely many iterate orders and does not independently certify the infinite mathematical argument. Historical priority against every possible specialized negative-base hole computation has not been independently certified.

## References

[1] Y. Ding, W. Steiner and Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first public 2 October 2026), https://arxiv.org/html/2610.03327v1 .

[2] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes*, public published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c .

[3] P. Glendinning and C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429v1 (2025), https://arxiv.org/html/2508.21429v1 .

[4] J. Olivares-Vinales, *The Artin-Mazur zeta function for interval maps*, arXiv:2405.10560v2 (2024), https://arxiv.org/html/2405.10560v2 .
