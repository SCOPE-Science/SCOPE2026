# Sharp fixed-vertex rarity and conditional Gaussian geometry of signed involutions on binary cubes

## Finding

Let \(B_n=C_2^n\rtimes S_n\) act in the standard way on the binary cube \(Q_n=\mathbb F_2^n\). Let \(D_n\) be the subgroup of even signed permutations, and let \(I_n^G=\{g\in G:g^2=1\}\), including the identity. For \(t\ge0\) set
\[
A_n(t)=n![z^n]\exp(tz+z^2)=n!\sum_{k=0}^{\lfloor n/2\rfloor}\frac{t^{n-2k}}{k!(n-2k)!}.
\]
For every \(n\ge4\), exactly \(A_n(1)\) involutions in **each** of \(B_n\) and \(D_n\) fix a cube vertex, whereas
\[
|I_n^B|=A_n(2),\qquad |I_n^D|=\frac{A_n(2)+A_n(0)}2.
\]
For \(0\le k\le\lfloor n/2\rfloor\), precisely \(n!/(k!(n-2k)!)\) involutions in either group fix exactly \(2^{n-k}\) cube vertices; every other involution fixes none. These exact counts use previously known classifications, and are included to specify the distribution, not asserted to be novel individually.

The sharp new asymptotic comparison is
\[
\frac{|\{g\in I_n^B:\operatorname{Fix}_{Q_n}(g)\ne\varnothing\}|}{|I_n^B|}
=e^{3/8-\sqrt{n/2}}\left(1+O(n^{-1/2})\right),
\]
\[
\frac{|\{g\in I_n^D:\operatorname{Fix}_{Q_n}(g)\ne\varnothing\}|}{|I_n^D|}
=2e^{3/8-\sqrt{n/2}}\left(1+O(n^{-1/2})\right).
\]
Furthermore, sample uniformly from the involutions fixing at least one cube vertex (the conditional law is identical for \(B_n\) and \(D_n\)), and set \(L_n=\log_2|\operatorname{Fix}_{Q_n}(g)|\). Then
\[
\frac{2L_n-n-\sqrt{n/2}}{(n/2)^{1/4}}\ \xrightarrow{\ d\ }\ N(0,1).
\]
In particular the conditional fixed affine subspace has dimension \(n/2+\sqrt{n/2}/2+O_{\mathsf P}(n^{1/4})\). These asymptotic statements, not Chen's earlier exact fixed-vertex criterion, are the subject of the originality assessment.

## Assumptions and scope

The group action is the standard affine coordinate action, \((\pi,b)\cdot x=y\), with \(y_i=x_{\pi^{-1}(i)}+b_i\) in \(\mathbb F_2\). The element is involutive if \(\pi^2=1\) and \(b_i=b_{\pi(i)}\). Membership in \(D_n\) means \(\sum_i b_i=0\) in \(\mathbb F_2\). The full group element counts include the identity. All fixed points are **cube vertices**, not fixed signed letters or Euclidean points. The asymptotic is over integer \(n\to\infty\); neither parity of \(n\) is excluded. The Gaussian is standard with mean zero and variance one.

## Proof

**(1) Exact spectrum.** Write an involution \(\pi\in S_n\) with \(k\) transpositions and \(f=n-2k\) singleton cycles. There are \(n!/(2^k k!f!)\) such \(\pi\). For \((\pi,b)^2=1\), the sign vector is constant on each orbit of \(\pi\), giving \(2^{k+f}\) choices. A fixed cube vertex must satisfy the coordinate equations. The equations on a transposed pair are consistent for either common sign and give one freely chosen bit; those on singleton coordinates force their signs to be zero and leave one free bit each. Thus, exactly \(2^k\) sign choices give vertex fixation and each fixes \(2^{k+f}=2^{n-k}\) vertices. Each such vector has even total sign, so every cube-fixing involution belongs to \(D_n\). Multiplying by the count of \(\pi\) gives \(n!/(k!f!)\), and summation gives \(A_n(1)\) in either group. Summing all \(2^{k+f}\) sign choices gives \(A_n(2)\) in \(B_n\). Among the sign choices, those with even total sign are half if \(f>0\); for \(f=0\) all choices are even. The parity correction is precisely \(A_n(0)/2\), giving the formula for \(D_n\).

**(2) Uniform coefficient estimate.** Put \(c_n(t)=[z^n]\exp(tz+z^2)\) and for fixed \(t\) in a compact interval of positive reals let \(r_t>0\) solve \(tr_t+2r_t^2=n\), so
\[
r_t=\sqrt{n/2}-t/4+O(n^{-1/2}),\qquad v_t=tr_t+4r_t^2=2n-tr_t.
\]
The following estimate is uniform on any fixed compact positive \(t\)-interval:
\[
c_n(t)=\frac{\exp(tr_t+r_t^2)}{r_t^n\sqrt{2\pi v_t}}\left(1+O(n^{-1/2})\right).
\]
For completeness, take independent Poisson variables \(U\) and \(V\) with means \(tr_t\) and \(r_t^2\). Their weighted sum \(U+2V\) has mean \(n\), variance \(v_t\), and \(\Pr(U+2V=n)=c_n(t)r_t^n\exp(-tr_t-r_t^2)\). Fourier inversion integrates \(\exp(tr_t(e^{i\theta}-1)+r_t^2(e^{2i\theta}-1)-in\theta)\). On a neighborhood of zero of width \(n^{-2/5}\), quadratic expansion and integration give \((2\pi v_t)^{-1/2}(1+O(n^{-1/2}))\); the cubic term is odd to leading order. Away from neighborhoods of both zero and \(\pi\), \(\Re(r_t^2(e^{2i\theta}-1))\le-c n^{1/5}\). The neighborhood of \(\pi\) has modulus bounded by \(e^{-2tr_t}\) times a Gaussian integral, hence is exponentially smaller. Uniform positive bounds on \(t\) control these estimates. This establishes the stated relative error.

**(3) Rare-event constant.** Define \(\Phi_n(t)=tr_t+r_t^2-n\log r_t\). Stationarity at \(r_t\) gives \(\Phi_n'(t)=r_t\). Therefore
\[
\Phi_n(2)-\Phi_n(1)=\int_1^2r_t\,dt=\sqrt{n/2}-3/8+O(n^{-1/2}).
\]
Since \(v_t=2n-tr_t\), the ratio of square-root variance prefactors for \(t=1,2\) is \(1+O(n^{-1/2})\). The estimate in (2) yields
\[
\frac{A_n(1)}{A_n(2)}=\exp(3/8-\sqrt{n/2})(1+O(n^{-1/2})).
\]
For odd \(n\), \(A_n(0)=0\). For even \(n\), \(A_n(0)=n!/(n/2)!\), and the same Fourier argument at \(t=0\), accounting for two equal saddle peaks at \(0,\pi\), gives \(A_n(0)/A_n(2)=O(e^{-2\sqrt{n/2}+O(1)})\). Thus \((A_n(2)+A_n(0))/2=(A_n(2)/2)(1+o(n^{-1/2}))\), proving both constants.

**(4) Conditional Gaussian fixed-space dimension.** In the conditional vertex-fixing population let \(F_n\) be the number of singleton cycles of the underlying \(\pi\). By (1),
\[
\mathbb E e^{sF_n}=\frac{A_n(e^s)}{A_n(1)},\qquad L_n=(n+F_n)/2.
\]
For \(s\) in a fixed real neighborhood of zero the uniform estimate in (2), together with \(\Phi_n'(t)=r_t\), gives
\[
\log\mathbb E e^{sF_n}=\sqrt{n/2}(e^s-1)-\frac18(e^{2s}-1)+O(n^{-1/2}).
\]
With \(R=\sqrt{n/2}\) and \(s=u/\sqrt R\), subtract \(u\sqrt R\). The resulting cumulant-generating function converges to \(u^2/2\) for each fixed real \(u\), giving \((F_n-R)/\sqrt R\Rightarrow N(0,1)\) by the moment-generating-function continuity theorem. The displayed normalization for \(L_n\) is algebraically identical.

## Verification

The accompanying standalone `verify.py` independently constructs every signed involution in dimensions \(1\) through \(6\), applies it to every cube vertex and checks the exact group totals, zero/positive fixed-vertex partition, and every positive fixed-point multiplicity. It then checks the coefficient recurrence and the convergence of the leading asymptotic constant numerically through dimension \(1000\). Finite computations are independent checks of the exact combinatorial argument; the infinite limit is established by the analytic estimates in the proof, not by the experiments.

For example, in dimension \(6\) there are \(1384\) involutions in \(B_6\), \(752\) in \(D_6\), and exactly \(331\) vertex-fixing involutions in both. The latter have fixed-vertex counts \(8,16,32,64\) with respective multiplicities \(120,180,30,1\).

## Relationship to prior work

Chen's analysis of induced cycle structures, including his Proposition 3.5 attributed to Chen and Stanley, already establishes the **general** criterion for cube-vertex fixation by arbitrary signed permutations. Consequently, neither that criterion nor its restriction to involutions is claimed new. Gutierres, Mamede and Santos (first posted 2024) give the standard type-B and type-D involution recurrences, which agree with the present exact denominators. Arumugam, Dietrich and Glasby's 2022 paper studies fixed-point/derangement proportions in wreath-product actions for uniform unrestricted elements, not uniform involutions of these Coxeter groups. The contribution assessed here is the combined **sharp conditional stretched-exponential rate with its constant, the type-D factor-two effect, and the conditional Gaussian fixed-affine-subspace-dimension law**; a full bibliographic priority claim is not made.

## Limitations

The assertions concern the binary vertex action, not the signed-letter action, and the uniform distribution over involutive elements including identity. The asymptotic constants change under other probability models. No convergence rate is claimed for the Gaussian limit beyond what is implicit in the displayed generating-function argument. Previous literature may contain the conditional asymptotic in another vocabulary; historical novelty remains subject to external checking. No independent audit has been performed.

## References

- W. Y. C. Chen, *Induced Cycle Structures of the Hyperoctahedral Group*, early proceedings text (1992), Proposition 3.5; https://fpsac-archive.github.io/FPSAC92/POSTERS/Chen_proc.pdf . Journal version DOI: 10.1137/0406028.
- J. Arumugam, H. Dietrich and S. P. Glasby, *Derangements in wreath products of permutation groups*, arXiv:2207.01215, first posted 2022-07-04; https://arxiv.org/abs/2207.01215 .
- G. Gutierres, R. Mamede and J. L. Santos, *Hamilton cycles for involutions of classical types*, arXiv:2401.12839, first posted 2024-01-23; https://arxiv.org/abs/2401.12839 .
