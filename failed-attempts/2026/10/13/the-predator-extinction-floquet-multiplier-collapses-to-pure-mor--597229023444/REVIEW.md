# Independent mathematical audit

## correctness

PASS

On the predator-free orbit the prey rises logistically from kappa*h_l/eta to h_l/eta, where kappa=1-p_1 E_l is in (0,1). Integrating the logistic reciprocal velocity gives the stated T>0 when 0<h_l<eta K; equality with eta K gives infinite time. At the event, d[eta*x+(1-eta)*y]/dt=eta*r*x*(1-x/K)>0, so the local return time is smooth under the source regularity assumptions. Parameterize the postharvest section by y; one-dimensional return is y times (1-p_2 E_l) times the exponential of the integrated per-capita predator rate. At y=0 that rate is -mu since psi(0)=0; variation of the event time affects no linear predator term because y vanishes on the orbit. The return derivative is (1-p_2 E_l) exp(-mu*T) in (0,1), also at p_2=0, proving local orbital asymptotic stability. The printed convergence ratio reduces to the same expression by integrating d(log x)/dt=r-rx/K. The independent replay /workspace/replay_2.py integrates in prey position and checks exactly exp(r*T)=4, the threshold 3/16 and rho=2/5 at p_2=1/10 (rho=3/10 for the original baseline p_2=1/5). This is a modified baseline example, not Xu–Zou's separate subthreshold run, which hits the infinite-time boundary. Theorem 2.2(1)'s reliance on boundary instability is not a proof of nonexistence of any positive cycle.

## originality

FAIL

A distinct earlier indexed Resultary finding, c010af9c1b0d, already establishes the same cancellation, the same exact multiplier, rejection of the same threshold on the same finite-cycle branch, and the identical subthreshold counterexample. The trivial p_2=0 endpoint follows immediately from that formula and its derivation; no substantive distinct remainder was presented. This is a demonstrated catalogue duplication, not a claim that the result was previously published in a journal.

## value

PASS

Scientifically, the exact multiplier corrects a qualitative stability reversal for a natural extinction cycle and names the false premise of an argument about positive cycles. It has a concrete example away from the degenerate hitting boundary. The mathematical correction is useful, but publishing this frozen result again would duplicate the earlier correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
