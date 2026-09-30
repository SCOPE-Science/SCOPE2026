# Uniform quantitative GOE Tracy-Widom rate with fixed centering 2 is false for sparse inhomogeneous Wigner matrices

## Context

The target asks whether the largest eigenvalue of a sparse inhomogeneous real Wigner matrix exhibits a uniform quantitative Tracy-Widom limit with deterministic centering exactly at 2 and scale $N^{2/3}$, uniformly over variance profiles $\sigma_{ij}^2$ with column sums 1 and $c_-/N \le \sigma_{ij}^2 \le c_+/N$, Bernoulli($p$)-masked subexponential entries, and sparsity $Np \ge N^{1/3+\delta}$. Precisely, do there exist $c(\delta,c_-,c_+)>0$ and $N_0$ such that for all $N \ge N_0$ and all in-scope profiles $\sup_s |P(N^{2/3}(\lambda_1-2)\le s)-F_1(s)| \le N^{-c}$, where $F_1$ is the GOE Tracy-Widom CDF? Either a proof via Dyson Brownian motion and profile local law with rigidity, or a disproof by one admissible profile/atom law and in-scope sequence, completely resolves the two-sided target.

## Definitions

Fix $\delta^\star=1/4$, $c_-=c_+=1$. Take homogeneous profile $\sigma_{ij}^2=1/N$ for all $i,j$ including the diagonal. Let $\xi_{ij}$ be i.i.d. Rademacher ($\pm 1$), $B_{ij}$ i.i.d. Bernoulli($p_N$) independent of $\xi$, with $p_N=N^{-5/12}$, i.e. $Np_N=N^{7/12}=N^{1/3+\delta^\star}$. For $i\le j$ set $H_{ij}=\sigma_{ij}B_{ij}\xi_{ij}/\sqrt{p_N}=(1/\sqrt{N})B_{ij}\xi_{ij}/\sqrt{p_N}$, $H_{ji}=H_{ij}$, independently on and above the diagonal, symmetrized. Then $E[H_{ij}]=0$, $E[H_{ij}^2]=1/N$. Put $q_N^2=Np_N=N^{7/12}$, $q_N=N^{7/24}$. Column sums are $N\cdot(1/N)=1$. Let $\lambda_1$ be the largest eigenvalue, $\kappa^{(4)}$ the fourth cumulant of an off-diagonal entry, $s^{(4)}=Nq_N^2\kappa^{(4)}$ the normalized cumulant, $L_N$ the upper edge of the deterministic equilibrium measure $\tilde\rho$, $Y_N=N^{2/3}(\lambda_1-L_N)$, $X_N=N^{2/3}(\lambda_1-2)=Y_N+\mu_N$ with $\mu_N=N^{2/3}(L_N-2)$.

## Result

The uniform bound $(\star)$ is FALSE. For the above admissible ensemble and sequence, $X_N=N^{2/3}(\lambda_1-2)\to +\infty$ in probability, so its limit is degenerate at $+\infty$, not $F_1$. In particular at $s=0$, $\sup_s|P(X_N\le s)-F_1(s)|\ge F_1(0)/2>0$ eventually, hence the left side does not tend to 0, let alone at rate $N^{-c}$: for every $c>0$, $\sup_s|\cdots|>N^{-c}$ eventually. This falsifies $(\star)$ for $\delta^\star=1/4$ (hence every $\delta\le 1/4$ with the same sequence). More generally for fixed $\delta\in(0,1/3)$ with $Np_N=N^{1/3+\delta}$, the same family gives $\mu_N\gtrsim N^{1/3-\delta}/4\to\infty$.

## Proof / evidence

Scope membership: exact column sums $1$, variance bounds with $c_-=c_+=1$, centered Bernoulli-masked Rademacher law on and off diagonal, $Np_N=N^{7/12}$ in scope. Moment identity: for $k\ge 3$, $E|H_{ij}|^k=N^{-k/2}p_N^{1-k/2}=1/(Nq_N^{k-2})$ for every $i,j$ including the diagonal, so Assumption 2.3 of Lee-Schnelli (arXiv:1605.08767) holds with $\phi=7/24>1/6$ (the paper states $H_{ii}=0$ can easily be dropped, and the diagonal obeys the same bound). Fourth cumulant: $E[H^4]=1/(Nq_N^2)$, $E[H^2]^2=1/N^2$, so $\kappa^{(4)}=(1-3p_N)/(Nq_N^2)$ and $s^{(4)}=1-3p_N\to 1$, in particular $s^{(4)}\ge 3/4$ eventually, on and off diagonal. Cited edge-shift theorem: Lee-Schnelli Theorems 2.9-2.10 and Eq.(2.27) give $N^{2/3}(\lambda_1-L_N)\Rightarrow F_1$ for $\phi>1/6$ and $L_N=2+s^{(4)}/q_N^2+O(q_N^{-4})$ with fixed constant. Diagonal contributes only $O(1/(Nq_N^2))$ to the self-consistent equation versus the $N^2$ off-diagonal bulk, a fraction $q_N^2/N=p_N=o(1)$ of the $q_N^{-4}$ scale, hence absorbed in the existing remainder up to a fixed constant. Thus $L_N-2\ge s^{(4)}/q_N^2-C'/q_N^4\ge 1/(4q_N^2)$ eventually, and $\mu_N\ge \frac14 N^{2/3-7/12}=\frac14 N^{1/12}\to\infty$. Tightness: $P(X_N\le s)=P(Y_N\le s-\mu_N)\to 0$ for each fixed $s$ since $Y_N\Rightarrow F_1$ is tight and $F_1$ is a continuous CDF vanishing at $-\infty$. Hence $X_N\to+\infty$ in probability. At $s=0$, $G_N(0)\to 0$ while $F_1(0)\in(0,1)$ is fixed positive (TW1 has strictly positive density on all of $\mathbb R$), so $\sup_s|G_N-F_1|\ge F_1(0)-G_N(0)\ge F_1(0)/2>0$ eventually, violating every polynomial rate. Proved here: scope, moments, cumulant, lower bound given cited expansion, divergence, tightness lemma, sup bound. Cited (not re-proved): Lee-Schnelli edge universality and expansion; TW1 continuity and full support. No conjectures, no Dyson Brownian motion needed for the negative answer.

## Limitations

The disproof uses the cited Lee-Schnelli edge expansion and edge universality rather than re-proving them, and covers fixed $\delta\in(0,1/3)$, in particular $\delta=1/4$. For $\delta\ge 1/3$ the deterministic shift is $O(1)$ and this obstruction disappears; no claim is made there. The remainder constant in $L_N$ is existential, with the lower bound valid eventually for large $N$.

## Reproducibility

The script `artifacts/check_shift.py` verifies exact column sums, scope membership, the off-diagonal and diagonal moment identities $E|H|^k=1/(Nq^{k-2})$, $s^{(4)}=1-3p_N\to 1$, the ratio $q_N^2/N=p_N\to 0$ (diagonal error absorbed), and exponents $7/24>1/6$, $2/3-7/12=1/12$. Run `python3 artifacts/check_shift.py`; it prints the $N$, $p$, $Np$, $q$, $s_4$, $\mu$ table and `ALL CHECKS PASSED`.

## References

- J. O. Lee, K. Schnelli, "Local law and Tracy-Widom limit for sparse random matrices," arXiv:1605.08767 (2016), Assumption 2.3, Theorems 2.4/2.9/2.10, Eqs.(2.27)/(2.29).
- K. Schnelli, Y. Xu, "Quantitative Tracy-Widom laws for the largest eigenvalue of generalized Wigner matrices," EJP 2023 (DOI 10.1214/23-ejp1028); Wigner quantitative rate arXiv:2102.04330.
- C. Tracy, H. Widom: TW1 continuity and full support on $\mathbb R$ (Painleve-II representation); standard.
