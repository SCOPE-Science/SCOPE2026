# Parameter-free stationary activity calibration in the quadratic-perturbed Sprott E family
## Finding
Consider the three-parameter quadratic perturbation of the Sprott E flow
\[
\dot x=yz+h(x),\qquad \dot y=x^2-y,\qquad \dot z=1-4x,
\]
where \(h(x)=e x^2+f x+g\) and \(e,f,g\in\mathbb R\). For every compactly supported invariant Borel probability measure \(\mu\),
\[
\mathbb E_\mu[x\mid z]=\frac14,\qquad
\mathbb E_\mu[x^2\mid y]=y,\qquad
\mathbb E_\mu[yz\mid x]=-h(x).
\]
In particular \(y\ge0\) \(\mu\)-almost surely and
\[
\mathbb E_\mu[y]=\mathbb E_\mu[x^2]
=\frac1{16}+\operatorname{Var}_\mu(x)
=\frac1{16}+\frac1{16}\mathbb E_\mu[\dot z^2].
\]
The same conditional laws give the exact fluctuation decompositions
\[
\operatorname{Var}_\mu(yz)=\operatorname{Var}_\mu(h(x))+\mathbb E_\mu[\dot x^2],
\]
\[
\operatorname{Var}_\mu(x^2)=\operatorname{Var}_\mu(y)+\mathbb E_\mu[\dot y^2],
\qquad
\operatorname{Var}_\mu(x)=\frac1{16}\mathbb E_\mu[\dot z^2].
\]
The mean-activity floor \(\mathbb E_\mu[y]\ge1/16\) is sharp. Equality holds exactly for the equilibrium Dirac measure at
\[
E=\left(\frac14,\frac1{16},-e-4f-16g\right).
\]
Hence every non-equilibrium compact stationary state has \(\mathbb E_\mu[y]>1/16\), uniformly over all real perturbation parameters.

## Assumptions and scope
The flow is the polynomial vector field displayed above on \(\mathbb R^3\), with arbitrary real \(e,f,g\). The measure \(\mu\) is a Borel probability measure invariant under the flow and supported on a compact invariant set. Compact support ensures that all polynomial observables used below are integrable and that the generator identity can be applied without growth issues.

No existence claim is made for non-equilibrium compact invariant sets at every parameter triple. The statement is conditional: whenever such a compact stationary state exists, the displayed identities hold. The equilibrium \(E\) exists for every real \(e,f,g\).

## Proof
Let \(L\) be the generator of the flow. Invariance gives \(\int L\phi\,d\mu=0\) for every continuously differentiable test function \(\phi\). Because the coordinate projections of the compact support are compact intervals, continuous one-variable test functions suffice to identify the corresponding conditional expectations.

For a continuously differentiable primitive \(\Phi\) of a continuous test function \(\psi\), take \(\phi(x,y,z)=\Phi(z)\). Then
\[
0=\int \psi(z)(1-4x)\,d\mu.
\]
Since this holds for every continuous \(\psi\),
\[
\mathbb E_\mu[1-4x\mid z]=0,
\]
which is equivalent to \(\mathbb E_\mu[x\mid z]=1/4\).

Similarly, with \(\phi=\Phi(y)\),
\[
0=\int \psi(y)(x^2-y)\,d\mu,
\]
so \(\mathbb E_\mu[x^2\mid y]=y\). Because a conditional expectation of the nonnegative random variable \(x^2\) is nonnegative, this also gives \(y\ge0\) almost surely. With \(\phi=\Phi(x)\),
\[
0=\int \psi(x)(yz+h(x))\,d\mu,
\]
so \(\mathbb E_\mu[yz\mid x]=-h(x)\).

Taking ordinary expectations in the first two conditional identities gives
\[
\mathbb E_\mu[x]=\frac14,\qquad \mathbb E_\mu[y]=\mathbb E_\mu[x^2].
\]
Therefore
\[
\mathbb E_\mu[y]=\frac1{16}+\operatorname{Var}_\mu(x).
\]
Since \(\dot z=1-4x=-4(x-1/4)\),
\[
\operatorname{Var}_\mu(x)=\frac1{16}\mathbb E_\mu[\dot z^2],
\]
which proves the mean-activity law.

For the fluctuation laws, write \(R_x=\dot x=yz+h(x)\). The conditional identity gives \(\mathbb E_\mu[R_x\mid x]=0\), so \(R_x\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(x\), in particular to \(h(x)-\mathbb E_\mu[h(x)]\). Because \(yz=-h(x)+R_x\), Pythagoras in \(L^2(\mu)\) yields
\[
\operatorname{Var}_\mu(yz)=\operatorname{Var}_\mu(h(x))+\mathbb E_\mu[R_x^2].
\]
Likewise \(R_y=\dot y=x^2-y\) has \(\mathbb E_\mu[R_y\mid y]=0\), and \(x^2=y+R_y\), giving
\[
\operatorname{Var}_\mu(x^2)=\operatorname{Var}_\mu(y)+\mathbb E_\mu[R_y^2].
\]

Finally, equality \(\mathbb E_\mu[y]=1/16\) is equivalent to \(\operatorname{Var}_\mu(x)=0\), hence \(x=1/4\) almost surely. The preceding variance decomposition then gives \(\operatorname{Var}_\mu(x^2)=0=\operatorname{Var}_\mu(y)+\mathbb E_\mu[\dot y^2]\), so \(y=1/16\) almost surely. The support of an invariant probability measure is invariant; on that support the coordinate \(x\) is constant, so \(\dot x=0\). Thus
\[
0=\frac1{16}z+h\!\left(\frac14\right),
\]
forcing \(z=-e-4f-16g\). Hence \(\mu=\delta_E\). Conversely \(\delta_E\) is invariant and attains equality.

## Verification
The proof uses only the invariant-measure generator identity, conditional-expectation orthogonality, and elementary variance algebra. A standalone symbolic checker verifies the equilibrium coordinates, the centered identity \(\dot z=-4(x-1/4)\), and the algebraic residual forms used in the variance decompositions. Its output is included with the result.

The key probabilistic step is exact, not numerical: if \(R_x=yz+h(x)\), then \(\mathbb E[R_x\mid x]=0\); if \(R_y=x^2-y\), then \(\mathbb E[R_y\mid y]=0\). No finite simulation is used to infer an infinite-time identity.

## Relationship to prior work
Sprott's 1994 catalogue introduced case E, whose unperturbed equations are \(\dot x=yz\), \(\dot y=x^2-y\), and \(\dot z=1-4x\). Wei and Wang introduced the three-parameter quadratic perturbation \(h(x)=e x^2+f x+g\) and identified its unique equilibrium; their study emphasized chaotic regimes, bifurcation structure, and synchronization. Wang, Sun, Wei, and Xi subsequently analyzed Hopf bifurcation, dynamics at infinity, and robust synchronization for the same quadratic-perturbed system.

The present result concerns invariant probability measures rather than local bifurcation or synchronization. Its parameter-independent conditional regressions and exact stationary activity calibration are not consequences of the equilibrium formula alone: they constrain every compact recurrent statistical state, including periodic or chaotic ones, and isolate the equilibrium as the unique equality case of the mean-activity floor.

## Limitations
The theorem does not prove that a non-equilibrium compact invariant set exists for a given parameter triple, does not classify attractors, and does not establish ergodicity or mixing. It applies only to compactly supported invariant probability measures. The literature comparison cannot exclude an unindexed or differently phrased prior statement; the closest inspected sources establish the vector field and analyze bifurcation/control questions rather than these stationary conditional and fluctuation laws.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* 50 (1994), R647–R650. DOI: 10.1103/PhysRevE.50.R647. Published 1 August 1994.
2. Z. Wei and Z. Wang, “Chaotic behavior and modified function projective synchronization of a simple system with one stable equilibrium,” *Kybernetika* 49 (2013), 359–374. DML-CZ: dmlcz/143372.
3. Z. Wang, W. Sun, Z. Wei, and X. Xi, “Dynamics analysis and robust modified function projective synchronization of Sprott E system with quadratic perturbation,” *Kybernetika* 50 (2014), 616–631. DOI: 10.14736/kyb-2014-4-0616.
