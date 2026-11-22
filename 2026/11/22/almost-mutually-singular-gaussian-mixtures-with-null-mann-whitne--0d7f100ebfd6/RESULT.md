# Almost mutually singular Gaussian mixtures with null Mann–Whitney and niche-overlap effects

## Finding
Let \(\Phi\) denote the standard normal CDF and let \(\mathcal N(\mu,s^2)\) denote the normal law with mean \(\mu\) and variance \(s^2\). For every \(s>0\), define
\[
q_s=\Phi\!\left(\frac{1}{\sqrt2 s}\right)-\frac12,\qquad
r_s=\Phi\!\left(\frac{3}{\sqrt2 s}\right)-\frac12,\qquad
w_s=\frac{q_s}{q_s+r_s}.
\]
Consider the two probability laws
\[
F_s=\tfrac12\mathcal N(-1,s^2)+\tfrac12\mathcal N(1,s^2),\qquad
G_s=(1-w_s)\mathcal N(0,s^2)+\tfrac{w_s}{2}\mathcal N(-2,s^2)+\tfrac{w_s}{2}\mathcal N(2,s^2).
\]
Both have strictly positive real-analytic densities on \(\mathbb R\), are symmetric about zero, and are distinct; their variances are \(1+s^2\) and \(4w_s+s^2\), respectively, so the latter is strictly larger for every \(s>0\). For independent \(X\sim F_s\) and \(Y\sim G_s\), the Mann–Whitney functional \(\theta=\Pr(X<Y)\) and the median-split niche-overlap functional \(I_2\) used in Beck–Langthaler–Bathke's two-sample test satisfy **exactly**
\[
\boxed{\theta(F_s,G_s)=I_2(F_s,G_s)=\tfrac12\quad\text{for all }s>0.}
\]
The reverse-oriented niche-overlap functional \(I_1\) is also \(1/2\). Within the indicated three-component family with fixed \(s\) and variable outer weight \(w\in[0,1]\), the choice \(w_s\) is the **unique** weight with \(I_2=1/2\), and \(1/4<w_s<1/2\). Nevertheless, with \(d_{\mathrm{TV}}\) denoting total variation distance,
\[
\boxed{1-4\Phi\!\left(-\frac1{2s}\right)\le d_{\mathrm{TV}}(F_s,G_s)\le1,\qquad
\lim_{s\downarrow0}d_{\mathrm{TV}}(F_s,G_s)=1.}
\]
Thus the null-effect fiber contains pairs of everywhere-positive smooth densities arbitrarily close to the maximal possible total variation separation. At \(s=0.1\), the rigorous lower bound is \(0.9999988533937125\). For every fixed \(s>0\), the published fixed-level Gaussian-ball joint test based solely on the pair of estimated functionals is not consistent against \((F_s,G_s)\): its rejection probability does not tend to one when both sample sizes grow in a fixed positive ratio. This does **not** imply any analogous limitation of omnibus tests using the entire empirical distributions.

## Assumptions and scope
The two samples are independent, with iid observations within each group; all variables are real-valued. The median-split overlap functional is the one defined for continuous \(F,G\) with \(G\)'s median \(m_G\) by
\[
I_2(F,G)=2\!\left(\int_{m_G}^{\infty}F(y)\,dG(y)-\int_{-\infty}^{m_G}F(y)\,dG(y)\right).
\]
Here both medians are zero and their densities are positive. The first source in the references defines the functionals and its joint test. The theorem concerns **each fixed** \(s>0\), and then the separate limit \(s\downarrow0\) for total variation. It does not interchange the small-noise and increasing-sample-size limits. The entire family of mixtures is a theoretical set of alternatives, not a model for any particular dataset.

## Proof
**1. Symmetric reduction.** Let \(F,G\) be atomless and symmetric about zero with strictly increasing CDFs. Then \(X-Y\) is symmetric and continuous, so \(\theta=\Pr(X<Y)=1/2\). Since \(G(0)=1/2\), symmetry yields
\[
I_2(F,G)=4\int_0^\infty F(y)\,dG(y)-1.
\]
For \(y>0\), \(2F(y)-1=\Pr(|X|<y)\); integrating against \(2\,dG(y)\), the conditional law of \(|Y|\) on the positive half-line, gives the exact identity
\[
\boxed{I_2(F,G)=\Pr(|X|<|Y|).}
\]
This is the *median-split niche overlap*, not the density-intersection overlap coefficient. Since both medians are zero, the reverse functional satisfies \(I_1=1-I_2\), either by integration by parts on the positive half-line or the known equal-median identity.

**2. Folded-normal comparison.** For independent \(U\sim\mathcal N(a,s^2)\) and \(V\sim\mathcal N(b,s^2)\), \(V-U\) and \(V+U\) are independent normals, of means \(b-a,b+a\) and variances \(2s^2\). Consequently, writing
\[
p=\Phi\!\left(\frac{b-a}{\sqrt2s}\right),\qquad
h=\Phi\!\left(\frac{b+a}{\sqrt2s}\right),
\]
we have
\[
\Pr(|U|<|V|)=\Pr((V-U)(V+U)>0)=ph+(1-p)(1-h).
\]
Since \(|X|\) for \(X\sim F_s\) has the folded \(\mathcal N(1,s^2)\) law, this formula gives, for \(Y\sim\mathcal N(0,s^2)\),
\[
A_s=\Pr(|X|<|Y|)=\tfrac12-2q_s^2.
\]
For \(Y\) drawn from the symmetric outer pair \(\tfrac12\mathcal N(-2,s^2)+\tfrac12\mathcal N(2,s^2)\), it gives
\[
B_s=\Pr(|X|<|Y|)=\tfrac12+2q_sr_s.
\]
The overlap against the three-component mixture with outer weight \(w\) therefore is
\[
I_2(F_s,G_{s,w})=(1-w)A_s+wB_s=\tfrac12+2q_s\bigl(wr_s-(1-w)q_s\bigr).
\]
Both \(q_s,r_s\) are strictly positive; hence the unique zero of the final parenthesis is \(w=w_s=q_s/(q_s+r_s)\). The function \(\Phi(t)-1/2\) is increasing and strictly concave for \(t>0\), so \(q_s<r_s<3q_s\). This implies \(1/4<w_s<1/2\). The limits \(w_s\to1/2\) as \(s\downarrow0\) and \(w_s\to1/4\) as \(s\to\infty\) follow from normal tail limits and differentiability at zero. The mixture densities are strictly positive and real analytic. Distinctness for every \(s\) follows directly by evaluating their characteristic functions at frequency \(\pi\): after factoring out \(e^{-s^2\pi^2/2}\), the respective values are \(-1\) and \(1-w_s+w_s\cos(2\pi)=1\). Their variances are \(s^2+1\) and \(s^2+4w_s\); since \(w_s>1/4\), the second is strictly larger.

**3. Sharp total-variation supremum.** Let
\[
E=[-3/2,-1/2]\cup[1/2,3/2],\qquad \overline\Phi(z)=1-\Phi(z).
\]
Each of the two components of \(F_s\) is centered in one interval of \(E\), so \(F_s(E)\ge1-2\overline\Phi(1/(2s))\). Each of the three components of \(G_s\) is centered at least \(1/2\) away from \(E\), hence \(G_s(E)\le2\overline\Phi(1/(2s))\). By the event characterization of total variation,
\[
d_{\mathrm{TV}}(F_s,G_s)\ge F_s(E)-G_s(E)\ge1-4\overline\Phi(1/(2s)).
\]
The upper bound \(d_{\mathrm{TV}}\le1\) is universal, proving convergence to one. As the two densities are everywhere positive, equality \(d_{\mathrm{TV}}=1\) is not attained for any finite \(s\); the result is a **sharp supremum** within strictly positive real-analytic pairs.

**4. Consequence for the joint test.** With \(s>0\) fixed, the Gaussian mixture densities are positive and smooth, and the ratio \(f_s/g_s\) is bounded on the inverse image under \(G_s\) of every compact subinterval of \((0,1)\). Thus the regularity hypotheses of the joint empirical-process central limit theorem in Beck–Langthaler–Bathke apply when the sample-size ratio tends to a finite positive constant. Both population coordinates equal \(1/2\), so the centered and sample-size-scaled estimated effect vector converges to a finite centered Gaussian law, rather than diverging under the alternative. The null-calibrated joint test rejects outside a fixed nonzero-radius ball in this normalized plane; a centered finite Gaussian law always assigns positive probability to that ball. Therefore its asymptotic rejection probability is strictly smaller than one. This argument does not identify the exact alternative rejection probability and does not apply to a test based on additional features of the full empirical distributions.

## Verification
The standalone `verify.py` evaluates \(w_s,A_s,B_s\), directly integrates both CDF-based functionals and both mixture densities, and numerically integrates the total-variation distance for seven or more representative noise widths. Its assertions independently compare the direct integrals to the analytic identities and check the rigorous event bound. Run with `python verify.py` using Python 3 with NumPy and SciPy. These numerical checks are supplementary; the proof above establishes all parameter values without a finite-enumeration inference.

For example, at \(s=0.1\), the checker obtains an integrated total variation of approximately \(0.999999022\), compared with the rigorous lower bound \(0.9999988533937125\). The exact effect equalities and supremum proof do not rely on this numerical integration.

## Relationship to prior work
Beck, Langthaler and Bathke introduced inference combining the Mann–Whitney relative effect and an asymmetric niche-overlap functional, derived their joint asymptotic theory and explicitly noted that the resulting test is not omnibus (Section 5, Remark 6). Their Theorem 1 gives the attainable two-dimensional *effect range*, not the maximal statistical distance between pairs with exactly null effects. Their journal article's examples and appendices do not exhibit the present closed-form Gaussian-mixture null-effect family or its total-variation supremum. Parkinson-Schwarz and Bathke earlier studied testing via a niche-overlap functional, including an equal-median reciprocal identity, but did not establish the present mixture family or maximal separation. The folded-normal probability reduction and simple normal comparisons used here are classical ingredients; the claim is their exact joint-test null-fiber construction and sharp distance consequence, not a new Gaussian integral identity.

## Limitations
The two effects do not characterize distribution equality; that general fact is already acknowledged in the primary source. The contribution is the explicit **all-noise Gaussian mixture** tuning rule and the **maximal total-variation failure within regular strictly positive analytic densities**. The result does not prove that a permutation or omnibus two-sample test is inconsistent, does not give a finite-sample power expression for the source test, and does not assert a simultaneous \(s\downarrow0\), sample-size-\(\infty\) limit. Historical-priority assessment is based on the listed sources and targeted record/literature searches; older general observations about rank effects may overlap with the construction's mechanism.

## References
1. J. Beck, P. B. Langthaler, A. C. Bathke, *Combining stochastic tendency and distribution overlap towards improved nonparametric effect measures and inference*, arXiv:2311.17564 (first public preprint 2023-11-29); *Scandinavian Journal of Statistics* 52 (2025), 1138–1175. https://arxiv.org/abs/2311.17564 ; https://doi.org/10.1111/sjos.12783 .
2. J. H. Parkinson-Schwarz and A. C. Bathke, *Testing for equality of distributions using the concept of (niche) overlap*, *Statistical Papers* 63 (2022), 225–242; first published online 2021-05-26. https://doi.org/10.1007/s00362-021-01239-y .
3. MSC2020 62G10, *Nonparametric hypothesis testing*. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=62G20 .
