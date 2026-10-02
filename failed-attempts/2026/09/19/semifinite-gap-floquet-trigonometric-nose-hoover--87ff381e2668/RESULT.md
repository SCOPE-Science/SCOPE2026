# Semifinite-gap parity selection for the trigonometric Nosé–Hoover central orbit

## Corrected originality boundary

The exact periodic central orbit and its normal variational equation come from Szumiński–Llibre, arXiv:2609.19958. The periodic-gauge reduction to an s=1 Whittaker–Hill equation, reciprocal transverse multipliers, and the numerical b=1/2 Floquet edge near a=1.590316803 were already recorded in the earlier accepted SCOPE result `2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19`. They are background here, not new claims.

## Surviving result

With τ=(z0-bt)/2 and α=a/(2b), the already-established reduction is

-ψ''-(4α cos 2τ+2α^2 cos 4τ)ψ = λψ,   λ=4/b^2-2α^2.

This is the s=1 Whittaker–Hill operator. The classical semifinite-gap theorem states that for s=2m+1 all even spectral gaps except the first m are closed. At s=1, m=0, so every even (periodic) gap is closed for every real α. Therefore weak-coupling instability tongues of the central orbit cannot emanate from the periodic resonances

2/|b|=2j,  equivalently |b|=1/j,  j=1,2,... .

Only anti-periodic resonances

2/|b|=2j+1,  equivalently |b|=2/(2j+1),

can open local instability tongues. In particular no linear transverse tongue emanates from (a,b)=(0,1/2).

For the principal anti-periodic resonance near b=2, put r=a/b and A=4/b^2-r^2/2. Degenerate perturbation theory for

ψ''+[A+2r cos 2τ+(r^2/2) cos 4τ]ψ=0

gives A_±=1±r-r^2/8+O(r^3). Solving for b yields

b_±(a)=2±a/2-a^2/32+O(a^3).

Inside this wedge the orbit is transversely hyperbolic, and for b-2=O(a) the positive physical-time Floquet exponent is

χ(a,b)=1/4 sqrt(a^2-4(b-2)^2)+O(a^2).

## Verification and scope

Direct integration of the original normal variational equation at small a reproduces the two trace -2 boundaries with the displayed expansion through second order. The theorem concerns linear transverse stability of the exact central orbit only; it does not prove nonlinear KAM stability, a global route to chaos, or the existence of nonlinear period-doubled branches.

## References

1. W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability*, arXiv:2609.19958 (2026).
2. A. D. Hemery and A. P. Veselov, *Whittaker-Hill equation and semifinite-gap Schrödinger operators*, arXiv:0906.1697 (2010).
3. Earlier SCOPE reduction: `2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19`.
