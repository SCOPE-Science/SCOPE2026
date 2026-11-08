# Dyadic finite core chains and pointwise arcsine laws below the generalized Hata–Yano threshold

## Finding

For every integer \(k\ge 2\), consider the generalized Hata–Yano random interval maps at the parameter
\[
\delta_k=2^{-(k+2)},\qquad c_k=4\delta_k=2^{-k}.
\]
The induced core dynamics admits an explicit, irreducible \(2k\)-state invariant subsystem on which the transition operator is the simple random walk on a path with deterministic reflection at both endpoints. Its unique stationary probability is given explicitly below. Both of the core's two excursion gates have stationary mass \(1/[2(2k-1)]>0\). Independently, the original physical maps preserve the full, countable dyadic lattice and act there as a simple symmetric random walk **at every \(0<\delta\le1/6\)**. Thus the ordinary Lévy arcsine law holds from every point of that lattice, including all exhibited core nodes, with no use of a conditional induced-core theorem. The explicit finite-core stationary family addresses the source's invariant-measure question along infinitely many perturbations below \(1/8\) tending to zero; it does not settle all intervening parameters.

In addition, the complete core transition spectrum is
\[
\left\{\cos\left(\frac{j\pi}{2k-1}\right):0\le j\le 2k-1\right\}.
\]
The slowest nonperiodic spectral gap equals \(1-\cos(\pi/(2k-1))\sim\pi^2/[2(2k-1)^2]\). The endpoint-reflected chain has period two, so this gap is **not** an assertion of convergence of its one-step distribution to stationarity.

## Assumptions and scope

For \(0<\delta\le 1/6\), let \(f_0,f_1:[0,1]\to[0,1]\) be
\[
f_0(x)=\begin{cases}x/2,&0\le x<1/2+\delta,\\2x-1,&1/2+\delta\le x\le1,\end{cases}\qquad
f_1(x)=\begin{cases}2x,&0\le x<1/2-\delta,\\(x+1)/2,&1/2-\delta\le x\le1.\end{cases}
\]
At each *original* iteration choose either map independently with probability \(1/2\). For \(k\ge2\), let \(c=c_k\), \(\delta=\delta_k\), \(Y=[c/2,1-c/2)\), and
\[
I_1^-=[c/2,c),\quad I_0=[c,1-c),\quad I_1^+=[1-c,1-c/2).
\]
On the core, put \(g_0=f_0|_{[c,1-c/2)}\) and \(g_1=f_1|_{[c/2,1-c)}\), and use the standard accelerated core maps
\[
h_0(x)=\begin{cases}g_1(x),&x\in I_1^-,\\g_0(x),&x\in I_0\cup I_1^+,\end{cases}\quad
h_1(x)=\begin{cases}g_1(x),&x\in I_1^-\cup I_0,\\g_0(x),&x\in I_1^+.\end{cases}
\]
These maps, chosen independently with equal probabilities, form the induced core random dynamics of Nakamura–Nakano–Toyokawa–Yano. We do not identify the accelerated core step with a single physical iteration of \(f_0\) or \(f_1\).

Define the \(2k\) ordered nodes \(z_0,\ldots,z_{2k-1}\) by
\[
z_i=2^{-(k+1-i)}\quad(0\le i\le k),\qquad
z_{k+j}=1-2^{-(j+1)}\quad(1\le j\le k-1).
\]
In particular, \(z_0=c/2\), \(z_k=1/2\), and \(z_{2k-1}=1-c\). All these nodes belong to the half-open core \(Y\).

## Proof

**1. Exact core transition graph.** At the extreme left point \(z_0=c/2\in I_1^-\), both core maps use \(g_1\), so \(h_0(z_0)=h_1(z_0)=2z_0=z_1\). For \(1\le i\le k-1\) the point \(z_i\) lies in \(I_0\) on the left of \(1/2-\delta\); thus \(h_0(z_i)=z_i/2=z_{i-1}\) and \(h_1(z_i)=2z_i=z_{i+1}\). At \(z_k=1/2\), the same index relations hold because \(f_0(1/2)=1/4=z_{k-1}\) and \(f_1(1/2)=3/4=z_{k+1}\). For \(k+1\le i\le2k-2\), one has \(z_i\in I_0\), \(z_i>1/2+\delta\), and consequently \(h_0(z_i)=2z_i-1=z_{i-1}\), \(h_1(z_i)=(z_i+1)/2=z_{i+1}\). Finally, \(z_{2k-1}=1-c\in I_1^+\) uses \(g_0\) for *both* core maps and hence is mapped to \(z_{2k-2}\). All inequalities include their actual half-open boundary conventions. Therefore the finite node set is invariant for every realization, and its transition matrix \(P\) satisfies
\[
P_{0,1}=P_{2k-1,2k-2}=1,\qquad
P_{i,i-1}=P_{i,i+1}=\tfrac12\quad(1\le i\le2k-2),
\]
with all other entries zero. The chain is irreducible because every adjacent step has positive transition probability.

**2. The stationary probability and gate masses.** Set
\[
w_i=\begin{cases}\displaystyle\frac1{2(2k-1)},&i\in\{0,2k-1\},\\[3pt]
\displaystyle\frac1{2k-1},&1\le i\le2k-2.
\end{cases}
\]
The masses sum to one. Detailed balance holds on each edge: \(w_0P_{0,1}=w_1P_{1,0}\), \(w_{2k-2}P_{2k-2,2k-1}=w_{2k-1}P_{2k-1,2k-2}\), and similarly at all interior edges. Hence
\[
\nu_k=\sum_{i=0}^{2k-1}w_i\,\delta_{z_i}
\]
is invariant under the averaged core transfer operator; irreducibility makes it the unique stationary probability **on this finite closed graph**. Moreover only \(z_0\) lies in \(I_1^-\), and only \(z_{2k-1}\) lies in \(I_1^+\). Consequently
\[
\nu_k(I_1^-)=\nu_k(I_1^+)=\frac1{2(2k-1)}>0.
\]
Because the chain is finite and irreducible, any two positive-\(\nu_k\) sets have a strictly positive transition probability between them for some number of steps: this is precisely the annealed metric transitivity required by the core theorem. The chain's period two does not obstruct this property.

**3. A direct physical-iteration walk and pointwise arcsine law.** For any positive generalized Hata–Yano parameter \(0<\delta\le1/6\), define a two-sided dyadic lattice by
\[
q_j=\begin{cases}2^{j-1},&j\le0,\\1-2^{-(j+1)},&j\ge0.\end{cases}
\]
The two expressions agree at \(j=0\), giving \(q_0=1/2\). For every integer \(j\), direct substitution into the *physical* maps gives
\[
f_0(q_j)=q_{j-1},\qquad f_1(q_j)=q_{j+1}.
\]
Indeed, for \(j\le-1\), \(q_j\le1/4<1/2-\delta\), so halving/doubling apply. At \(j=0\), the strict positivity of \(\delta\) gives \(f_0(1/2)=1/4\) and \(f_1(1/2)=3/4\). For \(j\ge1\), \(q_j\ge3/4>1/2+\delta\), so the right branches give \(2q_j-1\) and \((q_j+1)/2\). These identities hold over the **entire positive parameter range** of the family, not only at \(\delta_k\).

Let \(\omega_1,\omega_2,\ldots\) be independent fair bits and \(F_n=f_{\omega_n}\circ\cdots\circ f_{\omega_1}\), with \(F_0\) the identity. Starting at \(q_j\), the index of \(F_n(q_j)\) is exactly the simple symmetric random walk \(J_n=j+\sum_{r=1}^n(2\omega_r-1)\). Since \(q_j\ge1/2\) exactly when \(j\ge0\), the physical occupation fraction is \(N^{-1}\sum_{n=0}^{N-1}\mathbf1_{\{J_n\ge0\}}\). Lévy's classical arcsine theorem yields, for every fixed starting index \(j\in\mathbb Z\),
\[
\frac1N\sum_{n=0}^{N-1}\mathbf1_{\{F_n(q_j)\ge1/2\}}
\ \xrightarrow[N\to\infty]{\mathrm{law}}\ Z,\qquad
\mathbb P(Z\le a)=\frac2\pi\arcsin\sqrt a\quad(0\le a\le1).
\]
To pass from the usual strict-sign arcsine statement to \(J_n\ge0\), or to a fixed shifted starting index, note that the expected number of visits to any fixed finite set of indices through time \(N\) is \(O(\sqrt N)\) by the binomial local bound \(\sup_r\Pr(J_n=r)=O((n+1)^{-1/2})\). Thus these boundary/shift changes alter the occupation fraction by \(o_{\Pr}(1)\). Every \(z_i\) belongs to this two-sided dyadic lattice, so the asserted pointwise law follows for each exhibited finite-core node without importing the source's conditional core limit theorem. The finite-core stationary construction and the direct original-time random walk are two compatible aspects of the same dyadic graph.

**4. Spectrum.** Writing \(L=2k-1\), the vectors \(v^{(j)}_i=\cos(\pi ji/L)\) for \(0\le j,i\le L\) satisfy \(Pv^{(j)}=\cos(\pi j/L)v^{(j)}\): at interior nodes this is the cosine addition identity; at either reflecting endpoint it follows from \(\sin(\pi j)=0\). The \(L+1\) eigenvalues are distinct, so this exhausts the spectrum. Since \(j=L\) gives eigenvalue \(-1\), convergence to the invariant law without parity averaging is not claimed. The first positive eigenvalue below one is \(\cos(\pi/L)\), giving the stated gap and its standard cosine asymptotic.

## Verification

The accompanying standalone Python 3 checker, `check_core.py`, uses exact rational arithmetic with no third-party packages. It constructs the actual piecewise maps, applies the core acceleration with the half-open inequalities, checks all \(2k\) arrows against the path graph, and checks \(wP=w\) and both gate masses for every integer \(2\le k\le150\). It also verifies the physical dyadic left/right translation identity on 705 states across five positive perturbations including both boundary and interior values. These are finite consistency tests (22,648 core nodes plus 705 physical nodes), not infinite proofs. The proof above establishes the graph and stationary formulas for every integer \(k\ge2\).

For the first unaddressed parameter, \(k=2\) and \(\delta=1/16\), the four nodes are \(1/8,1/4,1/2,3/4\) with invariant weights \(1/6,1/3,1/3,1/6\); they are the smallest example beyond the source's deterministic-core parameter range. For \(k=3\), the six nodes are \(1/16,1/8,1/4,1/2,3/4,7/8\), with endpoint weights \(1/10\) and interior weights \(1/5\).

## Relationship to prior work

Nakamura, Nakano, Toyokawa and Yano (arXiv:2206.00226v2, Theorem 1.2 and Remarks 1.3/1.5) established the general core criterion and its resulting arcsine law. Their Section 1.2.2 constructs invariant core measures for \(\delta\ge1/8\) and their Problem 1.8 asks for qualifying measures at all nonzero generalized Hata–Yano parameters. **Neither their criterion nor their already-treated examples alone proves the existence of a qualifying measure for the family \(\delta=2^{-(k+2)}<1/8\).** The present contribution is the explicit irreducible finite core, invariant weights and spectrum on those unresolved parameters, together with a separate direct physical-walk proof of the pointwise dyadic arcsine law throughout the positive parameter range. The general arcsine principle itself is classical and not claimed as novel.

Hata and Yano (arXiv:2108.01332) proved arcsine/Darling–Kac laws for the unperturbed \(\delta=0\) map using a different countable Markov partition. That limiting parameter does not supply the finite reflected cores at \(\delta>0\). Related finite-state cores in other piecewise-linear random families have different map definitions and parameters and do not imply this family by a change of notation.

## Limitations

No closed finite core of the displayed form is established for all \(0<\delta<1/8\), or for parameters outside the specified dyadic sequence; this restriction does not apply to the separate direct dyadic-point arcsine law. The stationary probability is unique *on the exhibited finite closed graph*, not proven unique among all measures on the whole core. The pointwise arcsine assertion holds on the full countable dyadic lattice for every \(0<\delta\le1/6\), not on every Lebesgue-typical initial point or a whole interval. The chain is periodic of period two, which precludes ordinary one-step convergence to stationarity. Broader equivalence or independent priority claims beyond the inspected literature remain possible; there is no independent mathematical audit.

## References

1. F. Nakamura, Y. Nakano, H. Toyokawa, K. Yano, *Arcsine law for random dynamics with a core*, arXiv:2206.00226v2 (first public arXiv release 2022-06-01), Theorem 1.2, Remarks 1.3 and 1.5, Section 1.2.2 and Problem 1.8. https://arxiv.org/abs/2206.00226 ; https://arxiv.org/pdf/2206.00226.
2. G. Hata, K. Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, arXiv:2108.01332v1 (2021-08-03), Theorem 1.1 and Section 1. https://arxiv.org/abs/2108.01332.
