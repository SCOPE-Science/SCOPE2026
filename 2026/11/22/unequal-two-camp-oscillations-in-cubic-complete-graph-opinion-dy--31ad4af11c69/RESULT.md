# Unequal two-camp oscillations in cubic complete-graph opinion dynamics

## Finding

Let \(N\ge3\), let \(m,\ell\ge1\) be integers with \(m+\ell=N\), and fix a partition into blocks of these sizes. For \(a,\gamma>0\) and \(W=(\mathbf1\mathbf1^\top-I)/(N-1)\) consider
\[
F(v)=[(1-\gamma)I+\gamma W]v+\gamma a[(I-W)v]^{\circ3},\qquad v\in\mathbb R^N,
\]
where the cube is componentwise. Write
\[
\nu=\frac{N\gamma}{N-1},\quad \beta=\nu-2,\quad k=\gamma a\left(\frac{N}{N-1}\right)^3,\quad D=m^2-m\ell+\ell^2,\quad M=\max(m,\ell),\quad q=\min(m,\ell).
\]
There is a nonzero sign-reversing interblock difference if and only if \(\beta>0\). Then there is a unique antipodal orbit (the same unordered pair regardless of phase), with block difference of magnitude \(d_*=N\sqrt{\beta/(kD)}\). Every common translation of it is also a period-two orbit. Its two-step return map is exponentially attracting on the uniform-translation quotient exactly when
\[
\frac12<\frac m\ell<2,\qquad 0<\beta<\beta_c=\frac{2D}{N(2M-q)}.
\]
In this case all sufficiently nearby trajectories approach translates of the two-phase cycle. The full system has a neutral translation multiplier; individual translates are not isolated attractors.

To distinguish spectral instability from equality in this test, suppose \(\beta>0\). If \(M<2q\), a quotient return multiplier has modulus greater than one exactly for \(\beta>\beta_c\); at \(\beta=\beta_c\) the quotient is nonhyperbolic with no multiplier of modulus greater than one. If \(M>2q\), a quotient multiplier has modulus greater than one for every \(\beta>0\). If \(M=2q\), one quotient multiplier is identically one. On that balance boundary a multiplier exceeds one exactly when \(\beta>2/3\) for \(q\ge2\), or when \(\beta>1\) for \(q=1\). Thus the strict-attraction upper bound need not by itself mark linear instability at the singleton boundary \((M,q)=(2,1)\).

The smallest odd \(N\) admitting a transversely exponentially attracting unequal antipodal two-camp cycle is five. Block sizes \((2,3)\) have \(\beta_c=7/10\). With \(\gamma=9/5\), \(a=16/63\), an exact example is
\[
\left(\frac{81}{140},\frac{81}{140},-\frac{59}{140},-\frac{59}{140},-\frac{59}{140}\right)\quad\longleftrightarrow\quad -\left(\frac{81}{140},\frac{81}{140},-\frac{59}{140},-\frac{59}{140},-\frac{59}{140}\right),
\]
with one-step quotient eigenvalues \(-1/2,-2/7,-23/28,-23/28\).

## Assumptions and scope

The opinions lie in \(\mathbb R^N\), with no clipping, stubborn agents, or time-dependent influences. A two-camp cycle here has two internally homogeneous blocks whose difference exactly reverses each step. The theorem concerns this orbit and its local stability to arbitrary small perturbations, not all cycles or global convergence. The spectral boundary descriptions do not assert a nonlinear classification at modulus one. The five-agent example lies in \([-1,1]^5\) in both phases; no invariance of the whole cube is assumed.

## Proof

**1. Exact two-block reduction.** Put \(P=I-\mathbf1\mathbf1^\top/N\). Then \(I-W=(N/(N-1))P\) and \(F(v)=v-\nu Pv+k(Pv)^{\circ3}\). If the block values are \(u,z\), write their difference \(d=u-z\) and their population mean \(s=(mu+\ell z)/N\). The blockwise deviations from the mean are \(\ell d/N\) and \(-md/N\). Inserting them yields
\[
d'=(1-\nu)d+\frac{kD}{N^2}d^3,\qquad s'=s+\frac{km\ell(\ell-m)}{N^3}d^3.
\]
In the first formula use \(m^3+\ell^3=ND\); in the second sum the blockwise cubes with multiplicity and divide by \(N\).

**2. The antipodal orbit.** For \(d\ne0\), the condition \(d'=-d\) is \(kDd^2/N^2=\beta\). Hence there are no such differences at \(\beta\le0\). For \(\beta>0\), choose phase \(d=d_*>0\) and put
\[
H=\frac{km\ell(\ell-m)}{N^3}d_*^3,\qquad s_*=-H/2,\qquad (u_*,z_*)=\left(s_*+\frac\ell N d_*,s_*-\frac mN d_*\right).
\]
The new difference and mean are \(-d_*\) and \(-s_*\), so \(F(v_*)=-v_*\). Oddness gives \(F(-v_*)=v_*\), with primitive period two. The antipodal condition fixes the mean for each sign of the difference, yielding uniqueness up to phase. Since \(F(v+t\mathbf1)=F(v)+t\mathbf1\), all common translates form the cycle family.

**3. Full return spectrum.** The one-step Jacobian is \(J(v)=I-\nu P+3k\operatorname{diag}((Pv)_i^2)P\), so the phase Jacobians coincide even on every translate. The uniform multiplier is one. On tangent vectors supported in one block with zero sum, \(P\) is the identity and the diagonal term is constant; the eigenvalues are
\[
\lambda_m=-1+\frac{\beta N(2\ell-m)}D\quad(m-1\text{ copies}),\qquad
\lambda_\ell=-1+\frac{\beta N(2m-\ell)}D\quad(\ell-1\text{ copies}).
\]
The remaining quotient direction measures the block difference; differentiating the scalar difference equation gives \(\lambda_d=-1+2\beta\). The mean can depend on this direction but cannot feed back into the quotient, and there is no mixing of the within-block subspaces. Thus the complete return spectrum is \(1,\lambda_d^2,\lambda_m^2,\lambda_\ell^2\) with the indicated multiplicities. A singleton block contributes no within-block eigenvalue.

**4. Strict stability and its boundaries.** The difference direction requires \(0<\beta<1\). Consider the within-block eigenvalue of the larger block, present since \(N\ge3\). If \(M>2q\), that eigenvalue is less than \(-1\) for \(\beta>0\); if \(M=2q\), it is exactly \(-1\). When \(M<2q\), both blocks are nonsingletons, and both within-block eigenvalues increase from \(-1\) as \(\beta\) increases. The larger coefficient of \(\beta\) is \(N(2M-q)/D\), from the smaller-block mode (both coefficients coincide if \(M=q\)). It reaches \(+1\) at \(\beta_c\). Also \(N(2M-q)-2D=3q(M-q)\ge0\), so \(\beta_c\le1\). This proves the strict criterion and the spectral behavior at and above \(\beta_c\) when \(M<2q\).

When \(M=2q\), \(N=3q\), \(D=3q^2\), and the smaller-block eigenvalue, **if present**, is \(-1+3\beta\). For \(q\ge2\) it gives the strict-instability boundary \(\beta>2/3\), including the case \(\beta>1\) where the difference mode is also unstable. For \(q=1\) the mode \(-1+3\beta\) is absent, so the return spectrum on the quotient is just \(1,(-1+2\beta)^2\) and strict instability requires \(\beta>1\). For example, at \(N=3\), block sizes \((1,2)\), and \(\beta=3/4\), the quotient return multipliers are \(1,1/4\), despite \(\beta>\beta_c=2/3\).

When the quotient spectrum lies strictly inside the unit circle, the two-step quotient map is locally contracting in an equivalent norm. If \(s\) denotes the mean, the two-step change in \(s\) depends smoothly only on the quotient coordinates and vanishes at the cycle. Thus along nearby iterates this change is bounded by a summable geometric sequence. The even-step mean converges, the odd-step state follows by continuity, and both phases approach a common translate as claimed.

**5. Odd-size witness.** At \(N=3\) only block sizes \((1,2)\) or \((2,1)\) are possible, so the larger-block return multiplier equals one. At \(N=5\), \((2,3)\) is strictly balanced in the sense of the ratio test, and \(D=7\). The chosen parameters give \(\nu=9/4\), \(\beta=1/4\), \(k=25/28\), \(d_*=1\) and \(H=3/70\). The block formulas and eigenvalue formulas give the displayed cycle and spectrum.

## Verification

The companion `checker.py` uses exact rational arithmetic. Its recorded run checked 65 partitions with \(3\le N\le12\) at \(\beta=1/4\) and the rational five-agent example. It checks construction, Jacobian actions and agreement with the strict inequalities at that sample. It does not test the singleton upper-instability endpoint at \(\beta=1\); that endpoint and the other boundary cases follow from the exact spectrum in Proof steps 3–4.

## Relationship to prior work

Kumar and Yao introduce this cubic model and obtain the \(2<\nu<3\) balanced oscillation interval for a uniformly weighted complete graph. Their treatment of asymmetry through nonuniform directed weight perturbations differs from changing the cluster sizes while keeping uniform complete-graph weights. Here the extension is the exact size-dependent criterion on the translation quotient and the odd-size minimum; the equal-size interval is recovered, not new. Cosenza and Parravano give structural precedents for stability of two clusters with quadratic local maps and common forcing. Glendinning's work on asymmetric clusters in globally coupled maps is related; the exact coverage of that broader literature is a historical limitation. The two-cluster results for discrete Kuramoto networks have a different sine-coupled update.

## Limitations

Only this sign-reversing two-block family for exact complete-graph coupling is classified. The behavior at unit quotient multipliers is not settled nonlinearly, and local attraction modulo translation does not imply global convergence or isolated attraction. A finite comparison does not establish historical priority.

## References

1. R. Kumar and N. Yao, *Analysis and Consensus Control of Emergent Dynamic Polarization in Minimally-Nonlinear Opinion Dynamics*, arXiv:2608.09724v1 (2026), https://arxiv.org/abs/2608.09724.
2. M. G. Cosenza and A. Parravano, *Dynamics of Coupling Functions in Globally Coupled Maps: Size, Periodicity and Stability of Clusters*, arXiv:nlin/0107046 (2001), https://arxiv.org/abs/nlin/0107046.
3. P. Glendinning, *Stability of Asymmetric Cluster States in Globally Coupled Maps*, author manuscript, https://personalpages.manchester.ac.uk/staff/paul.glendinning/preprints/clust.pdf.
