# Sharp fixed-point entropy contrast for majority and minority dynamics on helm graphs

## Finding

Let \(H_n\) be the **helm graph** formed from the wheel \(K_1\vee C_n\) by attaching one private leaf to each rim vertex, with \(n\ge3\). For simultaneous binary **minority** and **majority** updates with retention on ties, write \(U_n\) and \(V_n\) for their respective numbers of one-step fixed configurations on the \(2n+1\) labelled vertices. Define \([t^k]f(t)\) as the coefficient of \(t^k\). Then, for all integers \(n\ge3\),

\[
U_n=2\sum_{z=\lceil n/2\rceil}^{n}\frac{n}{z}[t^{n-z}](1+t+t^2)^z,
\]

\[
V_n=2+2\sum_{k=2}^{\lfloor n/2\rfloor}
\sum_{r=1}^{\min(\lfloor k/2\rfloor,n-k)}
\frac{n}{r}\binom{k-r-1}{r-1}\binom{n-k-1}{r-1}.
\]

Let \(\tau\) be the unique real root of \(\tau^3-\tau^2-\tau-1=0\) greater than one (\(\tau=1.839286755214\ldots\)). Then the **sharp, distinct asymptotics** are

\[
U_n=2\tau^n+O(\gamma^n)\quad\text{for some }0<\gamma<\tau,
\]

\[
V_n\sim 8\left(\frac{\sqrt3}{2}\right)^{n\bmod2}
\sqrt{\frac{3}{2\pi n}}\,3^{n/2}.
\]

Consequently, the fixed-state entropy per vertex is \(\tfrac12\log\tau\) under minority and \(\tfrac14\log 3\) under majority. In particular, the ratio of minority to majority fixed states grows exponentially with base \(\tau/\sqrt3>1\), with an additional \(\sqrt n\) multiplier and an exact parity-dependent leading coefficient.

## Assumptions and scope

The graph is simple, undirected and finite. Its hub \(h\) is adjacent to every rim vertex \(v_i\), whose cyclic neighbors are \(v_{i-1}\) and \(v_{i+1}\), and whose private leaf is \(\ell_i\); indices are modulo \(n\). The hub has degree \(n\), rim vertices degree four, and leaves degree one. A vertex adopts the strict majority (respectively minority) opinion among its **open neighbors**, retaining its own opinion if the neighbor counts tie. There are no random couplings, asynchronous updates, or self-neighbor votes. Both color labels and all vertex positions are distinguished. Only **one-step fixed configurations** are counted, not periods two, transients, or basin sizes. The claim covers every \(n\ge3\), including the triangular wheel \(n=3\).

## Proof

**1. Local dynamics is equivalent to a globally constrained binary word.** For either rule, a fixed configuration makes each private leaf unique: the leaf agrees with its rim parent under majority, and disagrees under minority. Fix an arbitrary hub color; there are two symmetric choices.

Under minority define \(w_i=1\) when rim color equals the hub color. A fixed rim with \(w_i=0\) has its leaf and the hub as opposite-color neighbors, so it is automatically stable. A fixed rim with \(w_i=1\) has only its leaf certainly opposite, so it needs at least one opposite-color rim neighbor. Thus the cyclic word \(w\) must avoid \(111\), and this condition is sufficient for all rim vertices. At the hub, stability requires at least half of its \(n\) neighbors to disagree with it, so \(\sum_i w_i\le\lfloor n/2\rfloor\).

Under majority, instead define \(w_i=1\) when rim color is **opposite** the hub. A rim with \(w_i=0\) has its hub and leaf agreeing with it. A rim with \(w_i=1\) must have at least one rim neighbor with \(w=1\), since its leaf agrees but the hub disagrees. Therefore \(w\) avoids the cyclic pattern \(010\). The hub majority constraint again is \(\sum_i w_i\le\lfloor n/2\rfloor\). These conditions are necessary and sufficient, and the leaves and hub then determine the full configuration uniquely. Hence each count is twice a constrained cyclic-word count.

**2. Exact cyclic-run enumeration.** For minority, put \(k=\sum_iw_i\) and \(z=n-k\). Since \(z\ge\lceil n/2\rceil>0\), the \(z\) gaps after consecutive zeros can contain only zero, one or two ones. There are \([t^k](1+t+t^2)^z\) such gap vectors. Counting pairs consisting of a labelled word and a distinguished zero gives \(z\) times the number of words on one side and \(n\) times the number of gap vectors on the other, proving the formula for \(U_n\).

For majority the all-zero word contributes one per hub color. Every other permitted cyclic word has \(k\ge2\) ones and \(z=n-k\ge1\) zeros, and consists of \(r\ge1\) cyclic runs of ones of lengths at least two alternating with \(r\) nonempty zero runs. The compositions of their lengths number \(\binom{k-r-1}{r-1}\binom{z-1}{r-1}\). Marking an initial one-run boundary counts each labelled cyclic word \(r\) times and gives the factor \(n/r\). Summing over \(r\) and \(k\le\lfloor n/2\rfloor\) proves the formula for \(V_n\).

**3. Weighted cyclic-word transfer matrices.** Index pair states by \(00,01,10,11\). Append a bit \(b\in\{0,1\}\), giving edge \(ab\to bc\) of weight \(y^c\) when the three-bit word \(abc\) avoids the forbidden pattern. The two matrices are explicitly

\[
T_{111}(y)=\begin{pmatrix}
1&y&0&0\\0&0&1&y\\1&y&0&0\\0&0&1&0
\end{pmatrix},\qquad
T_{010}(y)=\begin{pmatrix}
1&y&0&0\\0&0&0&y\\1&y&0&0\\0&0&1&y
\end{pmatrix}.
\]

For \(n\ge3\), the coefficient of \(y^k\) in \(\operatorname{tr}(T_b(y)^n)\) counts exactly the labelled cyclic words avoiding the forbidden triple \(b\) and containing \(k\) ones. Direct expansion yields

\[
\det(xI-T_{111}(y))=x\bigl(x^3-x^2-xy-y^2\bigr),
\]

\[
\det(xI-T_{010}(y))=x\bigl(x^3-(1+y)x^2+xy-y^2\bigr).
\]

**4. Minority exponential with no polynomial penalty.** Let \(L_-(y)\) be the Perron root of \(T_{111}(y)\), which is primitive for positive \(y\). At \(y=1\) it equals \(\tau\), and implicit differentiation gives the typical density of ones

\[
\mu_-:=\left.\frac{d\log L_-(y)}{d\log y}\right|_{y=1}
=\frac{\tau+2}{\tau^2+2\tau+3}<\frac12.
\]

The strict inequality is exactly \(1<\tau^2\). Thus for some fixed \(y>1\) near one, \(L_-(y)/\sqrt y<\tau\). Since all coefficients of the trace polynomial are nonnegative,

\[
\sum_{k>n/2} a_{n,k}
\le y^{-n/2}\sum_{k=0}^n a_{n,k}y^k
=y^{-n/2}\operatorname{tr}(T_{111}(y)^n)
=O\!\left((L_-(y)/\sqrt y)^n\right),
\qquad a_{n,k}:=[t^k]\operatorname{tr}(T_{111}(t)^n).
\]

The nonnegative primitive matrix \(T_{111}(1)\) has one dominant eigenvalue \(\tau\) and all other eigenvalues strictly smaller in modulus. Hence its trace is \(\tau^n+O(\eta^n)\) for some \(\eta<\tau\). Subtract the exponentially small high-density tail and multiply by two to obtain the stated minority asymptotic.

**5. Majority critical-boundary saddle and the parity factor.** Let \(L_+(y)\) be the positive Perron root of \(T_{010}(y)\). At \(y_0=3/4\), the characteristic cubic has the exact root \(L_+(y_0)=3/2\), with remaining two roots of modulus \(\sqrt6/4<3/2\). Implicit differentiation of that cubic yields

\[
\left.\frac{d\log L_+(y)}{d\log y}\right|_{y_0}=\frac12,
\qquad
\left.\frac{d^2\log L_+(e^t)}{dt^2}\right|_{t=\log y_0}=\frac13.
\]

The four-state graph is primitive: it is strongly connected and has loops at both \(00\) and \(11\). Moreover the loops have bit weights zero and one, so the Fourier-twisted matrix \(T_{010}(y_0e^{i\theta})\) has strictly smaller spectral radius than \(3/2\) for every \(\theta\not\equiv0\pmod{2\pi}\). Fourier inversion and the analytic Perron eigenvalue expansion therefore give the lattice local central limit estimate, uniformly for \(k=n/2+O(\log n)\),

\[
[y^k]\operatorname{tr}(T_{010}(y)^n)
\sim y_0^{-k}(3/2)^n\sqrt{\frac{3}{2\pi n}}.
\]

The same Fourier bound gives a uniform upper bound by a constant times this expression, for all \(k\); hence the lower-half sum is dominated by a convergent geometric series. Write \(\epsilon=n\bmod2\) and \(k=\lfloor n/2\rfloor-j\), \(j\ge0\). Relative to \(y_0^{-n/2}\), its weight is \(y_0^{\epsilon/2+j}\). Summing the local limit against \(\sum_{j\ge0}y_0^j=4\) and multiplying by the two hub colors proves

\[
V_n\sim2(3/2)^ny_0^{-n/2}\sqrt{\frac{3}{2\pi n}}
\cdot\frac{y_0^{\epsilon/2}}{1-y_0}
=8(\sqrt3/2)^\epsilon\sqrt{\frac{3}{2\pi n}}\,3^{n/2}.
\]

Because \(\tau>\sqrt3\), the entropy inequality is strict, and dividing the logarithms by \(2n+1\) gives the claimed per-vertex entropies.

## Verification

Two separate standalone Python programs are supplied. `verify_direct.py` enumerates all \(2^{2n+1}\) labelled states for each \(3\le n\le9\), updating each vertex using its actual neighborhood and comparing both rules' one-step fixed-point counts to an independently encoded forbidden-word test. This covers \(699008\) configurations for each rule. `verify_symbolic.py` checks the exact characteristic polynomials and saddle derivatives in rational arithmetic, and independently evaluates the cyclic-run sums against the trace generating functions for all \(3\le n\le54\). It reports large-length numerical ratios as diagnostics, not proofs of limits. Both programs' saved stdout files were reproduced from the standalone scripts in the package. Their independent finite checks are supplementary; the infinite statements follow from the local reduction, exact compositions and spectral/Fourier arguments above.

Small exact counts \((U_n,V_n)\) are \((8,2),(22,10),(32,12),(72,26),(114,30),(246,74),(404,92)\) at \(n=3,4,5,6,7,8,9\), respectively.

## Relationship to prior work

Agur, Fraenkel and Klein (1988) exactly count majority fixed points on an ordinary ring by **simultaneously** forbidding the two isolated-bit patterns, and also count binary rings simultaneously forbidding \(000\) and \(111\). Their formulas do not give the one-sided forbidden patterns **with a global half-density bound** that arise here, nor the helm-graph entropy comparison and critical \(n^{-1/2}\) asymptotic. Their cyclic-word methodology and formulas are acknowledged background, not claimed as new.

Wacław and Burda (arXiv:0801.1224; public preprint of January 8, 2008) study one-spin-stable states of random-coupling Ising spin glasses and estimate disorder-averaged metastable-state complexity. Their coupling ensemble is different from fixed deterministic binary tie-retaining dynamics on helms. Banks and Djirar (1992) describe graph-theoretic methods for fixed points and shift cycles in cellular automata, without an accessible covering exact helm census. The known sunlet majority fixed-state census concerns \(C_n\) with one private leaf at each cycle vertex but **without a universal hub**, so it does not impose the half-density condition. The classical wheel and fan results concern graphs without a leaf at every rim vertex; their fixed-state counts and periods do not imply these helm-specific formulas. The helm graph itself is standard and its definition is not a new contribution.

## Limitations

Only fixed states are counted; no assertion is made about the full period spectrum, basins or convergence time. The large-\(n\) asymptotics distinguish even and odd lengths; dropping the parity factor from the leading majority coefficient would be incorrect. The detailed 1992 Banks–Djirar report was not fully accessible, so historical priority is qualified; an older specialised weighted-word enumeration may exist. The standard Fourier local-limit step is proved here by spectral-gap and Taylor-expansion arguments, not by finite checking. Independent external validation has not been performed.

## References

1. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224 (first public preprint 2008-01-08), https://arxiv.org/abs/0801.1224 .
2. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, doi:10.1016/0012-365X(88)90005-2; accessible full text at https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
3. S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, Sheffield ACSE Research Report 459 (1992), https://eprints.whiterose.ac.uk/id/eprint/79286/ .
4. E. W. Weisstein, *Helm Graph*, MathWorld, https://mathworld.wolfram.com/HelmGraph.html .
