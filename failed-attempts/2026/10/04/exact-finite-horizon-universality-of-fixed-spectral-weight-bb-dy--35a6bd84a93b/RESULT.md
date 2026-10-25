# Exact finite-horizon universality of fixed spectral-weight BB dynamics in matched norms
## Finding

Let
\[
f(x)=\frac12x^{\mathsf T}Hx-b^{\mathsf T}x,
\qquad
H=H^{\mathsf T}\succ0,
\]
and let \(W=\omega(H)\succ0\) be any fixed positive spectral weight. The weighted delayed Rayleigh step is
\[
\alpha_W(u)=\frac{u^{\mathsf T}Wu}{u^{\mathsf T}WHu}.
\]
The choices \(W=I\) and \(W=H\) are BB1 and BB2.

On the compatible consecutive-gradient cone
\[
\Omega_{BB}(H)
=
\left\{(u,v):v=(I-\alpha H)u\text{ for some }\alpha\in[\lambda_{\max}(H)^{-1},\lambda_{\min}(H)^{-1}]\right\},
\]
write \(T_W\) for the weighted pair transition from the source.

Define the matched product norm
\[
\|(u,v)\|_{W,\times}
:=
\left(u^{\mathsf T}Wu+v^{\mathsf T}Wv\right)^{1/2}
\]
and, for every integer \(k\ge0\), the exact finite-horizon worst-case gain
\[
A_k(W)
:=
\sup_{z\in\Omega_{BB}(H)\setminus\{0\}}
\frac{\|T_W^kz\|_{W,\times}}{\|z\|_{W,\times}}.
\]
Then
\[
A_k(W)=A_k(I)
\qquad
\text{for every }k\ge0.
\]

Thus BB1, BB2, and every fixed positive spectral-weight delayed Rayleigh rule have the same complete worst-case transient-gain sequence once each rule is measured in its natural matched product norm. This is stronger than equality of their asymptotic homogeneous growth radii.

Two exact consequences are immediate. For every \(\theta\in(0,1)\), the first contraction horizon
\[
N_\theta(W)
:=
\inf\{k\ge1:A_k(W)\le\theta\}
\]
is independent of \(W\). For every \(\rho\in(0,1)\), the sharp prefactor for a uniform estimate at rate \(\rho\),
\[
C_W(\rho)
:=
\sup_{k\ge0}A_k(W)\rho^{-k},
\]
is also independent of \(W\), including whether it is finite.

The source proves, in the Euclidean product norm, only the condition-number sandwich
\[
\kappa(\mathcal S_W)^{-1}a_k(T_I)
\le
 a_k(T_W)
\le
\kappa(\mathcal S_W)a_k(T_I)
\]
and consequently a transferred \(R\)-linear bound with a factor \(\sqrt{\kappa_2(W)}\). The matched-norm identity shows that this distortion is absent after the conjugacy is made isometric. It does not claim that the Euclidean prefactor is sharp or dispensable in Euclidean coordinates.

## Assumptions and scope

The objective is a finite-dimensional strictly convex quadratic. The weight is fixed along the run and has the spectral form
\[
W=\omega(H),
\qquad
\omega(\lambda)>0
\quad
\text{for every }\lambda\in\sigma(H).
\]
Hence \(W\) commutes with \(H\), and \(W^{1/2}\) is invertible.

The state space is exactly the compatible cone used by the source. Its realization lemma states that every point of this cone is the consecutive-gradient state obtained after one admissible warm-up step. Therefore the supremum defining \(A_k(W)\) is a worst-case algorithmic transient, not a relaxation over impossible states.

The result does not compare the methods in one common Euclidean metric. It compares each rule in the norm naturally induced by its conjugating spectral weight. It also does not cover iteration-dependent weights, nonlinear objectives, or line-search variants.

## Proof

Set
\[
S=W^{1/2}
\]
and define
\[
\mathcal S_W(u,v)=(Su,Sv).
\]
Because \(S\) commutes with \(H\), the source proves that \(\mathcal S_W\) maps \(\Omega_{BB}(H)\) bijectively onto itself and that
\[
\mathcal S_WT_W=T_I\mathcal S_W.
\]
Iterating gives
\[
\mathcal S_WT_W^k=T_I^k\mathcal S_W
\qquad
(k\ge0).
\]

By definition of the matched norm,
\[
\|z\|_{W,\times}
=
\|\mathcal S_Wz\|_{\times},
\]
where \(\|\cdot\|_\times\) is the ordinary Euclidean product norm. Hence for every nonzero compatible state \(z\),
\[
\frac{\|T_W^kz\|_{W,\times}}{\|z\|_{W,\times}}
=
\frac{\|\mathcal S_WT_W^kz\|_\times}{\|\mathcal S_Wz\|_\times}
=
\frac{\|T_I^k(\mathcal S_Wz)\|_\times}{\|\mathcal S_Wz\|_\times}.
\]
Since \(\mathcal S_W\) is a bijection of the compatible cone, taking the supremum over all nonzero \(z\) gives
\[
A_k(W)=A_k(I).
\]

The identities for \(N_\theta(W)\) and \(C_W(\rho)\) follow immediately because they are functions only of the sequence \(\{A_k(W)\}_{k\ge0}\).

For BB2, the matched norm is explicitly
\[
\|(u,v)\|_{H,\times}
=
\left(u^{\mathsf T}Hu+v^{\mathsf T}Hv\right)^{1/2}.
\]
For a power weight \(W=H^\tau\), the same statement holds with \(H^\tau\) in place of \(H\).

## Verification

The proof is exact and uses only the source conjugacy and the definition of an isometric pullback norm. The critical source statements were checked in the full primary text: the compatible cone is invariant; \(\mathcal S_W\) maps it onto itself; Proposition 3.2 gives the exact conjugacy; the paper records only a condition-number sandwich for Euclidean finite-horizon gains; and Lemma 3.3 realizes every compatible state as an actual post-warm-up algorithm state.

The standalone script `artifacts/verify_matched_bb_conjugacy.py` evaluates several diagonal strictly positive quadratic models, multiple positive spectral weights, compatible starting states, and horizons. It checks step-by-step conjugacy and equality of corresponding gain ratios to floating-point tolerance. This finite replay is a consistency check only; the all-horizon theorem is proved algebraically above.

## Relationship to prior work

The primary closed-cone paper introduces the compatible pair dynamics, proves spectral conjugacy of every fixed positive spectral-weight rule to BB1, and concludes equality of homogeneous growth radii. In the Euclidean product norm it gives a two-sided finite-horizon estimate with the condition number of the conjugacy, rather than an equality of the full gain sequences. The matched-norm identity above is not stated there.

A companion paper constructs an exact endpoint Lyapunov law for BB1, BB2, and every fixed positive weighted delayed Rayleigh rule and uses it to prove \(R\)-linear convergence. It supplies another weight-uniform asymptotic mechanism but does not state horizon-by-horizon equality of worst-case transient gains.

The earlier sharp-rate paper determines the optimal asymptotic root factor and matched uniform-envelope threshold for BB1 and transfers those asymptotic conclusions to BB2 and fixed positive weighted delayed Rayleigh rules by spectral conjugacy. It does not identify an exact finite-horizon isometry or the complete transient-gain sequence in matched norms.

Targeted searches using Barzilai--Borwein, weighted delayed Rayleigh, finite-horizon gain, matched norm, transient profile, spectral conjugacy, BB1, and BB2 found no statement equivalent to \(A_k(W)=A_k(I)\) for every horizon.

## Limitations

The equality is metric-sensitive. In a common Euclidean product norm, different spectral weights can have different transient gains, and the result gives no exact formula for that difference.

The theorem is restricted to fixed positive spectral weights commuting with \(H\). It does not cover adaptive mixtures of BB rules or iteration-dependent weights.

The scientific novelty is the transient interpretation of a new conjugacy, not a new asymptotic convergence factor. Linear conjugacies become isometries under pulled-back norms in general; the substantive optimization consequence here is that the newly defined compatible BB dynamics therefore have identical sharp finite-step contraction horizons and sharp rate-prefactor profiles across the full fixed spectral-weight family.

## References

1. S. Yang, Y.-x. Yuan, *R-Linear Convergence of Barzilai--Borwein Methods on Strictly Convex Quadratics via Closed-Cone Homogeneous Dynamics*, arXiv:2609.12100v1, 2026.
2. S. Yang, Y.-x. Yuan, *Lyapunov Functions and R-Linear Convergence for Quadratic Barzilai--Borwein Dynamics*, arXiv:2609.12084v1, 2026.
3. S. Yang, Y.-X. Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai--Borwein Method in \(\mathbb R^d\) and Hilbert Spaces*, arXiv:2608.07839v1, 2026.
