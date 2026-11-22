# Exact bath-domain fragmentation law for steady heat transport in Glauber rings

## Finding
For every integer \(N\ge4\), choose \(h\ge2\) infinitely hot sites and \(c=N-h\ge1\) finitely cold sites in any order around a periodic ferromagnetic Ising chain. At each site use the continuous-time single-spin Glauber rate specified below. Write \(\ell_1,\ldots,\ell_r\) for the lengths of its maximal consecutive cold runs, so \(\sum_{j=1}^r\ell_j=c\). Put
\[
\gamma=\tanh(2J/T_c),\quad \alpha=\gamma/4,\quad a_0=0,\quad a_{\ell}=\frac{\alpha}{1-\alpha a_{\ell-1}}\quad(\ell\ge1).
\]
Then the unique stationary total mean energy influx from the infinitely hot reservoir into the chain is **exactly**
\[
\boxed{Q_{\mathrm h}=2J\sum_{j=1}^{r}a_{\ell_j}.}
\]
With the fixed numbers \(h,c\), define \(r_*=\min(h,c)\), \(q=\lfloor c/r_*\rfloor\), and \(s=c-qr_*\). The sharp bounds are
\[
\boxed{2J a_c\le Q_{\mathrm h}\le 2J\bigl[(r_*-s)a_q+s a_{q+1}\bigr].}
\]
The lower equality holds exactly when the cold sites are one contiguous block. The upper equality holds exactly when there are \(r_*\) cold runs, with every run of length \(q\) or \(q+1\) (exactly \(s\) having length \(q+1\)); if \(h>c\), the additional hot sites may occupy arbitrary hot gaps. For \(c=1\), the two extrema coincide. For \(c\ge2\), any genuine split of a cold block enabled by repositioning one hot site strictly raises \(Q_{\mathrm h}\). In particular, when \(h=c\), the unique maximum up to rotation is the alternating assignment. The stationary total heat outflux to the cold bath equals \(Q_{\mathrm h}\), and the reservoir entropy production rate (with \(k_B=1\)) equals \(Q_{\mathrm h}/T_c\).

## Assumptions and scope
Let sites be labeled modulo \(N\), spins \(\sigma_i\in\{-1,+1\}\), and \(J>0\). The Hamiltonian and flip rate at site \(i\) are
\[
\mathcal H(\sigma)=-J\sum_{i=0}^{N-1}\sigma_i\sigma_{i+1},\qquad
w_i(\sigma)=\frac12\left[1-\frac{\gamma_i}{2}\sigma_i(\sigma_{i-1}+\sigma_{i+1})\right],
\]
where \(\gamma_i=0\) at an infinitely hot site and \(\gamma_i=\gamma=\tanh(2J/T_c)\in(0,1)\) at a cold site. There are at least two *distinct* hot sites; this is essential because the two boundaries of any cold run must be different hot spins. The arbitrary overall spin-flip clock is normalized by the displayed factor \(1/2\). We use natural time and energy units and \(k_B=1\). No zero-temperature limit is included.

## Proof
**Stationarity and the two-point equation.** Every flip rate is at least \((1-\gamma)/2>0\), so the finite spin-flip chain is irreducible and has a unique stationary law. Write \(C_{ij}=\langle\sigma_i\sigma_j\rangle_{\mathrm{st}}\), with \(C_{ii}=1\). Applying the generator to \(\sigma_i\sigma_j\) for distinct sites gives
\[
2C_{ij}=\frac{\gamma_i}{2}(C_{i-1,j}+C_{i+1,j})+
\frac{\gamma_j}{2}(C_{i,j-1}+C_{i,j+1}).\tag{1}
\]
In particular, if \(i\ne j\) are both hot, then \(C_{ij}=0\). If \(i\) is hot and \(j\) is cold, equation (1) becomes
\[
C_{ij}=\alpha(C_{i,j-1}+C_{i,j+1}).\tag{2}
\]

**Decoupling of cold runs.** Fix a hot spin \(i\). On any cold run of length \(\ell\), equation (2) is a strictly diagonally dominant tridiagonal boundary-value problem. Its two endpoint correlations with the adjoining hot spins are zero except that the boundary corresponding to \(i\) is one (\(C_{ii}=1\)). The two hot endpoints of the run are distinct by assumption. Consequently a run not incident to \(i\) has the zero solution; a run incident to \(i\) has boundary values \((1,0)\) or \((0,1)\). Its nearest-neighbor endpoint correlation equals \(a_\ell\), as obtained by eliminating the last cold unknown recursively: \(a_0=0\) and \(a_\ell=\alpha/(1-\alpha a_{\ell-1})\). The recursion is exact and requires no infinite-volume approximation.

**Energy transport.** Flipping spin \(i\) changes \(\mathcal H\) by \(2J\sigma_i(\sigma_{i-1}+\sigma_{i+1})\). At a hot site its flip rate is \(1/2\), hence its mean heat injection is \(J(C_{i,i-1}+C_{i,i+1})\). Every hot-hot edge contributes zero, and each cold run has exactly two hot-cold boundary edges, each contributing \(J a_{\ell}\). Summing yields \(Q_{\mathrm h}=2J\sum a_{\ell}\). Stationarity of mean energy forces the cold bath to remove the same total heat. Since the hot inverse temperature is zero, the reservoir entropy production is \(Q_{\mathrm h}/T_c\).

**Strict concavity and extremizers.** Write \(f(x)=\alpha/(1-\alpha x)\), so \(a_{\ell+1}=f(a_\ell)\). Since \(0<\alpha<1/4\), its smaller nonnegative fixed point
\[
a_*=\frac{1-\sqrt{1-4\alpha^2}}{2\alpha}
\]
satisfies \(\alpha a_*<1/2\). Starting at zero, the iteration grows strictly toward \(a_*\). On \([0,a_*]\),
\[
0<f'(x)=\frac{\alpha^2}{(1-\alpha x)^2}<4\alpha^2<1.
\]
Thus the increments \(a_{\ell+1}-a_\ell\) are positive and strictly decreasing, even from \(\ell=0\): the sequence with \(a_0=0\) is strictly discretely concave. In particular \(a_{p+q}<a_p+a_q\) for all positive integers \(p,q\), by comparing successive increments. Merging two cold runs strictly lowers total flux; splitting a cold run strictly raises it. Hence the unique minimum run count \(r=1\) yields \(2Ja_c\). The greatest available run count is \(r_*=\min(c,h)\), attainable by separating cold blocks with hot sites. At fixed \(r_*\), moving a site from a run of length at least two more than another run strictly increases the sum, by decreasing increments. Repeating yields precisely the balanced lengths \(q\) and \(q+1\) and the stated maximum. All strict-equality assertions follow from these two strict inequalities. \(\square\)

## Verification
The attached `verify_hot_domains.py` is a standalone Python 3 exact-rational verification program. It constructs and solves the full spin-state Markov balance equations for selected rings, separately constructs the closed stationary two-point balance equations, and checks the run-length prediction. It further checks all \(456\) hot/cold allocations with \(4\le N\le8\) and at least two hot spins, including both extremal values, at \(\gamma=3/5\). A separate rational check confirms strict concavity/subadditivity for initial lengths at \(\gamma=7/9\). These finite checks support but do not replace the all-size proof above.

## Relationship to prior work
The foundational staggered two-temperature Glauber chain, its stationary two-point hierarchy, and its heat-current definition are established in Schmüser–Schmittmann (2002) and Schmittmann–Schmüser (2002), preceded by Rácz–Zia (1994). In particular, the strictly alternating two-bath current is known and is **not claimed as new**. Lavrentovich (2012) studies a different, infinite two-domain junction with a spatial heat profile. Bauer–Cornu (2017) analyze alternating baths with unequal kinetic rates. The result here is a finite periodic ring with an *arbitrary* placement of finitely many infinitely hot sites: its exact cold-run decomposition, strict fragmentation ordering, and the complete sharp fixed-count extremizers. The general two-point equation is prior mathematical machinery; the arrangement theorem and its equality cases require the explicit run Dirichlet reduction and concavity argument.

## Limitations
The result requires \(N\ge4\), at least two hot sites, strictly finite positive cold temperature, nearest-neighbor ferromagnetic coupling, uniform spin-flip clock normalization, and a strictly infinite-temperature hot reservoir. It does not establish arbitrary finite hot temperatures, quenched bond disorder, current fluctuations, nonstationary transport or nonequilibrium finite-size scaling. The novelty comparison cannot rule out every unpublished or unindexed treatment of patterned reservoirs; independent scientific audit is not yet performed.

## References
1. F. Schmüser and B. Schmittmann, *Non-equilibrium stationary state of a two-temperature spin chain* (first public preprint 2002-06-18), https://arxiv.org/abs/cond-mat/0206345 .
2. B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain* (first public preprint 2002-12-27), https://arxiv.org/abs/cond-mat/0212616 .
3. Z. Rácz and R. K. P. Zia, *Two-temperature kinetic Ising model in one dimension: Steady-state correlations in terms of energy and energy flux*, Phys. Rev. E 49, 139 (1994), https://doi.org/10.1103/PhysRevE.49.139 .
4. M. O. Lavrentovich, *Steady-state properties of coupled hot and cold Ising chains* (2012-01-18 preprint), https://arxiv.org/abs/1201.3906 .
5. M. Bauer and F. Cornu, *Thermal contact through a two-temperature kinetic Ising chain* (2017-12-06 preprint), https://arxiv.org/abs/1712.02273 .
