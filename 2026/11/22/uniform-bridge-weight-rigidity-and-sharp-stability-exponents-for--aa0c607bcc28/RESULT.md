# Uniform bridge-weight rigidity and sharp stability exponents for near-fastest mixing on unequal clique barbells

## Finding
Let integers \(p,q\ge5\), and form \(B_{p,q}\) from two disjoint complete graphs on \(p\) and \(q\) vertices by adding exactly one edge \(uv\), where \(u\) and \(v\) are the distinguished gateways. Let \(P\) be **any** real symmetric, entrywise nonnegative, row-stochastic matrix whose off-diagonal support is contained in this graph; arbitrary asymmetry in edge weights within the graph, holding probabilities, and vanishing allowed-edge probabilities are permitted. Define the centered spectral-norm progress
\[
d(P)=1-\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{p+q}\right\|_2,
\qquad s=\frac1{p-1}+\frac1{q-1},\quad
c=P_{uv},\quad g=3-2\sqrt2,\quad c_*=\sqrt2-1.
\]
Then the following three conclusions hold simultaneously.

**Universal bottleneck and rigidity.** For every admissible \(P\),
\[
 d(P)\le s\frac{c(1-c)}{1+c}\le gs.
\]
If \(0\le\varepsilon<1\) and \(d(P)\ge(1-\varepsilon)gs\), then
\[
 |P_{uv}-c_*|\le\sqrt{2g\varepsilon},
 \qquad P_{uu}+P_{vv}\le\frac{\varepsilon}{(1-\varepsilon)g}.
\]
These estimates apply to all near-optimal feasible matrices, not only automorphism-invariant choices.

**Explicit finite-size approximation.** Denoting by \(d_{p,q}^*\) the largest possible \(d(P)\) and setting \(C=6-\sqrt2\),
\[
\boxed{\frac{gs}{1+Cs}\le d_{p,q}^*\le gs.}
\]
Consequently, without any restriction on the relative growth rates of the clique sizes, \(d_{p,q}^*/(gs)\to1\) as \(p,q\to\infty\). Every globally maximizing matrix, including potentially nonsymmetric-in-edge-orbits maximizers, satisfies
\[
 |P_{uv}-c_*|\le \sqrt{\frac{2gCs}{1+Cs}},
 \qquad P_{uu}+P_{vv}\le\frac{Cs}{g}.
\]
Thus all optimal bridge probabilities converge to the same nonzero constant and both gateway self-loop probabilities converge to zero, uniformly over all clique-size ratios.

**Sharp order of stability.** Near \(c=c_*\), an asymptotically optimal family with bridge weight \(c\) and zero gateway holding has relative progress loss of order \((c-c_*)^2\), so a square-root bound in the relative loss is unavoidable. Holding the bridge at \(c_*\) while adding a small gateway self-loop probability \(h\) on each side causes relative progress loss of first order \(h\), making a linear holding bound optimal in exponent. The assertion is asymptotic for balanced cliques with size tending to infinity and small fixed perturbations.

## Assumptions and scope
Write \(n=p-1\), \(r=q-1\); hence \(n,r\ge4\). The **bulk** on each side means all vertices except its gateway. Set
\[
 A=\sum_{i\text{ left bulk}}P_{ui},\qquad
 B=\sum_{j\text{ right bulk}}P_{vj},\qquad c=P_{uv}.
\]
The constraints give \(A+c+P_{uu}=1\) and \(B+c+P_{vv}=1\). For \(A,B,c>0\), write
\[
R=(A^{-1}+c^{-1}+B^{-1})^{-1};
\]
set \(R=0\) if any of the three conductances vanishes. All norms in this note are Euclidean operator norms. If \(P\) is reducible or periodic, the progress can be zero; the stated inequalities remain valid.

## Proof
**Step 1: a sharp, symmetry-free bottleneck bound.** For a real test vector taking respective values \(U,a,b,V\) on left bulk, left gateway, right gateway, right bulk, its Laplacian energy is exactly
\[
 z^{\mathsf T}(I-P)z=A(U-a)^2+c(a-b)^2+B(b-V)^2.
\]
All edges inside either bulk disappear from this energy. For fixed \(U,V\), minimization over \(a,b\) gives \(R(U-V)^2\), by adding the three edge resistances in series. The centered weighted variance of this vector is at least the bulk-only variance \(nr(U-V)^2/(n+r)\). The min–max principle therefore bounds the smallest nonzero Laplacian eigenvalue by \(R(1/n+1/r)\). Since \(d(P)\) is no greater than the Laplacian gap, this proves \(d(P)\le Rs\) (including the zero-conductance case by taking an appropriate limiting vector).

As \(A,B\le1-c\),
\[
 R\le f(c):=\left(\frac2{1-c}+\frac1c\right)^{-1}
 =\frac{c(1-c)}{1+c},\qquad 0\le c\le1.
\]
The identity
\[
 \boxed{\bigl(g-f(c)\bigr)(1+c)=(c-c_*)^2}
\]
shows exactly that \(f(c)\le g\), with a unique maximizer \(c_*\). This establishes the universal bound.

**Step 2: quantitative rigidity.** If \(d(P)\ge(1-\varepsilon)gs>0\), then \(R\ge(1-\varepsilon)g\), \(f(c)\ge(1-\varepsilon)g\), and the identity above gives
\[
(c-c_*)^2=(1+c)(g-f(c))\le2g\varepsilon.
\]
The gateway self-loop sum is \(H=(1-c-A)+(1-c-B)\). Since \(A,B\le1-c\le1\),
\[
 \frac1R-\frac1{f(c)}
 =\frac{1-c-A}{A(1-c)}+\frac{1-c-B}{B(1-c)}\ge H.
\]
Using \(R\ge(1-\varepsilon)g\), \(f(c)\le g\) gives
\[
H\le\frac1{(1-\varepsilon)g}-\frac1g
 =\frac{\varepsilon}{(1-\varepsilon)g}.
\]
No averaging over graph automorphisms has been used.

**Step 3: an explicit nearly optimal kernel.** Fix \(c=c_*\) and \(x=1-c_*=2-\sqrt2\). Give the bridge probability \(c\), the gateway-to-each-left-bulk edge probability \(x/n\), and the gateway-to-each-right-bulk edge probability \(x/r\). Give distinct within-left-bulk edges probability \(1/n\), distinct within-right-bulk edges probability \(1/r\), and each bulk vertex a holding probability \((1-x)/n\) or \((1-x)/r\), respectively. Give both gateways zero holding. Every row sum is exactly one, and all probabilities are nonnegative.

In the orthonormal class-indicator basis (left bulk, left gateway, right gateway, right bulk), the matrix restriction is
\[
 Q=\begin{pmatrix}
1-x/n &x/\sqrt n&0&0\\
x/\sqrt n&0&c&0\\
0&c&0&x/\sqrt r\\
0&0&x/\sqrt r&1-x/r
\end{pmatrix}.
\]
All other eigenvalues of \(P\) equal \(-x/n\) with multiplicity \(n-1\) and \(-x/r\) with multiplicity \(r-1\). To lower-bound the positive spectral gap, work instead with the four-site path with masses \(n,1,1,r\) and edge conductances \(x,c,x\). For any four values \(U,a,b,V\), let \(z_0=(nU+rV)/(n+r)\) and set
\[
 E=x(U-a)^2+c(a-b)^2+x(b-V)^2.
\]
The weighted variance \(\mathcal V=\min_t[n(U-t)^2+(a-t)^2+(b-t)^2+r(V-t)^2]\) satisfies
\[
\begin{aligned}
 \mathcal V&\le\frac{nr}{n+r}(U-V)^2
 +2[(a-U)^2+(b-V)^2]+2[(U-z_0)^2+(V-z_0)^2]\\
 &\le\left(\frac1{gs}+\frac2x+\frac2g\right)E
 \le \left(\frac1{gs}+\frac Cg\right)E,
\end{aligned}
\]
because \(E\ge g(U-V)^2\), \((U-z_0)^2+(V-z_0)^2\le(U-V)^2\), and \(C=4+2g/x=6-\sqrt2\). Thus the smallest nonzero eigenvalue of \(I-Q\) is at least \(gs/(1+Cs)\).

It remains to show that negative eigenvalues cannot be the SLEM bottleneck. Compare \(Q\) with \(Q_0=\operatorname{diag}(1,0,0,1)\) with only the central two-by-two off-diagonal entries \(c\). The eigenvalues of \(Q_0\) are \(1,1,c,-c\), and the perturbation norm is at most \(x(1/\sqrt4+1/4)=3x/4\), since \(n,r\ge4\). By Weyl's inequality, each of the two smaller eigenvalues of \(Q\) has absolute value at most \(c+3x/4<0.854\), while its second-largest eigenvalue is at least \(1-gs\ge1-g/2>0.914\). The peripheral zero-sum eigenvalues have absolute value at most \(x/4<0.147\). Hence SLEM is the **second-largest positive eigenvalue of** \(Q\). Its complement is exactly the four-site positive Laplacian gap, establishing the constructive lower bound and the finite optimal sandwich. The bounds for every global optimizer now follow from Step 2 with \(\varepsilon=Cs/(1+Cs)\).

**Step 4: sharpness of the two exponents.** Replace the bridge probability by \(c\) near \(c_*\) and assign each gateway holding probability \(h\ge0\) small enough that \(w=1-c-h>0\), replacing \(x\) above by \(w\). Retain the same bulk-complete edge and holding normalization. The four-site effective series conductance is
\[
 R(c,h)=\left(\frac2{1-c-h}+\frac1c\right)^{-1}.
\]
With balanced side sizes \(p=q=N\to\infty\), the same variational upper and lower estimates (with \(w\) replacing \(x\)) and separation of the other eigenvalues give \(d(P)/s\to R(c,h)\). At \(h=0\), the exact identity from Step 1 shows the coefficient loss \(g-R(c,0)=(c-c_*)^2/(1+c)\). At \(c=c_*\), differentiation gives \(R(c_*,h)/g=1-h+O(h^2)\). This establishes both exponents. No claim of globally sharp multiplicative constants is made for the displayed stability inequalities.

## Verification
The standalone `verify.py` evaluates the key radical identities using SymPy, constructs full stochastic matrices for 121 integer pairs of clique orders, compares the entire spectrum with the four-site quotient, checks the finite two-sided rate bound, and tests symmetry-free series-conductance bounds on 225 nonuniform random weighted examples. It also numerically checks the sharp-exponent limiting family. The script uses Python 3, NumPy and SymPy and prints `VERIFY_OK 1072` on success. The infinite-family proof does not depend on these finite tests. The public source and byte-identical verifier are embedded with this document.

## Relationship to prior work
The foundational fastest-mixing SDP of Boyd–Diaconis–Xiao (2004) establishes the objective and its convex formulation, not these quantitative universal bridge-weight and holding-rigidity estimates. Importantly, Boyd–Diaconis–Parrilo–Xiao (2009), §5.4.4, **already gives an exact all-size solution for the balanced two-clique one-bridge graph** and already identifies the limiting optimal bridge weight \(\sqrt2-1\), so those facts are **not** claimed as new. Jafarizadeh (2025), §6.3, also treats extended barbells, including unequal cliques and a single bridge, and presents optimal values/transition probabilities. We make **no novelty claim for simply finding an optimum or its leading balanced constant**. Our distinct assertion is the global, non-orbit-restricted, **quantitative inverse statement**: every feasible nearly-fastest chain must have its actual bridge entry within square-root relative error of a universal constant and must nearly eliminate both gateway holdings, with finite constants and sharp stability exponents, even for unequal communities and arbitrary internal edge probabilities. Neither inspected statement of an exact optimizer entails such a bound for all approximate solutions. The general conductance bounds of Olesker-Taylor–Zanetti (2024) give order comparisons, not this edgewise inverse stability. Related indexed results on multi-bridge partial matchings and crown-graph near-optimality concern different graphs or objectives; those deductions do not cover the single-bridge unequal-clique statement.

## Limitations
The finite quantitative optimal-progress approximation is proven for \(p,q\ge5\); the universal upper and stability bounds actually use only positive bulk sizes, but extension of the constructive estimate to smaller sizes is not claimed. Chains must be symmetric with uniform stationary distribution, and holding is permitted; arbitrary nonreversible dynamics are excluded. The asymptotics require both clique orders to diverge. This theorem does not classify the entire exact optimizer face, and prior papers already provide exact balanced optimum formulae. Claims about publication priority remain limited to the inspected sources; unindexed or inaccessible equivalent stability theorems may exist. The step-4 tightness is an exponent statement, not an exact finite-rate formula for all perturbations. No independent mathematical validation has been performed.

## References
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264; publisher PDF records first public electronic publication October 29, 2004.
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optim. 20 (2009), 792–819, §4.3 and §5.4.4, https://arxiv.org/abs/0709.0955; https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
- S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421 (first public January 2025), §6.3, https://arxiv.org/abs/2501.02421.
- S. Olesker-Taylor, L. Zanetti, *Geometric bounds on the fastest mixing Markov chain*, Probab. Theory Relat. Fields 188 (2024), 1017–1062, https://doi.org/10.1007/s00440-023-01257-x.
