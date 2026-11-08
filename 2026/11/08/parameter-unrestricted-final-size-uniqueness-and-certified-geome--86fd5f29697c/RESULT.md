# Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks

## Finding

For a finite, fully interacting deterministic SIRD system with any number \(m\ge2\) of demographic groups, strictly positive transmission, recovery and disease-mortality rates, positive initial susceptibles, and at least one initially infectious individual, the biologically admissible final susceptible vector is the **unique** fixed point of its active-population final-size equations. No relative-transmission, diagonal-dominance or contraction restriction is needed. In addition, explicit parameters derived solely from the initial data and model rates produce two-sided final-size bounds with an a priori geometric error certificate, even when all four sufficient uniqueness conditions of the two-group source fail.

Specifically, define
\[
 N_j=S_{j0}+I_{j0}+R_{j0},\qquad
 \varepsilon_j=\frac{\mu_j}{\gamma_j+\mu_j},\qquad
 Z_j=(1-\varepsilon_j)N_j+\varepsilon_jR_{j0},\qquad a_{ij}=\frac{\beta_{ij}}{\mu_j}.
\]
Set
\[
 F_i(y)=\sum_{j=1}^m a_{ij}\log\frac{N_j}{Z_j+\varepsilon_jS_{j0}e^{-y_j}},\qquad
 c_i=F_i(0),\qquad M_i=\sum_{j=1}^m a_{ij}\log\frac{N_j}{Z_j}.
\]
Then \(0<c_i<M_i\), and the explicit dimensionless constants
\[
 \eta=\min_i\frac{c_i}{M_i},\qquad q=1-\eta\in(0,1),\qquad K=\eta^{-1}
\]
give, for the iterates \(l^{(0)}=0\), \(u^{(0)}=M\), \(l^{(n+1)}=F(l^{(n)})\), \(u^{(n+1)}=F(u^{(n)})\), the **coordinatewise certified enclosure**
\[
 l^{(n)}\le y^*\le u^{(n)},\qquad
 0\le u_i^{(n)}-l_i^{(n)}\le K q^n M_i\quad(n\ge0),
\]
where \(y^*\) is the unique fixed point of \(F\). The epidemic's final susceptibles obey
\[
 S_{i0}e^{-u_i^{(n)}}\le S_{i\infty}=S_{i0}e^{-y_i^*}\le S_{i0}e^{-l_i^{(n)}}.
\]
The same fixed point is reached by iterating \(F\) from any nonnegative vector. This claim concerns the exact deterministic ODE and its final-size map, not a stochastic finite-population epidemic.

## Assumptions and scope

Let \(m\ge2\) be a finite integer and \(i,j\in\{1,\ldots,m\}\). The state is \((S_i,I_i,R_i,D_i)\) with active population \(N_i(t)=S_i(t)+I_i(t)+R_i(t)\), governed by
\[
 \dot S_i=-S_i\sum_{j=1}^m\beta_{ij}\frac{I_j}{N_j(t)},\quad
 \dot I_i=S_i\sum_{j=1}^m\beta_{ij}\frac{I_j}{N_j(t)}-(\gamma_i+\mu_i)I_i,\quad
 \dot R_i=\gamma_i I_i,\quad \dot D_i=\mu_i I_i.
\]
Assume \(\beta_{ij}>0\), \(\gamma_i>0\), \(\mu_i>0\), \(S_{i0}>0\), \(R_{i0},D_{i0},I_{i0}\ge0\), and \(\sum_iI_{i0}>0\). No population movement, births, waning immunity, external importation or time-dependent coefficients are included. The initial deceased count does not enter \(N_i\).

An initially infectious individual is essential to the strict lower bound \(c\gg0\). At \(I_{i0}=0\) for every group, the final state is trivially the initial susceptible state, but the algebraic map may also have additional fixed points; the uniqueness assertion is intentionally not made in that case.

## Proof

**1. Well-defined limits and the final-size equation.** Nonnegative compartment states remain nonnegative and bounded by each group's conserved total \(S_i+I_i+R_i+D_i\). Moreover, \(S_i\) is decreasing, \(R_i,D_i\) increasing, and \(N_i(t)\) decreasing. Since \(\dot N_j=-\mu_jI_j\) and \(\dot S_i/S_i=-\sum_j\beta_{ij}I_j/N_j\), direct integration gives
\[
 \log\frac{S_i(t)}{S_{i0}}=\sum_j a_{ij}\log\frac{N_j(t)}{N_j}.
\]
Both sides are defined because \(S_i(t)>0\) and \(N_i(t)\ge S_i(t)>0\). The identity implies a strictly positive lower bound for each \(S_i(t)\). Indeed, write \(J_j(t)=\int_0^tI_j(s)\,ds\). Since \(N_j(t)=N_j-\mu_jJ_j(t)\), \(R_j(t)=R_{j0}+\gamma_jJ_j(t)\) and \(N_j(t)\ge R_j(t)\), one has \(J_j(t)\le(N_j-R_{j0})/(\gamma_j+\mu_j)\), hence \(N_j(t)\ge Z_j>0\). Thus \(S_{i\infty}>0\). Convergence of the monotone compartments shows \(I_i(t)\) has a limit. Since \(\int_0^\infty I_i(t)\,dt\le N_i/\mu_i<\infty\), that limit is zero.

Let \(x_j=S_{j\infty}\). The equality \(R_{j\infty}=R_{j0}+(\gamma_j/\mu_j)(N_j-N_{j\infty})\), together with \(N_{j\infty}=x_j+R_{j\infty}\), gives \(N_{j\infty}=Z_j+\varepsilon_jx_j\). Consequently,
\[
 x_i=S_{i0}\prod_{j=1}^m\left(\frac{Z_j+\varepsilon_jx_j}{N_j}\right)^{a_{ij}}.
\]
For \(0<x_i\le S_{i0}\), substitute \(y_i=\log(S_{i0}/x_i)\), giving precisely \(y=F(y)\) on \([0,\infty)^m\).

**2. Positive, bounded, increasing, concave map.** Because \(Z_j+\varepsilon_jS_{j0}=N_j-\varepsilon_jI_{j0}\), the assumption of a positive infectious seed and \(a_{ij}>0\) implies \(c_i>0\). Since \(Z_j>0\) and \(S_{j0}>0\), \(M_i>c_i\). For every \(y\ge0\), \(c\le F(y)\le M\) coordinatewise. Direct differentiation gives
\[
 \frac{\partial F_i}{\partial y_j}
 =a_{ij}\frac{\varepsilon_jS_{j0}e^{-y_j}}{Z_j+\varepsilon_jS_{j0}e^{-y_j}}>0,
\quad
 \frac{\partial^2F_i}{\partial y_j^2}
 =-a_{ij}\frac{Z_j\varepsilon_jS_{j0}e^{-y_j}}{(Z_j+\varepsilon_jS_{j0}e^{-y_j})^2}<0,
\]
and mixed second derivatives vanish. Hence each component is continuous, monotone increasing and concave. The compact box \([c,M]\) is mapped into itself, so Brouwer's theorem gives a fixed point \(y^*\in[c,M]\).

**3. Uniqueness without a parameter restriction.** Suppose two fixed points \(y,z\gg0\) differ. Exchanging their roles if necessary, take \(\rho=\max_i y_i/z_i>1\). Then \(y\le\rho z\) with equality in some coordinate \(k\). Concavity applied to \(z=\rho^{-1}(\rho z)+(1-\rho^{-1})0\) gives
\[
 F(\rho z)\le\rho F(z)-(\rho-1)F(0)
 =\rho z-(\rho-1)c\ll\rho z.
\]
But monotonicity yields \(y=F(y)\le F(\rho z)\); coordinate \(k\) would satisfy \(y_k<\rho z_k=y_k\), a contradiction. Therefore the fixed point is unique. In particular the ODE's physical final size is that fixed point.

**4. Certified two-sided geometric rate.** Start \(l^{(0)}=0\), \(u^{(0)}=M\). Monotonicity and the fixed-point identity give \(l^{(n)}\nearrow y^*\), \(u^{(n)}\searrow y^*\) once uniqueness is known. By \(y_i^*\le M_i\) and \(c_i\ge\eta M_i\), one has \(c\ge\eta y^*\). Concavity then implies, for \(0\le t\le1\),
\[
 F(ty^*)\ge tF(y^*)+(1-t)F(0)\ge[\eta+(1-\eta)t]y^*.
\]
Induction with \(t=1-q^n\) proves \(l^{(n)}\ge(1-q^n)y^*\).

Differentiating the concavity inequality at \(y^*\) along the segment toward zero gives \(DF(y^*)y^*\le y^*-c\le qy^*\). Also \(M_i\le Kc_i\le Ky_i^*\), so \(0\le M-y^*\le(K-1)y^*\). At any \(v\ge y^*\), the concavity tangent inequality gives \(F(v)-y^*\le DF(y^*)(v-y^*)\). Therefore induction yields \(0\le u^{(n)}-y^*\le(K-1)q^ny^*\). Combining both estimates gives
\[
 0\le u^{(n)}-l^{(n)}\le Kq^ny^*\le Kq^nM.
\]
Since every nonnegative initial vector enters \([c,M]\) after one application of \(F\), order squeezing by the two extremal sequences proves geometric convergence from any nonnegative starting point. Reversing \(y_i=\log(S_{i0}/x_i)\) yields the claimed susceptible enclosure.

## Verification

A standalone Python checker verifies the logarithmic second-derivative identities exactly with SymPy, reproduces a rational-parameter example outside every source condition, checks the explicit enclosure across forty iterations with \(60\)-digit arithmetic, tests \(500\) randomly sampled positive systems of two through five groups, and validates a seed-free boundary example. The random tests are falsification probes, not substitutes for the preceding general proof.

For two groups, let \(S_0=(1,1)\), \(I_0=(1/5,1/5)\), \(R_0=(0,0)\), \(\gamma_i=\mu_i=1\), and
\[
 (\beta_{ij})=\begin{pmatrix}2&1/4\\3/5&9/5\end{pmatrix}.
\]
The two row sums are \(9/4\) and \(12/5\), while \(N_i=6/5\), \(Z_i=3/5\), \(\varepsilon_i=1/2\). This violates the source's conditions H2a (because several ratios \(\beta_{ij}/\mu_j\) are below one), H2b (both row sums exceed one), H2c and H2d (both corresponding row sums divided by \(6/5\) exceed one). Nevertheless, the theorem applies with
\[
 \eta=\frac{\log(12/11)}{\log2},\qquad
 q=1-\frac{\log(12/11)}{\log2}\approx0.874469117916141.
\]
Numerical evaluation, not an exact closed form, gives \(S_{1\infty}\approx0.3983227211518863\) and \(S_{2\infty}\approx0.3614414715826819\), with rigorous symbolic parameter-bound validity established above.

## Relationship to prior work

Melo and Santos derive the two-group SIRD final-size map and prove uniqueness under H2a–H2d; their Remark 3.3 explicitly leaves uniqueness outside those regimes unresolved, while their Proposition 3.2 obtains an explicit linear rate only under H2d. The present result uses a different *negative logarithmic susceptible* variable, verifies strictly positive concavity, resolves that particular unrestricted uniqueness question, extends it to any finite number of groups, and supplies explicit two-sided rates calculated from model parameters.

The general order-preserving concave fixed-point uniqueness principle is **not new**: Kennan (2001), and earlier positive-operator literature, already imply abstract uniqueness once the transformation and strict positivity are established. Likewise, Piotrowski and Cavalcante (2022) prove abstract geometric convergence of positive concave iterations. The claim of mathematical contribution is limited to recognizing this structure for the actively normalized SIRD final-size equations and obtaining the specific formula \(Kq^nM_i\), which directly certifies susceptible bounds without a spectral calculation or prior knowledge of the fixed point. The source's existing final-size identity, monotone iteration and general fixed-point principles are credited rather than claimed independently.

Other multigroup SIR/SEIR final-size studies involve standard constant-population incidence and do not, on the inspected material, establish this parameter-unrestricted active-population certificate. Relevant inaccessible work is noted under limitations.

## Limitations

The explicit rate can be conservative, particularly for very small initial infectious seeds, where \(q\) approaches one. This is an error guarantee, not an exact asymptotic convergence factor. Strictly positive cross-group transmission is used to propagate a seed to all logarithmic coordinates; zero links and disconnected group blocks require a separate analysis. The theorem does not cover stochastic epidemic final sizes, temporary interventions, vaccination, demographic turnover or migrating populations.

The uniqueness step is a model-specific application of existing general concave-map theory; neither the generic fixed-point theorem nor generic geometric convergence is presented as novel. A relevant older article on implicit epidemic final-size equations was located only by abstract, so an uninspected equivalent transformation or explicit certificate remains a residual originality risk. No independent external scientific validation was performed.

## References

1. A. M. V. D. L. Melo and M. C. Santos, *Final size of a structured SIRD Model with active-population force of infection*, arXiv:2601.15388, first version January 21, 2026, especially equations (6)–(9), Theorems 3.3–3.5, Remarks 3.3–3.4 and Proposition 3.2. https://arxiv.org/abs/2601.15388
2. J. Kennan, *Uniqueness of Positive Fixed Points for Increasing Concave Functions on \(\mathbb R^n\): An Elementary Result*, 2001. https://www.ssc.wisc.edu/~jkennan/research/FixedPoint21.pdf
3. T. Piotrowski and R. L. G. Cavalcante, *The Fixed Point Iteration of Positive Concave Mappings Converges Geometrically if a Fixed Point Exists*, arXiv:2110.11055 (2022). https://arxiv.org/abs/2110.11055
4. E. Almeida et al., *Final size and convergence rate for an epidemic in heterogeneous population*, arXiv:2010.15410. https://arxiv.org/abs/2010.15410
5. A. Bidari et al., *Solvability of implicit final size equations for SIR epidemic models*, Mathematical Biosciences (2016), doi:10.1016/j.mbs.2016.10.012 (abstract examined; full text not accessible during this review). https://doi.org/10.1016/j.mbs.2016.10.012
