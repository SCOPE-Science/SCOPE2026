# Equality cases for Fourier bias on incomplete finite-field line pencils

## Finding

Let \(q\) be a prime power, \(2\le k\le q\), and \(S\) the union of \(k\) distinct lines through zero in \(\mathbb F_q^2\). Fix a nontrivial field additive character \(\psi\). For a nonnegative probability mass \(\mu\) supported on \(S\), define \(\widehat\mu(\xi)=\sum_x\mu(x)\psi(-\xi\cdot x)\) and minimize \(\max_{\xi\ne0}|\widehat\mu(\xi)|\). No symmetry or evenness of \(\mu\) is assumed.

* For \(q\le2k\), the minimizing probability is **unique**, not only unique among symmetric measures. It assigns \(a=(2k-q)/[q(2k-1)]\) to zero and \(b=2/[q(2k-1)]\) to each other point of \(S\).
* For \(q>2k\), every minimizer assigns zero mass to zero and has the same Fourier coefficient on every selected dual line, namely \((q-k)/[k(q-1)]\) at its nonzero frequencies. Uniqueness need not persist: a pencil of three lines over \(\mathbb F_7\) has nonsymmetric minimizers.

The turnover at \(q=2k\) is thus an equality-case constraint on arbitrary nonnegative measures, not merely on optimizers in a symmetry-reduced problem. The value of the minimax is included below to specify the equality case; no novelty is claimed for the value obtained from the homogeneous graph optimization.

## Proof

For each dual line \(D\), average \(\widehat\mu(\xi)\) over \(\xi\in D\setminus\{0\}\). If \(x\in D^\perp\) the average character value is \(1\). Otherwise the sum over all \(\xi\in D\) is zero, by a nontrivial field character sum, leaving \(-1/(q-1)\) after removing zero. Thus the exact average is \((q\mu(D^\perp)-1)/(q-1)\); this also holds for nonprime fields and characteristic two. Let \(a=\mu(0)\), and write \(t=(qa-1)/(q-1)\). For each omitted dual line the average is \(t\). The arithmetic mean of the averages on the \(k\) selected dual lines is
\[
y=\frac{1+(k-1)t}{k},
\]
because the sum of the masses of the selected primal lines is \(1+(k-1)a\). There is at least one omitted line. The Fourier bias is therefore at least \(\max\{|t|,y\}\) with \(t\in[-1/(q-1),1]\), and this bound is attained at each fixed \(a\) by taking the constant nonzero-point weight \(b=(1-a)/[k(q-1)]\). For that measure the two exact pointwise frequency levels are \(t\) and \(y\) by the same character sums.

Since \(y\ge0\) and strictly increases with \(t\), the unique minimizing \(t\) is the crossing \(-t=y\), at \(-1/(2k-1)\), when \(q\le2k\). Otherwise it is the left endpoint \(-1/(q-1)\), with value \(y=(q-k)/[k(q-1)]\). In particular every optimizer, without any symmetry assumption, must have the displayed \(a\) for \(q\le2k\) and \(a=0\) for \(q>2k\).

For the equality statement, if finitely many numbers \(z_i\) satisfy \(|z_i|\le m\) and their average is \(m\) or \(-m\), all numbers are equal to that average. This follows by taking real parts, which reach the corresponding endpoint only at \(z_i=\pm m\). For \(q\le2k\), apply this to each omitted ray with mean \(-m\), and to all nonzero selected dual frequencies together, with mean \(m=1/(2k-1)\). Every nonzero Fourier coefficient is therefore fixed, while \(\widehat\mu(0)=1\). Invertibility of the full Fourier transform proves uniqueness of the canonical mass, including at \(q=2k\). For \(q>2k\) only the selected dual averages are forced to saturate, giving the asserted pointwise values there; the nonselected averages have smaller modulus.

For the failure of uniqueness, take the horizontal axis, vertical axis and diagonal in \(\mathbb F_7^2\). Write \(g(1)=1,\ g(-1)=-1\), zero elsewhere on \(\mathbb F_7\). Define a real signed perturbation \(f\) by \(g(s)\) at \((s,0)\) and \((0,s)\), by \(-g(s)\) at \((s,s)\), and zero elsewhere. Its total mass is zero and \(\widehat f(u,v)=\widehat g(u)+\widehat g(v)-\widehat g(u+v)\), where \(\widehat g(0)=0\) and \(\widehat g(-u)=-\widehat g(u)\). It vanishes on the selected dual lines \(u=0, v=0, u+v=0\). The canonical nonzero weights equal \(1/18\) and the Fourier magnitudes on omitted lines equal \(1/6\), below the optimum \(2/9\). For any real \(0<|\varepsilon|<1/108\), adding \(\varepsilon f\) preserves nonnegativity and normalization and changes the omitted coefficients by at most \(6|\varepsilon|<1/18\). Hence these perturbed masses are also optimal and are not even.

## Relationship to prior work and scope

Translation walks \(P(x,y)=\mu(y-x)\) on the pencil graph realize the Fourier objective as the modulus of the largest nonconstant eigenvalue. Restricting to even \(\mu\) gives reversible uniform-equilibrium walks; averaging \(\mu(x)\) with \(\mu(-x)\) cannot increase the bias. The graph determined by the selected directions is strongly regular, with two nonconstant adjacency eigenvalues \(q-k\) and \(-k\). Thus the numerical optimum is also a homogeneous-edge fastest-mixing calculation on a two-class association scheme, related to the general fastest-mixing results below. The equality proof here concerns all convolution laws, including those that are not reversible, and gives an explicit loss of uniqueness despite a unique homogeneous optimum. It does not classify all nonsymmetric equality cases in the regime \(q>2k\). Fraser's finite-field direction-cover work concerns existence bounds; sharp fourth-power synthesis on the same support optimizes a different Fourier norm ratio over complex functions.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264.
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, §3, https://arxiv.org/abs/0709.0955.
3. S. Jafarizadeh, *Pareto–Optimal Design of Markov Chains on Networks Based on Association Schemes*, https://ieeexplore.ieee.org/abstract/document/11513850.
4. J. M. Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, https://doi.org/10.1112/blms.70367.
5. *Universal sharp fourth-power Fourier synthesis on finite-field line pencils*, Resultary record `87d7ea89b8bb`.
