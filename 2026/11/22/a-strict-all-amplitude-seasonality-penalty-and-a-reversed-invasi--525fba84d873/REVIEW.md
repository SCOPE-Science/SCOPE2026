# Independent mathematical audit

## correctness

PASS

With both couplings positive, the evolution over a positive period is strictly positive and its Perron mode has positive components. Integrating each component's logarithmic derivative gives Λ>max(−a,−d). Eliminating the second component and shifting by e^((a+d)t/2) gives y''=Qy with positive Floquet exponent γ, positive y, and Q>0. Hence y' strictly increases and satisfies y'(t+T)=e^(γT)y'(t), so r=y'/y is positive and periodic. Averaging r'=Q−r² gives γ²+Var(r)=mean Q with γ=mean r. Rationalization gives the exact defect; variance zero holds exactly for constant V. For a sine, r_max≤√(Q₀+q) by the periodic extremum condition. Testing the Riccati equation against the sine and integrating by parts gives q/2 bounded above by (ω+2r_max)√(Var(r)/2), yielding the stated penalty after dividing by √Q₀+mean r≤2√Q₀. For the frozen witness, positivity and V'+V>0 follow from 1001/1000>√2/4, and the exponent of the mean lies strictly between 0 and 1/2000. In the penalty, √(Q₀+q)<9/8 and √Q₀<1001/1000 give a strict penalty exceeding 250/(169·1001); subtracting gives −330831/338338000<−9/10000. These are analytic local invasion claims, not limits on nonlinear endemic persistence. Replay the scalar reduction and exact inequalities at RESULT.md lines 31–68; the frozen RK4 checker was inspected, not executed, and is not the sign proof.

## originality

PASS

The same-day predator-cycle result is material overlap in the exact Riccati variance method, all-amplitude suppression and a reversal interval on its ecological orbit family. Its proof of the integrated identity uses no further structure of N after the mean normalization, so the underlying calculation and the qualitative suppression mechanism cannot be credited as independently new. The frozen contribution that survives comparison is treatment of arbitrary prescribed profiles together with the frequency- and amplitude-explicit nonperturbative sine penalty and a source-admissible exact sign certificate employing that bound. Neither the overlapping formula, the perturbative evidence nor the geometric-mean lower bound supplies this penalty. Same-day indexing establishes overlap, not chronology.

## value

PASS

The arithmetic mean can give the wrong sign even for a smooth prescribed seasonal profile with an admissible source. The explicit harmonic floor controls the discrepancy across finite amplitudes and frequencies and certifies the sign with exact inequalities, beyond a numerical monodromy run or qualitative continuity argument. Its use is model-specific: fixed losses, one varying coupling, and local invasion only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
