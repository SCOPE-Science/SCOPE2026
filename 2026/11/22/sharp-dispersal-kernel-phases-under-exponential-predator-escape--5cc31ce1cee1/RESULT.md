# Sharp dispersal-kernel phases under exponential predator escape and a prescribed mean distance

## Finding

For parameters \(c>0\), \(\beta>0\), and prescribed mean dispersal distance \(m\geq0\), let
\[
f(r)=\exp(-cr-\beta e^{-r}),\qquad r\geq0,
\]
and maximize \(\mathbb E[f(R)]\) over **all** probability distributions of \(R\geq0\) with \(\mathbb E[R]=m\). Put
\[
B(c)=c+\frac12+\sqrt{c+\frac14}.
\]
The following classification is global, sharp, and includes attainment and uniqueness.

**Case I: \(\beta\leq c\).** At \(m=0\), only \(R=0\) is feasible. For every \(m>0\), the supremum is \(e^{-\beta}\) and is **not attained**.

**Case II: \(c<\beta\leq B(c)\).** Define \(r_*=\log(\beta/c)\). For \(0\leq m\leq r_*\), the **unique** maximizer is the deterministic law \(R=m\) and the maximum equals \(f(m)\). For \(m>r_*\), the supremum is \(f(r_*)\) and is **not attained**.

**Case III: \(\beta>B(c)\).** The same \(r_*\) is the pointwise optimal distance. There is a **unique** \(t\in(0,r_*)\) satisfying
\[
t(\beta e^{-t}-c)f(t)=f(t)-f(0).
\]
For \(0<m<t\), the unique maximizer is
\[
\Pr(R=0)=1-\frac mt,\qquad \Pr(R=t)=\frac mt,
\]
with maximum \(f(0)+(m/t)[f(t)-f(0)]\). For \(t\leq m\leq r_*\), the unique maximizer is \(R=m\) with maximum \(f(m)\). At \(m=0\), the only feasible law is \(R=0\). For \(m>r_*\), the supremum is \(f(r_*)\) and is **not attained**.

Thus the predator-exposure threshold \(\beta=B(c)\) is precisely where an optimal mixture of seeds staying at the parent and seeds traveling a fixed positive distance first becomes possible. The mean-only constraint also creates a nonattainment phase beyond the pointwise best travel distance.

## Assumptions and scope

Distances are dimensionless and nonnegative. The factor \(e^{-cr}\) models direct distance-dependent transport mortality; \(e^{-\beta e^{-r}}\) models survival against exponentially declining exposure to natural enemies concentrated near the parent. These are **exogenous, multiplicative** survival factors. There are no seed interactions, habitat boundaries, feedback on the predator population, spatial variation in habitat quality, or density-dependent competition. All Borel probability measures on \([0,\infty)\) with a **finite, exactly prescribed first moment** are admissible, including atomic measures and laws with unbounded support. The objective is expected individual establishment, **not** long-term evolutionary fitness, population expansion, or an evolutionarily stable strategy.

The exact-mean constraint is a mathematical transport-budget benchmark; replacing it by an upper bound, imposing a maximal travel distance, or limiting the kernel to a parametric family changes the answer.

## Proof

**1. Shape of the individual establishment curve.** Write \(z=\beta e^{-r}\). Direct differentiation gives
\[
f'(r)=(z-c)f(r),\qquad
f''(r)=\bigl[(z-c)^2-z\bigr]f(r).
\]
The roots of the bracketed quadratic in \(z\) are
\[
z_\pm=c+\frac12\pm\sqrt{c+\frac14}.
\]
Since \(z_-<c<z_+=B(c)\), for \(\beta>c\) the function increases strictly to its unique pointwise maximum at \(r_*=\log(\beta/c)\), then decreases strictly. If \(c<\beta\leq B(c)\), its second derivative is strictly negative in \((0,r_*)\). If \(\beta>B(c)\), it is strictly convex on \((0,r_i)\) and strictly concave on \((r_i,r_*)\), where \(r_i=\log(\beta/B(c))\). When \(\beta\leq c\), \(f\) is strictly decreasing for \(r>0\).

**2. Unique tangent in the convex-then-concave case.** For \(\beta>B(c)\), define
\[
N(r)=rf'(r)-f(r)+f(0).
\]
Then \(N(0)=0\) and \(N'(r)=rf''(r)\). Hence \(N\) increases strictly to a positive value at \(r_i\), then decreases strictly through \(N(r_*)=f(0)-f(r_*)<0\). Consequently \(N\) has exactly one zero \(t\in(r_i,r_*)\). Furthermore
\[
\frac{d}{dr}\frac{f(r)-f(0)}r=\frac{N(r)}{r^2}.
\]
The secant slope from the origin is uniquely maximized at \(t\). Therefore the chord from \((0,f(0))\) to \((t,f(t))\) lies strictly above \(f(r)\) for \(0<r<t\); its slope equals \(f'(t)\).

**3. Exact upper concave envelope.** If \(\beta\leq c\), the constant function \(G(r)=f(0)\) majorizes \(f\). If \(c<\beta\leq B(c)\), let \(G=f\) on \([0,r_*]\) and \(G=f(r_*)\) for \(r>r_*\). By Step 1 this is a concave majorant with a horizontal join at \(r_*\). If \(\beta>B(c)\), let
\[
G(r)=
\begin{cases}
f(0)+\dfrac r t[f(t)-f(0)],&0\leq r<t,\\
f(r),&t\leq r\leq r_*,\\
f(r_*),&r>r_*.
\end{cases}
\]
Step 2 shows the chord majorizes \(f\), while the derivative matches at \(t\); Step 1 shows strict concavity from \(t\) to \(r_*\), and the derivative vanishes at \(r_*\). Thus \(G\) is continuous and concave on \([0,\infty)\), and \(G\geq f\).

**4. Upper bound, attainment and equality.** For every admissible \(R\), Jensen's inequality for concave \(G\) yields
\[
\mathbb E[f(R)]\leq\mathbb E[G(R)]\leq G(\mathbb E R)=G(m).
\]
For \(0<m<t\) in Case III, the stated two-atom distribution has the prescribed mean and expectation exactly \(G(m)\); uniqueness follows because \(G>f\) strictly on \((0,t)\) and the linear upper-envelope face has contact with \(f\) only at \(0\) and \(t\). On any strict concavity interval where \(G=f\), equality in Jensen forces a point mass at \(m\); the adjoining chord or plateau does not introduce other equality cases. At \(m=t\), \(m=r_*\), and \(m=0\), the same contact/equality reasoning gives the asserted unique point masses.

When \(\beta\leq c\) and \(m>0\), any feasible law differs from the only pointwise maximizer \(0\), so \(\mathbb E[f(R)]<f(0)\). Yet the law putting mass \(1-m/M\) at \(0\) and \(m/M\) at \(M\) has mean \(m\) and approaches \(f(0)\) as \(M\to\infty\). When \(\beta>c\) and \(m>r_*\), choose mass \(1-(m-r_*)/(M-r_*)\) at \(r_*\) and the remainder at \(M>m\). The mean equals \(m\), and expected establishment approaches \(f(r_*)\). No law with \(m>r_*\) can be concentrated at the unique pointwise maximizer \(r_*\), so the supremum is not attained. This completes every case.

## Verification

The standalone Python program `verify.py` uses only standard-library arithmetic. It checks the curvature sign and the tangent's defining equation across several positive parameter regimes, checks the upper envelope pointwise on finite grids, tests feasible two-point distributions against the claimed optimal value, verifies the explicit equality constructions, and checks illustrative nonattainment sequences. Its finite tests are **not** the proof of the universal optimization statement; Steps 1–4 provide that proof.

For the reproducible example \(c=1\), \(\beta=4\), one has \(B(1)=(3+\sqrt5)/2\), \(r_*=\log 4\), and \(t\approx0.632992968921\). At prescribed mean \(m=1/4\), about \(39.4949\%\) of seeds optimally travel distance \(t\), and the remainder stay at the parent. Expected establishment is approximately \(0.03615418509\), versus \(0.03455499617\) for deterministic travel distance \(1/4\): a gain of about \(4.628\%\) within the stated model.

## Relationship to prior work

Rousset and Gandon (2002) analyze freely varying distributions of dispersal distances and distance-dependent survival costs, but identify evolutionarily stable distributions through kin competition and genetic relatedness on a finite spatial lattice, **without** the prescribed mean-distance optimization and the exogenous survival function above. Ezoe (1998) varies seed size and a fixed Gaussian family of dispersal distances; Harada (1999) studies a two-type allocation in a lattice model using invasion and pair approximation. Their evolutionary and resource-allocation conditions do not imply the displayed all-law concave envelope or exact threshold.

Muller-Landau, Levin and Keymer (2003) study the evolutionary value of escaping specialized pests through long-distance dispersal. Nathan and Casagrandi (2004) give a mechanistic seed-predation/recruitment model and **already explicitly suggest dispersal dimorphism**. Fronhofer, Poethke and Dieckmann (2015) derive bimodal dispersal kernels through maternal investment in an individual-based evolutionary model. Neither dimorphism as a general biological concept nor the generic mathematical principle of taking a concave envelope is claimed here as new. The distinct mathematical content is the exact \(B(c)\) threshold, unique tangent and support classification for the specified survival law, together with the sharp nonattainment region under a fixed first moment. Priority against all classical resource-allocation or seed-dispersal theory is not independently established.

## Limitations

The result proves an ideal mathematical optimization for prescribed survival factors, not empirical seed transport or predator behavior. No prediction of an actual plant population, seed-dimorphic phenotype, or evolutionary stable strategy follows without additional modeling and data. Rare arbitrarily distant seeds create the nonattainment regime; bounded environments or tight-tail constraints remove that construction. The theorem does not quantify variance, propagation fronts, ecological feedback, or optimal kernels under different functionals. The closest published full texts were examined, but a relevant 1999 lattice-allocation paper was only available at abstract level; this is a residual historical-priority risk. No independent mathematical audit has been performed.

## References

- H. Ezoe (1998), “Optimal dispersal range and seed size in a stable environment,” *Journal of Theoretical Biology* 190, 287–293. DOI: 10.1006/jtbi.1997.0553.
- Y. Harada (1999), “Short- vs. long-range disperser: the evolutionarily stable allocation in a lattice-structured habitat,” *Journal of Theoretical Biology* 201, 171–187. DOI: 10.1006/jtbi.1999.1022.
- F. Rousset and S. Gandon (2002), “Evolution of the distribution of dispersal distance under distance-dependent cost of dispersal,” *Journal of Evolutionary Biology* 15, 515–523. DOI: 10.1046/j.1420-9101.2002.00430.x.
- H. C. Muller-Landau, S. A. Levin and J. E. Keymer (2003), “Theoretical perspectives on evolution of long-distance dispersal and the example of specialized pests,” *Ecology* 84, 1957–1967. DOI: 10.1890/01-0617.
- R. Nathan and R. Casagrandi (2004), “A simple mechanistic model of seed dispersal, predation and plant establishment: Janzen–Connell and beyond,” *Journal of Ecology* 92, 733–746. DOI: 10.1111/j.0022-0477.2004.00914.x.
- E. A. Fronhofer, H. J. Poethke and U. Dieckmann (2015), “Evolution of dispersal distance: Maternal investment leads to bimodal dispersal kernels,” *Journal of Theoretical Biology* 365, 270–279. DOI: 10.1016/j.jtbi.2014.10.024.
