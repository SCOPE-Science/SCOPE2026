# Exact covariance-sign phase diagram in a two-site birth–annihilation exclusion channel

## Finding

Consider the two-site continuous-time exclusion channel defined below. With equal injection and extraction rate \(t\in(0,1]\), unit rightward hopping, and equal *per-edge* facilitated-birth and pair-annihilation rate \(r\geq0\), its unique stationary connected nearest-neighbor covariance is
\[
 C(t,r)=\operatorname{Cov}(\eta_1,\eta_2)=\frac{tP_t(r)}{(r+t)^2\bigl(r^2+3rt+r+2t^2+3t\bigr)^2},
\]
where
\[
\begin{aligned}
P_t(r)={}&r^5+(4t+2)r^4+(4t^2+6t+1)r^3\\
&+(3t^2+3t)r^2+3t^2(1-t)r+t^3(1-2t).
\end{aligned}
\]
This yields a complete sign classification throughout the parameter rectangle \(0<t\leq1\), \(r\geq0\):

- If \(0<t<1/2\), then \(C(t,r)>0\) for every \(r\geq0\).
- If \(t=1/2\), then \(C(t,0)=0\) and \(C(t,r)>0\) for every \(r>0\).
- If \(1/2<t\leq1\), there is **exactly one** \(r_c(t)>0\) such that \(C(t,r)<0\) for \(0\leq r<r_c(t)\), \(C(t,r_c(t))=0\), and \(C(t,r)>0\) for \(r>r_c(t)\). The threshold is the unique positive root of \(P_t\).

The transition line emerges from \((t,r)=(1/2,0)\) with
\[
 r_c(t)=\frac23\bigl(t-\tfrac12\bigr)+O\bigl((t-\tfrac12)^2\bigr)\quad\text{as }t\downarrow\tfrac12.
\]
At maximally driven boundaries \(t=1\), the exact threshold solves
\[
 r^5+6r^4+11r^3+6r^2-1=0,
 \qquad r_c(1)=0.3148293584778\ldots.
\]
The strong-reaction covariance has the positive asymptotic \(C(t,r)=t/r+O_t(r^{-2})\).

## Assumptions and scope

The state is \(\eta=(\eta_1,\eta_2)\in\{0,1\}^2\). Empty site 1 receives particles at rate \(t\); an occupied site 2 loses its particle at rate \(t\). A particle hops \(10\to01\) at rate 1. On the unique internal bond, facilitated birth changes \(10\to11\) or \(01\to11\), each at rate \(r\), and pair annihilation changes \(11\to00\) at rate \(r\). These are the local birth and annihilation mechanisms motivated by Chatterjee–Goswami–Mukherjee (2026). Here \(r\) denotes the actual rate of each indicated bond transition, independently of any bulk rate-normalization convention. In particular, \(01\to11\) has aggregate rate \(t+r\), combining injection and birth.

This is an explicitly defined **two-site bond model**, not an assertion that a two-site system with no interior sites is the finite-size realization adopted in any particular large-lattice simulation. The theorem makes no large-size or hydrodynamic assertion.

## Proof

Order the four states as \(00,01,10,11\). The Markov generator, with row sums zero, is
\[
 Q=\begin{pmatrix}
 -t&0&t&0\\
 t&-(2t+r)&0&t+r\\
 0&1&-(1+r)&r\\
 r&0&t&-(t+r)
 \end{pmatrix}.
\]
For every \(t>0\), \(r\geq0\), the chain is irreducible, so it has a unique stationary law. Define \(D=r^2+3rt+r+2t^2+3t\) and \(Z=(r+t)D\). Solving \(Q^{\mathsf T}p=0\), \(\sum_i p_i=1\), gives
\[
\begin{aligned}
p_{00}&=\frac{r^3+2r^2t+r^2+2rt+t^2}{Z},\\
p_{01}&=\frac{t}{D},\\
p_{10}&=\frac{t(r+2t)}{D},\\
p_{11}&=\frac{t(r^2+2rt+r+t)}{Z}.
\end{aligned}
\]
One can check these without matrix inversion: stationarity of state \(01\) gives \(p_{10}=(2t+r)p_{01}\), state \(11\) gives \((r+t)p_{11}=(t+r)p_{01}+rp_{10}\), state \(00\) gives \(tp_{00}=tp_{01}+rp_{11}\), and normalization determines \(p_{01}\). All denominators are positive on the stated domain.

For two binary variables, the covariance is \(p_{11}p_{00}-p_{10}p_{01}\). Substitution and collection of powers of \(r\) gives the displayed rational expression. For \(0<t\leq1\), every nonconstant coefficient of \(P_t\) is nonnegative, and coefficients of powers \(r^2,\ldots,r^5\) are strictly positive. Consequently \(P_t\) increases strictly on \([0,\infty)\). Its constant coefficient is \(t^3(1-2t)\). For \(t\leq1/2\) the claimed signs follow immediately; for \(t>1/2\), \(P_t(0)<0\) and \(P_t(r)\to+\infty\), so continuity and strict increase imply exactly one positive root with the indicated sign pattern.

At \(r=0\), direct simplification gives \(C(t,0)=(1-2t)/(2t+3)^2\). At fixed \(t>0\), comparing leading polynomial degrees gives \(rC(t,r)\to t\). At \((t,r)=(1/2,0)\), the derivatives satisfy \(\partial_tP=-1/4\) and \(\partial_rP=3/8\), so the implicit-function theorem yields the stated slope. Substitution of \(t=1\) produces the displayed quintic; its unique positive root is approximated numerically, with uniqueness already proved.

## Verification

The standalone script `verification.py` uses exact symbolic arithmetic to verify \(Q^{\mathsf T}p=0\), normalization, covariance factorization, the zero-reaction and strong-reaction identities, the quintic specialization, and the two derivatives controlling the threshold opening. It also checks 24 rational parameter instances against the generator and stationary law. Run it with Python 3 and SymPy by executing `python verification.py` in the directory containing the files. The classification itself is proved algebraically above, not inferred from finite sampling.

## Relationship to prior work

Chatterjee, Goswami and Mukherjee, *Steady states in asymmetric exclusion processes with reactions: Fluctuations and non-mean field behaviour* (arXiv:2611.06463v1, first submitted 4 November 2026), introduce the nearest-neighbor facilitated birth and pair annihilation mechanisms in an open driven exclusion process. Their mean-field and numerical study emphasizes nearest-neighbor correlations and identifies their systematic influence on stationary densities in larger lattices. The present finding instead gives a complete exact sign phase diagram for the explicitly specified smallest active bond channel. It separates a low-boundary-rate regime with positive covariance from a high-boundary-rate regime in which the same reaction strength reverses anticorrelation into positive association.

Classical open-TASEP correlation theory (Derrida and Evans, 1993) concerns the reaction-free model. Juhász and Santen (2003) study a distinct Langmuir-type creation/annihilation process with independent single-site reservoir attachment and detachment. Known finite-state Markov stationary methods provide the algebraic foundation; the nontrivial result here is the exact positive-root classification and its boundary transition for this particular bond-reaction mechanism.

## Limitations

The theorem is finite-dimensional and does not determine correlations, phase boundaries, or finite-size scaling for chains with three or more sites. At exactly \(t=0\), irreducibility can fail; that case is excluded. The physical distinction between the per-edge transition rate \(r\) and any large-lattice convention for bulk rates is essential. Positive covariance at large \(r\) does not imply positive spatial correlations throughout a macroscopic lattice. The result does not prove universal agreement or disagreement with mean-field theory outside this specified four-state process. The priority comparison is bounded by the explicitly inspected literature; a previously unlocated equivalent finite-chain calculation remains possible.

## References

- R. Chatterjee, A. Goswami, S. Mukherjee, *Steady states in asymmetric exclusion processes with reactions: Fluctuations and non-mean field behaviour*, arXiv:2611.06463v1 (2026), https://arxiv.org/html/2611.06463v1.
- B. Derrida and M. R. Evans, *Exact correlation functions in an asymmetric exclusion model with open boundaries*, J. Phys. I France 3, 311–322 (1993), https://doi.org/10.1051/jp1:1993132.
- R. Juhász and L. Santen, *Dynamics of an exclusion process with creation and annihilation*, arXiv:cond-mat/0311208 (2003), https://arxiv.org/abs/cond-mat/0311208.
