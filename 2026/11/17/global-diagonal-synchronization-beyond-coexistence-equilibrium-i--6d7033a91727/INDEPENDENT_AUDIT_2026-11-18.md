# Independent mathematical audit

## correctness

PASS

For positive 2D Ricker map, one step bounds total T=x+y by L=2 e^{h-1}; crowding loads are at most T so T_next>=T e^{h-T}, which ensures after some finite N a lower mass floor m>0. The exact log ratio update u_next=u-(1-c)T tanh(u/2)=[1-(1-c)T p(u)]u, p(u)=tanh(u/2)/u with p(0)=1/2, is strict non-expansion because 0<(1-c)T p(u)<(1-c)e^{h-1}<2 from n>=1. This bounds the entire subsequent |u| by its first bounded-iterate magnitude, so p(u)>=p(|u_1|)>0. Combining lower T=m with the upper bound produces a strict geometric multiplier q<1 after N and thus x/y->1, |x-y|->0 for every positive seed. At h=3,c=0.9, longitudinal fixed-point eigenvalue 1-h=-2 despite the sufficient contraction condition. Five distinct parameter/seed 1200-iteration checks confirmed the analytic inequality and relaxation; source checks/check.py was read. Finite checks not the all-positive proof.

## originality

PASS

Wu–Wong global fixed-point attraction does not cover the h=3 counterexample because the diagonal coexistence fixed point is longitudinally unstable. Goldar et al. 2026 and Kulakov–Neverova–Frisman 2022 study fixed point/bifurcation/multistability and synchronization patterns, not the same uniform all-seed sufficient diagonal-attraction inequality across fixed-point instability. Related planar Ricker results for intrinsic 2 cannot dominate arbitrary h>0, and no equivalent global transverse contraction criterion was found in the actual published Results search.

## value

PASS

Global attraction to the synchronization diagonal with an explicit parameter guard despite coexistence-equilibrium instability is a structural distinction between synchronized and stationary dynamics. The sharp counterexample h=3,c=0.9 makes that conceptual separation mathematically motivated even though the sufficient condition is not optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
