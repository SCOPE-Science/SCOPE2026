# Entropy collapse and a complete two-stage orbit census for finite-depth Kolakoski shifts

## Finding

Let \(X_k\) be the bilateral binary subshift of sequences whose first \(k\) run-length derivatives all exist over the alphabet \(\{1,2\}\), and put \(h_k=h_{\mathrm{top}}(X_k,\sigma)\). For every integer \(k\ge2\),

\[
\frac23 h_{k-1}\le h_k\le\frac34 h_{k-1},\qquad h_1=\log\varphi,\quad \varphi=\frac{1+\sqrt5}{2}.
\]

In particular every finite-depth shift has positive entropy, while the upper bound decays geometrically:

\[
\left(\frac23\right)^{k-1}\log\varphi\le h_k\le
\left(\frac34\right)^{k-1}\log\varphi.
\]

The second stage has a complete finite-type and periodic-orbit classification. It is exactly the subshift forbidding the six blocks

`111`, `222`, `12121`, `21212`, `112211`, `221122`.

Its entropy is \(h_2=\log\lambda\), where \(\lambda\) is the unique positive root of \(\lambda^4-\lambda^3-1=0\), namely \(\lambda=1.3802775690976141\ldots\). Its Artin–Mazur zeta function is exactly

\[
\zeta_{X_2}(z)=\frac{1}{(1+z+z^2)(z^4+z-1)(z^6-z^5-z^4+z^3-1)}.
\]

The second-stage system is a mixing shift of finite type, so its unique measure of maximal entropy is the Parry measure of the finite graph described below.

## Assumptions and scope

All sequences are indexed by \(\mathbb Z\), with the ordinary left shift \(\sigma\). A *run* is a maximal constant block; a sequence is one-time differentiable if all its runs have length one or two. If a sequence is so differentiable, its derivative \(d(x)\) lists its successive run lengths in order. For bilateral sequences the index origin of this run list is immaterial to membership in a shift-invariant class. Define

\[
X_0=\{1,2\}^{\mathbb Z},\qquad
X_k=\{x\in X_1:d(x)\in X_{k-1}\}\quad(k\ge2),
\]

with \(X_1\) the set having no runs longer than two. Equivalently \(X_k\) is the space of \(k\)-times differentiable bilateral sequences, not the finite-word class with truncated boundary runs. Each \(X_k\) is nonempty, compact, and shift invariant. There are no finite or one-sided runs in these two-sided sequences, since lengths are bounded.

The zeta function counts all *indexed* spatial-periodic configurations, not circular words up to rotation:

\[
\zeta_{X_2}(z)=\exp\left(\sum_{n\ge1}
\frac{|\operatorname{Fix}(\sigma^n)|}{n}z^n\right).
\]

## Proof

### 1. Exact suspension entropy identity

For \(k\ge1\), write \(Y=X_{k-1}\). Each \(x\in X_k\) is uniquely specified by a sequence \(y\in Y\) of run lengths, a binary choice \(a\in\{1,2\}\) of the first run's symbol, and an offset \(0\le j<y_0\) of the physical origin inside that run. This is an explicit topological conjugacy between \((X_k,\sigma)\) and the integer tower with roof \(r(y,a)=y_0\) over the finite extension

\[
T(y,a)=(\sigma y,3-a).
\]

At the last tower level, the map moves to \((T(y,a),0)\); at other levels it increments the offset. The first return from the beginning of one run to the beginning of the next takes exactly \(y_0\) physical shifts. The map and its inverse are continuous because all run lengths are bounded by two and locating a run boundary requires only a bounded window.

For any invariant probability \(\nu\) of \(T\), write \(\mu\) for its shift-invariant marginal on \(Y\). The extension has a finite two-element fiber, so its relative entropy is zero and \(h_\nu(T)=h_\mu(\sigma)\). By the tower entropy formula, the physical shift has metric entropy

\[
\frac{h_\mu(\sigma)}{\int y_0\,d\mu}
=\frac{h_\mu(\sigma)}{1+\mu([2])}.
\]

Conversely every invariant probability \(\mu\) on \(Y\) lifts to the \(T\)-invariant measure \(\mu\otimes\operatorname{Unif}\{1,2\}\). The variational principle thus gives the **exact identity**

\[
\boxed{\displaystyle h_k=\sup_{\mu\in\mathcal M_\sigma(X_{k-1})}
\frac{h_\mu(\sigma)}{1+\mu([2])}}.
\]

The formula also holds at \(k=1\), using \(X_0\) as the binary full shift. It does not assert that maximizers on successive levels are related by a simple Markov law.

### 2. Uniform two-sided entropy contraction

For \(k\ge2\), every \(y\in X_{k-1}\) has no run of three consecutive ones. Consequently each length-three window contains a two, and every invariant measure \(\mu\) on \(X_{k-1}\) satisfies \(\mu([2])\ge1/3\). Since \(h_\mu(\sigma)\le h_{k-1}\), the exact identity implies \(h_k\le(3/4)h_{k-1}\).

For the other bound, take any measure of maximal entropy \(\mu_0\) on \(X_{k-1}\). Global interchange of the letters \(1\leftrightarrow2\) preserves \(X_{k-1}\), since it leaves all run lengths unchanged; write \(c_*\mu_0\) for the interchanged measure. The invariant mixture \(\mu=(\mu_0+c_*\mu_0)/2\) has \(\mu([2])=1/2\). Measure-theoretic entropy is affine on invariant measures, so \(h_\mu(\sigma)=h_{k-1}\). The exact identity gives \(h_k\ge(2/3)h_{k-1}\).

Finally \(X_1\) is the finite-type shift forbidding `111` and `222`. Its standard run-length Fibonacci recurrence has Perron root \(\varphi\), giving \(h_1=\log\varphi\). Iteration yields both stated bounds, positivity at every finite level, and zero entropy for \(\bigcap_{k\ge1}X_k\), as the latter is a subshift of every \(X_k\).

### 3. Exact forbidden patterns at depth two

Membership in \(X_2\) means that both \(x\) and its run-length sequence \(d(x)\) have no constant runs of length three. The first restriction forbids `111` and `222`. Three successive run lengths equal to one produce three consecutive singleton runs in \(x\), equivalently `12121` or `21212` in a bilateral word with runs at most two. Three successive run lengths equal to two produce three consecutive double runs, equivalently `112211` or `221122`. These exhaust the restrictions. This proves the six-pattern characterization without a finite-enumeration assumption.

Let \(V\) be the set of all length-five words avoiding these six patterns. There are fourteen such words:

`11211`, `11212`, `11221`, `12112`, `12122`, `12211`, `12212`, `21121`, `21122`, `21211`, `21221`, `22112`, `22121`, `22122`.

Form the zero-one adjacency matrix \(A=(A_{uv})_{u,v\in V}\), with \(A_{uv}=1\) precisely when the last four symbols of \(u\) equal the first four of \(v\), and the concatenation of \(u\) with the last symbol of \(v\) avoids all six forbidden words. (Otherwise set \(A_{uv}=0\).) This fourteen-state presentation has eighteen edges. Its edge shift is conjugate to \(X_2\) by the usual overlapping-block coding; therefore

\[
|\operatorname{Fix}(\sigma^n)|=\operatorname{tr}(A^n)\quad(n\ge1),
\qquad\zeta_{X_2}(z)=\det(I-zA)^{-1}.
\]

An exact integer polynomial calculation, independently specified by the state list and adjacency rule above, gives

\[
\begin{aligned}
\det(I-zA)={}&(1+z+z^2)(z^4+z-1)\\
&\cdot(z^6-z^5-z^4+z^3-1),\\[2pt]
\det(\lambda I-A)={}&\lambda^2(\lambda^2+\lambda+1)(\lambda^4-\lambda^3-1)\\
&\cdot(\lambda^6-\lambda^3+\lambda^2+\lambda-1).
\end{aligned}
\]

The same exact calculation finds every entry of \(A^{15}\) positive. Therefore \(A\) is primitive. Interchanging the letters acts freely on the fourteen states and commutes with \(A\). The quotient by this involution is a seven-state nonnegative matrix \(B\), with characteristic polynomial

\[
\det(\lambda I-B)=\lambda(\lambda^2+\lambda+1)(\lambda^4-\lambda^3-1).
\]

The positive Perron eigenvector of \(A\) is unique up to scaling and hence fixed by letter interchange; its eigenvalue is therefore a positive eigenvalue of \(B\). The polynomial \(\lambda^4-\lambda^3-1\) has exactly one positive real root (Descartes' rule, with existence by sign change), whereas the other displayed factors of \(\det(\lambda I-B)\) have no positive roots. Thus the Perron eigenvalue is exactly that root and \(h_2=\log\lambda\). Primitivity also proves topological mixing and the unique measure of maximal entropy.

## Verification

The standalone `checker.py` reconstructs the state graph directly from the six forbidden blocks; checks the fourteen vertices, eighteen edges, both determinant identities, and the seven-state letter-interchange quotient; confirms \(A^{15}\) has strictly positive entries; and independently enumerates all \(2^n\) cyclic binary words for every \(1\le n\le12\), comparing the exact allowed counts to \(\operatorname{tr}(A^n)\). The resulting fixed-point counts are

\[
(0,0,6,0,0,18,0,8,42,10,22,90)\qquad(1\le n\le12).
\]

Run with `python3 checker.py` using Python 3.10 or later and SymPy. The graph and determinant computations are exact integer/symbolic calculations; the displayed decimal root alone is an approximation. The infinite-depth inequalities and conjugacy are proved above rather than inferred from finite enumeration.

## Relationship to prior work

Mitchell, Walton and Whittaker (2026, arXiv:2611.06878v1) establish topological transitivity of the full infinite-depth Kolakoski shift and state its finite derivative hierarchy explicitly. Cassaigne and Henry (2026, arXiv:2603.10733v1) establish structural results and word-complexity bounds for infinitely smooth words. The present statement concerns different dynamical invariants: a uniform quantitative entropy comparison across finite differentiation depths and an exact second-stage periodic-orbit/zeta classification. No claim is made that the run-length tower construction, variational principle, Fibonacci recurrence, or general finite-type zeta identity is new. The distinct contribution lies in their explicit application and resulting finite-depth formulas; priority beyond the inspected literature remains open to further checking.

## Limitations

The contraction factors \(2/3\) and \(3/4\) are rigorously valid uniform bounds, not claimed optimal. The theorem does not calculate \(h_k\) exactly for all higher \(k\), nor classify their zeta functions. It does not settle uniqueness, frequencies, or periodicity of the classical Kolakoski word. The periodic census concerns \(X_2\), not the full infinite-depth shift. Finite computational checks certify the explicit finite matrix algebra but do not replace the structural entropy proof. Historical literature may contain equivalent finite-depth formulas not identified here.

## References

1. A. C. Mitchell, J. J. Walton, M. F. Whittaker, *The full Kolakoski shift is topologically transitive*, arXiv:2611.06878v1, 4 November 2026, https://arxiv.org/html/2611.06878v1 .
2. J. Cassaigne and R. Henry, *The complexity of finite smooth words over binary alphabets*, arXiv:2603.10733v1, 11 March 2026, https://arxiv.org/abs/2603.10733 .
3. M. Zwierzyński, *Shuffle Squares in Differentiable Words*, arXiv:2610.07828, 6 October 2026, https://arxiv.org/abs/2610.07828 .
