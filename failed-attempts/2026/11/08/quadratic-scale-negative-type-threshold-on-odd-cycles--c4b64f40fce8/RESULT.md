# Quadratic-scale negative-type threshold on odd cycles

## Finding
Let \(n\ge5\) run through odd integers and equip \(C_n=\mathbb Z/n\mathbb Z\) with its shortest-path metric
\[
d_n(a,b)=\min\{|a-b|,\,n-|a-b|\},
\]
where representatives are chosen in \(\{0,\ldots,n-1\}\). Let \(\wp_n\) be the supremum of exponents \(p\ge0\) such that, for all real coefficients \(c_a\) with \(\sum_a c_a=0\),
\[
\sum_{a,b\in C_n}c_ac_b\,d_n(a,b)^p\le0.
\]
Set
\[
F=\int_0^{2\pi}\frac{1-\cos t}{t}\,dt
 =\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)>0,
\qquad K=\frac{2\pi^2}{F}.
\]
Then
\[
\boxed{\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}n^2(\wp_n-1)=K=8.0976273568\ldots.}
\]
Equivalently, the largest exponent for which \(\exp(-t d_n^p)\) is positive definite for *every* \(t>0\) is \(1+K/n^2+o(n^{-2})\); the largest Hilbert snowflake exponent \(\alpha\) for isometric embedding of \(d_n^\alpha\) is \(1/2+K/(2n^2)+o(n^{-2})\). The crucial obstructing Fourier frequency at this scale is \(j=2\) (and its conjugate \(n-2\)).

For comparison, the ordinary four-point roundness \(\rho_n\) of the same odd cycle, as characterized by Horak--LaRose--Moore--Rooney--Rosenthal, obeys \(\rho_n-1\sim 1/(n\log2)\). Consequently
\[
\frac{\rho_n-1}{\wp_n-1}\sim\frac{n}{K\log2}.
\]
This comparison concerns *different* invariants: four-point roundness is not generalized roundness.

## Assumptions and scope
All cycles have unit edges and odd vertex counts \(n\ge5\). Define \(0^p=0\) for the distance diagonal, including at \(p=0\). The assertions are asymptotic as \(n\) traverses odd integers; they do not assert an exact finite-\(n\) formula for \(\wp_n\) or that \(j=2\) is always the first failing frequency at every finite \(n\). \(\operatorname{Ci}\) denotes the classical cosine integral, defined so that \(\gamma+\log x-\operatorname{Ci}(x)=\int_0^x(1-\cos t)\,dt/t\).

## Proof
**1. Exact unpowered spectrum.** Put \(n=2m+1\) and use characters \(\chi_j(x)=e^{2\pi ijx/n}\), \(1\le j\le m\). The nonconstant eigenvalues of the powered distance matrix are
\[
\Lambda_{j,n}(p)=2\sum_{r=1}^m r^p\cos(2\pi jr/n).
\]
They determine conditional negative definiteness by diagonalization of a real symmetric circulant matrix. Differentiating the finite geometric sum \(\sum_{r=1}^{m}z^r\) at \(z=e^{2\pi ij/n}\), using \(z^n=1\), gives
\[
\Lambda_{j,n}(1)=
\begin{cases}
-\bigl[4\cos^2(\pi j/(2n))\bigr]^{-1},&j\text{ even},\\
-\bigl[4\sin^2(\pi j/(2n))\bigr]^{-1},&j\text{ odd}.
\end{cases}
\]
In particular \(\Lambda_{j,n}(1)\le-1/4\) for every nontrivial mode. Thus every odd cycle has strict \(1\)-negative type and \(\wp_n>1\). For fixed even \(j\), the eigenvalue tends to \(-1/4\); for fixed odd \(j\), it tends to \(-\infty\).

**2. Uniform perturbation at scale \(n^{-2}\).** Fix \(T>0\), write \(p=1+t/n^2\) with \(0\le t\le T\), and define \(h(x)=x\log x\) for \(x>0\), \(h(0)=0\). Since \(r^p=n^{t/n^2}r(r/n)^{t/n^2}\), Taylor's theorem for a nonpositive argument yields, uniformly in \(j\) and bounded \(t\),
\[
n^{-t/n^2}\Lambda_{j,n}(1+t/n^2)
=\Lambda_{j,n}(1)+tB_{j,n}+O_T(n^{-2}),
\quad
B_{j,n}=\frac2n\sum_{r=1}^m h(r/n)\cos(2\pi jr/n).
\]
Indeed \(0\le e^u-1-u\le u^2/2\) for \(u\le0\), so the total remainder is bounded by \((t^2/n^4)\sum_{r=1}^m r\log^2(r/n)=O_T(n^{-2})\), because \(x\log^2 x\) is bounded on \([0,1/2]\).

For each fixed positive integer \(j\), the Riemann-sum limit is
\[
B_{j,n}\longrightarrow I_j=2\int_0^{1/2}x\log x\cos(2\pi jx)\,dx.
\]
Moreover \(h\) has bounded variation on \([0,1/2]\). Summation by parts and the geometric sum estimate \(\left|\sum_{s=1}^r e^{2\pi ijs/n}\right|\le 1/\sin(\pi j/n)\) give a constant \(C\), independent of \(n\) and \(j\), such that
\[
|B_{j,n}|\le C/j\qquad(1\le j\le(n-1)/2).
\]
Here \(\sin(\pi j/n)\ge2j/n\). This tail estimate is essential: it makes the comparison uniform over the growing set of characters.

**3. The strictly dominant scaled harmonic.** For \(j=2k\) with \(k\ge1\), two integrations by parts (or an integration using \(\int_0^a(1-\cos u)\,du/u\)) give
\[
I_{2k}=\frac{1}{8\pi^2 k^2}\int_0^{2\pi k}\frac{1-\cos u}{u}\,du
=\frac{F(2\pi k)}{8\pi^2 k^2},
\quad F(y)=\int_0^y\frac{1-\cos u}{u}\,du.
\]
In particular \(I_2=F/(8\pi^2)>0\). For every integer \(k\ge2\),
\[
F(2\pi k)\le F(2\pi)+2\log k<k^2F(2\pi),
\]
because \(F(2\pi)>1\) (integrate over \((0,\pi)\) and use \(1/t>1/\pi\)) and \(2\log k<k^2-1\). Therefore \(0<I_{2k}<I_2\) for all \(k\ge2\).

**4. All-frequency sign comparison and sharp transition.** Define \(K=(4I_2)^{-1}\). For fixed \(0\le t<K\), the scaled limit of the \(j=2\) eigenvalue is \(-1/4+tI_2<0\). Every other fixed even mode has the strictly smaller limit \(-1/4+tI_{2k}<0\). Every fixed odd mode stays negative because its unpowered eigenvalue tends to \(-\infty\) while \(B_{j,n}\) stays bounded. Finally, choose a large fixed cutoff \(J\) with \(tC/J<1/8\); the uniform estimate in Step 2 and \(\Lambda_{j,n}(1)\le-1/4\) show negativity simultaneously for all \(j\ge J\) when \(n\) is sufficiently large. Thus every nonconstant eigenvalue is negative at \(p=1+t/n^2\) for all sufficiently large odd \(n\).

If \(t>K\), Step 2 at \(j=2\) gives \(n^{-t/n^2}\Lambda_{2,n}(1+t/n^2)\to-1/4+tI_2>0\). Therefore conditional negative definiteness fails at this exponent. The negative-type exponents form an interval (powers of conditionally negative definite kernels remain conditionally negative definite for exponents in \((0,1]\)), so squeezing the supremum between these two sides proves \(n^2(\wp_n-1)\to K\). Schoenberg's positive-kernel and Hilbert embedding equivalences give the stated consequences.

**5. Four-point comparison.** The cited four-point roundness formulas are, for \(n=4k+1\), \(2(2k)^\rho=3k^\rho+(k+1)^\rho\), and for \(n=4k-1\), \(2(2k-1)^\rho=3k^\rho+(k-1)^\rho\). Dividing by \(k^\rho\) shows the defining difference is \(-1/k\) at \(\rho=1\) and its derivative tends to \(4\log2\). The unique root tends to one, whence the mean-value theorem gives \(\rho_n-1\sim 1/(4k\log2)\sim1/(n\log2)\). Dividing the two asymptotic relations yields the ratio in the Finding.

## Verification
The standalone file `check_odd_cycle.py` evaluates all nonconstant Fourier eigenvalues numerically for representative odd cycle orders, verifies the exact \(p=1\) spectral identity, identifies the first numerical sign crossing, and checks the limiting constant by independent quadrature. Run with `python3 check_odd_cycle.py`; the concluding expected message is `ODD_CYCLE_NEGATIVE_TYPE_FINITE_CHECKS_OK`. Finite checks are corroboration only. The infinite-family proof is the uniform frequency argument above; it does not depend on any numerical root finding.

## Relationship to prior work
Graovac--Jashari--Strunje calculated the unpowered distance spectrum of cycles (1985); this supplies the exact \(p=1\) baseline but not an exponent threshold. Sánchez (arXiv 2011) developed general formulas for the supremal negative type, calculated the five-cycle example and provided a nonsharp odd-cycle bound; he cited an earlier convergence-to-one result, without a quadratic rate. Horak--LaRose--Moore--Rooney--Rosenthal (2010) obtained the *four-point* roundness of cycles, a distinct larger invariant. Murugan (2011) related vertex-transitive distance matrices to negative type in general but did not derive the \(n^{-2}\) correction here. The new content is the sharp constant and all-frequency uniformity, and the resulting quantitative separation of the two roundness notions.

## Limitations
The result is an asymptotic theorem and does not identify the first failing frequency for every finite odd \(n\). The claimed priority is based on a bounded comparison and may be affected by unlocated literature on powered cycle distance spectra or negative-type gaps. Independent validation has not been performed.

## References
- A. Graovac, G. Jashari and M. Strunje, *On the distance spectrum of a cycle*, Aplikace matematiky 30 (1985), 286–290, https://doi.org/10.21136/AM.1985.104151 .
- M. Horak, E. LaRose, J. Moore, M. Rooney and H. Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), 67–91, https://msp.org/involve/2010/3-1/involve-v3-n1-p05-p.pdf .
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first posted 2011-08-02, https://arxiv.org/abs/1108.0451 .
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first posted 2011-12-23, https://arxiv.org/abs/1112.5657 .
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44 (1938), 522–536.
