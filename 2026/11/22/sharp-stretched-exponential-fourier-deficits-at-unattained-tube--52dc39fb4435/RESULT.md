# Sharp stretched-exponential Fourier deficits at unattained tube boundaries

## Finding

A positive, translation-bounded measure on a horizontal complex strip can have a pure-point \(c\)-Fourier transform whose local total variation grows at the maximum possible exponential type, yet remains below that exponential by a precisely controlled stretched-exponential factor. In the dyadic shifted-lattice construction of Değer and Favorov [1], this deficit is tunable to every fractional exponent strictly between zero and one. In a quadratic model, the logarithmic remainder is bounded uniformly in the Fourier location, not merely small relative to the leading stretched-exponential term.

**General family.** Fix \(a,b>0\), \(\beta>1\), \(\gamma>0\), and an integer \(Q\ge2\) such that \(bQ^{-\gamma}<1\). For every integer \(q\ge Q\), put
\[
 h_q=1-bq^{-\gamma},\qquad w_q=e^{-aq^\beta}.
\]
Define the positive measure on \(\mathbb C\)
\[
 \mu=\sum_{q=Q}^{\infty}w_q\sum_{n\in\mathbb Z}
 \left(\delta_{2^q(n+1/2)+ih_q}+\delta_{2^q(n+1/2)-ih_q}\right),
 \qquad \nu=\widehat\mu^{\,c}.
\]
The minimal closed convex vertical support interval is \([-1,1]\), even though no atom lies on its boundary. The \(c\)-Fourier transform \(\nu\) is a locally finite-total-variation pure-point measure on \(\mathbb R\). Set
\[
 V(t)=|\nu|((t-1,t+1)),\quad
 s=\frac{\beta}{\beta+\gamma},\quad
 L=\frac{\beta+\gamma}{\gamma}
 a^{\gamma/(\beta+\gamma)}
 \left(\frac{2\pi b\gamma}{\beta}\right)^{\beta/(\beta+\gamma)}.
\]
Then, for every such fixed parameter choice,
\[
 \boxed{\displaystyle\lim_{|t|\to\infty}
 \frac{2\pi|t|-\log V(t)}{|t|^s}=L.}
\]
In particular, by taking \(\beta=2\) and \(\gamma=2(1-s)/s\), every \(s\in(0,1)\) occurs. The coefficient \(L\) can also be varied by changing \(a\) and \(b\).

**Uniform bounded-error model.** For the natural choice \(a=b=1\), \(\beta=2\), \(\gamma=1\), \(Q=2\), the stronger, two-sided estimate holds for all real \(t\) of sufficiently large absolute value:
\[
 \boxed{\displaystyle\log V(t)=2\pi|t|-3(\pi|t|)^{2/3}+O(1).}
\]
The \(O(1)\) is independent of \(t\). Equivalently, there exist absolute constants \(c,C,T_0>0\) such that for \(|t|\ge T_0\),
\[
 c\exp\{2\pi|t|-3(\pi|t|)^{2/3}\}
 \le V(t)\le
 C\exp\{2\pi|t|-3(\pi|t|)^{2/3}\}.
\]

## Assumptions and scope

The \(c\)-Fourier transform is the distribution on compactly supported smooth functions \(\varphi\) defined by
\[
 \langle\widehat\mu^{\,c},\varphi\rangle
 =\int_{\mathbb C}\left[\int_{\mathbb R}\varphi(t)e^{-2\pi izt}\,dt\right]d\mu(z).
\]
For each such test function, the inner entire Fourier transform decreases faster than any polynomial in \(\operatorname{Re}z\) uniformly in the fixed strip \(|\operatorname{Im}z|\le1\); the integral therefore converges absolutely. All constants in the general-family asymptotic may depend on the fixed parameters. The quantitative bounded-error assertion concerns the explicit quadratic instance only.

The original dyadic shifted-lattice architecture and the termwise transform below occur in [1, §3]. The claims here concern new *rates of growth* and the Fourier character selection used for the bounded-error lower bound, not the first construction of such measures.

## Proof

**1. Measure and exact Fourier transform.** For each \(q\), the real parts of the atoms form the coset \(2^{q-1}+2^q\mathbb Z\). Since \(\sum_{q\ge Q}w_q<\infty\), each horizontal unit strip contains uniformly bounded mass. Also \(h_q\uparrow1\), so the minimal closed convex set containing the imaginary parts is \([-1,1]\), with no atom at either endpoint.

Poisson summation applied on each coset gives the identity of complex measures, with locally absolutely summable layer variations,
\[
 \nu=\sum_{q=Q}^{\infty}\frac{w_q}{2^q}
 \sum_{k\in\mathbb Z}(-1)^k
 \left(e^{2\pi h_q k/2^q}+e^{-2\pi h_q k/2^q}\right)\delta_{k/2^q}.
 \tag{1}
\]
Indeed the frequency lattice of the \(q\)-th coset has spacing \(2^{-q}\) and the shift by half its period supplies \((-1)^k\). Each bounded frequency interval meets at most \(2R2^q+2\) sites from the \(q\)-th lattice if the interval has length \(2R\). After multiplying by \(2^{-q}w_q\), the sum of these local bounds over \(q\) converges. Consequently, \(\nu\) is a complex Radon measure even though distinct dyadic levels share frequency atoms and may cancel.

**2. A discrete saddle-point lemma.** For \(a,c>0\), \(\beta>1\), \(\gamma>0\), \(d\ge0\), define
\[
 S_d(T)=\sum_{q\ge Q}\exp\{-aq^\beta-cTq^{-\gamma}-dq\},\qquad T>0.
\]
The continuous phase \(f_T(x)=ax^\beta+cTx^{-\gamma}\) is minimized at
\[
 x_T=\left(\frac{c\gamma T}{a\beta}\right)^{1/(\beta+\gamma)},\qquad
 f_T(x_T)=\frac{\beta+\gamma}{\gamma}a x_T^\beta.
\]
The nearest integer to \(x_T\) gives \(f_T(q)=f_T(x_T)+o(T^{\beta/(\beta+\gamma)})\) by Taylor's theorem, and \(dq=o(T^{\beta/(\beta+\gamma)})\) because \(\beta>1\). This proves the lower bound for \(\log S_d\). For an upper bound choose \(K>1/(\beta+\gamma)\): the at most \(O(T^K)\) terms with \(q\le T^K\) are each no larger than \(e^{-f_T(x_T)}\). The remaining terms have sum at most \(\sum_{q>T^K}e^{-aq^\beta}=e^{-\Omega(T^{K\beta})}\), whose exponent dominates \(T^{\beta/(\beta+\gamma)}\). Hence
\[
 \log S_d(T)=-\frac{\beta+\gamma}{\gamma}a
 \left(\frac{c\gamma}{a\beta}\right)^{\beta/(\beta+\gamma)}
 T^{\beta/(\beta+\gamma)}+o(T^{\beta/(\beta+\gamma)}).
 \tag{2}
\]

**3. The general sharp deficit.** For \(t>2\), estimate the absolute contribution of each layer in (1) over \((t-1,t+1)\). Since every represented frequency \(x\) satisfies \(t-1<x<t+1\), counting lattice sites and using \(0<h_q<1\) give
\[
 V(t)\le C e^{2\pi t}\sum_{q\ge Q}
 e^{-aq^\beta-2\pi b(t-1)q^{-\gamma}}.
 \tag{3}
\]
The constant \(C\) does not depend on \(t\). At the integer frequency \(m\), every dyadic level in (1) contributes with positive phase: \((-1)^{m2^q}=1\). Thus for each positive integer \(m\),
\[
 V(t)\ge\nu(\{m\})\ge
 e^{2\pi m}\sum_{q\ge Q}e^{-aq^\beta-2\pi bm q^{-\gamma}-(\log2)q}
 \quad\text{whenever }|m-t|\le\tfrac12.
 \tag{4}
\]
The integer belongs to the open interval defining \(V(t)\). Since \(m=t+O(1)\), equations (2)--(4) sandwich \(2\pi t-\log V(t)\) between two quantities with the same leading term \(Lt^s\). The exact coefficients from (2), with \(c=2\pi b\), give the stated \(L\). The transform formula (1) is invariant under reflection of the frequency variable, so \(V(-t)=V(t)\), completing the two-sided limit.

**4. A bounded remainder for the quadratic model.** Specialize to \(w_q=e^{-q^2}\), \(h_q=1-1/q\), \(q\ge2\). For integers \(m\ge1\), write
\[
 F_m(x)=x^2+\frac{2\pi m}{x},\quad u_m=(\pi m)^{1/3},\quad
 N_m\in\mathbb Z_{\ge2}\text{ nearest to }u_m.
\]
For large \(m\), the continuous minimum is \(F_m(u_m)=3(\pi m)^{2/3}\); moreover \(F_m''(x)=2+4\pi m/x^3\ge2\) and the local second derivative near \(u_m\) is uniformly bounded. Therefore
\[
 F_m(N_m)=3(\pi m)^{2/3}+O(1),\quad
 \sum_{q\ge2}e^{-F_m(q)}\le C e^{-F_m(N_m)},\quad
 \sum_{q\ge2}\frac{e^{-F_m(q)}}q=o(e^{-F_m(N_m)}).
 \tag{5}
\]
For the final little-o, split at \(q=u_m/2\): on the larger indices \(1/q\le2/u_m\), while strong convexity makes the smaller-index tail negligible compared to \(e^{-F_m(N_m)}\).

To prevent cancellation from the different dyadic levels, test the Fourier measure against a character on a full unit frequency cell:
\[
 P_m=\int_{[m,m+1)}e^{-2\pi x}e^{2\pi i2^{N_m-1}x}\,d\nu(x).
\]
The contribution of the exponentially increasing branch in (1) from level \(q\) is
\[
 \frac{e^{-q^2}}{2^q}\sum_{k=m2^q}^{(m+1)2^q-1}
 (-1)^k e^{2\pi i2^{N_m-1}k/2^q}
 e^{-2\pi k/(q2^q)}.
\]
Freeze the last factor at \(e^{-2\pi m/q}\). The full-cell character sum becomes exactly
\[
 \frac1{2^q}\sum_{k=m2^q}^{(m+1)2^q-1}(-1)^k
 e^{2\pi i2^{N_m-1}k/2^q}
 =\begin{cases}1,&q=N_m,\\0,&q\ne N_m.\end{cases}
 \tag{6}
\]
This is ordinary finite geometric-series orthogonality: the character frequencies are \(2^{q-1}\) and \(2^{N_m-1}\) modulo \(2^q\). The total freezing error is bounded by
\[
 2\pi\sum_{q\ge2}q^{-1}e^{-F_m(q)}
 =o(e^{-F_m(N_m)})
\]
using \(|e^{-2\pi(x-m)/q}-1|\le2\pi/q\) for \(x\in[m,m+1)\). The exponentially decreasing branches contribute at most \(C e^{-3\pi m}\) because \(h_q\ge1/2\). Thus (5)--(6) yield
\[
 P_m=e^{-F_m(N_m)}(1+o(1)).
 \tag{7}
\]
By total variation, \(|P_m|\le e^{-2\pi m}|\nu|([m,m+1))\); hence
\[
 |\nu|([m,m+1))\ge c\exp\{2\pi m-3(\pi m)^{2/3}\}
\]
for sufficiently large integers \(m\). If \(t\ge2\) and \(m=\lfloor t\rfloor\), this cell lies in \((t-1,t+1)\); replacing \(m\) by \(t\) changes the displayed exponent by \(O(1)\). For the matching upper bound, (3) and the strong-convexity estimate in (5), now with \(m\) replaced by \(t-1\), give
\[
 V(t)\le C\exp\{2\pi t-3(\pi t)^{2/3}\}.
\]
Reflection gives the same bounds for negative \(t\), and the bounded-error theorem follows.

## Verification

The standalone file `CHECKER.py` verifies the dyadic character-selection identity (6) over finitely many levels and cells, the exact quadratic saddle evaluation, and additional normalized finite-sum inequalities. Invoke `python3 CHECKER.py` in the directory containing this file. The analytic proofs of (2), (5), and the all-real-frequency conclusion are **not** inferred from finite tests. The checker has no third-party dependencies and uses Python's standard library.

## Relationship to prior work

Değer and Favorov [1, §3] introduce the dyadic shifted-lattice example, derive its termwise Poisson formula, and prove only the qualitative statement \(|\widehat\mu^{\,c}|((t-1,t+1))=o(e^{2\pi|t|})\) for arbitrary positive summable weights and heights approaching the tube boundary. This paper retains their construction but quantifies the exact growth deficit, supplies a continuum of fractional exponents, and proves a uniform bounded remainder in one nontrivial quadratic example by a Fourier-character selector. Their qualitative little-o claim alone gives no fractional exponent or matching two-sided bound. The earlier strip analysis [2] establishes exponential-type bounds under its hypotheses, not these precise local variation asymptotics.

## Limitations

The constructed examples are a prescribed parameter family, not universal growth bounds for all positive crystalline measures. The bounded-error refinement is proved for the explicit quadratic model and not for all \(a,b,\beta,\gamma\). It determines neither the eventual exact multiplicative prefactor nor the full oscillatory distribution of the local total variation. Shared dyadic frequency atoms can cancel; the cell-character argument, rather than positivity of each coefficient, is essential for the refined lower bound. Previous source [1] already provides the dyadic architecture and transform identity; no claim of independently discovering those is made. A broader or differently indexed earlier theorem on sharp tube-transform growth could affect novelty.

## References

1. Özkan Değer and Sergii Yu. Favorov, *Analogs of crystalline measures in tube sets*, arXiv:2611.16506v1, first posted 12 November 2026, §3. https://arxiv.org/html/2611.16506v1
2. Sergii Favorov and Özkan Değer, *Some properties of Fourier quasicrystals and measures on a strip*, arXiv:2605.10766v1, 11 May 2026. https://arxiv.org/html/2605.10766v1
