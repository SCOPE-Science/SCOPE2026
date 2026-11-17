# A sharp arithmetic spectral gap for three-time weak-mixing correlations

## Finding

For each integer \(m\ge2\) and each integer \(n\ge1\), let \(T\) be an invertible weakly mixing probability-preserving transformation and let \(f\) be a real mean-zero observable with \(\|f\|_2=1\). Set \(r_j=\langle f,f\circ T^j\rangle\) and
\[
\mathcal R_{m,n}(T,f)=r_n+r_{(m-1)n}+r_{mn}.
\]
Define the nonnegative arithmetic defect
\[
\Delta_m=\frac12\min_{\theta\in[0,2\pi]}
\left|1+e^{i\theta}+e^{im\theta}\right|^2.
\]
Then the **sharp** weak-mixing inequality is
\[
\mathcal R_{m,n}(T,f)\ge-\frac32+\Delta_m,
\qquad
\inf_{T,f}\mathcal R_{m,n}(T,f)=-\frac32+\Delta_m.
\]
The infimum is never attained by a weakly mixing system, but is approached by real stationary Gaussian shifts whose spectral measures are smooth, symmetric and atomless. Exactly
\[
\Delta_m=0\quad\Longleftrightarrow\quad m\equiv2\pmod3.
\]
On the other two congruence classes there is a strictly positive defect, with the **sharp coefficient**
\[
\boxed{\Delta_m=\frac{\pi^2}{6m^2}+O(m^{-3})
\quad(m\to\infty,\ m\equiv0,1\pmod3).}
\]
The zero/nonzero congruence alone follows from the established unit-circle root classification; the quantitative asymptotic and the sharp nonattained weak-mixing formulation are the claim here.

## Assumptions and scope

The integers \(m\ge2\) and \(n\ge1\) are arbitrary, and the probability-preserving transformation is invertible and weakly mixing. The observable is real, mean zero and normalized to unit variance. The notation \(O(m^{-3})\) means that one absolute constant bounds the error for all sufficiently large integers in the indicated two residue classes. No uniformity in the observable or the transformation is needed, since the sharp constant depends only on \(m\).

## Proof

**1. Reduction to a circle minimum.** The real spectral measure \(\sigma\) of \(f\) is a symmetric probability measure on the circle, with \(r_j=\int\cos(jt)\,d\sigma(t)\). Weak mixing makes \(\sigma\) atomless. For any \(t\), elementary expansion gives
\[
3+2\bigl(\cos(nt)+\cos((m-1)nt)+\cos(mnt)\bigr)
=\left|1+e^{int}+e^{imnt}\right|^2.
\]
The claimed inequality follows by integration. The function of \(t\) on the left is nonconstant and real analytic, so its minimum set is finite; no atomless measure attains the circle minimum. Conversely, if \(\theta_*\) minimizes the trinomial modulus, choose a smooth symmetric probability measure supported on two short arcs about \(\pm\theta_*/n\). As the arcs shrink, its spectral functional converges to the circle minimum. The usual real stationary Gaussian shift with this continuous spectral measure is weakly mixing (Maruyama's theorem), and its coordinate observable has the required normalization. Thus the weak-mixing infimum equals the circle minimum for every \(n\).

**2. Exact resonance classification.** Put \(\omega=e^{2\pi i/3}\). Three complex numbers of modulus one sum to zero precisely when, after fixing the first as \(1\), the other two are \(\omega\) and \(\omega^2\) in some order. Hence \(1+e^{i\theta}+e^{im\theta}=0\) forces \(\theta\equiv\pm2\pi/3\pmod{2\pi}\) and \(m\equiv2\pmod3\). Conversely these values give a zero. Compactness gives \(\Delta_m>0\) for every nonresonant integer \(m\).

**3. Matching upper asymptotic.** Let \(m\equiv0\) or \(1\pmod3\), set \(\theta_0=2\pi/3\), and choose \(R=-2\pi/3\) in the former case and \(R=2\pi/3\) in the latter. Then \(e^{im\theta_0}e^{iR}=\omega^2\). At
\[
\theta=\theta_0+\delta,\qquad
\delta=R/m+R/(2m^2),\qquad
\eta=m\delta-R=R/(2m),
\]
one has
\[
1+e^{i\theta}+e^{im\theta}
=\omega(e^{i\delta}-1)+\omega^2(e^{i\eta}-1).
\]
Taylor expansion, using \(\operatorname{Re}(\omega\overline{\omega^2})=-1/2\), shows
\[
|1+e^{i\theta}+e^{im\theta}|^2
=\delta^2+\eta^2-\delta\eta+O(m^{-3})
=\frac{\pi^2}{3m^2}+O(m^{-3}).
\]
Thus the squared-modulus minimum has this expression as an upper bound.

**4. Matching lower asymptotic.** Take any minimizer \(\theta_m\) of the squared modulus. The preceding trial point implies
\[
|1+e^{i\theta_m}+e^{im\theta_m}|=O(m^{-1}).
\]
The reverse triangle inequality yields
\[
\left|\,|1+e^{i\theta_m}|-1\,\right|=O(m^{-1}).
\]
Because the two simple solutions of \(|1+e^{i\theta}|=1\) on the circle are \(\theta_0\equiv\pm2\pi/3\), this forces \(\theta_m=\theta_0+\delta_m\) modulo \(2\pi\) with \(\delta_m=O(m^{-1})\). The third exponential is then within \(O(m^{-1})\) of the other nontrivial cube root, so there is an integer phase lift \(R_m\) and a residual \(\eta_m=O(m^{-1})\) such that
\[
m\delta_m=R_m+\eta_m,
\qquad
R_m\in2\pi(\mathbb Z+1/3)\ \cup\ 2\pi(\mathbb Z-1/3).
\]
In particular \(|R_m|\ge2\pi/3\). Boundedness of \(m\delta_m\) shows \(R_m=O(1)\), so every relevant Taylor remainder is uniform. Let \(b_m=m\eta_m=O(1)\). The same cube-root expansion, with the signs interchanged if necessary, gives
\[
\begin{aligned}
m^2|1+e^{i\theta_m}+e^{im\theta_m}|^2
&=(m\delta_m)^2+(m\eta_m)^2-(m\delta_m)(m\eta_m)+O(m^{-1})\\
&=R_m^2+b_m^2-R_m b_m+O(m^{-1})\\
&=\frac34 R_m^2+(b_m-R_m/2)^2+O(m^{-1})\\
&\ge \frac{\pi^2}{3}-O(m^{-1}).
\end{aligned}
\]
Combining both estimates yields
\[
\min_\theta|1+e^{i\theta}+e^{im\theta}|^2
=\frac{\pi^2}{3m^2}+O(m^{-3}),
\]
which proves the asserted defect constant after dividing by two.

## Verification

The standalone script `checker.py` independently samples the algebraic identity at 867 input pairs, checks five exact resonant exponents, numerically refines 18 nonresonant global-minimum candidates through exponent \(301\), and checks approach to the infimum by explicit atomless symmetric uniform-arc spectral measures. The scaled squared moduli at \(m=300\) and \(m=301\) are respectively about \(3.294161\) and \(3.307429\), approaching \(\pi^2/3\approx3.289868\). These finite computations corroborate, but do not prove, the limit or the infimum statement. The four-step argument above is the infinite proof.

## Relationship to prior work

Dibyendu De, *Spectral Characterizations, Harmonic Analysis, and Phase Transitions in 2-Nice and k-Nice Recurrence* (first posted 2026-11-06), Theorem 5.3 supplies the general three-lag spectral setting, while Proposition 10.1 establishes the classical \(-3/2\) Fejér bound at the arithmetic-progression triple. The present result computes a sharp arithmetic **improvement of the one-time bound** for the family of triples \(\{0,n,mn\}\), including the non-arithmetic cases and their exact leading asymptotic.

Barrera, Barrera and Navarrete, *Unimodular Zeros of Selmer's Harmonic Trinomials* (first posted 2026-10-15), classify the cases in which the associated unit-circle trinomial has exact zeros; accordingly the modulo-three zero criterion is explicitly credited to established work and is not the novelty claim. Their root-classification theorem does not state the nonzero minimum's \(m^{-2}\) asymptotic coefficient or the weak-mixing extremal interpretation.

Classical papers on the minimum modulus of polynomials and minima of trigonometric polynomials may contain related general techniques. Full texts of two plausible historical sources were not accessible in this review, so an unrecognized historical implication remains a priority risk.

## Limitations

The result concerns a **single fixed three-time spectral functional**, not simultaneous negativity over an infinite recurrence set or any new characterization of \(k\)-nice recurrence. It does not give a closed form for the minimum for each individual nonresonant exponent. Its \(O(m^{-3})\) estimate is an asymptotic statement, not a finite-exponent lower bound with an explicit error coefficient. Historical-priority checks were bounded by accessible primary full text and publicly indexed search records. Independent validation has not been performed.

## References

1. Dibyendu De, *Spectral Characterizations, Harmonic Analysis, and Phase Transitions in 2-Nice and k-Nice Recurrence*, arXiv:2611.09143v1, first posted 2026-11-06. https://arxiv.org/abs/2611.09143
2. Gerardo Barrera, Waldemar Barrera and Juan Pablo Navarrete, *Unimodular Zeros of Selmer's Harmonic Trinomials*, arXiv:2610.22132v1, first posted 2026-10-15. https://arxiv.org/abs/2610.22132
3. F. W. Carroll, D. Eustice and T. Figiel, *The Minimum Modulus of Polynomials with Coefficients of Modulus One*, Journal of the London Mathematical Society (1977), doi:10.1112/jlms/s2-16.1.76. Historical full text not available for comparison.
4. S. F. Papadopoulos, *Minima of Trigonometric Polynomials*, Bulletin of the London Mathematical Society 30 (1998), 291–294, doi:10.1112/S0024609397004232. Historical full text not available for comparison.
