# Sharp lane-layout bounds for counting noise in a one-vacancy exclusion cylinder

## Finding

Consider an exclusion process on a periodic cylinder of \(K\ge3\) lanes and \(L\ge2\) longitudinal sites per lane, with exactly one vacant site. A particle in lane \(i\in\mathbb Z/K\mathbb Z\) hops one site clockwise along its lane at rate \(p_i>0\) when the destination is vacant. It moves sideways into a vacant corresponding site on either neighboring lane at rate \(\chi>0\) per neighbor. Let \(N_t\) count **all** successful longitudinal particle hops throughout the cylinder during \([0,t]\), not hops through only one chosen cross-section.

Set
\[
\bar p=\frac1K\sum_{i=0}^{K-1}p_i,\qquad
F_j=\sum_{i=0}^{j-1}(p_i-\bar p),\quad 0\le j<K,\qquad
\bar F=\frac1K\sum_{j=0}^{K-1}F_j.
\]
Starting in the unique stationary distribution, the exact long-time count mean and variance rates are
\[
\lim_{t\to\infty}\frac{\mathbb E N_t}{t}=\bar p,
\qquad
\boxed{\lim_{t\to\infty}\frac{\operatorname{Var}(N_t)}t
=\bar p+\frac{2}{K\chi}\sum_{j=0}^{K-1}(F_j-\bar F)^2.}
\]
These quantities are independent of the longitudinal circumference \(L\).

In particular, fix \(K=2m\), \(m\ge2\), and assign rate \(a>b>0\) to exactly \(m\) lanes and rate \(b\) to the remaining \(m\). **Among all \(\binom{2m}{m}\) placements**, the variance rate \(\mathcal V\) satisfies the sharp bounds
\[
\boxed{
\frac{a+b}{2}+\frac{(a-b)^2}{8\chi}
\ \le\ \mathcal V\ \le\ 
\frac{a+b}{2}+\frac{(a-b)^2(m^2+2)}{24\chi}.}
\]
The lower equality occurs **exactly** when the two rates alternate cyclically; the upper equality occurs **exactly** when all \(a\)-rate lanes form one contiguous circular block. All placements have exactly the same stationary measure and mean total hop rate \((a+b)/2\). Yet the ratio of the non-Poissonian variance excesses at the two extremal arrangements is \((m^2+2)/3\), growing quadratically with the lane count.

## Assumptions and scope

The state space has \(KL\) configurations: a state specifies the lone vacancy's lane and longitudinal position. Periodic longitudinal motion is unidirectional, and lateral moves are allowed in both neighboring directions. Lateral rates are homogeneous and equal to \(\chi\); all stated rates are strictly positive. For \(K\ge3\), the two lateral neighbors are distinct. The finite process is irreducible, and its unique stationary distribution is uniform over vacancy positions. Expectations use this stationary initial law. The long-time variance is a variance *per unit time*; it is not an instantaneous occupancy variance, a single-bond current variance, or a large-system thermodynamic limit.

## Proof

**1. One-vacancy reduction and exact counting law.** If the vacancy occupies lane \(i\) and column \(j\), one successful clockwise particle hop in that lane moves the vacancy to column \(j-1\) at rate \(p_i\). A sideways particle hop moves the vacancy from lane \(i\) to lane \(i\pm1\), at rate \(\chi\) in each direction. The vacancy lane \(I_t\) is thus an autonomous continuous-time symmetric random walk on the \(K\)-cycle with generator
\[
(Qh)_i=\chi(h_{i+1}+h_{i-1}-2h_i).
\]
It is uniform in stationarity. Longitudinal moves leave the lane unchanged. By constructing longitudinal jumps from an independent Poisson random measure, conditional on \((I_s)_{0\le s\le t}\), their count is Poisson with integrated intensity \(\int_0^t p_{I_s}\,ds\). Therefore
\[
\operatorname{Var}(N_t)=\bar p t+
2\int_0^t(t-s)\operatorname{Cov}(p_{I_0},p_{I_s})\,ds.
\]
On the finite irreducible lane cycle, correlations decay exponentially. For \(f_i=p_i-\bar p\), the zero-mean Poisson equation \(-Qh=f\) consequently yields
\[
\lim_{t\to\infty}\frac{\operatorname{Var}(N_t)}t
=\bar p+2\langle f,h\rangle_{\mathrm{unif}}.
\]
The stationary vacancy distribution is uniform: at each site its incoming and outgoing longitudinal rates both equal its lane rate, while the two lateral incoming and outgoing rates are each \(\chi\).

**2. Cycle potential formula.** Put \(d_i=h_i-h_{i-1}\). The Poisson equation gives \(\chi(d_i-d_{i+1})=f_i\). Hence all \(d_i\) equal a common constant minus \(F_i/\chi\), with the common constant chosen so that \(\sum_i d_i=0\). Thus
\[
d_i=\frac{\bar F-F_i}{\chi}
\]
(up to a simultaneous cyclic shift in the choice of edge index). Discrete summation by parts gives
\[
\langle f,h\rangle_{\mathrm{unif}}
=\frac{\chi}{K}\sum_i(h_{i+1}-h_i)^2
=\frac1{K\chi}\sum_i(F_i-\bar F)^2.
\]
This proves the general formula.

**3. Binary rates and the minimum.** Write \(p_i=(a+b)/2+c s_i\), where \(c=(a-b)/2>0\), the signs \(s_i\in\{-1,1\}\), and \(\sum_i s_i=0\). Let \(H_j=\sum_{i=0}^{j-1}s_i\), with \(H_0=0\). The variance excess becomes
\[
\mathcal V-\bar p
=\frac{(a-b)^2}{2\chi}\operatorname{Var}_{j\in\mathbb Z/(2m)}(H_j).
\]
Each \(H_j\) is an integer of the same parity as \(j\). For any real \(z\), exactly half of the indices have even height and half odd height, so
\[
\frac1{2m}\sum_j(H_j-z)^2
\ge\frac12\operatorname{dist}(z,2\mathbb Z)^2
+\frac12\operatorname{dist}(z,2\mathbb Z+1)^2
\ge\frac14.
\]
Taking the minimum over \(z\) gives \(\operatorname{Var}(H)\ge1/4\). Equality forces one common even height at every even index and one common adjacent odd height at every odd index. Therefore the signs alternate, and this arrangement attains the lower bound.

**4. Sharp upper bound and rigidity.** Denote the \(m\) high-rate lane positions by the cyclic set \(S\). For the unit-rate cycle Laplacian \(\mathscr L\), the mean-zero Green kernel satisfies
\[
(\mathscr L^+)_{xy}=\frac{K^2-1}{12K}-\frac{d(K-d)}{2K},
\qquad d=|x-y|\pmod K,
\]
where the product \(d(K-d)\) does not depend on which of the two arcs is selected. This identity follows by applying \(\mathscr L\) to the displayed kernel and checking its zero row sum. Since \(s=2\mathbf1_S-\mathbf1\) and \(\mathscr L^+\mathbf1=0\), maximizing the variance excess is equivalent to minimizing
\[
E(S)=\sum_{\{x,y\}\subset S}d(x,y)(K-d(x,y)).
\]
Cyclically order the high-rate positions and let \(g_1,\ldots,g_m\ge1\) be their consecutive clockwise gaps, with \(\sum_i g_i=2m\). For an unordered pair of high-rate sites, choose its clockwise separation \(x\), a linear sum of some consecutive gaps. Its contribution is \(x(2m-x)\), which is strictly concave in \(x\). Hence \(E\) is a concave function on the gap simplex. It is **strictly concave** there: using coordinates \(g_1,\ldots,g_{m-1}\), the terms for consecutive ordered pairs include \(\sum_{i=1}^{m-1}g_i(2m-g_i)\), whose Hessian is negative definite, and all remaining summands have negative-semidefinite Hessian. A strict-concavity minimum on the simplex occurs only at vertices. Each vertex has exactly one gap equal to \(m+1\) and every other gap equal to one, precisely a contiguous block of high-rate lanes. Conversely every such block attains the common minimal \(E\), establishing uniqueness up to cyclic rotation.

For that block the heights \(H_j\), \(0\le j<2m\), consist of one zero, one \(m\), and two copies of each integer from one through \(m-1\). Their mean equals \(m/2\), their mean square equals \((2m^2+1)/6\), and their variance is \((m^2+2)/12\). Inserting this and the alternating height variance \(1/4\) into step 3 proves both bounds and the excess ratio.

## Verification

The accompanying `verify.py` uses standard-library exact rational arithmetic. It builds the **complete vacancy generator** on each finite cylinder, verifies its row sums and uniform stationarity, independently solves its full Poisson equation for longitudinal hop counts, and compares the resulting tilted-generator variance coefficient to the closed prefix-sum expression. It passed 18 full-generator checks on cylinders with \(K=3,4,5,6,8\), longitudinal sizes \(L=2,3\), and both binary and genuinely multivalued rate profiles. It also enumerated all 4,704 balanced binary arrangements for \(K=4,6,8,10,12,14\), checking the two exact sharp bounds and their equality cases. The finite enumeration is not used as proof of the all-size classification; that proof is in steps 3–4 above. Run from the delivered directory with `python3 verify.py`.

## Relationship to prior work

Ezaki and Nishinari derived exact factorized stationary measures and stationary currents for a toroidal heterogeneous multilane exclusion process. Their lane dynamics and product stationary law motivate the present one-vacancy, homogeneous-lane-change specialization. The inspected author-uploaded full manuscript describes the hopping and lane-switching rules and analyzes stationary measures and mean currents, not the long-time counting variance or sharp arrangement optimization. The 2011 published version's existence and date are independently verified by its journal record.

Markov-modulated Poisson-process theory already supplies general overdispersion and second-moment machinery, including the work of Asanjarani and Nazarathy. That general machinery is used rather than claimed here. The additional result is the closed cylinder-specific cycle potential and exact **all-placement** extremal classification, with rigidity and growing separation between different arrangements despite identical stationary laws. The full article by Ishiguro and Sato establishes general multidimensional stationary measures and studies mean currents for heterogeneous fast/slow lanes; it does not supply the long-time total-hop counting variance or the extremal layout classification.

## Limitations

The explicit rearrangement inequality requires exactly one vacancy, homogeneous symmetric lane-change rates, an even number of lanes, and an equal count of the two distinct longitudinal hopping rates. The general variance formula allows arbitrary positive longitudinal hopping rates and any \(K\ge3\) but still assumes exactly one vacancy and homogeneous lateral rates. No such arrangement bound is claimed at other densities, with lane-dependent lateral rates, or for a count through one fixed longitudinal bond. The count-noise limit is taken at each fixed finite cylinder before increasing the lane count. The proof does not assert optimality for full counting distributions or higher cumulants. Independent bibliographic confirmation remains outstanding.

## References

1. T. Ezaki and K. Nishinari, “Exact solution of a heterogeneous multilane asymmetric simple exclusion process,” *Physical Review E* **84**, 061141 (2011), DOI: 10.1103/PhysRevE.84.061141. Author-uploaded full manuscript: arXiv:1502.04804.
2. A. Asanjarani and Y. Nazarathy, “Stationary Markovian arrival processes: Results and open problems,” *ANZIAM Journal* **64**, 54–68 (2022), DOI: 10.1017/S1446181122000013; preprint arXiv:1905.01736.
3. Y. Ishiguro and J. Sato, “Exact steady states in the asymmetric simple exclusion process beyond one dimension,” *Physical Review Research* **6**, 033030 (2024), arXiv:2403.01934.
