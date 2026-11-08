# Hidden winding waves in square-flat three-color prism dynamics

## Finding

For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) have labelled upper rail \(u_i\), lower rail \(v_i\), and rungs \(u_iv_i\), with indices modulo \(n\). Give every vertex a color in \(\mathbb Z/3\mathbb Z\). For colors \(a,b\), let \(\delta(a,b)\) be \(0\) when the colors agree, \(1\) when \(b=a+1\pmod3\), and \(-1\) otherwise. A coloring is **square-flat** if the signed \(\delta\)-sum around each of its \(n\) elementary squares is zero. Define its longitudinal winding
\[
H_n=\sum_{i=0}^{n-1}\delta(X(u_i),X(u_{i+1})).
\]
For square-flat colorings, \(H_n\in3\mathbb Z\). The eventual activity rates for the synchronous three-color cyclic cellular automaton (CCA) and the synchronous threshold-one Greenberg--Hastings model (GHM), started separately from the **same** coloring, are respectively
\[
\alpha_{\rm CCA}=\frac{|H_n|}{n},\qquad
\alpha_{\rm GHM}=\frac{|H_n|}{3n}.
\]
In particular, square-flatness does **not** imply eventual synchronization: for each \(n\ge3\), some square-flat colorings have nonzero winding.

Let \(F_n\) count the labelled square-flat initial colorings. Its exact value is
\[
F_n=\lambda_+^n+\lambda_-^n+3\cdot2^n+4(-1)^n,\qquad
\lambda_\pm=\frac{7\pm\sqrt{33}}2.
\]
Define a \(9\times9\) matrix indexed by ordered pairs of colors, with Laurent polynomial entries
\[
T(z)_{(a,b),(c,d)}=
\mathbf1\bigl\{\delta(a,c)+\delta(c,d)-\delta(b,d)-\delta(a,b)=0\bigr\}
 z^{\delta(a,c)}.
\]
For each integer \(h\), the **exact** number of square-flat colorings of winding \(h\) is
\[
N_n(h)=[z^h]\operatorname{tr}(T(z)^n).
\]
In particular, \(N_n(0)\) is the exact number of square-flat colorings that synchronize, for **either** CCA or GHM.

Sample a uniformly random square-flat coloring. With
\[
\sigma^2=\frac54-\frac{19\sqrt{33}}{132}=0.4231311342\ldots,
\]
its winding satisfies
\[
\frac{H_n}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,\sigma^2),
\qquad
\frac{N_n(0)}{F_n}\sim\frac{3}{\sqrt{2\pi\sigma^2 n}}.
\]
Consequently, **almost every square-flat coloring is eventually active**, although its typical CCA activity goes to zero, and
\[
\sqrt n\,\alpha_{\rm CCA}\Longrightarrow|\mathcal N(0,\sigma^2)|,
\qquad
\sqrt n\,\alpha_{\rm GHM}\Longrightarrow\frac13|\mathcal N(0,\sigma^2)|.
\]

## Assumptions and scope

The graph is finite, simple, connected, and exactly the prism \(C_n\square K_2\), with \(n\ge3\). Edges join neighboring vertices within each rail and paired vertices across rungs. CCA advances a vertex from \(c\) to \(c+1\pmod3\) when some neighbor has the successor color, and otherwise leaves it unchanged. In GHM, states \(1\) and \(2\) advance unconditionally, while state \(0\) advances to \(1\) exactly if a neighboring state is \(1\). Every site has a well-defined eventual excitation frequency. All probabilities and distributional statements here are **conditional on square-flatness** under independent uniform initial colors; they do not concern unconditional initial data. The fixed labels of both rails and all rungs matter to the population counts.

## Proof

**1. Flatness and the surviving topological winding.** Regard \(\delta\) as an antisymmetric integer edge form. The elementary square boundaries together with one upper-rail cycle generate the graph's integer cycle space (the \(n\) square boundaries are independent). On a square-flat coloring, all closed-walk integrals are integer multiples of the single upper-rail integral \(H_n\). A closed walk with longitudinal winding number \(w\) has integral \(wH_n\) and length at least \(n|w|\): each horizontal edge moves the column by at most one in the lifted infinite strip. The upper rail realizes \(|H_n|/n\). The general finite-graph activity theorem in [1, Theorem 3] therefore yields the CCA rate \(|H_n|/n\).

For GHM the oriented edge form \(\delta_{\rm GHM}\) equals \(1\) on \(0\to1\), \(-1\) on \(1\to0\), and \(0\) otherwise. Setting \(f(0)=0,f(1)=-2,f(2)=-1\), direct inspection of all color pairs gives
\[
\delta(a,b)=3\delta_{\rm GHM}(a,b)+f(b)-f(a).
\]
The two forms have closed-walk integrals in exact ratio three, proving the GHM rate. Since the sum around any closed rail is congruent to zero modulo three, \(H_n\in3\mathbb Z\). For existence of nonzero winding at any \(n\ge3\), assign the same color to both vertices of each rung and make the first three successive upper-rail steps \(+1\) and the remaining steps \(0\), resulting in \(H_n=3\).

**2. Exact finite-size transfer.** Write the coloring of rung \(i\) as \((a_i,b_i)\). The square with adjacent rung \((c,d)\) has signed sum \(\delta(a,c)+\delta(c,d)-\delta(b,d)-\delta(a,b)\). Thus permissible successive rungs are exactly the nonzero entries of \(T(1)\), with upper-rail winding increment \(\delta(a,c)\). Closing after \(n\) rungs counts each labelled square-flat coloring once, proving the coefficient formula. Direct exact determinant expansion of the explicit \(9\times9\) integer matrix gives
\[
\det(xI-T(1))=(x-2)^3(x+1)^4(x^2-7x+4).
\]
Taking the trace of the \(n\)-th power proves the stated formula for \(F_n\). The stand-alone exact-arithmetic checker verifies the determinant identity without numerical eigensolvers.

**3. The twisted Perron root and its variance.** The matrix \(T(1)\) is primitive; in fact \(T(1)^2\) is entrywise positive. The simultaneous color shift \((a,b)\mapsto(a+1,b+1)\) commutes with \(T(e^s)\). On shift-invariant vectors, the weighted transfer reduces to the positive \(3\times3\) matrix
\[
B(z)=\begin{pmatrix}
z+1+z^{-1}&1+z^{-1}&1+z\\
z+1&z+1+z^{-1}&z\\
1+z^{-1}&z^{-1}&z+1+z^{-1}
\end{pmatrix},\qquad z=e^s.
\]
Its characteristic polynomial has a factor \(x-z-z^{-1}\) and a quadratic factor
\[
x^2-(3+4\cosh s)x+(2\cosh 2s+2\cosh s).
\]
The Perron root \(\lambda(s)\) near \(s=0\) is the larger root of this quadratic. It obeys \(\lambda(0)=\lambda_+\), \(\lambda'(0)=0\), and
\[
\lambda''(0)=2+\frac4{\sqrt{33}},\qquad
\left.\frac{d^2}{ds^2}\log\lambda(s)\right|_{s=0}
=\frac{2+4/\sqrt{33}}{\lambda_+}=\sigma^2>0.
\]
Because all other eigenvalues of \(T(1)\) have smaller modulus, the winding characteristic functions satisfy
\[
\mathbb E[e^{itH_n/\sqrt n}\mid\text{square-flat}]
=\frac{\operatorname{tr}(T(e^{it/\sqrt n})^n)}{F_n}
\longrightarrow e^{-\sigma^2t^2/2}.
\]
This proves the central limit theorem.

**4. The lattice local limit.** For real \(t\), the spectral radius of \(T(e^{it})\) cannot exceed \(\lambda_+\). Equality in the triangle inequality for a primitive nonnegative matrix forces all nonzero edge phases to be a diagonal gauge, up to a global phase. Every rung state has a zero-increment self-loop, making the global phase one. The directed three-step rung cycle \((0,0)\to(1,1)\to(2,2)\to(0,0)\) has total increment three, forcing \(e^{3it}=1\). Conversely, whenever \(e^{3it}=1\), every edge phase equals a ratio of the gauge factors \(e^{ita}\) and \(e^{itc}\), so equality holds. Thus the only maximum-radius Fourier points are the three cube roots of unity. Near each one, the principal eigenvalue has Gaussian modulus with the same variance \(\sigma^2\), and the rest of the Fourier integral is exponentially smaller. Fourier inversion at winding zero therefore gives
\[
N_n(0)=\frac1{2\pi}\int_{-\pi}^{\pi}\operatorname{tr}(T(e^{it})^n)\,dt
\sim\frac{3\lambda_+^n}{\sqrt{2\pi\sigma^2n}}.
\]
Dividing by \(F_n\sim\lambda_+^n\) proves the synchronization fraction. The activity distribution limits follow from step 1 and continuous mapping.

## Verification

All code is self-contained Python 3 using only the standard library. Run `python check_transfer.py`, `python check_dynamics.py`, and `python check_algebra.py` from the extracted package folder. `check_transfer.py` performs exact dynamic programming for \(3\le n\le12\), checking the characteristic-polynomial count and all permitted winding multiples. `check_dynamics.py` independently constructs the graphs and directly evolves both update rules to their eventual cycles, exhaustively testing the square-flat initial states for \(n=3,4\) against the predicted rational activity. `check_algebra.py` computes the exact characteristic polynomial with rational Faddeev--LeVerrier arithmetic and verifies the numerical variance identity. The programs print `TRANSFER_OK`, `DYNAMICS_OK`, and `ALGEBRA_OK`, respectively. The analytic Perron--Frobenius and Fourier arguments, not finite computations, establish the infinite-size statements.

## Relationship to prior work

The arbitrary-graph cycle-integral activity theorem, as well as the CCA/GHM dynamical definitions, come from Gravner, Lyu and Sivakoff [1]. The topological distinction between local height consistency and global winding in graph colorings is also part of the graph-recoloring context discussed in [2]. Neither of these inspected sources evaluates the square-flat cylindrical-prism winding census, the exact transfer spectrum \(\lambda_\pm\), the nontrivial variance \(\sigma^2\), or its local-limit synchronization probability. Earlier open-ladder excitation censuses concern a graph without the longitudinal cycle, while earlier prism results for initially primitive-three GHM orbits address a different invariant; those statements do not determine the conditional winding law here. The spectral and local-limit deductions use standard finite-state transfer-matrix arguments and are not claimed as new general machinery.

## Limitations

This theorem conditions on all elementary-square circulations being zero; it does not classify the activity rates or their populations for arbitrary prism colorings. It determines eventual excitation frequencies, not transient lengths, first periodic-entry times, or primitive temporal orbit populations. The result is supported by a mathematical proof and reproducibility checks, not by independent external assessment. A mathematically equivalent enumeration in little-indexed literature cannot be ruled out.

## References

[1] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first public October 24, 2016, Theorem 3 and Sections 2--4. https://arxiv.org/abs/1610.07320

[2] D. Eppstein, *Reconfiguring 3-colorings*, November 25, 2019, discussion of height functions and winding obstructions. https://11011110.github.io/blog/2019/11/25/reconfiguring-3-colorings.html
