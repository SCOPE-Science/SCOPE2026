# Parity-controlled weak-channel jamming for alternating-rate lattice rods

## Finding
For every integer rod length \(k\ge4\), place consecutive \(k\)-site rods irreversibly on the initially vacant integer lattice. Independent rods beginning at even sites attempt adsorption at rate \(1\); those beginning at odd sites attempt at rate \(\varepsilon>0\). An attempt succeeds only when its entire footprint is vacant. Let \(C_0(t;\varepsilon)\) and \(C_1(t;\varepsilon)\) be the respective occupation probabilities of one even and one odd lattice site.

Put
\[
 r=\lceil k/2\rceil,\qquad H_{r-1}=\sum_{j=1}^{r-1}\frac1j,\qquad Q_r=e^{-2H_{r-1}},
\]
\[
 \Theta_r=r\int_0^\infty\exp\left[-u-2\sum_{j=1}^{r-1}\frac{1-e^{-ju}}j\right]du.
\]
The last quantity is the classical saturated occupation fraction of uniform length-\(r\) rods on a unit lattice. At every fixed slow time \(s>0\), the following limits are exact:

* If \(k=2r\ge4\), then
\[
\lim_{\varepsilon\downarrow0}\left(C_0(s/\varepsilon;\varepsilon),C_1(s/\varepsilon;\varepsilon)\right)=(\Theta_r,\Theta_r).
\]
* If \(k=2r-1\ge5\), then
\[
\lim_{\varepsilon\downarrow0}\left(C_0(s/\varepsilon;\varepsilon),C_1(s/\varepsilon;\varepsilon)\right)=\left(\Theta_r+(r-1)Q_r(1-e^{-s}),\frac{r-1}{r}\Theta_r+rQ_r(1-e^{-s})\right).
\]

Let \(\rho_k(\varepsilon)=\lim_{t\to\infty}[C_0(t;\varepsilon)+C_1(t;\varepsilon)]/2\), including the separately defined zero-rate dynamics at \(\varepsilon=0\). The jump at the boundary is
\[
 \boxed{\lim_{\varepsilon\downarrow0}\rho_k(\varepsilon)-\rho_k(0)=\begin{cases}0,&k\text{ even},\\ \dfrac{k}{2}e^{-2H_{(k-1)/2}},&k\text{ odd}.\end{cases}}
\]
For odd lengths it is strictly positive and decays as \(2e^{-2\gamma}/k\) when \(k\to\infty\), where \(\gamma\) is Euler's constant. In particular, the first length beyond the previously studied dimers and trimers to display a singular jump is \(k=5\), with jump \(5e^{-3}/2\).

## Assumptions and scope
Each candidate footprint \(\{i,i+1,\ldots,i+k-1\}\) has a spatially independent exponential first-arrival clock of rate \(1\) for even \(i\) and rate \(\varepsilon\) for odd \(i\). Later attempts at the same site are irrelevant because vacancy decreases in time. The infinite-volume process is the local limit of finite systems and is well-defined by finite backward dependency clusters. Coverage always means one-site occupation probability, not the event that infinitely many sites are all covered. The slow-time limit holds for each fixed \(s>0\), not uniformly at \(s=0\). The zero-rate case removes the odd clocks from the beginning, rather than taking an infinite-time positive-rate limit.

## Proof
**1. Priority reduction and the singular order of limits.** Give each start site an independent first-attempt time. Sorting these times and accepting a footprint if its sites remain empty produces the irreversible adsorption dynamics. Two candidate starts can interact only if their indices differ by at most \(k-1\). The accepted state of a fixed finite neighborhood can therefore be determined by exploring backward paths of strictly decreasing times in this bounded-degree conflict graph. The number of length-\(\ell\) paths from a fixed candidate is at most \([2(k-1)]^\ell\). Along each path of distinct candidates, at least \(\lceil(\ell+1)/2\rceil\) have the same start parity; within that subsequence the independent clocks are identically distributed, so the required ordering has probability at most \(1/\lceil(\ell+1)/2\rceil!\). The resulting summable upper bound holds uniformly in \(\varepsilon>0\). Thus local ancestor clusters can be truncated with an arbitrarily small error uniformly over the rates.

Couple the clocks as \(T_i=E_i\) at even starts and \(T_i=E_i/\varepsilon\) at odd starts, where all \(E_i\) are independent unit exponentials. On any finite truncated ancestor set, every relevant even-start attempt precedes every odd-start attempt as \(\varepsilon\downarrow0\). At time \(t=s/\varepsilon\), all relevant even attempts have also occurred and an odd attempt has occurred exactly when \(E_i\le s\). The uniform ancestor bound therefore proves convergence of the local positive-rate process to two stages: first saturate all even-start candidates, then accept independently clocked odd-start candidates at unit slow time. Applying the same argument to terminal occupied states (without a time cutoff) proves convergence of jammed one-site probabilities. This separately justifies the two orders of limits; no interchange is assumed.

**2. Fast-stage compression.** Write an even candidate start as \(2j\). Two such length-\(k\) rods conflict exactly when the compressed start separation is at most \(r-1\), where \(r=\lceil k/2\rceil\). Their random-priority acceptance law is thus exactly the usual uniform length-\(r\) lattice-rod RSA on the compressed line. The accepted density is \(\Theta_r/r\) per compressed start. If \(k=2r\), each accepted fast rod covers \(r\) sites of each physical parity, giving the fast profile \((\Theta_r,\Theta_r)\). If \(k=2r-1\), it covers \(r\) even sites and \(r-1\) odd sites, giving \((\Theta_r,(r-1)\Theta_r/r)\).

**3. Exact maximal-gap density.** In the compressed length-\(r\) RSA let \(E_\ell(u)\) be the probability that \(\ell\) consecutive compressed sites remain vacant at unit time \(u\). For \(\ell\ge r-1\), the empty-interval evolution has the explicit solution
\[
 E_\ell(u)=\exp\left[-(\ell-r+1)u-2\sum_{j=1}^{r-1}\frac{1-e^{-ju}}j\right].
\]
Indeed, the \(\ell-r+1\) internal candidate starts (zero at \(\ell=r-1\)) and the two sets of \(r-1\) boundary-crossing starts give the differential equation
\[
 E_\ell'=-(\ell-r+1)E_\ell-2\sum_{j=1}^{r-1}E_{\ell+j},
\]
which the displayed formula satisfies because \(E_{\ell+j}/E_\ell=e^{-ju}\). The initial condition is one. Uniqueness follows from bounded-degree graphical dynamics, or the same finite-ancestor argument as above. Therefore \(E_{r-1}(\infty)=Q_r\). Since a saturated length-\(r\) packing cannot have \(r\) consecutive vacant sites, every surviving block of \(r-1\) empty sites is exactly one maximal gap. Its intensity per compressed location is \(Q_r\). Independently, depositing rods at rate one gives \(\Theta_r=r\int_0^\infty E_r(u)du\), as used in the statement. These uniform-RSA formulas are standard and are not claimed as new.

**4. Odd versus even physical gaps.** Between consecutive accepted even-start physical rods, let \(g\in\{0,\ldots,r-1\}\) be their compressed vacant-gap length. Their compressed start distance is \(r+g\). Hence the corresponding physical vacant-gap length is
\[
 2(r+g)-k=\begin{cases}2g,&k=2r,\\2g+1,&k=2r-1.\end{cases}
\]
When \(k=2r\), all physical gaps have length at most \(k-2\). No odd-start rod can ever fit; this proves the even-length formulas at all slow times. When \(k=2r-1\), only the compressed maximal gaps \(g=r-1\) have physical length \(k\); these are filled exactly by one odd-start rod each. Such eligible odd footprints are pairwise disjoint. They occur at intensity \(Q_r/2\) per original site and fill independently by slow time \(s\) with probability \(1-e^{-s}\). Each successful odd-start rod covers \(r-1\) even and \(r\) odd physical sites. Dividing by the density \(1/2\) of each parity class adds \((r-1)Q_r(1-e^{-s})\) and \(rQ_r(1-e^{-s})\) to the respective occupancy probabilities. This proves both parity-resolved formulas and, on sending \(s\to\infty\), the stated jamming jump.

**5. Long-rod asymptotic.** For odd \(k=2r-1\), \(H_{r-1}=\log(r-1)+\gamma+O(r^{-1})\). Consequently \((k/2)e^{-2H_{r-1}}\sim e^{-2\gamma}/r\sim 2e^{-2\gamma}/k\). No uniformity in \(k\) is claimed for the small-rate limit.

## Verification
The standalone `verify.py` uses only the Python standard library. It independently generates random-priority two-stage jammed packings on periodic systems, checks that every eligible odd rod is disjoint from the others, checks that no odd rod remains feasible for even lengths, and compares parity-resolved slow-time coverage against the exact formulas for eight rod lengths and three positive slow times. Numerical Simpson integration also checks the classical uniform dimer and trimer coverage benchmarks. Running `python verify.py` reports `PARITY_STAGGERED_ADSORPTION_CHECKS_PASSED 2138`. Finite periodic Monte Carlo is supplementary and does not prove the infinite-chain statements, which follow from the analytical priority and empty-interval arguments.

## Relationship to prior work
The classical uniform length-\(r\) RSA coverage and largest-gap density are already known; in particular Pinsky (arXiv:2608.04730, Theorems 1 and 2 and the maximal-gap remark) records exactly \(\Theta_r\) and \(Q_r\), and a two-stage model involving rods **of different lengths**. The new claim is not these inputs but their physical start-sublattice compression and the resulting **same-length**, alternating-clock, parity-resolved limit for every \(k\ge4\). Earlier alternating-rate calculations cover dimers (even-length boundary) and trimers (odd-length singular boundary) individually. Their formulas are acknowledged as the two smallest special cases; this finding concerns the entire unbounded length family and its sharp parity-dependent distinction. Rodgers (1992) treats mixtures of two distinct rod lengths rather than periodic rates of fixed-length footprints. De Oliveira and Tomé (1994) study unequal adsorption probabilities on bipartite lattices, but the available abstract does not resolve whether their exclusion footprint yields any implication for the present k-mer theorem; that full-text comparison remains a priority risk. The new assertion does not depend on an unproved numerical extrapolation from the dimer/trimer cases.

## Limitations
There is no claim of a formula for arbitrary positive rate ratio, a convergence speed in the weak-rate limit, all-time uniformity down to the initial time, or a simultaneous limit in \(\varepsilon\) and growing \(k\). The large-length asymptotic is taken after the positive-rate-to-zero limit at each fixed length. The model is one-dimensional, has rods of one fixed length, and has strictly periodic start-position rates. Existing uniform-RSA input formulas and the earlier individual dimer/trimer results are not novel contributions. Full historical priority remains subject to external examination, including an inaccessible closely relevant 1994 source; independent scientific validation has not occurred.

## References
1. G. J. Rodgers, *Random sequential adsorption of different-sized k-mers on a line*, Physical Review A **45**, 3432 (1992), https://doi.org/10.1103/PhysRevA.45.3432 (published 1992-03-01).
2. M. J. de Oliveira and T. Tomé, *Inhomogeneous random sequential adsorption on bipartite lattices*, Physical Review E **50**, 4523 (1994), https://doi.org/10.1103/PhysRevE.50.4523.
3. R. G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730v1 (2026-08-05), https://arxiv.org/abs/2608.04730, in particular Theorems 1, 2 and 4.
4. *Exact Bessel jamming law for alternating-rate dimers on the integer chain*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-bessel-jamming-law-for-alternating-rate-dimers-on-the-inte--62e8a2fea2b8.
5. *Parity-resolved trimer jamming with a singular slow-rate crossover*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-parity-resolved-trimer-jamming-with-a-singular-slow-rate-crossov--8dc0ad127255.
