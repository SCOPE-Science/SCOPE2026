# Stable two-patch symmetry breaking increases mean cooperation in a three-player ecological public-goods game

## Finding

For the ecological public-goods metapopulation equations specified below, with exactly two connected patches and group size three, a spatially homogeneous, defector-dominated coexistence state undergoes a **supercritical steady-state pitchfork** at the exact defector-to-cooperator mobility ratio
\[
\kappa_* = \frac{583}{46}.
\]
For all sufficiently small \(\delta=\kappa-\kappa_*>0\), precisely two nonhomogeneous equilibria lie in a neighborhood of that state, they are related by exchanging the patches, and both are locally asymptotically stable in the full four-dimensional system. Their mean cooperator density satisfies the strict, quantitative increase
\[
\frac{u_1+u_2}{2}=\frac1{10}+\frac{464961376}{134363134885}\,\delta+O(\delta^2).
\]
For \(\delta<0\) sufficiently close to zero the homogeneous equilibrium is locally asymptotically stable and no neighboring nonhomogeneous equilibrium exists; for \(\delta>0\), it has exactly one unstable direction. This is an exact local mechanism for increasing total cooperator abundance on a *regular two-vertex network*: degree heterogeneity is unnecessary. No claim is made that either patch becomes cooperator-dominated, or that the resulting branches are globally attracting.

## Assumptions and scope

Consider the deterministic mean-field ecological public-goods model in Roy et al., arXiv:2607.15989v1, with three-person nominal interaction groups (\(N=3\)), multiplication factor \(r=9/4\), baseline reproduction \(b=1/10\), mortality \(d=23/160\), cooperator diffusion \(\varepsilon=1/100\), and positive defector/cooperator diffusion ratio \(\kappa\). The graph consists of two vertices joined by a single undirected edge. At patch \(i\), let \(u_i\) and \(v_i\) be cooperator and defector densities and put \(z_i=1-u_i-v_i\). The local payoff functions, specialized from the source's binomial group-payoff closure, are
\[
 f_D(u,v)=\frac{3u}{4}(2+z),\quad
 F(z)=\frac{(1-z)(1-2z)}4,\quad
 f_C(u,v)=f_D(u,v)-F(z),\quad z=1-u-v.
\]
Writing \(j\) for the other patch, the equations are
\[
 \dot u_i=u_i\{z_i[b+f_C(u_i,v_i)]-d\}+\varepsilon(u_j-u_i),
\]
\[
 \dot v_i=v_i\{z_i[b+f_D(u_i,v_i)]-d\}+\kappa\varepsilon(v_j-v_i).
\]
We analyze only equilibria and trajectories sufficiently near \((u_1,v_1,u_2,v_2)=(1/10,2/5,1/10,2/5)\), where all three densities \(u_i,v_i,z_i\) are strictly positive. These local conclusions do not require global invariance of the patchwise density simplex for arbitrary far-away initial states.

## Proof

**1. Local kinetics and spectral crossing.** Define the polynomial vector field
\[
 \mathcal F(u,v)=
 \begin{pmatrix}
 u\{(1-u-v)[b+f_C(u,v)]-d\}\\
 v\{(1-u-v)[b+f_D(u,v)]-d\}
 \end{pmatrix}.
\]
At \(Q=(1/10,2/5)\), \(z=1/2\), \(F(z)=0\), and \(f_D(Q)=3/16\), giving \((1/2)(1/10+3/16)=23/160=d\). Hence \(\mathcal F(Q)=0\). Direct differentiation gives the exact one-patch Jacobian
\[
 J=D\mathcal F(Q)=\begin{pmatrix}
 39/800&-9/200\\49/200&-13/100
 \end{pmatrix},\quad
 \operatorname{tr}J=-13/160,\quad\det J=3/640.
\]
The homogeneous perturbation block is \(J\), whose eigenvalues are \(-13/320\pm i\sqrt{311}/320\), both with negative real part. The antisymmetric perturbation block is
\[
 A(\kappa)=J-2\varepsilon\operatorname{diag}(1,\kappa),
 \quad \det A(\kappa)=\frac{583-46\kappa}{80000},
 \quad \operatorname{tr}A(\kappa)=-\frac{13}{160}-\frac{1+\kappa}{50}<0.
\]
Thus \(A(\kappa)\) is Hurwitz precisely for \(0<\kappa<583/46\), is a saddle for \(\kappa>583/46\), and has a simple zero eigenvalue at \(\kappa=\kappa_*\). Its other eigenvalue at the threshold is \(-6527/18400\). The right zero eigenvector, normalized by its first component, and left eigenvector normalized to have unit pairing, are
\[
 h=\begin{pmatrix}1\\23/36\end{pmatrix},\qquad
 \ell=\begin{pmatrix}7056/6527\\-828/6527\end{pmatrix},\qquad \ell^{\mathsf T}h=1.
\]
The eigenvalue crossing speed is
\[
 a=\ell^{\mathsf T}\bigl[\partial_\kappa A(\kappa_*)\bigr]h
 =\frac{529}{326350}>0.
\]

**2. Nonlinear branch coefficients.** Put the patchwise mean \(m=(U,V)=((u_1+u_2)/2,(v_1+v_2)/2)\) and half-difference \((p,q)=((u_1-u_2)/2,(v_1-v_2)/2)\). The full equations become
\[
 \dot m=\frac{\mathcal F(m+(p,q))+\mathcal F(m-(p,q))}{2},\qquad
 \begin{pmatrix}\dot p\\\dot q\end{pmatrix}
 =\frac{\mathcal F(m+(p,q))-\mathcal F(m-(p,q))}{2}
 -2\varepsilon\operatorname{diag}(1,\kappa)\begin{pmatrix}p\\q\end{pmatrix}.
\]
For nonzero \(p\) near zero, divide both stationary half-difference equations by \(p\), set \(q=p\eta\), and use the stationary mean equations. At \((p,\eta,m,\kappa)=(0,23/36,Q,\kappa_*)\), these four analytic equations determine \((U,V,\eta,\kappa)\) uniquely as even analytic functions of \(p\): the mean derivative is the nonsingular \(J\), and the remaining two-by-two derivative in \((\eta,\kappa)\) is nonsingular because the critical eigenvalue is simple and \(a\ne0\). Patch-exchange symmetry makes only even powers of \(p\) appear in those variables.

Substitution into the four stationary equations, followed by exact coefficient matching through cubic order, yields
\[
 \begin{aligned}
 U&=\tfrac1{10}+\tfrac{27467}{4050}p^2+O(p^4),\\
 V&=\tfrac25+\tfrac{262103}{64800}p^2+O(p^4),\\
 q&=\tfrac{23}{36}p-\tfrac{456554941}{4199040}p^3+O(p^5),\\
 \kappa&=\tfrac{583}{46}+\tfrac{26872626977}{13711680}p^2+O(p^4).
 \end{aligned}
\]
All four rational coefficients are verified independently by substitution into the polynomial equations in `CHECK.py`. In particular, the coefficient of \(p^2\) in \(\kappa\) is strictly positive, proving existence of exactly two small nonuniform equilibria \(p=\pm\sqrt{\delta/D}+O(\delta^{3/2})\) for each sufficiently small \(\delta>0\), where \(D=26872626977/13711680\), and none nearby when \(\delta<0\). The two equilibria remain biologically interior by continuity from \(Q\).

**3. Stability and increase in cooperator abundance.** In a scalar center-manifold coordinate equal to \(p\) at leading order, the reduced vector field is odd under patch exchange and has the normal form
\[
 \dot p=a\delta p-cp^3+O(\delta^2|p|+|\delta||p|^3+|p|^5),
 \quad a=\frac{529}{326350},\quad c=\frac{26872626977}{8458992000}>0.
\]
The cubic coefficient follows by expanding the mean slaving term \(-J^{-1}D^2\mathcal F(Q)[h,h]/2\) and projecting the cubic half-difference equation against \(\ell\); equivalently the equilibrium coefficient comparison gives \(c=aD\). At each nonzero small branch, the reduced eigenvalue is \(-2a\delta+O(\delta^2)<0\). The three remaining eigenvalues converge to the strictly stable eigenvalues of \(J\) and the noncritical transverse eigenvalue, so both branches are locally asymptotically stable in the full system.

Finally, eliminating \(p^2=\delta/D+O(\delta^2)\) from the mean-cooperator expansion gives
\[
 U=\frac1{10}+\frac{27467/4050}{26872626977/13711680}\delta+O(\delta^2)
 =\frac1{10}+\frac{464961376}{134363134885}\delta+O(\delta^2),
\]
whose linear coefficient is strictly positive. No inference about global attractors or finite-amplitude cooperator dominance is required.

## Verification

Run `python CHECK.py` with Python 3 and SymPy. The checker reconstructs the original polynomial kinetics, homogeneous and antisymmetric Jacobians, zero-mode vectors, mean and difference series coefficients, the critical crossing speed and the cubic sign using exact rational arithmetic. The finite numerical evaluations included in the checker illustrate consistency only; they are not used as proofs of local bifurcation or stability. All exact identities needed above are stated in this file and can be verified by hand from the displayed polynomials.

## Relationship to prior work

Roy, Anwar, Carletti, Perc and Ghosh (2026) introduce the underlying network eco-evolutionary equations, establish a general linear Turing-instability criterion and numerically study heterogeneity, mostly on large networks and larger interaction groups. Their full text and supplement include the discrete-Laplacian dispersion relation and simulations of increased global cooperation, but explicitly leave an analytical derivation of the global-average increase to further work. Their results **do cover** the linear-stability methodology; no new general Turing criterion is claimed here. The new statement is the exact nonlinear, locally stable two-site branch at the smallest nontrivial group size, together with its strictly positive, rational mean-cooperation response coefficient. Standard exchange-symmetric pitchfork theory supplies the local mechanism, not these model-specific coefficients or signs. Hauert, Holmes and Doebeli (2006) establish ecological public-goods coexistence without the present two-patch nonlinear spatial calculation.

## Limitations

The assertion is local in state and in \(\kappa\) around \(583/46\); far-from-equilibrium dynamics, basin sizes, stochastic finite populations, heterogeneous networks and global physical invariance are not covered. The new equilibria need not satisfy \(u_i>v_i\) on either patch. This is a single precisely motivated parameter set, not an all-parameter criticality classification. Exact symmetry-breaking bifurcation techniques are established mathematics. The source's linear criterion and numerical cooperation enhancement are prior results, and unindexed equivalent nonlinear calculations remain an originality risk. Independent scientific validation has not been performed.

## References

1. S. Roy, M. S. Anwar, T. Carletti, M. Perc, D. Ghosh, *Diffusion-induced instabilities promote cooperation in eco-evolutionary networks*, arXiv:2607.15989v1 (preprint posted 17 July 2026; publisher online release verified 8 July 2026), https://arxiv.org/abs/2607.15989 ; publisher article https://doi.org/10.1073/pnas.2530131123 ; full text and supplementary calculations available at https://www.researchgate.net/publication/410594221_Diffusion-induced_instabilities_promote_cooperation_in_eco-evolutionary_networks .
2. C. Hauert, M. Holmes, M. Doebeli, *Evolutionary games and population dynamics: maintenance of cooperation in public goods games*, Proc. R. Soc. B 273 (2006), 2565–2570, https://doi.org/10.1098/rspb.2006.3600 ; open full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC1634915/ .
