# Bridge-price phase transition in optimal diffusion on asymmetric double stars

## Finding
Fix integers \(p\ge q\ge1\), a budget \(B>0\), and a bridge-price parameter \(s>0\). Let \(T_{p,q}\) have hubs \(U,V\), \(p\) leaves attached to \(U\), \(q\) leaves attached to \(V\), and the bridge \(UV\). Give every edge its own nonnegative conductance. Leaf edges cost one per unit of conductance and the bridge costs \(s^2\) per unit. The sum of costs is \(B\). Define the objective as the second-smallest eigenvalue of the combinatorial weighted Laplacian (continuous-time diffusion spectral gap).

Put \(N=p+q+2\) and \(s_c=(p-q)/(q+1)\). The **unique** global maximizing allocation among all independent conductance choices is:

**(I) If \(s\ge s_c\):** Put
\[
\mu=\frac{(q+1)(2+s)}{N},\qquad
C_{\rm line}=p\mu^2+(1-\mu)^2+(1+s-\mu)^2+q(2+s-\mu)^2.
\]
Every left spoke has conductance \(a=B\mu/C_{\rm line}\), every right spoke has conductance \(b=B(2+s-\mu)/C_{\rm line}\), and the bridge has conductance
\[
c=\frac{B((p+1)\mu-1)}{sC_{\rm line}}.
\]
The maximum gap is \(B/C_{\rm line}\).

**(II) If \(0<s<s_c\):** Put \(C_{\rm split}=p+s^2+q(1+s)^2\). Every left spoke has conductance \(a=B/C_{\rm split}\), every right spoke has conductance \(b=B(1+s)/C_{\rm split}\), and the bridge has conductance
\[
c=\frac{B(1+q+q/s)}{C_{\rm split}}.
\]
The maximum gap is \(B/C_{\rm split}\). This branch is possible only when \(p>q\).

The formulas agree at \(s=s_c>0\). The optimal gap has multiplicity \(p\) for \(0<s\le s_c\), and is simple for \(s>s_c\). When \(p=q\), the gap is simple for every \(s>0\). Consequently, if \(p>q\), crossing \(s_c\) separates a multiply degenerate diffusion bottleneck from a single longitudinal bottleneck. All optimal conductances are strictly positive in both regimes: **this transition is not an edge-deletion transition**.

The two denominators satisfy the exact identity
\[
C_{\rm line}-C_{\rm split}=-\frac{(p-q-(q+1)s)^2}{N}.
\]
At the transition the optimal spectral gap is continuously differentiable as a function of \(s\), but its second derivative generally jumps. The price of the single bridge is \(s^2\), so the sharp *relative bridge price* is \((p-q)^2/(q+1)^2\).

## Assumptions and scope
The graph is a finite, simple, undirected double star of diameter three (with \(p=q=1\) giving a four-vertex path). Hub/leaf labels are fixed; no symmetry of the chosen weights is assumed. The Laplacian is \(L=\sum_{\{u,v\}}w_{uv}(e_u-e_v)(e_u-e_v)^\mathsf T\), with eigenvalues \(0=\lambda_1\le\lambda_2\le\cdots\). The unconstrained variables are all \(p+q+1\) edge conductances. The formulas refer to the original budget \(\sum_{\rm spokes}w_e+s^2w_{UV}=B\). No limit case \(s=0\) is included.

## Proof
**1. Universal dual upper bound.** Let \(P=I-\mathbf1\mathbf1^\mathsf T/N\). For any positive-semidefinite matrix \(Q\) with \(Q\mathbf1=0\), the variational formula gives \(\lambda_2(L)\operatorname{tr}Q\le\operatorname{tr}(LQ)\). If \((e_u-e_v)^\mathsf TQ(e_u-e_v)\) equals the price of edge \(uv\) for every edge, then \(\operatorname{tr}(LQ)=B\), hence \(\lambda_2(L)\le B/\operatorname{tr}Q\), with no assumption of symmetric edge weights.

**2. Longitudinal certificate.** For \(s\ge s_c\), set the test vector \(x\) to \(-\mu,1-\mu,1+s-\mu,2+s-\mu\) on the left leaves, left hub, right hub, and right leaves, respectively. It is mean-zero, and its squared jumps along the three edge types are exactly \(1,s^2,1\). Thus \(Q=xx^\mathsf T\) proves \(\lambda_2(L)\le B/C_{\rm line}\). For the displayed candidate allocation, direct substitution in every vertex's Laplacian equation gives \(Lx=(B/C_{\rm line})x\). Indeed, the left-leaf equations force \(a=(B/C_{\rm line})\mu\); the right-leaf equations force \(b=(B/C_{\rm line})(2+s-\mu)\); and the left-hub equation forces \(cs=(B/C_{\rm line})((p+1)\mu-1)\). The right-hub equation follows from zero row sums and \(\mathbf1^\mathsf T x=0\). The budget follows by the energy identity \(x^\mathsf TLx=\sum_e w_e(x_u-x_v)^2=B=(B/C_{\rm line})\|x\|^2\).

**3. Split-mode certificate.** For \(0<s<s_c\), define \(h=(q+(q+1)s)/p\), so \(0<h<1\), and set \(x\) to \(-h,0,s,s+1\) on the same vertex classes. Let \(P_L\) denote the orthogonal projector onto vectors supported on the left leaves and summing to zero. Set
\[
Q=xx^\mathsf T+\frac{p}{p-1}(1-h^2)P_L.
\]
Since \(p\ge2\), this is well-defined and positive semidefinite. It annihilates constants. Every left spoke has squared \(Q\)-distance \(h^2+(1-h^2)=1\); right spokes have distance one; and the bridge has squared distance \(s^2\). Also \(\operatorname{tr}Q=p+s^2+q(s+1)^2=C_{\rm split}\). Hence the same upper bound gives \(\lambda_2(L)\le B/C_{\rm split}\). For the stated weights, \(Lx=(B/C_{\rm split})x\); the entire \((p-1)\)-dimensional left-leaf contrast subspace is an eigenspace with that eigenvalue, since its leaf-edge conductance is exactly \(B/C_{\rm split}\). The budget identity follows as in step 2.

**4. The certified eigenvalue is the spectral gap.** In either candidate, every edge weight is strictly positive. The vertex space decomposes orthogonally into left-leaf contrasts (eigenvalue \(a\), when \(p>1\)), right-leaf contrasts (eigenvalue \(b\), when \(q>1\)), and a four-dimensional class-constant subspace. On the latter, the mass-normalized quotient Laplacian is an irreducible real symmetric tridiagonal Jacobi matrix with negative nearest-neighbor off-diagonal entries; its zero eigenvector has strictly positive components. The explicit class-constant vector \(x\) is strictly increasing along the four classes and has exactly one sign change, ignoring a possible zero at the left hub. The Sturm oscillation rule for a Jacobi matrix therefore identifies its positive eigenvalue as the first positive quotient eigenvalue. In the longitudinal branch, \(a/(B/C_{\rm line})=\mu\ge1\) by \(s\ge s_c\), while \(b/(B/C_{\rm line})=2+s-\mu>1\). In the split branch, \(a/(B/C_{\rm split})=1\) and \(b/(B/C_{\rm split})=1+s>1\). Therefore no transverse eigenvalue is smaller, and both dual upper bounds are attained. The same decomposition proves the stated multiplicities, including the equality boundary.

**5. Global uniqueness.** Equality in the dual trace bound forces \((L-(B/C)P)Q=0\). In the longitudinal branch, \(Q=xx^\mathsf T\), so \(Lx=(B/C)x\). Its nonzero spoke differences determine each individual left and right conductance, and the hub equation then determines the bridge: no asymmetric optimum remains. In the split branch, the range of \(Q\) contains every left-leaf contrast, so equality forces every left spoke to have conductance \(B/C_{\rm split}\). The equation \(Lx=(B/C_{\rm split})x\) then determines every right spoke and the bridge individually. At the boundary the longitudinal uniqueness argument still applies. Hence the optimizer is unique among **all** feasible allocations.

**6. Exact transition.** Expanding the centered variance of the four class positions proves \(C_{\rm line}-C_{\rm split}=-(p-q-(q+1)s)^2/N\); at \(s=s_c\), the two displayed weight formulas coincide. The mismatch vanishes to second order, yielding first-derivative continuity of the sharp optimum as a function of \(s\). When \(p>q\), the second derivative of the value generally has a jump because the normalized cost denominators differ by a nonzero quadratic factor on opposite sides.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check all budgets, positivity of optimal weights, every vertex equation, and each edge of both dual semidefinite certificates over 848 parameter configurations with \(1\le q\le p\le13\). It also checks the algebraic square identity symbolically, checks the complete numerical Laplacian spectra and optimal-gap multiplicities, and compares 1,000 random feasible asymmetric allocations to the claimed global bound. Reproduce with `python verify.py` using Python 3, NumPy and SymPy. The numerical tests are finite corroboration; the proof above applies to all permitted integer pairs and every positive real price.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) give the general continuous-time fastest-mixing spectral-gap SDP and its geometric dual. Fiedler (1990) treats absolute algebraic connectivity of trees for a **uniform** cost per conductance. Richter and Rocha (2015) explicitly classify unpriced double brooms, so in particular the slice \(s=1\) and the existence of a leaf-imbalance transition are not asserted to be new here. The distinguished contribution is an exact all-price law, including the shifted threshold \(s_c\), the two optimal conductance allocations, the eigenvalue multiplicity transition, and uniqueness under fully independent edge weights. The existing general SDP supplies a method to obtain these results but not the present evaluated parameter-dependent formulas in the inspected material.

## Limitations
Only diameter-three double stars with uniform prices on leaf edges are classified; general trees and arbitrary collections of edge prices are not covered. The result concerns continuous-time Laplacian gap maximization, not discrete-time fastest mixing SLEM, leader-selection coherence, or spanning-tree determinant maximization. The cost-price parameter is \(s^2\), not \(s\). No claim of independence from all published work is made: historical sources beyond the inspected corpus may contain an equivalent cost-weighted double-star classification. The underlying unpriced geometric ideas and generic optimization duality are prior work.

## References
1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf. Electronic publication: 2006-11-02.
2. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106, DOI: 10.1080/03081089008817967 (full text not available in this review).
3. S. Richter and I. Rocha, *Absolute algebraic connectivity of double brooms and trees*, Discrete Applied Mathematics 201 (2016), 213–221, DOI: 10.1016/j.dam.2015.08.009. Author-hosted preprint dated 2014: https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf.
