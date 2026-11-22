# Hidden translation and sharp leafwise pitchfork in a three-dimensional sine map

## Finding

Consider the real three-dimensional discrete system studied by Rajagopal, Kanagaraj, Volos and Karthikeyan [1],
\[
F(x,y,z)=\bigl(y,\sin z,\alpha+\beta x+\gamma y-\delta\sin z+\mu z\bigr).
\]
On the neutral-feedback cancellation surface \(\mu=1\), \(\delta=\beta+\gamma\), with \(\beta>0\) and \(\gamma\ge0\), write \(s=\beta+\delta\) and
\[
W(x,y,z)=z+\beta x+\delta y.
\]
**Theorem.** For every \(\alpha\in\mathbb R\), the exact identity \(W(F(x,y,z))=W(x,y,z)+\alpha\) holds. For any \(s>0\), if \(\alpha\ne0\), every orbit obeys \(z_n/n\to\alpha\) and the map has no invariant Borel probability on \(\mathbb R^3\). If \(0<s<1\), there exists exactly one continuous \(2\pi\)-periodic graph \(h_\alpha=(X_\alpha,Y_\alpha):\mathbb R/(2\pi\mathbb Z)\to[-1,1]^2\) such that, for every initial state and \(\theta_n=W(x_0,y_0,z_0)+n\alpha\pmod{2\pi}\),
\[
\max\{|x_n-X_\alpha(\theta_n)|,|y_n-Y_\alpha(\theta_n)|\}
\le s^{\lfloor n/2\rfloor}
\max\{|x_0-X_\alpha(\theta_0)|,|y_0-Y_\alpha(\theta_0)|\}.
\]
When \(\alpha/(2\pi)\) is irrational, every orbit has the same bounded-coordinate empirical distribution \((h_\alpha)_*m\), where \(m\) is normalized Haar measure on the circle; its two coordinate means agree, and their common value satisfies the *uniform* explicit estimate
\[
\left|\int Y_\alpha\,dm-\frac{\beta\sin(2\alpha)+\delta\sin\alpha}{2}\right|\le\frac32s^2.
\]
When \(\alpha=0\), every plane \(W=w\) contains exactly one equilibrium and attracts all its own trajectories, with convergence as above. Every invariant Borel probability for this case is a mixture of point masses on these equilibria.

The condition \(s<1\) is sharp for this uniform leafwise uniqueness and exponential-contraction statement. At \(\alpha=0\), the leaf \(W=\pi\) has the fixed point \((0,0,\pi)\). At \(s=1\) its derivative *within that leaf* has eigenvalue \(1\); for every \(s>1\) the same leaf contains at least two additional equilibria. More precisely, fixing \(0<\beta_0\le\delta_0\) with \(\beta_0+\delta_0=1\), and setting \(\beta=t\beta_0\), \(\delta=t\delta_0\), \(\gamma=\delta-\beta\), the transition at \(t=1\) is a supercritical leafwise pitchfork: for all sufficiently small \(t-1>0\), there are exactly three equilibria on \(W=\pi\), the noncentral two are leafwise attracting, and their common first and second coordinates are
\[
r_\pm(t)=\pm\sqrt{6(t-1)}+O((t-1)^{3/2}).
\]
No hyperbolic attraction in the full three-dimensional space is claimed, because \(W\) is conserved at \(\alpha=0\).

## Assumptions and scope

The model and parameter names are exactly those in Equation (1) of [1]; the cancellation surface is a specific parameter subfamily. Conditions \(\beta>0\), \(\gamma\ge0\) imply \(\delta=\beta+\gamma\ge\beta\) and \(s=2\beta+\gamma>0\). All initial states in \(\mathbb R^3\) are permitted, all iterates exist, and no boundedness hypothesis is imposed on the initial \(z\)-coordinate. The phase variable is \(\theta=W\pmod{2\pi}\). The quantitative graph and empirical-measure assertions require \(s<1\); the exact translation identity does not. The pitchfork is stated on a single *invariant* real plane at zero drift, not on the full space.

## Proof

1. **Exact factor and reduction.** Direct substitution in the stated map yields
   \[
   W\circ F=\mu z+\beta x+(\gamma+\beta)y+\alpha+(\delta-\delta)\sin z=W+\alpha
   \]
   under \(\mu=1\) and \(\gamma+\beta=\delta\). Thus, writing \(\theta=W\pmod{2\pi}\), \(z=W-\beta x-\delta y\), the map becomes the triangular skew product
   \[
   \theta' =\theta+\alpha\pmod{2\pi},\qquad (x',y')=G_\theta(x,y):=\bigl(y,\sin(\theta-\beta x-\delta y)\bigr).
   \]
   Moreover \(W_n=W_0+n\alpha\) exactly.

2. **Uniform two-step contraction and invariant graph.** Two fibers with the same forcing phase satisfy the componentwise error domination
   \[
   (|\Delta x'|,|\Delta y'|)^\mathsf T\le M(|\Delta x|,|\Delta y|)^\mathsf T,
   \quad M=\begin{pmatrix}0&1\\\beta&\delta\end{pmatrix}.
   \]
   The maximum row sum of \(M^2\) is
   \[
   \max\{s,\,\beta+\delta s\}=s<1,
   \]
   since \(\beta+\delta s=s-\delta(1-s)\le s\), and \(\|M\|_\infty=1\). The graph transform on continuous periodic maps, \((\mathcal Th)(\theta)=G_{\theta-\alpha}(h(\theta-\alpha))\), therefore satisfies \(\|\mathcal T^2h-\mathcal T^2k\|_\infty\le s\|h-k\|_\infty\). By the contraction theorem, \(\mathcal T^2\) has a unique fixed graph, and commutation with \(\mathcal T\) forces it to be fixed by \(\mathcal T\) itself. Every invariant graph is that graph. Invariance forces both components into \([-1,1]\). Comparing an arbitrary fiber orbit to this graph proves the displayed global rate, including the first step and all initial states.

3. **Drift, measures, and stationary bias.** Since \(|x_n|,|y_n|\le1\) for \(n\ge2\), the exact identity \(z_n=W_0+n\alpha-\beta x_n-\delta y_n\) yields \(z_n/n\to\alpha\) for \(\alpha\ne0\). An invariant probability on \(\mathbb R^3\) would push forward under \(W\) to a probability on \(\mathbb R\) invariant under the nonzero translation \(w\mapsto w+\alpha\), which is impossible by partition into half-open intervals of length \(|\alpha|\).

   When \(\alpha/(2\pi)\) is irrational, uniform convergence to the graph and unique ergodicity of irrational circle rotation imply the asserted empirical law for every continuous bounded test function of \((x,y)\). Invariance yields \(X_\alpha(\theta+\alpha)=Y_\alpha(\theta)\), hence their Haar means coincide. Setting \(X_0(\theta)=\sin(\theta-2\alpha)\) and \(Y_0(\theta)=\sin(\theta-\alpha)\), invariance and \(|X_\alpha|,|Y_\alpha|\le1\) give the uniform sup-norm estimates \(|X_\alpha-X_0|\le s\), \(|Y_\alpha-Y_0|\le s\). Expanding the identity \(Y_\alpha(\theta+\alpha)=\sin(\theta-\beta X_\alpha(\theta)-\delta Y_\alpha(\theta))\) at zero displacement has Taylor remainder at most \(s^2/2\). Replacing \(X_\alpha,Y_\alpha\) by \(X_0,Y_0\) in the linear term adds at most \(s^2\). Finally, \(\int\cos\theta\sin(\theta-k\alpha)\,dm=-\tfrac12\sin(k\alpha)\), proving the quantitative bias bound.

4. **Zero drift and the sharp boundary.** If \(\alpha=0\), each real plane \(W=w\) is invariant. Its fixed points have \(x=y=r\) and satisfy \(r=\sin(w-sr)\). For \(s<1\), this scalar equation is a strict contraction, so it has exactly one solution, denoted \(r(w)\), and the two-step contraction brings every point on that plane to \((r(w),r(w),w-sr(w))\). The equilibrium curve is continuous. For any invariant probability, Poincaré recurrence together with convergence to the equilibrium on each leaf forces its mass onto the equilibrium curve, giving exactly arbitrary probability mixtures of its Dirac masses.

   On the plane \(w=\pi\), the fixed-point equation reduces to \(r=\sin(sr)\). For \(s\le1\), only \(r=0\) solves it. For \(s>1\), \(\sin(sr)-r\) is positive just to the right of zero and nonpositive at \(r=1\), so a positive solution exists; oddness gives a negative solution. For \(t\) sufficiently close to \(1\), monotonicity of \(\sin(tr)/r\) for \(0<r\le1\) ensures exactly one positive solution. Taylor expansion gives \(r_\pm(t)^2=6(t-1)/t^3+O((t-1)^2)\). The leafwise derivative at a fixed point is \(\cos(tr)\begin{pmatrix}0&1\\t\beta_0&t\delta_0\end{pmatrix}\). At \(r=0\) its Perron eigenvalue passes from below to above one at \(t=1\). At each nonzero branch, the Perron eigenvalue is \(1-(3-1/(1+\beta_0))(t-1)+O((t-1)^2)<1\), and the other eigenvalue remains strictly inside the unit disk. Thus the noncentral equilibria attract within the leaf and the central equilibrium is unstable within it. At \(t=1\) the Perron eigenvalue is exactly one. This establishes sharpness and the stated supercritical pitchfork.

## Verification

The standalone file `check_resonance.py` tests 400 algebraic-drift instances, 100 independent global contraction cases, six small-supercritical pitchfork/stability cases, and an irrational-rotation mean diagnostic. Its deterministic finite tests passed. The proof of all-real-state, all-time, and invariant-measure assertions is analytic and does not depend on numerical sampling. Run `python3 check_resonance.py` using Python 3 standard library. The graph mean estimate is an explicit inequality, not a numerical extrapolation.

## Relationship to prior work

The initiating article [1], Section 2 Equation (1) and Sections 3–6, varies the feedback and coupling parameters and reports numerical bifurcation, symmetry and synchronization phenomena. It does not identify \(W\), the neutral cancellation surface, the phase-fiber reduction, global quantitative graph attraction, the invariant-probability dichotomy, or the leafwise pitchfork. The precursor [2] has the same first two components but *no linear feedback \(\mu z\)* and uses a bounded-orbit argument instead; its stability assertions do not entail the result here. General invariant-graph literature [3] establishes constructions in other skew-product classes; standard contraction theory is invoked explicitly here and is not presented as new. What is model-specific is the exact resonant coordinate, globally sharp small-gain regime, measured mean correction and explicit neutral-leaf transition.

## Limitations

The subfamily \(\mu=1\), \(\delta=\beta+\gamma\) is nongeneric (codimension two in the full five-parameter system) and different from the illustrative numerical parameter values in [1]. The invariant graph theorem covers \(s<1\), not arbitrary strong feedback; its sharpness is for the *uniform all-phase leafwise* property, not an assertion that every \(s\ge1\) orbit is unstable. No mixing, positive entropy or cryptographic properties are asserted. The stationary law is for the bounded coordinates; for nonzero drift the full real system has no invariant probability. An independent audit and exhaustive publication-priority search have not been performed.

## References

[1] K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, “Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems,” *Symmetry* **15** (2023), 780, first published 2023-03-23. https://doi.org/10.3390/sym15040780

[2] M. Mammeri, “Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps,” *Bulletin of Mathematical Analysis and Applications* **9** (2017), no. 1, 1–8. https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf

[3] T. Withers, *Invariant Graphs of Skew Product Dynamical Systems*, PhD thesis, University of Manchester (2017). https://research.manchester.ac.uk/en/studentTheses/invariant-graphs-of-skew-product-dynamical-systems/
