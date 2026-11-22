# Sharp hexagonal contraction beyond small gain in two inhibitory event operators

## Finding

Let \(D_{\mathrm p},D_{\mathrm n}\) be nonempty compact intervals in \((0,\infty)\), let \(I=[L,U]\) be a compact interval, and let \(\epsilon\ge0\). Assume
\[
D_{\mathrm p}+D_{\mathrm n}+[-\epsilon,\epsilon]\subseteq I,
\qquad \max(D_{\mathrm p}\cup D_{\mathrm n})<L.
\]
Suppose \(f:I\to D_{\mathrm p}\) and \(g:I\to D_{\mathrm n}\) are nonincreasing and globally Lipschitz with constants \(0\le a<1\) and \(0\le b<1\). For every two-sided timing perturbation \(\eta=(\eta^{\mathrm p},\eta^{\mathrm n})\) with \(\|\eta^i\|_\infty\le\epsilon\), the one-lag event feedback
\[
\begin{aligned}
p_k&=f(p_{k-1}+n_{k-1}+\eta^{\mathrm p}_{k-1}),\\
n_k&=g(n_{k-1}+p_k+\eta^{\mathrm n}_{k-1}),\qquad k\in\mathbb Z,
\end{aligned}
\]
has exactly one solution in \((D_{\mathrm p}\times D_{\mathrm n})^{\mathbb Z}\). It is strictly causal and shift-equivariant as a function of the perturbation.

Define the hexagonal difference norm
\[
N(u,v)=\max\{|u|,|v|,|u+v|\},\qquad
q=a+b-ab=1-(1-a)(1-b)<1.
\]
For two trajectories with the **same** forcing, their state differences contract at every forward step by the factor \(q\). For arbitrary forcings \(\eta,\widetilde\eta\), the unique bilateral responses obey the uniform bound
\[
\sup_k N(p_k-\widetilde p_k,n_k-\widetilde n_k)
\le \frac{a\|\eta^{\mathrm p}-\widetilde\eta^{\mathrm p}\|_\infty+b\|\eta^{\mathrm n}-\widetilde\eta^{\mathrm n}\|_\infty}{(1-a)(1-b)}.
\]
At zero forcing the unique solution is constant and yields one positive alternating periodic event rhythm. Its common period is the unique root of \(T=f(T)+g(T)\) in \(I\).

The factor \(q\) is **the sharp universal one-step factor in this norm** for the stated gain class. In particular, both gains can be \(4/5\), so their sum \(8/5\) violates the usual sum-small-gain condition while the closed loop is still globally contractive with the sharp factor \(24/25\). Strict individual gains below one are also a sharp universal boundary: at gains \((1,0)\), an admissible affine example has a continuum of distinct bounded two-cycles.

## Assumptions and scope

The event operator for the first subsystem is \((\Psi^{\mathrm p}\mathbf T)_k=f(T_{k-1})\); that for the second is \((\Psi^{\mathrm n}\mathbf T)_k=g(T_{k-1})\). They have exactly one-step interval memory, not arbitrary infinite fading memory. The chronological ordering is \(\cdots<t_{\mathrm n,k}<t_{\mathrm p,k}<t_{\mathrm n,k+1}<\cdots\). Their delays are \(p_k=t_{\mathrm p,k}-t_{\mathrm n,k}\) and \(n_k=t_{\mathrm n,k+1}-t_{\mathrm p,k}\), and the elapsed event intervals are \(p_k+n_k\) and \(n_k+p_{k+1}\), with additive perturbations as defined above.

The prescribed interval condition ensures both input-interval arguments stay in \(I\), and \(p_k,n_k<L\) ensures that a response precedes the next driving input. No smoothness beyond monotonicity and Lipschitz continuity is assumed. All conclusions concern the event-domain recurrence, not existence of any particular physical state-space neuron realization.

## Proof

**1. One-step contraction.** Take two starting pairs \((p,n)\) and \((\widetilde p,\widetilde n)\), with the same forcing. Put \(u=p-\widetilde p\), \(v=n-\widetilde n\), and write the successor differences as \((u',v')\). By monotonicity and Lipschitz continuity, for some \(A\in[0,a]\) and \(B\in[0,b]\), including the zero-input-difference cases,
\[
u'=-A(u+v),\qquad v'=-B(u'+v).
\]
Let \(M=N(u,v)\). Because \(0\le A,B<1\),
\[
|u'|\le aM,\qquad
|u'+v|=|-Au+(1-A)v|\le M,\qquad
|v'|\le bM.
\]
Finally,
\[
|u'+v'|=|(1-B)u'-Bv|
\le [A+B-AB]M\le [a+b-ab]M.
\]
The other two components are bounded by the same \(q=a+b-ab\). Thus \(N(u',v')\le qN(u,v)\), uniformly over all admissible states, forcing sequences and times.

**2. Forced perturbations.** Hold the input state fixed and compare two perturbations at the same time. Denote the forcing differences by \(e_{\mathrm p},e_{\mathrm n}\). The successor differences have the form \(u'=-Ae_{\mathrm p}\) and \(v'=-B(u'+e_{\mathrm n})\). Consequently,
\[
N(u',v')\le a|e_{\mathrm p}|+b|e_{\mathrm n}|.
\]
A triangle inequality between a state change and a forcing change gives
\[
M_k\le qM_{k-1}+a|e_{\mathrm p,k-1}|+b|e_{\mathrm n,k-1}|.
\]
Repeated iteration produces the stated two-sided response inequality when the solutions exist, since \(1-q=(1-a)(1-b)\).

**3. Existence and uniqueness on the full time axis.** Each time-dependent state update maps the compact rectangle \(D_{\mathrm p}\times D_{\mathrm n}\) into itself and has the same \(q<1\) Lipschitz constant in \(N\). Fix a time \(k\). Start the recurrence at \(-m\) from an arbitrary state and evolve to \(k\). For two different starting times, compare at their later starting time; the values at \(k\) differ by at most \(q^{k+m}\operatorname{diam}_{N}(D_{\mathrm p}\times D_{\mathrm n})\). The pullback states therefore form a Cauchy sequence, defining a full bilateral solution by continuity. Any two full bounded solutions, compared over \(m\) preceding steps, differ by at most \(q^m\operatorname{diam}_{N}\), so are equal. The same construction makes the response strictly causal; shifting both forcing streams and their solution indices yields another solution and therefore the same shifted response. Forward differences decay at least at rate \(q^j\).

**4. Unforced periodic rhythm.** The zero perturbation is shift invariant, so uniqueness forces \(p_k=p^*\) and \(n_k=n^*\) independent of \(k\). The interval \(I\) contains every sum of admissible output delays. Hence, for \(h(T)=T-f(T)-g(T)\), one has \(h(L)\le0\) and \(h(U)\ge0\); moreover \(h\) is strictly increasing because \(f\) and \(g\) are nonincreasing. The unique root \(T^*\) gives \((p^*,n^*)=(f(T^*),g(T^*))\). The positive delays strictly below \(L\) realize the alternating rhythm.

**5. Sharpness beyond summed small gain.** Fix \(0<\delta<1/4\), choose \(D_{\mathrm p}=D_{\mathrm n}=[1-\delta,1+\delta]\), \(I=[2-3\delta,2+3\delta]\), and perturbation budget \(\epsilon=\delta\). For any \(0<a,b<1\) put
\[
f(T)=1-\delta\tanh\left(\frac a\delta(T-2)\right),\qquad
g(T)=1-\delta\tanh\left(\frac b\delta(T-2)\right).
\]
All event-operator assumptions hold and the exact incremental gains are \(a,b\). At the fixed state \((1,1)\), the differential of the successor map in the direction \((0,1)\) is \((-a,-b(1-a))\). Its \(N\)-norm is exactly \(a+b-ab=q\), while the input direction has norm one. No smaller universal contraction factor is possible. For \(\delta=1/10\) and \(a=b=4/5\), the sum of gains equals \(8/5>1\), but \(q=24/25\).

For a sharp endpoint counterexample, take \(D_{\mathrm p}=[4/5,6/5]\), \(D_{\mathrm n}=\{1\}\), \(I=[9/5,11/5]\), \(\epsilon=0\), \(f(T)=3-T\) and \(g(T)=1\). All conditions except \(a<1\) hold, with exact gains \((a,b)=(1,0)\). Then \(n_k\equiv1\) and \(p_k=2-p_{k-1}\); every \(p_{2j}=1+s\), \(p_{2j+1}=1-s\), \(|s|\le1/5\), is a bounded bilateral solution. By reversing the roles one obtains the analogous endpoint with gains \((0,1)\). Thus strict individual gain bounds cannot be relaxed to inclusive inequalities in a universal uniqueness theorem.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. The checker includes 6,561 exact-rational one-step contraction cases; 21 exact boundary two-cycle cases; 2,401 nonlinear admissible-state comparisons; 1,080 nonlinear forced contraction steps; four limiting-derivative sharpness tests; and four above-threshold two-cycle computations. The norm inequality, the infinite-time existence and uniqueness, and endpoint nonuniqueness are proved in the preceding paragraphs; none relies on finite enumeration.

## Relationship to prior work

Cecconi, Bin, Marconi and Sepulchre (2026) formulate the two-event feedback recurrence and prove unique stable solutions if the sum of incremental gains is below one, for arbitrary fading-memory event operators. Their first-order filter has a *decreasing* event describing function. The present result replaces the sum condition by two individual strict unit bounds in the narrower natural class of nonincreasing one-lag response operators; it supplies a sharp hexagonal contraction factor, explicit admissible examples outside the original gain regime, and a counterexample at the boundary. It makes no claim about arbitrary memory operators.

Al-Salman, AlSharawi and Kallel (2019) study global stability of planar mixed-monotone second-order recurrences via invariant domains and embeddings, not the sharp event-loop two-component estimate or its two-sided perturbed-response bounds. Garab and Pötzsche (2019) study Morse decompositions for scalar delay-difference equations with feedback; this likewise does not identify the present one-lag event-space threshold. General Gauss–Seidel fixed-point principles provide useful background, but their standard assumptions do not directly state the sharp coefficient \(a+b-ab\) for this inhibitory event chronology.

## Limitations

The conclusion applies only to one-interval-memory, nonincreasing response functions on the specified globally invariant compact domains. An arbitrary fading-memory operator with the same individual Lipschitz bounds need not satisfy this proof. The constant \(q\) is a sharp uniform one-step *norm* factor and need not equal the asymptotic spectral radius for a fixed smooth model. The mathematical construction is in event space; it does not by itself produce a physical neuron circuit with the same response law. A historical equivalent specialized to sequential inhibitory response maps cannot be ruled out by the available literature searches. The work has received no independent validation.

## References

1. A. Cecconi, M. Bin, L. Marconi and R. Sepulchre, *Event-based analysis of neuromorphic feedback systems*, arXiv:2611.13832v1 (first public version, 10 November 2026), Sections III–V, especially equations (12)–(19). https://arxiv.org/html/2611.13832v1
2. A. Al-Salman, Z. AlSharawi and S. Kallel, *Extension, embedding and global stability in two dimensional monotone maps*, arXiv:1912.07493 (2019), Sections 1–2. https://arxiv.org/abs/1912.07493
3. Á. Garab and C. Pötzsche, *Morse Decompositions for Delay-Difference Equations*, Journal of Dynamics and Differential Equations 31 (2019), 903–932 (first online 2018). https://doi.org/10.1007/s10884-018-9685-8
