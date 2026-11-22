# A saturated-hub law and a square-root Kemeny penalty on wheel networks

## Finding

Let \(W_{m+1}=K_1\vee C_m\), where \(m\ge3\). Among **all** irreducible symmetric stochastic matrices supported off diagonal on the wheel edges, with nonnegative self-loop probabilities allowed, the unique minimizer of the non-return Kemeny constant
\[
\mathcal K(P)=\operatorname{tr}\!\left[(I-P+J/(m+1))^{-1}\right]-1
\]
assigns probability \(1/m\) to every hub–rim edge and probability \((m-1)/(2m)\) to every rim edge. Its hub and rim self-loops are zero. This is unrestricted optimality, not optimality only among rotationally symmetric candidates.

The exact minimum is, with \(q_m=1-1/m\), \(\delta_m=\sqrt{1-q_m^2}\) and \(\rho_m=q_m/(1+\delta_m)\),
\[
\mathcal K_m^*=\frac{m}{m+1}+\frac{m}{\delta_m}\frac{1+\rho_m^m}{1-\rho_m^m}-m.
\]
In particular,
\[
\boxed{\mathcal K_m^*\sim\frac{m^{3/2}}{\sqrt2}.}
\]

In contrast, the standard symmetric maximum-degree transition rule assigns \(1/m\) to *every* wheel edge, leaving holding probability \(1-3/m\) at each rim vertex. Put \(\lambda=(3-\sqrt5)/2\). Its Kemeny constant is
\[
\mathcal K_m^{\mathrm{md}}=\frac m{m+1}+\frac{m^2}{\sqrt5}\frac{1+\lambda^m}{1-\lambda^m}-m,
\]
so the exact asymptotic multiplicative inefficiency is
\[
\boxed{\lim_{m\to\infty}\frac{\mathcal K_m^{\mathrm{md}}/\mathcal K_m^*}{\sqrt m}=\sqrt{\frac25}.}
\]
The unique optimum has a positive rim edge weight even at the smallest wheel, while the hub row is saturated for **every** \(m\ge3\).

## Assumptions and scope

The vertex set comprises one hub \(h\) and rim vertices labelled cyclically by \(0,\ldots,m-1\). The only permitted positive off-diagonal transitions are along the \(m\) hub–rim spokes and the \(m\) rim edges. A feasible \(P\) must be symmetric, entrywise nonnegative and row-stochastic, with irreducible underlying positive-transition graph. Holding probabilities \(P_{ii}\ge0\) are allowed. Thus every admissible walk has the uniform stationary law; varying the stationary law is outside scope. Here \(J=\mathbf1\mathbf1^{\mathsf T}\) is the all-ones matrix. The Kemeny convention excludes the return-time contribution; adding the usual constant one to every value changes no optimum and no asymptotic conclusion.

## Proof

**1. Unrestricted global uniqueness and symmetry.** Set \(N=m+1\) and \(A(P)=I-P+J/N\). For every admissible irreducible symmetric \(P\), \(A(P)\) is symmetric positive definite, with eigenvalue one on constants and eigenvalues \(1-\lambda_j(P)>0\) on their orthogonal complement. Hence \(\mathcal K(P)=\operatorname{tr}A(P)^{-1}-1\). On a nonzero symmetric perturbation \(E\) with \(E\mathbf1=0\), direct differentiation gives
\[
\frac{d^2}{dt^2}\operatorname{tr}(A-tE)^{-1}
=2\operatorname{tr}[(A-tE)^{-1}E(A-tE)^{-1}E(A-tE)^{-1}]>0.
\]
Indeed the last trace is the squared Frobenius norm of \((A-tE)^{-1/2}E(A-tE)^{-1}\), multiplied by two. Thus the Kemeny objective is **strictly** convex in the full space of symmetric stochastic transition matrices with connected support. Taking the average of any feasible matrix over cyclic rotations leaves it feasible; strict convexity shows that a minimizer must be rotationally invariant, and two distinct minimizers cannot coexist. Existence follows from compactness of the nonnegative stochastic polytope together with the divergence of the inverse trace when the positive-transition graph becomes disconnected. A feasible interior irreducible matrix exists.

**2. Exact invariant spectrum.** An invariant walk has common spoke probability \(b>0\), common rim-edge probability \(a\ge0\), hub hold \(1-mb\) and rim hold \(1-b-2a\). Therefore
\[
0<b\le\frac1m,\qquad 0\le a\le\frac{1-b}{2}.
\]
Its nonzero Laplacian eigenvalues are \((m+1)b\), from the two-dimensional constant-rim/hub sector, and
\[
 b+2a\bigl(1-\cos(2\pi k/m)\bigr),\quad 1\le k<m,
\]
from the orthogonal rim Fourier modes. Consequently,
\[
\mathcal K(b,a)=\frac1{(m+1)b}+
\sum_{k=1}^{m-1}\frac1{b+2a(1-\cos(2\pi k/m))}.
\]
For every fixed \(b>0\), every summand decreases strictly as \(a\) increases; hence \(a=(1-b)/2\), and every rim holding probability vanishes.

**3. Saturation of all spokes.** Write \(c_k=\cos(2\pi k/m)\) and \(f(b)=\mathcal K(b,(1-b)/2)\). Then
\[
f'(b)=-\frac1{(m+1)b^2}-\sum_{k=1}^{m-1}\frac{c_k}{[1-(1-b)c_k]^2}.
\]
For \(0<b\le1/m\), \(1-b\ge0\). If \(c_k<0\), the denominator is at least one and \(c_k/[1-(1-b)c_k]^2\ge-1\); if \(c_k\ge0\), the term is nonnegative. Thus
\[
f'(b)\le-\frac1{(m+1)b^2}+(m-1)
\le-\frac{m^2}{m+1}+m-1=-\frac1{m+1}<0.
\]
The unique feasible minimum occurs at the maximal spoke probability \(b=1/m\). Both hub and rim hold probabilities therefore vanish, proving the claimed optimizer in the **full** original problem.

**4. Exact value.** At the optimum the Fourier denominators are \(1-q_m\cos(2\pi k/m)\), with \(q_m=1-1/m\in(0,1)\). For any \(0<q<1\), let \(\delta=\sqrt{1-q^2}\) and \(\rho=q/(1+\delta)\). The convergent Poisson-kernel expansion
\[
\frac1{1-q\cos\theta}=\frac1\delta\left(1+2\sum_{j\ge1}\rho^j\cos(j\theta)\right)
\]
gives the exact finite root-of-unity sum
\[
\sum_{k=0}^{m-1}\frac1{1-q\cos(2\pi k/m)}
=\frac m\delta\frac{1+\rho^m}{1-\rho^m}.
\]
Removing the \(k=0\) term \(1/(1-q_m)=m\) and adding the hub–rim eigenvalue's contribution \(m/(m+1)\) proves the minimum formula. Similarly, for the maximum-degree walk the nonradial eigenvalues of \(I-P\) are \((3-2\cos(2\pi k/m))/m\). The same sum with \(q=2/3\) yields its exact displayed value.

**5. Asymptotics.** We have \(\delta_m=\sqrt{2m-1}/m\) and \(\rho_m^m=\exp(-\sqrt{2m}+O(1))\to0\). Therefore
\[
\mathcal K_m^*=\frac{m^2}{\sqrt{2m-1}}(1+o(1))-m+O(1)
\sim\frac{m^{3/2}}{\sqrt2}.
\]
Since \(0<\lambda<1\), \(\lambda^m\to0\) and \(\mathcal K_m^{\mathrm{md}}\sim m^2/\sqrt5\). Taking the ratio gives \(\sqrt{2/5}\sqrt m\).

## Verification

The companion standalone `verify_wheel.py` uses only the Python standard library. It forms exact rational stochastic matrices, inverts the complete rank-corrected Laplacian by fraction-preserving Gaussian elimination, and compares it against independently evaluated finite Fourier formulas. For all \(3\le m\le12\), it checks the optimal candidate against rationally perturbed admissible spoke and rim allocations and the maximum-degree chain, including the \(m=3\) equality case. It also spot-checks four larger sizes against the predicted scaling. It passes 138 assertions. These finite checks are corroboration only: unrestricted uniqueness and the all-size statements rest on the proof above, not enumeration.

Run from the directory containing the file: `python3 verify_wheel.py`. No third-party packages or data files are needed.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced symmetric stochastic graph-constrained design and the maximum-degree comparator for **SLEM**, not Kemeny's inverse-trace objective. Patel, Agharkar and Bullo (2014/2015) established the general convex formulation for reversible Kemeny optimization, but their inspected presentation does not give the wheel optimizer or its exact scaling. Zhang and collaborators (2012) study Kemeny constants of **fixed degree-normalized random walks on variable network topologies** rather than optimization over symmetric transition matrices on a fixed wheel.

Separate work on Kirchhoff-index-optimal *conductance-budgeted wheels* gives a rotational spectrum and sharp rim-price thresholds. Its constraint is a **global edge-price budget**, not the per-vertex stochastic row capacities here; those optima therefore do not imply the saturated hub row, the maximum-degree Kemeny gap, or the stated optimizer. The present claim concerns the fixed graph with a prescribed uniform stationary distribution and vertexwise stochastic constraints. The wheel Fourier diagonalization and generic convexity are treated as established methods rather than new principles.

## Limitations

The result applies to uniform-stationary symmetric walks on unweighted wheel **support**. It does not optimize general nonreversible walks, prescribe a nonuniform stationary distribution, or address graph-conductance budgets, fastest mixing, or arbitrary graph families. The maximum-degree comparison is asymptotic; no universal finite-size numerical speedup factor is claimed beyond the exact formulas. Bibliographic search and inspection cannot establish absolute publication priority, particularly against unindexed special cases of reversible-chain or resistance optimization. Independent expert validation has not been performed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689, DOI: 10.1137/S0036144503423264, first published October 29, 2004. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. R. Patel, P. Agharkar and F. Bullo, “Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant,” *IEEE Transactions on Automatic Control* 60 (2015), 3156–3167, DOI: 10.1109/TAC.2015.2426317. Author's copy: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf .
3. Z. Zhang, Y. Sheng, Z. Hu and G. Chen, “Optimal and suboptimal networks for efficient navigation measured by mean-first passage time of random walks,” arXiv:1211.4295, initially public November 19, 2012. https://arxiv.org/abs/1211.4295 .
4. “A sharp rim-price transition and critical window for resistance-optimized wheels,” research record, October 13, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-rim-price-transition-and-critical-window-for-resistance--c2f59dd7b8a5 .
