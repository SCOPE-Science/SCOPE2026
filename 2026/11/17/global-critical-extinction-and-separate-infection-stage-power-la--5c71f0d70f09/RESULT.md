# Global critical extinction and separate infection-stage power laws in a discrete SISI model

## Finding

For a probability-admissible, doubly critical parameter slice of the four-compartment discrete SISI epidemic model, every initially infected population clears infection globally. However, the first-infection and reinfection compartments decay with **different universal powers**. Explicitly, for any \(0<b\le 1/3\) and any initial state in the population simplex with \(u_0+v_0>0\),

\[
\lim_{n\to\infty}\sqrt n\,u_n=\lim_{n\to\infty}\sqrt n\,y_n=\frac{1}{4\sqrt b},\qquad
\lim_{n\to\infty}n v_n=\frac{1}{8b},\qquad
\lim_{n\to\infty}\sqrt n\,(1-x_n)=\frac{1}{2\sqrt b}.
\]

The convergence to the disease-free fixed point is global in the initially infected portion of the closed simplex, including its boundary. Infection-free initial states follow a separate exponential law.

## Assumptions and scope

The model is the discrete-time SISI operator of Shoyimardonov (2020, Eq. (6); 2021, Eq. (2.1)) with birth/death probability \(b\), recovery probability \(\alpha=b\), susceptibility parameters \(\beta_1=\beta_2=2b\), and equal infectivities \(k_1=k_2=1\). The populations \(x,u,y,v\) are respectively never-infected susceptible, first-time infected, previously infected susceptible, and reinfected. Define \(i=u+v\). For every integer \(n\ge0\),

\[
\begin{aligned}
x_{n+1}&=x_n+b(1-x_n)-2b i_n x_n,\\
u_{n+1}&=(1-2b)u_n+2b i_nx_n,\\
y_{n+1}&=(1-b)y_n+b u_n-2b i_ny_n,\\
v_{n+1}&=(1-b)v_n+2b i_n y_n.
\end{aligned}
\]

Assume \(0<b\le1/3\) and \((x_0,u_0,y_0,v_0)\in\Delta_3:=\{(x,u,y,v)\in[0,1]^4:x+u+y+v=1\}\). The stated asymptotic law applies whenever \(u_0+v_0>0\). The parameter restrictions satisfy all simplex-preservation inequalities in the original operator. In fact every map component above is nonnegative: \(x_{n+1}=b+(1-b-2bi_n)x_n\), the coefficient of \(y_n\) is likewise \(1-b-2bi_n\), and \(1-b-2bi_n\ge1-3b\ge0\). Their sum is exactly one.

The two critical equalities are

\[
\beta_1 k_1=b+\alpha,\qquad b(b+\alpha)=\alpha\beta_2 k_2.
\]

The first makes the disease-free first-infection multiplier equal to one, and the second cancels the leading quadratic drift along the slow epidemic direction.

## Proof

**Step 1: exact slow and stable coordinates.** Introduce \(z_n=u_n+2v_n\) and \(q_n=y_n-u_n-v_n=y_n-i_n\). Direct substitution using the simplex constraint yields

\[
\boxed{\begin{aligned}
z_{n+1}&=z_n+2b i_n q_n,\\
q_{n+1}&=(1-b-2b i_n)q_n-2b v_n,\\
v_{n+1}&=(1-b)v_n+2b i_n y_n.
\end{aligned}}
\]

For an initially infected state, \(z_n>0\) for all \(n\): when \(u_n>0\), the factor \(1-2b>0\) preserves positivity; when \(v_n>0\), the factor \(1-b>0\) does so. Moreover, \(v_n>0\) eventually. Indeed if \(v_0=0\), then \(u_0>0\), \(u_1>0\), and \(y_1\ge b u_0>0\), hence \(v_2=2b i_1y_1>0\).

**Step 2: eventual monotonicity and global extinction.** Set \(a_n=1-b-2bi_n\). Since \(i_n\le1\) and \(b\le1/3\), \(0\le a_n\le1-b<1\). Once \(v_m>0\), the recurrence implies \(v_{m+j}\ge(1-b)^jv_m\). If \(q_n>0\) for all sufficiently large \(n\), then

\[
\frac{q_{n+1}}{(1-b)^{n+1}}\le\frac{q_n}{(1-b)^n}-\frac{2b v_n}{(1-b)^{n+1}}.
\]

The last term is bounded below by a fixed positive constant after time \(m\), so the right side would eventually become negative, a contradiction. Thus \(q_n\le0\) at some finite time; once nonpositive it remains nonpositive because \(a_n\ge0\) and \(v_n\ge0\). Consequently \(z_n\) is eventually positive and nonincreasing, with limit \(L\ge0\).

If \(L>0\), then \(i_n\ge z_n/2\ge L/2\), because \(z_n=i_n+v_n\le2i_n\). The telescoping sum \(z_n-z_{n+1}=2bi_n(-q_n)\) gives \(\sum_n(-q_n)<\infty\), hence \(q_n\to0\). Then \(2bv_n=a_n q_n-q_{n+1}\to0\). Thus \(i_n=z_n-v_n\to L\) and \(y_n=i_n+q_n\to L\). However, \(v_{n+1}=(1-b)v_n+2bi_ny_n\to2bL^2>0\), contradicting \(v_n\to0\). Hence \(L=0\). It follows that \(u_n,v_n,i_n\to0\). The stable recurrence \(y_{n+1}=(1-b-2bi_n)y_n+b u_n\), with \(0\le1-b-2bi_n\le1-b<1\), gives \(y_n\to0\), and therefore \(x_n\to1\).

**Step 3: a stable-response lemma.** We use the following elementary consequence of contraction. If \(s_n>0\) and \(s_{n+1}/s_n\to1\), and \(w_{n+1}=a_nw_n+f_n\), with \(a_n\to a\), \(|a|<1\), and \(f_n/s_n^p\to c\), then \(w_n/s_n^p\to c/(1-a)\) for every fixed \(p>0\). Indeed division by \(s_{n+1}^p\) gives a scalar affine recurrence whose coefficient tends to \(a\), and whose forcing tends to \(c\); its fixed-point error is eventually contracted by some uniform factor smaller than one. This argument applies to signed \(w_n\).

Since \(z_n>0\), \(z_n\to0\), \(0\le i_n/z_n\le1\), and \(q_n\to0\), the first boxed recurrence gives

\[
\frac{z_{n+1}}{z_n}=1+2b\frac{i_n}{z_n}q_n\longrightarrow1.
\]

First apply the stable-response lemma with \(s_n=z_n\), \(p=1\) to \(v_{n+1}=(1-b)v_n+2bi_ny_n\). The forcing is \(o(z_n)\), because \(i_n\le z_n\) and \(y_n\to0\), so \(v_n/z_n\to0\). Apply the same lemma to \(q_{n+1}=(1-b)q_n-2bi_nq_n-2bv_n\); both forcing terms are \(o(z_n)\), yielding \(q_n/z_n\to0\). It follows that \(i_n/z_n=1-v_n/z_n\to1\) and \(y_n/z_n=i_n/z_n+q_n/z_n\to1\).

The \(v\) recurrence now has forcing \(2bi_ny_n\sim2bz_n^2\). Applying the lemma with \(p=2\) yields

\[
\frac{v_n}{z_n^2}\longrightarrow2.
\]

The \(q\) recurrence has forcing \(-2b(i_nq_n+v_n)=-4bz_n^2+o(z_n^2)\). Again using \(p=2\) gives

\[
\frac{q_n}{z_n^2}\longrightarrow-4.
\]

Substitution in the exact slow equation produces the cubic drift

\[
z_{n+1}=z_n-8b z_n^3(1+o(1)),
\qquad z_{n+1}^{-2}-z_n^{-2}\longrightarrow16b.
\]

Cesàro averaging of the positive reciprocal-square increments yields \(z_n^{-2}/n\to16b\), or \(\sqrt n\,z_n\to1/(4\sqrt b)\). Since \(u_n=z_n-2v_n\sim z_n\), \(y_n\sim z_n\), and \(v_n\sim2z_n^2\), all four stated limits follow. In particular \(1-x_n=u_n+y_n+v_n\sim2z_n\).

**Step 4: exceptional disease-free face.** If \(u_0=v_0=0\), the infectious classes remain zero, \(y_n=(1-b)^n y_0\), and \(x_n=1-y_n\). Thus the universal algebraic law is correctly restricted to initially infected states.

## Verification

The standalone `VERIFY.py` implements symbolic checks of the map identities, the exact critical equalities and the infection-free orbit, followed by finite trajectory diagnostics at \(b=1/10\), \(b=1/4\) and \(b=1/3\), including simplex boundary initial states. Run `python VERIFY.py` with SymPy installed. The finite diagnostics test consistency of the derived coefficients; the proof above, not finite iteration, establishes the asymptotic statement.

## Relationship to prior work

Shoyimardonov (2020), §3 Eq. (6), gives the exact four-compartment map and probability-preserving constraints, and §5 formulates Conjecture 2 covering disease-free convergence at the critical equalities but without a proof for this parameter slice or any sharp compartmentwise decay. Shoyimardonov (2021), Theorem 2.4, analyzes fixed-point existence with emphasis on the positive-equilibrium side; its conditional convergence analysis does not provide the present doubly critical power laws. The result here proves a natural positive-parameter slice of the earlier global-convergence prediction and quantifies the distinct first-infection/reinfection decay scales. Its proof does not follow merely from nonhyperbolicity or positive-equilibrium nonexistence.

## Limitations

The theorem is confined to \(\alpha=b\), \(\beta_1=\beta_2=2b\), \(k_1=k_2=1\) and \(0<b\le1/3\). It does not establish the general SISI convergence conjecture, finite-population stochastic extinction statistics, or rates for nearby unequal infection parameters. The novelty assessment is based on the inspected original articles, related available source text and indexed mathematical records; unindexed equivalent results remain possible.

## References

1. S. K. Shoyimardonov, *A non-linear discrete-time dynamical system related to epidemic SISI model*, arXiv:2008.12677, first publicly submitted 2020-08-28; *Communications in Mathematics* **29** (2021), 505–525. https://arxiv.org/abs/2008.12677 ; open journal PDF: https://cm.episciences.org/9549/pdf . In particular Eq. (6), Proposition 1, Proposition 3 and Conjecture 2.
2. S. K. Shoyimardonov, *A discrete-time epidemic SISI model*, arXiv:2111.13430, first preprint submission 2021-11-26. https://arxiv.org/abs/2111.13430 . In particular Theorem 2.4 and the conditional limit analysis.
3. S. J. Schreiber, S. Huang, J. Jiang and H. Wang, *Extinction and Quasi-Stationarity for Discrete-Time, Endemic SIS and SIR Models*, *SIAM J. Applied Math.* **81** (2021), 2195–2217, https://doi.org/10.1137/20M1339015 (different stochastic epidemic models, contextual comparison only).
