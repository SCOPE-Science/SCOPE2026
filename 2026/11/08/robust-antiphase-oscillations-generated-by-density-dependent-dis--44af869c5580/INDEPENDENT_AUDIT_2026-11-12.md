# Independent mathematical audit

## correctness

PASS

Set q=4/5, f(z)=4z/(1+z), d(1)=1/20, d(3)=1/2 and d′(1)=d′(3)=0. Smoothstep H=3v²−2v³ on z∈[1,3] is C1, nondecreasing, 1/20≤d≤1/2<q. Independently evaluated f(1)=2,f(3)=3 and F(1,3)=(3,1), F(3,1)=(1,3). Computed exact J13 and J31 and product [[47/800,21/1600],[21/160,23/320]], strict infinity norm 13/64<1, proving local attraction analytically. On diagonal the positive equilibrium is (11/5,11/5), with symmetric λ+=5/16 and explicit profile transverse λ−=−13891/8000<−1. For any constant d0∈(0,q), positive mixing squeezes min/max between iterates of h(z)=qf(z); reciprocal recurrence w_{t+1}=5(w_t+1)/16 converges to 5/11 and proves global positive convergence. Implicit-function persistence follows from I−DF² invertibility and continuous C1 perturbations. Tested rational derivative and orbit identities independently; neither finite sample nor logged VERIFY_OK is used as universal proof.

## originality

PASS

Compared same population map assumptions and published 2024 numerical Ricker/Hassell examples; no inspected theorem deduced the exact same-patch strictly increasing BH feedback-driven locally attracting antiphase orbit paired with universal constant-migration convergence. The inaccessible 2018 article is specifically identified as bibliographic risk, not treated as a novelty proof.

## value

PASS

Constructive robust counterexample isolates a genuinely motivated mechanism: monotone, intrinsically stabilizing recruitment can exhibit sustained antiphase cycles solely through nonlinear migration, despite all constant-migration variants converging. Exact rational stability and a perturbation-open witness are reusable structural facts in patch-population dynamics; not an unsupported claim of generic oscillation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
