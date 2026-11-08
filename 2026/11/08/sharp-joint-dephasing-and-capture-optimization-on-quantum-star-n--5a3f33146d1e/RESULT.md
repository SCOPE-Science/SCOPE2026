# Sharp joint dephasing and capture optimization on quantum star networks

## Finding
For every integer \(N\ge3\), hopping strength \(J>0\), leaf-capture rate \(\kappa>0\), and uniform coherence-dephasing rate \(\gamma>0\), a single excitation initially on a nontrapping leaf of a star with \(N-1\) leaves has the exact mean absorption time
\[
\mathbb E[T]=\frac{N}{\kappa}+\frac{(N-1)\kappa}{4J^2}+\frac{N\gamma}{2J^2}+\frac{N-3}{\gamma}+\frac{(N-2)(N-3)}{2\gamma+\kappa}.
\]
For \(N\ge4\), this function has a unique jointly optimal pair \((\gamma_N,\kappa_N)\) with both parameters strictly positive. In particular the jointly controlled optimum obeys the sharp large-star laws
\[
\frac{\gamma_N}{J\sqrt N}\longrightarrow a_*:=\frac{1-\sqrt3+\sqrt{2\sqrt3}}2,\qquad
\frac{\kappa_N}{J\sqrt N}\longrightarrow b_*:=1+\sqrt3-\sqrt{2\sqrt3},
\]
\[
\min_{\gamma,\kappa>0}\mathbb E[T]
=\frac{N^{3/2}}J+\frac{c\sqrt N}J+o\!\left(\frac{\sqrt N}J\right),
\qquad c=\frac{1}{2(1-a_*)}-\frac{1-a_*}{2}+\frac1{a_*}-\frac52.
\]
Here \(a_*\simeq0.5645794553\), \(b_*\simeq0.8708410894\), and \(c\simeq0.2018347375\). If \(\kappa\) is fixed and \(N\ge4\), the unique dephasing optimum \(\gamma_*(\kappa)\) strictly decreases as capture increases and lies between \(J\sqrt{2(N-3)/N}\) and \(J\sqrt{N-3}\). At \(N=3\), optimal dephasing is instead zero; the minimum over both controls is attained at \((\gamma,\kappa)=(0,\sqrt6J)\) and equals \(\sqrt6/J\).

## Assumptions and scope
Label the central vertex \(0\) and its leaves \(1,\dots,N-1\). The Hamiltonian is \(H=J\sum_{j=1}^{N-1}(|0\rangle\langle j|+|j\rangle\langle0|)\), with \(\hbar=1\), no onsite detuning or peripheral coupling, and the initial transient density matrix \(\rho(0)=|2\rangle\langle2|\). Leaf \(1\) is the absorbing sink. The non-trace-preserving one-excitation evolution is
\[
\mathcal L(\rho)=-i[H,\rho]-\gamma(\rho-\operatorname{diag}\rho)
-\frac\kappa2\{|1\rangle\langle1|,\rho\}.
\]
Thus every off-diagonal entry has dephasing rate \(\gamma\), corresponding to local Lindblad site projectors with rates \(\gamma\); the sink removes probability at rate \(\kappa\rho_{11}\). Define \(T\) through survival \(\Pr(T>t)=\operatorname{tr}\rho(t)\) and \(\mathbb E[T]=\int_0^\infty\operatorname{tr}\rho(t)\,dt\). For \(\gamma>0\), the sink captures with probability one, so this is an unconditional finite mean.

## Proof
**Absorption and resolvent.** The Hilbert–Schmidt dissipative form for any transient matrix \(X\) satisfies
\[
\operatorname{Re}\langle X,\mathcal LX\rangle_{\rm HS}
=-\gamma\sum_{j\ne k}|X_{jk}|^2-\frac\kappa2\sum_j(|X_{1j}|^2+|X_{j1}|^2).
\]
If \(\gamma,\kappa>0\), an eigenmatrix with a nonnegative real-part eigenvalue must be diagonal, with zero entries in row and column \(1\). Its off-diagonal eigenvalue equation says \(X_{jj}=X_{00}\) for each star edge \((0,j)\). Therefore all diagonal entries agree with \(X_{11}=0\), forcing \(X=0\), a contradiction. Every generator eigenvalue has strictly negative real part. Its integrated density matrix \(R=\int_0^\infty\rho(t)dt\) exists and solves \(-\mathcal L R=|2\rangle\langle2|\), with \(\kappa R_{11}=1\).

**Seven-variable exact reduction.** By permutation symmetry among the \(m=N-2\) nontrapping leaves, one may replace the initial matrix by their uniform mixture without changing \(\mathbb E[T]\); trace after absorption is unchanged under these symmetries. Write the shared real diagonal entries as \(p=\rho_{00},q=\rho_{11},o=\rho_{jj}\) (\(j\ge2\)), the imaginary coherences as \(\rho_{01}=ia,\rho_{0j}=ib\), the real trap/nontrap coherence as \(\rho_{1j}=c\), and the real distinct nontrap coherence as \(\rho_{jh}=d\). Direct substitution yields
\[
\begin{aligned}
\dot p&=-2J(a+mb),&\dot q&=2Ja-\kappa q,&\dot o&=2Jb,\\
\dot a&=J(p-q-mc)-(\gamma+\kappa/2)a,
&\dot b&=J(p-c-o-(m-1)d)-\gamma b,\\
\dot c&=J(a+b)-(\gamma+\kappa/2)c,
&\dot d&=2Jb-\gamma d.
\end{aligned}
\]
The initial data are \(o(0)=1/m\) and every other displayed component zero. Writing capitals for time integrals, the integrated equations give
\[
Q=\frac1\kappa,\quad A=\frac1{2J},\quad B=-\frac1{2Jm},\quad
D=-\frac1{m\gamma},\quad C=\frac{m-1}{m(2\gamma+\kappa)},
\]
\[
P=Q+mC+\frac{(\gamma+\kappa/2)A}J,\qquad
O=P-C-(m-1)D-\frac{\gamma B}J.
\]
For \(m=1\), the unused variable \(d\) and its coefficient \(m-1\) are omitted. Adding \(P+Q+mO\) proves the boxed exact mean-time formula.

**Strict convexity, bounds, and the special three-vertex boundary.** For \(N\ge4\), the Hessian is positive definite because the two terms \((N-3)/\gamma\) and \(N/\kappa\) are strictly convex separately in independent positive coordinates; the remaining reciprocal term is convex as a reciprocal of a positive affine function, and the other terms are linear. The function diverges at every boundary of the positive quadrant, including infinity, so it has one and only one minimizer. Its stationary equations are
\[
\frac{N}{2J^2}=\frac{N-3}{\gamma^2}+\frac{2(N-2)(N-3)}{(2\gamma+\kappa)^2},\qquad
\frac{N-1}{4J^2}=\frac N{\kappa^2}+\frac{(N-2)(N-3)}{(2\gamma+\kappa)^2}.
\]
The first equation, strictly monotonic in \(\gamma\), gives for fixed \(\kappa\) a unique optimum. Implicit comparison in \(\kappa\) proves strict decrease; taking \(\kappa\to\infty\) and \(\kappa\downarrow0\) proves the claimed strict two-sided bounds. For \(N=3\) all singular terms have zero coefficients. The continuous \(\gamma=0\) extension is \(3/\kappa+\kappa/(2J^2)+3\gamma/(2J^2)\), with the stated boundary optimum.

**Large-network joint optimum.** Introduce \(a=\gamma/(J\sqrt N)>0\), \(b=\kappa/(J\sqrt N)>0\), and \(s=2a+b\). The exact decomposition is
\[
J\mathbb E[T]=N^{3/2}\left(\frac s4+\frac1s\right)
+\sqrt N\left(\frac1b-\frac b4+\frac{1-3/N}a+\frac{-5+6/N}s\right).
\]
The leading factor is \(1+(s-2)^2/(4s)\), minimized only at \(s=2\). Comparing a joint minimizer with any fixed positive \((a,b)\) on \(2a+b=2\), and using the positive terms of the original mean-time expression, first bounds \(s\) above and away from zero, then bounds \(a,b\) away from zero; hence every subsequential optimizer limit lies on the compact interior segment \(s=2\). On that segment, \(b=2(1-a)\) and the subleading coefficient is
\[
f(a)=\frac1{2(1-a)}-\frac{1-a}{2}+\frac1a-\frac52,\quad 0<a<1.
\]
It satisfies \(f''(a)=(1-a)^{-3}+2a^{-3}>0\), and its sole critical point is \(a_*=(1-\sqrt3+\sqrt{2\sqrt3})/2\); hence convergence to \((a_*,b_*)\). The stationarity equations additionally give \(s-2=O(N^{-1})\), so \(N[s/4+1/s-1]\to0\), proving the two-term minimum asymptotic with the specified \(c=f(a_*)\). All limits are over integers \(N\to\infty\), with \(J\) fixed.

## Verification
The standalone `verify.py` reconstructs the seven integrated equations symbolically, checks rational derivatives and exact asymptotic constants, and independently solves the full \(N^2\)-variable complex Lindbladian resolvent for \(N=3,4,5,6,7\) at four distinct positive parameter triples. It also solves the numerical strictly convex control equations for multiple sizes through \(N=10000\). Command: `python verify.py`; dependencies: `numpy`, `sympy` as recorded in `requirements.txt`. The packaged checker completed 103 assertions. The analytic argument, not the finite tests, establishes the results for all \(N\) and all permitted rates.

## Relationship to prior work
Le, Donati, Severini, and Caruso (2017) analyze noise-assisted transport and the suppression of dark subspaces in quantum networks, motivating the absorbing-star question but not presenting this peripheral-sink mean-time formula. Alterman, Berman, and Strauch (2023) solve related optimization questions for a **fully connected** network; its network adjacency and transport dynamics are different from a star. Pepe, Pouthier, and Yalouz (2023) treat **extended stars with a central absorbing core** and optimize peripheral energy defects, whereas here the trap is a peripheral leaf and both pure dephasing and capture are optimized. Novo and collaborators (2015) study coherent transport on nonregular graphs without this dephased peripheral-star formula. Although the model is solvable by finite Lindblad linear algebra and an implicit derivation from more general methods cannot be ruled out, the stated all-size exact formula and sharp joint optimizer are not supplied by those inspected results.

## Limitations
This is a one-excitation, time-homogeneous, Markovian Haken–Strobl model; it does not cover correlated noise, many-excitation dynamics, detuning, heterogeneous hopping, or traps at the central vertex. The large-star coefficient pertains to simultaneous optimization of both positive rates and not to arbitrary prescribed rates. The initial state must be a single nontrapping leaf (or its permutation). The three-site boundary optimum is separate. The reported priority comparison is limited to the identified and inspected literature; independent audit and experimental validation have not been performed.

## References
- Le, Donati, Severini, and Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures* (2017), https://arxiv.org/abs/1707.07482 (first posted 2017-07-24).
- Alterman, Berman, and Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network* (2023), https://arxiv.org/abs/2309.00164.
- Pepe, Pouthier, and Yalouz, *Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing* (2023), https://arxiv.org/abs/2308.15857.
- Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs* (2015), https://pmc.ncbi.nlm.nih.gov/articles/PMC4657518/.
