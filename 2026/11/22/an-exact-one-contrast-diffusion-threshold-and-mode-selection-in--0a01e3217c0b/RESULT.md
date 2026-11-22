# An exact one-contrast diffusion threshold and mode selection in a closed plankton ecosystem

## Finding

A strictly positive, mass-conserving nutrient–phytoplankton–zooplankton–detritus (NPZD) equilibrium loses spatial linear stability even if **only the phytoplankton diffusion coefficient differs** from the other three. For the rational ecological kinetics specified below, on \([0,2\pi]\) with Neumann boundaries, the threshold is exact:

\[
\text{strict spatial instability}\quad\Longleftrightarrow\quad 0<d<\frac{43}{1440}.
\]

At \(d=43/1440\), the unique neutral nonconstant mode is \(\cos(2x)\), with a simple zero growth eigenvalue. For \(d>43/1440\), all nonconstant modes have strictly negative spectral abscissa. The sharper window

\[
\frac{101}{3915}<d<\frac{43}{1440}
\]

has exactly one unstable spatial harmonic, \(\cos(2x)\), and exactly one positive real eigenvalue for that harmonic. The homogeneous equilibrium is stable at fixed total biomass throughout this parameter family. The stated threshold and mode window are not claims of nonlinear patterned equilibria or of nonlinear pattern stability.

## Assumptions and scope

Let \(N(x,t),P(x,t),Z(x,t),D(x,t)\) be nonnegative nutrient, phytoplankton, zooplankton and detritus concentrations. The system is exactly

\[
\begin{aligned}
N_t&=-\frac{2PN}{1+N}+D+N_{xx},\\
P_t&=\frac{2PN}{1+N}-\frac{ZP}{1+P}-\frac{P}{2}+dP_{xx},\\
Z_t&=\frac{ZP}{1+P}-\frac{Z}{2}+Z_{xx},\\
D_t&=\frac{P+Z}{2}-D+D_{xx}.
\end{aligned}
\]

Here \(d>0\), the spatial interval is \([0,2\pi]\), all four derivatives vanish at its endpoints, and the kinetics are the positive-parameter specialization \(\nu=2,g=\alpha=1,\lambda=\delta=1/2\) of the closed NPZD model of Xu–Campbell–Poulin [1]. Initial perturbations are taken in the standard linearized Neumann domain. The integral of \(N+P+Z+D\) is conserved. The reference constant state \(E=(1,1,1,1)\), with total integrated biomass \(8\pi\), is an exact positive equilibrium. The zero spatial mode contains one neutral direction from conservation; stability of that mode is asserted only on the hyperplane of fixed total biomass.

Positive Neumann wavenumbers are \(k_n=n/2\) for integers \(n\ge1\), and \(q_n=k_n^2=n^2/4\). The fourth *positive* Neumann mode \(n=4\) is \(\cos(2x)\).

## Proof

Direct differentiation of the four reaction terms at \(E\) gives

\[
J=\begin{pmatrix}
-1/2&-1&0&1\\
1/2&1/4&-1/2&0\\
0&1/4&0&0\\
0&1/2&1/2&-1
\end{pmatrix}.
\]

The homogeneous characteristic polynomial equals

\[
\det(sI-J)=s\left(s^3+\frac54s^2+\frac34s+\frac5{16}\right).
\]

Its cubic factor is Hurwitz because all three coefficients are positive and \((5/4)(3/4)-5/16=5/8>0\). Hence the constant state is strictly stable within the fixed-biomass homogeneous subspace.

For each \(q>0\), the spatial linearization is \(M(q,d)=J-q\operatorname{diag}(1,d,1,1)\). Write

\[
\det(sI-M(q,d))=s^4+b_3s^3+b_2s^2+b_1s+b_0.
\]

Exact determinant expansion gives

\[
\begin{aligned}
b_3&=\frac{4dq+12q+5}{4},\\
b_2&=\frac{3(4dq^2+2dq+4q^2+3q+1)}4,\\
b_1&=\frac{48dq^3+48dq^2+8dq+16q^3+12q^2+16q+5}{16},\\
b_0&=\frac q{16}\left[d(16q^3+24q^2+8q)-4q^2+4q+5\right].
\end{aligned}
\]

For every \(q,d>0\), the first three \(b\)-coefficients are positive. The remaining Routh–Hurwitz expressions are strictly positive regardless of the sign of \(b_0\):

\[
\begin{aligned}
H_2:=b_3b_2-b_1
=\frac1{16}(&48d^2q^3+24d^2q^2+144dq^3+120dq^2+34dq\\
&+128q^3+156q^2+65q+10)>0.
\end{aligned}
\]

Moreover, \(H_3:=b_3b_2b_1-b_1^2-b_3^2b_0=K(q,d)L(q,d)/128>0\), where

\[
\begin{aligned}
K(q,d)&=64dq^3+48dq^2+8dq+64q^3+32q^2+16q+5,\\
L(q,d)&=16d^2q^3+12d^2q^2+32dq^3+40dq^2+17dq\\
&\quad+16q^3+28q^2+20q+5.
\end{aligned}
\]

Both factors have positive coefficients. Thus the quartic Routh–Hurwitz criterion implies **all four eigenvalues have negative real part if and only if \(b_0>0\)**. If \(b_0<0\), continuity and the positive leading term give a positive real eigenvalue; by Descartes' rule there is precisely one positive real root, and the Routh array yields precisely one eigenvalue in the open right half-plane. If \(b_0=0\), the root \(s=0\) is simple since \(b_1>0\), while the remaining cubic is strictly Hurwitz because \(b_3b_2>b_1\).

Consequently the mode with squared wavenumber \(q\) is unstable precisely when \(d<R(q)\), where

\[
R(q)=\frac{4q^2-4q-5}{16q^3+24q^2+8q}.
\]

Differentiation and factorization give

\[
R'(q)=-\frac{8q^4-16q^3-46q^2-30q-5}{8q^2(q+1)^2(2q+1)^2}.
\]

The polynomial in its numerator has exactly one positive root (Descartes' sign rule), situated strictly between \(9/4\) and \(4\) by evaluation. Therefore \(R\) increases up to that root and decreases thereafter. For the Neumann lattice, \(R(q_n)\) is increasing through \(n=3\) and decreasing from \(n=4\) onward. The two candidates satisfy

\[
R(9/4)=\frac{25}{1287}<R(4)=\frac{43}{1440}.
\]

It follows that the unique maximizing lattice mode is \(n=4\), with threshold \(43/1440\). The second-highest lattice value occurs at \(n=5\), since \(R(25/4)=101/3915>25/1287\), proving the single-unstable-mode window. Finally, substituting \(q=4\) and \(d=1/100\) gives \(b_0=-143/20<0\), an explicit strictly positive diffusion example. For \(d=1\), all four diffusivities are identical and every nonconstant mode is stable.

## Verification

A standalone exact-symbolic checker is included as `verify.py`; install its sole dependency with `python -m pip install -r requirements.txt`, then run `python verify.py` from the extracted folder. It derives the reaction Jacobian directly from the four equations, expands every quartic coefficient, checks both positive Hurwitz factorizations, the modal-ratio derivative, all three critical lattice values, and the rational negative-determinant witness. The proof of the all-mode maximum is analytical and does not rely on a bounded numerical sweep.

## Relationship to prior work

Xu, Campbell and Poulin [1] introduced the underlying conservative four-compartment model and derived a general determinant-based sufficient test for stationary diffusion-driven instability, exhibiting three distinct transport scales in their numerical study. This finding instead fixes a rational equilibrium and varies exactly one of four diffusivities; it proves an all-modes **necessary and sufficient** threshold, rules out missed oscillatory instability by full Hurwitz factorizations, and determines an exact isolated-harmonic window on the bounded domain. The authors' earlier publicly available thesis [2] concerns the closely related NPZ/NPZD framework, but its full text was not obtained in this review; it remains a material historical-priority uncertainty. General finite-domain Turing theory and related plankton models do not by themselves give this parameter-specific sharp boundary.

## Limitations

The result is for one exact rational choice of ecological rates, a fixed interval, positive constant diagonal diffusion, and linear stability of the homogeneous equilibrium. No nonlinear branch, patterned attractor, parameter robustness radius, empirical calibration, or claim covering all NPZD kinetics follows. The candidate is algebraically implied by the model plus general spectral tools after substantial specialization; priority of its particular exact characterization cannot be certified against inaccessible or unindexed full texts, including [2].

## References

[1] X. Xu, S. A. Campbell, F. J. Poulin, *Turing Instability of a Closed Nutrient-Phytoplankton-Zooplankton-Detritus Model*, arXiv:2611.10221v1 (first released 2026-11-06), https://arxiv.org/abs/2611.10221 . Equations (1), (20)–(30) and numerical section consulted.

[2] X. Xu, *Turing Instability of a Closed Nutrient-Phytoplankton-Zooplankton Model with Nutrient Recycling*, University of Waterloo thesis (repository public availability 2025-11-19), https://hdl.handle.net/10012/22640 . Metadata and abstract consulted; full thesis inaccessible in this review.

[3] A. M. Turing, *The Chemical Basis of Morphogenesis*, Philosophical Transactions of the Royal Society B 237 (1952), 37–72. General diffusion-instability context, not an exact claim about this NPZD model.
