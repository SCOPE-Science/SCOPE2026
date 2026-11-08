# Sharp fastest-mixing transition on pineapple graphs

## Finding

Let \(a,r\) be arbitrary integers with \(a\ge2\) and \(r\ge2\). Form the pineapple graph \(G_{a,r}\) by adjoining \(r\) private leaves to one distinguished vertex \(h\) of \(K_{a+1}\). For every symmetric, nonnegative, row-stochastic transition matrix \(P\) supported on the edges of \(G_{a,r}\), with arbitrary nonnegative holding probabilities, let \(\mu(P)\) be the largest modulus of an eigenvalue on the orthogonal complement of the constants. Then

\[
\min_P\mu(P)=
\begin{cases}
\displaystyle \frac{4ar-1}{4ar+a+r},&2\le r\le a,\\[3pt]
\displaystyle 1-\frac1{a+r},&r\ge a.
\end{cases}
\]

The two expressions coincide at \(r=a\). A globally optimal matrix assigns probability \(p\) to every edge from \(h\) to one of the other \(a\) clique vertices and probability \(q\) to every leaf edge, where

\[
(p,q)=
\begin{cases}
\displaystyle\left(\frac{2r+1}{4ar+a+r},\frac{2a+1}{4ar+a+r}\right),&r\le a,\\[5pt]
\displaystyle\left(\frac1{a+r},\frac1{a+r}\right),&r\ge a.
\end{cases}
\]

Each edge between two non-hub clique vertices may be assigned probability \(s=(1-p)/a\), and every holding probability is the residual row mass. The hub holding probability is zero. The displayed pair \((p,q)\) is the **unique optimal pair within the automorphism-invariant family**. We do not claim that every global optimum is invariant or that arbitrary non-invariant optimizers are unique.

The sharp change is at \(r=a\): when \(r<a\), using the clique edges improves the optimal SLEM strictly beyond the star supported on the same hub edges, while when \(r\ge a\), the optimum equals the \(a+r\)-leaf star optimum and clique-to-clique edges are not needed for the optimal value.

## Assumptions and scope

The graph has \(1+a+r\) labeled vertices: hub \(h\), core vertices \(c_1,\dots,c_a\), and leaves \(\ell_1,\dots,\ell_r\). Its allowed nonloop edges are all \(\{h,c_i\}\), all \(\{h,\ell_j\}\), and all \(\{c_i,c_j\}\) for distinct core vertices. No irreducibility restriction is imposed on competing matrices. A symmetric stochastic matrix always has the uniform stationary distribution; the SLEM is exactly \(\|P-J/(1+a+r)\|_2\). Zero edge probabilities and nonnegative diagonal entries are allowed. The group of permutations of the core vertices and of the leaves acts by automorphisms.

## Proof

**1. Global symmetry reduction.** The feasible matrices are convex. Since \(\mu(P)=\|P-J/(1+a+r)\|_2\) is convex and invariant under simultaneous permutation of rows and columns, averaging any feasible matrix over the group \(S_a\times S_r\) gives an invariant feasible matrix with no larger SLEM. Thus an invariant optimal matrix exists and solving the invariant family gives the global optimum, without asserting that all optimizers are invariant.

**2. Exact invariant spectrum.** Write \(p,q,s\) for the invariant probabilities on hub–core, hub–leaf, and core–core edges. Feasibility is
\[
p,q,s\ge0,\quad ap+rq\le1,\quad p+(a-1)s\le1.
\]
The hub has holding mass \(1-ap-rq\), each leaf has holding mass \(1-q\), and each core vertex has holding mass \(1-p-(a-1)s\). The two transverse spaces contribute the eigenvalues \(1-q\) with multiplicity \(r-1\) and \(1-p-as\) with multiplicity \(a-1\). The block constant on each of the three vertex groups contributes eigenvalues \(1\), \(1-\alpha_-\), \(1-\alpha_+\), where \(0\le\alpha_-\le\alpha_+\) solve
\[
 z^2-\bigl((a+1)p+(r+1)q\bigr)z+(a+r+1)pq=0.
\]
These statements follow directly by applying \(I-P\) to vectors constant on each group and to vectors summing to zero inside one group. In particular
\[
\mu(P)\ge\max\{1-q,\,1-\alpha_-\}.
\]
For fixed \(q\), the smaller positive eigenvalue \(\alpha_-\) cannot decrease when \(p\) increases: the symmetric normalized three-group Laplacian gains a positive-semidefinite hub–core edge form. Consequently its upper bound under \(ap+rq\le1\) is attained at \(p=(1-rq)/a\). At the boundary \(q=0\) or \(p=0\), \(\alpha_-=0\), so such matrices cannot be optimal compared with the strictly improving constructions below.

**3. A sharp discriminant bound.** Put \(N=a+r+1\), \(H=4ar+a+r\) and \(t_*=N/H\). Under the saturated hub budget, the characteristic polynomial at an arbitrary \(t\), multiplied by \(a\), is
\[
G_t(q)=-Nrq^2+\bigl[N+(r-a)t\bigr]q-(a+1)t+at^2.
\]
An exact square identity gives
\[
G_{t_*}(q)=-Nr\left(q-\frac{2a+1}{H}\right)^2.
\]
At saturation the sum of the two nonzero Laplacian eigenvalues is \(1+p+q\), so \(\alpha_+\ge(1+p+q)/2\ge1/2\). Since \(t_*<1/2\) for \(a,r\ge2\), the square identity implies \(\alpha_-\le t_*\) for every saturated choice. By monotonicity in \(p\), this also holds without saturation. Hence \(\mu(P)\ge1-t_*\) for every feasible invariant matrix.

For \(r\le a\), set \(q_*=(2a+1)/H\) and \(p_*=(2r+1)/H\); then \(ap_*+rq_*=1\), \(\alpha_-=t_*\), and \(\alpha_+=1+t_*\). Moreover, \(q_*-t_*=(a-r)/H\ge0\). Choose \(s=(1-p_*)/a\), making the core transverse eigenvalue zero. The remaining magnitudes are \(1-q_*\le1-t_*\) and \(t_*\le1-t_*\). Consequently the lower bound is attained, giving \(\mu_*=1-t_*=(4ar-1)/H\). The square identity forces \(q=q_*\) in any optimal invariant matrix, and then the strict hub-budget condition is ruled out by direct evaluation of the characteristic polynomial: lowering \(p\) below \(p_*\), while fixing \(q=q_*\), makes its value at \(t_*\) negative and hence forces \(\alpha_-<t_*\). Thus \(p=p_*\) also is necessary.

**4. Leaf-bottleneck transition.** Suppose \(r\ge a\), and put \(u=1/(a+r)\). The leaf-transverse eigenvalue gives \(\mu(P)\ge1-q\); thus a competitor with \(\mu(P)<1-u\) would require \(q>u\). At saturated budget, the preceding quadratic satisfies
\[
G_u(u)=0,\quad \frac{\partial G_u}{\partial q}(u)=a-r\le0,
\quad G_u(q)=(a-r)(q-u)-Nr(q-u)^2<0\quad(q>u).
\]
Here \(\alpha_+>u\), so \(G_u(q)<0\) implies \(\alpha_-<u\), contradicting \(\mu(P)<1-u\). Unsaturated choices only decrease \(\alpha_-\), so they do not improve the bound. Taking \(p=q=u\), \(s=(1-u)/a\) makes the nontrivial eigenvalues \(1-u\) (multiplicity \(r\)), \(-u\), and zeros (multiplicity \(a-1\)); hence \(\mu_*=1-u\). For equality in the optimum, \(q<u\) violates the leaf lower bound and \(q>u\) violates the quotient lower bound. Thus \(q=u\), and with fixed \(q=u\) a slack hub budget means \(p<u\); at \(t=u\) the characteristic polynomial equals \(r(p-u)/(a+r)<0\), forcing \(\alpha_-<u\). This proves \(p=q=u\) for every optimal invariant matrix. At \(r=a\), the two constructions and their uniqueness conditions coincide.

**5. Sharp improvement over the star.** Removing all core–core transitions leaves an \(a+r\)-leaf star whose fastest mixing value is \(1-1/(a+r)\). This also follows by the leaf-difference modes and the hub–leaf quotient or by the preceding construction with \(p=q=u\). For \(r<a\),
\[
\frac{N}{H}-\frac1{a+r}=\frac{(a-r)^2}{(a+r)H}>0,
\]
so the displayed pineapple optimum is strictly better. For \(r\ge a\), the star optimum and the pineapple optimum agree exactly, proving the cutoff.

## Verification

Run `python verify.py` with Python 3, NumPy and SymPy. The standalone script checks five exact symbolic identities, all \(121\) integer parameter pairs \(2\le a,r\le12\) by direct full-matrix eigenspectra, and \(2700\) randomly generated feasible non-invariant competitors on small instances. The exact algebraic proof, not finite testing, establishes the all-parameter theorem. Code checks are supplementary and neither assert exhaustive enumeration of real stochastic matrices nor establish publication priority.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004), Sections 1 and 7, introduced the global symmetric fastest-mixing problem, convexity, semidefinite optimization and automorphism averaging, and solved a complete bipartite example. Boyd, Diaconis, Parrilo and Xiao (2007), Sections 2–5, developed symmetry and block-reduction techniques and analyzed complete multipartite graphs, wheels, binary trees and related examples. Those general frameworks imply the existence of an invariant optimum but do not themselves state the present evaluated pineapple two-regime formula or the exact cutoff \(r=a\) in the inspected material. A published pineapple-graph curvature optimization result addresses a different invariant. The single-leaf clique case was previously evaluated elsewhere and is not claimed as new; the contribution is the entire multiple-leaf phase classification and support threshold.

## Limitations

The objective is the SLEM for a symmetric, uniform-stationary, single-step transition matrix, not total variation mixing time at a particular finite horizon, nonlinear dynamics, or nonreversible chains. Only the invariant hub-edge probabilities are proved unique. The proof does not characterize all non-invariant optimal matrices, nor claim every optimal matrix suppresses core edges when \(r\ge a\). The sources inspected establish a best-knowledge originality comparison, not a comprehensive proof of publication priority. The 2004 source has a documented electronic-publication day; earlier submission and technical-report history may predate it without an independently verified initial public day.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI 10.1137/S0036144503423264. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chains on Graphs with Symmetries* (2007), Sections 2–5. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-52.pdf
