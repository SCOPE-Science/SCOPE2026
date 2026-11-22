# Short-to-long horizon reversal and a one-sixth placement law for path shortcuts

## Finding

Let \(P_n\) be the unweighted path on the labelled vertices \(1,\ldots,n\). Exactly one previously absent edge \(e=\{a,b\}\) is added with unit conductance, leaving all original conductances unchanged. Denote the augmented combinatorial Laplacian by \(L_e\) and its heat trace by
\[
 H_e(t)=\operatorname{tr}(e^{-tL_e}),\qquad t>0.
\]
**Theorem.** For every integer \(n\ge9\):

1. The endpoint-closing link \(e_{\mathrm{cyc}}=\{1,n\}\) is the **unique** minimizer of \(H_e(t)\) over all nonedges for all sufficiently small positive \(t\).
2. The interior reflection-centered link \(e_\mathrm{in}=\{2,n-1\}\) strictly beats the endpoint-closing link for all sufficiently large \(t\). More precisely, with \(\Lambda_n=2-2\cos(2\pi/n)\),
\[
H_{e_\mathrm{in}}(t)-H_{e_\mathrm{cyc}}(t)
=-e^{-\Lambda_n t}+o(e^{-\Lambda_n t})\quad(t\to\infty).
\]
3. For each \(n\ge9\), at least one edge minimizes \(H_e(t)\) for **every sufficiently large** time (an eventual optimizer). Every such edge is reflection-centered and, writing it \(\{i_n+1,n-i_n\}\) with \(0\le i_n<\lfloor n/4\rfloor\), every sequence of eventual optimizers as \(n\to\infty\) satisfies
\[
\boxed{\frac{i_n}{n}\longrightarrow\frac16.}
\]
Thus horizon-dependent optimization selects the cycle closure initially but eventually selects a chord with two exterior tails, asymptotically one-sixth of the path length each. The one-sixth position is **not** asserted to optimize every finite time, and no explicit finite-\(n\) switching time is claimed.

## Assumptions and scope

All edges have conductance one, the Laplacian is the combinatorial (not degree-normalized) Laplacian, and the optimization is over exactly one nonedge of \(P_n\); there are \((n-1)(n-2)/2\) candidates. Time is measured with the generator \(-L_e\). The trace includes the single zero eigenvalue, whose contribution is one for all candidates. The proof gives global short- and eventual-long-time statements, with no restrictions on other candidate locations. In part 3, the large-\(n\) limit is taken **after** the eventual long-time optimum is defined separately for each finite \(n\); the two limits are not interchangeable without analysis.

## Proof

**1. Short-time strict uniqueness.** Every augmentation has \(n\) unit edges and hence \(\operatorname{tr}L_e=2n\). For any simple graph, \(\operatorname{tr}L^2=\sum_v d_v^2+2|E|\). If the new edge joins two vertices of original degrees \(d_a,d_b\), this gives
\[
\operatorname{tr}L_e^2=6n-4+2(d_a+d_b).
\]
The original path has exactly two degree-one vertices, so \(d_a+d_b=2\) occurs only for \(\{a,b\}=\{1,n\}\); every competing edge gives at least three. Consequently
\[
H_e(t)-H_{e_{\mathrm{cyc}}}(t)
=(d_a+d_b-2)t^2+O(t^3)>0
\]
for sufficiently small positive \(t\). A common sufficiently small interval exists because the candidate set is finite.

**2. Rank-one saturation and strict spectral-multiplicity splitting.** Let \(L_0=L(P_n)\), put \(\theta=2\pi/n\), \(\Lambda_n=2-2\cos\theta\), and use zero-based path labels temporarily. The exact eigenvalues of \(L_0\) are \(\lambda_k=2-2\cos(k\pi/n)\), \(0\le k<n\), so \(\lambda_2=\Lambda_n\). For any added edge vector \(b\), positive rank-one interlacing gives
\[
\lambda_1(L_0+bb^{\mathsf T})\le\lambda_2(L_0)=\Lambda_n,
\]
where \(\lambda_1\) denotes the first nonzero eigenvalue. The cycle \(C_n\), obtained by joining the endpoints, has \(\Lambda_n\) as a **double** first positive eigenvalue.

For the link \(\{2,n-1\}\), let \(b=e_1-e_{n-2}\) in zero-based indexing. Reversal symmetry separates the path into symmetric and antisymmetric eigenspaces. The new edge acts only on the antisymmetric subspace. The first positive symmetric eigenvalue remains \(\Lambda_n\) and is simple there. Restrict \(L_0-\Lambda_n I\) to the antisymmetric subspace, calling this invertible matrix \(A\). Its eigenvalues are the path's odd Fourier modes shifted by \(-\Lambda_n\), so it has exactly one negative eigenvalue, and all remaining eigenvalues are positive. Direct solution of the antisymmetric second-difference recurrence gives
\[
g=b^{\mathsf T}A^{-1}b=-\frac{\sin(3\theta)}{\sin\theta}
=1-4\cos^2\theta.
\]
For completeness, write \(y=A^{-1}b\), with \(\phi=3\theta/2\), \(c=-\sin\phi/\sin\theta\). On the left half of the path, its entries are \(y_0=c\cos(\theta/2)\), \(y_1=c\cos(3\theta/2)\), and \(y_j=c\cot\phi\sin((j+1/2)\theta)\) for \(j\ge1\) up to the center; extend to the right half antisymmetrically. The two formulas coincide at \(j=1\), satisfy the path recurrence away from the two sources, and produce residues \(+1,-1\) at the source vertices. Hence \(g=2y_1\) as displayed. This explicit recurrence proof does not require any numerical spectral approximation.

The Schur-complement inertia identity for a matrix with exactly one negative eigenvalue shows that \(A+bb^{\mathsf T}\) is positive definite precisely when \(1+g<0\); at \(1+g=0\) it is positive semidefinite and singular. Here
\[
1+g=2-4\cos^2(2\pi/n),
\]
which is negative for every \(n\ge9\), zero at \(n=8\), and positive for \(5\le n\le7\). Therefore the added-chord Laplacian has \(\Lambda_n\) as its **simple** first positive eigenvalue for \(n\ge9\), with all other positive eigenvalues strictly larger. Subtracting the spectral heat traces gives the claimed negative leading exponential, proving part 2.

**3. Exact finite-size restriction on eventual optimizers.** The candidate set is finite. Differences of two finite sums of real exponentials are either identically zero or eventually have a fixed sign, so the set of global minimizers stabilizes for sufficiently large \(t\). Any edge with spectral gap strictly below \(\Lambda_n\) loses at large time to \(e_\mathrm{in}\). Among gap-saturating edges, every edge whose \(\Lambda_n\) eigenvalue is multiple loses to \(e_\mathrm{in}\), which has multiplicity one. Among the remaining candidates, every eventual minimizer must maximize the *next* eigenvalue \(\nu_2(L_e)\) (the second positive eigenvalue, numbering positive eigenvalues from one), since their leading \(e^{-\Lambda_n t}\) terms agree. Equality of next eigenvalues can leave a tie to be resolved at higher orders, but cannot invalidate this necessary condition.

For clarity, gap saturation itself can be checked without relying on any prior specialized theorem. Let \(u_2(j)=\cos((j+1/2)\theta)\) be the symmetric path Fourier mode at \(\Lambda_n\). A rank-one shortcut attains the interlacing ceiling only if it is orthogonal to \(u_2\), since otherwise a combination of the first two positive path modes orthogonal to the edge vector has Rayleigh quotient below \(\Lambda_n\). Orthogonality forces the two endpoint indices to sum to \(n-1\) in zero-based indexing. For a centered edge \(b_i=e_i-e_{n-1-i}\), repeating the antisymmetric recurrence above with \(\phi=(i+1/2)\theta\) gives
\[
b_i^{\mathsf T}(L_0-\Lambda_n I)_{\mathrm{anti}}^{-1}b_i
=-\frac{\sin((2i+1)\theta)}{\sin\theta}.
\]
The inertia criterion therefore gives saturation exactly for the centered indices \(0\le i<\lfloor n/4\rfloor\) when the added weight is one. Every eventual optimizer belongs to this set. (This *spectral-gap-only* characterization was established previously; the present result concerns the distinct finite-time heat objective and the second-mode refinement.)

**4. Continuum limit of the second mode.** Let \(\mu_{n,i}\) be the smallest eigenvalue in the antisymmetric sector after inserting the centered edge at index \(i\). For every sequence \(i=i(n)\) with \(i/n\to\alpha\in[0,1/4]\),
\[
\boxed{n^2\mu_{n,i}\longrightarrow
q(\alpha):=\min\left\{\frac{\pi^2}{4\alpha^2},
\frac{\pi^2}{(1/2-\alpha)^2}\right\},}
\]
where the first term is interpreted as \(+\infty\) when \(\alpha=0\). Here is a variational justification including endpoints. Identify an antisymmetric discrete vector with its values on the left half, extend it linearly on grid points \((j+1/2)/n\) over \([0,1/2]\), hold it constant to the left boundary, and set it to zero at \(1/2\). The antisymmetric Rayleigh numerator is the path difference energy plus the chord term \(4|v_i|^2\). If its eigenvalue multiplied by \(n^2\) remains bounded, after normalizing the interpolants to unit \(L^2\) norm their one-dimensional \(H^1\) norms are bounded. The chord contribution gives \(n^2|v_i|^2=O(1)\) under the discrete unit-norm convention; consequently the value \(\sqrt{n}v_i\) of the continuum-normalized interpolant tends to zero. By compactness of bounded sets of \(H^1([0,1/2])\) in \(C^0\), every limit vanishes at \(\alpha\) and at \(1/2\), with a free (natural Neumann) condition at \(0\). Lower semicontinuity gives the lower bound by the first eigenvalue of the two intervals \([0,\alpha]\) (Neumann–Dirichlet) and \([\alpha,1/2]\) (Dirichlet–Dirichlet). Conversely, sample the piecewise-sine first eigenfunction of the cheaper interval, with the zero placed at the **actual chord vertex** \((i+1/2)/n\); its chord energy vanishes exactly and its normalized difference energy converges to that continuum eigenvalue. This proves the upper bound and hence the displayed limit for arbitrary sequences, including \(\alpha=0,1/4\).

The next symmetric eigenvalue after \(\Lambda_n\) is the path's even mode \(2-2\cos(4\pi/n)\), which after multiplication by \(n^2\) tends to \(16\pi^2\). Since \(q(\alpha)\le9\pi^2<16\pi^2\), the second positive eigenvalue of every gap-saturating chord obeys
\[
 n^2\nu_2(L_{e_i})\longrightarrow q(\alpha)
\quad\text{whenever }i/n\to\alpha.
\]
The function \(\pi^2/(4\alpha^2)\) strictly decreases while \(\pi^2/(1/2-\alpha)^2\) strictly increases on \((0,1/4)\). Their minimum has the **unique** maximum \(9\pi^2\) where they meet: \(\alpha=1/6\). Pick a candidate centered chord with index closest to \(n/6\); it is gap-saturating for all sufficiently large \(n\). If a sequence of eventual optimizers did not approach \(1/6\), a convergent subsequence of their normalized indices would approach another \(\alpha\), giving a strictly smaller limit of \(n^2\nu_2\) than the candidate near \(1/6\). That contradicts the necessary exact finite-size maximum property in Step 3. This proves part 3.

## Verification

The included `verify.py` constructs the actual augmented Laplacians from scratch and checks integer degree/moment identities through direct floating-point matrix evaluation, the double-versus-simple first-positive eigenvalue distinction for small and moderate orders, the shifted antisymmetric resolvent identity, short- and long-time comparisons, and the approach of the best centered second positive eigenvalue location toward one-sixth. Run `python verify.py` with NumPy. These finite checks test implementations and critical intermediate identities but **do not substitute for the all-\(n\) analytic or variational arguments**. In particular they do not enumerate infinite orders or prove a universal finite switching-time formula.

## Relationship to prior work

Ghosh and Boyd (2006) introduced and analyzed algebraic-connectivity optimization by graph edge augmentation; their edge-selection objective uses only the smallest positive eigenvalue, not the time-dependent heat trace. Summers, Shames, Lygeros and Dörfler (2014) developed edge-augmentation design for stationary network coherence, based on a Laplacian inverse trace rather than \(\operatorname{tr}(e^{-tL})\). Clark, Alomair, Bushnell and Poovendran (2013) studied finite-time leader selection, where the decision variable is a **leader subset**, not an added link.

A previously available path-shortcut theorem [4] completely classifies which single unit edges attain the maximal first positive eigenvalue \(\Lambda_n\). This known result is openly used in identifying the comparison class, and its gap-saturation statement is **not** claimed as new. Crucially it does not order the many gap-saturating paths by their *second* positive eigenvalue, identify the one-sixth asymptotic refinement, or establish the small-versus-large-time heat-trace reversal. The new contribution is the heat-spectral lexicographic refinement and its limiting free-boundary eigenvalue law. Searches of the primary and available comparison literature did not identify an equivalent pointwise heat-trace augmentation theorem, but undiscovered equivalent treatments remain possible.

## Limitations

This is a finite, undirected, unweighted, one-edge augmentation problem, not a theorem about arbitrary conductances, multiple added links, or vertex-normalized walks. The asymptotic statement describes eventual optimizers and does not give a closed formula for the best chord at each finite \(n\), a unique crossover time, or a joint scaling law with \(t/n^2\) fixed. The continuum proof uses variational compactness; the standalone script is a reproducibility aid, not a formal proof checker or independent scientific audit. Full coverage of every unpublished or unindexed work cannot be certified.

## References

[1] A. Ghosh and S. Boyd, *Growing Well-connected Graphs*, 45th IEEE Conference on Decision and Control, San Diego, December 13–15, 2006, pp. 6605–6611. Full text: https://stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf .

[2] T. Summers, I. Shames, J. Lygeros and F. Dörfler, *Topology Design for Optimal Network Coherence*, arXiv:1411.4884, first posted November 18, 2014. Full text: https://arxiv.org/pdf/1411.4884 .

[3] A. Clark, B. Alomair, L. Bushnell and R. Poovendran, *Minimizing Convergence Error in Multi-Agent Systems via Leader Selection: A Supermodular Optimization Approach*, arXiv:1306.4949, first posted June 20, 2013. Full text: https://arxiv.org/pdf/1306.4949 .

[4] *Sharp conductance and placement thresholds for path shortcuts*, published published-finding corpus record, October 18, 2026. Full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-conductance-and-placement-thresholds-for-path-shortcuts--189d704825c3/RESULT.md .
