# Stable-filter conjugacy fixes the \(b\)-dependence of the Zhang–Tian–Li–Wu–Cui flow
## Finding
Consider the four-dimensional flow
\[
\dot x=ky,\qquad \dot y=-x-yz,\qquad \dot z=|x|+xy-a,\qquad \dot w=x-bw,
\]
with \(a\ne0\), \(k\ne0\), and \(b>0\). The first three equations form a closed, \(b\)-independent base flow. Every compact invariant set of the four-dimensional flow is a single continuous graph over a compact invariant set of that base, and the graph projection is a flow conjugacy. Conversely every compact base invariant set has a unique compact lift.

For a bounded complete base trajectory \(u(t)=(x(t),y(t),z(t))\), its unique bounded complete lift is
\[
w(t)=\int_0^\infty e^{-bs}x(t-s)\,ds.
\]
For every compact regular ergodic invariant measure, the four-dimensional tangent Lyapunov spectrum is exactly the three-dimensional base spectrum plus \(-b\), counting multiplicity. Hence varying \(b>0\) cannot alter the number of positive Lyapunov exponents and cannot generate a genuine hyperchaos transition at fixed \(a,k\).

The introducing article reports that, with \(a=1.35\) and \(k=1\), varying \(b\) produces parameter intervals with two positive numerical Lyapunov exponents. The exact skew-product structure rules out a \(b\)-induced change in the asymptotic positive-exponent count. At its baseline \(b=1\), the article reports the four values \(0.053671\), \(-0.0049675\), \(-0.099401\), and \(-3.0757\). Any true full tangent spectrum at that parameter must contain the exact vertical exponent \(-1\), so that four-number estimate cannot be the asymptotic full spectrum.

## Assumptions and scope
The claim concerns the exact autonomous ODE above with \(a\ne0\), \(k\ne0\), and \(b>0\). Compact invariant sets are understood as sets on which the flow is defined for all positive and negative times. The Lyapunov statement concerns standard tangent exponents along compact regular ergodic invariant measures. Because of \(|x|\), the vector field is only piecewise \(C^1\); on a compact complete trajectory every crossing of \(x=0\) is transverse. Indeed, \(x=y=0\) at one time would force \(x=y=0\) for all time and \(z(t)=z(0)-at\), contradicting compactness. Thus the usual piecewise variational equation is defined along compact trajectories; continuity of the vector field makes the saltation across a transverse \(x=0\) crossing the identity.

No assertion is made that the three-dimensional base can never be hyperchaotic in a generalized sense. The proved statement is that the added stable filter coordinate cannot create a new positive exponent and that changing \(b\) alone cannot change the positive-exponent count.

## Proof
Write \(u=(x,y,z)\) and let \(\phi_t\) denote the three-dimensional base flow. The fourth equation is a scalar forced linear equation. Variation of constants gives, for any \(t\ge t_0\),
\[
w(t)=e^{-b(t-t_0)}w(t_0)+\int_{t_0}^t e^{-b(t-s)}x(s)\,ds.
\]
If the base trajectory is bounded and complete, letting \(t_0\to-\infty\) gives the bounded solution
\[
h_b(u(t))=\int_0^\infty e^{-bs}x(t-s)\,ds.
\]
The integral converges uniformly on every compact base invariant set, so \(h_b\) is continuous there.

Let \(K\) be a compact invariant set of the four-dimensional flow. If two points of \(K\) had the same base coordinate and fourth-coordinate difference \(d\ne0\), then along their common base orbit the difference would satisfy \(\dot d=-bd\), hence \(d(t)=e^{-bt}d(0)\). It would grow without bound as \(t\to-\infty\), contradicting compactness of \(K\). Therefore projection \(\pi:K\to K_0=\pi(K)\) is injective. It is a continuous bijection from compact \(K\) to Hausdorff \(K_0\), hence a homeomorphism, and it intertwines the flows. The variation-of-constants formula shows that its inverse is exactly \(u\mapsto(u,h_b(u))\). Conversely the graph of \(h_b\) over any compact base invariant set is compact and invariant. This proves the one-to-one conjugacy of compact invariant dynamics for every \(b>0\).

Away from the isolated transverse crossings of \(x=0\), the tangent equation has block lower-triangular form
\[
\begin{pmatrix}\delta u\\ \delta w\end{pmatrix}'
=
\begin{pmatrix}A(t)&0\\ (1,0,0)&-b\end{pmatrix}
\begin{pmatrix}\delta u\\ \delta w\end{pmatrix},
\]
where \(A(t)\) is the base variational matrix. Its fundamental matrix therefore has the form
\[
\Phi_b(t)=\begin{pmatrix}\Phi_0(t)&0\\ q_b(t)&e^{-bt}\end{pmatrix}.
\]
The vertical line bundle is invariant and has Lyapunov exponent exactly \(-b\); the quotient cocycle by that line bundle is exactly the base tangent cocycle. The standard invariant-subspace/quotient form of the multiplicative ergodic theorem therefore makes the multiset of full exponents equal to the base multiset together with \(-b\). Since \(-b<0\) and the base equations do not depend on \(b\), the number of positive exponents is independent of \(b\).

## Verification
The accompanying `verify.py` checks symbolically, on both smooth branches \(x>0\) and \(x<0\), that the Jacobian is block lower triangular and that its characteristic polynomial factors as
\[
\det(\lambda I-J_4)=(\lambda+b)\det(\lambda I-J_3).
\]
It also checks that the first three equations contain neither \(w\) nor \(b\), and that the vertical difference equation has the exact solution \(e^{-bt}\). Executing the packaged file returns `VERIFY_OK`.

The graph and conjugacy statements are proved directly above and do not rely on numerical integration. The Lyapunov conclusion uses only the exact invariant vertical bundle, the exact quotient cocycle, and the standard multiplicative-ergodic decomposition for an invariant subbundle and its quotient.

## Relationship to prior work
Zhang, Tian, Li, Wu, and Cui introduced this four-dimensional system by adding \(w\) to a previously studied three-dimensional no-equilibrium flow. Their article explicitly gives the triangular equations, reports a baseline Lyapunov spectrum, and states that varying \(b\) yields ranges with two positive Lyapunov exponents and hence hyperchaotic behavior. The article does not derive the bounded-lift graph, a conjugacy to the base flow, or the forced exponent \(-b\).

The peer-review record asked whether the four-dimensional system could be hyperchaotic and later cautioned that numerical largest-Lyapunov methods can be erroneous in multistable systems, but it did not identify the stable-filter reduction. General multiplicative-ergodic theory for linear skew-product flows supplies the standard framework for the invariant-subspace/quotient spectrum statement; the application here is specific to the exact triangular structure of this ODE.

Statement-level searches for the article title and DOI combined with `skew product`, `linear filter`, `forced exponent`, `Lyapunov spectrum`, `hyperchaos correction`, and `erratum` found the introducing article, its peer-review record, and general skew-product literature, but no source deriving this system-specific conjugacy or the \(-b\) spectral obstruction.

## Limitations
The result classifies compact invariant dynamics and asymptotic tangent spectra; it does not claim that finite-time Lyapunov estimates cannot temporarily show two positive values. It also does not classify the compact invariant sets of the three-dimensional base or prove chaos for any parameter. The non-smooth surface \(x=0\) requires the stated transverse-crossing interpretation of the variational equation. Literature searches cannot exclude every unindexed note or unpublished derivation, so residual originality risk remains despite the direct comparison with the primary article and its public peer-review record.

## References
1. X. Zhang, Z. Tian, J. Li, X. Wu, and Z. Cui, “A Hidden Chaotic System with Multiple Attractors,” *Entropy* 23 (2021), 1341. DOI: `10.3390/e23101341`. Published 2021-10-14.
2. Public peer-review record for the same article, *Entropy* 23 (2021), 1341, DOI: `10.3390/e23101341`.
3. V.-T. Pham, C. Volos, S. Jafari, and T. Kapitaniak, “Coexistence of hidden chaotic attractors in a novel no-equilibrium system,” *Nonlinear Dynamics* 87 (2017), 2001–2010. DOI: `10.1007/s11071-016-3170-x`.
4. R. A. Johnson, K. J. Palmer, and G. R. Sell, “Ergodic Properties of Linear Dynamical Systems,” *SIAM Journal on Mathematical Analysis* 18 (1987), 1–33. DOI: `10.1137/0518001`.
