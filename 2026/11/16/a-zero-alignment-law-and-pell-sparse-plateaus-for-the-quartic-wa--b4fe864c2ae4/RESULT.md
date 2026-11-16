# A zero-alignment law and Pell-sparse plateaus for the quartic Walsh projection

## Finding
For every integer \(n\ge4\), let \(\Pi_{4,n}\) be the homogeneous degree-four Fourier–Walsh projector on functions on \(\{-1,1\}^n\), and let
\[
L_4(n)=\|\Pi_{4,n}\|_{L^\infty\to L^\infty}=\|\Pi_{4,n}\|_{L^1\to L^1}.
\]
The norm is nondecreasing in dimension. Its **exact** increment is supported only on the two positive sign-change intervals of the quartic Krawtchouk kernel, with the formula below. Moreover, a plateau \(L_4(N)=L_4(N-1)\), \(N\ge5\), occurs if and only if all four real roots of the quartic Krawtchouk kernel at dimension \(N\) lie on its parity lattice. In particular, all possible plateau dimensions belong to two explicit Pell recurrences, so
\[
\#\{4\le n\le X:L_4(n+1)=L_4(n)\}=O(\log X).
\]
One plateau occurs at \(n=7\), where \(L_4(7)=L_4(8)=35/8\). An exact-integer certificate checks that this is the only plateau with \(n+1\le10^{100}\); this finite verification is not asserted to classify all larger dimensions.

For precise evaluation, write
\[
P_N(t)=\frac{t^4-(6N-8)t^2+3N(N-2)}{24},\qquad
Q_N=6N^2-18N+16,
\]
\[
\rho_-=\sqrt{3N-4-\sqrt{Q_N}},\qquad
\rho_+=\sqrt{3N-4+\sqrt{Q_N}},
\]
and \(\mathcal G_N=\{-N,-N+2,\ldots,N\}\). For each \(\rho_j\) not belonging to \(\mathcal G_N\), let \(v_j\in\mathcal G_N\) be uniquely determined by \(v_j<\rho_j<v_j+2\). Then the **two-binomial increment law** is
\[
\boxed{\displaystyle
L_4(N)-L_4(N-1)=2^{2-N}\!
\sum_{\substack{j\in\{-,+\}\\\rho_j\notin\mathcal G_N}}
\binom{N-1}{(N+v_j)/2}
\min\bigl(|P_N(v_j)|,|P_N(v_j+2)|\bigr).}
\]
Empty sums equal zero. All terms are nonnegative, and every included term is strictly positive.

Equivalently, let \(D_N=\sqrt{24N^2-72N+64}\). The plateau criterion is the entirely arithmetic condition that \(D_N\) be integral and that both
\[
\frac{6N-8-D_N}{2},\qquad\frac{6N-8+D_N}{2}
\]
be perfect squares whose nonnegative square roots have the same parity as \(N\). Every possible plateau parameter \(N\) therefore satisfies
\[
z^2-6m^2=10,\qquad m=2N-3>0.
\]
The positive solutions of this Pell-type equation come from exactly two seeds \((z,m)=(4,1)\) and \((8,3)\) under
\[
(z,m)\longmapsto(5z+12m,\ 2z+5m).
\]
Possible \(N\) start at \(8,17,66,155,640,1521,6322,15043,\ldots\); only those additionally satisfying the perfect-square and parity test are plateaus.

## Assumptions and scope
All spaces carry uniform probability measure. The projection retains exactly the Walsh characters \(\chi_I(x)=\prod_{i\in I}x_i\) for \(|I|=4\); no lower degrees are included. The result concerns the canonical Fourier projection, including complex-valued inputs, and its operator norm. It is not a claim about arbitrary projections onto the same subspace. The increment formula and zero-alignment equivalence hold for every integer \(N\ge5\). No assumption is made that all Pell candidates attain equality.

## Proof
**1. Exact endpoint norm and one-coordinate recursion.** For \(d\ge0\) and \(n\ge d\), define the Walsh kernel
\[
K_{d,n}(x)=\sum_{|I|=d}\prod_{i\in I}x_i.
\]
Convolution by this kernel is the Fourier projection, so its \(L^\infty\)-norm is its \(L^1\)-norm, \(\mathbb E|K_{d,n}|\); finite-group convolution achieves the norm by the sign of the kernel. Duality gives the same \(L^1\)-operator norm. For an additional independent Rademacher sign \(\varepsilon\),
\[
K_{d,n+1}(x,\varepsilon)=K_{d,n}(x)+\varepsilon K_{d-1,n}(x).
\]
For real \(A,B\), \((|A+B|+|A-B|)/2=\max(|A|,|B|)\). Hence
\[
L_d(n+1)-L_d(n)=\mathbb E\bigl(|K_{d-1,n}|-|K_{d,n}|\bigr)_+\ge0.
\]
This identity also proves monotonicity for the quartic degree.

**2. Sign-change identity.** Put \(U=A+B\), \(V=A-B\). A direct check of the two sign cases shows
\[
(|B|-|A|)_+=\mathbf1_{\{UV<0\}}\min(|U|,|V|).
\]
For a sign vector with coordinate sum \(s\), its two extensions have sums \(s+1\) and \(s-1\). The sum \(s\) has probability \(2^{-n}\binom n{(n+s)/2}\). Therefore, for every degree \(d\), the increment is an exact binomial-weighted sum over neighboring, oppositely signed samples of the \((n+1)\)-dimensional Krawtchouk kernel. No numerical approximation enters.

**3. Quartic roots and their separation.** Expanding the fourth elementary symmetric function in the signs gives \(K_{4,N}(x)=P_N(s)\) at \(s=\sum_i x_i\). The four roots are \(-\rho_+,-\rho_-,\rho_-,\rho_+\). For every \(N\ge5\), elementary squaring verifies
\[
1<\rho_-<\rho_+<N,\qquad \rho_+-\rho_->2.
\]
Indeed, \((3N-5)^2-Q_N=3(N-1)(N-3)>0\), \((N^2-3N+4)^2-Q_N=N(N-1)(N-2)(N-3)>0\), and
\[
(\rho_+-\rho_-)^2=6N-8-2\sqrt{3N(N-2)}>4
\]
because \((3N-6)^2-3N(N-2)=6(N-2)(N-3)>0\). Also \(2\rho_->2\). Hence each simple root lies in a distinct length-two interval between consecutive nodes of \(\mathcal G_N\), unless it is itself a node. When a root is between nodes, the endpoint values have opposite nonzero signs. When it is a node, neither neighboring edge changes sign across that zero. Exactly four edges, or fewer when some roots align, can contribute; symmetry pairs the positive and negative roots, and the binomial weights agree. The displayed two-binomial formula follows, as does the equivalence between a plateau and alignment of **all four** roots.

**4. Pell reduction.** If both positive roots belong to \(\mathcal G_N\), their squares are integers, and the discriminant of the quadratic equation for \(t^2\) is an integer square:
\[
D_N^2=(6N-8)^2-12N(N-2)=6(2N-3)^2+10.
\]
Conversely, an integral \(D_N\), together with the two perfect-square and parity conditions in the finding, puts all four roots on \(\mathcal G_N\), proving the arithmetic test.

For completeness, every positive integral solution of \(z^2-6m^2=10\) has \(m\) odd and \(z\) even. For \(m\ge7\), the inverse transformation
\[
(z,m)\mapsto(5z-12m,\ 5m-2z)
\]
has positive integer coordinates, preserves the equation, and decreases \(m\): positivity of the new second coordinate follows from \(m^2>40\), and positivity of the first from \(5\sqrt6>12\). Repeated descent reaches \(m\in\{1,3,5\}\). The only positive solutions there are \((z,m)=(4,1),(8,3)\). In the forward direction, each step multiplies \(z+m\sqrt6\) by \(5+2\sqrt6\), so \(m\) grows geometrically. Thus at most \(O(\log X)\) possible \(N\le X+1\) satisfy the necessary Pell equation. Finally, at \(N=8\), \(P_8(t)=(t^2-4)(t^2-36)/24\) has all its roots on \(\mathcal G_8\), and direct binomial summation gives \(L_4(7)=L_4(8)=35/8\).

## Verification
Execute `python3 verify_quartic.py` with the Python standard library. The checker constructs the quartic Krawtchouk kernel independently from combinatorial binomial coefficients, compares the exact polynomial formula on every parity node, verifies the weighted sign-change identity and arithmetic plateau criterion for all dimensions \(4\le n\le300\), and uses exact integer square roots to examine both Pell recurrences for every candidate \(N\le10^{100}\). Its expected conclusion is `QUARTIC_WALSH_INCREMENT_PASS`; the finite cutoff yields only \(n=7\). The proof of the all-dimensional formula, equivalence, and logarithmic bound does not rely on that finite run.

## Relationship to prior work
Defant, Galicer, Mansilla, Mastyło and Muro (arXiv:2208.06467, Chapter 8, and their arXiv:2302.00233, Sections 3–4) establish the general Fourier–Walsh projection-kernel expectation formula and fixed-degree asymptotics. Those identities are used here and are **not** claimed as new. Their treatment of the quartic Hermite limit does not provide this exact consecutive-dimension increment, the four-zero plateau characterization, or the Pell sparsity law. Chihara and Stanton's *Zeros of Generalized Krawtchouk Polynomials* (Sections 2–4) studies integral zeros and their arithmetic significance; it provides known zero-theoretic background, but not these endpoint projection-norm comparison statements. The classification of individual integral zeros is more difficult than this exact plateau test; no unrestricted uniqueness of \(n=7\) is claimed. The literature on the cubic Walsh norm treats a different homogeneous degree and does not imply the quartic results.

## Limitations
The logarithmic estimate bounds **possible** quartic norm plateaus rather than proving that infinitely many occur. Apart from the explicitly certified range, the problem of eliminating further Pell candidates is not settled here. The finite computation through \(10^{100}\) does not constitute an infinite proof. No claims are made for spectral bands containing several degrees, for norms other than these two endpoints, or for arbitrary Fourier projectors. Bibliographic priority remains subject to specialists identifying equivalent results under alternative Krawtchouk or projection-constant terminology.

## References
- A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467 (first posted 2022-08-12), Chapter 8. https://arxiv.org/abs/2208.06467
- A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233 (first posted 2023-02-01), Sections 3–4. https://arxiv.org/abs/2302.00233
- L. Chihara and D. Stanton, *Zeros of generalized Krawtchouk polynomials*, Sections 2–4. https://www-users.cse.umn.edu/~stant001/PAPERS/krlaur.pdf
- I. Krasikov and S. Litsyn, *On integral zeros of Krawtchouk polynomials*, J. Combin. Theory Ser. A 74 (1996), 71–99, DOI:10.1006/jcta.1996.0038. (Bibliographic record and abstract consulted; complete text not inspected.)
