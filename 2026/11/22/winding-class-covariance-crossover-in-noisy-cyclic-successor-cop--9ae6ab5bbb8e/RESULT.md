# Winding-class covariance crossover in noisy cyclic successor-copying rings

## Finding
Consider a directed cycle with \(n\ge3\) sites and \(q\ge3\) cyclic colours. Each site updates at rate one to the colour immediately preceding it along the directed cycle, advanced by one in \(\mathbb Z/q\mathbb Z\); independent uniform-colour refreshes occur at rate \(a>0\). With \(\omega=e^{2\pi i/q}\), set \(Z_j=\omega^{S_j}\) and \(C_d=\mathbb E_\pi[Z_{j+d}\overline{Z_j}]\). There is a unique stationary law \(\pi\). If \(\kappa=\operatorname{arcosh}(1+a)\), the stationary demodulated two-point function is
\[
\boxed{\omega^{-d}C_d=\frac{\sinh((n-d)\kappa)+\omega^{-n}\sinh(d\kappa)}{\sinh(n\kappa)}},\qquad 0\le d\le n.
\]
For \(n\equiv r\pmod q\), \(a=c/n^2\), \(c>0\), and \(d/n\to x\in[0,1]\), the demodulated two-point function converges to
\[
F_{r,c}(x)=\frac{\sinh((1-x)\sqrt{2c})+\omega^{-r}\sinh(x\sqrt{2c})}{\sinh\sqrt{2c}}.
\]
At the further weak-refresh boundary \(c\downarrow0\), \(F_{r,c}(x)\to(1-x)+\omega^{-r}x\). Thus a cycle length divisible by \(q\) retains unit demodulated coherence in this boundary, whereas every nonzero winding residue has a nontrivial complex, strictly subunit interior profile.

## Assumptions and scope
The graph is a simple cyclic directed ring with vertex set \(\mathbb Z/n\mathbb Z\); its predecessor of \(j\) is \(j-1\). A successor-copying event at \(j\) assigns \(S_j\leftarrow S_{j-1}+1\pmod q\), irrespective of its former colour. Refresh replaces \(S_j\) by an independent uniform colour. The rate \(a\) denotes the total refresh-clock rate, **not** the rate to each noncurrent colour. All rates are homogeneous and clocks independent. No Gibbs or reversibility assumption is made. The integers \(q\ge3\) and \(n\ge3\) are arbitrary. All correlation statements concern the unique continuous-time stationary law at \(a>0\); zero-refresh statements are iterated limits, not claims of stationary uniqueness at \(a=0\).

## Proof
At any \(a>0\), a sequence of independent refresh events can reach any colour configuration, making the finite chain irreducible. Rotation and global colour shift commute with its generator, hence the unique stationary law has those symmetries, \(\mathbb E Z_j=0\), and \(C_d\) depends only on directed separation. Also \(C_0=C_n=1\). For \(1\le d\le n-1\), only updates of the two marked sites contribute to the generator acting on \(Z_{j+d}\overline{Z_j}\). Updating the first marked site yields \(\omega C_{d-1}-C_d\), updating the second yields \(\overline\omega C_{d+1}-C_d\), and the independent refreshes together yield \(-2a C_d\). Stationarity therefore gives
\[
2(1+a)C_d=\omega C_{d-1}+\overline\omega C_{d+1}.
\]
Write \(R_d=\omega^{-d}C_d\). The recurrence becomes \(R_{d+1}-2(1+a)R_d+R_{d-1}=0\), with boundary conditions \(R_0=1\), \(R_n=\omega^{-n}\). Its characteristic roots are \(e^{\pm\kappa}\), where \(\cosh\kappa=1+a\). Solving the two-point Dirichlet problem gives exactly the displayed hyperbolic-sine formula. Because \(a>0\) implies \(\kappa>0\), the tridiagonal difference problem has a unique solution; no separate unproved assumption about a correlation ansatz is used.

For \(a=c/n^2\), \(n\kappa\to\sqrt{2c}\). On any subsequence \(n\equiv r\pmod q\), \(\omega^{-n}=\omega^{-r}\). Substituting and taking \(d/n\to x\) proves the stated scaling function. As \(c\downarrow0\), \(\sinh(ty)/\sinh y\to t\) for real \(y\downarrow0\), so \(F_{r,0}(x)=(1-x)+\omega^{-r}x\). For \(0<x<1\) and \(r\ne0\), this is a strict convex combination of two distinct unit complex numbers and has modulus strictly below one. For \(r=0\), it equals one. More generally, \(a n^2\to0\) gives the same interpolant by the small-\(n\kappa\) expansions. The natural crossover variable is \(n\kappa\), establishing the \(n^{-2}\) rate scale.

## Verification
The supplied standalone Python program `verify.py` builds the full finite-state generator independently of the correlation recurrence, solves the stationary law numerically, and compares all nonzero separations against the formula for \((n,q)=(3,3),(4,3),(5,3),(4,4),(5,4)\) at \(a=1/2\). It also checks several winding-residue scaling evaluations. These finite computations test implementation; the all-size assertion rests on the complete generator calculation and recurrence proof above.

## Relationship to prior work
Szabó and Szolnoki's cyclic-invasion Potts study (first arXiv posting 12 October 2001) studies pair invasions on a square lattice, not deterministic successor-shift imitation along a directed ring with independent refresh. Vazquez, Loscar and Baglietto study multistate imperfect copying in mean field on an all-to-all network, not a one-sided ring or its winding sectors. Carro, Toral and San Miguel treat the conventional noisy voter on networks using positive copying. General binary anti-voter and directed Ising results concern two spins, and the directed Ising equivalence does not give the \(q\ge3\) successor-shift covariance or the modular winding profile. These comparisons are about mathematical implications, not merely topic labels.

## Limitations
This is a stationary **two-point** theorem; it does not determine the entire stationary law, entropy production, or the gap/mixing time. It does not extend to symmetric-neighbor imitation, arbitrary shift distributions, inhomogeneous refresh or noncycle graphs. The \(a=0\) result is a limiting correlation profile only; the no-refresh chain may have multiple communicating classes. General dual-process methods may potentially provide another derivation, and exhaustive historical priority beyond the inspected literature is not certified.

## References
1. G. Szabó and A. Szolnoki, *A three-state cyclic voter model extended with Potts energy*, arXiv:cond-mat/0110255 (first public 2001-10-12), https://arxiv.org/abs/cond-mat/0110255.
2. F. Vazquez, E. S. Loscar and G. Baglietto, *A multi-state voter model with imperfect copying*, arXiv:1902.07253 (2019), https://arxiv.org/abs/1902.07253.
3. A. Carro, R. Toral and M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (2016), https://arxiv.org/abs/1602.06935.
4. C. Godrèche, *Dynamics of the directed Ising chain*, arXiv:1102.0141 (2011), https://arxiv.org/abs/1102.0141.
